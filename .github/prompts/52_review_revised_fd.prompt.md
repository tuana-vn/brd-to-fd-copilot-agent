# 52 - Review Revised FD

## Purpose

Review the revised customer-facing Functional Design and revised internal traceability before human/domain expert review.

This review has three goals:

1. Verify that issues from the first FD review were fixed by step 50.
2. Ensure `output/50_FD_DRAFT_REVISED.md` is clean, customer-facing, and free from internal pipeline artifacts.
3. Ensure all meaningful revised FD content is supported by `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md` and source-bound evidence.

This task is a review gate. It must not rewrite the FD, generate DD, or introduce new requirements.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent requirements, field meanings, business rules, messages, screen behavior, command behavior, diagrams, or design decisions.
- Preserve source-specific terms unless `output/11_translation_policy.md` or `output/21_glossary.md` explicitly defines a controlled rendering.
- Mark ambiguous, missing, or conflicting information instead of guessing.
- Keep customer-facing content free from internal pipeline terms and internal IDs.
- Internal review and traceability files may use internal IDs.
- Write outputs in English unless the source value must remain unchanged.
- Do not modify the original BRD.
- Do not modify `output/50_FD_DRAFT_REVISED.md`.
- Do not modify `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md`.
- Customer answers or manual text evidence are supplemental evidence only.
- Respect strikethrough rules from the pipeline:
  - strikethrough-only evidence is inactive/deleted/deprecated/superseded evidence by default.
  - strikethrough-only evidence must not be treated as active FD behavior, active requirement, or active business rule unless the source explicitly says otherwise.

### Important

- `output/50_FD_DRAFT_REVISED.md` must not expose internal analysis artifacts.
- `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md` may expose internal IDs because it is for internal review only.
- The review must check both customer-facing quality and evidence traceability.
- The review must not require internal IDs to appear in the customer-facing FD.

## Tasks

### Precondition

Use the latest available FD correction and traceability artifacts:

- `output/50_FD_DRAFT_REVISED.md` is the revised customer-facing FD created by step 50.
- `output/50_FD_REVISION_LOG.md` records what step 50 changed.
- `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md` traces the revised FD.
- `output/42_FD_REVIEW_REPORT.md` is the first FD review report that step 50 should have addressed.

Continue only if:

- `output/50_FD_DRAFT_REVISED.md` exists.
- `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md` exists.
- `output/42_FD_REVIEW_REPORT.md` exists.

If any required input is missing, stop and report `No-Go`.

### Instructions

Review these layers separately:

#### Layer 1: Previous Review Issue Closure

Check whether issues in `output/42_FD_REVIEW_REPORT.md` were resolved by `output/50_FD_DRAFT_REVISED.md` and reflected in `output/50_FD_REVISION_LOG.md`.

Find:

- Critical issues fixed
- Major issues fixed
- Minor issues fixed
- Issues partially fixed
- Issues not fixed
- Issues converted to Open Questions
- New issues introduced during revision

#### Layer 2: Customer-Facing Cleanliness Review

Check `output/50_FD_DRAFT_REVISED.md` for:

- Professional Functional Design structure
- English clarity and technical readability
- No visible internal pipeline artifacts
- No exposed internal IDs
- No references to internal files
- No mentions of requirement inventory, business rule catalog, glossary, image analysis, translation review, internal traceability, intermediate artifacts, prompts, Copilot, AI, model, or pipeline
- No `REQ-xxx`, `BR-xxx`, `TERM-xxx`, `OQ-xxx`, `FIG-xxx`, `TRACE-xxx`, `RTRACE-xxx`, or `PTRACE-xxx`
- No implementation details invented without source support
- No generic business/domain knowledge added
- Proper use of `TBD` and `Requires confirmation`
- Proper treatment of unsupported behavior
- Proper treatment of figure-derived behavior
- Proper treatment of strikethrough/deprecated evidence
- Proper use of Markdown image references
- Proper use of Mermaid diagrams
- Concise customer-facing writing
- No internal revision log or patch summary accidentally left in the customer-facing deliverable body

#### Layer 3: Evidence and Traceability Quality

Check `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md` against:

- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`
- `output/21_glossary.md`
- `output/20_image_analysis.md`
- `output/12_normalized_evidence.md`
- raw extracted text/tables only when targeted verification is needed

Find:

- Revised FD statements without traceability
- Revised FD statements partially traced
- Revised FD statements stronger than source evidence
- Revised FD statements created from assumptions
- Revised FD statements based only on figure inference but written too strongly
- Revised FD statements based on strikethrough-only evidence as active behavior
- Requirements missing from the revised FD
- Business rules missing from the revised FD
- Unsupported cases missing from the revised FD
- Open questions missing from the revised FD
- Glossary-controlled terms misused in the revised FD
- Source contradictions not reflected as open questions
- Translation uncertainties incorrectly written as confirmed behavior

#### Layer 4: Visual Evidence Quality

Check visual content in `output/50_FD_DRAFT_REVISED.md`:

- Markdown image references
- Mermaid flowcharts
- Mermaid sequence diagrams
- Mermaid state diagrams
- visual captions
- visual notes

Find:

- Missing or broken image paths
- Decorative images without requirement value
- Mermaid diagrams with unsupported nodes, states, actors, timing, or transitions
- Figure-derived behavior overstated as confirmed text behavior
- Visuals that duplicate text without adding clarity
- Relevant source diagrams omitted when their omission weakens FD understanding
- Diagram ambiguity not carried into Open Questions

## Inputs

### Primary inputs

- `output/50_FD_DRAFT_REVISED.md`
- `output/50_FD_REVISION_LOG.md`
- `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md`
- `output/42_FD_REVIEW_REPORT.md`
- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`
- `output/21_glossary.md`
- `output/20_image_analysis.md`
- `output/12_normalized_evidence.md`

### Supporting inputs, open only when needed

- `output/41_FD_INTERNAL_TRACEABILITY.md`
- `output/40_FD_DRAFT.md`
- `output/11_translation_policy.md`
- `output/10_document_inventory.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`
- `working/extracted/image_inventory_raw.md`
- `working/extracted/formatting_inventory.md`, if available

## Outputs

### Output file to create or update

Create or overwrite:

- `output/52_FD_REVISED_REVIEW_REPORT.md`

## Required output structure

Write `output/52_FD_REVISED_REVIEW_REPORT.md` using this structure:

```markdown
# Revised FD Review Report

## 1. Executive Review Summary

Overall recommendation: `Go` / `Go with minor corrections` / `No-Go`

Include:

- Short reason
- Main risks
- Whether previous critical/major review issues were fixed
- Whether the revised FD is customer-facing clean
- Whether revised internal traceability is sufficient
- Whether visual content is appropriate and traceable
- Whether any active FD behavior appears to come from strikethrough-only evidence

## 2. Previous Review Issue Closure

| Review Issue | Source Review Report | Original Severity | Closure Status | Revised FD Location | Evidence / Notes | Recommendation |
|---|---|---|---|---|---|---|

Closure Status:

- Fixed
- Partially fixed
- Not fixed
- Converted to Open Question
- Not applicable
- New issue introduced

Rules:

- Critical and major issues from `output/42_FD_REVIEW_REPORT.md` must be explicitly checked.
- If an issue was not fixed, state whether it blocks review.

## 3. Customer-Facing Cleanliness Review

| Check Item | Result | Evidence / Location | Recommendation |
|---|---|---|---|

Check items:

- Internal file names are not exposed
- Internal IDs are not exposed
- Intermediate artifact names are not exposed
- Revised FD does not mention the analysis pipeline
- Revised FD uses customer-facing wording
- Revised FD avoids internal review notes
- Revised FD does not contain internal revision log / patch summary in the deliverable body
- Revised FD marks uncertain items as `TBD` or `Requires confirmation`
- Revised FD uses visual content appropriately
- Revised FD does not present strikethrough-only/deprecated evidence as active behavior

## 4. Critical Issues

| Issue ID | Issue | Location | Evidence | Impact | Recommended Fix |
|---|---|---|---|---|---|

Critical issue examples:

- Revised FD includes unsupported behavior as confirmed behavior
- Revised FD includes untraced behavior
- Revised FD exposes internal artifact IDs in customer-facing content
- Revised FD misses a mandatory business rule
- Revised FD contradicts source evidence
- Revised FD invents implementation design not supported by source
- Revised FD contains unsupported visual workflow
- Revised FD treats strikethrough-only evidence as active behavior
- Previous critical issue remains unresolved

If none, write:

`No critical issues found.`

## 5. Major Issues

| Issue ID | Issue | Location | Evidence | Impact | Recommended Fix |
|---|---|---|---|---|---|

Major issue examples:

- Partially traced revised FD behavior
- Missing unsupported case
- Missing source condition
- Missing exception/footnote
- Figure-inferred behavior written too strongly
- Open question not carried into revised FD
- Term with High meaning risk used without confirmation
- Relevant source diagram omitted
- Mermaid diagram needs simplification
- Previous major issue remains unresolved

If none, write:

`No major issues found.`

## 6. Minor Issues

| Issue ID | Issue | Location | Evidence | Impact | Recommended Fix |
|---|---|---|---|---|---|

Minor issue examples:

- Wording issue
- Formatting issue
- Slightly unclear sentence
- Missing helpful note
- Repeated content
- Caption wording issue
- Mermaid readability issue

If none, write:

`No minor issues found.`

## 7. Revised Traceability Review

| Trace Check | Result | Count / Details | Recommendation |
|---|---|---|---|

Check:

- Total revised FD statements reviewed
- Traced revised FD statements
- Partially traced revised FD statements
- Untraced revised FD statements
- Potential overstatements
- Items needing confirmation
- Figure-only evidence items
- Open questions carried into revised FD
- Missing requirements
- Missing business rules
- Missing unsupported cases
- Previous review issues closed
- Previous review issues still open
- Items incorrectly based on strikethrough-only evidence

## 8. Requirement and Rule Coverage

Compare revised FD content against `output/30_requirement_inventory.md`, `output/31_business_rule_catalog.md`, and `output/32_open_questions.md`.

| Source Item | Coverage Status | Revised FD Location | Issue | Recommendation |
|---|---|---|---|---|

Coverage Status:

- Covered
- Partially covered
- Missing
- Converted to Open Question
- Not applicable

Rules:

- Do not require internal IDs to appear in the customer-facing revised FD.
- Use internal IDs only in this review report.
- Customer-facing FD may use natural numbering instead of internal IDs.

## 9. Terminology Review

Check revised FD terminology against `output/21_glossary.md` and `output/11_translation_policy.md`.

| Term | Revised FD Usage | Expected Usage | Risk | Recommendation |
|---|---|---|---|---|

Check:

- Locked terms preserved
- Acronyms not expanded without evidence
- Field names not renamed
- Product-specific terms not freely translated
- Uncertain terms marked as requiring confirmation
- Multiple English renderings avoided
- Deprecated/strikethrough-only terms not treated as active terminology unless active evidence exists

## 10. Figure and Visual Evidence Review

Check revised FD usage of image/diagram-derived behavior.

| Visual / Diagram Reference | Revised FD Usage | Evidence Type | Source Image Path | Risk | Recommendation |
|---|---|---|---|---|---|

Check:

- Embedded source images are relevant and traceable
- Markdown image paths appear valid
- Mermaid diagrams are source-supported
- Mermaid diagrams do not invent behavior
- Figure-derived behavior is not overstated
- Figure-only details are marked carefully
- Diagram ambiguity is carried into open questions
- Figure evidence does not contradict text evidence
- Relevant source diagrams were not omitted when needed

## 11. Open Questions Review

Check whether unresolved issues are represented correctly.

| Open Question Source | Revised FD Representation | Status | Recommendation |
|---|---|---|---|

Status:

- Included
- Missing
- Incorrectly converted to assumption
- Incorrectly converted to confirmed behavior
- Not applicable

## 12. Recommended Corrections

Provide concrete corrections.

| Correction ID | Target File | Target Section | Current Text / Issue | Recommended Change | Priority |
|---|---|---|---|---|---|

Target File should be one of:

- `output/50_FD_DRAFT_REVISED.md`
- `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md`
- `output/50_FD_REVISION_LOG.md`
- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`
- `output/21_glossary.md`
- `output/20_image_analysis.md`

Priority:

- Critical
- High
- Medium
- Low

## 13. Final Go / No-Go Recommendation

Provide one of:

- `Go`
- `Go with minor corrections`
- `No-Go`

Decision criteria:

- Use `Go` only if the revised FD is customer-facing clean, previous critical/major issues are resolved, internal traceability is sufficient, and visual content is traceable.
- Use `Go with minor corrections` if issues are minor and do not change business meaning.
- Use `No-Go` if the revised FD contains untraced behavior, exposed internal artifacts, missed mandatory rules, source contradictions, unsupported assumptions, unsupported visual content, strikethrough-only active behavior, or unresolved previous critical/major issues.

Include:

- Decision
- Reason
- Required action before customer/domain expert review
- Whether customer/domain expert Q&A is recommended
```

## Required output quality

- Do not rewrite the revised FD in this task.
- Do not generate FD, DD, code design, or implementation plan.
- Do not add new requirements.
- Do not invent missing source evidence.
- Do not require internal IDs to appear in the customer-facing revised FD.
- Use internal IDs only in this review report.
- Keep all output in English.
- Be strict about hallucination, traceability, unsupported behavior, exposed internal artifacts, unsupported visuals, and strikethrough-only evidence.
- If the revised FD is clean but traceability is weak, mark as `No-Go` or `Go with minor corrections` depending on severity.
- If the revised FD exposes internal artifact names or IDs, mark at least Major issue.
- If the revised FD has behavior unsupported by evidence, mark Critical issue.
- If the revised FD has visual content unsupported by evidence, mark Major or Critical depending on impact.
- If previous critical/major issues are not resolved, do not mark `Go`.

## Stop conditions

- Stop and report `No-Go` if required primary inputs are missing.
- Stop and report `No-Go` if `output/50_FD_DRAFT_REVISED.md` does not exist.
- Stop and report `No-Go` if `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md` does not exist.
- Stop and report `No-Go` if `output/42_FD_REVIEW_REPORT.md` does not exist.
- Stop and report `No-Go` if the review would require unsupported assumptions.
- Do not continue to downstream phases when this review decision is `No-Go`.
