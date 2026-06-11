# 34 - Review Feature Understanding Brief

## Purpose

Review `output/33_FEATURE_UNDERSTANDING_BRIEF.md` for usefulness, evidence alignment, clarity, terminology control, and hallucination risk before using it as a fast onboarding document for BA, developer, reviewer, or project member.

This is a quality gate for feature understanding. It does **not** approve the full Functional Design, Detailed Design, coding design, or code generation.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not rewrite the whole brief.
- Do not invent missing BRD content.
- Do not approve unsupported business logic presented as fact.
- Do not require DD-level or coding-level details unless the brief claims them.
- Preserve source-specific terms unless the translation policy or glossary explicitly defines an approved rendering.
- Mark ambiguous, missing, or conflicting information instead of guessing.
- Keep feedback actionable.
- Write outputs in English unless the user explicitly asks otherwise.

### Formatting evidence rules

- Treat source formatting as evidence when it changes meaning.
- Strikethrough text means inactive, deleted, deprecated, superseded, or draft-removed evidence unless the source explicitly says otherwise.
- Do not treat strikethrough-only text as active requirement behavior, active business rules, active operation flow, active field definitions, or active UI/API behavior.
- If a paragraph, table cell, caption, or figure note contains both active and strikethrough text, use only the non-strikethrough portion as active evidence.
- Preserve strikethrough evidence in traceability notes when it helps explain removed or deprecated behavior.
- If strikethrough content conflicts with active evidence, prefer active non-strikethrough evidence and record the struck-through content as deprecated/conflict context, not as a confirmed requirement.
- Highlighted text is not automatically active or mandatory. If highlighted text is also strikethrough, the strikethrough rule wins.
- If formatting status is unclear or missing from upstream artifacts, mark the affected item as ambiguous instead of guessing.

For review, check whether the brief accidentally used strikethrough-only content as active behavior, active scope, active rule, or active operation. Treat that as a Major or Critical finding depending on impact.

### Important

- This is a review gate for an internal understanding artifact.
- The review decision applies only to whether the brief is safe and useful for BA/developer onboarding.
- It does not validate the final FD.
- It does not authorize DD or coding.

## Tasks

### Precondition

Required input:

- `output/33_FEATURE_UNDERSTANDING_BRIEF.md`

Primary evidence for review:

- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`

Recommended supporting evidence:

- `output/20_image_analysis.md`
- `output/21_glossary.md`

If the brief is missing, stop and report `No-Go`.

If source evidence files are missing, continue only if enough evidence remains to review the brief safely. Clearly state missing inputs and reduce confidence accordingly.

### Instructions

Create `output/34_FEATURE_UNDERSTANDING_REVIEW.md`.

Evaluate whether the Feature Understanding Brief helps BA/developer/reviewer quickly understand the feature without reading the original Japanese BRD.

Check the brief for:

1. Evidence alignment
2. Missing major source-supported topics
3. Hallucinated or unsupported claims
4. Confusing or over-translated terminology
5. Incomplete flow understanding
6. Missing key inputs/outputs
7. Missing business rules, validations, constraints, or unsupported cases
8. Missing or weak open questions
9. Misuse of diagrams/images
10. Premature FD/DD/coding assumptions

## Inputs

### Primary inputs

- `output/33_FEATURE_UNDERSTANDING_BRIEF.md`
- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`

### Supporting inputs, open only when needed

- `output/20_image_analysis.md`
- `output/21_glossary.md`
- `output/12_normalized_evidence.md`
- `output/10_document_inventory.md`
- `output/11_translation_policy.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`
- `working/extracted/image_inventory_raw.md`
- `working/extracted/formatting_inventory.md`, if present

Use supporting inputs only to verify suspicious claims, unclear terminology, diagram usage, or source references.

## Outputs

### Output file to create or update

- `output/34_FEATURE_UNDERSTANDING_REVIEW.md`

### Decision levels

Use one of these decisions:

- `Go` - The brief is useful and safe enough for BA/developer onboarding.
- `Go with minor notes` - The brief is usable, but minor edits are recommended.
- `Fix required` - The brief has fixable issues that should be corrected before use.
- `No-Go` - The brief is misleading, materially incomplete, or has serious unsupported claims.

### Severity guidance

Use these severity levels:

- `Critical` - Could mislead BA/dev and cause wrong design or implementation.
- `Major` - Important missing or unclear information that affects understanding.
- `Minor` - Wording, organization, or small completeness issue.
- `Info` - Observation only.

### Output structure

Write `output/34_FEATURE_UNDERSTANDING_REVIEW.md` using this structure:

```markdown
# Feature Understanding Brief Review

## 1. Review Decision
Decision: `Go` / `Go with minor notes` / `Fix required` / `No-Go`

## 2. Executive Review Summary
Short summary of whether the brief is useful for BA/developer onboarding.

## 3. Evidence Alignment Findings
List claims that are well-supported and claims that appear unsupported or weakly supported.

| Finding ID | Brief Section | Finding | Evidence Source | Severity | Recommended Action |
|---|---|---|---|---|---|

## 4. Missing or Underdeveloped Topics
List important source-supported topics that should be added or expanded.

| Finding ID | Missing Topic | Evidence Source | Severity | Recommended Action |
|---|---|---|---|---|

## 5. Terminology and Translation Review
Check whether source terms, Japanese terms, field names, screen names, operation names, product terms, and acronyms are preserved correctly.

| Finding ID | Term / Phrase | Issue | Evidence Source | Recommended Action |
|---|---|---|---|---|

## 6. Flow and Rule Review
Check whether main flow, alternative flows, validations, messages, unsupported cases, and business rules are understandable and source-supported.

| Finding ID | Area | Issue | Evidence Source | Severity | Recommended Action |
|---|---|---|---|---|---|

## 7. Image / Diagram Usage Review
Check whether diagrams/images were used as evidence correctly and not treated as decoration or unsupported business logic.

| Finding ID | Image / Diagram | Issue | Evidence Source | Recommended Action |
|---|---|---|---|---|

## 8. Open Question Quality Review
Check whether open questions are clear, necessary, and useful for BA/customer clarification.

| Finding ID | Question / Area | Issue | Recommended Action |
|---|---|---|---|

## 9. Risk Assessment for Using This Brief
Explain risks if the team uses this brief to proceed to FD/DD/coding.

## 10. Required Corrections
List must-fix corrections before use.

## 11. Optional Improvements
List nice-to-have improvements.

## 12. Reviewer Notes
Any additional notes, including missing input files or confidence limitations.
```

## Required output quality

- The decision must match the severity of findings.
- Every Critical or Major issue must have a recommended action.
- The review must distinguish between missing evidence and weak writing.
- The review must not ask the generator to hallucinate missing information.
- The brief must remain positioned as an understanding artifact, not FD/DD/code design.
- Do not reject the brief only because open questions exist; reject it only if the brief hides or mishandles important uncertainty.
- Do not require implementation architecture, APIs, database schema, or test design unless the brief makes unsupported claims about them.
- Feedback must be actionable and concise.

## Stop conditions

Stop and report `No-Go` if:

- `output/33_FEATURE_UNDERSTANDING_BRIEF.md` is missing.
- The brief contains serious unsupported business logic that could mislead BA/developer work.
- The brief omits core source-supported behavior required to understand the feature.
- The brief uses terminology in a way that conflicts with `output/21_glossary.md` and changes meaning.
- The brief presents unresolved open questions as confirmed facts.

Do not stop only because some supporting source files are missing. Instead, report missing files and reduce review confidence if enough evidence remains to review the brief.
