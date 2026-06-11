# 71 - Generate FD After Customer Answers Traceability

## Purpose

Create internal traceability for the customer-facing Functional Design generated after customer/domain expert answers.

This task maps `output/70_FD_DRAFT_AFTER_QA.md` back to original source evidence, after-QA requirement artifacts, customer/domain expert answers, and unresolved open questions.

This task must not revise the FD, create new requirements, or make new business decisions.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent requirements, field meanings, business rules, messages, screen behavior, diagrams, or implementation details.
- Customer/domain expert answers are supplemental evidence; do not pretend they were part of the original BRD.
- Preserve source-specific terms unless `output/11_translation_policy.md` or `output/21_glossary.md` explicitly defines a normalized term.
- Mark ambiguous, missing, contradictory, or partially supported content instead of guessing.
- Internal traceability files may use internal IDs such as `REQ-xxx`, `BR-xxx`, `TERM-xxx`, `OQ-xxx`, `ANS-xxx`, `IMP-xxx`, and `QATRACE-xxx`.
- Do not modify the customer-facing FD.
- Keep all output in English.

### Strikethrough / deprecated evidence rule

- Strikethrough-only, deleted, deprecated, superseded, or draft-removed source evidence must not be treated as active FD behavior unless the source explicitly says otherwise.
- If the FD after Q&A uses strikethrough-only evidence as active behavior, mark the trace status as `Potential overstatement` or `Needs confirmation`.
- If customer/domain expert answers explicitly revive or confirm previously struck-through content, mark it as `Confirmed by customer answer` and note the source relationship clearly.

## Tasks

### Precondition

Use the latest after-QA artifacts:

- `output/70_FD_DRAFT_AFTER_QA.md` as the customer-facing FD to trace.
- `output/63_requirement_inventory_after_qa.md` as the after-QA requirement source.
- `output/64_business_rule_catalog_after_qa.md` as the after-QA business rule source.
- `output/65_open_questions_after_qa.md` as the after-QA open question source.
- `output/61_customer_answer_inventory.md` and `output/62_customer_answer_impact_analysis.md` as supplemental answer evidence.

Stop if `output/70_FD_DRAFT_AFTER_QA.md` is missing.

### Instructions

For each meaningful item in `output/70_FD_DRAFT_AFTER_QA.md`, create a trace row.

Trace these item types:

1. Functional behavior statements
2. Business rules and constraints
3. Unsupported cases and negative statements
4. Preconditions, triggers, exceptions, notes, and footnotes
5. Data items, identifiers, field names, operation names, and command options
6. Open questions and TBD items
7. Markdown image references and captions
8. Mermaid diagrams and diagram-derived behavior
9. Customer-answer-derived clarifications
10. Mixed original-source and customer-answer behavior

Do not create new FD content. Only trace existing FD content.

## Inputs

### Primary inputs

- `output/70_FD_DRAFT_AFTER_QA.md`
- `output/63_requirement_inventory_after_qa.md`
- `output/64_business_rule_catalog_after_qa.md`
- `output/65_open_questions_after_qa.md`
- `output/61_customer_answer_inventory.md`
- `output/62_customer_answer_impact_analysis.md`
- `output/60_CUSTOMER_QA.md`
- `output/21_glossary.md`

### Supporting inputs, open only when needed

- `output/20_image_analysis.md`
- `output/12_normalized_evidence.md`
- `output/11_translation_policy.md`
- `output/10_document_inventory.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`
- `working/extracted/image_inventory_raw.md`

## Outputs

### Output file to create or update

- `output/71_FD_AFTER_QA_INTERNAL_TRACEABILITY.md`

## Required output structure

Write `output/71_FD_AFTER_QA_INTERNAL_TRACEABILITY.md` using this structure:

```markdown
# FD After Q&A Internal Traceability

## 1. Traceability Decision

Decision: `Go` / `Go with minor corrections` / `No-Go`

Explain whether the FD after Q&A is traceable enough for review.

## 2. Traceability Table

| Trace ID | FD Section | FD Statement / Visual Item | Item Type | Related Requirement ID | Related Rule ID | Related Answer ID | Related Impact ID | Related Open Question ID | Related Term IDs | Source Reference | Supplemental Answer Reference | Source Image Path | Evidence Type | Confidence | Meaning Risk | Trace Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

### Field definitions

- Trace ID: Use `QATRACE-001`, `QATRACE-002`, etc.
- FD Section: section number/title in `output/70_FD_DRAFT_AFTER_QA.md`.
- FD Statement / Visual Item: concise copy or summary of the FD statement, image, Mermaid diagram, caption, or open question.
- Item Type:
  - Text statement
  - Business rule
  - Unsupported case
  - Data item
  - Open question
  - Embedded source image
  - Mermaid flowchart
  - Mermaid sequence diagram
  - Mermaid state diagram
  - Customer-answer-derived behavior
  - Figure-derived scenario
  - Mixed evidence behavior
  - Other
- Related Requirement ID: `REQ-xxx` from `output/63_requirement_inventory_after_qa.md`, if applicable.
- Related Rule ID: `BR-xxx` from `output/64_business_rule_catalog_after_qa.md`, if applicable.
- Related Answer ID: `ANS-xxx` from `output/61_customer_answer_inventory.md`, if applicable.
- Related Impact ID: `IMP-xxx` from `output/62_customer_answer_impact_analysis.md`, if applicable.
- Related Open Question ID: `OQ-xxx` from `output/65_open_questions_after_qa.md`, if applicable.
- Related Term IDs: `TERM-xxx` from `output/21_glossary.md`, if applicable.
- Source Reference: original source section, paragraph, table, note, footnote, figure, or normalized evidence reference.
- Supplemental Answer Reference: customer/domain expert answer reference, if applicable; otherwise `N/A`.
- Source Image Path: extracted source image path if the FD item uses or derives from an embedded source image; otherwise `N/A`.
- Evidence Type:
  - Confirmed by original text
  - Confirmed by original table
  - Confirmed by original figure
  - Inferred from original figure
  - Confirmed by customer answer
  - Mixed original + customer answer
  - Open question
  - Untraced
- Confidence: High / Medium / Low.
- Meaning Risk: None / Low / Medium / High.
- Trace Status:
  - Traced
  - Partially traced
  - Untraced
  - Needs confirmation
  - Potential overstatement
  - Customer-confirmed

Continue with these sections:

```markdown
## 3. Coverage Summary

| Metric | Count / Result | Notes |
|---|---:|---|
| Total FD statements/items reviewed | ... | ... |
| Traced items | ... | ... |
| Partially traced items | ... | ... |
| Untraced items | ... | ... |
| Customer-answer-derived items | ... | ... |
| Mixed original + customer answer items | ... | ... |
| Potential overstatements | ... | ... |
| Items needing confirmation | ... | ... |
| Open questions carried into FD | ... | ... |
| Visual items traced | ... | ... |
| Mermaid diagrams traced | ... | ... |

## 4. Customer Answer Coverage

| Answer ID | Used in FD? | FD Location | How Used | Evidence Type | Risk | Notes |
|---|---|---|---|---|---|---|

## 5. Requirement and Rule Coverage After Q&A

| Source Item ID | Source Item Type | Coverage Status | FD Location | Trace ID | Notes |
|---|---|---|---|---|---|

Coverage Status must be one of:

- Covered
- Partially covered
- Missing
- Converted to Open Question
- Not applicable

## 6. Open Question Coverage

| Open Question ID | FD Representation | Status | Trace ID | Notes |
|---|---|---|---|---|

Status must be one of:

- Included
- Missing
- Closed by customer answer
- Still open
- Incorrectly converted to confirmed behavior
- Not applicable

## 7. Visual Traceability Summary

| Visual / Diagram Reference | FD Location | Source Evidence | Evidence Type | Trace Status | Risk | Recommendation |
|---|---|---|---|---|---|---|

## 8. Remaining Risk Summary

List:

- Customer answers not reflected
- Customer answers over-applied
- Remaining contradictions
- Remaining open questions
- Untraced FD content
- Potential overstatements
- Visual traceability risks
- Strikethrough/deprecated evidence risks

## 9. Go / No-Go Recommendation

Provide one of:

- `Go`
- `Go with minor corrections`
- `No-Go`

Explain the reason and required next action.
```

## Required output quality

- Every major FD behavior must have a trace row.
- Every business rule must have a trace row.
- Every unsupported case must have a trace row.
- Every open question must have a trace row.
- Every customer-answer-derived statement must reference an `ANS-xxx` or `IMP-xxx` where applicable.
- Every visual item and Mermaid diagram must have a trace row.
- Do not use generic domain knowledge to trace FD content.
- Do not hide untraced content.
- Do not require internal IDs to appear in the customer-facing FD.

## Stop conditions

- Stop and report `No-Go` if `output/70_FD_DRAFT_AFTER_QA.md` is missing.
- Stop and report `No-Go` if required after-QA artifacts `63/64/65` are missing.
- Stop and report `No-Go` if customer-answer-derived FD content cannot be traced to `61` or `62`.
- Do not continue to downstream review if traceability cannot be established for major FD behavior.
