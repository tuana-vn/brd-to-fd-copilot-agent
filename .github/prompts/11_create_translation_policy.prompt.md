# 11 - Create Translation Policy

## Purpose

Create a controlled Japanese-to-English translation policy for this project before converting the requirement inventory into English.

## Operating rules
- Do not generate FD.
- Do not extract requirements yet.
- Do not guess undefined acronyms.
- Do not invent requirements, field meanings, business rules, messages, screen behavior, or diagrams.
- Keep product/domain acronyms unchanged.
- Keep field names exactly as written.
- Preserve source-specific terms unless a translation policy or glossary explicitly defines them.
- For Japanese domain terms, provide the safest technical English rendering.
- If meaning is uncertain, keep the Japanese term and mark confidence as Low.
- Do not invent business meaning.

## Task

1. Identify source terms that should not be freely translated.
2. Define translation rules for headings, field labels, operation names, screen names, message names, acronyms, and unknown terms.
3. Define how to represent uncertainty.
4. Define how Japanese source snippets should be referenced when the English rendering is uncertain.
5. Define customer-facing terminology rules.

## Inputs

Use the Japanese requirement evidence from:
- `output/10_document_inventory.md`, if present
- `working/extracted/document_text.md`
- `working/extracted/tables.md`

## Output

### Outputs to create or update

- `output/11_translation_policy.md`

### Required output quality

- Do not define business meaning without evidence.
- Keep policy generic enough for multiple BRDs.
- Include a "Do Not Translate Freely" section.

### Term Translation Policy

| Source Term | English Rendering | Keep Original? | Term Type | Source Reference | Confidence | Notes |
|---|---|---|---|---|---|---|

Term Type should be one of:
- Acronym
- Field name
- Operation
- Business term
- Technical term
- UI/API term
- Unknown

After the table, add:

### Translation Rules

List project-specific rules for converting Japanese requirement evidence into English.

## Stop conditions

- Stop and report `No-Go` if required inputs are missing.
- Stop and report `No-Go` if the output would require unsupported assumptions.
- Do not continue to downstream phases when the current quality gate is `No-Go`.