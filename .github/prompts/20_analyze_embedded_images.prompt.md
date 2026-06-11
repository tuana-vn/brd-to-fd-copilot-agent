# 20 - Analyze Embedded Images

## Purpose

Analyze extracted embedded images as source-bound requirement evidence and normalize the findings into technical English.

This step covers diagrams, screenshots, screen mockups, flows, tables embedded as images, and other visual evidence extracted from the BRD.

This is not free interpretation of diagrams. This is controlled, source-bound image evidence analysis.

## Operating rules

- Use only the source artifacts listed in this prompt.
- Do not invent requirements, field meanings, business rules, messages, screen behavior, actors, systems, states, or diagrams.
- Do not generate FD.
- Do not extract final requirements yet.
- Preserve source-specific terms unless a translation policy or glossary explicitly defines them.
- Mark ambiguous, missing, conflicting, or unreadable information instead of guessing.
- Write outputs in English unless the source value must remain unchanged.
- Keep acronyms, field names, product terms, command names, option names, UI labels, API names, file names, and domain terms unchanged unless the translation policy explicitly defines an approved English rendering.
- Do not expand undefined acronyms.
- Do not modify the original BRD.
- Customer answers, if any, are supplemental evidence only and must not be treated as original BRD evidence.
- Customer-facing documents must not expose internal pipeline terms, internal IDs, or prompt workflow details.
- Internal review and traceability files may use internal IDs such as FIG-xxx.

### Formatting evidence rules

- Treat source formatting as evidence when it changes meaning.
- Strikethrough text means inactive, deleted, deprecated, superseded, or draft-removed evidence unless the source explicitly says otherwise.
- Do not treat strikethrough-only text as active requirement behavior, active business rules, active operation flow, active field definitions, or active UI/API behavior.
- If a paragraph, table cell, caption, or figure note contains both active and strikethrough text, use only the non-strikethrough portion as active evidence.
- Preserve strikethrough evidence in traceability notes when it helps explain removed or deprecated behavior.
- If strikethrough content conflicts with active evidence, prefer active non-strikethrough evidence and record the struck-through content as deprecated/conflict context, not as a confirmed requirement.
- Highlighted text is not automatically active or mandatory. If highlighted text is also strikethrough, the strikethrough rule wins.
- If formatting status is unclear or missing from upstream artifacts, mark the affected item as ambiguous instead of guessing.

For image analysis, do not treat strikethrough nearby captions, struck-through figure notes, or struck-through flow descriptions as active figure meaning. If an extracted image is near struck-through text, record it as contextual/deprecated evidence unless active nearby text confirms the figure is still current.

## Precondition

Use the latest effective translation quality gate:

1. If `output/15_translation_review_followup_report.md` exists, use it as the latest translation gate.
2. Otherwise, use `output/13_translation_review_report.md`.
3. Continue only if the latest gate decision is `Go` or `Go with warnings`.
4. Stop and report `No-Go` if the latest gate decision is `No-Go`.
5. Do not re-open resolved translation issues unless the image evidence creates a new conflict.

## Inputs

### Primary inputs

Use these inputs by default:

- `working/extracted/image_inventory_raw.md`
- `working/extracted/formatting_inventory.md`, if present
- all files under `working/extracted/images/`
- `output/12_normalized_evidence.md`
- latest effective translation gate report:
  - `output/15_translation_review_followup_report.md`, if present
  - otherwise `output/13_translation_review_report.md`

### Supporting inputs

Open these only when needed for verification, source mapping, or terminology control:

- `output/10_document_inventory.md`
- `output/11_translation_policy.md`

Do not load unnecessary raw source artifacts by default. Use the normalized evidence as the main text context.

## Tasks

For each extracted image:

1. Identify the image type:
   - screenshot
   - flow
   - architecture
   - table
   - form
   - message
   - state diagram
   - operation diagram
   - unknown
2. Describe only the visible content.
3. Extract visible labels, fields, buttons, flows, actors, systems, states, commands, options, and conditions.
4. Link image observations to normalized text evidence if identifiable.
5. Link image observations to document inventory items only when identifiable without guessing.
6. Mark unreadable, ambiguous, hidden, or partially visible areas.
7. Mark potential conflicts between image evidence and normalized text evidence.
8. Record any possible evidence implications as downstream notes, not confirmed requirements.

## Output

Create or update:

- `output/20_image_analysis.md`

## Required output structure

Write `output/20_image_analysis.md` using this structure.

# Embedded Image Analysis

## 1. Review decision

Use one of:

- `Go`
- `Go with warnings`
- `No-Go`

Rules:

- Use `Go` only when all required inputs are present, the latest translation gate is acceptable, and all images are readable or non-critical.
- Use `Go with warnings` when one or more images are partially unreadable, ambiguous, weakly mapped to text, or require downstream caution.
- Use `No-Go` only when required input files are missing, no extracted images are available, or the latest effective translation gate is `No-Go`.
- Do not return `No-Go` only because one or more images are partially unreadable. For unreadable or ambiguous images, create an image entry with high meaning risk and add figure-derived open questions.

## 2. Input files checked

| File | Status | How it was used |
|---|---|---|

Only list files actually inspected.

## 3. Image analysis summary

| Metric | Value | Notes |
|---|---:|---|
| Images listed in inventory | ... | ... |
| Images analyzed | ... | ... |
| Images with clear text link | ... | ... |
| Images with weak or missing text link | ... | ... |
| Images partially unreadable | ... | ... |
| Images requiring open questions | ... | ... |

## 4. Figure analyses

For each image, create one section:

## FIG-xxx: Image Analysis

| Field | Value |
|---|---|
| Figure ID | FIG-xxx |
| Image file path | `working/extracted/images/...` |
| Image type | screenshot / flow / architecture / table / form / message / state diagram / operation diagram / unknown |
| Visible title / caption | ... |
| Related normalized evidence item | Reference from `output/12_normalized_evidence.md`, if identifiable |
| Related document inventory item | Item ID from `output/10_document_inventory.md`, if identifiable |
| Scenario / use case shown | ... |
| Components / entities shown | ... |
| Timeline / operation steps visible | ... |
| State changes visible | ... |
| Business rules visible in the diagram | ... |
| Evidence implication / downstream note | ... |
| Evidence type | Confirmed by figure / Inferred from figure / Unreadable / Not applicable |
| Translation confidence | High / Medium / Low |
| Meaning risk | None / Low / Medium / High |
| Ambiguities | ... |
| Text that must be preserved exactly | ... |

### Notes for this figure

Write concise notes. Do not use normative requirement language such as `must`, `shall`, or `should` unless the same behavior is explicitly visible in the image or supported by normalized text evidence.

## 5. Cross-reference with normalized text evidence

Create a table:

| Figure ID | Related normalized evidence reference | Related document inventory item | Relationship | Notes |
|---|---|---|---|---|

Relationship must be one of:

- Supports text evidence
- Explains text evidence
- Adds figure-only detail
- Potential conflict
- No clear link

## 6. Figure-derived open questions

Create a table:

| Question ID | Figure ID | Question | Reason |
|---|---|---|---|

Rules:

- Add a question if an image is unreadable, ambiguous, visually conflicts with normalized evidence, or appears to contain figure-only detail that cannot be confirmed from text.
- Do not add questions for harmless decorative images.
- Do not convert inferred behavior into confirmed requirements.

## 7. Downstream usage notes

Explain how downstream prompts should use this file:

- What image evidence is safe to use.
- What image evidence is risky.
- Which figures require caution.
- Which figures should not be used as confirmed requirement evidence.

## Output quality rules

- Images are evidence, not decoration.
- Never infer behavior from a screenshot or diagram unless visible or supported by normalized text evidence.
- If behavior is inferred from the figure, label it as `Inferred from figure`.
- Do not convert inferred behavior into confirmed requirement.
- If image text is unreadable or too small, mark it as unreadable.
- If a figure appears to support or explain an item in `output/12_normalized_evidence.md`, link it to that item.
- If a figure appears to support or explain an item in `output/10_document_inventory.md`, link it to that item only when needed.
- If the figure conflicts with normalized text evidence, mark it as `Potential conflict`.
- Follow `output/11_translation_policy.md` when it is opened for terminology verification.
- Do not generate FD.
- Do not extract final requirements yet.

## Stop conditions

Stop and report `No-Go` only if:

- Required image inventory is missing.
- Extracted image folder is missing or contains no images.
- `output/12_normalized_evidence.md` is missing.
- The latest effective translation gate is missing.
- The latest effective translation gate is `No-Go`.

Do not stop only because one or more images are partially unreadable or weakly mapped. Record the risk and continue the analysis for other images.
