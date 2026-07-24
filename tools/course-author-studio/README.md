# OWOS Course Author Studio

Author Studio is the module-level control surface for structured OWOS courses. It does not edit
compiled HTML.

Start it from the repository root:

```bash
python3 tools/course_author_studio.py
```

Then open `http://127.0.0.1:8787`.

The studio provides separate views for the design brief, narrative, storyboard, visuals,
interactions, assessments, sources, glossary, QA, and compiled preview. Every save preserves the
prior file under the module's `.history/` directory. Validation uses the same compiler gate as
command-line builds.

Release approval is intentionally unavailable in the interface until all named human reviews have
been completed and recorded.
