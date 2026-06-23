# 60 - Generate Customer / Domain Expert Q&A

## Purpose

Generate a concise customer/domain expert Q&A list for unresolved items that cannot be safely finalized from the current FD evidence.

Use this step only when the latest FD review or patched FD review indicates that clarification is needed before the FD can be considered safe for customer/domain expert review, DD, coding design, or testing.

This task must not generate, revise, or patch the FD.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent requirements, business rules, messages, screen behavior, command behavior, API behavior, or design decisions.
- Ask only questions that require customer/domain expert clarification.
- Do not ask questions for issues that can be fixed internally from existing source evidence.
- Do not ask questions caused only by AI writing style, formatting, or traceability-table quality.
- Do not expose internal artifact names or internal IDs in the customer-facing Q&A.
- Rewrite internal findings into natural customer-facing questions.
- Preserve source-specific terms, product terms, command names, option names, field names, acronyms, and code-like identifiers exactly unless the translation policy or glossary defines a safe rendering.
- Follow `output/11_translation_policy.md` and `output/21_glossary.md` for terminology control.
- Respect strikethrough/deprecated evidence rules: strikethrough-only content must not become an active behavior question unless it conflicts with active evidence or the source explicitly says otherwise.
- Write the Q&A in English.

### Important

- This is a clarification artifact, not an FD correction task.
- This task should filter questions aggressively.
- The output should be short enough to send to a customer/domain expert.
- If an issue can be corrected internally using `output/30_requirement_inventory.md`, `output/31_business_rule_catalog.md`, `output/32_open_questions.md`, `output/21_glossary.md`, `output/20_image_analysis.md`, or `output/12_normalized_evidence.md`, do not ask the customer.

## Tasks

### Precondition

Use the latest available FD review gate in this order:

1. If `output/55_FD_PATCHED_REVIEW_REPORT.md` exists, use it as the latest review source.
2. Otherwise, if `output/52_FD_REVISED_REVIEW_REPORT.md` exists, use it as the latest review source.
3. Otherwise, use `output/42_FD_REVIEW_REPORT.md`.

Generate Q&A when the latest review result is:

- `No-Go`, or
- `Go with minor corrections`, or
- `Go` but the report explicitly recommends customer/domain expert Q&A.

If the latest review result is `Go` and no customer/domain expert Q&A is recommended, create the output file with a short summary stating that no customer/domain expert questions are required at this time.

### Instructions

1. Review unresolved issues from the latest review report.
2. Cross-check against previous review reports when relevant so repeated unresolved issues are not lost.
3. Cross-check against source-of-truth artifacts to remove questions that can be answered internally.
4. Convert only real source ambiguity or missing source detail into customer/domain expert questions.
5. Group questions by priority and topic.
6. For each question, include a customer-facing source reference.
7. Provide a safe suggested default handling only when a safe default exists.
8. If no safe default exists, use `TBD`.
9. Do not expose internal IDs such as `REQ-xxx`, `BR-xxx`, `TERM-xxx`, `OQ-xxx`, `FIG-xxx`, `TRACE-xxx`, `RTRACE-xxx`, or `PTRACE-xxx`.
10. Do not expose internal artifact names such as requirement inventory, business rule catalog, glossary, image analysis, translation review, traceability, intermediate artifact, prompt, AI, or pipeline.

## Inputs

### Primary inputs

Use the latest available FD and review set:

- `output/55_FD_PATCHED_REVIEW_REPORT.md`, if available
- `output/54_FD_PATCHED_INTERNAL_TRACEABILITY.md`, if available
- `output/53_FD_DRAFT_REVISED_PATCHED.md`, if available
- `output/53_FD_PATCH_LOG.md`, if available

If patched FD artifacts are not available, use the revised FD set:

- `output/52_FD_REVISED_REVIEW_REPORT.md`, if available
- `output/51_FD_REVISED_INTERNAL_TRACEABILITY.md`, if available
- `output/50_FD_DRAFT_REVISED.md`, if available
- `output/50_FD_REVISION_LOG.md`, if available

If revised FD artifacts are not available, use the first FD review set:

- `output/42_FD_REVIEW_REPORT.md`
- `output/41_FD_INTERNAL_TRACEABILITY.md`
- `output/40_FD_DRAFT.md`

### Source-of-truth inputs

Use these to decide whether a question is genuinely needed or can be resolved internally:

- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`
- `output/21_glossary.md`
- `output/20_image_analysis.md`
- `output/12_normalized_evidence.md`

### Supporting inputs, open only when needed

- `output/11_translation_policy.md`
- `output/10_document_inventory.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`
- `working/extracted/image_inventory_raw.md`

## Outputs

### Output file to create or update

Create or overwrite:

- `output/60_CUSTOMER_QA.md`

## Required output structure

Write `output/60_CUSTOMER_QA.md` using this structure:

```markdown
# Customer / Domain Expert Q&A

## 1. Summary

Include:

- Purpose of this Q&A
- Latest review source used
- Number of questions
- Main clarification areas
- Impact if unanswered
- Whether the FD can proceed internally while waiting for answers

## 2. High Priority Questions

| QID | Category | Question | Source Reference | Why Clarification Is Needed | Impact If Unresolved | Suggested Default Handling |
|---|---|---|---|---|---|---|

## 3. Medium Priority Questions

| QID | Category | Question | Source Reference | Why Clarification Is Needed | Impact If Unresolved | Suggested Default Handling |
|---|---|---|---|---|---|---|

## 4. Low Priority Questions

| QID | Category | Question | Source Reference | Why Clarification Is Needed | Impact If Unresolved | Suggested Default Handling |
|---|---|---|---|---|---|---|

## 5. Questions by Topic

### Business behavior

- ...

### Operation flow

- ...

### Data definition

- ...

### UI / API behavior

- ...

### Error / warning handling

- ...

### Terminology

- ...

### Diagram / visual ambiguity

- ...

### Non-functional / performance

- ...

### Source contradiction

- ...

## 6. Items Not Asked

List items intentionally not included as customer questions because they can be resolved internally.

| Item | Reason Not Asked | Internal Resolution |
|---|---|---|

## 7. Internal Filtering Notes

This section is internal and may mention review source names only if needed for team traceability.
Do not send this section to the customer unless explicitly approved.

Include:

- Issues removed because they are writing/style-only
- Issues removed because existing evidence already answers them
- Issues removed because they are internal traceability problems
- Issues converted into customer-facing questions
```

## Field definitions

- QID: Use `Q-001`, `Q-002`, etc.
- Category must be one of:
  - Business behavior
  - Operation flow
  - Data definition
  - UI/API behavior
  - Error/warning handling
  - Terminology
  - Diagram / visual ambiguity
  - Non-functional / performance
  - Source contradiction
  - Other
- Question: one clear customer-facing question.
- Source Reference: customer-facing source reference such as section, paragraph, table, note, footnote, figure, or diagram caption.
- Why Clarification Is Needed: explain the ambiguity or missing detail.
- Impact If Unresolved: explain impact on FD, DD, implementation, testing, operation, or customer acceptance.
- Suggested Default Handling:
  - Use `TBD` if no safe default exists.
  - Use `Treat as unsupported` only if the source leans that way.
  - Use `Keep current FD behavior` only if existing evidence is strong enough.
  - Use `Requires confirmation before DD/coding` when the FD can stay cautious but downstream work should wait.
  - Do not invent a default.

## Priority rules

- High: blocks FD behavior, business rule, unsupported behavior, data definition, testability, or customer acceptance.
- Medium: affects design clarity or downstream DD/testing but does not block the main FD.
- Low: wording preference, terminology preference, minor diagram clarification, or low-impact confirmation.

## Question writing rules

- Ask one thing per question.
- Use concise professional English.
- Do not expose internal IDs or internal artifact names.
- Do not mention Copilot, AI, model, prompt, pipeline, traceability, requirement inventory, business rule catalog, glossary, image analysis, or translation review.
- Use customer-facing source references only.
- Do not ask the customer to confirm obvious facts already clear in the source.
- Do not ask questions caused by hallucination; classify those as internal fixes instead.
- Do not ask implementation questions unless the source requires technical behavior that affects FD/DD/testing.
- Preserve exact command names, option names, parameters, product terms, acronyms, and field names.
- If a question comes from figure-only behavior, phrase it carefully: `For the scenario shown in the figure, please confirm whether...`
- If a question comes from source contradiction, state both sides neutrally without blaming the source.

Recommended wording examples:

- `Please confirm whether...`
- `Should the system...`
- `When <condition>, what is the expected behavior?`
- `Is <term> intended to mean...?`
- `For the scenario shown in the figure, should...?`
- `If <case> occurs, should it be treated as unsupported, warning, or error?`

## Quality rules

- Every question must be tied to source ambiguity or missing source detail.
- Every question must have a source reference.
- High priority questions must be genuinely blocking or high impact.
- Do not include questions that can be answered from existing evidence.
- Do not include questions that only reflect AI writing quality.
- Do not include questions that only reflect internal traceability formatting.
- Keep the Q&A concise enough for customer/domain expert review.

## Stop conditions

- Stop and report `No-Go` if no FD review report is available from step 42, 52, or 55.
- Stop and report `No-Go` if source-of-truth artifacts from steps 30, 31, 32, 21, 20, and 12 are missing.
- Do not generate or revise FD content in this step.
- Do not continue to DD/coding from Q&A alone.
