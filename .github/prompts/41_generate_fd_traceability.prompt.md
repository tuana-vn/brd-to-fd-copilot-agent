# 41 - Generate FD Internal Traceability

## Purpose

Create an internal traceability file that maps the customer-facing Functional Design draft back to the source-bound evidence produced by the BRD-to-FD pipeline.

This task is for internal review only. It must not modify the customer-facing FD and must not introduce new FD behavior.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent requirements, business rules, validations, command behavior, UI/API behavior, diagrams, or design decisions.
- Do not rewrite `output/40_FD_DRAFT.md`.
- Do not create new requirements or business rules.
- Do not hide untraced FD statements, visual items, Mermaid diagrams, assumptions, TBDs, or open questions.
- Internal IDs are allowed in this traceability file.
- Customer-facing content cleanliness is reviewed later in step 42.
- Preserve source-specific terms unless `output/11_translation_policy.md` or `output/21_glossary.md` explicitly defines a normalized rendering.
- Preserve command names, option names, parameters, field names, product terms, acronyms, state names, and code-like identifiers exactly.
- Respect strikethrough rules from the pipeline:
  - Strikethrough-only content is inactive / deleted / deprecated / superseded evidence by default.
  - Do not trace active FD behavior to strikethrough-only evidence unless the source explicitly says the strikethrough content remains active.
  - If FD behavior appears to depend on strikethrough-only evidence, mark the trace status as `Potential overstatement` or `Needs confirmation`.
- Write the output in English.

## Tasks

### Precondition

Use the latest effective upstream gates:

- Translation gate:
  - If `output/15_translation_review_followup_report.md` exists, use it as the latest translation gate.
  - Otherwise, use `output/13_translation_review_report.md`.
- Feature understanding gate:
  - Use `output/34_FEATURE_UNDERSTANDING_REVIEW.md` if it exists.

Continue only if the latest applicable gates are `Go`, `Go with warnings`, or `Go with minor notes`.

Stop if any latest applicable gate is `No-Go`.

If a gate is `Fix required`, continue only if the FD draft explicitly reflects the required fixes; otherwise mark the traceability recommendation as `No-Go`.

### Instructions

For each meaningful item in `output/40_FD_DRAFT.md`, create a trace row. Meaningful items include:

1. Scope statements.
2. Out-of-scope statements.
3. Functional behavior.
4. Main flow steps.
5. Alternative or exception behavior.
6. Business rules and constraints.
7. Unsupported cases.
8. Data items.
9. Error, warning, or status handling.
10. Data mapping or naming rules.
11. Assumptions.
12. Open questions.
13. Embedded Markdown image references.
14. Mermaid diagrams.
15. Figure-derived scenarios.
16. Source notes that may affect interpretation.

For each item:

1. Identify the related requirement, business rule, glossary term, open question, figure/image evidence, and normalized evidence source.
2. Classify the evidence type.
3. Determine trace confidence and meaning risk.
4. Mark unsupported, partially supported, overstated, or uncertain content clearly.
5. Do not fix the FD in this step. Provide traceability notes only.

## Inputs

### Primary inputs

- `output/40_FD_DRAFT.md`
- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`
- `output/21_glossary.md`
- `output/20_image_analysis.md`
- `output/12_normalized_evidence.md`

### Gate / context inputs

- `output/13_translation_review_report.md`
- `output/15_translation_review_followup_report.md` if available
- `output/34_FEATURE_UNDERSTANDING_REVIEW.md` if available
- `output/33_FEATURE_UNDERSTANDING_BRIEF.md` if available

### Supporting inputs, open only when needed

- `output/11_translation_policy.md`
- `output/10_document_inventory.md`
- `working/extracted/image_inventory_raw.md`
- `working/extracted/formatting_inventory.md` if available
- `working/extracted/document_text.md`
- `working/extracted/tables.md`

## Outputs

### Output file to create or update

Create or overwrite:

- `output/41_FD_INTERNAL_TRACEABILITY.md`

## Required output structure

Write `output/41_FD_INTERNAL_TRACEABILITY.md` using this structure:

```markdown
# FD Internal Traceability

## 1. Traceability Decision

Decision: `Go` / `Go with minor corrections` / `No-Go`

Explain whether the FD draft is sufficiently traceable for review.

## 2. Input Gate Summary

| Gate | Source File | Decision | Notes |
|---|---|---|---|
| Translation gate | ... | ... | ... |
| Feature understanding gate | ... | ... | ... |

## 3. FD Traceability Matrix

| Trace ID | FD Section | FD Statement / Visual Item | Item Type | Internal Requirement ID | Internal Rule ID | Internal Term IDs | Internal Open Question IDs | Source Reference | Source Image Path | Evidence Type | Confidence | Meaning Risk | Trace Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 4. Coverage Summary

| Metric | Count | Notes |
|---|---:|---|
| Total FD statements/items reviewed | ... | ... |
| Traced items | ... | ... |
| Partially traced items | ... | ... |
| Untraced items | ... | ... |
| Potential overstatements | ... | ... |
| Items needing confirmation | ... | ... |
| Embedded source images included | ... | ... |
| Mermaid diagrams included | ... | ... |
| Visual items based on figure-only evidence | ... | ... |
| Open questions carried into the FD | ... | ... |
| Items affected by strikethrough/deprecated evidence | ... | ... |

## 5. Visual Coverage Summary

| Visual Item | FD Location | Source Evidence | Trace Status | Risk | Recommendation |
|---|---|---|---|---|---|

## 6. Strikethrough / Deprecated Evidence Check

| FD Item | Related Source Evidence | Issue | Risk | Recommendation |
|---|---|---|---|---|

## 7. Risk Summary

List:

- FD statements with Low confidence.
- FD statements with Medium or High meaning risk.
- FD statements based only on figure inference.
- FD statements that may be stronger than source evidence.
- FD statements requiring customer/domain expert confirmation.
- Visual items with weak or missing traceability.
- Mermaid diagrams that may overstate source behavior.
- Any item possibly based on strikethrough-only evidence.

## 8. Traceability Findings

List actionable findings:

| Finding ID | Area | Finding | Severity | Recommended Action |
|---|---|---|---|---|

Severity must be one of:

- `Critical`
- `Major`
- `Minor`
- `Info`

## 9. Go / No-Go Recommendation

Provide one of:

- `Go`: FD is internally traceable and ready for step 42 review.
- `Go with minor corrections`: FD is mostly traceable, but minor cleanup is needed.
- `No-Go`: FD contains untraced, overstated, or risky content that must be corrected before review.
```

## Field definitions

For the traceability matrix:

- Trace ID: Use `TRACE-001`, `TRACE-002`, etc.
- FD Section: Section number/title in `output/40_FD_DRAFT.md`.
- FD Statement / Visual Item: Concise copy or summary of the FD statement, embedded image, Mermaid diagram, visual caption, or source note.
- Item Type must be one of:
  - Text statement
  - Business rule
  - Unsupported case
  - Data item
  - Open question
  - Assumption
  - Embedded source image
  - Mermaid flowchart
  - Mermaid sequence diagram
  - Mermaid state diagram
  - Figure-derived scenario
  - Source note
  - Other
- Internal Requirement ID: Related `REQ-xxx`, or `N/A`.
- Internal Rule ID: Related `BR-xxx`, or `N/A`.
- Internal Term IDs: Related `TERM-xxx`, or `N/A`.
- Internal Open Question IDs: Related `OQ-xxx`, or `N/A`.
- Source Reference: Original source paragraph, table, note, footnote, figure, normalized evidence reference, or `N/A`.
- Source Image Path: Extracted image path if the FD item uses or derives from an embedded DOCX image; otherwise `N/A`.
- Evidence Type must be one of:
  - Confirmed by text
  - Confirmed by table
  - Confirmed by figure
  - Inferred from figure
  - Mixed evidence
  - Open question
  - Manual text evidence
  - Deprecated / strikethrough evidence
  - Untraced
- Confidence: High / Medium / Low.
- Meaning Risk: None / Low / Medium / High.
- Trace Status must be one of:
  - Traced
  - Partially traced
  - Untraced
  - Needs confirmation
  - Potential overstatement

## Evidence priority

Use this priority order when tracing FD content:

1. `output/30_requirement_inventory.md`
2. `output/31_business_rule_catalog.md`
3. `output/32_open_questions.md`
4. `output/21_glossary.md`
5. `output/20_image_analysis.md`
6. `output/12_normalized_evidence.md`
7. `output/35_manual_text_evidence_analysis.md`, if available, as supplemental focused evidence only
8. `output/10_document_inventory.md` and raw extracted files only for targeted verification

Do not use generic domain knowledge to trace FD content.

## Visual traceability rules

- Trace every Markdown image reference in the FD.
- Trace every Mermaid diagram in the FD.
- Trace every customer-facing figure caption in the FD.
- Confirm that each embedded image path exists in image inventory or image analysis evidence.
- Confirm that each Mermaid node, step, state, actor, transition, or timing element is source-supported.
- If a Mermaid diagram simplifies a source figure, mark it as `Mixed evidence` or `Inferred from figure` as appropriate.
- If a visual is included only for decoration, mark it as `Untraced` and recommend removal.
- If the FD uses manual pasted text evidence, mark the item as supplemental and verify it against normalized evidence when possible.

## Quality rules

- Keep the output concise, technical, and English-only.
- Internal IDs are allowed here.
- Make coverage gaps visible.
- Do not edit the customer-facing FD in this phase.
- Do not create new requirements or business rules.
- Do not hide assumptions, TBDs, or open questions.
- Do not trace active FD behavior to strikethrough-only evidence unless explicitly supported by active source text.

## Stop conditions

- Stop and report `No-Go` if `output/40_FD_DRAFT.md` is missing.
- Stop and report `No-Go` if `output/30_requirement_inventory.md` or `output/31_business_rule_catalog.md` is missing.
- Stop and report `No-Go` if the latest applicable upstream gate is `No-Go`.
- Do not stop only because some FD items are partially traceable; instead, mark them and recommend corrections.
- Do not continue to downstream DD/coding phases from this task.
