# 54 - Generate Patched FD Traceability

## Purpose

Create an internal traceability file for the patched customer-facing Functional Design.


## Inputs

- `output/53_FD_DRAFT_REVISED_PATCHED.md`
- `output/53_FD_PATCH_LOG.md`
- Internal requirement and rule artifacts
- Latest normalized evidence file


## Outputs to create or update

- `output/54_PATCHED_FD_INTERNAL_TRACEABILITY.md`


## Task

Important:
This file is for internal review only.
Do not modify `output/53_FD_DRAFT_REVISED_PATCHED.md`.
Do not create new FD behavior.
Do not expose this file as a customer-facing deliverable unless explicitly approved.

Context:
`output/53_FD_DRAFT_REVISED_PATCHED.md` is expected to fix issues identified in:

* `output/52_FD_REVISED_REVIEW_REPORT.md`
* earlier review reports if still relevant

This task must verify that the patched FD:

* fixed critical and major issues from previous reviews
* removed customer-facing cleanliness issues
* removed or corrected untraced editorial statements
* added missing source-supported coverage
* moved uncertain items to Open Questions when needed
* preserved unsupported behavior, negative statements, conditions, exceptions, notes, footnotes, and visual evidence
* kept visual content source-supported and traceable

Instructions:
Create `output/54_FD_PATCHED_INTERNAL_TRACEABILITY.md`.

For each meaningful statement, section, rule, behavior, data item, open question, unsupported case, exception, condition, visual item, embedded image reference, Mermaid diagram, figure-derived scenario, or newly patched content in `output/53_FD_DRAFT_REVISED_PATCHED.md`, create a trace row.

Use this table:

| Trace ID | Patched FD Section | Patched FD Statement / Visual Item | Item Type | Change Type | Internal Requirement ID | Internal Rule ID | Internal Term IDs | Internal Open Question IDs | Source Reference | Source Image Path | Evidence Type | Confidence | Meaning Risk | Trace Status | Related Review Issue | Notes |
| -------- | ------------------ | ---------------------------------- | --------- | ----------- | ----------------------- | ---------------- | ----------------- | -------------------------- | ---------------- | ----------------- | ------------- | ---------- | ------------ | ------------ | -------------------- | ----- |

Field definitions:

* Trace ID: Use `PTRACE-001`, `PTRACE-002`, etc.
* Patched FD Section: section number/title in `output/53_FD_DRAFT_REVISED_PATCHED.md`.
* Patched FD Statement / Visual Item: concise copy or summary of the patched FD statement, embedded image, Mermaid diagram, or visual caption.
* Item Type:

  * Text statement
  * Business rule
  * Unsupported case
  * Data item
  * Open question
  * Embedded source image
  * Mermaid flowchart
  * Mermaid sequence diagram
  * Mermaid state diagram
  * Figure-derived scenario
  * Other
* Change Type:

  * Unchanged from revised FD
  * Revised wording
  * Added coverage
  * Added visual
  * Revised visual
  * Removed visual
  * Removed internal guidance
  * Moved to Open Question
  * Removed untraced content
  * Clarified uncertainty
  * Other
* Internal Requirement ID: related `REQ-xxx`, if applicable.
* Internal Rule ID: related `BR-xxx`, if applicable.
* Internal Term IDs: related `TERM-xxx`, if applicable.
* Internal Open Question IDs: related `OQ-xxx`, if applicable.
* Source Reference: original source paragraph, table, note, footnote, figure, or normalized source reference.
* Source Image Path: extracted image path if the patched FD item uses or derives from an embedded DOCX image; otherwise `N/A`.
* Evidence Type:

  * Confirmed by text
  * Confirmed by table
  * Confirmed by figure
  * Inferred from figure
  * Mixed evidence
  * Open question
  * Untraced
* Confidence: High / Medium / Low.
* Meaning Risk: None / Low / Medium / High.
* Trace Status:

  * Traced
  * Partially traced
  * Untraced
  * Needs confirmation
  * Potential overstatement
  * Corrected
* Related Review Issue: reference the relevant issue from previous review reports if the patched FD item addresses it.
* Notes: coverage issue, ambiguity, risk, correction suggestion, or review comment.

Rules:

* Do not rewrite `output/53_FD_DRAFT_REVISED_PATCHED.md`.
* Do not add new FD behavior.
* Do not create new requirements.
* Do not create new business rules.
* Do not hide untraced patched FD statements or untraced visual items.
* If a patched FD statement has no internal evidence, mark Trace Status as `Untraced`.
* If a visual item has no source image, source behavior, or source-supported scenario, mark Trace Status as `Untraced`.
* If a Mermaid diagram contains behavior not supported by source evidence, mark Trace Status as `Potential overstatement`.
* If a patched FD statement is only partially supported, mark Trace Status as `Partially traced`.
* If a patched FD statement is stronger than the source evidence, mark Trace Status as `Potential overstatement`.
* If a patched FD statement depends on unresolved terminology, mark Trace Status as `Needs confirmation`.
* If a patched FD statement or visual is based only on figure inference, mark Evidence Type as `Inferred from figure`.
* If a patched FD statement or visual is based on both text and figure evidence, mark Evidence Type as `Mixed evidence`.
* Preserve internal IDs in this traceability file.
* Keep all output in English.
* Use concise technical wording.

Evidence priority:

1. `output/04_requirement_inventory.md`
2. `output/05_business_rule_catalog.md`
3. `output/03_glossary.md`
4. `output/06_open_questions.md`
5. `output/02_image_analysis.md`
6. `output/01B_document_inventory_english.md`
7. Raw source files only for verification

Do not use generic domain knowledge to trace patched FD content.

Visual Traceability Rules:

* Trace every Markdown image reference in the patched FD.
* Trace every Mermaid diagram in the patched FD.
* Trace every customer-facing figure caption in the patched FD.
* Confirm that each embedded image path exists in the extracted image inventory or image analysis evidence.
* Confirm that each Mermaid node, step, state, actor, transition, or timing element is source-supported.
* If a Mermaid diagram simplifies a source figure, mark it as `Mixed evidence` or `Inferred from figure` as appropriate.
* If a visual is included only for decoration, mark it as `Untraced` and recommend removal.
* If a previous review issue was caused by untraced or overstated visual content, explicitly check whether the patched FD fixed it.

After the trace table, add:

## Patched Coverage Summary

Include:

* Total patched FD statements/items reviewed
* Number of traced items
* Number of partially traced items
* Number of untraced items
* Number of potential overstatements
* Number of items needing confirmation
* Number of embedded source images included
* Number of Mermaid diagrams included
* Number of visual items based on figure-only evidence
* Number of open questions carried into the patched FD
* Number of previous review issues addressed
* Number of previous review issues not addressed

## Visual Coverage Summary

Use this table:

| Visual Item | Patched FD Location | Source Evidence | Trace Status | Risk | Recommendation |
| ----------- | ------------------- | --------------- | ------------ | ---- | -------------- |

Check:

* Embedded source images
* Mermaid flowcharts
* Mermaid sequence diagrams
* Mermaid state diagrams
* Figure-derived scenarios
* Captions and visual notes

## Previous Review Issue Closure

Use this table:

| Review Issue | Source Review Report | Status | Patched FD Location | Evidence | Notes |
| ------------ | -------------------- | ------ | ------------------- | -------- | ----- |

Status:

* Fixed
* Partially fixed
* Not fixed
* Converted to Open Question
* Not applicable

## Risk Summary

List:

* Patched FD statements with Low confidence
* Patched FD statements with Medium or High meaning risk
* Patched FD statements based only on figure inference
* Patched FD statements that may be stronger than source evidence
* Patched FD statements requiring customer/domain expert confirmation
* Visual items with weak or missing traceability
* Mermaid diagrams that may overstate source behavior

## Review Findings

List:

* Missing traceability
* Potential overstatements in patched FD
* Patched FD statements that should be changed to `TBD`
* Patched FD statements that should become Open Questions
* Internal evidence conflicts
* Terminology inconsistencies
* Visual content that should be removed, simplified, or marked as requiring confirmation
* Previous review issues not fully resolved
* Recommended corrections for the patched FD

## Go / No-Go Recommendation

Provide one of:

* `Go`: Patched FD is internally traceable and ready for review.
* `Go with minor corrections`: Patched FD is mostly traceable but minor cleanup is needed.
* `No-Go`: Patched FD contains untraced, overstated, or risky content that must be corrected before review.

Final validation:
Before completing the output, verify:

* Every major patched FD behavior has a trace row.
* Every business rule in the patched FD has a trace row.
* Every unsupported case in the patched FD has a trace row.
* Every open question in the patched FD has a trace row.
* Every embedded image in the patched FD has a trace row.
* Every Mermaid diagram in the patched FD has a trace row.
* Every figure-derived scenario in the patched FD is clearly marked.
* Previous critical and major review issues are checked for closure.
* No new FD behavior was introduced by this traceability task.
