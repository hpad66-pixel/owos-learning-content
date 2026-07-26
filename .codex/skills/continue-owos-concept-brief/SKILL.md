---
name: continue-owos-concept-brief
description: Take a diagram, concept, article, technical brief, regulation, study, procedure, standard operating procedure, conversation, existing HTML page, or mixed source package through the governed OWOS Concept Brief lifecycle. Use when the user asks to create, continue, revise, research, verify, compile, connect, review, or release a Concept Brief or says to run the Concept Engine on supplied material.
---

# Continue an OWOS Concept Brief

Give the user one conversational workspace. Run internal extraction, research, compilation, and QA
tools yourself.

## Start

1. Read `AGENTS.md`.
2. Read `core/standards/COURSE-PRODUCTION-CONTRACT.md` for the shared OWOS release floor.
3. Read `core/standards/CONCEPT-BRIEF-PRODUCTION-CONTRACT.md` completely.
4. Read `core/standards/OWOS-GRAPHITE-VISUAL-STANDARD.md`.
5. Read `docs/CONCEPT-BRIEF-AUTHORING-GUIDE.md`.
6. Read `../hardeep-soul/SOUL.md` and `../hardeep-soul/authoring/AUTHORING_STANDARD.md` when Hardeep's
   knowledge or voice is used.
7. Locate the existing package under `concept-briefs/`, or create a new structured package with the
   files required by the Concept Brief contract.
8. Preserve the user's substantive direction in the package intake or the initiative conversation
   record.

Treat a supplied page as source material. Never call it verified because it already looks finished.

Follow this default order: preserve and spar over the supplied draft, inventory claims, research and
verify original sources, approve the evidence-backed narrative and storyboard, compile cited HTML,
perform QA, then seek publication approval. Do not generate a new learner-facing HTML page before
research merely because a visual prototype exists. When inheriting an prematurely generated page,
preserve it as a pre-research draft and return the package to research.

## Intake

- Preserve each original with its locator, snapshot when possible, SHA-256 checksum, creator,
  capture date, visibility, permission, extraction coverage, limitations, and disposition.
- Keep internal, private, sealed, permission-pending, and tenant material out of public output.
- Use the PDF, document, browser, image, or other relevant skill when the source format requires it.
- Extract complete material with page, section, figure, paragraph, table, timestamp, or line locators.
- Separate source content from prior assistant interpretation.

## Build the claim register before the page

Inventory every material statement as:

- sourced fact;
- regulatory requirement;
- technical standard;
- expert interpretation;
- Hardeep position;
- instructional scenario;
- commercial claim; or
- unresolved question.

For every claim, record exact source locators, scope, jurisdiction, limitations, affected blocks,
visuals, interactions, Graph edges, and correction impact.

Research services may discover sources. Verify against the original authority. Prefer regulations,
standards, papers, datasets, and issuing organizations for load-bearing claims.

For water, wastewater, stormwater, and One Water topics, use United States governing authorities
only. Start with current federal primary authority and EPA guidance. Exclude state requirements and
non-United States regulations, standards, government guidance, design guides, operator guides, and
health guidelines from the public source register, claim basis, learner narrative, Graph, Community
verification, and reviewer dossier. AWWA material may be used when labeled as United States
professional context rather than federal authority. Research
conducted outside the United States may be retained only as clearly labeled peer-reviewed research
with visible experimental and transfer limitations. It never becomes a governing standard.

Do not promise eternal or absolute truth. Require 100 percent material-claim verification coverage
for release, including independent source trace, independent verifier, freshness dates, and
qualified review for claims affecting engineering, operations, safety, compliance, health, or the
environment.

Keep uncertain or contested claims visible. Do not convert missing evidence into confident prose.

## Design a unique experience

Complete `core/templates/CONCEPT-BRIEF-DESIGN-BRIEF.md` before implementation.

Apply the approved Graphite visual standard by default. Preserve its palette, typography, contrast,
depth, and accent meanings while designing a unique narrative composition for the brief's learning
job. Do not turn Graphite into a fixed section sequence or page mold.

Define the brief's:

- learner job;
- opening pattern;
- narrative archetype;
- central mental model;
- signature mechanism;
- dominant visual;
- interaction signature;
- role treatment;
- closing action;
- surface rhythm;
- avoided patterns; and
- differences from adjacent briefs.

Use the proposed coverage jobs only when the concept needs them. Never force monument numbers, a
simulator, a protocol, term cards, a correction table, a diagnostic, or a commercial section.

Select visuals from `core/standards/VISUAL-ARSENAL.md`. Every visual and interaction needs an
instructional job, instructor explanation, accessible equivalent, mobile treatment, reduced-motion
treatment, source, permission, and rendered review.

Create and obtain approval for the beat-by-beat storyboard before production implementation.

Use the standard names **OWOS Concept Engine** for this lifecycle and **OWOS Concept Brief Compiler**
for its renderer. Read `core/standards/OWOS-LEARNING-CAPABILITY-STANDARD.md` and select all visuals,
interactions, animation, and quizzes through `core/learning-capabilities/registry.yaml`. Do not
duplicate a shared capability definition inside a brief. A full Concept Brief is one focused
learning module with dynamic explanation, distributed checks, an applied transfer check,
cross-sector connection, and deterministic completion evidence unless an approved exception is more
accurate.

Read and apply `core/standards/OWOS-LEARNING-RECORD-CREDENTIAL-AND-PATHWAY-STANDARD.md`. Bind each
brief to the canonical xAPI record, cmi5 launch preference, governed SCORM 2004 compatibility
adapter, fail-closed credential profile, and explainable learner-controlled deepen, reskill, and
cross-skill pathways. Never let an LMS completion value become credential authority.

Complete the six durable learning-system records before implementation: placement and remediation;
shared-registry capability lock; stable learning events with consent, privacy, authority, and
retention plus completion-version preservation and correction notification; assessment governance;
simulation model assurance; and language, units, localization, and measured instructional time.
Public Concept Briefs prohibit facility-sensitive data collection and instructional simulations
prohibit operational use.

Apply the learner-economy contract before compilation. Preserve the deep claim and governance
records internally while keeping the public experience focused: a short orientation, no more than
four primary controls, no public claim-count marketing, one compact feedback entry point at the true
end, the full Community experience in its drawer or route, an outline-only public SOP boundary,
hidden inactive commercial placements, and the approved three-part closing recap and short
disclaimer. Treat these as reusable package and compiler requirements, not manual HTML cleanup.

## Author and compile

Keep intake, identity, design brief, storyboard, narrative, claims, sources, visual manifest,
interactions, Graph, Community, commercial relationships, QA, and approvals separately reviewable.

Validate a working package:

```bash
python3 tools/concept_brief_compiler.py validate concept-briefs/<brief>
```

Compile a visible working preview:

```bash
python3 tools/concept_brief_compiler.py build concept-briefs/<brief> \
  --output concept-briefs/<brief>/dist/preview.html
```

The compiler renders the authored storyboard. It never researches, selects a design, invents
instruction, verifies a claim, or approves a release.

## Connect the Graph

Declare stable nodes and reviewed relationships in `graph.yaml`.

Use exact term, claim, source, question, course module, role, competency, contributor, organization,
and adjacent-concept identifiers. Make reciprocal links explicit.

Keep `SPONSORED_BY`, `CONTRIBUTED_TO`, `REVIEWED_BY`, and `CITES` structurally separate.
`SPONSORED_BY` is never evidence.

Graph publication requires explicit approval. A preview is not a graph publication.

## Connect the Community

Reserve `#owos-concept-community` on the compiled page and carry the brief identifier and version
into the forum context.

Record seed questions, moderation owner, verified-answer policy, discussion boundary, correction
escalation, accessibility, drawer behavior, and focus return in `community.yaml`.

Community discussion never silently changes verified instruction. Route a proposed correction back
through source review, technical review, revision, and approval.

## Protect commercial integrity

Support verified directory relevance, attributed contribution, disclosed sponsorship, and private
tenant briefs.

Keep sponsor, contributor, reviewer, advertiser, and evidence-source roles separate. A sponsor gets
no claim approval, evidence-tier selection, source suppression, correction removal, or editorial
veto.

Run the commercial firewall validation even when monetization is disabled.

## QA and release

Run:

```bash
python3 tools/test-concept-brief-compiler.py
python3 tools/concept_brief_compiler.py portfolio-check concept-briefs
python3 tools/concept_brief_compiler.py validate concept-briefs/<brief> --release-ready
```

Render and inspect desktop, tablet, phone, keyboard, touch, screen reader, reduced motion, no
JavaScript, and read-without-animation states. Retain evidence.

Complete `core/templates/CONCEPT-BRIEF-QA-REPORT.md`. Keep automated checks separate from independent
source, qualified practitioner, editorial, accessibility, novice-reader, Graph, Community,
commercial-conflict, and owner reviews.

A working score never overrides a blocked gate.

Create a release manifest only after release-ready validation passes:

```bash
python3 tools/concept_brief_compiler.py release-manifest concept-briefs/<brief> \
  --html concept-briefs/<brief>/dist/brief.html \
  --output concept-briefs/<brief>/dist/release-manifest.json
```

Require Hardeep's explicit approval before Graph publication, Community release, commercial
placement, credential use, or public release.

## Maintain durable state

Before ending a material turn:

- update intake and source checksums;
- update claim, source, learning-system, correction, Graph, Community, commercial, QA, and approval
  records;
- record the exact compiler commands and results;
- state which manual reviews remain unresolved;
- retain working previews as visibly non-release artifacts; and
- never describe incomplete verification coverage as 100 percent accuracy.
