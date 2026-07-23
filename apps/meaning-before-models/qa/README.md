# Quality Assurance

This directory contains the scored reports, repository-verifiable checks, and unresolved human
review gates for the complete eighteen-module candidate set.

- Eighteen canonical `module-*-quality-control-report.md` files use the scored OWOS template.
- `2026-07-23-standardization-failure-audit.md` preserves the original production failure.
- `archive/` preserves invalidated reports without allowing them to appear canonical.
- `lesson-browser-validation.cjs` is the browser learner-path test. It must be expanded and run
  successfully across all eighteen current modules before technical review can pass.
- `module-05-practitioner-review-form.md` and `module-05-novice-pilot-form.md` provide the initial
  human-review instruments. Course-wide sampling and module-specific expert review remain required.

Repository conformance is checked with:

```bash
python3 tools/test-meaning-before-models-course.py
```

These checks do not authorize publication, a credential, operational use, graph publication, or
course release.
