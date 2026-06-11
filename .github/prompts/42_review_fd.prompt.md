# 42 - Review Customer-facing FD

## Purpose

Review the customer-facing Functional Design draft before it is considered usable for customer review.

This task checks whether `output/40_FD_DRAFT.md` is clean, source-bound, traceable, customer-readable, and safe to send for review.

This is a quality gate. It must not rewrite the FD and must not introduce new FD behavior.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not modify `output/40_FD_DRAFT.md`.
- Do not create new requirements, business rules, validations, diagrams, UI/API behavior, or design decisions.
- Do not approve the FD if it contains unsupported, overstated, untraced, or customer-confusing content.
- Do not require DD-level or coding-level detail unless the FD claims such detail.
- Keep the review report internal.
- Internal IDs are allowed in the review report.
- Customer-facing FD content must not expose internal IDs, internal artifact names, prompt/pipeline terms, traceability labels, or AI/Copilot/model references.
- Preserve source-specific terms unless `output/11_translation_policy.md` or `output/21_glossary.md` explicitly defines a normalized rendering.
- Respect strikethrough rules from the pipeline:
  - Strikethrough-only content must not appear as active FD behavior unless explicitly confirmed by active source evidence.
  - If the FD uses strikethrough-only content as active behavior, treat it as a Major or Critical finding.
- Write the output in English.

## Tasks

### Precondition

Use the latest effective upstream gates:

- Translation gate:
  - If `output/15_translation_review_followup_report.md` exists, use it as the latest translation gate.
  - Otherwise, use `output/13_translation_review_report.md`.
- Feature understanding gate:
  - Use `output/34_FEATURE_UNDERSTANDING_REVIEW.md` if it exists.
- FD traceability gate:
  - Use `output/41_FD_INTERNAL_TRACEABILITY.md` if it exists.

Continue only if the latest applicable gates are `Go`, `Go with warnings`, `Go with minor notes`, or `Go with minor corrections`.

Stop if any latest applicable gate is `No-Go`.

If step 41 is missing, continue the review but mark traceability confidence as Low and add a Major finding recommending step 41 execution.

### Instructions

Review `output/40_FD_DRAFT.md` against source-bound evidence and traceability artifacts.

Evaluate:

1. Customer-facing cleanliness.
2. Evidence alignment.
3. Coverage of requirements and rules.
4. Preservation of unsupported cases, negative statements, conditions, exceptions, notes, and footnotes.
5. Correct use of terminology.
6. Correct handling of open questions, TBDs, and uncertainty.
7. Correct use of visuals and Mermaid diagrams.
8. Absence of unsupported assumptions and generic domain knowledge.
9. Absence of internal IDs and pipeline artifact names in customer-facing text.
10. Absence of active behavior derived from strikethrough-only evidence.

Do not rewrite the FD. Provide findings and recommended corrections only.

## Inputs

### Primary inputs

- `output/40_FD_DRAFT.md`
- `output/41_FD_INTERNAL_TRACEABILITY.md` if available
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

- `output/35_manual_text_evidence_analysis.md` if available
- `output/11_translation_policy.md`
- `output/10_document_inventory.md`
- `working/extracted/image_inventory_raw.md`
- `working/extracted/formatting_inventory.md` if available
- `working/extracted/document_text.md`
- `working/extracted/tables.md`

## Outputs

### Output file to create or update

Create or overwrite:

- `output/42_FD_REVIEW_REPORT.md`

## Required output structure

Write `output/42_FD_REVIEW_REPORT.md` using this structure:

```markdown
# FD Review Report

## 1. Review Decision

Decision: `Go` / `Go with minor corrections` / `Fix required` / `No-Go`

Explain the decision briefly.

## 2. Gate Summary

| Gate | Source File | Decision | Notes |
|---|---|---|---|
| Translation gate | ... | ... | ... |
| Feature understanding gate | ... | ... | ... |
| FD traceability gate | ... | ... | ... |

## 3. Executive Review Summary

Summarize whether the FD is suitable for customer review.

## 4. Customer-facing Cleanliness Review

| Finding ID | FD Section | Issue | Severity | Recommended Action |
|---|---|---|---|---|

Check for:

- Internal IDs such as `REQ-xxx`, `BR-xxx`, `TERM-xxx`, `OQ-xxx`, `FIG-xxx`, `TRACE-xxx`.
- Internal artifact names such as requirement inventory, business rule catalog, glossary, image analysis, normalized evidence, translation review, traceability file, prompt, pipeline, Copilot, AI, or model.
- Internal notes that should not be customer-facing.

## 5. Evidence Alignment Review

| Finding ID | FD Section | Claim / Content | Evidence Status | Severity | Recommended Action |
|---|---|---|---|---|---|

Evidence Status must be one of:

- Supported
- Partially supported
- Unsupported
- Potential overstatement
- Needs confirmation
- Open question

## 6. Requirement and Rule Coverage Review

| Finding ID | Area | Coverage Issue | Related Internal ID | Severity | Recommended Action |
|---|---|---|---|---|---|

Check whether important requirements, business rules, unsupported cases, constraints, and open questions from steps 30–32 are represented appropriately.

## 7. Terminology Review

| Finding ID | Term / Phrase | Issue | Severity | Recommended Action |
|---|---|---|---|---|

Check whether glossary-controlled terms, acronyms, field names, command names, option names, product terms, and code-like identifiers are preserved correctly.

## 8. Visual and Mermaid Review

| Finding ID | Visual / Diagram | FD Location | Issue | Severity | Recommended Action |
|---|---|---|---|---|---|

Check:

- Every Markdown image reference is source-supported and relevant.
- Every Mermaid diagram is source-supported.
- Mermaid nodes, states, actors, steps, timing, and transitions are not invented.
- Figure-only behavior is not overstated as text-confirmed behavior.
- Unreadable or ambiguous figures are marked as requiring confirmation.

## 9. Strikethrough / Deprecated Evidence Review

| Finding ID | FD Section | Issue | Severity | Recommended Action |
|---|---|---|---|---|

Check whether any active FD behavior appears to come from strikethrough-only, deleted, deprecated, or superseded evidence.

## 10. Open Questions and TBD Review

| Finding ID | FD Section | Issue | Severity | Recommended Action |
|---|---|---|---|---|

Check whether uncertainty is handled as customer-facing questions or TBDs instead of hidden assumptions.

## 11. Source-bound Completeness Review

| Finding ID | Topic | Missing / Weak Coverage | Severity | Recommended Action |
|---|---|---|---|---|

Check major source-supported topics that should be in the FD but are missing or underdeveloped.

## 12. Risk Assessment

List:

- High-risk unsupported claims.
- Potential overstatements.
- Missing important unsupported cases or exceptions.
- Visual interpretation risks.
- Terminology risks.
- Traceability gaps.
- Customer-confirmation risks.

## 13. Required Corrections

List must-fix corrections before the FD can be used for customer review.

## 14. Optional Improvements

List nice-to-have improvements.

## 15. Final Recommendation

Provide one of:

- `Go`: FD is clean, source-bound, and ready for customer review.
- `Go with minor corrections`: FD is usable after minor cleanup.
- `Fix required`: FD has fixable issues that should be corrected before customer review.
- `No-Go`: FD contains serious unsupported, misleading, untraced, or customer-facing cleanliness issues.
```

## Severity guidance

Use these severity levels:

- `Critical`: Could mislead the customer or cause wrong FD/DD/coding direction.
- `Major`: Important source alignment, traceability, or clarity issue.
- `Minor`: Wording, organization, or small completeness issue.
- `Info`: Observation only.

## Review rules

- Do not rewrite the FD in this review file.
- Do not invent missing BRD content.
- Do not approve the FD if unsupported behavior is presented as fact.
- Do not approve the FD if internal pipeline artifacts or IDs are visible in customer-facing content.
- Do not require implementation design unless the FD claims implementation behavior.
- Do not penalize the FD for carrying valid open questions.
- Treat missing uncertainty handling as a finding.
- Treat active use of strikethrough-only evidence as Major or Critical.
- Keep feedback actionable.

## Evidence priority

Use this priority order when reviewing the FD:

1. `output/41_FD_INTERNAL_TRACEABILITY.md`, if available
2. `output/30_requirement_inventory.md`
3. `output/31_business_rule_catalog.md`
4. `output/32_open_questions.md`
5. `output/21_glossary.md`
6. `output/20_image_analysis.md`
7. `output/12_normalized_evidence.md`
8. `output/35_manual_text_evidence_analysis.md`, if available, as supplemental focused evidence only
9. `output/10_document_inventory.md` and raw extracted files only for targeted verification

Do not use generic domain knowledge to approve FD content.

## Quality checklist before finishing

Before completing the review report, verify:

- The decision matches the severity of findings.
- Every Critical/Major issue has a recommended action.
- The review distinguishes between missing evidence, weak writing, and legitimate open questions.
- The review does not ask the FD generator to hallucinate missing information.
- Customer-facing cleanliness was checked.
- Visual and Mermaid content was checked.
- Strikethrough/deprecated evidence handling was checked.
- The review remains a review artifact, not a rewritten FD.

## Stop conditions

- Stop and report `No-Go` if `output/40_FD_DRAFT.md` is missing.
- Stop and report `No-Go` if `output/30_requirement_inventory.md` or `output/31_business_rule_catalog.md` is missing.
- Stop and report `No-Go` if the latest applicable upstream gate is `No-Go`.
- Do not stop only because some FD items need correction; report findings and recommend a decision.
- Do not continue to FD revision, DD, or coding from this task.
