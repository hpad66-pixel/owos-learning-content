---
course_id: owos-course-semantic-data-ai-001
course_title: "Meaning Before Models: RDF and Knowledge Graphs for Utilities"
version: 0.9.0-live-review
review_date: 2026-07-24
reviewer: Codex automated and rendered working review
score: 89
score_out_of: 100
working_status: approved_working_candidate
release_status: blocked
source_commit:
platform_commit:
deployment_id:
---

# Course Quality-Control Dossier

## Executive decision

- Working-review result: passed for continued live-review production
- Release result: blocked for final credential-bearing release
- Evidence-backed score: 89 of 100
- Hard gates passed: learning design and automated technical implementation
- Hard gates conditional or blocked: independent accuracy, practitioner, accessibility, learner,
  authentication, credential, and final-release review

Modules 01 through 17 use verified structured source and distinct compiled experiences. The course
passes automated conformance and distinctiveness, the graphic scrub now passes 71 of 71 SVG files,
and the redesigned landing page passes source and packaged desktop, tablet, and phone browser
review. The planned nineteen-module curriculum is not complete until Modules 18 and 19 are produced.

## Scored course review

| Area | Weight | Score | Evidence location | Defects or remaining work |
| --- | ---: | ---: | --- | --- |
| Curriculum formulation and sequence | 10 | 10 | `curriculum/CURRICULUM-SEQUENCE-REVIEW.md`, 19 contracts | Modules 18 and 19 not produced |
| Complete conversational teaching without video | 12 | 11 | Module source packages and full conformance | Novice human pilot pending |
| Module uniqueness and course coherence | 10 | 10 | `course_distinctiveness.py`: 18 lessons, 18 archetypes | Final 19-module rerun required |
| Visual reasoning, containment, and pacing | 12 | 11 | 71 SVGs, 1,119 text elements, zero final failures | Human zoom review pending |
| Interactions and simulations | 10 | 9 | Module browser suites and signature-component captures | Human usability review pending |
| Assessment variety, feedback, and retry | 9 | 9 | Structured assessments and distinct quiz sequences | Learner observation pending |
| Professional work-product progression | 7 | 6 | Module work products and starter-pack progression | Final capstone not produced |
| Utility relevance and practitioner credibility | 8 | 6 | Water, wastewater, and stormwater cases | Independent practitioner review pending |
| Accuracy, provenance, and evidence boundaries | 8 | 6 | Source files, claims boundaries, W3C references | Independent technical review pending |
| Accessibility, responsive behavior, and motion | 7 | 5 | Automated desktop, tablet, phone, focus, overflow, motion | Screen-reader and physical-device review pending |
| Platform integration and live proof | 7 | 6 | Existing live deployment evidence through Module 17 | Retrofit not yet republished |
| **Total** | **100** | **89** | Repository evidence | Hard gates remain |

## Module score register

| Module group | Score evidence | Hard gates | Package evidence | Release status |
| --- | --- | --- | --- | --- |
| Module 01 | 86 | conditional | Structured checksum and rendered captures | live review |
| Modules 02 through 11 | Individual QA evidence reports | conditional | Verified structured packages | live review |
| Modules 12 and 13 | 94 each | conditional | Structured checksums and 18 browser runs | live review |
| Module 14 | 90 | conditional | Structured checksum and 9 browser runs | live review |
| Modules 15 and 16 | 91 each | conditional | Structured checksums and 18 browser runs | live review |
| Module 17 | 93 | conditional | Structured checksum and 9 browser runs | live review |
| Module 18 | not scored | blocked | Lesson contract only | not produced |
| Module 19 | not scored | blocked | Lesson contract only | not produced |

## Evidence index

| Evidence class | Exact location or identifier | Result |
| --- | --- | --- |
| Curriculum | `curriculum/CURRICULUM-SEQUENCE-REVIEW.md` | 19-module sequence approved |
| Lesson contracts | `modules/module-*/lesson-contract.yaml` | 19 contracts passed |
| Structured source | `.course/authoring.json` | 17 structured, 1 legacy live lesson |
| Module QA | `qa/module-*-quality-control-report.md` | Present for the current 18 live lessons |
| Visual containment | `qa/graphic-text-containment-report.md` | 71 files and 1,119 text elements passed |
| Landing-page rendering | `qa/rendered/course-landing/` | Desktop, tablet, and phone captures |
| Landing behavior | `qa/course-landing-browser-validation.cjs` | Source and packaged runs passed |
| Distinctiveness | `tools/course_distinctiveness.py` | 18 lessons and 18 archetypes passed |
| Full conformance | `tools/course_full_conformance.py` | Existing 18-lesson release passed |
| Release manifest | `dist/release-manifest.json` | 97 checksum-controlled files |

## Hard release gates

| Gate | Status | Evidence | Required action |
| --- | --- | --- | --- |
| Accuracy and evidence | conditional | Source packages and W3C boundaries | Independent semantic review |
| Learning design and course coherence | passed | Contracts, sequence, conformance, distinctiveness | Rerun after Modules 18 and 19 |
| Utility-practitioner credibility | blocked | Utility examples present | Qualified practitioner review |
| Technical accessibility and security | conditional | Automated browser results | Screen-reader, zoom, physical-device, and security review |
| Release, credential, and authority | blocked | Live-review authority only | Final human and credential approval |

## Defect and correction ledger

| Defect | Severity | Affected scope | Repair | Regression evidence | Status |
| --- | --- | --- | --- | --- | --- |
| SVG text escaped intended boxes | high | 21 labels in 12 graphics | Repaired source text bounds | 71 SVGs, 1,119 elements, zero failures | closed |
| Landing-page hero had weak hierarchy and production-state copy | high | Course landing top | New semantic course hero and route | Six source and packaged browser runs | closed |
| Approved curriculum has 19 modules while live course has 18 | high | Modules 18 and 19 | Contracts retained and activation held | Curriculum review and approvals | open |

## Human review register

| Review | Result |
| --- | --- |
| Factual and source review | pending |
| Utility-practitioner review | pending |
| Novice-learner review | pending |
| Desktop, tablet, phone, and zoom visual review | pending |
| Keyboard and screen-reader review | pending |
| Authentication and learner-event review | pending |
| Credential and final-release review | pending |

## Publication proof

This retrofit has not yet been republished. Populate source commit, platform commit, deployment,
custom-domain checksums, live browser results, and remote synchronization after publication is
explicitly authorized.
