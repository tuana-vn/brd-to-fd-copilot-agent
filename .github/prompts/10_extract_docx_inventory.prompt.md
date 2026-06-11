# 10 - Review DOCX Extraction Inventory

## Purpose

Review the DOCX extraction package produced by `tools/extract_docx.py` and create a controlled evidence inventory for downstream BRD-to-FD prompts.

This prompt does **not** extract DOCX content. The Python script already produced raw evidence and technical extraction reports.

## Inputs

Primary inputs:
- `output/10_extraction_summary.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`
- `working/extracted/image_inventory_raw.md`

Supporting inputs, if present:
- `working/extracted/formatting_inventory.md`
- `working/extracted/external_references.md`
- `working/extracted/comments.md`
- `working/extracted/footnotes.md`
- `working/extracted/visual_object_risk_scan.md`
- `working/review/manual_visual_review.md`

## Output to create or overwrite

- `output/10_document_inventory.md`

Do not modify files under `working/extracted/`.
Do not modify files under `working/review/`.

## Operating rules

- Do not generate FD.
- Do not translate the whole document.
- Do not extract detailed requirements yet.
- Do not infer missing business behavior.
- Do not treat visual content as fully understood before step 20 image analysis.
- Do not treat external `.pptx`, `.xlsx`, `.docx`, `.pdf`, or `.vsdx` references as automatic blockers.
- Do not treat comments as active requirements unless the source explicitly makes them part of the requirement.
- Do not treat footnotes as inactive; footnotes may be valid requirement evidence and must be tracked if present.
- Keep the output concise enough to be reused by downstream prompts without excessive token cost.

## Formatting rules

The Python extractor preserves formatting markers.

### Strikethrough

Text marked as:

```text
[STRIKETHROUGH: ...]
```

means the source text was struck through.

Rules:
- Preserve it in inventory as inactive/deprecated candidate evidence.
- Do not classify strikethrough-only content as active requirement, active business rule, or active operation flow.
- If a cell/paragraph contains both active and strikethrough text, use only the active text for active evidence classification.
- Mention struck-through text in remarks or formatting notes only when it may affect interpretation.
- If active/inactive meaning is unclear, create an extraction warning or open issue.

### Highlight

Text marked as:

```text
[HIGHLIGHT:<color> ...]
```

means the source text was highlighted.

Rules:
- Highlight alone does not prove final/changed/important behavior.
- Preserve highlighted text as evidence.
- Do not invent meaning from highlight color.
- If highlighted text is also strikethrough, the strikethrough rule wins.

## Visual risk rules

Read `working/extracted/visual_object_risk_scan.md` and `output/10_extraction_summary.md`.

### Low visual risk

Decision:
- Use `Go` if required text/table files are present.

### Medium visual risk

Typical case:
- The DOCX contains ordinary drawing/image objects.
- Image blip references were successfully extracted to `working/extracted/images/`.
- `missing_blip_images = 0`.
- No non-image visual object risks are detected: no Word/VML textboxes, VML shapes, charts, SmartArt, OLE objects, or legacy pict objects.

Decision:
- Use `Go with warnings`, not `No-Go`, unless another blocking problem exists.
- Manual visual review is **not required at step 10** for this case.
- `working/review/manual_visual_review.md` may say `Manual visual review not required at this stage`; treat that as non-blocking.
- Require step 20 image analysis before visual-derived requirements are used.
- Use candidate image captions from `working/extracted/image_inventory_raw.md` only as navigation hints, not final semantic interpretation.

### High visual risk

Typical causes:
- Word/VML textboxes, shapes, charts, SmartArt, OLE objects, legacy pict objects, or missing image media were detected.
- These may contain requirement-relevant evidence not represented in extracted text/images.

Decision:
- If `working/review/manual_visual_review.md` is missing, not filled, says `Not reviewed yet`, or has unresolved blocking placeholders, return `No-Go`.
- If manual review says `Manual visual review failed`, return `No-Go`.
- If manual review says `Manual visual review passed with warnings`, return `Go with warnings` and carry unresolved warnings.
- If manual review says `Manual visual review passed`, return `Go` or `Go with warnings` depending on remaining issues.

## External reference rules

External references such as `TIA_Flexible_Grouping_図.pptx` should be listed as external references.

Do not return `No-Go` only because an external reference exists.

Return `No-Go` only if:
- the BRD explicitly requires the external artifact to understand behavior, and
- the artifact is not available or not reviewed, and
- the missing information is required before translation/normalization can safely continue.

Otherwise, mark external references as warning/open issue only.

## Manual visual review rules

If `working/review/manual_visual_review.md` exists:
- Treat `Current decision: Manual visual review not required at this stage` as non-blocking when visual risk is Low/Medium and no non-image visual risks exist.
- Treat it as evidence only if `Current decision` or `Conclusion` is completed.
- Do not assume placeholders are filled.
- Rows with `Unclear`, `Unknown`, `<fill ...>`, or `Not reviewed` are unresolved.
- Use completed rows to downgrade High risk only when the review explicitly confirms coverage.

If the file exists but is only a generated template:
- Do not treat it as completed manual review.
- Mention it as available but not completed.
- Do not block step 11 solely because the template exists when visual risk is Low/Medium.

## Required inventory content

Write `output/10_document_inventory.md` with this structure:

```markdown
# DOCX Extraction Inventory Review

## 1. Review decision

One of:
- `Go`
- `Go with warnings`
- `No-Go`

Reason: <concise reason>

## 2. Input files checked

| File | Status | Notes |
|---|---|---|

## 3. Extraction counts

| Item | Count | Notes |
|---|---:|---|

## 4. Visual and formatting risk review

| Risk item | Count / status | Impact | Required action |
|---|---|---|---|

## 5. Section inventory

Create a concise source-order inventory from `working/extracted/document_text.md`.

Use this table:

| Inventory ID | Source reference | Original Japanese title / key phrase | Short classification summary | Evidence type | Confidence | Remarks |
|---|---|---|---|---|---|---|

Evidence type should be one of:
- Policy
- Business rule candidate
- Operation flow candidate
- Data definition candidate
- UI/API behavior candidate
- Figure / diagram reference
- Table reference
- External reference
- Comment / review note
- Deprecated / struck-through evidence
- Open issue / ambiguity
- Note

Important:
- Use active text for active evidence classification.
- Strikethrough-only text must be classified as `Deprecated / struck-through evidence`.
- Figure captions and visual references may be listed as `Figure / diagram reference`, but do not claim image meaning yet.
- Keep the inventory concise. Do not copy every long paragraph verbatim.

## 6. Table inventory

| Inventory ID | Source reference | Table description / first visible key phrase | Possible use | Confidence | Remarks |
|---|---|---|---|---|---|

Important:
- Mention tables with strikethrough/highlight formatting.
- Mention tables whose meaning may depend on merged/sparse layout.
- Do not convert table contents into business rules yet.

## 7. Image inventory

Use `working/extracted/image_inventory_raw.md`.

| Inventory ID | Source image ID | Extracted path | Candidate caption / source context | Possible content type | Confidence | Remarks |
|---|---|---|---|---|---|---|

Important:
- If candidate caption is present, use it as a navigation hint only.
- Do not claim full diagram meaning in step 10.
- Refer to step 20 for image analysis.
- If image extraction succeeded and candidate captions exist, confidence may be Medium for trace/navigation, but semantic confidence remains pending step 20.

## 8. External references

| Source reference | External reference | Blocking? | Notes |
|---|---|---|---|

Blocking should normally be `No` unless the source explicitly requires that external artifact to understand behavior.

## 9. Comments / footnotes / formatting notes

Summarize comments, footnotes, strikethrough, highlight, and other formatting evidence that may affect downstream interpretation.

## 10. Extraction risks and open issues

| Risk ID | Risk | Evidence | Severity | Recommended action |
|---|---|---|---|---|

## 11. Downstream readiness

| Downstream step | Ready? | Notes |
|---|---|---|
| 11 Create translation policy | Yes / Yes with warnings / No | |
| 12 Normalize evidence to English | Yes / Yes with warnings / No | |
| 20 Analyze embedded images | Yes / Yes with warnings / No | |
| 30 Extract requirements | Yes / Yes with warnings / No | |
| 40 Generate customer-facing FD | Yes / Yes with warnings / No | |
```

## Decision guidance for this repository

- If extraction summary shows `Visual risk level: Medium`, `image_blip_references == extracted_images`, `missing_blip_images == 0`, and all non-image visual object counts are zero, the expected decision is `Go with warnings`.
- The warning should say that images must still be analyzed in step 20 before visual-derived requirements are used.
- Do not force manual visual review for this Medium-risk image-only case.
- Do not block on external `.pptx` links unless the extracted DOCX images/text are insufficient to understand behavior.
