# Changelog

All notable changes to One Water OS are recorded here, newest first.
Dates are YYYY-MM-DD. Versions follow simple semantic-ish numbering.

## [0.11.0] - 2026-07-19
### Added: complete Data and Artificial Intelligence Governance syllabus
- Added `apps/data-ai-governance/` as the governed course-content home for the Data Before AI Master
  Class.
- Added a complete 25-chapter, 75-section syllabus built for drinking water, wastewater, stormwater,
  reuse, and integrated One Water utilities.
- Mapped every Version 2.3 assessment criterion from D01.1 through D12.5 and assigned all 21 controlled
  figures a teaching job.
- Added Foundation, Practitioner, and Leader lenses; seven role pathways; the fictional Riverbend
  utility running case; chapter-level utility examples; deployment studios; evidence gates; visual and
  simulation plans; varied checks; and a 20-artifact Utility Data and AI Governance Launch Pack.
- Added the proposed entry diagnostic, chapter checks, part assessments, final scenario assessment,
  capstone, critical-gate pass rule, and course-completion credential boundary.
- Added the applied capstone for deploying one governed material decision chain with a 90-day launch
  and 12 to 24 month funded roadmap.
- Added `course.yaml` with the stable OWOS course ID, pinned Version 2.3 method commit, release gates,
  structure, roles, planning effort, assessment proposal, and credential status.
- Added a controlled build order from owner lock through utility pilot, OWOS Learn integration,
  Supabase learner records, Knowledge Graph alignments, acceptance, release, and improvement.

### Changed
- Updated the root and apps indexes to include the new Master Class.
- Synchronized the root README version with `VERSION` at 0.11.0.

## [0.10.1] - 2026-07-19
### Fixed
- The `cpmsim` critical-path diagram ran off the right edge of the page. It now scales the fixed-width
  activity-on-node network to fit the card width (with room for the float badges) and re-fits on resize,
  so the whole diagram is visible with nothing cut off. Tightened the node/gap sizing so the fit lands
  at a readable ~76% rather than shrinking too far.

## [0.10.0] - 2026-07-19
### Added: a critical-path simulator + the "show it" principle
- New library `cpmsim` renderer: an interactive activity-on-node simulation that DERIVES the critical
  path step by step. Reset / Back / Step / Play controls walk the forward pass (earliest dates), the
  backward pass (latest dates), float, then light up the critical chain in gold, with live narration at
  each step. Added to Chapter 05, Section 3. Verified: floats compute to permit 5, procurement 0, and
  the critical chain reads survey → procure → pipe → tie-ins → test → close out.
- Standards updated (WRITING-STANDARD, VISUAL-ARSENAL) with the **"simulate, do not just describe"**
  rule: any process, algorithm, or thing-that-unfolds gets an interactive that shows it happening
  (step-through, live model, or reveal), not just prose. Build it into the shared library so every
  future chapter can reuse it. This is now a standing requirement, per Hardeep.
### Deployed
- Rebuilt all five lessons + course page and published to owos.ai; verified live.

## [0.9.0] - 2026-07-18
### Added: Chapter 05 + two scheduling components
- New library `gantt` renderer: an interactive Gantt that runs a real Critical Path Method engine
  (forward and backward pass, float), highlights the critical path in gold, shows slack, and gives
  per-activity dates and float on click. Verified: the Millpond schedule computes to a 30-week
  critical path through survey, long-lead procurement, pipe, tie-ins, test, and closeout, with the
  permit correctly showing 5 weeks of float.
- New library `scurve` renderer: a cost-loaded cash-flow S-curve (period bars plus cumulative line).
- Chapter 05 "Scheduling and the Critical Path" built on the library: the Gantt, dependency-type
  classification, lag and lead, the CPM method, a zero-float slip estimate, a crash-the-critical-path
  judgment, and the S-curve. Working lens, Millpond thread, recap and leader's bottom line.
### Changed
- Masterclass chrome: Chapter 05 now live; status note "Chapters 01 to 05 are live." Rebuilt all five
  lessons + course page self-contained.
### Deployed
- Published all five lessons + the course page to owos.ai and verified each renders on the live,
  authenticated site.

## [0.8.0] - 2026-07-18
### Added: Chapter 04 + a WBS tree component
- New library `tree` renderer: an interactive Work Breakdown Structure (expand/collapse branches, click
  any node for its detail). CSS added for the tree.
- Chapter 04 "Scope and requirements" built fresh on the library: requirement-type classification, a
  vague-vs-testable contrast, a gather-and-lock-down method, a traceability check, the Millpond WBS tree
  (23 nodes to work packages), in/out-of-scope sorting, a scope-change judgment, and myths. Working lens,
  Millpond thread, recap and leader's bottom line.
### Changed
- Masterclass chrome: Chapter 04 now live; status note "Chapters 01 to 04 are live."
- Rebuilt all four lessons + the course page self-contained.
### Process
- New rule: a deploy is not "done" until the LIVE authenticated page is confirmed rendering in the
  browser (not just the local build). Verified Chapters 01 to 04 render on owos.ai before shipping.
### Deployed
- Published all four lessons + the course page to owos.ai via the Cloudflare Pages deploy.

## [0.7.0] - 2026-07-18
### Added: two library components
- `calc` renderer: a reusable business-case calculator (NPV, payback, benefit-cost ratio) with a live
  cash-flow curve and a spend-vs-return bar chart. Config sets the input ranges, labels, and defaults.
- Upgraded the `triangle` renderer to the richer version: a stretching polygon with a live quality dot
  (0 to 100) and a dynamic badge, instead of the simpler static triangle.
### Changed: Chapter 01 migrated onto the library
- "What a project is" rebuilt from hand-rolled markup to the shared library: the one-question test,
  classify, the rich iron triangle, the phase-gate life cycle, the business-case calculator (verified
  identical math: NPV +$2.57M, payback 7.2 years, BCR 2.97 at the defaults), and the mixed quizzes.
- Threaded the Millpond Road job through it, wired the Full/Plain/Leader lens for real, defined NPV and
  BCR on first use, added a closing recap and leader's bottom line.
### Added: Chapter 03 (new)
- "Governance, integration and tailoring" built fresh on the library: a why-gates contrast, a three-kinds
  -of-PMO comparison table, must-do vs scored classification, the charter-to-PM-plan method, subsidiary-plan
  matching, an integration judgment, a tailoring spectrum and recommender, an ordering quiz, and myths.
  Working lens, Millpond program thread, recap and leader's bottom line.
### Changed
- Masterclass chrome: Chapter 03 now live; status note corrected to "Chapters 01 to 03 are live."
- `build-selfcontained.py`: added the Chapter 03 link mapping.
### Deployed
- Rebuilt all three lessons and the course page self-contained and published to the `2-brain` site (owos.ai)
  via the Cloudflare Pages deploy (git push alone does not publish).

## [0.6.0] - 2026-07-18
### Changed: Chapter 02 deepened (it felt thin as a survey)
- Wired the Full / Plain / Leader lens for real. It had zero content variants and did nothing; now
  Full shows the detail, Plain trims it, and Leader shows only the call. Verified across all three modes.
- Threaded one running job through the whole chapter: the Millpond Road lift station rebuild. Every
  component now works that job (spectrum, phase-gate, comparison table, recommender, quizzes).
- Added a numbers moment (a schedule-savings estimate) and an ordering quiz, taking it to eight quiz
  types. Added a closing recap and a leader's bottom line.
- Added the Florida procurement reality: qualifications-based design selection under the Consultants'
  Competitive Negotiation Act (CCNA), and how competitive-bid rules and alternative-delivery authority
  bound the delivery choice. New library styles: `.casebox`, `.leadcall`, `.recap`.
- Grew from ~1,955 to ~2,884 words (depth, not padding), no em/en dashes.
### Deployed
- Rebuilt the self-contained Chapter 02 and republished it to the `2-brain` site (owos.ai).

## [0.5.0] - 2026-07-18
### Added: the shared component library (the real fix)
- `core/components/academy.css` and `core/components/academy.js`: one place that holds every
  polished component and quiz. A module now writes small declarative markup
  (`<div data-ac="spectrum">` with a JSON config) and the library renders the identical, gallery-grade
  component. Fix a component once, every module updates. Renderers: flip, match, mc, multi, classify,
  estimate, truefalse, order, reflect, spectrum, table, recommender, decide, triangle, process, method,
  twofig, plus tooltips, lens, reading progress, goals, and the Droobi cue.
- `tools/build-selfcontained.py`: inlines the library into one distributable HTML file (escapes any
  `</script>` so the inline script parses), rewrites nav links to deployed names, and asserts no dashes.
### Changed: Chapter 02 rebuilt on the library (this was the "shittiest version" complaint)
- Every diagram and quiz is now the real library component, not a hand-rolled version. Twelve components:
  flip cards, a predictive-to-adaptive spectrum, a line-versus-loop contrast, an interactive phase-gate,
  a delivery-method comparison table, matching, a five-step method, a recommender, and classify /
  multiple-choice / true-false / reflection quizzes.
- Every acronym is spelled out on first use (DBB, DB, CMAR, PDB, GMP) with a hover definition.
- Exactly one tooltip element, zero native `title` attributes. The "two tooltips" bug is gone.
- Verified live in the browser: all 12 components render and interact correctly.
### Deployed
- Rebuilt the self-contained Chapter 02 and published it to the `2-brain` site (owos.ai).

## [0.4.1] - 2026-07-18
### Changed (standards, per Hardeep's direction)
- Added hard rules: spell out every acronym in full on first use (short form in parentheses); every
  term and acronym gets ONE hover tooltip (no second `title`-attribute tooltip).
- Added the top rule: a module is ASSEMBLED by copying the exact components out of `component-gallery.html`
  and `quiz-gallery.html` (chosen via the Selection Prompt, content from `SYLLABUS.md`). Never hand-roll
  a simpler diagram or quiz. The galleries are the single source of truth for how components look and work.
- Reinforced the same in `VISUAL-ARSENAL.md` and `QUIZ-TYPES.md`.
### Next
- Build a shared component library (one CSS + one JS) so every module uses the real gallery components,
  then rebuild Chapter 02 on it. Acronyms defined first, tooltip doubling fixed.

## [0.4.0] - 2026-07-18
### Added
- Chapter 02 (Delivery & life cycles), built with a fresh visual palette so it does not echo
  Chapter 01: a predictive-vs-agile spectrum, a linear-vs-loop diagram, an interactive delivery-method
  comparison table and recommender, plus five quiz types (classify, matching, flip cards, multiple
  choice, true/false) and a reflection. Plain voice, no em dashes.
- Native deploy page `dist/site/lesson-pm-02-delivery-life-cycles.html`.
### Changed
- Course chrome: Chapter 02 now live; Chapter 05 set back to "coming soon" until it is deployed
  (we deploy in sequence).
### Deployed
- Published Chapter 02 and the updated course landing to the `2-brain` site (owos.ai).

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
