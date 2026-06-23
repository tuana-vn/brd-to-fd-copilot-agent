# 53 - Apply Revised FD Review Corrections

## Purpose

Apply a second and final targeted correction pass to the revised customer-facing Functional Design based on the revised FD review report.

This step exists to fix remaining issues after step 52 without starting an infinite AI revision loop.

This task must not generate DD, code design, implementation design, or new source behavior.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Treat this as a targeted patch task, not a full FD regeneration task.
- Do not regenerate the full FD from scratch unless `output/52_FD_REVISED_REVIEW_REPORT.md` explicitly says the entire FD structure is unusable.
- Keep the patched FD customer-facing.
- Do not expose internal artifact names in the customer-facing FD.
- Do not expose internal IDs such as `REQ-xxx`, `BR-xxx`, `TERM-xxx`, `OQ-xxx`, `FIG-xxx`, `TRACE-xxx`, or `RTRACE-xxx` in the customer-facing FD.
- Do not mention requirement inventory, business rule catalog, glossary, image analysis, translation review, internal traceability, intermediate artifact, prompt, AI, or pipeline in the customer-facing FD.
- Do not add new requirements.
- Do not invent source evidence.
- Do not introduce implementation architecture unless the source explicitly supports it.
- Preserve source-supported conditions, exceptions, notes, footnotes, negative statements, unsupported behavior, and visual evidence.
- Preserve customer-facing Markdown image references and Mermaid diagrams only when they are source-supported and traceable.
- Remove, simplify, or mark as `Requires confirmation` any visual content that is weakly traced, figure-only, ambiguous, or overstated.
- If a review issue cannot be safely fixed as confirmed FD behavior, move it to the Open Questions section.
- If a statement is untraced and not needed, remove it.
- If a statement is editorial, generic, or marketing-like, remove it or rewrite it as a source-supported technical statement.
- Respect strikethrough/deprecated evidence rules: strikethrough-only evidence must not be used as active FD behavior unless the source explicitly says otherwise.
- Keep output in English.

## Tasks

### Precondition

Use `output/52_FD_REVISED_REVIEW_REPORT.md` as the controlling review gate.

Continue only when the step 52 recommendation is one of:

- `No-Go`
- `Go with minor corrections`

If the step 52 recommendation is `Go`, stop and report that no second correction pass is required.

This step patches:

- `output/50_FD_DRAFT_REVISED.md`

This step creates:

- `output/53_FD_DRAFT_REVISED_PATCHED.md`
- `output/53_FD_PATCH_LOG.md`

### Correction priorities

Apply corrections in this order:

1. Fix Critical issues from `output/52_FD_REVISED_REVIEW_REPORT.md`.
2. Fix Major issues from `output/52_FD_REVISED_REVIEW_REPORT.md`.
3. Fix customer-facing cleanliness issues.
4. Fix untraced or partially traced FD statements.
5. Fix potential overstatements.
6. Add missing source-supported requirement/rule coverage.
7. Move uncertain source-supported items to Open Questions.
8. Fix visual traceability issues.
9. Fix minor wording and formatting issues.

### Instructions

Create a complete patched FD at:

- `output/53_FD_DRAFT_REVISED_PATCHED.md`

The patched FD must be a full document, not a diff.

Also create a separate internal patch log at:

- `output/53_FD_PATCH_LOG.md`

Do not append the internal patch log to the customer-facing FD.

## Inputs

### Primary inputs

- `output/50_FD_DRAFT_REVISED.md`
- `output/50_FD_REVISION_LOG.md`
- `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md`
- `output/52_FD_REVISED_REVIEW_REPORT.md`

### Source-of-truth inputs for correction validation

- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`
- `output/21_glossary.md`
- `output/20_image_analysis.md`
- `output/12_normalized_evidence.md`

### Supporting inputs, open only when needed

- `output/40_FD_DRAFT.md`, if comparison with the first FD draft is needed
- `output/41_FD_INTERNAL_TRACEABILITY.md`, if comparison with the first traceability report is needed
- `output/42_FD_REVIEW_REPORT.md`, if previous issue history is needed
- `output/11_translation_policy.md`, if terminology verification is needed
- `output/10_document_inventory.md`, if source navigation is needed
- `working/extracted/document_text.md`, only for targeted verification
- `working/extracted/tables.md`, only for targeted verification
- `working/extracted/image_inventory_raw.md`, only for targeted visual path verification

## Outputs

### Output files to create or update

- `output/53_FD_DRAFT_REVISED_PATCHED.md`
- `output/53_FD_PATCH_LOG.md`

## Required output quality

### Customer-facing patched FD rules

The file `output/53_FD_DRAFT_REVISED_PATCHED.md` must:

- be a complete customer-facing Functional Design document;
- use professional English;
- preserve the FD structure unless the review report explicitly requires restructuring;
- contain only source-supported behavior;
- preserve source-supported unsupported cases, negative statements, constraints, exceptions, notes, and footnotes;
- mark uncertain items as `TBD`, `Requires confirmation`, or Open Questions;
- include only relevant, source-supported, traceable visual content;
- avoid internal IDs and internal artifact names;
- avoid internal review notes and patch summaries.

### Internal patch log rules

The file `output/53_FD_PATCH_LOG.md` may include internal IDs and internal review issue references.

Write the patch log using this structure:

```markdown
# FD Second-Pass Patch Log

## 1. Patch Decision

Decision: `Patched` / `Partially patched` / `Unable to patch safely`

Explain the decision briefly.

## 2. Issues Addressed from Step 52

| Review Issue ID / Description | Severity | Status | Patched FD Location | Action Taken | Notes |
|---|---|---|---|---|---|

Status must be one of:

- Fixed
- Partially fixed
- Converted to Open Question
- Removed unsupported content
- Not fixed
- Not applicable

## 3. Critical Issues Fixed

- ...

## 4. Major Issues Fixed

- ...

## 5. Customer-Facing Cleanliness Fixes

- ...

## 6. Visual / Mermaid Fixes

- ...

## 7. Missing Coverage Added

| Added Item | Target FD Section | Source Evidence | Notes |
|---|---|---|---|

## 8. Untraced or Overstated Content Removed / Weakened

| Original Issue | Action Taken | Patched FD Location | Notes |
|---|---|---|---|

## 9. Items Moved to Open Questions

| Item | Reason | Patched FD Open Question Location | Notes |
|---|---|---|---|

## 10. Remaining Risks

| Risk | Impact | Recommended Human Review |
|---|---|---|

## 11. Final Validation Checklist

| Check | Result | Notes |
|---|---|---|
| No internal artifact names in customer-facing FD | Pass / Fail | ... |
| No internal IDs in customer-facing FD | Pass / Fail | ... |
| No untraced statement remains as confirmed behavior | Pass / Fail | ... |
| No overstatement remains as confirmed behavior | Pass / Fail | ... |
| Visual content is source-supported and traceable | Pass / Fail | ... |
| Uncertain items are marked as TBD, Requires confirmation, or Open Questions | Pass / Fail | ... |
| Strikethrough-only evidence is not used as active behavior | Pass / Fail | ... |
| Patched FD reads like a clean customer-facing Functional Design | Pass / Fail | ... |
```

## Correction handling rules

### Internal artifact exposure

If the revised FD contains internal file names, internal IDs, or analysis-pipeline wording:

- remove the wording; or
- rewrite it as normal customer-facing FD text.

Do not leave phrases such as:

- requirement inventory
- business rule catalog
- glossary-controlled
- image analysis
- translation review
- internal traceability
- intermediate artifact
- prompt
- AI-generated
- pipeline

### Missing coverage

If the review report says a requirement, business rule, unsupported case, condition, exception, or open question is missing:

- add it to the most appropriate FD section if source-supported;
- do not expose its internal ID in the customer-facing FD;
- use normal customer-facing numbering.

If the item is not safe to write as confirmed behavior:

- add it to the Open Questions section.

### Untraced statements

If an FD statement is marked as untraced:

- remove it if it is editorial or unnecessary;
- rewrite it as `TBD` or `Requires confirmation` if it may be important but unsupported;
- move it to Open Questions if it affects behavior;
- do not keep it as confirmed behavior.

### Potential overstatement

If a statement is stronger than the source evidence:

- weaken it to match the source;
- use wording such as `The source diagram indicates...` only when appropriate;
- add `Requires confirmation` when business meaning is not fully confirmed.

### Figure-derived behavior

If a statement or Mermaid diagram is based only on figure evidence:

- do not write it as text-confirmed behavior;
- phrase it carefully;
- add an Open Question if the diagram meaning affects behavior and is ambiguous.

### Strikethrough or deprecated evidence

If evidence is marked as strikethrough, deleted, deprecated, superseded, or inactive:

- do not use it as active FD behavior;
- do not create active rules from it;
- use it only as historical/deprecated context if needed;
- if it conflicts with active evidence, move the conflict to Open Questions or mark the active behavior as requiring confirmation.

### Visual content

For Markdown images:

- keep only relevant source-supported images;
- ensure the relative path remains valid;
- use customer-facing captions;
- remove decorative or untraced images.

For Mermaid diagrams:

- keep diagrams simple;
- include only source-supported nodes, states, actors, timing, and transitions;
- remove invented steps;
- simplify diagrams that overstate behavior;
- add notes if the diagram is based on figure-derived behavior.

### Open Questions

Ensure Open Questions include:

- unresolved terminology;
- source contradictions;
- missing triggers, preconditions, or components;
- ambiguous figure-derived behavior;
- translation uncertainty affecting behavior;
- items that cannot be safely written as confirmed behavior.

## Stop conditions

- Stop and report `No-Go` if required primary inputs are missing.
- Stop and report `No-Go` if `output/52_FD_REVISED_REVIEW_REPORT.md` is missing.
- Stop and report `No-Go` if the output would require unsupported assumptions.
- Stop and report `No-Go` if required corrections depend on missing source evidence and cannot be safely moved to Open Questions.
- Stop and report `No action required` if the step 52 recommendation is `Go`.
- Do not continue to FD/DD/coding from this step alone.

## Final validation

Before completing the output, verify:

- No internal artifact names are exposed in the customer-facing FD body.
- No internal IDs are exposed in the customer-facing FD body.
- No untraced statement remains as confirmed behavior.
- No overstatement remains as confirmed behavior.
- Visual content is source-supported and traceable.
- Uncertain items are marked as `TBD`, `Requires confirmation`, or Open Questions.
- Strikethrough-only evidence is not used as active behavior.
- The output reads like a clean customer-facing Functional Design document.
