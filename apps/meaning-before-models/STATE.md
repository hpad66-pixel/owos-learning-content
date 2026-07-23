# Course State

Updated: 2026-07-23

## Current phase

Version 0.7.0 live-review release preparation

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

## Remaining hard gates

- Hardeep working review of the complete sequence and representative lessons
- Independent RDF, RDFS, SPARQL, OWL, SHACL, semantic architecture, and AI-context review
- Real water, wastewater, stormwater, data, cybersecurity, and operations practitioner review
- Novice-learner comprehension pilots
- Successful rendered browser learner-path regression for every module
- Desktop, tablet, phone, keyboard, screen-reader, contrast, zoom, touch, and reduced-motion reviews
- Authenticated learner-event and enrollment validation
- Capstone scoring review
- Graph publication approval
- Credential approval
- Final credential-bearing release approval

## Next action

Merge the validated OWOS platform registration, merge the exact learning-content release, dispatch
the governed course intake, merge the generated intake pull request, and verify the Cloudflare
production URL. Continue staged human review after deployment. Do not publish approved domain claims
to the shared graph or issue a credential until those separate approvals are recorded.
