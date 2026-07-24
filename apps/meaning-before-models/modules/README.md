# Structured modules

Each folder is an authoritative module source package. The package separates its design brief, teaching, storyboard,
visual assets, interactions, assessments, sources, glossary, and quality evidence. Compiled HTML is
delivery output.

Build and validate a package with:

```bash
python3 tools/course_compiler.py validate apps/meaning-before-models/modules/module-01-rdf-in-15-minutes
python3 tools/course_compiler.py build apps/meaning-before-models/modules/module-01-rdf-in-15-minutes
```

Release validation adds `--release-ready` and fails while any human approval or rendered review is
pending.
