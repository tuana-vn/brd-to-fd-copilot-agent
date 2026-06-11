# 14 - Apply Translation Review Corrections

## Purpose

Correct normalized evidence based on the translation review report.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent requirements, field meanings, business rules, messages, screen behavior, or diagrams.
- Preserve source-specific terms unless a translation policy or glossary explicitly defines them.
- Mark ambiguous, missing, or conflicting information instead of guessing.
- Keep customer-facing content free from internal pipeline terms and internal IDs.
- Internal review and traceability files may use internal IDs.
- Write outputs in English unless the source value must remain unchanged.
- Do not modify the original BRD. Customer answers are supplemental evidence only.

## Inputs
- `output/10_document_inventory.md`
- `output/11_translation_policy.md`
- `output/12_normalized_evidence.md`
- `output/13_translation_review_report.md`

- Source extraction files under `working/extracted/`


## Outputs to create or update

- `output/14_normalized_evidence_corrected.md`
- `output/14_translation_correction_log.md`


## Task

1. Apply only corrections supported by the review report and source extraction.
2. Preserve existing source IDs.
3. Do not add new inferred requirements.
4. Log each correction with before/after and reason.


## Required output quality

- Corrections must be traceable to source evidence.
- Do not hide remaining uncertainty.


## Stop conditions

- Stop and report `No-Go` if required inputs are missing.
- Stop and report `No-Go` if the output would require unsupported assumptions.
- Do not continue to downstream phases when the current quality gate is `No-Go`.
