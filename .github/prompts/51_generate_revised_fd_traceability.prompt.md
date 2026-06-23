# 51 - Generate Revised FD Internal Traceability

## Purpose

Create internal traceability for the revised customer-facing Functional Design produced by step 50.

This step verifies whether the revised FD remains source-bound after review corrections were applied.
It maps the revised FD back to the approved requirement, rule, glossary, image, open-question, and normalized evidence artifacts.

This is an internal review artifact. It must not be delivered to the customer unless explicitly approved.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not modify `output/50_FD_DRAFT_REVISED.md`.
- Do not create new FD behavior.
- Do not create new requirements or business rules.
- Do not use generic domain knowledge to justify FD content.
- Do not hide untraced, partially traced, or overstated content.
- Internal IDs are allowed in this traceability file.
- Keep customer-facing cleanliness concerns visible if they remain in the revised FD.
- Preserve source-supported negative statements, unsupported behavior, conditions, exceptions, notes, footnotes, and visual evidence.
- Respect strikethrough rules from the pipeline: strikethrough-only evidence must not be treated as active FD behavior unless the source explicitly says otherwise.
- Write the output in English.

### Important

Step 51 is the revised-FD version of step 41.

- Step 41 traces the initial FD: `output/40_FD_DRAFT.md`.
- Step 51 traces the revised FD: `output/50_FD_DRAFT_REVISED.md`.

This step does not patch the FD. It only creates traceability and identifies remaining risk.

## Tasks

### Precondition

Use the latest FD review and correction artifacts:

- `output/42_FD_REVIEW_REPORT.md` is the review report that step 50 was expected to address.
- `output/50_FD_REVISION_LOG.md` records what step 50 changed.
- `output/50_FD_DRAFT_REVISED.md` is the revised FD to trace.

Continue only if:

- `output/50_FD_DRAFT_REVISED.md` exists.
- `output/42_FD_REVIEW_REPORT.md` exists.
- Source-of-truth artifacts from steps 20/21/30/31/32 are available.

If required artifacts are missing, stop and report `No-Go`.

### Instructions

Create `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md`.

For each meaningful item in `output/50_FD_DRAFT_REVISED.md`, create a trace row.

Meaningful items include:

- FD section statements
- functional behavior
- business rules and constraints
- unsupported cases
- conditions and exceptions
- input/output data
- terminology definitions
- assumptions
- open questions
- Markdown image references
- Mermaid diagrams
- figure-derived scenarios
- notes that affect behavior
- revised or newly added content from step 50

For each item:

1. Identify the FD section.
2. Determine whether it is unchanged, revised, added, moved to Open Questions, or otherwise changed by step 50.
3. Trace it to the strongest available internal evidence.
4. Check whether it addresses a finding from `output/42_FD_REVIEW_REPORT.md`.
5. Mark trace status honestly.
6. Flag any overstatement, unsupported content, weak visual traceability, terminology risk, or strikethrough misuse.

## Inputs

### Primary inputs

- `output/50_FD_DRAFT_REVISED.md`
- `output/50_FD_REVISION_LOG.md`
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
- `working/extracted/image_inventory_raw.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`

## Outputs

### Output file to create or update

Create:

- `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md`

## Required output structure

Write `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md` using this structure:

```markdown
# Revised FD Internal Traceability

## 1. Traceability Decision

Decision: `Go` / `Go with minor corrections` / `No-Go`

Explain whether the revised FD is internally traceable enough for the next review step.

## 2. Input Verification

| Input Artifact | Status | Notes |
|---|---|---|
| output/50_FD_DRAFT_REVISED.md | Present / Missing | ... |
| output/50_FD_REVISION_LOG.md | Present / Missing | ... |
| output/42_FD_REVIEW_REPORT.md | Present / Missing | ... |
| output/30_requirement_inventory.md | Present / Missing | ... |
| output/31_business_rule_catalog.md | Present / Missing | ... |
| output/32_open_questions.md | Present / Missing | ... |
| output/21_glossary.md | Present / Missing | ... |
| output/20_image_analysis.md | Present / Missing | ... |
| output/12_normalized_evidence.md | Present / Missing | ... |

## 3. Revised FD Traceability Matrix

| Trace ID | Revised FD Section | Revised FD Statement / Visual Item | Item Type | Change Type | Internal Requirement ID | Internal Rule ID | Internal Term IDs | Internal Open Question IDs | Source Reference | Source Image Path | Evidence Type | Confidence | Meaning Risk | Trace Status | Related Review Issue | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

### Field definitions

- Trace ID: Use `RTRACE-001`, `RTRACE-002`, etc.
- Revised FD Section: section number/title in `output/50_FD_DRAFT_REVISED.md`.
- Revised FD Statement / Visual Item: concise copy or summary of the revised FD statement, embedded image, Mermaid diagram, or visual caption.
- Item Type:
  - Text statement
  - Business rule
  - Unsupported case
  - Data item
  - Terminology
  - Assumption
  - Open question
  - Embedded source image
  - Mermaid flowchart
  - Mermaid sequence diagram
  - Mermaid state diagram
  - Figure-derived scenario
  - Other
- Change Type:
  - Unchanged from initial FD
  - Revised wording
  - Added coverage
  - Added visual
  - Revised visual
  - Removed visual
  - Removed internal guidance
  - Moved to Open Question
  - Removed untraced content
  - Clarified uncertainty
  - Not clear from revision log
  - Other
- Internal Requirement ID: related `REQ-xxx`, if applicable.
- Internal Rule ID: related `BR-xxx`, if applicable.
- Internal Term IDs: related `TERM-xxx`, if applicable.
- Internal Open Question IDs: related `OQ-xxx`, if applicable.
- Source Reference: original source paragraph, table, note, footnote, figure, normalized source reference, or `N/A`.
- Source Image Path: extracted image path if the revised FD item uses or derives from an embedded DOCX image; otherwise `N/A`.
- Evidence Type:
  - Confirmed by text
  - Confirmed by table
  - Confirmed by figure
  - Inferred from figure
  - Mixed evidence
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
  - Corrected
- Related Review Issue: issue ID or finding from `output/42_FD_REVIEW_REPORT.md`, if applicable.
- Notes: coverage issue, ambiguity, risk, correction suggestion, strikethrough concern, visual concern, or review comment.

Continue the output with:

```markdown
## 4. Revision Coverage Summary

| Metric | Count | Notes |
|---|---:|---|
| Total revised FD statements/items reviewed | ... | ... |
| Traced items | ... | ... |
| Partially traced items | ... | ... |
| Untraced items | ... | ... |
| Potential overstatements | ... | ... |
| Items needing confirmation | ... | ... |
| Embedded source images included | ... | ... |
| Mermaid diagrams included | ... | ... |
| Visual items based on figure-only evidence | ... | ... |
| Open questions carried into the revised FD | ... | ... |
| Previous review issues addressed | ... | ... |
| Previous review issues not addressed | ... | ... |

## 5. Visual Coverage Summary

| Visual Item | Revised FD Location | Source Evidence | Trace Status | Risk | Recommendation |
|---|---|---|---|---|---|

## 6. Previous Review Issue Closure

| Review Issue | Source Review Report | Status | Revised FD Location | Evidence | Notes |
|---|---|---|---|---|---|
```

Status must be one of:

- Fixed
- Partially fixed
- Not fixed
- Converted to Open Question
- Not applicable
- Unable to verify

Continue with:

```markdown
## 7. Strikethrough / Deprecated Evidence Check

| Item | Revised FD Location | Issue | Risk | Recommendation |
|---|---|---|---|---|

## 8. Risk Summary

List:

- Revised FD statements with Low confidence
- Revised FD statements with Medium or High meaning risk
- Revised FD statements based only on figure inference
- Revised FD statements that may be stronger than source evidence
- Revised FD statements requiring customer/domain expert confirmation
- Visual items with weak or missing traceability
- Mermaid diagrams that may overstate source behavior
- Any active behavior that appears to rely on strikethrough-only/deprecated evidence

## 9. Traceability Findings

List:

- Missing traceability
- Potential overstatements in the revised FD
- Revised FD statements that should be changed to `TBD`
- Revised FD statements that should become Open Questions
- Internal evidence conflicts
- Terminology inconsistencies
- Visual content that should be removed, simplified, or marked as requiring confirmation
- Previous review issues not fully resolved
- Recommended corrections for the revised FD

## 10. Go / No-Go Recommendation

Recommendation: `Go` / `Go with minor corrections` / `No-Go`

Explain the recommendation briefly.
```

## Evidence priority

Use this priority order when tracing revised FD content:

1. `output/30_requirement_inventory.md`
2. `output/31_business_rule_catalog.md`
3. `output/32_open_questions.md`
4. `output/21_glossary.md`
5. `output/20_image_analysis.md`
6. `output/12_normalized_evidence.md`
8. Raw extracted files only for targeted verification

## Traceability rules

- Every major revised FD behavior must have a trace row.
- Every business rule in the revised FD must have a trace row.
- Every unsupported case in the revised FD must have a trace row.
- Every open question in the revised FD must have a trace row.
- Every embedded image in the revised FD must have a trace row.
- Every Mermaid diagram in the revised FD must have a trace row.
- Every figure-derived scenario must be clearly marked.
- Do not mark an item as `Traced` if the supporting evidence is only partial.
- Mark `Potential overstatement` when the FD wording is stronger than the source evidence.
- Mark `Needs confirmation` when the FD depends on unresolved terminology, unresolved source ambiguity, or customer confirmation.
- Mark `Untraced` when no supporting internal evidence is found.
- Do not use the revision log itself as source evidence for FD behavior; use it only to understand what changed.

## Visual traceability rules

- Trace every Markdown image reference in the revised FD.
- Trace every Mermaid diagram in the revised FD.
- Trace every customer-facing figure caption in the revised FD.
- Confirm that each embedded image path exists in image evidence or extracted image inventory.
- Confirm that each Mermaid node, step, state, actor, transition, or timing element is source-supported.
- If a Mermaid diagram simplifies a source figure, mark it as `Mixed evidence` or `Inferred from figure` as appropriate.
- If a visual is included only for decoration, mark it as `Untraced` and recommend removal.
- If a previous review issue was caused by untraced or overstated visual content, explicitly check whether the revised FD fixed it.

## Strikethrough and deprecated evidence rules

- Strikethrough-only evidence is inactive/deleted/deprecated by default.
- Do not trace active FD behavior to strikethrough-only evidence unless the source explicitly says it remains active.
- If revised FD content appears to rely on strikethrough-only text, mark it as `Potential overstatement` or `Needs confirmation`.
- If strikethrough evidence conflicts with active text/table/figure evidence, treat active evidence as primary and record the strikethrough item as deprecated/conflict context.
- If the status is unclear, create a trace finding and recommend moving the affected FD content to Open Questions or `Requires confirmation`.

## Required output quality

- Internal IDs are allowed here.
- Make coverage gaps visible.
- Keep findings actionable.
- Do not edit the customer-facing FD in this phase.
- Do not introduce new FD behavior.
- Do not create new requirements or business rules.
- Keep writing concise and technical.

## Stop conditions

- Stop and report `No-Go` if `output/50_FD_DRAFT_REVISED.md` is missing.
- Stop and report `No-Go` if the main source-of-truth artifacts from steps 30/31/32 are missing.
- Stop and report `No-Go` if the traceability output would require unsupported assumptions.
- Do not continue to step 52 when this traceability decision is `No-Go`.
