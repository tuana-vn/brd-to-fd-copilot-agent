# RUNBOOK - BRD to FD Copilot Workflow

## 1. Prepare input

Copy the customer BRD DOCX to:

```text
input/original/requirement.docx
```

Do not edit the source BRD.

## 2. Extract DOCX

Run:

```bash
python3 tools/extract_docx.py input/original/requirement.docx
```

Expected outputs:

```text
working/extracted/document_text.md
working/extracted/tables.md
working/extracted/image_inventory_raw.md
working/extracted/images/
output/10_extraction_summary.md
```

## 3. Run extraction and translation gate

Run prompts:

```text
10_extract_docx_inventory
11_create_translation_policy
12_normalize_evidence_to_english
13_review_translation_quality
```

If `13` returns `No-Go`, run:

```text
14_apply_translation_review_corrections
15_review_translation_quality_followup
```

Continue only when translation quality is acceptable.

## 4. Analyze images and glossary

Run:

```text
20_analyze_embedded_images
21_create_domain_glossary
```

Images must be treated as evidence, not decoration.

## 5. Extract requirements

Run:

```text
30_extract_requirements
```

Expected outputs:

```text
output/30_requirement_inventory.md
output/31_business_rule_catalog.md
output/32_open_questions.md
```

## 6. Generate first FD

Run:

```text
40_generate_customer_fd
41_generate_fd_traceability
42_review_fd
```

If `42 = Go`, the customer-facing FD is:

```text
output/40_FD_DRAFT.md
```

## 7. Apply bounded FD corrections

If `42` is fixable:

```text
50_apply_fd_review_corrections
51_generate_revised_fd_traceability
52_review_revised_fd
```

If `52 = Go`, the customer-facing FD is:

```text
output/50_FD_DRAFT_REVISED.md
```

If still fixable:

```text
53_apply_revised_fd_review_corrections
54_generate_patched_fd_traceability
55_review_patched_fd
```

If `55 = Go`, the customer-facing FD is:

```text
output/53_FD_DRAFT_REVISED_PATCHED.md
```

If `55 = No-Go`, stop automated revision. Use customer Q&A or human correction.

## 8. Customer Q&A path

If the BRD is ambiguous, contradictory, or incomplete:

```text
60_generate_customer_qa
```

Send the resulting file to the customer:

```text
output/60_CUSTOMER_QA.md
```

After customer answers are received, save them to:

```text
input/supplemental/customer_answers.md
```

Then run:

```text
61_normalize_customer_answers
62_analyze_customer_answer_impact
63_update_requirements_from_customer_answers
70_generate_fd_after_customer_answers
71_generate_fd_after_customer_answers_traceability
72_review_fd_after_customer_answers
```

If `72 = Go`, the customer-facing FD is:

```text
output/70_FD_DRAFT_AFTER_QA.md
```

## 9. Output check

Run:

```bash
bash tools/check_outputs.sh
```

## 10. Reset working/output files

To clean generated working/output/design files while keeping input files:

```bash
bash tools/reset_workspace.sh
```

## 11. Important cautions

- Do not edit `input/original/requirement.docx`.
- Do not treat customer answers as changes to the original BRD.
- Do not expose internal IDs in customer-facing FD.
- Do not continue after `No-Go` gates.
- Do not jump directly from long Markdown FD to code generation.
