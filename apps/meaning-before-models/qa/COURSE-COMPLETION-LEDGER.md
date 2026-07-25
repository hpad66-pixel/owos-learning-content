# Meaning Before Models: Course Completion Ledger

Date: 2026-07-25

This ledger is the authoritative answer to “Is the course complete?” It separates curriculum
design, production, review, publication, and final release so that one status cannot be mistaken
for another.

## Current decision

The twenty-module curriculum architecture is complete and approved.

The course is **not yet final-release complete**. The current learner-facing live-review release
contains Modules 1–18. Module 19 is an approved design package awaiting structured production.
Module 20 is a compiled structured prototype awaiting owner review, full responsive and human
review, Module 19 handoff validation, and release approval.

## Completion matrix

| Area | Status | Evidence | What remains |
|---|---|---|---|
| Topic, research, evidence boundaries | Complete for current scope | `research/`, `COURSE-BRIEF.md`, `SYLLABUS.md` | Update only when claims or scope change |
| Twenty-module curriculum | Complete and approved | `curriculum/CURRICULUM-PACKAGE.md`, `curriculum/COURSE-DESIGN-MATRIX.md` | Final coherence review after Modules 19–20 exist |
| Twenty lesson contracts | Complete and validated | `curriculum/lesson-contracts/` and module packages | Revalidate when a contract changes |
| Modules 1–18 | Published for live review | `dist/site/`, release manifest, production evidence in `STATE.md` | Remaining named human and final-release gates where not recorded |
| Module 19 | Design package complete | `modules/module-19-design-the-one-water-knowledge-spine/` | Owner design approval, structured authoring, compilation, QA, human review, release |
| Module 20 | Structured prototype complete | `modules/module-20-one-water-knowledge-spine-lab/` | Owner review, remediation, complete Phase 13/14 matrix, named human reviews, Module 19 handoff, release |
| Module 20 checksum | Fixed prototype candidate | `7baddc5a423ef7f037fa84361b0d28126a782e5244bbd7f9ee7b0f4590ece962` | Any source change creates a new checksum and invalidates prior review evidence |
| Course landing and navigation | Complete for 18-module live-review release | `dist/site/course-meaning-before-models.html` | Reconcile to 20 modules only after Modules 19–20 pass release gates |
| Course Quality-Control Dossier | Incomplete | module QA and rendered evidence under `qa/` | Assemble final immutable 20-module dossier |
| Final release | Not approved | `course.yaml` delivery boundary | Named reviews, exact-checksum approval, Git, deployment, and custom-domain proof |

## Status language

- **Designed** means the contract, sequence, scenario, evidence boundary, and storyboard are ready.
- **Prototype complete** means structured source compiles and the intended mechanisms can be
  reviewed. It does not mean release ready.
- **Automated QA passed** means only the performed machine checks passed.
- **Owner approved** means the owner accepted the named checksum. It does not substitute for
  practitioner, factual, security, accessibility, physical-device, credential, or coherence review.
- **Published for live review** means a learner-facing candidate is available. It is not the same
  as final-release approved.
- **Final-release complete** requires the exact approved checksum, all named gates, reproducible
  source and output, Git proof, production deployment, and live custom-domain verification.

## Next actions in prerequisite order

1. Return to Module 19, approve its design package, and produce it through structured authoring,
   deterministic QA, owner review, and named human review.
2. Revalidate the Module 19-to-Module 20 handoff against the existing Module 20 prototype.
3. Review Module 20’s structured prototype in Author Studio and apply only bounded findings.
4. Complete Module 20’s remaining responsive, accessibility, practitioner, factual, security,
   physical-device, credential, and coherence gates against one checksum.
5. Reassemble and test the twenty-module landing page and connected curriculum.
6. Produce the final Course Quality-Control Dossier.
7. Obtain final release approval, then commit, deploy, and verify the live custom-domain release.

Until all seven actions are evidenced, the honest status is:

> Twenty-module system designed; eighteen modules in live review; Module 19 design ready; Module 20
> prototype ready; final course release pending.
