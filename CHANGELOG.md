# Changelog

All notable changes to One Water OS are recorded here, newest first.
Dates are YYYY-MM-DD. Versions follow simple semantic-ish numbering.

## [0.3.1] - 2026-07-18
### Added
- Native owos.ai deploy page for the course landing: `dist/site/course-project-management.html`
  (course overview + curriculum), shell-wrapped and verified with the dark-hero and button guards.
### Fixed
- Removed em/en dashes from the course chrome to meet the writing standard.
### Deployed
- Published the course landing and Chapter 01 into the `2-brain` site (owos.ai) as
  `course-project-management.html` and `lesson-pm-01-what-is-a-project.html`.

## [0.3.0] - 2026-07-18
### Added
- Two ship-ready output formats for the PM course, in `apps/project-management/dist/`:
  - `dist/site/` native owos.ai pages that link the shared shell (`/owos-brand.css`, `/owos-shell.js`),
    so they match every other lesson on the site. Chapter 01 built and verified against the real shell.
  - `dist/scorm/ch01/` a SCORM 1.2 package (`pm-ch01-scorm12.zip`) for uploading to any external LMS,
    with `imsmanifest.xml`, `content.html`, and a `scorm-api.js` completion reporter.
- `dist/README.md` explaining the outputs and how to wire the course into owos.ai (git submodule).

### Notes
- Single source of truth stays in `onewater-os`; `dist/` holds the built formats next to the source.

## [0.2.1] - 2026-07-18
### Changed
- Finished Chapter 01 (What a project is) as the full exemplar. It now uses the whole palette:
  a decision framework, an interactive iron-triangle diagram, a clickable life-cycle process, a
  method, a calculator with a cash-flow curve and a bar chart, and seven quiz types (classify,
  multiple choice, estimate, flip cards, matching, true/false, reflection). Plain voice, no em dashes.

## [0.2.0] - 2026-07-18
### Changed
- Restructured into a monorepo so every app can reuse one shared foundation.
  - `core/` now holds the reusable wheel: `brand/`, `standards/` (writing standard + visual arsenal),
    and `components/` (component gallery, quiz gallery, module template, catalogs).
  - The Project Management work moved into `apps/project-management/` (curriculum, playbook, starter kit).
- Renamed the repo from `onewater-pm-system` to `onewater-os`.
- Rewrote the README to document the monorepo and how to add a new app.

## [0.1.0] - 2026-07-18
Initial commit. Everything to date is captured and put under version control.

### Brand
- One Water OS "Clearwater" brand guidelines and extracted assets (Droobi, logo, icons, OG image).

### Playbook
- Utilities & Construction PM field playbook (HTML + print PDF).

### Masterclass framework
- `WRITING-STANDARD.md` — voice rules (plain, conversational, no em dashes, no cliches), required
  learning components, and quiz variety.
- `VISUAL-ARSENAL.md` — catalog of ~35 visual types plus the Selection Prompt.
- `component-gallery.html` — every visual rendered live.
- `quiz-gallery.html` — ten quiz types, all interactive.
- `COMPONENTS.md` and `QUIZ-TYPES.md` — Markdown catalogs of the two galleries.
- `module-template.html` — the reusable empty module scaffold, wired to the files above.

### Masterclass content
- `SYLLABUS.md` — 21 chapters, 60 sections, mapped to PMBOK.
- `masterclass-project-management.html` — the course shell ("chrome").
- `module-01-what-is-a-project.html` — Chapter 01, built with framework, diagram, process, chart,
  curve, method, and four quiz types.
- `module-b3-b6-critical-path.html` — Scheduling & Critical Path, the interactive format mold.

### Starter kit
- Plain-file project scaffold (Brief, Board, Budget, Risks, Permits, Schedule, Compliance,
  Stakeholders, Classification, Notes, Inbox, CLAUDE.md).

<!-- Template for future entries:
## [0.x.0] - YYYY-MM-DD
### Added / Changed / Fixed / Removed
- ...
-->
