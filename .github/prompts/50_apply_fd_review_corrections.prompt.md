# 50 - Apply FD Review Corrections

## Purpose

Apply first-round review corrections to the customer-facing Functional Design (FD) without introducing unsupported content.

This task patches the FD generated in step 40 using the review result from step 42 and the source-bound evidence artifacts from steps 12, 20, 21, 30, 31, and 32.

This task must produce a complete revised FD document, not a diff.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not regenerate the full FD from scratch unless `output/42_FD_REVIEW_REPORT.md` explicitly says the FD structure is unusable.
- Do not invent requirements, business rules, validations, command behavior, UI/API behavior, messages, diagrams, or implementation design.
- Do not introduce implementation architecture unless the source explicitly supports it.
- Preserve source-supported conditions, exceptions, notes, footnotes, negative statements, unsupported behavior, and visual evidence.
- Preserve command names, option names, parameters, field names, product-specific terms, acronyms, and code-like identifiers exactly.
- Keep the revised FD customer-facing.
- Do not expose internal artifact names, internal IDs, review issue IDs, or pipeline terminology in the customer-facing FD body.
- Internal review details may appear only in `output/50_FD_REVISION_LOG.md`, not in the customer-facing FD body.
- Write outputs in English unless a source value must remain unchanged.

### Customer-facing cleanliness rules

The customer-facing FD body must not mention or expose:

- internal artifact file names
- `REQ-xxx`
- `BR-xxx`
- `TERM-xxx`
- `OQ-xxx`
- `FIG-xxx`
- `TRACE-xxx`
- review issue IDs
- requirement inventory
- business rule catalog
- glossary-controlled
- image analysis
- translation review
- internal traceability
- intermediate artifact
- prompt, model, Copilot, or AI pipeline wording

### Strikethrough and deprecated evidence rules

- Strikethrough text represents inactive, deleted, deprecated, superseded, or draft-removed evidence unless the source explicitly states otherwise.
- Do not use strikethrough-only content as active FD behavior.
- Do not use strikethrough-only content as an active business rule, active operation flow, active command syntax, active UI/API behavior, or active field definition.
- If the existing FD used strikethrough-only content as active behavior, remove it, mark it as not confirmed, or move the uncertainty to Open Questions.
- If strikethrough content conflicts with active evidence, preserve the active evidence and add an Open Question only when the conflict affects behavior.

## Tasks

### Precondition

Use the latest FD review gate from `output/42_FD_REVIEW_REPORT.md`.

Continue only when the step 42 decision is one of:

- `Go with minor corrections`
- `Fix required`
- `No-Go` where the review report clearly identifies fixable corrections

Stop if:

- `output/42_FD_REVIEW_REPORT.md` is missing.
- `output/40_FD_DRAFT.md` is missing.
- the review report says the FD cannot be safely corrected from available evidence.
- applying corrections would require unsupported assumptions.

### Instructions

Apply targeted corrections in this priority order:

1. Fix Critical findings from `output/42_FD_REVIEW_REPORT.md`.
2. Fix Major findings from `output/42_FD_REVIEW_REPORT.md`.
3. Remove customer-facing cleanliness issues.
4. Remove or rewrite untraced FD statements.
5. Weaken potential overstatements to match the source evidence.
6. Add missing source-supported requirement/rule coverage.
7. Move uncertain source-supported items to Open Questions.
8. Fix terminology inconsistencies.
9. Fix visual traceability issues.
10. Fix minor wording and formatting issues.

For each correction:

- Use the original FD wording as the starting point.
- Patch only the affected section unless a broader restructure is explicitly required by the review report.
- Keep confirmed source-supported behavior as confirmed behavior.
- Convert unsupported or uncertain behavior into `TBD`, `Requires confirmation`, or an Open Question.
- Remove editorial, generic, marketing-like, or untraced statements that do not help the FD.
- Do not add new behavior just because it seems reasonable.

## Inputs

### Primary inputs

- `output/40_FD_DRAFT.md`
- `output/41_FD_INTERNAL_TRACEABILITY.md`
- `output/42_FD_REVIEW_REPORT.md`
- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`
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

### Output files to create or update

- `output/50_FD_DRAFT_REVISED.md`
- `output/50_FD_REVISION_LOG.md`

## Required output structure

### Output 1: `output/50_FD_DRAFT_REVISED.md`

Create a complete revised customer-facing FD document.

The revised FD must:

- keep the same overall customer-facing FD style as `output/40_FD_DRAFT.md` unless the review report requires structural correction.
- be a full document, not a diff.
- not expose internal IDs or internal artifact names.
- include only source-supported behavior.
- mark uncertain behavior as `TBD`, `Requires confirmation`, or Open Question.
- preserve source-supported unsupported cases, negative statements, conditions, exceptions, notes, and footnotes.
- preserve source-supported visual content only when traceable.

Do not include an internal patch summary inside `output/50_FD_DRAFT_REVISED.md`.

### Output 2: `output/50_FD_REVISION_LOG.md`

Create an internal-only revision log using this structure:

```markdown
# FD Revision Log

## 1. Revision Decision

Decision: `Revised FD created` / `Revised FD created with remaining risks` / `No-Go`

Explain the decision briefly.

## 2. Inputs Used

| Input | Used? | Notes |
|---|---|---|

## 3. Review Findings Addressed

| Review Finding ID / Description | Severity | FD Section | Action Taken | Evidence Used | Status |
|---|---|---|---|---|---|

Status must be one of:

- Fixed
- Partially fixed
- Moved to Open Question
- Removed
- Not fixed
- Not applicable

## 4. Customer-facing Cleanliness Fixes

| Issue | Location | Action Taken |
|---|---|---|

## 5. Traceability and Evidence Fixes

| FD Item / Section | Trace Issue | Action Taken | Remaining Risk |
|---|---|---|---|

## 6. Visual Content Fixes

| Visual Item | Issue | Action Taken | Remaining Risk |
|---|---|---|---|

## 7. Terminology Fixes

| Term / Phrase | Issue | Action Taken |
|---|---|---|

## 8. Items Moved to Open Questions

| Item | Reason | Open Question Wording |
|---|---|---|

## 9. Content Removed

| Removed Content Summary | Reason | Evidence / Review Basis |
|---|---|---|

## 10. Missing Coverage Added

| Added FD Content Summary | Source Evidence | FD Location |
|---|---|---|

## 11. Remaining Risks

List remaining risks that require BA, customer, or domain expert review.

## 12. Final Validation Checklist

| Check | Result | Notes |
|---|---|---|
| No internal artifact names in customer-facing FD | Pass / Fail | ... |
| No internal IDs in customer-facing FD | Pass / Fail | ... |
| No untraced statement remains as confirmed behavior | Pass / Fail | ... |
| No overstatement remains as confirmed behavior | Pass / Fail | ... |
| Visual content is source-supported and traceable | Pass / Fail | ... |
| Strikethrough-only content is not used as active behavior | Pass / Fail | ... |
| Uncertain items are marked as TBD, Requires confirmation, or Open Questions | Pass / Fail | ... |
| Revised FD reads as a clean customer-facing FD | Pass / Fail | ... |
```

## Specific handling rules

### Internal artifact exposure

If the FD contains internal file names, internal IDs, review issue IDs, or analysis-pipeline wording:

- remove it from the customer-facing FD body, or
- rewrite it as normal customer-facing FD text.

Do not leave internal wording in the customer-facing FD body.

### Missing coverage

If the review report says a requirement, business rule, unsupported case, condition, exception, note, footnote, visual point, or open question is missing:

- add it to the most appropriate FD section only if source-supported.
- do not expose its internal ID.
- use normal customer-facing numbering.

If the item is not safe to write as confirmed behavior:

- add it to the Open Questions section.

### Untraced statements

If an FD statement is marked as untraced:

- remove it if it is editorial, generic, or unnecessary.
- rewrite it as `TBD` or `Requires confirmation` if it may be important but unsupported.
- move it to Open Questions if it affects behavior.
- do not keep it as confirmed behavior.

### Potential overstatement

If an FD statement is stronger than source evidence:

- weaken it to match the source evidence.
- use careful wording such as `The source diagram indicates...` only when appropriate.
- add `Requires confirmation` when the business meaning is not fully confirmed.

### Figure-derived behavior

If a statement or Mermaid diagram is based only on figure evidence:

- do not present it as text-confirmed behavior.
- phrase it carefully as diagram-indicated behavior.
- add an Open Question if the diagram meaning affects behavior and is ambiguous.

### Visual content

For Markdown images:

- keep only relevant source-supported images.
- ensure the relative path remains valid.
- use customer-facing captions.
- remove decorative, duplicate, irrelevant, weakly traced, or untraced images.

For Mermaid diagrams:

- keep diagrams simple.
- include only source-supported nodes, states, actors, timing, and transitions.
- remove invented steps.
- simplify diagrams that overstate behavior.
- add notes if the diagram is based on figure-derived behavior.

### Open Questions

Ensure Open Questions include unresolved items that affect FD correctness, including:

- unresolved terminology
- source contradictions
- missing triggers, preconditions, components, data definitions, or messages
- ambiguous figure-derived behavior
- translation uncertainty affecting behavior
- content that cannot be safely written as confirmed behavior

## Required output quality

- The revised FD must be customer-facing and professional.
- The revised FD must not contain internal pipeline wording.
- The revision log may contain internal references and review finding IDs.
- The revised FD must not include a diff or patch notation.
- The revised FD must not contain unsupported new behavior.
- The revised FD must preserve source-supported unsupported behavior and negative statements.
- The revised FD must not use strikethrough-only evidence as active behavior.
- The revised FD must keep exact spelling for command names, option names, parameters, field names, acronyms, and product-specific terms.

## Stop conditions

- Stop and report `No-Go` if required primary inputs are missing.
- Stop and report `No-Go` if the review report cannot be interpreted.
- Stop and report `No-Go` if applying the requested corrections would require unsupported assumptions.
- Stop and report `No-Go` if the source-bound artifacts do not contain enough evidence to fix Critical or Major findings.
- Do not continue to downstream phases when this correction step results in `No-Go`.
