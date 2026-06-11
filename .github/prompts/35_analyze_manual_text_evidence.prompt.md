# 35 - Analyze Manual Text Evidence Against Source Artifacts

## Purpose

Analyze a manually pasted text snippet that the user confirms is copied from the BRD or a trusted requirement source.

The goal is to determine whether the pasted text confirms, clarifies, conflicts with, or adds missing detail to the existing source-bound artifacts from steps 10–34.

This task may produce requirement/rule/update recommendations, but it must not directly rewrite the Functional Design, Detailed Design, code design, or implementation tasks.

This prompt is intended for focused text evidence review, especially when a user manually copies a small command syntax, table row, note, paragraph, or label from the source document after step 34.

## Operating rules

- Treat the pasted text as focused supplemental evidence.
- Do not analyze screenshots or images in this prompt.
- Do not infer hidden context beyond the pasted text and existing source artifacts.
- Do not invent requirements, business rules, validations, command behavior, API behavior, or design decisions.
- Preserve command names, option names, parameters, field names, product terms, acronyms, and code-like identifiers exactly.
- Follow `output/21_glossary.md` and `output/11_translation_policy.md`.
- Respect strikethrough rules from the pipeline:
  - Strikethrough-only content must not be treated as active behavior unless the source explicitly says otherwise.
  - If the pasted text came from strikethrough content, mark it as inactive/deprecated candidate evidence.
- Use pasted text to check existing requirements and rules, not to bypass the source-bound pipeline.
- Write the output in English.

## Tasks

### Precondition

Use the latest available evidence gate:

- If `output/34_FEATURE_UNDERSTANDING_REVIEW.md` exists, use it as the latest understanding gate.
- If the step 34 decision is `No-Go`, do not use the pasted text to bypass the review result.
- If the step 34 decision is `Fix required`, analyze the pasted text only as supplemental evidence and state that downstream FD/DD work should wait until the brief is fixed.
- If the step 34 decision is `Go` or `Go with minor notes`, continue normally.

Also verify whether the pasted text can be found or cross-checked in one of these artifacts:

- `output/12_normalized_evidence.md`
- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`
- supporting raw extracted source, only if needed

### Instructions

Given the pasted text snippet:

1. Extract visible factual elements from the pasted text:
   - command names
   - operation names
   - options
   - parameters
   - required/optional indicators
   - constraints
   - unsupported cases
   - state names
   - input/output data
   - notes

2. Classify the snippet:
   - command syntax
   - business rule
   - operation constraint
   - data definition
   - UI/API behavior
   - state transition
   - note/comment
   - unknown

3. Map the snippet to existing source artifacts:
   - `output/30_requirement_inventory.md`
   - `output/31_business_rule_catalog.md`
   - `output/32_open_questions.md`
   - `output/21_glossary.md`
   - `output/12_normalized_evidence.md`

4. Determine whether the snippet:
   - confirms an existing requirement
   - clarifies an existing requirement
   - confirms an existing business rule
   - clarifies an existing business rule
   - adds a missing requirement candidate
   - adds a missing business rule candidate
   - creates or resolves an open question
   - conflicts with existing evidence
   - is duplicate/reference-only evidence
   - is too narrow to use without more context

5. If the pasted text contains enough evidence, propose requirement/rule candidates.
   Do not mark them as final unless they are already supported by existing source artifacts.

6. Recommend what to update:
   - requirement inventory
   - business rule catalog
   - open questions
   - glossary
   - feature understanding brief
   - no update required

## Inputs

### Manual input

The user will provide a pasted text snippet in chat.

Example format:

```text
raidcom modify snapshot -splt_time_id <SPLT-TIME-ID> -snapshot_data snapshotgroup_add -snapshotgroup <name>
```

### Primary source-of-truth artifacts

- `output/34_FEATURE_UNDERSTANDING_REVIEW.md`
- `output/33_FEATURE_UNDERSTANDING_BRIEF.md`
- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`
- `output/21_glossary.md`
- `output/12_normalized_evidence.md`

### Supporting inputs, open only when needed

- `output/20_image_analysis.md`
- `output/11_translation_policy.md`
- `output/10_document_inventory.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`
- `working/extracted/formatting_inventory.md`

## Outputs

### Output file to create or update

Create or overwrite:

- `output/35_manual_text_evidence_analysis.md`

## Required output structure

Write `output/35_manual_text_evidence_analysis.md` using this structure:

```markdown
# Manual Text Evidence Analysis

## 1. Analysis Decision

Decision: `Usable as supplemental evidence` / `Usable with warnings` / `Needs clarification` / `Not usable`

Explain the decision briefly.

## 2. Pasted Text Classification

| Field | Value |
|---|---|
| Snippet type | ... |
| Main subject | ... |
| Related feature area | ... |
| Is this primary BRD evidence? | Supplemental focused evidence |
| Active / inactive status | Active / Inactive-strikethrough / Unknown |
| Confidence | High / Medium / Low |

## 3. Extracted Factual Elements

| Element ID | Element | Element Type | Exact Text | Notes |
|---|---|---|---|---|

Element Type examples:

- Command
- Option
- Parameter
- Operation
- Required condition
- Optional condition
- Constraint
- Unsupported case
- State
- Data field
- Unknown

## 4. Plain-English Explanation

Explain what the pasted text says in plain technical English.

Do not introduce behavior that is not visible in the snippet or supported by existing source artifacts.

## 5. Mapping to Source-of-Truth Artifacts

| Snippet Element ID | Related Artifact | Related ID / Section | Relationship | Notes |
|---|---|---|---|---|

Relationship must be one of:

- Confirms existing evidence
- Clarifies existing evidence
- Adds supplemental detail
- Potential conflict
- Not found in existing evidence
- Unclear

## 6. Requirement Candidate Assessment

| Candidate ID | Related Requirement ID | Candidate Requirement / Clarification | Evidence Status | Recommended Action |
|---|---|---|---|---|

Evidence Status must be one of:

- Already covered
- Covered but wording should be clarified
- Missing candidate
- Potential conflict
- Needs BA/customer confirmation
- Not enough context

Do not create final requirement IDs here unless updating `output/30_requirement_inventory.md` is explicitly requested.

## 7. Business Rule Candidate Assessment

| Candidate ID | Related Rule ID | Candidate Rule / Clarification | Evidence Status | Recommended Action |
|---|---|---|---|---|

## 8. Terminology / Glossary Impact

| Term / Phrase | Existing Glossary Match | Issue | Recommended Action |
|---|---|---|---|

## 9. Open Questions Impact

| Existing / New Question | Related Snippet Element | Reason | Priority | Recommended Action |
|---|---|---|---|---|

## 10. Recommended Updates

### Update `output/30_requirement_inventory.md`

- ...

### Update `output/31_business_rule_catalog.md`

- ...

### Update `output/32_open_questions.md`

- ...

### Update `output/21_glossary.md`

- ...

### Update `output/33_FEATURE_UNDERSTANDING_BRIEF.md`

- ...

### No update required

- ...

## 11. Risks and Cautions

List any risk of over-interpreting the pasted text.

## 12. Final Summary for BA / Developer

Write a concise summary explaining what should be done next.
```

## Quality rules

- Do not treat a pasted snippet as complete context when it is only a partial command, partial row, or partial paragraph.
- Do not create a final requirement from command syntax alone unless the related behavior is also supported by existing evidence.
- If the snippet only clarifies syntax, recommend updating the related requirement/rule wording rather than creating a new requirement.
- If the snippet confirms an existing requirement/rule, mark it as confirmation and recommend adding an evidence reference.
- If the snippet adds a missing condition, parameter, option, or unsupported case, mark it as a candidate update and require source confirmation through `output/12_normalized_evidence.md` or raw extracted source.
- Preserve exact option spelling such as `-splt_time_id`, `-snapshot_data`, `snapshotgroup_add`, and `-snapshotgroup`.
- Do not expand undefined acronyms.
- Do not rename operation identifiers or command options.
- Keep the analysis concise, technical, and source-bound.

## Stop conditions

- Stop and report `No-Go` if the pasted text is missing.
- Stop and report `No-Go` if required primary artifacts from steps 30–34 are missing.
- Stop and report `Needs clarification` if the pasted text is too short, cropped, or lacks enough context to compare against source artifacts.
- Do not continue to FD/DD/coding from pasted text alone.
