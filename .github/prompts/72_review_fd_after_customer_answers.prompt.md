# 72 - Review FD After Customer Answers

## Purpose

Review the customer-facing Functional Design generated after customer/domain expert answers and its internal traceability before final human/domain expert review.

This review verifies that:

1. The FD after Q&A is customer-facing clean.
2. Customer/domain expert answers were applied correctly and not over-applied.
3. Original source evidence and supplemental answers are represented separately and safely.
4. Unresolved items remain as Open Questions.
5. All meaningful FD content is traceable through `output/71_FD_AFTER_QA_INTERNAL_TRACEABILITY.md`.

This task must not rewrite the FD, generate DD, add new requirements, or invent missing evidence.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent requirements, field meanings, business rules, messages, screen behavior, diagrams, or implementation details.
- Customer/domain expert answers are supplemental evidence; do not pretend they were part of the original BRD.
- Keep customer-facing content free from internal pipeline terms and internal IDs.
- Internal review reports may use internal IDs.
- Mark ambiguous, missing, contradictory, or partially supported content instead of guessing.
- Keep all output in English.

### Strikethrough / deprecated evidence rule

- Strikethrough-only, deleted, deprecated, superseded, or draft-removed source evidence must not be treated as active FD behavior unless the source or customer/domain expert answer explicitly confirms it.
- If the FD after Q&A uses strikethrough-only evidence as active behavior without confirmation, treat it as a Major or Critical issue depending on impact.

## Tasks

### Precondition

Use these latest after-QA artifacts:

- `output/70_FD_DRAFT_AFTER_QA.md` as the customer-facing FD under review.
- `output/71_FD_AFTER_QA_INTERNAL_TRACEABILITY.md` as the internal traceability evidence.
- `output/63_requirement_inventory_after_qa.md`, `output/64_business_rule_catalog_after_qa.md`, and `output/65_open_questions_after_qa.md` as the after-QA source-of-truth artifacts.
- `output/61_customer_answer_inventory.md` and `output/62_customer_answer_impact_analysis.md` as supplemental answer evidence.

Stop if `output/70_FD_DRAFT_AFTER_QA.md` or `output/71_FD_AFTER_QA_INTERNAL_TRACEABILITY.md` is missing.

### Review scope

Review these layers separately:

#### Layer 1: Customer answer application

Check whether customer/domain expert answers were applied correctly:

- Answers are applied only to relevant FD content.
- Answers are not over-applied to unrelated requirements/rules.
- Partial answers remain partially open.
- Unclear answers remain Open Questions.
- Contradictions are not hidden.
- Supplemental answers are not presented as original BRD text.

#### Layer 2: Customer-facing cleanliness

Check `output/70_FD_DRAFT_AFTER_QA.md` for:

- Professional Functional Design structure
- Clear English and technical readability
- No visible internal pipeline artifacts
- No exposed internal IDs
- No references to internal files
- No mentions of requirement inventory, business rule catalog, glossary, image analysis, translation review, impact analysis, traceability, prompts, AI, or intermediate artifacts
- Proper use of `TBD` and `Requires confirmation`
- Proper treatment of unsupported behavior
- Proper treatment of figure-derived behavior
- Proper handling of customer-answer-derived behavior
- Proper Markdown image references and Mermaid diagrams

#### Layer 3: Evidence and traceability quality

Check `output/71_FD_AFTER_QA_INTERNAL_TRACEABILITY.md` against:

- `output/63_requirement_inventory_after_qa.md`
- `output/64_business_rule_catalog_after_qa.md`
- `output/65_open_questions_after_qa.md`
- `output/61_customer_answer_inventory.md`
- `output/62_customer_answer_impact_analysis.md`
- `output/21_glossary.md`
- `output/20_image_analysis.md`
- `output/12_normalized_evidence.md`

Find:

- FD statements without traceability
- FD statements partially traced
- FD statements stronger than source evidence or customer answer evidence
- FD statements created from assumptions
- Customer answers incorrectly applied
- Customer answers missing from the FD when they should be reflected
- Original source contradictions hidden or incorrectly resolved
- Business rules missing from FD
- Unsupported cases missing from FD
- Open questions missing from FD
- Glossary-controlled terms misused in FD

#### Layer 4: Visual evidence quality

Check visual content in `output/70_FD_DRAFT_AFTER_QA.md`:

- Markdown image references
- Mermaid flowcharts
- Mermaid sequence diagrams
- Mermaid state diagrams
- Visual captions and visual notes

Find:

- Missing or broken image paths
- Decorative images without requirement value
- Mermaid diagrams with unsupported nodes, states, actors, timing, or transitions
- Figure-derived behavior overstated as confirmed text/customer-confirmed behavior
- Visuals that duplicate text without adding clarity
- Relevant source diagrams omitted without reason
- Diagram ambiguity not carried into Open Questions

## Inputs

### Primary inputs

- `output/70_FD_DRAFT_AFTER_QA.md`
- `output/71_FD_AFTER_QA_INTERNAL_TRACEABILITY.md`
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

- `output/72_FD_AFTER_QA_REVIEW_REPORT.md`

## Required output structure

Write `output/72_FD_AFTER_QA_REVIEW_REPORT.md` using this structure:

```markdown
# FD After Q&A Review Report

## 1. Executive Review Summary

Include:

- Overall recommendation: `Go`, `Go with minor corrections`, or `No-Go`
- Main reason
- Main risks
- Whether customer answers were applied correctly
- Whether customer-facing cleanliness is acceptable
- Whether traceability is sufficient
- Whether unresolved ambiguity is correctly represented

## 2. Customer Answer Application Review

| Answer ID | Application Status | FD Location | Issue | Risk | Recommendation |
|---|---|---|---|---|---|
```

Application Status must be one of:

- Correctly applied
- Partially applied
- Not applied
- Over-applied
- Incorrectly applied
- Converted to Open Question
- Not applicable

Continue with these sections:

```markdown
## 3. Customer-Facing Cleanliness Review

| Check Item | Result | Evidence / Location | Recommendation |
|---|---|---|---|

## 4. Critical Issues

| Issue ID | Issue | Location | Evidence | Impact | Recommended Fix |
|---|---|---|---|---|---|
```

If none, write: `No critical issues found.`

```markdown
## 5. Major Issues

| Issue ID | Issue | Location | Evidence | Impact | Recommended Fix |
|---|---|---|---|---|---|
```

If none, write: `No major issues found.`

```markdown
## 6. Minor Issues

| Issue ID | Issue | Location | Evidence | Impact | Recommended Fix |
|---|---|---|---|---|---|
```

If none, write: `No minor issues found.`

```markdown
## 7. Traceability Review

| Trace Check | Result | Count / Details | Recommendation |
|---|---|---|---|
```

Check:

- Total FD statements reviewed
- Traced statements
- Partially traced statements
- Untraced statements
- Customer-answer-derived statements
- Mixed original + customer answer statements
- Potential overstatements
- Visual items traced
- Open questions carried into FD

```markdown
## 8. Requirement and Rule Coverage After Q&A

| Source Item | Coverage Status | FD Location | Issue | Recommendation |
|---|---|---|---|---|
```

Coverage Status must be one of:

- Covered
- Partially covered
- Missing
- Converted to Open Question
- Not applicable

```markdown
## 9. Open Questions Review

| Open Question Source | FD Representation | Status | Recommendation |
|---|---|---|---|
```

Status must be one of:

- Included
- Missing
- Incorrectly converted to assumption
- Incorrectly converted to confirmed behavior
- Closed by customer answer
- Still open
- Not applicable

```markdown
## 10. Terminology Review

| Term | FD Usage | Expected Usage | Risk | Recommendation |
|---|---|---|---|---|

## 11. Visual Evidence Review

| Visual / Diagram Reference | FD Usage | Evidence Type | Source Image Path | Risk | Recommendation |
|---|---|---|---|---|---|

## 12. Recommended Corrections

| Correction ID | Target File | Target Section | Current Text / Issue | Recommended Change | Priority |
|---|---|---|---|---|---|
```

Target File should be one of:

- `output/70_FD_DRAFT_AFTER_QA.md`
- `output/71_FD_AFTER_QA_INTERNAL_TRACEABILITY.md`
- `output/63_requirement_inventory_after_qa.md`
- `output/64_business_rule_catalog_after_qa.md`
- `output/65_open_questions_after_qa.md`
- `output/21_glossary.md`
- `output/20_image_analysis.md`

Priority: Critical / High / Medium / Low.

```markdown
## 13. Final Go / No-Go Recommendation

Decision: `Go` / `Go with minor corrections` / `No-Go`

Include:

- Reason
- Required action before customer/domain expert review
- Whether additional customer/domain expert Q&A is recommended
```

## Decision criteria

- Use `Go` only if the FD is customer-facing clean, traceable, customer answers are correctly applied, unresolved ambiguity is captured, and visual content is supported.
- Use `Go with minor corrections` for minor wording/formatting issues only.
- Use `No-Go` if the FD contains untraced behavior, exposed internal artifacts, over-applied customer answers, hidden contradictions, unsupported assumptions, unsupported visuals, or strikethrough/deprecated evidence used as active behavior.

## Required output quality

- Do not rewrite the FD in this task.
- Do not generate DD.
- Do not add new requirements.
- Do not invent missing evidence.
- Do not require internal IDs to appear in the customer-facing FD.
- Use internal IDs only in this review report.
- Be strict about hallucination, traceability, unsupported behavior, exposed internal artifacts, over-applied customer answers, and unsupported visuals.

## Stop conditions

- Stop and report `No-Go` if `output/70_FD_DRAFT_AFTER_QA.md` is missing.
- Stop and report `No-Go` if `output/71_FD_AFTER_QA_INTERNAL_TRACEABILITY.md` is missing.
- Stop and report `No-Go` if required after-QA artifacts `63/64/65` are missing.
- Do not approve the FD if customer-answer-derived behavior is not traceable to `61` or `62`.
