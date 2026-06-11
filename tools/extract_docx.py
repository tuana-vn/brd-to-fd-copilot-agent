#!/usr/bin/env python3
"""
Extract DOCX evidence for the BRD-to-FD workflow.

This extractor is intentionally conservative and formatting-aware.

It extracts:
- working/extracted/document_text.md
- working/extracted/tables.md
- working/extracted/image_inventory_raw.md
- working/extracted/formatting_inventory.md
- working/extracted/external_references.md
- working/extracted/comments.md
- working/extracted/footnotes.md
- working/extracted/visual_object_risk_scan.md
- working/extracted/images/*
- working/review/manual_visual_review.md
- output/10_extraction_summary.md

Design rules:
- Python extracts and flags evidence; it does not infer business behavior.
- Strikethrough text is preserved but marked as inactive/deprecated candidate.
- Highlighted text is preserved as formatting evidence.
- External file links such as .pptx are references, not automatic blockers.
- Ordinary DOCX drawing objects that are backed by image blips are not treated as High risk by themselves.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "v": "urn:schemas-microsoft-com:vml",
    "o": "urn:schemas-microsoft-com:office:office",
    "c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
    "dgm": "http://schemas.openxmlformats.org/drawingml/2006/diagram",
    "rels": "http://schemas.openxmlformats.org/package/2006/relationships",
}


@dataclass
class TextSegment:
    text: str
    strike: bool = False
    highlight: str | None = None
    hyperlink: str | None = None


@dataclass
class ParagraphItem:
    sec_id: str
    block_index: int
    text: str
    active_text: str
    inactive_text: str
    has_strike: bool
    has_highlight: bool
    hyperlinks: list[tuple[str, str]]
    image_rids: list[str]


@dataclass
class ImageItem:
    image_id: str
    rid: str
    docx_path: str
    output_path: str
    block_index: int
    nearby_section: str
    nearby_text: str
    candidate_caption_section: str = ""
    candidate_caption_text: str = ""
    previous_section: str = ""
    previous_text: str = ""


def qn(prefix: str, local: str) -> str:
    return f"{{{NS[prefix]}}}{local}"


def attr(element: ET.Element, prefix: str, local: str) -> str | None:
    return element.attrib.get(qn(prefix, local))


def md_escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def clean_text(value: str) -> str:
    return re.sub(r"[ \t\r\f\v]+", " ", value).strip()


def load_relationships(zf: zipfile.ZipFile, rels_path: str = "word/_rels/document.xml.rels") -> dict[str, str]:
    if rels_path not in zf.namelist():
        return {}
    root = ET.fromstring(zf.read(rels_path))
    rels: dict[str, str] = {}
    for rel in root:
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rid and target:
            rels[rid] = target
    return rels


def run_format(run: ET.Element) -> tuple[bool, str | None]:
    rpr = run.find("w:rPr", NS)
    if rpr is None:
        return False, None
    strike = rpr.find("w:strike", NS) is not None or rpr.find("w:dstrike", NS) is not None
    # w:strike w:val="false" means explicitly off.
    st = rpr.find("w:strike", NS)
    if st is not None and attr(st, "w", "val") in {"false", "0", "off"}:
        strike = False
    hi = rpr.find("w:highlight", NS)
    highlight = attr(hi, "w", "val") if hi is not None else None
    return strike, highlight


def text_from_run(run: ET.Element) -> str:
    parts: list[str] = []
    for child in run:
        if child.tag == qn("w", "t") and child.text:
            parts.append(child.text)
        elif child.tag == qn("w", "tab"):
            parts.append("\t")
        elif child.tag == qn("w", "br"):
            parts.append("\n")
    return "".join(parts)


def paragraph_segments(p: ET.Element, rels: dict[str, str]) -> tuple[list[TextSegment], list[tuple[str, str]], list[str]]:
    segs: list[TextSegment] = []
    links: list[tuple[str, str]] = []
    image_rids: list[str] = []

    def add_run(run: ET.Element, hyperlink_target: str | None = None) -> None:
        txt = text_from_run(run)
        if txt:
            strike, highlight = run_format(run)
            segs.append(TextSegment(txt, strike=strike, highlight=highlight, hyperlink=hyperlink_target))
        for blip in run.iter(qn("a", "blip")):
            rid = attr(blip, "r", "embed") or attr(blip, "r", "link")
            if rid:
                image_rids.append(rid)

    for child in p:
        if child.tag == qn("w", "r"):
            add_run(child)
        elif child.tag == qn("w", "hyperlink"):
            rid = attr(child, "r", "id")
            target = rels.get(rid or "", "")
            label_parts = []
            for run in child.findall(".//w:r", NS):
                txt = text_from_run(run)
                if txt:
                    label_parts.append(txt)
                    add_run(run, hyperlink_target=target or None)
            label = clean_text("".join(label_parts))
            if label or target:
                links.append((label, target))
        else:
            # Collect image blips that may be nested outside a simple run.
            for blip in child.iter(qn("a", "blip")):
                rid = attr(blip, "r", "embed") or attr(blip, "r", "link")
                if rid:
                    image_rids.append(rid)

    return segs, links, image_rids


def render_segments(segs: Iterable[TextSegment]) -> str:
    rendered: list[str] = []
    for seg in segs:
        txt = seg.text
        if not txt:
            continue
        if seg.strike:
            txt = f"[STRIKETHROUGH: {txt}]"
        if seg.highlight:
            txt = f"[HIGHLIGHT:{seg.highlight} {txt}]"
        if seg.hyperlink:
            txt = f"{txt} (link: {seg.hyperlink})"
        rendered.append(txt)
    return clean_text("".join(rendered))


def active_and_inactive_text(segs: Iterable[TextSegment]) -> tuple[str, str]:
    active_parts: list[str] = []
    inactive_parts: list[str] = []
    for seg in segs:
        if seg.strike:
            inactive_parts.append(seg.text)
        else:
            active_parts.append(seg.text)
    return clean_text("".join(active_parts)), clean_text("".join(inactive_parts))


def collect_paragraphs(body: ET.Element, rels: dict[str, str]) -> tuple[list[ParagraphItem], list[dict[str, str]]]:
    paragraphs: list[ParagraphItem] = []
    block_images: list[dict[str, str]] = []
    sec_count = 0
    block_index = 0

    for child in body:
        if child.tag == qn("w", "p"):
            block_index += 1
            segs, links, image_rids = paragraph_segments(child, rels)
            rendered = render_segments(segs)
            active, inactive = active_and_inactive_text(segs)
            if rendered or image_rids:
                if rendered:
                    sec_count += 1
                    sec_id = f"SEC-{sec_count:03d}"
                    paragraphs.append(
                        ParagraphItem(
                            sec_id=sec_id,
                            block_index=block_index,
                            text=rendered,
                            active_text=active,
                            inactive_text=inactive,
                            has_strike=bool(inactive),
                            has_highlight=any(s.highlight for s in segs),
                            hyperlinks=links,
                            image_rids=image_rids,
                        )
                    )
                else:
                    sec_id = f"VISUAL-BLOCK-{block_index:03d}"
                for rid in image_rids:
                    block_images.append({"rid": rid, "block_index": str(block_index), "nearby_section": sec_id, "nearby_text": active or rendered})
        elif child.tag == qn("w", "tbl"):
            block_index += 1
            # Images embedded in tables are uncommon but possible.
            for blip in child.iter(qn("a", "blip")):
                rid = attr(blip, "r", "embed") or attr(blip, "r", "link")
                if rid:
                    block_images.append({"rid": rid, "block_index": str(block_index), "nearby_section": f"TBL-BLOCK-{block_index:03d}", "nearby_text": ""})

    return paragraphs, block_images


def cell_text(cell: ET.Element, rels: dict[str, str]) -> tuple[str, str, str, bool, bool]:
    parts: list[str] = []
    active_parts: list[str] = []
    inactive_parts: list[str] = []
    has_strike = False
    has_highlight = False
    for p in cell.findall("./w:p", NS):
        segs, _, _ = paragraph_segments(p, rels)
        txt = render_segments(segs)
        active, inactive = active_and_inactive_text(segs)
        if txt:
            parts.append(txt)
        if active:
            active_parts.append(active)
        if inactive:
            inactive_parts.append(inactive)
            has_strike = True
        if any(s.highlight for s in segs):
            has_highlight = True
    return (
        clean_text(" / ".join(parts)),
        clean_text(" / ".join(active_parts)),
        clean_text(" / ".join(inactive_parts)),
        has_strike,
        has_highlight,
    )


def collect_tables(body: ET.Element, rels: dict[str, str]) -> list[dict]:
    tables: list[dict] = []
    table_count = 0
    for child in body:
        if child.tag != qn("w", "tbl"):
            continue
        table_count += 1
        table_id = f"TBL-{table_count:03d}"
        rows: list[list[str]] = []
        row_meta: list[list[dict[str, object]]] = []
        for tr in child.findall("./w:tr", NS):
            cells: list[str] = []
            metas: list[dict[str, object]] = []
            for tc in tr.findall("./w:tc", NS):
                formatted, active, inactive, has_strike, has_highlight = cell_text(tc, rels)
                cells.append(formatted)
                metas.append({
                    "active": active,
                    "inactive": inactive,
                    "has_strike": has_strike,
                    "has_highlight": has_highlight,
                })
            rows.append(cells)
            row_meta.append(metas)
        tables.append({"id": table_id, "rows": rows, "row_meta": row_meta})
    return tables


def normalize_docx_media_path(target: str) -> str:
    target = target.replace("\\", "/")
    if target.startswith("/"):
        target = target.lstrip("/")
    if target.startswith("word/"):
        return target
    return "word/" + target


def extract_images_in_document_order(zf: zipfile.ZipFile, rels: dict[str, str], block_images: list[dict[str, str]], out_dir: Path) -> list[ImageItem]:
    out_dir.mkdir(parents=True, exist_ok=True)
    image_items: list[ImageItem] = []
    used_rids: set[str] = set()

    for info in block_images:
        rid = info["rid"]
        if rid in used_rids:
            continue
        used_rids.add(rid)
        target = rels.get(rid, "")
        if not target:
            continue
        docx_path = normalize_docx_media_path(target)
        if docx_path not in zf.namelist():
            continue
        ext = Path(docx_path).suffix.lower() or ".bin"
        image_id = f"IMG-{len(image_items) + 1:03d}"
        out_name = f"{image_id}{ext}"
        out_path = out_dir / out_name
        out_path.write_bytes(zf.read(docx_path))
        image_items.append(
            ImageItem(
                image_id=image_id,
                rid=rid,
                docx_path=docx_path,
                output_path=str(out_path.as_posix()),
                block_index=int(info.get("block_index", "0") or 0),
                nearby_section=info.get("nearby_section", ""),
                nearby_text=info.get("nearby_text", ""),
            )
        )

    # Fallback: copy any media not referenced from body order.
    copied_paths = {item.docx_path for item in image_items}
    for name in sorted(n for n in zf.namelist() if n.startswith("word/media/")):
        if name in copied_paths:
            continue
        ext = Path(name).suffix.lower() or ".bin"
        image_id = f"IMG-{len(image_items) + 1:03d}"
        out_path = out_dir / f"{image_id}{ext}"
        out_path.write_bytes(zf.read(name))
        image_items.append(
            ImageItem(
                image_id=image_id,
                rid="",
                docx_path=name,
                output_path=str(out_path.as_posix()),
                block_index=0,
                nearby_section="",
                nearby_text="",
            )
        )
    return image_items


def count_tag(root: ET.Element, namespace_prefix: str, local: str) -> int:
    return sum(1 for _ in root.iter(qn(namespace_prefix, local)))


def visual_risk_scan(zf: zipfile.ZipFile, root: ET.Element, image_count: int) -> dict[str, object]:
    drawing = count_tag(root, "w", "drawing")
    inline = count_tag(root, "wp", "inline")
    anchor = count_tag(root, "wp", "anchor")
    pict = count_tag(root, "w", "pict")
    word_txbx = count_tag(root, "w", "txbxContent")
    v_shape = count_tag(root, "v", "shape")
    v_textbox = count_tag(root, "v", "textbox")
    chart = count_tag(root, "c", "chart")
    dgm = count_tag(root, "dgm", "relIds")
    ole = count_tag(root, "o", "OLEObject")
    blips = count_tag(root, "a", "blip")
    non_image_visual = pict + word_txbx + v_shape + v_textbox + chart + dgm + ole
    missing_blip_images = max(0, blips - image_count)

    if non_image_visual > 0 or missing_blip_images > 0:
        level = "High"
    elif blips > 0:
        level = "Medium"
    else:
        level = "Low"

    return {
        "risk_level": level,
        "drawing_objects": drawing,
        "inline_drawing_objects": inline,
        "anchored_drawing_objects": anchor,
        "legacy_pict_objects": pict,
        "word_textbox_objects": word_txbx,
        "vml_shape_objects": v_shape,
        "vml_textbox_objects": v_textbox,
        "chart_objects": chart,
        "smartart_diagram_objects": dgm,
        "ole_embedded_objects": ole,
        "image_blip_references": blips,
        "extracted_images": image_count,
        "missing_blip_images": missing_blip_images,
        "comments_part_present": "word/comments.xml" in zf.namelist(),
        "footnotes_part_present": "word/footnotes.xml" in zf.namelist(),
        "endnotes_part_present": "word/endnotes.xml" in zf.namelist(),
    }


def extract_comments(zf: zipfile.ZipFile) -> list[tuple[str, str, str]]:
    if "word/comments.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("word/comments.xml"))
    comments = []
    for cmt in root.findall(".//w:comment", NS):
        cid = attr(cmt, "w", "id") or ""
        author = attr(cmt, "w", "author") or ""
        texts = []
        for t in cmt.iter(qn("w", "t")):
            if t.text:
                texts.append(t.text)
        comments.append((cid, author, clean_text("".join(texts))))
    return comments


def extract_notes(zf: zipfile.ZipFile, part: str, tag: str) -> list[tuple[str, str]]:
    path = f"word/{part}.xml"
    if path not in zf.namelist():
        return []
    root = ET.fromstring(zf.read(path))
    notes = []
    for note in root.findall(f".//w:{tag}", NS):
        nid = attr(note, "w", "id") or ""
        texts = []
        for t in note.iter(qn("w", "t")):
            if t.text:
                texts.append(t.text)
        txt = clean_text("".join(texts))
        if txt:
            notes.append((nid, txt))
    return notes


def is_external_file_reference_only(text: str) -> bool:
    return bool(re.fullmatch(r"[\w\-一-龥ぁ-んァ-ンー]+(?:_図)?\.(?:pptx|xlsx|docx|pdf|vsdx)", text.strip(), flags=re.IGNORECASE))


def is_strict_figure_caption(text: str) -> bool:
    t = text.strip()
    if is_external_file_reference_only(t):
        return False
    # Real captions in this BRD begin with 図 and usually include a figure number.
    return bool(re.match(r"^図\s*\d", t))


def figure_caption_candidates(paragraphs: list[ParagraphItem]) -> list[ParagraphItem]:
    return [p for p in paragraphs if is_strict_figure_caption(p.active_text)]


def clean_caption_for_display(text: str) -> str:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    lines = [ln for ln in lines if not is_external_file_reference_only(ln)]
    return clean_text(" ".join(lines))


def enrich_image_caption_candidates(images: list[ImageItem], paragraphs: list[ParagraphItem]) -> None:
    # Map each image to the nearest strict figure caption by document block order.
    # In Word documents, captions may appear immediately before OR after the image.
    # This is a best-effort navigation hint for step 20, not a business interpretation.
    sorted_paras = sorted([p for p in paragraphs if p.active_text], key=lambda x: x.block_index)
    caps = [p for p in sorted_paras if is_strict_figure_caption(p.active_text)]
    for img in images:
        prev = [p for p in sorted_paras if p.block_index < img.block_index]
        if prev:
            # Prefer the nearest non-external-reference text as context.
            for cand in reversed(prev):
                if not is_external_file_reference_only(cand.active_text):
                    img.previous_section = cand.sec_id
                    img.previous_text = cand.active_text
                    break

        if caps:
            nearest = min(caps, key=lambda p: abs(p.block_index - img.block_index))
            # Only auto-suggest caption when it is local to the image.
            if abs(nearest.block_index - img.block_index) <= 3:
                img.candidate_caption_section = nearest.sec_id
                img.candidate_caption_text = clean_caption_for_display(nearest.active_text)
            else:
                # Fallback to the last preceding caption; lower confidence but still useful for navigation.
                prev_caps = [p for p in caps if p.block_index < img.block_index]
                if prev_caps:
                    cap = prev_caps[-1]
                    img.candidate_caption_section = cap.sec_id
                    img.candidate_caption_text = clean_caption_for_display(cap.active_text)

def external_references(paragraphs: list[ParagraphItem]) -> list[tuple[str, str, str]]:
    refs: list[tuple[str, str, str]] = []
    exts = (".pptx", ".xlsx", ".docx", ".pdf", ".vsdx")
    for p in paragraphs:
        # Hyperlinks
        for label, target in p.hyperlinks:
            if label.lower().endswith(exts) or target.lower().endswith(exts):
                refs.append((p.sec_id, label or target, target))
        # Plain text file names
        for match in re.findall(r"[\w\-一-龥ぁ-んァ-ンー]+(?:_図)?\.(?:pptx|xlsx|docx|pdf|vsdx)", p.active_text, re.IGNORECASE):
            refs.append((p.sec_id, match, ""))
    # Deduplicate by source + label. Prefer a row that has a hyperlink target.
    by_key: dict[tuple[str, str], tuple[str, str, str]] = {}
    for sec, label, target in refs:
        key = (sec, label)
        if key not in by_key or (not by_key[key][2] and target):
            by_key[key] = (sec, label, target)
    return list(by_key.values())


def write_document_text(path: Path, docx_path: Path, paragraphs: list[ParagraphItem]) -> None:
    lines = ["# Extracted Document Text", "", f"Source file: `{docx_path.as_posix()}`", ""]
    lines += [
        "Formatting markers:",
        "- `[STRIKETHROUGH: ...]` means the text was struck through in the source and must not be treated as active behavior by default.",
        "- `[HIGHLIGHT:<color> ...]` means highlighted text in the source.",
        "",
    ]
    for p in paragraphs:
        lines.append(f"## {p.sec_id}")
        lines.append("")
        lines.append(p.text)
        if p.has_strike:
            lines.append("")
            lines.append(f"- Inactive/struck-through text: `{p.inactive_text}`")
        if p.hyperlinks:
            lines.append("")
            lines.append("- Hyperlinks:")
            for label, target in p.hyperlinks:
                lines.append(f"  - `{label}` -> `{target}`")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_tables(path: Path, docx_path: Path, tables: list[dict]) -> None:
    lines = ["# Extracted Tables", "", f"Source file: `{docx_path.as_posix()}`", ""]
    lines += [
        "Formatting markers:",
        "- `[STRIKETHROUGH: ...]` means the text was struck through in the source and must not be treated as active behavior by default.",
        "- `[HIGHLIGHT:<color> ...]` means highlighted text in the source.",
        "",
    ]
    for table in tables:
        lines.append(f"## {table['id']}")
        lines.append("")
        rows = table["rows"]
        if not rows:
            lines.append("_No readable rows extracted._")
            lines.append("")
            continue
        width = max(len(r) for r in rows)
        normalized = [r + [""] * (width - len(r)) for r in rows]
        header = [md_escape_cell(c or f"Column {i+1}") for i, c in enumerate(normalized[0])]
        lines.append("| " + " | ".join(header) + " |")
        lines.append("| " + " | ".join(["---"] * width) + " |")
        for row in normalized[1:]:
            lines.append("| " + " | ".join(md_escape_cell(c) for c in row) + " |")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_image_inventory(path: Path, docx_path: Path, images: list[ImageItem]) -> None:
    lines = ["# Raw Image Inventory", "", f"Source file: `{docx_path.as_posix()}`", ""]
    for item in images:
        lines.append(f"## {item.image_id}")
        lines.append("")
        lines.append(f"- Relationship ID: `{item.rid or 'N/A'}`")
        lines.append(f"- DOCX path: `{item.docx_path}`")
        lines.append(f"- Extracted path: `{item.output_path}`")
        lines.append(f"- Nearby section: `{item.nearby_section or 'not detected'}`")
        lines.append(f"- Nearby text: {item.nearby_text or '_not detected_'}")
        lines.append(f"- Candidate caption section: `{item.candidate_caption_section or 'not detected'}`")
        lines.append(f"- Candidate caption text: {item.candidate_caption_text or '_not detected_'}")
        lines.append(f"- Previous text section: `{item.previous_section or 'not detected'}`")
        lines.append(f"- Previous text: {item.previous_text or '_not detected_'}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_formatting_inventory(path: Path, paragraphs: list[ParagraphItem], tables: list[dict]) -> None:
    lines = ["# Formatting Inventory", ""]
    lines += [
        "Purpose: preserve formatting that may change requirement meaning.",
        "",
        "Rules:",
        "- Strikethrough text is inactive/deprecated candidate evidence, not active behavior by default.",
        "- Highlighted text may indicate review emphasis or changed text; downstream prompts must not invent meaning from highlight alone.",
        "",
        "## Paragraph formatting",
        "",
        "| Source | Formatting | Text | Active text |",
        "|---|---|---|---|",
    ]
    found = False
    for p in paragraphs:
        if p.has_strike or p.has_highlight:
            found = True
            fmt = []
            if p.has_strike:
                fmt.append("Strikethrough")
            if p.has_highlight:
                fmt.append("Highlight")
            lines.append(f"| {p.sec_id} | {', '.join(fmt)} | {md_escape_cell(p.text)} | {md_escape_cell(p.active_text)} |")
    if not found:
        lines.append("| _None detected_ |  |  |  |")

    lines += ["", "## Table-cell formatting", "", "| Table | Row | Column | Formatting | Cell text | Active text |", "|---|---:|---:|---|---|---|"]
    found = False
    for table in tables:
        for r_idx, row in enumerate(table["row_meta"], start=1):
            for c_idx, meta in enumerate(row, start=1):
                if meta["has_strike"] or meta["has_highlight"]:
                    found = True
                    fmt = []
                    if meta["has_strike"]:
                        fmt.append("Strikethrough")
                    if meta["has_highlight"]:
                        fmt.append("Highlight")
                    raw = table["rows"][r_idx - 1][c_idx - 1] if r_idx - 1 < len(table["rows"]) and c_idx - 1 < len(table["rows"][r_idx - 1]) else ""
                    lines.append(f"| {table['id']} | {r_idx} | {c_idx} | {', '.join(fmt)} | {md_escape_cell(raw)} | {md_escape_cell(str(meta['active']))} |")
    if not found:
        lines.append("| _None detected_ |  |  |  |  |  |")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_external_references(path: Path, refs: list[tuple[str, str, str]]) -> None:
    lines = ["# External References", "", "External references are not automatic blockers.", ""]
    lines += ["| Source reference | External reference | Hyperlink target | Notes |", "|---|---|---|---|"]
    if refs:
        for sec, label, target in refs:
            lines.append(f"| {sec} | `{label}` | `{target or 'N/A'}` | Review only if required to understand behavior. |")
    else:
        lines.append("| _None detected_ |  |  |  |")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_comments(path: Path, comments: list[tuple[str, str, str]]) -> None:
    lines = ["# Extracted Comments", "", "Comments may be review notes. They are not active requirements unless confirmed.", ""]
    lines += ["| Comment ID | Author | Text |", "|---|---|---|"]
    if comments:
        for cid, author, text in comments:
            lines.append(f"| {cid} | {md_escape_cell(author)} | {md_escape_cell(text)} |")
    else:
        lines.append("| _None detected_ |  |  |")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_notes(path: Path, footnotes: list[tuple[str, str]], endnotes: list[tuple[str, str]]) -> None:
    lines = ["# Extracted Footnotes and Endnotes", ""]
    lines += ["## Footnotes", "", "| ID | Text |", "|---|---|"]
    if footnotes:
        for nid, text in footnotes:
            lines.append(f"| {nid} | {md_escape_cell(text)} |")
    else:
        lines.append("| _None detected_ |  |")
    lines += ["", "## Endnotes", "", "| ID | Text |", "|---|---|"]
    if endnotes:
        for nid, text in endnotes:
            lines.append(f"| {nid} | {md_escape_cell(text)} |")
    else:
        lines.append("| _None detected_ |  |")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_visual_scan(path: Path, scan: dict[str, object]) -> None:
    lines = ["# Visual Object Risk Scan", "", f"Risk level: **{scan['risk_level']}**", ""]
    lines += ["| Item | Count / status | Notes |", "|---|---:|---|"]
    rows = [
        ("Drawing objects", "drawing_objects", "Ordinary Word drawing containers."),
        ("Inline drawing objects", "inline_drawing_objects", "Inline visual objects."),
        ("Anchored drawing objects", "anchored_drawing_objects", "Positioned visual objects."),
        ("Legacy pict objects", "legacy_pict_objects", "May not be extracted as normal images."),
        ("Word textbox objects", "word_textbox_objects", "Text inside shape/textbox may be missed."),
        ("VML shape objects", "vml_shape_objects", "Legacy shape objects may be missed."),
        ("VML textbox objects", "vml_textbox_objects", "Legacy textboxes may contain text evidence."),
        ("Chart objects", "chart_objects", "Charts may require manual review."),
        ("SmartArt/diagram objects", "smartart_diagram_objects", "SmartArt may require manual review."),
        ("OLE embedded objects", "ole_embedded_objects", "Embedded objects may require manual review."),
        ("Image blip references", "image_blip_references", "Image references detected in document XML."),
        ("Extracted images", "extracted_images", "Images copied to working/extracted/images/."),
        ("Missing blip images", "missing_blip_images", "Image references not copied to extracted images."),
    ]
    for label, key, note in rows:
        lines.append(f"| {label} | {scan[key]} | {note} |")
    lines += [
        "",
        "Risk interpretation:",
        "- `Low`: no major visual object detected.",
        "- `Medium`: visual images exist and should be analyzed in step 20, but extraction is not blocked by image presence alone.",
        "- `High`: non-image visual objects or missing image references may hide evidence; manual review is required before downstream use.",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def write_manual_review_template(path: Path, docx_path: Path, scan: dict[str, object], captions: list[ParagraphItem], images: list[ImageItem], refs: list[tuple[str, str, str]], tables: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    risk = str(scan["risk_level"])
    non_image_risk = sum(int(scan[k]) for k in [
        "legacy_pict_objects", "word_textbox_objects", "vml_shape_objects", "vml_textbox_objects",
        "chart_objects", "smartart_diagram_objects", "ole_embedded_objects", "missing_blip_images",
    ])

    lines = ["# Manual Visual Review", ""]
    lines += [
        "This file is generated by `tools/extract_docx.py`.",
        "It is a manual review worksheet only when extraction risk is High or when a later prompt explicitly asks for manual review.",
        "For Medium risk caused only by successfully extracted images, image meaning should be handled by step 20 image analysis, not by this worksheet.",
        "",
        "## Review decision",
        "",
    ]

    if risk in {"Low", "Medium"} and non_image_risk == 0:
        lines += [
            "Current decision: `Manual visual review not required at this stage`",
            "",
            "Reason: image drawing objects were detected, but the corresponding image blip references were extracted successfully and no non-image visual object risk was detected.",
            "",
            "## Source reviewed",
            "",
            f"- Original DOCX: `{docx_path.as_posix()}`",
            "- PDF export: `Not required at this stage`",
            "- Reviewer: `N/A`",
            "- Review date: `N/A`",
            "",
            "## Extraction risk summary from script",
            "",
            f"- Visual risk level: **{scan['risk_level']}**",
            f"- Drawing objects detected: {scan['drawing_objects']}",
            f"- Image blip references detected: {scan['image_blip_references']}",
            f"- Extracted images: {scan['extracted_images']}",
            f"- Missing blip images: {scan['missing_blip_images']}",
            f"- Non-image visual risks: pict={scan['legacy_pict_objects']}, word_textbox={scan['word_textbox_objects']}, vml_shape={scan['vml_shape_objects']}, vml_textbox={scan['vml_textbox_objects']}, chart={scan['chart_objects']}, smartart={scan['smartart_diagram_objects']}, ole={scan['ole_embedded_objects']}",
            "",
            "## Image analysis handoff",
            "",
            "The following images were extracted successfully. Step 20 should analyze image content and confirm diagram meaning.",
            "Candidate captions are best-effort navigation hints from nearby source order; they are not final semantic interpretation.",
            "",
            "| Extracted image | Candidate source caption | Candidate caption section | Previous source text | Step 20 action |",
            "|---|---|---|---|---|",
        ]
        if images:
            for img in images:
                lines.append(
                    f"| `{img.image_id}` / `{img.output_path}` | {md_escape_cell(img.candidate_caption_text or '_not detected_')} | `{img.candidate_caption_section or 'not detected'}` | {md_escape_cell(img.previous_text or '_not detected_')} | Analyze image content and confirm mapping. |"
                )
        else:
            lines.append("| _No images extracted_ |  |  |  |  |")

        lines += [
            "",
            "## External reference note",
            "",
            "External references are recorded for traceability only. They are not blockers unless a later review confirms the DOCX images/text are insufficient without the external file.",
            "",
            "| Source reference | External file reference | Hyperlink target | Blocking at step 10? |",
            "|---|---|---|---|",
        ]
        if refs:
            for sec, label, target in refs:
                lines.append(f"| {sec} | `{label}` | `{target or 'N/A'}` | No |")
        else:
            lines.append("| _None detected_ |  |  |  |")
        lines += [
            "",
            "## When to manually fill this file",
            "",
            "Manual review is needed later only if:",
            "- step 20 cannot read or explain an extracted image,",
            "- a required figure appears missing from `working/extracted/images/`,",
            "- a table layout looks corrupted or ambiguous,",
            "- a reviewer finds mismatch between DOCX/PDF and extracted artifacts, or",
            "- `visual_object_risk_scan.md` reports High risk.",
            "",
            "## Final manual conclusion",
            "",
            "Conclusion: `Not required at this stage`",
        ]
        path.write_text("\n".join(lines), encoding="utf-8")
        return

    # High-risk worksheet: keep it explicit but do not ask for irrelevant zero-count objects.
    lines += [
        "Choose one after review:",
        "",
        "- `Not reviewed yet`",
        "- `Manual visual review passed`",
        "- `Manual visual review passed with warnings`",
        "- `Manual visual review failed`",
        "",
        "Current decision: `Not reviewed yet`",
        "",
        "## Source reviewed",
        "",
        f"- Original DOCX: `{docx_path.as_posix()}`",
        "- PDF export: `<optional path if used>`",
        "- Reviewer: `<name>`",
        "- Review date: `<YYYY-MM-DD>`",
        "",
        "## Extraction risk summary from script",
        "",
        f"- Visual risk level: **{scan['risk_level']}**",
        f"- Drawing objects detected: {scan['drawing_objects']}",
        f"- Image blip references detected: {scan['image_blip_references']}",
        f"- Extracted images: {scan['extracted_images']}",
        f"- Missing blip images: {scan['missing_blip_images']}",
        f"- Non-image visual risks: pict={scan['legacy_pict_objects']}, word_textbox={scan['word_textbox_objects']}, vml_shape={scan['vml_shape_objects']}, vml_textbox={scan['vml_textbox_objects']}, chart={scan['chart_objects']}, smartart={scan['smartart_diagram_objects']}, ole={scan['ole_embedded_objects']}",
        "",
        "## Blocking visual/object review",
        "",
        "Review only items with non-zero counts or missing extracted media.",
        "",
        "| Object type | Count from script | Manual review result | Requirement-relevant missing content? | Notes |",
        "|---|---:|---|---|---|",
    ]
    object_rows = [
        ("Legacy pict", "legacy_pict_objects"), ("Word textbox", "word_textbox_objects"),
        ("VML shape", "vml_shape_objects"), ("VML textbox", "vml_textbox_objects"),
        ("Chart", "chart_objects"), ("SmartArt/diagram", "smartart_diagram_objects"),
        ("OLE embedded object", "ole_embedded_objects"), ("Missing blip image", "missing_blip_images"),
    ]
    any_row = False
    for label, key in object_rows:
        if int(scan[key]) > 0:
            any_row = True
            lines.append(f"| {label} | {scan[key]} | `Not reviewed` | `Unknown` |  |")
    if not any_row:
        lines.append("| _No non-image blocking visual objects detected_ | 0 |  |  |  |")

    lines += [
        "",
        "## Image analysis handoff",
        "",
        "| Extracted image | Candidate source caption | Candidate caption section | Previous source text | Notes |",
        "|---|---|---|---|---|",
    ]
    for img in images:
        lines.append(f"| `{img.image_id}` / `{img.output_path}` | {md_escape_cell(img.candidate_caption_text or '_not detected_')} | `{img.candidate_caption_section or 'not detected'}` | {md_escape_cell(img.previous_text or '_not detected_')} | Analyze in step 20 if downstream proceeds. |")
    lines += [
        "",
        "## Remaining warnings",
        "",
        "- `<fill remaining warning or write None>`",
        "",
        "## Final manual conclusion",
        "",
        "Conclusion: `<Not reviewed yet / Passed / Passed with warnings / Failed>`",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")

def write_summary(path: Path, docx_path: Path, paragraphs: list[ParagraphItem], tables: list[dict], images: list[ImageItem], scan: dict[str, object], comments: list[tuple[str, str, str]], footnotes: list[tuple[str, str]], refs: list[tuple[str, str, str]]) -> None:
    lines = [
        "# Extraction Summary",
        "",
        f"Source file: `{docx_path.as_posix()}`",
        "",
        "## Counts",
        "",
        f"- Paragraph sections extracted: {len(paragraphs)}",
        f"- Tables extracted: {len(tables)}",
        f"- Images extracted: {len(images)}",
        f"- Comments extracted: {len(comments)}",
        f"- Footnotes extracted: {len(footnotes)}",
        f"- External references detected: {len(refs)}",
        "",
        "## Generated files",
        "",
        "- `working/extracted/document_text.md`",
        "- `working/extracted/tables.md`",
        "- `working/extracted/image_inventory_raw.md`",
        "- `working/extracted/formatting_inventory.md`",
        "- `working/extracted/external_references.md`",
        "- `working/extracted/comments.md`",
        "- `working/extracted/footnotes.md`",
        "- `working/extracted/visual_object_risk_scan.md`",
        "- `working/extracted/images/`",
        "- `working/review/manual_visual_review.md`",
        "",
        "## Visual object risk scan",
        "",
        f"Risk level: **{scan['risk_level']}**",
        "",
        f"- Drawing objects detected: {scan['drawing_objects']}",
        f"- Inline drawing objects detected: {scan['inline_drawing_objects']}",
        f"- Anchored drawing objects detected: {scan['anchored_drawing_objects']}",
        f"- Legacy pict objects detected: {scan['legacy_pict_objects']}",
        f"- Word textbox objects detected: {scan['word_textbox_objects']}",
        f"- VML shape objects detected: {scan['vml_shape_objects']}",
        f"- VML textbox objects detected: {scan['vml_textbox_objects']}",
        f"- Chart objects detected: {scan['chart_objects']}",
        f"- SmartArt/diagram objects detected: {scan['smartart_diagram_objects']}",
        f"- OLE embedded objects detected: {scan['ole_embedded_objects']}",
        f"- Image blip references detected: {scan['image_blip_references']}",
        f"- Missing blip images detected: {scan['missing_blip_images']}",
        "",
        "Visual scan detail file:",
        "",
        "- `working/extracted/visual_object_risk_scan.md`",
        "",
        "## Formatting and reference notes",
        "",
        "- Strikethrough text is preserved and marked in extracted text/tables.",
        "- Strikethrough text must not be treated as active behavior by default.",
        "- Highlighted text is preserved as formatting evidence.",
        "- External file links such as `.pptx` are recorded as references, not automatic blockers.",
        "- Comments and footnotes are extracted into separate files when present.",
        "",
        "## Manual review notes",
        "",
        "- DOCX image context extraction is best-effort only.",
        "- Extracted images should be analyzed in step 20 when they are requirement-relevant.",
        "- Ordinary image drawing objects are not a blocker by themselves when the referenced images were extracted.",
        "- Non-image visual objects, missing image media, complex merged tables, comments, and footnotes may require manual review.",
        "- Run prompt `10_extract_docx_inventory` after extraction to review inventory completeness and downstream readiness.",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def extract_docx(docx_path: Path, work_dir: Path, output_dir: Path) -> None:
    if not docx_path.exists():
        raise FileNotFoundError(f"DOCX not found: {docx_path}")

    extracted_dir = work_dir / "extracted"
    images_dir = extracted_dir / "images"
    review_dir = work_dir / "review"

    if images_dir.exists():
        shutil.rmtree(images_dir)
    images_dir.mkdir(parents=True, exist_ok=True)
    extracted_dir.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(docx_path) as zf:
        if "word/document.xml" not in zf.namelist():
            raise ValueError("Invalid DOCX: word/document.xml not found")

        rels = load_relationships(zf)
        root = ET.fromstring(zf.read("word/document.xml"))
        body = root.find("w:body", NS)
        if body is None:
            raise ValueError("Invalid DOCX: document body not found")

        paragraphs, block_images = collect_paragraphs(body, rels)
        tables = collect_tables(body, rels)
        images = extract_images_in_document_order(zf, rels, block_images, images_dir)
        enrich_image_caption_candidates(images, paragraphs)
        scan = visual_risk_scan(zf, root, len(images))
        comments = extract_comments(zf)
        footnotes = extract_notes(zf, "footnotes", "footnote")
        endnotes = extract_notes(zf, "endnotes", "endnote")
        captions = figure_caption_candidates(paragraphs)
        refs = external_references(paragraphs)

    write_document_text(extracted_dir / "document_text.md", docx_path, paragraphs)
    write_tables(extracted_dir / "tables.md", docx_path, tables)
    write_image_inventory(extracted_dir / "image_inventory_raw.md", docx_path, images)
    write_formatting_inventory(extracted_dir / "formatting_inventory.md", paragraphs, tables)
    write_external_references(extracted_dir / "external_references.md", refs)
    write_comments(extracted_dir / "comments.md", comments)
    write_notes(extracted_dir / "footnotes.md", footnotes, endnotes)
    write_visual_scan(extracted_dir / "visual_object_risk_scan.md", scan)
    write_manual_review_template(review_dir / "manual_visual_review.md", docx_path, scan, captions, images, refs, tables)
    write_summary(output_dir / "10_extraction_summary.md", docx_path, paragraphs, tables, images, scan, comments, footnotes, refs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", nargs="?", default="input/original/requirement.docx")
    parser.add_argument("--working-dir", default="working")
    parser.add_argument("--output-dir", default="output")
    args = parser.parse_args()

    try:
        extract_docx(Path(args.docx), Path(args.working_dir), Path(args.output_dir))
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print("Extraction completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
