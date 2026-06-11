# 15 - Review Translation Quality Follow-up

## Purpose

Re-run the translation quality gate after corrections.

## Operating rules

- Do not rewrite the whole file unnecessarily.
- Do not add new business meaning.
- Do not remove source references.
- Preserve all source conditions, exceptions, negative statements, and footnotes.
- Follow `output/11_translation_policy.md` strictly.
- If the review identifies an internal contradiction, add it as an explicit Open Question in the affected row.
- If a correction is uncertain, keep the original Japanese phrase in parentheses and mark Translation Confidence as Low.
- Keep the output in English.
- Do not generate FD.
- Do not extract requirements yet.

## Inputs

- `output/14_normalized_evidence_corrected.md`
- `output/14_translation_correction_log.md`
- `output/13_translation_review_report.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`


## Outputs to create or update

- `output/15_translation_review_followup_report.md`


## Task

1. Verify that required corrections were applied.
2. Identify remaining defects.
3. Provide final decision: `Go`, `Go with minor risks`, or `No-Go`.


## Required output quality

- If any major defect remains, return `No-Go`.
- Do not continue to requirements extraction unless acceptable.


## Stop conditions

- Stop and report `No-Go` if required inputs are missing.
- Stop and report `No-Go` if the output would require unsupported assumptions.
- Do not continue to downstream phases when the current quality gate is `No-Go`.
