# _course-template

A ready-to-clone starter for a new One Water OS Academy course. It already points at the shared
foundation in `core/`, so a new course inherits the voice, the components, the simulations, and the
quizzes with nothing to copy.

## Start a new course in 4 steps

1. **Run the course creator.** Do not manually copy or rename the template:

   ```bash
   python3 tools/create-course.py \
     --slug living-graph \
     --title "Living Graph for Utilities" \
     --course-id owos-course-living-graph-001 \
     --runtime-key lg001
   ```

   If a stable-slug folder already contains research, add `--adopt`. The tool preserves existing
   files, moves loose research sources into `research/originals/`, and creates only missing records.
2. **Fill in `course.yaml` and `SYLLABUS.md`** with stable IDs, provenance, release state, parts,
   chapters, and sections after the research, claims, and evidence boundaries are reviewed.
3. **Build each chapter** by copying `curriculum/module-01-example.html`, renaming it, and filling in
   the placeholders. It already links `../../../core/components/academy.css` and `academy.js`, so every
   `data-ac` component renders. Preview by opening the file over a local server rooted at the repo.
4. **Deploy** with the repo's `tools/build-selfcontained.py`, which inlines the library into one
   self-contained HTML file per lesson for owos.ai or any LMS.

Before release, run `python3 tools/build-course-release.py <your-course-slug>`. The command verifies
the course record and built files and creates `dist/release-manifest.json`. The GitHub course-release
workflow sends the exact source commit to OWOS, where a separate workflow opens a review pull request.

## The rules (all in core/)
- `core/standards/WRITING-STANDARD.md` — voice, structure, and the two big rules: assemble from the
  library (never hand-roll), and simulate a mechanism instead of only describing it.
- `core/standards/VISUAL-ARSENAL.md` — the visual/simulation menu and the Selection Prompt to run per chapter.
- `core/components/QUIZ-TYPES.md` — the quiz types; mix 3+ per chapter.
- `core/components/COMPONENTS.md` — the catalog of built `data-ac` components.
- `core/components/component-gallery.html` and `quiz-gallery.html` — every component and quiz, live.

## Why point at core instead of copying
One library, one set of standards, every course identical. Fix a component once in `core/` and every
course updates. That is the whole reason this is a monorepo.
