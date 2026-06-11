# 13 - Review Translation Quality

## Purpose

Gate the normalized English evidence before it is used for requirements extraction.

## Operating rules
- Do not generate FD.
- Do not extract new requirements.
- Do not rewrite the whole `output/12_normalized_evidence.md` file.
- Focus only on translation/normalization quality.
- If an issue is found, cite the source item and suggest the corrected English rendering.
- If meaning is uncertain, mark it as Open Question instead of guessing.

## Task:
- Missing conditions
- Missing negative statements
- Missing exceptions
- Missing footnotes
- Incorrectly translated domain terms
- Acronyms expanded without evidence
- Field names changed incorrectly
- Business rules softened or strengthened
- Japanese terms that should have been preserved
- English statements that add meaning not present in Japanese
- Source references missing or weakened

## Inputs
- `output/10_document_inventory.md`
- `output/11_translation_policy.md`
- `output/12_normalized_evidence.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`

## Outputs

###  Outputs file to create or update
- `output/13_translation_review_report.md`

### Required output quality

- Be strict.
- Focus on evidence fidelity, not writing style.

### Output structure:
1. Executive summary
2. Critical translation issues
3. Major translation issues
4. Minor translation issues
5. Terminology consistency issues
6. Missing source references
7. Recommended corrections

### Stop conditions

- Stop and report `No-Go` if required inputs are missing.
- Stop and report `No-Go` if the output would require unsupported assumptions.
- Do not continue to downstream phases when the current quality gate is `No-Go`.