---
phase: 13
module_id: mbm001:18
module_title: Graph-Grounded Agentic Applications
review_date: 2026-07-25
requested_package_checksum: 466bd24a0d94b09360dd7ccaa55425d78fbfde7dc288a4afa2195432dc3741e4
revised_package_checksum: 34f8325bd83447a1bb549da13a02b79c44b5d3e7c99b83e0b6aeaa9b8d8cf4ca
compiler_version: 1.1.0
phase_13_status: automated_checks_passed
release_status: blocked_pending_human_gates
---

# Phase 13 Deterministic QA Report

## Decision

Module 18 passes the performed Phase 13 automated checks and is recommended to enter Phase 14
human review as a working candidate. It is not approved for publication, credentialing, or final
release.

The checksum supplied at Phase 13 entry was
`466bd24a0d94b09360dd7ccaa55425d78fbfde7dc288a4afa2195432dc3741e4`.
The governed package changed only because Phase 13 repaired compiler/runtime conformance and
accessibility behavior. The resulting deterministic checksum is
`34f8325bd83447a1bb549da13a02b79c44b5d3e7c99b83e0b6aeaa9b8d8cf4ca`.

## 1. Passed automated checks

| Check | Result | Exact evidence |
| --- | --- | --- |
| Structured-package validation | Passed | `course_compiler.py validate`; module `mbm001:18`; checksum `34f832…f4ca` |
| Deterministic compilation | Passed | Compiler `1.1.0`; build at `modules/module-18-graph-grounded-agentic-applications/build/index.html` |
| Lesson-contract validation | Passed | 19 contracts validated |
| Full-module conformance | Passed | 5 visual types, 6 purposeful interactions, 4 quiz types, 7 required completion items, 10 terms, and all 6 Community capabilities |
| Course distinctiveness | Passed | 18 lessons and 18 distinct archetypes |
| Structured-authoring audit | Passed | 17 structured packages synchronized; legacy courses correctly remain identified as migration work |
| SVG containment | Passed | 76 files; 1,244 text elements; zero violations |
| Desktop browser QA | Passed | 1440 CSS px; no errors or horizontal overflow |
| iPad/tablet browser QA | Passed | 820 CSS px; no errors or horizontal overflow |
| iPhone/phone browser QA | Passed | 390 CSS px; no errors or horizontal overflow |
| 200% reflow QA | Passed | 720 CSS px equivalent; no errors or horizontal overflow |
| 400% reflow QA | Passed | 360 CSS px equivalent; no errors or horizontal overflow |
| Keyboard and focus QA | Passed | Graph and Community opened with Enter; Escape closed; focus returned |
| Reduced-motion QA | Passed | Maximum transition duration 0.01 ms in reduced-motion mode |
| Contract scoring and defense | Passed | Required fields, correct defense, scoring, save, and completion path executed |
| Contract export | Passed | Browser download completed with a JSON artifact filename |
| Author Studio production-copy structure | Passed | Permanent Courses workspace contains responsive preview controls and human-gate boundary |

## 2. Repaired tooling defects

1. The retired full-module checker only recognized legacy hand-authored markers. It now recognizes
   structured compiler metadata, governed Graph and Community drawers, visual provenance,
   distributed assessments, completion controls, glossary terms, connected learning, signature
   simulations, and native applied work products.
2. The structured runtime now supplies governed Graph and Community drawer provenance and all
   required Community capabilities.
3. The work-product renderer now exposes final-applied-check and artifact identifiers used by
   conformance and export QA.
4. Extreme magnification exposed a sticky-toolbar obstruction. At narrow reflow widths the toolbar
   is now non-sticky and vertically stacked, preserving access to assessments.
5. Author Studio now contains Desktop, iPad, and iPhone preview toggles plus 100%, 200%, and 400%
   zoom controls in the Courses workspace.

## 3. Conditional gates

| Gate | Why conditional | Required evidence |
| --- | --- | --- |
| Accuracy and evidence | Automated source boundaries are present; human factual judgment is not automated | Independent semantic-technology and source review |
| Utility realism | Wastewater cases and assumptions are explicit; operating realism needs practitioners | Wastewater operations, maintenance, governance, and cybersecurity review |
| Accessibility | Keyboard, focus, reflow, reduced motion, containment, and text equivalents passed | Screen-reader and physical-device review |
| Course coherence | Module 18 handoff is testable but Module 19 is not yet assembled into the final sequence | Module 19 and whole-course coherence review |
| Platform review | Production copy is prepared inside Author Studio | Authenticated owner inspection in Author Studio |

## 4. Blocked human gates

The following were not performed and are not represented as passed:

- Hardeep working approval
- utility practitioner review
- novice-learner observation
- independent factual and source review
- independent security and industrial-control review
- credential review
- screen-reader review
- physical iPhone and iPad review
- Module 19 and final course-coherence review
- final-release approval

## 5. Exact evidence and checksums

- Requested Phase 13 checksum:
  `466bd24a0d94b09360dd7ccaa55425d78fbfde7dc288a4afa2195432dc3741e4`
- Revised governed checksum:
  `34f8325bd83447a1bb549da13a02b79c44b5d3e7c99b83e0b6aeaa9b8d8cf4ca`
- Compiler version: `1.1.0`
- Full-module checker: `tools/course_conformance.py`
- Browser QA: `qa/module-18-structured-browser-validation.cjs`
- Desktop capture: `qa/rendered/module-18/desktop/full-page.png`
- Tablet capture: `qa/rendered/module-18/tablet/full-page.png`
- Phone capture: `qa/rendered/module-18/phone/full-page.png`
- 200% capture: `qa/rendered/module-18/zoom200/full-page.png`
- 400% capture: `qa/rendered/module-18/zoom400/full-page.png`
- SVG audit: 76 files, 1,244 text elements, zero violations
- Browser audit: five page runs, zero failures

## 6. Recommendation for Phase 14

Enter Phase 14 as a human-review candidate in One Water OS Author Studio. Use its integrated
Desktop, iPad, iPhone, 200%, and 400% controls to conduct owner review, then route the same
candidate to the named practitioner, novice, factual, security, accessibility, credential, and
course-coherence reviewers. Do not publish or mark final release approved until those gates have
documented evidence.
