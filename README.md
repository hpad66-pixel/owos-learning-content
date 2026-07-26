# OWOS Learning Content

The governed source and build repository for One Water Operating System learning products, by APAS.ai. Taught by Droobi.

**Version:** 0.18.0 &middot; **Last updated:** 2026-07-26

This is the learning-content monorepo. It contains two governed production systems:

- the **OWOS Course Engine**, which produces multi-module courses through the OWOS Course Compiler;
- the **OWOS Concept Engine**, which produces focused Concept Briefs through the OWOS Concept Brief
  Compiler.

Both engines consume the shared learning-capability registry in `core/`. Courses and briefs share
identity, accessibility rules, evidence discipline, visuals, interactions, assessments, Graph and
Community connections, and release controls without sharing one fixed page template.

This repository does not run the production OWOS platform. The production web application, APIs,
authentication, Supabase migrations, and Cloudflare runtime live in
`hpad66-pixel/onewater-os-platform`.

---

## Structure

```
core/                     the reusable foundation. Build once, every product uses it.
  brand/                  OWOS brand, Graphite tokens, Droobi, logos, guidelines
  learning-capabilities/  shared visual, interaction, animation, and assessment registry
  standards/              course, Concept Brief, writing, visual, and experience contracts
  components/             component-gallery.html, quiz-gallery.html, module-template.html,
                          COMPONENTS.md, QUIZ-TYPES.md
apps/                     one folder per application. Each reuses core/.
  project-management/     the Project Management masterclass (built)
    curriculum/           syllabus, the course "chrome", and the chapters
    playbook/             the utilities PM field playbook (HTML + PDF)
    starter-kit/          a plain-file project scaffold you copy to run a real job
  data-ai-governance/     the Data Before AI Master Class (Chapters 00 through 08 released)
    curriculum/           syllabus, landing page, released lessons, and governed chapter shells
    dist/site/            self-contained OWOS.ai build outputs
    course.yaml           machine-readable course and controlled-method record
docs/
  OWOS-COURSE-TO-LEARN-ARCHITECTURE.md  canonical source-to-runtime ownership and release map
  CONCEPT-BRIEF-AUTHORING-GUIDE.md      conversational Concept Engine workflow
  CONCEPT-BRIEF-OPERATING-MODEL.md      lifecycle and platform control planes
concept-briefs/            authoritative structured Concept Brief packages and compiled output
concept-brief-portfolio/   governed candidate inventory and activation prompts
README.md  CHANGELOG.md  VERSION
```

## Engines and build contracts

Courses use `owos-course-compiler/1` and follow
[`core/standards/COURSE-PRODUCTION-CONTRACT.md`](core/standards/COURSE-PRODUCTION-CONTRACT.md).
Concept Briefs use `owos-concept-brief/2` and follow
[`core/standards/CONCEPT-BRIEF-PRODUCTION-CONTRACT.md`](core/standards/CONCEPT-BRIEF-PRODUCTION-CONTRACT.md).

The Concept Engine accepts a diagram, concept, article, brief, procedure, regulation, conversation,
or existing HTML. It preserves the intake, inventories claims, researches original sources, applies
reverse QA/QC, approves a unique storyboard, compiles deterministic cited HTML, connects Graph and
Community, applies the commercial firewall, and retains version and correction history.

Public water-sector Concept Briefs use federal and EPA governing authority only; AWWA may appear as
professional context. State and non-United States requirements are excluded from the public
authority frame.

## How to add a new course
1. Make a folder under `apps/` using the course or learning-product slug.
2. Copy `core/components/module-template.html` as your starting page.
3. Point at the foundation in `core/`: the brand in `core/brand/`, the rules in `core/standards/`,
   and the palettes in `core/components/`.
4. Follow the build order in `core/standards/WRITING-STANDARD.md`.

Because every app pulls from the same `core/`, changing the brand or the writing standard once updates
the approach for all of them.

## Course module build order
1. Read `core/standards/WRITING-STANDARD.md` (voice + component + quiz rules).
2. Run the Selection Prompt in `core/standards/VISUAL-ARSENAL.md` (pick visuals that fit the ideas).
3. Pick visuals from `core/components/component-gallery.html` (catalog: `COMPONENTS.md`).
4. Pick and mix quizzes from `core/components/quiz-gallery.html` (catalog: `QUIZ-TYPES.md`).
5. Copy `core/components/module-template.html` and fill it in.

## Concept Brief commands

```bash
python3 tools/concept_brief_compiler.py validate concept-briefs/<brief>
python3 tools/concept_brief_compiler.py build concept-briefs/<brief> \
  --output concept-briefs/<brief>/dist/preview.html
python3 tools/concept_brief_compiler.py portfolio-check concept-briefs
python3 tools/test-concept-brief-compiler.py
```

Release-ready validation is deliberately stricter than current educational publication. Numeric
scores and attractive HTML never override missing source, practitioner, accessibility, Graph,
Community, commercial-conflict, or owner approval.

## Formats
Reference and standard docs are Markdown (easy to read and update). The galleries, template, and
chapters are HTML because they are interactive. `*.artifact.html` files are preview copies for
sharing; the plain `*.html` files are what you deploy.

## Versioning
`VERSION` holds the current number, `CHANGELOG.md` has dated entries, and each release is a git tag
(for example `v0.2.0`). When a document changes, it is committed here so it can be tracked and
rolled back.

The cross-repository course delivery contract is documented in
[`docs/OWOS-COURSE-TO-LEARN-ARCHITECTURE.md`](docs/OWOS-COURSE-TO-LEARN-ARCHITECTURE.md).
