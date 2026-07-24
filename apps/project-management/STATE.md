# Utility Project Delivery Course State

Last updated: 2026-07-23

## Current phase

Full-course working review. All twenty-one modules pass individual and whole-course conformance plus
course distinctiveness. Release remains blocked on human review.

## Completed working changes

- Modules 10, 12, 15, and 17 now use different assessment sequences and module-specific professional artifacts.
- Modules 01 through 09, 11, 13, 14, 16, and 18 through 21 were audited and corrected only where
  the current full-module contract exposed missing evidence or controls.
- All twenty-one modules now have current design briefs and scored QA reports.
- Each targeted module has written-first instructor explanation, at least two governed explanatory visual types, required interactions, deterministic applied checks, module-specific FAQs, role lenses, evidence boundaries, completion evidence, and Graph/Community controls.
- Module 17 has five safety, locate, and commissioning-specific FAQs.
- Each targeted module has a module design brief and scored quality-control report.
- Shared targeted-retrofit CSS and JavaScript provide responsive drawers, focus return, reduced-motion treatment, and visible completion controls.
- The course experience architecture records the four revised lesson fingerprints.
- Quality contract version 3 requires whole-course full-module conformance and distinctiveness before
  release.

## Validation record

- `node --check apps/project-management/curriculum/project-retrofit.js`: passed with exit code 0.
- `python3 apps/project-management/qa/test-targeted-retrofit.py`: passed; 4 lessons, 4 unique quiz sequences, 32 component configurations parsed, preserved simulations verified.
- Four `tools/course_conformance.py` commands using the Project Management full-module contract: passed for Modules 10, 12, 15, and 17.
- `python3 tools/course_distinctiveness.py --course apps/project-management`: passed; 21 lessons and 21 archetypes.
- `python3 tools/course_full_conformance.py --course apps/project-management`: passed for all
  twenty-one modules.
- `python3 tools/test-course-distinctiveness.py`: passed; varied lessons accepted and factory repetition blocked.
- `python3 tools/test-course-quality-gate.py`: passed; valid release accepted and three regressions blocked.
- `python3 apps/project-management/.course/build-targeted-retrofit.py`: passed; four scoped delivery pages rebuilt locally.
- The previous version-2 local release manifest verified before the quality-contract upgrade.
  Version 3 now blocks release until the named manual gates and release approval are complete.
- `python3 tools/course_workspace.py scan --course project-management --json`: passed; the dated conversation record is tracked.
- Repository-wide full-module and distinctiveness suites pass for Project Management, Data Before AI,
  and Meaning Before Models.
- The rendered cross-course smoke suite passed all 128 desktop and mobile/reduced-motion page runs
  across 64 lessons. It exposed and verified the correction of a completion-state observer loop in
  the four targeted retrofit modules.

## Release status

Blocked. The lessons are marked `working-review`. Practitioner, factual, desktop/mobile, keyboard, screen-reader, reduced-motion, live-event, and named release reviews remain human-controlled. No publish or commit was performed.

## Concurrent-work boundary

The repository contained pre-existing and concurrent changes, including `apps/project-management/course.yaml`. This retrofit does not overwrite or normalize unrelated edits.

## Next action

Conduct the named practitioner, factual, novice, and accessibility reviews without publishing.
