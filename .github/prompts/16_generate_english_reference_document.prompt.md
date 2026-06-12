# 16 - Generate English Reference Document

## Purpose

Generate a readable English Markdown reference document from the reviewed Japanese BRD evidence.

This document is intended for human reading by BA, developer, reviewer, and project members who need to understand the source requirement document more easily before image analysis, glossary creation, requirement extraction, FD generation, or DD/coding work.

This task does **not** create requirements, business rules, Functional Design, Detailed Design, test design, or implementation design.

The output is a supporting reference translation only. It must not replace the original Japanese BRD, the extracted source evidence, or the controlled normalized evidence.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent requirements, field meanings, business rules, messages, screen behavior, diagrams, actors, systems, states, or implementation details.
- Do not extract final requirements.
- Do not generate FD.
- Preserve source-specific terms unless `output/11_translation_policy.md` explicitly defines a safe English rendering.
- Preserve command names, option names, parameters, field names, product names, acronyms, code-like identifiers, operation identifiers, UI/API names, and file names exactly.
- Do not expand undefined acronyms.
- Preserve unsupported behavior, negative statements, conditions, exceptions, notes, footnotes, and source warnings.
- Mark ambiguous, missing, conflicting, unreadable, or low-confidence content instead of guessing.
- Keep the document readable, but do not smooth over technical uncertainty.
- Write the output in English unless the source value must remain unchanged.
- Do not modify the original BRD.
- Do not expose prompt names, AI, Copilot, model usage, or prompt workflow details in the generated English reference document.
- Internal source references may be included when useful for review, but the document must still read like a readable English reference translation.

### Reference document rule

This output is an English reference translation for readability only.

The authoritative source remains:

- the original Japanese BRD
- extracted source evidence
- `output/11_translation_policy.md`
- `output/12_normalized_evidence.md`
- `output/14_normalized_evidence_corrected.md`, when available
- the latest translation quality review result

Downstream extraction and FD prompts should continue to use the controlled evidence artifacts, not this reference document as the primary source of truth.

### Formatting evidence rules

- Treat source formatting as evidence when it changes meaning.
- Strikethrough text means inactive, deleted, deprecated, superseded, or draft-removed evidence unless the source explicitly says otherwise.
- Do not present strikethrough-only text as active behavior, active requirement, active business rule, active operation flow, active field definition, or active UI/API behavior.
- If a paragraph, table cell, caption, or note contains both active and strikethrough text, use only the non-strikethrough portion as active reference content.
- Preserve strikethrough evidence only as deleted/deprecated/inactive context when it helps the reader understand source changes.
- If highlighted text is also strikethrough, the strikethrough rule wins.
- Highlighted text is not automatically active, mandatory, or more important unless the source says so.
- If formatting status is unclear or missing from upstream artifacts, mark the affected content as ambiguous instead of guessing.

### Visual evidence rules

- Include extracted source images when they are relevant to the nearby translated content and can be linked with reasonable confidence.
- Use Markdown image references with relative paths from the output file, for example:
  `![Figure: <caption>](../working/extracted/images/IMG-001.png)`
- Do not recreate, redraw, modify, or simplify original source images in this step.
- Do not infer behavior, routing, failover, sequence, state transition, mandatory configuration, or business rules from image layout, arrows, colors, icons, or topology alone.
- For complex topology, network, architecture, routing, state, or operation diagrams, include the image as visual support and rely on nearby translated text/table evidence for behavior.
- If a figure mapping is uncertain, do not force the image into the main body as confirmed evidence. Put it in an appendix section titled `Extracted Images Requiring Mapping Check`.
- If image text is unreadable or partially readable, mark it as unreadable or partially readable.
- External `.pptx`, `.xlsx`, `.docx`, `.pdf`, or SharePoint links are references only. Do not treat missing external files as missing BRD evidence unless the source explicitly requires them to understand behavior.

## Precondition

Use the latest effective translation quality gate:

1. If `output/15_translation_review_followup_report.md` exists, use it as the latest translation gate.
2. Otherwise, use `output/13_translation_review_report.md`.
3. Continue only if the latest gate decision is one of:
   - `Go`
   - `Go with minor risks`
   - `Go with warnings`
4. Stop and report `No-Go` if the latest gate decision is `No-Go`.

Use the latest normalized evidence source:

1. If `output/14_normalized_evidence_corrected.md` exists and the latest translation gate allows continuation, use it as the primary normalized evidence.
2. Otherwise, use `output/12_normalized_evidence.md`.
3. Use `output/14_translation_correction_log.md`, if present, to avoid reintroducing corrected translation defects.

## Inputs

### Primary inputs

Use these inputs by default:

- `output/11_translation_policy.md`
- latest normalized evidence:
  - `output/14_normalized_evidence_corrected.md`, if present and accepted by the latest gate
  - otherwise `output/12_normalized_evidence.md`
- latest effective translation gate report:
  - `output/15_translation_review_followup_report.md`, if present
  - otherwise `output/13_translation_review_report.md`

### Visual inputs

Use these to include source images when appropriate:

- `working/extracted/image_inventory_raw.md`, if present
- all files under `working/extracted/images/`

### Supporting inputs

Open these only when needed for targeted verification, source ordering, formatting status, or image mapping:

- `output/10_document_inventory.md`
- `output/14_translation_correction_log.md`, if present
- `working/extracted/formatting_inventory.md`, if present
- `working/extracted/external_references.md`, if present
- `working/extracted/document_text.md`, only for targeted verification
- `working/extracted/tables.md`, only for targeted verification

Do not load unnecessary raw source artifacts by default. Use the latest normalized evidence as the main text context.

## Tasks

### Instructions

Create a readable English Markdown reference document from the latest normalized evidence.

Preserve the approximate source document order and structure as much as possible:

1. Headings and sections
2. Paragraphs and notes
3. Tables
4. Figures and embedded images
5. Figure captions
6. Footnotes or note-like content
7. Important comments or warnings if extracted and relevant
8. External references, marked as references only

For each source section:

- Use the reviewed English normalized evidence.
- Preserve technical terms according to `output/11_translation_policy.md`.
- Preserve exact command syntax, options, parameters, identifiers, and code-like text.
- Preserve unsupported behavior, negative statements, conditions, exceptions, notes, and footnotes.
- Preserve source references in a lightweight reader-friendly way when useful.
- If content was originally struck through, clearly mark it as deleted/deprecated/inactive context.
- If source meaning remains uncertain, write `Requires confirmation` or `Translation uncertain` instead of guessing.
- If a table is present in normalized evidence, reproduce it as a Markdown table as faithfully as practical.
- If table layout cannot be safely reconstructed, include a simplified table and add a note that layout should be checked against the source.

### Image placement instructions

For each figure/image:

1. Use `working/extracted/image_inventory_raw.md` and normalized evidence captions to determine the best placement.
2. Place images near their related caption or section when mapping is reasonably clear.
3. Use a customer-readable caption, not internal figure IDs.
4. Use relative paths from the output file:
   - Correct pattern: `../working/extracted/images/<image_file>`
5. Do not include duplicate, decorative, unreadable, or weakly mapped images in the main body unless the nearby source text clearly depends on them.
6. If an image is likely relevant but not confidently mapped, list it under `Appendix A - Extracted Images Requiring Mapping Check`.

## Output

Create or update:

- `output/16_requirement_english_reference.md`

## Required output structure

Write `output/16_requirement_english_reference.md` using this structure:

```markdown
# English Reference Translation

## Document Status

| Field | Value |
|---|---|
| Document type | English reference translation |
| Intended use | Human reading and review |
| Source basis | Original BRD extracted evidence and reviewed normalized evidence |
| Source-of-truth status | Not source of truth; reference only |
| Latest translation gate | Go / Go with minor risks / Go with warnings |
| Remaining translation risks | ... |

## Reader Notes

- This document is a readable English reference translation.
- It does not replace the original source document.
- Items marked `TBD`, `Requires confirmation`, or `Translation uncertain` should not be treated as confirmed behavior.
- Images are included as source visual references. Complex visual behavior should be confirmed by nearby text, tables, or domain expert clarification.

## Main Translated Content

Reconstruct the translated source document content here in source order.

Use source headings where available.
Use Markdown tables for source tables.
Use Markdown image references for mapped extracted images.
Preserve important notes, footnotes, unsupported cases, and negative statements.

## Appendix A - Extracted Images Requiring Mapping Check

List extracted images that appear relevant but could not be confidently placed in the main translated content.

| Image file | Possible related source text / caption | Reason mapping is uncertain | Recommended handling |
|---|---|---|---|

## Appendix B - External References

List external file references or links that appeared in the source evidence.

| Reference | Source location | Required for understanding? | Notes |
|---|---|---|---|

## Appendix C - Translation and Formatting Cautions

List remaining translation, formatting, strikethrough, highlight, table-layout, or visual-layout cautions that readers should know.

| Caution ID | Area | Caution | Impact |
|---|---|---|---|
```

## Output quality rules

- Output must be English.
- Do not expose internal requirement IDs, business rule IDs, glossary IDs, open-question IDs, trace IDs, or image-analysis IDs.
- Source references such as section names, table captions, figure captions, and source item references may be included if they help review.
- Do not mention Copilot, AI, model, prompt, pipeline, or internal workflow details.
- Do not generate FD.
- Do not extract final requirements.
- Do not create business rules from the translated content.
- Do not add source meaning that is not present in the latest normalized evidence.
- Do not remove negative statements, unsupported behavior, exceptions, notes, or footnotes.
- Do not silently resolve uncertainty.
- Preserve all important exact technical strings.
- If the latest normalized evidence conflicts with raw source during targeted verification, mark the issue in `Appendix C` and do not guess.
- If an image appears to show behavior not confirmed by nearby text/table evidence, describe it only as a visual reference and mark behavior interpretation as requiring confirmation.

## Stop conditions

Stop and report `No-Go` only if:

- `output/11_translation_policy.md` is missing.
- Both `output/12_normalized_evidence.md` and `output/14_normalized_evidence_corrected.md` are missing.
- The latest effective translation gate report is missing.
- The latest effective translation gate decision is `No-Go`.
- The output would require unsupported assumptions to reconstruct the reference document.

Do not stop only because some images cannot be confidently mapped. Put them in `Appendix A` and continue.
