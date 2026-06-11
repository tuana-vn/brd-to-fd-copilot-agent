# Draft FD YAML Schema Notes

This is a placeholder for the next phase. Define schemas before generating DD or code.

## Common fields

Each `.fd.yaml` file should include:

```yaml
schema_version: "0.1"
source_fd: "output/70_FD_DRAFT_AFTER_QA.md"
generated_from:
  - "output/63_requirement_inventory_after_qa.md"
  - "output/64_business_rule_catalog_after_qa.md"
evidence_policy:
  hallucination_guard: "source-bound"
  unresolved_information: "must_remain_open_question"
items: []
```

## Review requirement

A future `81_review_machine_readable_fd_package` prompt should verify:

- YAML completeness.
- No unsupported logic.
- Stable identifiers.
- Traceability to FD and source evidence.
- No customer-facing leakage problem if YAML is shared internally only.
