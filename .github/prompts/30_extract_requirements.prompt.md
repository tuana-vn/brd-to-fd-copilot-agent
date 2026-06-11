# 30 - Extract Requirements

## Purpose

Extract a source-bound requirement inventory, business rule catalog, and open question list from the normalized BRD evidence.

This step converts controlled evidence into requirement-level working artifacts. It does **not** generate the customer-facing Functional Design, Detailed Design, coding design, or implementation tasks.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent requirements, field meanings, business rules, messages, screen behavior, diagrams, APIs, components, or implementation design.
- Preserve source-specific terms unless the translation policy or glossary explicitly defines an approved rendering.
- Follow the glossary for locked terms, acronyms, field names, operation names, product-specific terms, and unknown terms.
- Mark ambiguous, missing, or conflicting information instead of guessing.
- Do not convert assumptions into confirmed requirements.
- Do not turn figure-inferred behavior into confirmed text behavior.
- Write outputs in English unless a source value must remain unchanged.
- Do not modify the original BRD. Customer answers are supplemental evidence only.

### Formatting evidence rules

- Treat source formatting as evidence when it changes meaning.
- Strikethrough text means inactive, deleted, deprecated, superseded, or draft-removed evidence unless the source explicitly says otherwise.
- Do not treat strikethrough-only text as active requirement behavior, active business rules, active operation flow, active field definitions, or active UI/API behavior.
- If a paragraph, table cell, caption, or figure note contains both active and strikethrough text, use only the non-strikethrough portion as active evidence.
- Preserve strikethrough evidence in traceability notes when it helps explain removed or deprecated behavior.
- If strikethrough content conflicts with active evidence, prefer active non-strikethrough evidence and record the struck-through content as deprecated/conflict context, not as a confirmed requirement.
- Highlighted text is not automatically active or mandatory. If highlighted text is also strikethrough, the strikethrough rule wins.
- If formatting status is unclear or missing from upstream artifacts, mark the affected item as ambiguous instead of guessing.

For requirement extraction, strikethrough-only content must not create REQ or BR items. If the struck-through content indicates a removed operation, record it only as deprecated context or as an open question when active evidence is contradictory. Unsupported behavior explicitly stated in active non-strikethrough evidence remains valid and must be captured as an operation constraint.

### Important

- This is not FD generation.
- This is not DD generation.
- This is not coding design.
- This is controlled requirement extraction from approved evidence.

## Tasks

### Precondition

Use the latest effective translation gate:

- If `output/15_translation_review_followup_report.md` exists, use it as the latest translation gate.
- Otherwise, use `output/13_translation_review_report.md`.
- Continue only if the latest gate is `Go` or `Go with warnings`.
- Stop if the latest gate is `No-Go`.

Use only approved evidence:

- Text evidence from `output/12_normalized_evidence.md`.
- Figure evidence from `output/20_image_analysis.md`.
- Terminology from `output/21_glossary.md`.
- Translation rules from `output/11_translation_policy.md`.
- Source inventory references from `output/10_document_inventory.md`.

Use raw extracted Japanese files only for targeted verification when the approved evidence is unclear or suspicious. Do not use raw source files as the primary extraction input.

### Instructions

Create three output files:

1. `output/30_requirement_inventory.md`
2. `output/31_business_rule_catalog.md`
3. `output/32_open_questions.md`

Extract requirements and rules only when there is source-supported evidence.

Approved evidence means:

- Confirmed text evidence from `output/12_normalized_evidence.md`.
- Confirmed table evidence represented in `output/12_normalized_evidence.md`.
- Confirmed figure evidence from `output/20_image_analysis.md`.
- Figure-inferred behavior only when clearly marked as `Inferred from figure`.
- Terminology controlled by `output/21_glossary.md`.

Do not create requirements from:

- assumptions
- unclear translations
- unresolved terminology
- unresolved contradictions
- generic domain knowledge
- expected system behavior not stated by evidence
- implementation preferences
- your own interpretation of how the system should work

## Inputs

### Primary inputs

- `output/12_normalized_evidence.md`
- `output/20_image_analysis.md`
- `output/21_glossary.md`
- latest effective translation gate report:
  - `output/15_translation_review_followup_report.md`, if present
  - otherwise `output/13_translation_review_report.md`

### Supporting inputs, open only when needed

- `output/10_document_inventory.md`
- `output/11_translation_policy.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`
- `working/extracted/image_inventory_raw.md`
- `working/extracted/formatting_inventory.md`, if present
- `working/extracted/comments.md`, if present
- `working/extracted/footnotes_endnotes.md`, if present

Use supporting inputs only to verify source references, exact Japanese terms, table details, formatting notes, comments, footnotes, or suspicious evidence.

## Outputs

### Output files to create or update

- `output/30_requirement_inventory.md`
- `output/31_business_rule_catalog.md`
- `output/32_open_questions.md`

### Output 1: `output/30_requirement_inventory.md`

Create the requirement inventory using this table:

| Requirement ID | Requirement Title | Requirement Type | Description | Actor / Component | Trigger | Preconditions | Main Behavior | Alternative / Exception Behavior | Input Data | Output Data | Related Terms | Source Reference | Evidence Type | Confidence | Meaning Risk | Related Rule IDs | Open Questions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Field definitions:

- Requirement ID: Use `REQ-001`, `REQ-002`, etc.
- Requirement Type must be one of:
  - Functional
  - Business rule
  - Operation constraint
  - Data definition
  - UI/API behavior
  - Time-based behavior
  - Error/warning behavior
  - Non-functional
  - TBD
- Description: concise English description.
- Actor / Component: user, system, external system, batch, API, component, or `TBD`.
- Trigger: event/action that starts the behavior, or `TBD`.
- Preconditions: conditions that must be true before behavior applies.
- Main Behavior: confirmed behavior.
- Alternative / Exception Behavior: exception, unsupported case, negative condition, or special handling.
- Input Data: data needed by the behavior, or `TBD`.
- Output Data: data/result/message/state change, or `TBD`.
- Related Terms: term IDs from `output/21_glossary.md`.
- Source Reference: normalized evidence item, paragraph, table, note, figure, or image analysis item.
- Evidence Type must be one of:
  - Confirmed by text
  - Confirmed by table
  - Confirmed by figure
  - Inferred from figure
  - Mixed evidence
- Confidence: High / Medium / Low.
- Meaning Risk: None / Low / Medium / High.
- Related Rule IDs: IDs from `output/31_business_rule_catalog.md`.
- Open Questions: question IDs from `output/32_open_questions.md`.

Rules for requirement extraction:

- Every requirement must have a source reference.
- Every requirement must use glossary-controlled terminology.
- If evidence is figure-only, clearly mark it as `Confirmed by figure` or `Inferred from figure`.
- If a statement is inferred from a figure, do not present it as confirmed text behavior.
- Preserve source-supported conditions, exceptions, negative statements, notes, and footnotes.
- If a requirement depends on uncertain terminology, keep it only if evidence supports it, mark Confidence as Low or Medium, and add an open question.
- If the source says something is unsupported, represent it as an operation constraint or exception behavior.
- Do not merge unrelated requirements.
- Do not split one atomic rule into multiple duplicate requirements unless needed for traceability.
- Do not create requirements from assumptions.

### Output 2: `output/31_business_rule_catalog.md`

Create the business rule catalog using this table:

| Rule ID | Rule Statement | Rule Type | Condition | Action / Constraint | Negative / Unsupported Case | Affected Function / Component | Related Requirement IDs | Related Terms | Source Reference | Evidence Type | Confidence | Meaning Risk | Test Implication | Open Questions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Field definitions:

- Rule ID: Use `BR-001`, `BR-002`, etc.
- Rule Type must be one of:
  - Validation
  - Eligibility
  - Operation constraint
  - Data mapping
  - Naming / field rule
  - Time-based rule
  - State transition
  - Error/warning rule
  - Unsupported behavior
  - TBD
- Rule Statement: concise English business rule.
- Condition: when the rule applies.
- Action / Constraint: what the system must do or enforce.
- Negative / Unsupported Case: what is not allowed or not supported.
- Affected Function / Component: target function/component, or `TBD`.
- Related Requirement IDs: requirement IDs from `output/30_requirement_inventory.md`.
- Related Terms: term IDs from `output/21_glossary.md`.
- Source Reference: normalized evidence item, paragraph, table, note, figure, or image analysis item.
- Evidence Type must be one of:
  - Confirmed by text
  - Confirmed by table
  - Confirmed by figure
  - Inferred from figure
  - Mixed evidence
- Confidence: High / Medium / Low.
- Meaning Risk: None / Low / Medium / High.
- Test Implication: how this rule should be tested at a requirement/functional level, not implementation-level test design.
- Open Questions: question IDs from `output/32_open_questions.md`.

Rules for business rule extraction:

- Preserve exact conditions.
- Preserve negative statements and unsupported operations.
- Preserve exceptions, notes, footnotes, comments, and formatting warnings when they affect behavior.
- Do not soften mandatory language into optional language.
- Do not strengthen optional/ambiguous language into mandatory behavior.
- Do not turn terminology notes into behavior rules unless the source clearly defines behavior.
- Use glossary terms exactly as controlled by `output/21_glossary.md`.

### Output 3: `output/32_open_questions.md`

Create open questions grouped by these categories:

1. Business behavior
2. Data definition
3. Operation flow
4. UI/API behavior
5. Terminology
6. Diagram ambiguity
7. Translation uncertainty
8. Source contradiction
9. Testability

Use this table:

| Question ID | Category | Question | Reason | Related Requirement IDs | Related Rule IDs | Related Terms | Source Reference | Priority |
|---|---|---|---|---|---|---|---|---|

Field definitions:

- Question ID: Use `OQ-001`, `OQ-002`, etc.
- Priority: Critical / High / Medium / Low.

Rules for open questions:

- Create an open question for any unresolved contradiction.
- Create an open question for any term with Medium or High meaning risk if it affects behavior.
- Create an open question when source evidence is insufficient to define trigger, precondition, exception, data, or component.
- Create an open question when image evidence adds behavior not confirmed by text.
- Create an open question when translation uncertainty affects behavior.
- Do not hide uncertainty inside requirement descriptions.

## Required output quality

- Outputs must be English.
- Follow `output/11_translation_policy.md` and `output/21_glossary.md` strictly.
- Keep acronyms, field names, product terms, operation identifiers, and source-specific terms unchanged unless a controlled rendering exists.
- Do not expand undefined acronyms.
- Do not rename field names, product-specific terms, operation identifiers, or code-like identifiers.
- If a glossary term has Medium or High meaning risk, reference the term but add an open question if it affects requirement behavior.
- If a term is missing from the glossary but appears necessary for requirement extraction, add an open question instead of inventing a definition.
- Every requirement and business rule must have a source reference.
- Every figure-derived item must be clearly marked.
- Negative statements and unsupported cases must be preserved.
- Conditions, exceptions, notes, comments, and footnotes must not be omitted when they affect behavior.
- No FD/DD design decisions may be introduced.
- No implementation architecture may be invented.
- No requirement may be created from generic domain knowledge.

## Stop conditions

Stop and report `No-Go` without creating final requirement outputs if:

- Required primary inputs are missing.
- The latest effective translation gate is `No-Go`.
- `output/20_image_analysis.md` is required for figure-dependent behavior but is missing or clearly incomplete.
- `output/21_glossary.md` is missing and terminology risk prevents safe extraction.
- The output would require unsupported assumptions.

Do not stop only because some figure details are unreadable or ambiguous. Capture those as open questions unless they block understanding of a critical requirement.
