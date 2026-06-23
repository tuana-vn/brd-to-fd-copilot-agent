# 62 - Analyze Customer Answer Impact

## Purpose

Analyze how normalized customer/domain expert answers affect terminology, requirements, business rules, open questions, FD content, visual interpretation, and traceability.

This task only determines impact and recommends the next rerun/update path. It must not directly update requirements, business rules, glossary, FD, or traceability.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Treat customer answers as supplemental evidence, not original BRD evidence.
- Do not invent changes not supported by customer answers.
- Do not automatically apply customer answers to unrelated requirements or rules.
- Do not silently override BRD/source evidence. If an answer contradicts the source, mark the contradiction and recommend human/domain decision.
- Preserve product-specific terms, command names, option names, field names, acronyms, and code-like identifiers exactly.
- Follow `output/21_glossary.md` and `output/11_translation_policy.md`.
- Respect strikethrough/deprecated evidence rules from the pipeline:
  - strikethrough-only source evidence must not be treated as active behavior unless explicitly re-confirmed by customer/domain expert.
  - if customer answers reactivate, reject, or clarify strikethrough/deprecated content, mark it as a high-attention impact.
- Internal IDs may be used in this analysis for traceability.
- Write outputs in English unless source values must remain unchanged.

## Tasks

### Precondition

Use `output/61_customer_answer_inventory.md` as the normalized answer source.

Use the latest available FD/review context in this order:

1. `output/55_FD_PATCHED_REVIEW_REPORT.md`, if available
2. `output/52_FD_REVISED_REVIEW_REPORT.md`, if available
3. `output/42_FD_REVIEW_REPORT.md`, if available

Use the latest available customer-facing FD in this order:

1. `output/53_FD_DRAFT_REVISED_PATCHED.md`, if available
2. `output/50_FD_DRAFT_REVISED.md`, if available
3. `output/40_FD_DRAFT.md`, if available

Use the latest available traceability in this order:

1. `output/54_FD_PATCHED_INTERNAL_TRACEABILITY.md`, if available
2. `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md`, if available
3. `output/41_FD_INTERNAL_TRACEABILITY.md`, if available

### Instructions

For each normalized customer answer:

1. Identify the affected source-derived item(s):
   - glossary term(s)
   - requirement(s)
   - business rule(s)
   - open question(s)
   - image/diagram interpretation
   - FD section(s)
   - traceability row(s)
2. Classify the impact type.
3. Determine whether the answer confirms, clarifies, supplements, contradicts, or fails to answer the source ambiguity.
4. Determine required action.
5. Recommend the earliest safe rerun/update step.
6. Identify risk and whether human/domain decision is required.
7. Do not directly update downstream artifacts.

## Inputs

### Primary inputs

- `output/61_customer_answer_inventory.md`
- `output/60_CUSTOMER_QA.md`
- `output/32_open_questions.md`
- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/21_glossary.md`

### Latest FD/review context, use available files

- `output/55_FD_PATCHED_REVIEW_REPORT.md`, if available
- `output/54_FD_PATCHED_INTERNAL_TRACEABILITY.md`, if available
- `output/53_FD_DRAFT_REVISED_PATCHED.md`, if available
- `output/52_FD_REVISED_REVIEW_REPORT.md`, if available
- `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md`, if available
- `output/50_FD_DRAFT_REVISED.md`, if available
- `output/42_FD_REVIEW_REPORT.md`, if available
- `output/41_FD_INTERNAL_TRACEABILITY.md`, if available
- `output/40_FD_DRAFT.md`, if available

### Supporting inputs, open only when needed

- `output/20_image_analysis.md`
- `output/12_normalized_evidence.md`
- `output/11_translation_policy.md`
- `output/10_document_inventory.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`

## Outputs

### Output file to create or update

Create:

- `output/62_customer_answer_impact_analysis.md`

## Required output structure

Write `output/62_customer_answer_impact_analysis.md` using this structure:

```markdown
# Customer Answer Impact Analysis

## 1. Impact Analysis Decision

Decision: `Proceed to requirement updates` / `Proceed to FD update only` / `Generate follow-up Q&A` / `Stop for human decision` / `No action required`

Explain the decision briefly.

## 2. Impact Table

| Impact ID | Answer ID | Related QID | Impact Type | Impact Description | Affected Artifact | Affected Item | Source Relationship | Required Action | Rerun From Step | Risk | Human Decision Needed? | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 3. Recommended Next Step

Choose one:

- Proceed to `63_update_requirements_from_customer_answers`
- Proceed directly to `70_generate_fd_after_customer_answers`
- Generate follow-up Q&A
- Stop for human decision
- No action required

Explain why.

## 4. Rerun / Update Path

| Path ID | Condition | Steps to Run | Reason |
|---|---|---|---|

## 5. Impact Summary

Include:

- Number of terminology impacts
- Number of requirement impacts
- Number of business rule impacts
- Number of open question closures
- Number of new open questions
- Number of FD-only impacts
- Number of diagram/visual impacts
- Number of contradictions
- Number of unresolved items
- Number of impacts requiring human/domain decision

## 6. Contradictions and Decision Notes

| Impact ID | Contradiction / Decision Point | Source Evidence | Customer Answer | Recommended Handling |
|---|---|---|---|---|

## 7. Follow-up Q&A Candidates

| Follow-up ID | Related Answer ID | Question | Reason | Priority |
|---|---|---|---|---|
```

## Field definitions

- Impact ID: Use `IMP-001`, `IMP-002`, etc.
- Answer ID: `ANS-xxx` from `output/61_customer_answer_inventory.md`.
- Related QID: Customer-facing QID from `output/60_CUSTOMER_QA.md`, if available.
- Impact Type must be one of:
  - Terminology update
  - Requirement update
  - Business rule update
  - Open question closure
  - New open question
  - FD wording update only
  - Diagram interpretation update
  - Data definition update
  - Error / warning handling update
  - Non-functional / performance update
  - Traceability update
  - Source contradiction
  - No impact
- Affected Artifact must be one of:
  - Glossary
  - Requirement inventory
  - Business rule catalog
  - Open questions
  - Image analysis
  - FD
  - Traceability
  - Multiple
  - None
- Source Relationship must be one of:
  - Supplements source
  - Confirms source
  - Clarifies source
  - Overrides previous assumption
  - Contradicts source
  - Not enough information
  - Not applicable
- Required Action must be one of:
  - Update glossary
  - Update requirements
  - Update business rules
  - Close open question
  - Add open question
  - Update image analysis
  - Update FD only
  - Update traceability
  - Generate follow-up Q&A
  - Human decision required
  - No action
- Rerun From Step must be one of:
  - `21`
  - `30`
  - `63`
  - `70`
  - `60`
  - `No rerun`
- Risk: None / Low / Medium / High.
- Human Decision Needed?: Yes / No.

## Rerun guidance

- If an answer changes terminology only and does not affect behavior, recommend rerun from `21`, then downstream affected steps as needed.
- If an answer changes terminology that affects behavior, recommend `63_update_requirements_from_customer_answers`, then `70_generate_fd_after_customer_answers`.
- If an answer changes business behavior, requirement behavior, unsupported behavior, validation, data definition, error/warning handling, or testability, recommend `63_update_requirements_from_customer_answers`, then `70_generate_fd_after_customer_answers`.
- If an answer closes an open question but does not change requirement/rule behavior, recommend `70_generate_fd_after_customer_answers` unless the open question closure must update `30/31/32`.
- If an answer only affects FD wording and all source-derived artifacts remain valid, recommend `70_generate_fd_after_customer_answers`.
- If an answer is unclear or partial and blocks safe update, recommend `Generate follow-up Q&A`.
- If an answer contradicts source evidence, recommend `Stop for human decision` unless project rules say customer answers override the BRD.
- If no answer affects terminology, requirements, rules, FD, or open questions, recommend `No action required`.

## Quality rules

- Do not generate requirements.
- Do not generate business rules.
- Do not update FD content.
- Do not update traceability.
- Do not invent changes not supported by customer answers.
- Do not automatically treat customer answers as if they were in the original BRD.
- Do not hide contradictions; mark them explicitly.
- Do not recommend rerunning from an earlier step than necessary.
- Do not recommend step `40`, `50`, or `53` as the main update route after customer answers; use `70` for FD generation after customer answers.
- Do not use generic domain knowledge to fill gaps in customer answers.
- If a customer answer is narrow, keep the impact narrow.

## Stop conditions

- Stop and report `No-Go` if `output/61_customer_answer_inventory.md` is missing.
- Stop and report `No-Go` if `output/60_CUSTOMER_QA.md` is missing.
- Stop and report `No-Go` if required source-of-truth artifacts `output/30_requirement_inventory.md`, `output/31_business_rule_catalog.md`, or `output/32_open_questions.md` are missing.
- Do not continue to requirement update or FD update from customer answers without creating `output/62_customer_answer_impact_analysis.md`.
