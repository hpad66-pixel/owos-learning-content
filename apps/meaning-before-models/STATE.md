# Course State

Updated: 2026-07-23

## Current phase

Version 0.9.0 public live review deployed

## Version 0.9.0 deployment evidence

- Learning-content pull request: `hpad66-pixel/owos-learning-content#8`
- Learning-content merge: `c7f8b6bc1c519dcc71de2b7c4d4c169c38c81758`
- Release ID: `owos-course-semantic-data-ai-001-v0.9.0`
- Rendered QA: 18 lessons, 36 desktop and phone views, zero failures
- Runtime files: 24 checksum-verified files
- Platform intake pull request: `hpad66-pixel/onewater-os-platform#35`
- Platform intake merge: `d6c100ce22cf9098b3f3ab6db73178dafb7a7ba4`
- Public-asset correction pull request: `hpad66-pixel/onewater-os-platform#36`
- Final production platform merge: `c061988d4fd3c9337b8227312a08db0c09d354c8`
- Cloudflare deployment: `https://78247e29.owos-3n1.pages.dev`
- Public course route: `https://owos.ai/course-meaning-before-models`
- Public access verification: landing and all eighteen canonical lessons return unauthenticated 200
- Live component verification: representative foundation, architecture, validation, and capstone
  lessons passed card, process, visual-control, overflow, and console checks
- Credentials, certification, graph publication, authoritative completion, and operational
  authority: disabled or not configured

## Approved

- Five-part, eighteen-module curriculum blueprint
- Comprehensive semantic-backbone master-class scope
- Foundation, Practitioner, and Leader instructional views
- Work-product, assessment, simulation, FAQ, and capstone direction
- Module 05 capability level for full-course production use
- Full production of all eighteen modules

## Production inventory

- 18 responsive lesson candidates
- 18 module design briefs
- 18 module recording scripts
- 1 course overview recording script
- 18 scored module QA reports, plus the preserved failure audit
- 18 professional work products
- 18 deterministic applied assessments
- 18 same-page Graph and Community experiences
- 18 module-specific FAQ sections
- One governed shared lesson runtime for Modules 01 to 04 and 06 to 18
- The richer Module 05 benchmark runtime remains intact
- A namespaced, self-contained production package for the course landing page and all eighteen
  lessons
- Explicit Hardeep approval to publish the complete course for live review

## Course-wide implementation result

`python3 tools/test-meaning-before-models-course.py`

Result: passed on 2026-07-23.

`python3 tools/build-course-release.py meaning-before-models --check`

Result: version 0.7.0 verified on 2026-07-23 with 24 checksum-controlled runtime files.

The OWOS platform registration branch
`agent/register-meaning-before-models-live-review` passed the Learn, pathway, graph, registry,
course-release, contrast, and formatting checks and was pushed to GitHub at commit
`8a0fa5b4e3443b5ea1e7b3751b47c48b547a9c31`.

## Live deployment evidence

- Learning-content release commit:
  `4b13fe2d1e4d3082fbbaa8af0f715897a8e6f436`
- Release ID: `owos-course-semantic-data-ai-001-v0.7.0`
- Runtime files verified and imported: 24
- OWOS platform registration pull request: `hpad66-pixel/onewater-os-platform#31`
- OWOS platform registration merge:
  `7fc5768fcaaf9d6053f51e3264f27b99851b578c`
- Checksum-verified runtime intake pull request: `hpad66-pixel/onewater-os-platform#32`
- Production platform merge:
  `eeea8727d5fe20f4d6018abc105f6bd8de33ff78`
- Cloudflare deployment:
  `https://754844ee.owos-3n1.pages.dev`
- Production course route:
  `https://owos.ai/course-meaning-before-models`
- Production registry verification: eighteen available modules, exact source commit and release ID,
  credential status `not_configured`
- Production access boundary: authenticated live review

The repository-dispatch secrets were not configured in either GitHub repository. The supported
manual intake path checked out the exact source commit, rebuilt and verified the manifest, ran the
same importer and platform tests, and opened the reviewed runtime intake pull request. Cloudflare
Git auto-deploy was not active, so the exact merged `site/` directory was deployed through the
existing authenticated Cloudflare Pages project.

The course test validates all eighteen lessons against the full-module contract, including:

- actual lesson, brief, recording script, and scored QA report;
- minimum visual, interaction, quiz, FAQ, glossary, work-product, and applied-assessment evidence;
- governed visual, interaction, quiz, Graph, and Community provenance;
- instructor explanation before every governed visual and required assessment;
- stable metadata, semantic landmarks, local assets, unique identifiers, and local navigation;
- responsive and reduced-motion rules;
- evidence boundaries and primary W3C links;
- course landing links to every module; and
- prohibited punctuation and selected blocked language.

## Important production boundary

Repository conformance is not a credential or final-release approval. Version 0.7.0 is authorized
for live review with completion events, credentials, certification claims, and operational authority
disabled. It still requires module-by-module human inspection and review. A high QA score cannot
override a blocked hard gate.

## Version 0.9.0 rendered-component remediation, 2026-07-23

Hardeep rejected the 0.8.0 live-review build after direct use exposed nonfunctional flip cards,
dark visual slabs, repetitive lesson composition, and weak instructional graphics. The release had
passed repository-shape checks while failing the learner's rendered experience. That is a release
gate failure, not a styling preference.

Version 0.9.0 rebuilds all eighteen lessons around eighteen named narrative experiences, eighteen
card compositions, manually authored utility-specific question and answer sets, meaningful visual
outputs, corrected assessment logic, keyboard-operable cards, reduced-motion states, and visible
process feedback. A real-browser suite now operates every required component in desktop and phone
views and records a source-bound receipt. Release packaging refuses a missing, failed, or stale
receipt.

The 0.9.0 candidate may replace the rejected live-review runtime after all automated checks pass.
Credentials, certification, graph publication, authoritative completion, and operational authority
remain disabled. Independent factual, practitioner, novice, screen-reader, and physical-device
reviews remain human gates.

## Remaining hard gates

- Hardeep working review of the complete sequence and representative lessons
- Independent RDF, RDFS, SPARQL, OWL, SHACL, semantic architecture, and AI-context review
- Real water, wastewater, stormwater, data, cybersecurity, and operations practitioner review
- Novice-learner comprehension pilots
- Independent screen-reader and physical touch-device review
- Desktop, tablet, phone, keyboard, screen-reader, contrast, zoom, touch, and reduced-motion reviews
- Authenticated learner-event and enrollment validation
- Capstone scoring review
- Graph publication approval
- Credential approval
- Final credential-bearing release approval

## Next action

Continue staged human, practitioner, accessibility, device, authenticated-runtime, and capstone
review against the deployed live-review course. Correct findings in governed source and release a
new version. Configure the two cross-repository GitHub secrets and Git-connected Cloudflare
deployment so future releases do not require the manual intake and direct Pages fallback. Do not
publish approved domain claims to the shared graph or issue a credential until those separate
approvals are recorded.

## Visual-variety remediation, 2026-07-23

Hardeep rejected the repeated lesson appearance and instructed a complete course rebuild plus a
permanent prevention mechanism. The root cause was a weak implementation gate: the generator reused
one dominant lesson body and one quiz sequence, while QA counted renamed `data-visual-type` labels
instead of rendered structures.

Version 0.8.0 replaces that system across all eighteen lessons:

- four lesson-specific explanatory graphics per lesson, selected from the approved visual blueprint;
- at least four question-and-answer flip cards per lesson;
- the approved module-specific quiz sequence plus an applied work-product assessment;
- explicit visual family and structural-shape fingerprints;
- course-wide checks for inner visual structure, unique dominant visuals, adjacent visual sequences,
  adjacent quiz sequences, and a minimum of fifty-five lesson-specific visual types; and
- permanent updates to the production contract, design system, Visual Arsenal, quiz rules, templates,
  course-continuation skill, repository agent instructions, and future-course scaffold.

Repository QA passes. Version 0.8.0 is authorized for corrected live-review publication by the
standing course publication instruction. Credentials, certification, graph publication, and
operational authority remain disabled.

The 0.8.0 publication workflow also added a packaged-runtime parity gate after exact-commit intake
detected stale `dist/site` files. Future releases must run
`python3 tools/build-meaning-before-models-release.py` before the generic manifest builder, and the
course regression test now compares source and packaged visual shapes, quiz sequences, JavaScript,
and CSS.

## Version 0.8.0 live deployment evidence

- Learning-content source and package commit:
  `8f87aecbcf5afb145d69e4acf117d08a3ff34a9c`
- Learning-content pull requests:
  `hpad66-pixel/owos-learning-content#5` and `#6`
- Release ID: `owos-course-semantic-data-ai-001-v0.8.0`
- Runtime files: 24 checksum-verified files
- OWOS platform intake pull request:
  `hpad66-pixel/onewater-os-platform#33`
- Production platform merge:
  `b53337183f64fd9999fa7d6d56826f8b998e5199`
- Cloudflare deployment:
  `https://b2ee424d.owos-3n1.pages.dev`
- Production course route:
  `https://owos.ai/course-meaning-before-models`
- Production registry verification:
  exact release ID and source commit on both deployment and primary domains
- Access boundary:
  authenticated live review; unauthenticated course requests redirect to sign-in
- Credentials, certification, graph publication, completion events, and operational authority:
  disabled or not configured
