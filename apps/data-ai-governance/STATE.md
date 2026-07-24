# Data Before AI Course State

Updated: 2026-07-23

## Current phase

Full-course working review. All twenty-five chapters pass individual and whole-course conformance
plus course distinctiveness. No release, publication, runtime intake, or credential work is
authorized.

## Completed in the current retrofit

- Chapters 00 through 09 audited, corrected where required, and supplied with individual design
  briefs and scored QA reports.
- Chapters 10 through 24 rebuilt from destination shells into complete written-first lessons.
- All twenty-five chapters now have individual design briefs and scored QA reports.
- Course-specific styling and behavior support distinct visual, interaction, assessment, and
  work-product fingerprints.
- Quality contract version 3 requires full-module conformance and course distinctiveness before
  release.

## Automated result

- `python3 tools/course_full_conformance.py --course apps/data-ai-governance`: passed for all
  twenty-five chapters.
- `python3 tools/course_distinctiveness.py --course apps/data-ai-governance`: passed with twenty-five
  lessons and twenty-five archetypes.
- `python3 tools/test-data-ai-governance-retrofit.py`: passed the Chapters 10 through 15 regression
  and unique-fingerprint checks.
- Shared and lesson-specific JavaScript syntax, component configuration parsing, and scoped
  formatting checks passed.
- The rendered cross-course smoke suite passed all 128 desktop and mobile/reduced-motion page runs
  across 64 lessons with zero runtime, Graph drawer, focus-return, overflow, or empty-control
  failures.

## Remaining hard gates

- Controlled-source and factual review for each domain.
- Utility-practitioner review, including billing, stormwater, OT, customer service, privacy, records, and operations.
- Desktop, mobile, touch, keyboard, screen-reader, and reduced-motion rendered review.
- Novice read-without-video pilot.
- Authenticated learner-event validation only after release scope is approved.
- Hardeep release approval is not recorded.

## Next action

Conduct the named source-owner, practitioner, novice, and accessibility reviews. Preserve
`release_status: blocked` until those reviews and final release approval are recorded.
