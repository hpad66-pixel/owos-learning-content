# Meaning Before Models: RDF and Knowledge Graphs for Utilities Course Instructions

Use `$continue-owos-course` for every material task in this folder.

The user adds documents to `inbox/` or speaks and types directly into the Codex task. Preserve substantive direction in `conversations/`. Run internal inventory, extraction, research, course generation, validation, and release tools yourself. Never ask the user to operate Python scripts.

Before drafting, read `COURSE-BRIEF.md`, `STATE.md`, `APPROVALS.md`, `course.yaml`, `SYLLABUS.md`, Hardeep Soul, the Course Production Contract, Course Operating Standard, Course Design System, Course Experience Architecture, `curriculum/COURSE-EXPERIENCE-BRIEF.md`, Visual Arsenal, component catalog, quiz catalog, and writing standard. Preserve originals, distinguish evidence from Hardeep's positions, and require approval before locking the blueprint, storyboard, golden lesson, or release.

Create a module design brief before each lesson and maintain the course design matrix. Chapter 09 is a capability benchmark, not a page template. Every module must select its visual, interaction, quiz, animation, and work-product mix from the learning problem and must be checked against adjacent modules for repetition.

The fixed lesson generator in `tools/build-meaning-before-models-course.py` is retired. It produced
the repeated five-section, four-quiz, eight-field-form pattern that failed Hardeep's experience
review. Rebuild each module from its approved archetype and signature mechanism. Run
`python3 tools/course_distinctiveness.py --course apps/meaning-before-models` after every three
rebuilt modules. The written lesson must stand without video.

Materially rebuilt modules use the structured package under `modules/<module>/`. The package keeps
narrative, storyboard, real visual assets, interactions, assessments, sources, glossary, and QA
separately reviewable. Run `tools/course_compiler.py validate` before compiling HTML. A
`data-visual-type` declaration, card grid, box, blob, or icon row is not a visual. Every counted
visual must resolve through `visuals/visual-manifest.yaml` to an actual asset or registered
executable component and must pass rendered review.

Before module design begins, every planned module must have an approved `lesson-contract.yaml`.
Run `python3 tools/validate-lesson-contracts.py --course meaning-before-models`. The contract gate
must pass before selecting the revised golden lesson.
