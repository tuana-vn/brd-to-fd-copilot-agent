# 33 - Generate Feature Understanding Brief

## Purpose

Generate a concise Feature Understanding Brief from the source-bound requirement artifacts so that BA, developer, reviewer, or project member can quickly understand what the feature does before reading the full Functional Design.

This is an internal onboarding artifact. It is **not** a customer-facing Functional Design, Detailed Design, coding design, or implementation plan.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent business rules, data fields, screens, actors, APIs, states, flows, components, or implementation design.
- Preserve source-specific terms unless the translation policy or glossary explicitly defines an approved rendering.
- Follow the glossary for locked terms, acronyms, field names, operation names, product-specific terms, and unknown terms.
- Mark ambiguous, missing, or conflicting information instead of guessing.
- Do not convert assumptions into facts.
- Do not hide ambiguity. Put ambiguity in the Open Questions section.
- Write outputs in English by default.
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

For the Feature Understanding Brief, do not describe strikethrough-only content as current scope, current flow, current rule, or current operation. If important, mention it only in Internal Evidence Notes as deprecated/struck-through context.

### Important

- This is a fast understanding artifact for internal BA/developer onboarding.
- This is not the final FD.
- This is not a substitute for requirement review.
- This must be understandable to a team member who has not read the Japanese BRD.

## Tasks

### Precondition

Use the latest effective requirement extraction state:

- Required:
  - `output/30_requirement_inventory.md`
  - `output/31_business_rule_catalog.md`
  - `output/32_open_questions.md`
- Recommended:
  - `output/20_image_analysis.md`
  - `output/21_glossary.md`

If any required file is missing, stop and report `No-Go`.

If requirement extraction contains high-risk open questions, still generate the brief but clearly state the risks and unresolved areas.

### Instructions

Create `output/33_FEATURE_UNDERSTANDING_BRIEF.md`.

The brief should help the reader answer:

- What is this feature?
- Why does it exist?
- Who uses it or what system calls it?
- What business process does it support?
- What is the main flow?
- What are the key inputs and outputs?
- What business rules, validations, constraints, or unsupported cases matter most?
- What is unclear and should be asked before FD/DD/coding?

Use `output/30_requirement_inventory.md`, `output/31_business_rule_catalog.md`, and `output/32_open_questions.md` as the primary source. Use `output/20_image_analysis.md` and `output/21_glossary.md` only to clarify diagrams and terminology.

Do not read raw Japanese source files by default. Open raw source only if the requirement artifacts contain a suspicious or unclear reference that must be verified.

## Inputs

### Primary inputs

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

## Outputs

### Output file to create or update

- `output/33_FEATURE_UNDERSTANDING_BRIEF.md`

### Language policy

Default output language: English.

If the user explicitly asks for Vietnamese, generate the brief in Vietnamese, but keep original Japanese source terms, field names, screen names, API names, operation names, acronyms, and product-specific terms unchanged unless the glossary provides an approved translation.

When a Japanese term is important and the English/Vietnamese meaning is uncertain, preserve the original Japanese term and add a short note such as `meaning unclear from source`.

### Output structure

Write `output/33_FEATURE_UNDERSTANDING_BRIEF.md` using this structure:

```markdown
# Feature Understanding Brief

## 1. Feature Summary
Briefly explain what this feature does and why it exists.

## 2. Business Context
Explain where this feature fits in the business process or operational scenario.

## 3. Users / Actors / External Systems
List known users, actors, roles, systems, APIs, jobs, or external parties involved.
If unknown, say so.

## 4. Scope Overview
### In Scope
List source-supported in-scope functions, screens, APIs, jobs, files, operations, or behaviors.

### Out of Scope / Not Confirmed
List items that are excluded, unsupported, unclear, or not confirmed by the source.

## 5. Main Flow
Describe the normal flow in simple numbered steps.
Each step must be evidence-supported.

## 6. Alternative / Exception Flows
Describe validation errors, branch flows, unsupported operations, error handling, state restrictions, or special cases if supported by the source.

## 7. Key Inputs
List major input data, screen fields, request parameters, command parameters, files, or upstream data.
Use a table when helpful.

## 8. Key Outputs
List major outputs, displayed data, saved data, response data, generated files, reports, status changes, or downstream updates.
Use a table when helpful.

## 9. Business Rules and Validations
Summarize important rules, conditions, formulas, mappings, status transitions, validations, and unsupported cases.
Do not invent missing rules.

## 10. Data / Entity Understanding
Summarize important entities, records, tables, objects, identifiers, statuses, or data groups if source-supported.
Avoid physical database design unless the BRD clearly states it.

## 11. Screens / UI / API / Command Understanding
Summarize screens, UI actions, API behavior, command syntax, parameters, messages, or system operations if source-supported.

## 12. Messages / Error Handling
Summarize important messages, warnings, errors, command rejection behavior, failure behavior, and system responses.

## 13. Diagrams / Images Used as Evidence
List diagrams/images that contributed to understanding.
For each item, explain what was understood from it and whether it was confirmed by text or figure-only.

## 14. Open Questions
List unclear, incomplete, or contradictory points that BA/customer should clarify.
Each question should include why it matters.

## 15. Developer Notes for Next Design Step
List practical notes that will help FD/DD/coding later, such as validations to preserve, data dependencies, unclear integration points, risky assumptions, or test-sensitive rules.
Do not write implementation design unless directly supported by source evidence.

## 16. Internal Evidence Notes
This section is internal and may contain source IDs, file references, image IDs, requirement IDs, rule IDs, and open-question IDs.
Do not copy this section into customer-facing FD unless explicitly requested.
```

## Required output quality

- Be concise but complete.
- Prefer plain language over formal specification language.
- Use tables only when they improve readability.
- Keep source terms stable and glossary-controlled.
- Do not expose prompt pipeline details except in `Internal Evidence Notes`.
- Do not claim the feature is fully understood if open questions remain.
- Every major claim must be supported by requirement inventory, rule catalog, image analysis, glossary, or open-question artifacts.
- Ambiguity must be listed as an open question.
- No customer-facing FD language should be mixed with internal trace notes except in the internal section.
- The brief must not pretend to be DD or coding design.

## Stop conditions

Stop and report `No-Go` if:

- `output/30_requirement_inventory.md` is missing.
- `output/31_business_rule_catalog.md` is missing.
- `output/32_open_questions.md` is missing.
- The brief would require unsupported assumptions.
- Requirement artifacts are clearly incomplete or internally contradictory in a way that prevents a useful understanding brief.

Do not stop only because open questions exist. Include them clearly in the brief.
