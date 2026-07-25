# OWOS Course Author Studio

This utility is an internal developer harness for structured OWOS course packages. It is not
Hardeep's permanent Author Studio and must not be presented as the human-facing production
workspace. The permanent workspace is `https://owos.ai/capture#studio?tab=courses`.

Start it from the repository root:

```bash
python3 tools/course_author_studio.py
```

Developers may then open the temporary harness at `http://localhost:8787`.

Open a specific module directly with:

```text
http://localhost:8787/review/<course-slug>/<module-slug>
```

For example:

```text
http://localhost:8787/review/meaning-before-models/module-18-graph-grounded-agentic-applications
```

The studio provides separate views for the design brief, narrative, storyboard, visuals,
interactions, assessments, sources, glossary, QA, and compiled preview. Every save preserves the
prior file under the module's `.history/` directory. Validation uses the same compiler gate as
command-line builds.

Release approval is intentionally unavailable in the interface until all named human reviews have
been completed and recorded.
