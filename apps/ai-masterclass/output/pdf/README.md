# Fellowship PDF Outputs

These PDFs are generated working artifacts. The controlled source remains the repository content in
`apps/ai-masterclass/`.

## Current artifacts

- `one-water-ai-executive-fellowship-master-curriculum.pdf`
  - 17 pages
  - Complete eight-course, 64-module master curriculum
  - Program value, audience, delivery model, Fieldbook, capstone, release boundary, and references
- `one-water-ai-fieldbook-working-edition.pdf`
  - 143 pages
  - Participant setup, baseline, 64 module worksheet pairs, capstone checklist, and final reflection

## Build

Run:

```bash
/Users/apas/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  apps/ai-masterclass/tools/build_fellowship_pdfs.py
```

The builder reads `SYLLABUS.md`. It stops unless it finds exactly eight courses and 64 modules.

## Status

Working edition only. Public release, accessibility certification, fillable form fields, printer proof,
and participant distribution remain separate approvals.
