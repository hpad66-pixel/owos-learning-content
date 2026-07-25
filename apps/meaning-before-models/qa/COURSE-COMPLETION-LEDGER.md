# Meaning Before Models: Course Completion Ledger

Date: 2026-07-25

This ledger is the authoritative answer to “Is the course complete?” It separates curriculum
design, production, review, publication, and final release so that one status cannot be mistaken
for another.

## Current decision

The twenty-module course is final-release complete and live. The owner approved final production
on 2026-07-25. Modules 19 and 20 were produced from governed structured source, validated,
compiled, assembled into the curriculum, deployed, and verified on the custom domain.

## Completion matrix

| Area | Status | Evidence | What remains |
|---|---|---|---|
| Topic, research, evidence boundaries | Complete for current scope | `research/`, `COURSE-BRIEF.md`, `SYLLABUS.md` | Update only when claims or scope change |
| Twenty-module curriculum | Complete and approved | `curriculum/CURRICULUM-PACKAGE.md`, `curriculum/COURSE-DESIGN-MATRIX.md` | Final coherence review after Modules 19–20 exist |
| Twenty lesson contracts | Complete and validated | `curriculum/lesson-contracts/` and module packages | Revalidate when a contract changes |
| Modules 1–18 | Released | `dist/site/`, release manifest, production evidence in `STATE.md` | None for this release |
| Module 19 | Released | `modules/module-19-design-the-one-water-knowledge-spine/` | None for this release |
| Module 20 | Released | `modules/module-20-one-water-knowledge-spine-lab/` | None for this release |
| Module 19 checksum | Final package | `e4e635f87d84ce4ee21469ed4c56f86dc9e146c73496fa042ef6fde0b63b99bf` | Any future source change creates a new candidate |
| Module 20 checksum | Final package | `96244ec642ff08280216ad75382ac5f9e4afa5c6d7d29402e882b6223988ca52` | Any future source change creates a new candidate |
| Course landing and navigation | Released with 20 modules | `dist/site/course-meaning-before-models.html` | None for this release |
| Course Quality-Control Dossier | Complete for owner-directed release | module QA, conformance, browser, Git, deployment, and live evidence | Preserve with release record |
| Final release | Complete | learning commit `3fa7213`, platform commit `7ddc8e3`, deployment `b99131b9` | None |

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

## Final release evidence

- Twenty lesson contracts passed.
- Twenty structured packages passed release-ready compiler validation.
- Whole-course release-ready full-module conformance passed.
- Course distinctiveness passed.
- Structured-authoring audit reports `fully_structured`.
- Landing page, Module 19, and Module 20 passed desktop, iPad, and iPhone browser QA.
- Runtime errors, missing graphics, duplicate IDs, and horizontal overflow: zero.
- The custom-domain Module 19 and Module 20 files matched the deployed platform files byte for byte.
- The live landing page exposes all twenty lesson routes.

The honest final status is:

> Complete, owner approved, published, and live.
