# OWOS Learning Content Instructions

This repository is the authoritative source for OWOS courses.

When a user asks to continue, update, research, build, revise, validate, or release a course under `apps/`, use the version-controlled `continue-owos-course` skill in `.codex/skills/continue-owos-course/` and follow the nearest course `AGENTS.md`.

When a user supplies a diagram, concept, article, technical brief, procedure, standard operating
procedure, regulation, study, conversation, existing HTML page, or mixed source package and asks to
create, continue, research, verify, compile, connect, review, or release a Concept Brief, use the
version-controlled `continue-owos-concept-brief` skill in
`.codex/skills/continue-owos-concept-brief/` and follow the nearest Concept Brief `AGENTS.md`.

The user works conversationally. Do not require the user to run Python, Git, extraction, build, or validation commands. Run internal tools yourself and report their results in plain English.

Apply Hardeep Soul, the OWOS Course Production Contract, Course Operating Standard, Course Design
System, Course Experience Architecture, Visual Arsenal, writing standard, component and quiz
catalogs, provenance, evidence boundaries, module state, approval gates, and Course Quality Contract
automatically. Read `core/standards/COURSE-PRODUCTION-CONTRACT.md` first; it is the non-optional
release floor for every course.

The Course Design System and Course Experience Architecture are both mandatory.

The OWOS Graphite Visual Standard in `core/standards/OWOS-GRAPHITE-VISUAL-STANDARD.md` is the
default identity for new public knowledge and learning products. Lock the palette, typography,
contrast, depth, and accent semantics without cloning one page composition. Existing operational
application screens remain on their approved system until deliberately migrated.

Every module needs a reviewed design brief and the course needs a design matrix. Chapter 09 is a capability benchmark, not a reusable page layout. Visuals, simulations, quizzes, work products, and animation must follow the learning problem and remain deliberately varied across adjacent modules.

New courses and materially rebuilt modules use structured module packages under
`apps/<course>/modules/`. HTML is compiled delivery output. Before implementation, approve the module
storyboard. Every counted visual must resolve through the visual manifest to an actual asset or
registered executable component. Use `tools/course_compiler.py` for validation and preview builds,
and use the module-level Author Studio when Hardeep needs narrative, storyboard, visual,
interaction, assessment, evidence, and QA control without editing HTML.

The stable compiler contract is `owos-course-compiler/1`. Do not replace it with a page generator or
silently change how approved structured sources are interpreted. Every course must declare its
structured-authoring migration truth in `.course/authoring.json`; run
`python3 tools/audit-structured-authoring.py` before claiming that existing courses are migrated.

Every course also needs an approved Course Experience Brief. Run
`python3 tools/course_distinctiveness.py --course apps/<course>` after every three produced lessons
and before release. Individual module passes cannot override a course-level repetition failure. Never
bulk-generate lesson teaching from one fixed page function with content substituted into slots.

Every major learning component must include visible instructor explanation in plain English. The
written lesson must stand on its own without video. Recording scripts are optional and follow the
course modality plan.

Use explanatory graphics where they reveal a concept, method, framework, relationship, sequence, or consequence. Graphics must have an instructional job, visible interpretation, accessible meaning, mobile behavior, and a reduced-motion equivalent when animated. Decorative imagery does not satisfy the course visual requirement.

After every built module, create a scored quality-control report from `core/templates/MODULE-QA-REPORT.md`. The report must show the score, evidence, missing work, automated checks, manual reviews, and hard-gate status. Do not call a module production ready because its numeric score is high.

For every full module, run `python3 tools/course_conformance.py` with the lesson, QA report,
design brief, optional modality script when one exists, and course `.course/full-module-contract.json`. This validator is
the binding implementation gate. A standards document, generated folder, minimum-floor test, or
high numeric score is never a substitute. Do not report full-module conformance unless this command
passes against the actual lesson. Report every unperformed browser, device, accessibility,
practitioner, learner, factual, and release review as unresolved.

Never treat a runtime copy in `onewater-os-platform` as the curriculum source. Never release a course without the mandatory Course Quality Contract and explicit approval.

Concept Briefs use the separate `owos-concept-brief/2` contract in
`core/standards/CONCEPT-BRIEF-PRODUCTION-CONTRACT.md`. Do not silently extend or reinterpret
`owos-course-compiler/1`. The Concept Brief Compiler renders approved structured sources, enforces
complete claim-verification coverage and fail-closed release gates, and preserves Graph, Community,
commercial-integrity, correction, and freshness records. It never approves its own facts.

OWOS water, wastewater, stormwater, and One Water instruction uses United States authorities only.
Use current federal primary authority first, then applicable state requirements clearly labeled by
state. Do not use a non-United States regulation, standard, government guidance document, design
guide, operator guide, or health guideline as governing evidence, a benchmark, or learner-facing
context. Peer-reviewed research from outside the United States may be considered only as research,
never as a governing standard, and only when its geography, experimental scope, and transfer limits
are visible.
