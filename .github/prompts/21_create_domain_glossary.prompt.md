# 21 - Create Domain Glossary

## Purpose

Create a controlled Japanese-English domain glossary for downstream requirement extraction and Functional Design generation.

This glossary consolidates terminology from normalized text evidence, extracted tables, and analyzed embedded images. It is not a requirement document and must not create new business behavior.

The glossary must help later prompts avoid:

- inconsistent translation
- hallucinated acronym expansion
- incorrect business interpretation
- accidental renaming of field names, product terms, operation names, or code-like identifiers
- treating terminology assumptions as confirmed requirements

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent requirements, field meanings, business rules, messages, screen behavior, or diagrams.
- Preserve source-specific terms unless the translation policy or prior glossary evidence explicitly defines a safe English rendering.
- Mark ambiguous, missing, or conflicting information instead of guessing.
- Write outputs in English unless the source value must remain unchanged.
- Do not generate FD.
- Do not extract final requirements.
- Do not rewrite source behavior.
- Do not modify the original BRD.
- Customer answers are supplemental evidence only.
- Internal review and traceability files may use internal IDs.
- Customer-facing content must not expose internal pipeline terms or internal IDs.

### Formatting evidence rules

- Treat source formatting as evidence when it changes meaning.
- Strikethrough text means inactive, deleted, deprecated, superseded, or draft-removed evidence unless the source explicitly says otherwise.
- Do not treat strikethrough-only text as active requirement behavior, active business rules, active operation flow, active field definitions, or active UI/API behavior.
- If a paragraph, table cell, caption, or figure note contains both active and strikethrough text, use only the non-strikethrough portion as active evidence.
- Preserve strikethrough evidence in traceability notes when it helps explain removed or deprecated behavior.
- If strikethrough content conflicts with active evidence, prefer active non-strikethrough evidence and record the struck-through content as deprecated/conflict context, not as a confirmed requirement.
- Highlighted text is not automatically active or mandatory. If highlighted text is also strikethrough, the strikethrough rule wins.
- If formatting status is unclear or missing from upstream artifacts, mark the affected item as ambiguous instead of guessing.

For glossary creation, terms appearing only in strikethrough text may be included only when useful for traceability, and must be marked with Meaning Risk = High or Notes = Deprecated / struck-through evidence only. Do not lock a term solely because it appears in strikethrough text unless it also appears in active evidence or the translation policy locks it.

### Important

This is terminology control, not requirement analysis.

A glossary entry may explain what a term appears to mean based on evidence, but it must not convert that meaning into a confirmed requirement unless the source explicitly states it.

## Tasks

### Precondition

Use the latest effective translation gate:

- If `output/15_translation_review_followup_report.md` exists, use it as the latest translation gate.
- Otherwise, use `output/13_translation_review_report.md`.
- Continue only if the latest translation gate is `Go` or `Go with warnings`.
- Stop if the latest translation gate is `No-Go`.

Use the latest controlled evidence artifacts:

- Use `output/12_normalized_evidence.md` as the primary normalized text/table evidence.
- Use `output/20_image_analysis.md` as figure/image evidence.
- Use `output/11_translation_policy.md` as the source of truth for locked translation policy terms.
- Use `output/10_document_inventory.md` only as supporting source navigation when source references need to be checked.
- Use raw Japanese source files only for targeted verification of exact source terms, not as the primary working input.

### Instructions

Create a glossary that later prompts can use consistently.

For each term:

1. Identify the original source term.
2. Provide the safest English or normalized rendering.
3. Decide whether the original term must be preserved.
4. Classify the term type.
5. Explain only the source-supported meaning.
6. Record the source reference.
7. Identify the evidence type.
8. Assign translation confidence and meaning risk.
9. Define a usage rule for downstream prompts.
10. Capture notes or open questions for uncertainty.

Include terms from:

- Japanese domain terms
- acronyms
- field names
- operation names
- command names
- UI/API terms
- product-specific terms
- table terms
- footnotes and notes
- embedded image / figure terms from `output/20_image_analysis.md`

Do not include common words unless they are domain-significant or translation-sensitive.

## Inputs

### Primary inputs

Use these inputs by default:

- `output/11_translation_policy.md`
- `output/12_normalized_evidence.md`
- `output/20_image_analysis.md`
- latest effective translation gate report:
  - `output/15_translation_review_followup_report.md`, if present
  - otherwise `output/13_translation_review_report.md`

### Supporting inputs

Open these only when needed for source navigation or exact-term verification:

- `output/10_document_inventory.md`
- `working/extracted/document_text.md`
- `working/extracted/tables.md`
- `working/extracted/formatting_inventory.md`, if present
- `working/extracted/external_references.md`, if present

Do not load raw source files unnecessarily when the controlled evidence artifacts already provide enough information.

## Outputs

### Output file to create or update

- `output/21_glossary.md`

### Required output structure

Create `output/21_glossary.md` with the following structure.

# Domain Glossary

## 1. Review basis

Summarize:

- latest translation gate used
- primary input files used
- supporting input files used, if any
- whether image-derived terms were included
- any important limitations

## 2. Glossary table

| Term ID | Source Term | English / Normalized Term | Keep Original? | Term Type | Meaning Based on Source Evidence | Source Reference | Evidence Type | Translation Confidence | Meaning Risk | Usage Rule | Notes / Open Questions |
|---|---|---|---|---|---|---|---|---|---|---|---|

Field definitions:

- Term ID: Use `TERM-001`, `TERM-002`, etc.
- Source Term: Original Japanese term, acronym, field name, operation name, command name, product term, or figure term.
- English / Normalized Term: Controlled English rendering.
- Keep Original?: `Yes`, `No`, or `Partial`.
- Term Type must be one of:
  - Acronym
  - Field name
  - Operation
  - Command
  - Business term
  - Technical term
  - UI/API term
  - Product-specific term
  - Figure term
  - Table term
  - Unknown
- Meaning Based on Source Evidence: Explain only what the source supports.
- Source Reference: Paragraph, table, figure, document inventory item, normalized evidence item, or image analysis item.
- Evidence Type must be one of:
  - Confirmed by translation policy
  - Confirmed by text
  - Confirmed by table
  - Confirmed by figure
  - Inferred from figure
  - Open question
- Translation Confidence: `High`, `Medium`, or `Low`.
- Meaning Risk: `None`, `Low`, `Medium`, or `High`.
- Usage Rule: How later requirement/FD/DD prompts must use this term.
- Notes / Open Questions: Add uncertainty, conflict, or customer-confirmation need.

## 3. Locked terms

List terms that must not be translated, renamed, or expanded.

| Term | Rule | Reason | Source |
|---|---|---|---|

Rules for this section:

- Derive locked terms from `output/11_translation_policy.md`.
- Also include field names, acronyms, unknown terms, code-like identifiers, operation names, command names, and product-specific terms found in text/table/figure evidence.
- Do not invent locked terms manually.

## 4. Terms requiring customer or BA confirmation

List terms whose translation, scope, or business meaning is uncertain.

| Term | Issue | Suggested Question | Source |
|---|---|---|---|

Only include items that genuinely need confirmation.

## 5. Figure-derived terms

List terms that came from embedded images or diagrams.

| Term | Figure ID / Image Reference | Relationship to text evidence | Meaning Risk | Notes |
|---|---|---|---|---|

Relationship must be one of:

- Also found in text evidence
- Supports text evidence
- Adds figure-only terminology
- Potential conflict with text evidence
- No clear text link

Rules:

- Do not convert figure-only terms into confirmed requirements.
- If a figure term is unreadable or ambiguous, mark meaning risk as `High` and add a note or open question.

## 6. Glossary consistency checks

Report findings for:

- terms with multiple English renderings
- acronyms expanded without evidence
- field names changed incorrectly
- product-specific terms translated too freely
- figure-only terms not found in text evidence
- terms with `Medium` or `High` meaning risk
- terms that should be locked but are not clearly marked in the translation policy

Use this table:

| Check item | Finding | Severity | Recommended action |
|---|---|---|---|

Severity must be one of:

- None
- Low
- Medium
- High

## 7. Usage rules for requirement extraction

Write concrete rules that `30_extract_requirements.prompt.md` must follow when using this glossary.

The rules must cover:

- how to use locked terms
- how to handle undefined acronyms
- how to handle uncertain Japanese terms
- how to handle figure-only terms
- how to handle terms with `Medium` or `High` meaning risk
- how to avoid creating requirements from terminology assumptions
- how to preserve field names, command names, operation names, and product-specific terms

## Required output quality

- Output must be English.
- Follow `output/11_translation_policy.md` strictly.
- Use the translation policy as the source of truth for locked terms.
- Preserve exact spelling for terms marked as:
  - `Keep Original = Yes`
  - `Term Type = Acronym`
  - `Term Type = Field name`
  - `Term Type = Command`
  - `Term Type = Operation`
  - `Term Type = Product-specific term`
  - `Term Type = Unknown`
- Do not hard-code or invent locked terms.
- Do not expand undefined acronyms.
- Do not rename field names, code-like identifiers, product-specific terms, operation identifiers, or command identifiers unless the source explicitly defines an English rendering.
- If a term may have multiple meanings, list alternatives and mark it as needing confirmation.
- If a term appears only in diagrams, include the figure reference and mark evidence type as `Confirmed by figure` or `Inferred from figure`.
- If a diagram term conflicts with text evidence, mark it as `Potential conflict with text evidence` in the figure-derived terms section.
- If Japanese source meaning is uncertain, keep the Japanese term together with the safest English rendering.
- Prefer concise technical English.
- If image analysis introduces a new term not found in text evidence, include it but mark the evidence source clearly.

## Stop conditions

Stop and report `No-Go` only if:

- required primary inputs are missing
- the latest effective translation gate is `No-Go`
- `output/20_image_analysis.md` is missing or explicitly `No-Go`
- creating the glossary would require unsupported assumptions for most key terms

Do not stop only because some image-derived terms are unreadable or ambiguous. Instead, include them as high-risk terms or open questions.

## Final validation

Before completing the output, verify:

- no hard-coded project-specific term list was introduced by this prompt
- all locked terms are derived from input evidence or translation policy
- every glossary term has a source reference
- every uncertain term has either a note or an open question
- no requirement, FD content, or business behavior was generated from terminology assumptions
- output was written to `output/21_glossary.md`
