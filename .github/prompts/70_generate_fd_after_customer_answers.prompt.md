# 70 - Generate FD After Customer Answers

## Purpose

Generate a clean customer-facing Functional Design after customer/domain expert answers have been normalized, impact-analyzed, and incorporated into after-QA internal requirement artifacts.

This task creates the customer-facing FD after Q&A. It must not expose internal artifacts, internal IDs, or pipeline terminology.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Treat customer/domain expert answers as supplemental clarification evidence, not as if they were part of the original BRD.
- Do not invent requirements, field meanings, business rules, messages, screen behavior, diagrams, or design decisions.
- Preserve source-supported and customer-confirmed conditions, exceptions, negative statements, unsupported behavior, notes, and footnotes.
- Preserve command names, option names, field names, product-specific terms, acronyms, and code-like identifiers exactly.
- Follow `output/21_glossary.md` and `output/11_translation_policy.md`.
- Respect strikethrough/deprecated evidence rules:
  - strikethrough-only source content must not appear as active FD behavior unless explicitly confirmed by accepted customer answer.
- Use `TBD` when required details are missing.
- Use `Requires confirmation` when business meaning remains uncertain.
- Do not expose internal artifact names or internal IDs such as `QID`, `ANS`, `IMP`, `REQ`, `BR`, `TERM`, `OQ`, `FIG`, `TRACE`, `RTRACE`, or `PTRACE` identifiers in the customer-facing FD body.
- Write the FD in professional English.

## Tasks

### Precondition

Use the latest customer-answer impact and after-QA artifacts:

- `output/62_customer_answer_impact_analysis.md`
- `output/63_requirement_inventory_after_qa.md`
- `output/64_business_rule_catalog_after_qa.md`
- `output/65_open_questions_after_qa.md`

Continue only if one of these is true:

- step 62 recommended proceeding directly to step 70, or
- step 63 has generated the after-QA requirement/rule/open-question artifacts.

If step 62 recommends follow-up Q&A or human decision and no accepted after-QA artifacts exist, stop and report `No-Go`.

### Instructions

1. Use `63/64/65` as the primary internal source for FD content after Q&A.
2. Use `61/62/60` only to understand how customer answers were applied and to avoid overstating supplemental answers.
3. Use `21/20/12` as supporting source-bound context when needed.
4. Optionally use the latest prior FD (`53`, `50`, or `40`) as a structural reference, but do not copy unsupported or previously rejected content.
5. Generate a full customer-facing FD, not a diff.
6. Do not mention internal review reports, traceability files, requirement inventory, business rule catalog, glossary, image analysis, impact analysis, or Q&A IDs.
7. If a customer answer contradicts the original source and the contradiction remains unresolved, do not write it as confirmed behavior. Put it in Open Questions or Source/Supplemental Clarification Notes.
8. Include visual content only when source-supported or customer-confirmed and still useful to the FD.
9. Do not generate DD, implementation design, or code design.

## Inputs

### Primary inputs

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

### Optional prior FD inputs for structure only

Use the latest available prior FD as a structure/style reference only:

- `output/53_FD_DRAFT_REVISED_PATCHED.md`
- `output/50_FD_DRAFT_REVISED.md`
- `output/40_FD_DRAFT.md`

Do not copy prior FD content that was rejected, untraced, overstated, or superseded by customer answers.

## Outputs

### Output file to create or update

- `output/70_FD_DRAFT_AFTER_QA.md`

## Required output structure

Write `output/70_FD_DRAFT_AFTER_QA.md` using this structure:

```markdown
# Functional Design

## 1. Overview

Describe the function based on the provided source document and confirmed supplemental customer/domain expert answers.

## 2. Scope

Describe covered behavior.

## 3. Out of Scope

Describe unsupported or explicitly excluded behavior.

If not explicitly defined, write:
`TBD - Not explicitly defined in the source document or supplemental clarification.`

## 4. Terminology

| Term | Meaning / Usage | Note |
|---|---|---|

## 5. Business / Operation Summary

Summarize source-supported and customer-confirmed behavior.

## 6. Functional Behavior

### 6.x <Function / Operation Name>

Include:

- Purpose
- Trigger
- Preconditions
- Main behavior
- Alternative / exception behavior
- Unsupported behavior
- Notes

## 7. Business Rules and Constraints

| No. | Rule / Constraint | Condition | Expected Behavior | Notes |
|---|---|---|---|---|

## 8. Visual Overview and Scenario Diagrams

Include this section only when source-supported or customer-confirmed diagrams/images/workflows help explain behavior.

## 9. Time-Based / Scenario Flows

| Step | Timing / Event | State / Operation | Result |
|---|---|---|---|

Include only if source-supported or customer-confirmed.

## 10. Input / Output Data

| Data Item | Direction | Description | Required? | Notes |
|---|---|---|---|---|

## 11. Error / Warning / Unsupported Handling

| Case | Condition | Handling | Message / Result | Notes |
|---|---|---|---|---|

## 12. Data Mapping / Naming Rules

| Item | Rule | Source / Component | Notes |
|---|---|---|---|

Include only if source-supported or customer-confirmed.

## 13. Assumptions

| No. | Assumption | Impact |
|---|---|---|

Keep assumptions minimal. Do not present assumptions as confirmed behavior.

## 14. Open Questions

| No. | Question | Reason / Impact |
|---|---|---|

Include unresolved items from `output/65_open_questions_after_qa.md` in customer-facing wording.

## 15. Source and Supplemental Clarification Notes

Use customer-facing wording similar to:

`This Functional Design draft is based on the provided source document content, including text, tables, notes, footnotes, embedded diagrams, and supplemental customer/domain expert clarifications. Items not explicitly defined or clarified are marked as TBD or Open Question.`
```

## Visual rules

- Use Markdown image references only for relevant extracted DOCX images.
- Use Mermaid diagrams only for source-supported or customer-confirmed workflows, states, timing, or scenarios.
- Do not invent actors, states, timing, transitions, systems, or components.
- If a visual meaning is still ambiguous, mark it as `Requires confirmation` or list it in Open Questions.
- Do not include decorative or untraced visuals.
- Keep Mermaid diagrams simple and source-bound.

## Customer-facing rules

- Output must be English.
- Do not expose internal artifact names.
- Do not expose internal IDs.
- Do not mention requirement inventory, business rule catalog, glossary, image analysis, translation review, impact analysis, traceability, prompts, AI, or pipeline.
- Do not expose customer answer IDs, impact IDs, requirement IDs, rule IDs, term IDs, question IDs, figure IDs, or trace IDs.
- Use clean customer-facing numbering such as Rule 1, Step 1, Question 1.
- Do not invent business behavior.
- Do not treat unresolved contradictions as confirmed behavior.
- If customer-answer-derived behavior is included, write it naturally as clarified behavior, not as an internal answer reference.
- Preserve exact mandatory/optional meaning.
- Preserve unsupported behavior and negative statements.
- Preserve notes and footnotes that affect behavior.
- Use `TBD` or `Requires confirmation` when needed.

## Required output quality

- The FD reads like a normal Functional Design document.
- Every behavior is supported by original source evidence, customer/domain expert answer, or both.
- Every remaining ambiguity is visible in Open Questions.
- No internal IDs or internal artifact names are exposed.
- Visual content is source-supported or customer-confirmed.
- The FD does not pretend customer answers were part of the original BRD.
- The FD does not include DD, implementation design, code design, or test design unless explicitly source-supported as functional behavior.

## Stop conditions

- Stop and report `No-Go` if required after-QA artifacts `63/64/65` are missing and step 62 did not allow direct FD update.
- Stop and report `No-Go` if the FD would require unsupported assumptions.
- Stop and report `No-Go` if customer answers contradict source evidence and no accepted resolution exists.
- Stop and report `No-Go` if required customer answers are too unclear to generate a safe FD.
- Do not generate DD or code design.
