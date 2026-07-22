# dist (build outputs)

Built, ship-ready versions of this course, produced from the source in `../curriculum/`. The source
is the single truth; these are the two formats we ship. Rebuild them whenever the source changes.

## `site/` — native owos.ai pages
Each chapter as a page that links the shared site shell (`/owos-brand.css` and `/owos-shell.js`), so
it uses the same nav, footer, and breadcrumbs as every other lesson on owos.ai. Drop these into the
`2-brain` site (for example as `site/lesson-pm-01-what-is-a-project.html`).

- Verified: the shared shell injects its nav and footer, the branding matches, and the interactive
  widgets all work.
- Note: the shell applies fonts with `!important`, so each page includes a small guard so our mono
  labels stay mono. That guard is baked into the built file.

**Wiring into owos.ai:** generate `course-manifest.json`, then use the governed course-release
workflow. The OWOS platform checks out the exact source commit, verifies every checksum, copies the
runtime files, rebuilds its catalog, and opens a review pull request. Direct runtime edits are not a
release process.

## `scorm/` — SCORM 1.2 packages
Each chapter as a SCORM 1.2 zip for uploading to any third-party LMS (Canvas, Moodle, TalentLMS,
Docebo, LearnDash). You do NOT need this for the owos.ai site; it is for external LMSs.

- `scorm/ch01/` holds the package parts: `imsmanifest.xml` (at the zip root, as SCORM requires),
  `content.html` (the chapter), and `scorm-api.js` (reports the module "completed" to the LMS when the
  learner reaches the bottom; does nothing when opened as a plain page).
- `scorm/ch01/pm-ch01-scorm12.zip` is the uploadable package.

To rebuild a SCORM package: put the chapter's self-contained HTML as `content.html`, keep
`scorm-api.js` and `imsmanifest.xml`, and zip the three files with the manifest at the root.

## Which format goes where
- owos.ai (your own site): use `site/`.
- A partner's or client's LMS: use `scorm/`.
- Same source, two outputs, one place. That is the "one source of truth per course" you wanted.
