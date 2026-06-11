# 12 - Normalize Evidence to English

## Purpose

Convert extracted Japanese evidence into source-bound English while preserving traceability to the extracted evidence.

## Task
- Normalize source text to English section by section.
- Normalize tables to English while preserving table structure.
- Preserve original source IDs.
- Mark uncertain translations explicitly.
- Do not infer requirements yet.

## Operating rules
- Output must be English.
- This is not free translation.
- Preserve the meaning of the Japanese evidence.
- Follow `output/11_translation_policy.md` strictly.
- Keep acronyms and field names unchanged.
- Do not add new requirements.
- Do not remove negative statements, constraints, exceptions, or footnotes.
- Keep source references.
- If translation is uncertain, keep the original Japanese phrase in parentheses and mark Translation Confidence as Low.
- Do not generate FD.

## Inputs
- `output/10_document_inventory.md`
- `output/11_translation_policy.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`
- `working/extracted/images_inventory_raw.md`

## Outputs to create or update

- `output/12_normalized_evidence.md`

# Required output quality
- Every normalized section must reference source IDs.
- Unknown terms must remain source-bound.
- No business rule extraction in this phase.

# Document Inventory - English Normalized

| Item ID | Source Reference | Original Japanese Text | Technical English Rendering | Preserved Terms | Translation Confidence | Meaning Risk | Notes / Open Questions |
|---|---|---|---|---|---|---|

## Stop conditions

- Stop and report `No-Go` if required inputs are missing.
- Stop and report `No-Go` if the output would require unsupported assumptions.
- Do not continue to downstream phases when the current quality gate is `No-Go`.