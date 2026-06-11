# 61 - Normalize Customer / Domain Expert Answers

## Purpose

Normalize customer/domain expert answers into structured supplemental evidence that can be safely used by later impact analysis and FD update steps.

Customer answers are supplemental evidence. They do not modify the original BRD and must not be silently merged into source-derived artifacts.

This task must not generate requirements, business rules, FD content, DD content, or code design.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Treat customer/domain expert answers as supplemental evidence, not as original BRD evidence.
- Do not invent meaning beyond the customer answer.
- Do not over-apply a narrow answer to unrelated requirements, rules, diagrams, or FD sections.
- Preserve customer answer wording where it affects meaning.
- Preserve product-specific terms, command names, option names, field names, acronyms, and code-like identifiers exactly.
- Follow `output/21_glossary.md` and `output/11_translation_policy.md`.
- Respect strikethrough/deprecated evidence rules from the pipeline:
  - strikethrough-only source evidence must not be treated as active behavior unless the source explicitly says otherwise.
  - if a customer answer appears to reactivate or reject strikethrough/deprecated evidence, mark the answer as requiring impact analysis.
- Do not expose internal prompt or pipeline details in customer-facing wording.
- Internal IDs may be used in this inventory for traceability.
- Write outputs in English unless source values must remain unchanged.

## Tasks

### Precondition

Use the latest available customer/domain expert Q&A file:

- Use `output/60_CUSTOMER_QA.md` as the question baseline.
- Use `input/supplemental/customer_answers.md` as the customer/domain expert answer source.
- If `input/supplemental/customer_answers.md` is missing or empty, stop with `No-Go`.

Use the latest available review context only to understand why the questions were asked:

- Prefer `output/55_FD_PATCHED_REVIEW_REPORT.md` if available.
- Otherwise use `output/52_FD_REVISED_REVIEW_REPORT.md` if available.
- Otherwise use `output/42_FD_REVIEW_REPORT.md` if available.

### Instructions

For each customer/domain expert answer:

1. Match it to the related customer-facing QID from `output/60_CUSTOMER_QA.md` when possible.
2. Preserve the original answer text in the inventory.
3. Normalize the answer into concise technical English.
4. Classify the answer type and affected area.
5. Link it to related source-derived items when identifiable:
   - requirements from `output/30_requirement_inventory.md`
   - business rules from `output/31_business_rule_catalog.md`
   - open questions from `output/32_open_questions.md`
   - terms from `output/21_glossary.md`
   - image evidence from `output/20_image_analysis.md`
6. Mark confidence and remaining ambiguity.
7. Do not update any downstream artifact in this task.

## Inputs

### Primary inputs

- `output/60_CUSTOMER_QA.md`
- `input/supplemental/customer_answers.md`
- `output/32_open_questions.md`
- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/21_glossary.md`

### Supporting inputs, open only when needed

- `output/55_FD_PATCHED_REVIEW_REPORT.md`, if available
- `output/52_FD_REVISED_REVIEW_REPORT.md`, if available
- `output/42_FD_REVIEW_REPORT.md`, if available
- `output/20_image_analysis.md`
- `output/12_normalized_evidence.md`
- `output/11_translation_policy.md`
- `output/10_document_inventory.md`

## Outputs

### Output file to create or update

Create:

- `output/61_customer_answer_inventory.md`

## Required output structure

Write `output/61_customer_answer_inventory.md` using this structure:

```markdown
# Customer Answer Inventory

## 1. Normalization Decision

Decision: `Usable` / `Usable with warnings` / `Needs clarification` / `No-Go`

Explain the decision briefly.

## 2. Customer Answer Inventory

| Answer ID | Related QID | Customer Answer | Normalized English Meaning | Answer Type | Affected Area | Related Source Reference | Related Requirement IDs | Related Rule IDs | Related Open Question IDs | Related Terms | Confidence | Remaining Ambiguity | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 3. Answer Summary

Include:

- Number of answers processed
- Number of complete answers
- Number of partial answers
- Number of unclear answers
- Number of answers that contradict source evidence
- Number of answers that may change requirement/rule behavior
- Number of answers that affect FD wording only
- Main affected areas

## 4. Remaining Clarifications

| Answer ID | Related QID | Remaining Ambiguity | Why It Matters | Recommended Follow-up |
|---|---|---|---|---|

## 5. Notes for Impact Analysis

List concise notes that step 62 should consider.
```

## Field definitions

- Answer ID: Use `ANS-001`, `ANS-002`, etc.
- Related QID: Customer-facing QID from `output/60_CUSTOMER_QA.md`, if available. Use `Unmatched` if no QID can be identified.
- Customer Answer: Original answer text, preserving important wording.
- Normalized English Meaning: Concise technical English interpretation.
- Answer Type must be one of:
  - Confirms existing behavior
  - Rejects existing behavior
  - Clarifies terminology
  - Defines missing condition
  - Defines unsupported behavior
  - Defines data rule
  - Defines operation flow
  - Clarifies diagram
  - Adds new supplemental detail
  - Contradicts source
  - Partial answer
  - Unclear answer
  - No impact
- Affected Area must be one of:
  - Terminology
  - Requirement
  - Business rule
  - Open question
  - Diagram / visual
  - FD wording
  - Non-functional / performance
  - Error / warning handling
  - Data definition
  - Traceability
  - Other
- Related Source Reference: Customer-facing section/table/note/figure reference when available; internal source IDs may be used only in this inventory.
- Related Requirement IDs: `REQ-xxx` from `output/30_requirement_inventory.md`, if identifiable.
- Related Rule IDs: `BR-xxx` from `output/31_business_rule_catalog.md`, if identifiable.
- Related Open Question IDs: `OQ-xxx` from `output/32_open_questions.md`, if identifiable.
- Related Terms: `TERM-xxx` from `output/21_glossary.md`, if identifiable.
- Confidence: High / Medium / Low.
- Remaining Ambiguity: Yes / No.

## Quality rules

- Do not generate requirements.
- Do not generate business rules.
- Do not generate FD content.
- Do not update glossary, requirement inventory, business rule catalog, open questions, FD, or traceability.
- Do not treat customer answers as original BRD evidence.
- Do not invent implied behavior from vague answers.
- Do not normalize an unclear answer into a confident rule.
- If the answer only says “yes”, “no”, or similar, resolve it only against the matched QID; do not generalize it.
- If the answer contradicts BRD/source evidence, mark Answer Type as `Contradicts source` and explain the contradiction.
- If the answer is partial, mark Answer Type as `Partial answer` and keep Remaining Ambiguity as `Yes`.
- If the answer is unclear, mark Answer Type as `Unclear answer` and keep Confidence as `Low`.
- Preserve exact command/option spelling such as `raidcom`, `-splt_time_id`, `snapshotgroup_add`, and similar source-specific identifiers.
- Preserve locked terms from `output/21_glossary.md` and `output/11_translation_policy.md`.

## Stop conditions

- Stop and report `No-Go` if `input/supplemental/customer_answers.md` is missing or empty.
- Stop and report `No-Go` if `output/60_CUSTOMER_QA.md` is missing.
- Stop and report `No-Go` if required source-of-truth artifacts `output/30_requirement_inventory.md`, `output/31_business_rule_catalog.md`, or `output/32_open_questions.md` are missing.
- Do not continue to impact analysis or FD update from customer answers alone without creating `output/61_customer_answer_inventory.md`.
