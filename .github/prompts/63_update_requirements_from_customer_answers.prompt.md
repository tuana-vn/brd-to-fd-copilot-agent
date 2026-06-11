# 63 - Update Requirements from Customer Answers

## Purpose

Create updated internal requirement, business rule, and open-question artifacts after incorporating normalized customer/domain expert answers as supplemental evidence.

This task updates the internal evidence layer after Q&A. It does **not** generate or revise the customer-facing Functional Design.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not overwrite the original pre-Q&A artifacts.
- Treat customer/domain expert answers as supplemental evidence, not as edits to the original BRD.
- Do not silently merge customer answers into the original source evidence.
- Do not over-apply a narrow customer answer to unrelated requirements, rules, terms, diagrams, or flows.
- Do not invent requirements, business rules, validations, command behavior, UI/API behavior, or design decisions.
- Preserve command names, option names, field names, product-specific terms, acronyms, and code-like identifiers exactly.
- Follow `output/21_glossary.md` and `output/11_translation_policy.md`.
- Respect strikethrough/deprecated evidence rules:
  - strikethrough-only source content is inactive/deprecated evidence unless the source explicitly says otherwise.
  - customer answers must not accidentally revive strikethrough-only behavior as active behavior unless the answer explicitly confirms that behavior should be active.
- Keep all output in English.

## Tasks

### Precondition

Use the customer-answer impact decision from:

- `output/62_customer_answer_impact_analysis.md`

Proceed only when step 62 recommends one of the following:

- `Proceed to 63_update_requirements_from_customer_answers`
- `Proceed to 63 then 70`
- equivalent wording that requires updating internal requirements/rules/questions before regenerating the FD

If step 62 recommends `Proceed directly to 70_generate_fd_after_customer_answers`, do not rewrite requirement/rule artifacts. Report that step 63 is not required.

If step 62 recommends `Generate follow-up Q&A` or `Stop for human decision`, stop and report `No-Go` with the reason.

### Instructions

1. Read the normalized customer answer inventory and impact analysis.
2. Start from the existing pre-Q&A internal artifacts:
   - `output/30_requirement_inventory.md`
   - `output/31_business_rule_catalog.md`
   - `output/32_open_questions.md`
3. Apply only customer-answer impacts that are explicitly supported by `output/61_customer_answer_inventory.md` and `output/62_customer_answer_impact_analysis.md`.
4. Preserve all unaffected requirements, rules, and open questions.
5. Add, update, close, or reclassify items only when the answer evidence supports it.
6. If a customer answer contradicts original source evidence, do not silently override the source. Mark the contradiction and keep or add an open question unless the answer is explicitly authoritative and the project team has accepted it.
7. If a customer answer is partial, update only the answered portion and keep unresolved parts as open questions.
8. If a customer answer affects terminology only, update term references and meaning-risk notes as needed, but do not create behavior requirements unless behavior is explicitly defined.
9. Do not generate FD content.

## Inputs

### Primary inputs

- `output/61_customer_answer_inventory.md`
- `output/62_customer_answer_impact_analysis.md`
- `output/60_CUSTOMER_QA.md`
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

## Outputs

### Output files to create or update

- `output/63_requirement_inventory_after_qa.md`
- `output/64_business_rule_catalog_after_qa.md`
- `output/65_open_questions_after_qa.md`

Do not overwrite:

- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`

## Required output structure

### Output 1: `output/63_requirement_inventory_after_qa.md`

Create the updated requirement inventory using this table:

| Requirement ID | Change Status | Requirement Title | Requirement Type | Description | Actor / Component | Trigger | Preconditions | Main Behavior | Alternative / Exception Behavior | Input Data | Output Data | Related Terms | Source Reference | Supplemental Answer Reference | Evidence Type | Confidence | Meaning Risk | Related Rule IDs | Open Questions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

#### Requirement ID rules

- Preserve existing `REQ-xxx` IDs from `output/30_requirement_inventory.md` for unchanged or updated requirements.
- Use new IDs only for answer-derived requirements, continuing the existing sequence.
- Do not reuse an ID for a different meaning.

#### Change Status values

- `Unchanged`
- `Updated by customer answer`
- `Added by customer answer`
- `Converted from open question`
- `Converted from assumption`
- `Converted to open question`
- `Removed / not supported`
- `Requires confirmation`

#### Evidence Type values

- `Confirmed by original text`
- `Confirmed by original table`
- `Confirmed by original figure`
- `Inferred from original figure`
- `Confirmed by customer answer`
- `Mixed original + customer answer`
- `Open question`

#### Requirement update rules

- Preserve existing source-supported requirements unless customer answers explicitly change or clarify them.
- Add answer-derived requirements only when the customer answer explicitly defines behavior.
- Do not convert vague customer comments into mandatory behavior.
- If an answer resolves an open question, update the requirement and reference the answer.
- If an answer is partial, keep unresolved parts as open questions.
- If an answer contradicts original source evidence, mark the risk and link to an open question unless explicitly accepted as authoritative.
- Do not create requirements from customer-answer implications that are not stated.

After the table, add:

```markdown
## Requirement Update Summary

- Requirements unchanged: ...
- Requirements updated by customer answer: ...
- Requirements added by customer answer: ...
- Requirements converted from open questions: ...
- Requirements still requiring confirmation: ...
- Contradiction-related requirements: ...
```

### Output 2: `output/64_business_rule_catalog_after_qa.md`

Create the updated business rule catalog using this table:

| Rule ID | Change Status | Rule Statement | Rule Type | Condition | Action / Constraint | Negative / Unsupported Case | Affected Function / Component | Related Requirement IDs | Related Terms | Source Reference | Supplemental Answer Reference | Evidence Type | Confidence | Meaning Risk | Test Implication | Open Questions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

#### Rule ID rules

- Preserve existing `BR-xxx` IDs from `output/31_business_rule_catalog.md` for unchanged or updated rules.
- Use new IDs only for answer-derived rules, continuing the existing sequence.
- Do not reuse an ID for a different meaning.

#### Change Status values

- `Unchanged`
- `Updated by customer answer`
- `Added by customer answer`
- `Converted from open question`
- `Converted to open question`
- `Removed / not supported`
- `Requires confirmation`

#### Business rule update rules

- Preserve original rules unless customer answers change or clarify them.
- Add answer-derived rules only when the customer answer explicitly defines a rule, condition, validation, unsupported case, error/warning handling, data rule, or operation constraint.
- Do not strengthen optional, partial, or ambiguous answers into mandatory rules.
- If the customer answer clarifies unsupported behavior, preserve it explicitly.
- If a rule remains unclear, keep it linked to an open question.
- Update test implications when a rule changes.

After the table, add:

```markdown
## Business Rule Update Summary

- Rules unchanged: ...
- Rules updated by customer answer: ...
- Rules added by customer answer: ...
- Rules converted from open questions: ...
- Rules still requiring confirmation: ...
- Contradiction-related rules: ...
```

### Output 3: `output/65_open_questions_after_qa.md`

Create the updated open question list using this table:

| Question ID | Change Status | Category | Question | Reason | Related Requirement IDs | Related Rule IDs | Related Terms | Source Reference | Supplemental Answer Reference | Priority |
|---|---|---|---|---|---|---|---|---|---|---|

#### Question ID rules

- Preserve existing `OQ-xxx` IDs from `output/32_open_questions.md` for still-open, partially answered, or closed questions.
- Use new IDs only for new questions introduced after customer answers.
- Do not reuse an ID for a different meaning.

#### Change Status values

- `Still open`
- `Answered / closed`
- `Partially answered`
- `New after customer answer`
- `Converted to requirement`
- `Converted to business rule`
- `Contradiction remains`
- `No longer applicable`

#### Open question update rules

- Close questions that are fully answered.
- Keep partially answered questions open with an updated reason.
- Create new questions for contradictions introduced by customer answers.
- Create new questions where an answer changes behavior but lacks enough detail.
- Do not hide uncertainty inside requirements or business rules.

After the table, add:

```markdown
## Open Question Update Summary

- Open questions closed: ...
- Open questions partially answered: ...
- Open questions still open: ...
- New open questions after customer answers: ...
- Contradictions remaining: ...
```

### Customer Answer Application Summary

After creating all three files, include a concise summary in each output file or create a shared final section if the tool writes all outputs together:

- Requirements updated
- Requirements added
- Rules updated
- Rules added
- Open questions closed
- Open questions still open
- New open questions
- Source contradictions remaining
- Recommended next step: `70_generate_fd_after_customer_answers`, `Generate follow-up Q&A`, or `Stop for human decision`

## Required output quality

- All outputs must be English.
- Every customer-answer-derived change must reference an `ANS-xxx` answer ID.
- Every requirement/rule/open-question item must preserve source references where available.
- No original artifact is overwritten.
- No customer answer is over-applied.
- Unresolved contradiction or uncertainty must remain visible.
- Strikethrough-only source content must not be converted into active requirements/rules unless explicitly confirmed by customer answer.

## Stop conditions

- Stop and report `No-Go` if `output/61_customer_answer_inventory.md` or `output/62_customer_answer_impact_analysis.md` is missing.
- Stop and report `No-Go` if any required original artifact `30/31/32` is missing.
- Stop and report `No-Go` if customer answers are too ambiguous to safely update the affected artifacts.
- Stop and report `No-Go` if step 62 recommends follow-up Q&A or human decision instead of updating artifacts.
- Do not generate FD in this step.
