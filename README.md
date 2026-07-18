# One Water OS PM System

The project-management masterclass, brand system, and course-building framework for
**One Water OS Academy**, by APAS.ai. Taught by Droobi.

**Version:** 0.1.0 &middot; **Last updated:** 2026-07-18

---

## What is in here

```
brand/            The One Water OS "Clearwater" brand: guidelines + assets (logo, Droobi, icons)
playbook/         The utilities/water PM field playbook (HTML + PDF)
curriculum/       The masterclass: syllabus, chapters, the course "chrome", and the build framework
starter-kit/      A plain-file project scaffold you copy to start a real job
```

## The course-building framework (how a module gets made)

Four files work together. Follow them in order to build any chapter:

1. **`curriculum/WRITING-STANDARD.md`** — the voice rules (plain, conversational, no em dashes, no
   cliches, always a water example) plus the required learning components and quiz variety.
2. **`curriculum/VISUAL-ARSENAL.md`** — a catalog of ~35 visual types and a Selection Prompt you run
   per module so the visuals fit the ideas (never default to the same triangle or curve).
3. **`curriculum/component-gallery.html`** — every visual rendered live. Pick what you need.
4. **`curriculum/quiz-gallery.html`** — every quiz type, working. Mix them so nothing repeats.

Then copy **`curriculum/module-template.html`** and fill it in.

Markdown catalogs of the galleries (for quick reference): **`curriculum/COMPONENTS.md`** and
**`curriculum/QUIZ-TYPES.md`**.

## The masterclass

- **`curriculum/masterclass-project-management.html`** — the course shell ("chrome"): 21 chapters,
  60 sections.
- **`curriculum/module-01-what-is-a-project.html`** — Chapter 01, built (interactive).
- **`curriculum/module-b3-b6-critical-path.html`** — the Scheduling & Critical Path chapter (the
  interactive format mold).
- **`curriculum/SYLLABUS.md`** — the full curriculum blueprint.

## Working note (HTML vs Markdown)
Reference and standard docs are Markdown so they are easy to read and update. The galleries,
template, and chapters are HTML because they are interactive (a flip card has to flip). The
`*.artifact.html` files are preview copies used for sharing; the plain `*.html` files are the ones
you deploy to the site.

## Versioning
See `CHANGELOG.md` for dated entries and `VERSION` for the current number. Each release is also a git
tag (for example `v0.1.0`). When a document changes, the change is committed here so it can be tracked
and rolled back.
