# OWOS Learning Content Instructions

This repository is the authoritative source for OWOS courses.

When a user asks to continue, update, research, build, revise, validate, or release a course under `apps/`, use the version-controlled `continue-owos-course` skill in `.codex/skills/continue-owos-course/` and follow the nearest course `AGENTS.md`.

When a user supplies a diagram, concept, article, technical brief, procedure, standard operating
procedure, regulation, study, conversation, existing HTML page, or mixed source package and asks to
create, continue, research, verify, compile, connect, review, or release a Concept Brief, use the
version-controlled `continue-owos-concept-brief` skill in
`.codex/skills/continue-owos-concept-brief/` and follow the nearest Concept Brief `AGENTS.md`.

The user works conversationally. Do not require the user to run Python, Git, extraction, build, or validation commands. Run internal tools yourself and report their results in plain English.

Apply Hardeep Soul, the OWOS Course Production Contract, Course Operating Standard, Course Design System, Visual Arsenal, writing standard, component and quiz catalogs, provenance, evidence boundaries, module state, approval gates, and Course Quality Contract automatically. Read `core/standards/COURSE-PRODUCTION-CONTRACT.md` first; it is the non-optional release floor for every course.

Every module needs a reviewed design brief and the course needs a design matrix. Chapter 09 is a capability benchmark, not a reusable page layout. Visuals, simulations, quizzes, work products, and animation must follow the learning problem and remain deliberately varied across adjacent modules. Count visual variety by rendered structure and structural fingerprint, never by a renamed label, color, icon, or heading. Full lessons normally need four visual types with at least three different structures and question flip cards for terminology or misconception retrieval.

Every major learning component must include visible instructor explanation in plain English. Every module must have a recording script, and every course must maintain an overview script that explains the lesson sequence.

The OWOS Graphite Visual Standard in `core/standards/OWOS-GRAPHITE-VISUAL-STANDARD.md` is the
default identity for new public knowledge and learning products. Lock the palette, typography,
contrast, depth, and accent semantics without cloning one page composition. Existing operational
application screens remain on their approved system until deliberately migrated.

Use explanatory graphics where they reveal a concept, method, framework, relationship, sequence, or consequence. Graphics must have an instructional job, visible interpretation, accessible meaning, mobile behavior, and a reduced-motion equivalent when animated. Decorative imagery does not satisfy the course visual requirement.

After every built module, create a scored quality-control report from `core/templates/MODULE-QA-REPORT.md`. The report must show the score, evidence, missing work, automated checks, manual reviews, and hard-gate status. Do not call a module production ready because its numeric score is high.

For every full module, run `python3 tools/course_conformance.py` with the lesson, QA report,
design brief, recording script, and course `.course/full-module-contract.json`. This validator is
the binding implementation gate. A standards document, generated folder, minimum-floor test, or
high numeric score is never a substitute. Do not report full-module conformance unless this command
passes against the actual lesson. Report every unperformed browser, device, accessibility,
practitioner, learner, factual, and release review as unresolved.

For courses whose `quality_contract` requires rendered browser QA, the release builder must reject a
missing, failed, or stale `qa/rendered-browser-report.json`. The browser run must verify final visible
states and full learner paths for every lesson on desktop and phone. Review all-module contact sheets
before release so metadata-only variety cannot pass as a distinct learner experience.

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
