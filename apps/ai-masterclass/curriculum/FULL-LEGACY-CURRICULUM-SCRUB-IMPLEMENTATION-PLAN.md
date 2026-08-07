# Full Legacy Curriculum Scrub Implementation Plan

## Decision

Extend the approved M00 curriculum-scrub pattern across legacy M01 through M63. Preserve M00 as the
benchmark and preserve the Fellowship line as a separate curated delivery sequence.

The result will give staff a complete research and production brief for every source module without
pretending that a blueprint is a finished lesson. Every current section, proposal, proposal
subtopic, targeted enhancement, and contributor record will remain visible by stable identifier and
will receive a reviewable placement recommendation.

## Governing authority

- Curriculum authority: `hpad66-pixel/owos-learning-content`
- Application authority: `hpad66-pixel/apas-academy-studio`
- Source line: `legacy:M00` through `legacy:M63`
- Curated delivery line: `fellowship:M01` through `fellowship:M64`
- Approved pattern: legacy M00, `Orientation, Setup, and Your Learning Path`
- Release state: internal blueprint production, not learner-facing release

## Required package for every remaining module

Each legacy module from M01 through M63 will receive:

1. `README.md`, explaining authority, status, source lineage, and how staff should use the package.
2. `MODULE-GUIDANCE.json`, carrying the module purpose, staff summary, learner outcomes, curriculum
   outcomes, internal marketing outcomes, professional work product, definition of done, evidence
   boundary, and governed file paths.
3. `STAFF-DIRECTION.md`, giving direct instructions to research, curriculum, writing, graphics,
   assessment, Articulate, marketing, and quality-control teams.
4. `AI-RESEARCH-AND-PRODUCTION-PROMPT.md`, requiring goal-first and plan-first work, exact source
   locators, claim separation, United States evidence boundaries, water-sector grounding, and human
   review.
5. `CONTENT-PLACEMENT-REGISTER.json`, preserving every granular content record and proposing retain,
   refine, move, copy, cross-reference, optional-preparation, consolidate, or defer without deleting
   the original.
6. `production-status.md`, showing the real state of research, evidence, design, practitioner,
   accessibility, production, and release gates.
7. A module-specific design brief under `curriculum/design-briefs/` with the learning job, opening
   situation, first decision, work product, natural visual shapes, purposeful interactions, varied
   assessments, role treatment, professional consequence, FAQ direction, and adjacent-module
   diversity check.

## Quality floor

Every module package must be specific enough that a staff member can answer these questions without
guessing:

- Why does this module exist?
- What real water, wastewater, stormwater, or One Water decision makes it matter?
- What must the learner explain, distinguish, evaluate, create, or defend?
- What professional work product proves useful learning?
- What belongs in this module, what belongs elsewhere, and what remains uncertain?
- What must the research team verify using exact sources and locators?
- What must the graphics and interaction team make visible?
- What evidence must assessment produce?
- What may marketing say, and what claims are prohibited?
- Which human reviewers must approve the work before production?

The packages will use plain English, Hardeep Soul, backward design, observable outcomes, the OWOS
Visual Arsenal, the course design matrix, the learning-record standard, and the Course Production
Contract. No package will use an em dash, en dash, blocked artificial-intelligence phrase,
unsupported statistic, invented incident, or decorative visual direction.

## Content-placement method

The scrub will cover the complete granular source inventory, including nested proposal subtopics.
The default is preservation. A move or consolidation recommendation must state why the learner's
sequence improves, where the content goes, whether the original keeps a reference, which source and
contributor remain attached, and who must approve the change.

Current sections will not be moved merely to create motion. Orientation, objective, assessment,
role-guidance, glossary, evidence, and source sections may be refined when they do not yet produce
observable learning or exact evidence. Proposed additions and contributor inputs remain proposed
until an owner decision changes their status. Duplicate records remain visible and consolidate
under a named surviving record.

## Data and generation architecture

The durable authoring source will be a readable, versioned module-guidance catalog with one unique
record for each of the 64 legacy modules. A deterministic builder will combine that catalog with the
canonical granular curriculum and contributor review to produce the module packages. Generated
files remain committed and readable so reviewers do not need to run a tool to understand the
curriculum.

The Academy registry builder will fail when:

- any legacy module lacks guidance;
- a stable current, proposal, subtopic, enhancement, or contributor identifier is omitted;
- a placement record points to an unknown module;
- an outcome, work product, prompt, direction file, or design brief is missing;
- a contributor or source identity is dropped; or
- the generated package and canonical sources drift.

## Academy implementation

The Academy will receive the rebuilt governed registry. Existing guidance editing, Markdown
preview, prompt copying, placement editing, destination selection, approval, audit, and provenance
controls will apply to every legacy module. The application must remain usable when a module has a
large placement inventory. Search, filters, expandable groups, and phone layouts must not regress.

Git remains canonical for approved teaching records. Academy database records remain collaboration
state until an authorized owner decision is committed back to the curriculum repository.

## Validation plan

1. Validate all JSON and generated Markdown paths.
2. Require exactly 64 guided legacy modules and 64 unique module packages.
3. Compare placement identifiers against the canonical granular inventory and contributor review.
4. Rebuild the Academy registry twice and require deterministic output.
5. Run the curriculum registry contract and new full-guidance contract tests.
6. Run Hardeep voice and punctuation checks across the new authoring files.
7. Import the registry into the Academy and run its build, lint, and automated tests.
8. Test a representative module from every curriculum part, including modules with proposals,
   enhancements, contributor inputs, and large section inventories.
9. Test the full M01 through M63 navigation and opening path on desktop and phone.
10. Verify editing, placement changes, preserved provenance, revision history, and error-free use.

## Completion boundary

This plan is complete when all 64 legacy modules have governed blueprint packages and the private
Academy presents them consistently. It does not make 64 learner-facing lessons complete. Each
lesson still requires registered sources, claim verification, manuscript production, recording
script, practitioner review, novice review, accessibility review, Articulate production, rendered
browser testing, the binding full-module conformance command, and owner release approval.

## Implementation record

Completed on 2026-08-06:

- 64 governed legacy module packages built;
- 63 new unique guidance specifications added for M01 through M63;
- 1,397 granular content records preserved and registered;
- 64 design briefs and one complete course design matrix built;
- Academy registry rebuilt with all guidance, prompts, placements, paths, and provenance;
- Academy editing expanded for the full blueprint and large placement inventories;
- deterministic content and registry contracts passed;
- Hardeep voice and punctuation checks passed;
- Academy build, lint, automated tests, desktop browser checks, and phone checks passed; and
- full-module conformance correctly recorded as not eligible because these packages are blueprints,
  not finished learner-facing lessons.
