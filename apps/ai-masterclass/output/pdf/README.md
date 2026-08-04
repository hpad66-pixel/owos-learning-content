# Fellowship PDF Outputs

These PDFs are generated working artifacts. The controlled source remains the repository content in
`apps/ai-masterclass/`.

## Current artifacts

- `one-water-ai-executive-fellowship-program-book.pdf`
  - 17 pages
  - Rebranded, comprehensive program document
  - Complete value proposition, audience, 64-module curriculum, capstone, Fieldbook, governed
    research and graphics process, delivery architecture, and legacy-content boundary
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

Build the synchronized HTML and PDF program book and the complete download package:

```bash
/Users/apas/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  apps/ai-masterclass/tools/build_fellowship_program_book.py
```

Check the program book, supporting PDFs, sources, and ZIP package:

```bash
/Users/apas/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  apps/ai-masterclass/tools/build_fellowship_program_book.py --check
```

Run the synchronization check after any curriculum, Fieldbook, metadata, or builder change:

```bash
/Users/apas/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  apps/ai-masterclass/tools/build_fellowship_pdfs.py --check
```

The check uses `fellowship-sync-manifest.json` and fails when a controlled source or either PDF has
changed independently.

## Status

The program book is the current controlled Fellowship document. Public course release, accessibility
certification, fillable Fieldbook fields, printer proof, and participant distribution remain separate
approvals. The older 686-page Master Class compilation is a legacy source library and is not presented
as completed Fellowship instruction.
