# Next Phase Note - Machine-readable FD Package

The current package focuses on prompts 10-72 for a controlled FD workflow.

Do not jump directly from customer-facing Markdown FD to code generation.

Recommended next safe extension:

```text
80_generate_machine_readable_fd_package
81_review_machine_readable_fd_package
```

Target machine-readable files:

```text
design/fd/function.fd.yaml
design/fd/flows.fd.yaml
design/fd/rules.fd.yaml
design/fd/data.fd.yaml
design/fd/screens.fd.yaml
design/fd/messages.fd.yaml
design/fd/open_questions.fd.yaml
design/fd/trace.fd.yaml
```

Principles:

- Human-readable FD is for people.
- `.fd.yaml` is for DD/code generation.
- YAML must preserve evidence links and unresolved questions.
- Code generation should not start until the machine-readable FD passes review.
