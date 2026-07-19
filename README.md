# One Water OS

The single home for all One Water OS technical content and apps, by APAS.ai. Taught by Droobi.

**Version:** 0.13.0 &middot; **Last updated:** 2026-07-19

This is a **monorepo**. The reusable foundation lives in `core/` and is shared by every app in
`apps/`. Build the wheel once in `core/`, reuse it everywhere. That is how we keep the branding,
the voice, and the approach consistent across every application.

---

## Structure

```
core/                     the reusable foundation. Build once, every app uses it.
  brand/                  Clearwater brand: owos-brand.css, Droobi, logos, BRAND-GUIDELINES.md
  standards/              WRITING-STANDARD.md, VISUAL-ARSENAL.md
  components/             component-gallery.html, quiz-gallery.html, module-template.html,
                          COMPONENTS.md, QUIZ-TYPES.md
apps/                     one folder per application. Each reuses core/.
  project-management/     the Project Management masterclass (built)
    curriculum/           syllabus, the course "chrome", and the chapters
    playbook/             the utilities PM field playbook (HTML + PDF)
    starter-kit/          a plain-file project scaffold you copy to run a real job
  data-ai-governance/     the Data Before AI Master Class (structure ready for owner lock)
    curriculum/           syllabus, landing page, and 25 linked chapter shells
    dist/site/            self-contained OWOS.ai build outputs
    course.yaml           machine-readable course and controlled-method record
docs/
  OWOS-COURSE-TO-LEARN-ARCHITECTURE.md  canonical source-to-runtime ownership and release map
  ( living-graph/ , fable-agent/ , one-water-os/ ... come next )
README.md  CHANGELOG.md  VERSION
```

## How to add a new app (so you never reinvent the wheel)
1. Make a folder under `apps/` (for example `apps/living-graph/`).
2. Copy `core/components/module-template.html` as your starting page.
3. Point at the foundation in `core/`: the brand in `core/brand/`, the rules in `core/standards/`,
   and the palettes in `core/components/`.
4. Follow the build order in `core/standards/WRITING-STANDARD.md`.

Because every app pulls from the same `core/`, changing the brand or the writing standard once updates
the approach for all of them.

## The build order for any module
1. Read `core/standards/WRITING-STANDARD.md` (voice + component + quiz rules).
2. Run the Selection Prompt in `core/standards/VISUAL-ARSENAL.md` (pick visuals that fit the ideas).
3. Pick visuals from `core/components/component-gallery.html` (catalog: `COMPONENTS.md`).
4. Pick and mix quizzes from `core/components/quiz-gallery.html` (catalog: `QUIZ-TYPES.md`).
5. Copy `core/components/module-template.html` and fill it in.

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
