---
title: Concept Engine Initiative Evaluation
status: APPROVED FOR IMPLEMENTATION
owner: Hardeep Anand
evaluated: 2026-07-25
scope: Cross-course OWOS learning and knowledge product
prototype: owf-concept-001-v4_2.html
---

# Concept Engine Initiative Evaluation

## Decision

Advance the Concept Engine as a governed OWOS product initiative.

Do not treat the attached HTML as a released brief, a completed course module, or a reusable fixed
lesson template. The valuable product is a connected family of concise concept experiences that can
serve the Dictionary, the Graph, courses, work products, role dashboards, and the Water Directory.

The proposed public name is **Concept Briefs**. "Concept Engine" is the internal authoring,
governance, and graph-publishing system that produces them.

### Implemented direction

The initiative is now implemented as a separate `owos-concept-brief/2` package and compiler, not an
extension of the course compiler. It shares the authoritative learning-capability registry with the
Course Engine and has its own intake, claims, sources, narrative, storyboard, learning, assessment,
visual, interaction, Graph, Community, commercial, QA, approval, compilation, and correction
records.

The public experience deliberately subtracts internal machinery: it opens with a short orientation,
uses no more than four primary controls, does not market claim counts, keeps SOP value to an outline,
routes full discussion to Community, shows only active commercial connections after teaching, and
ends with a three-part recap plus one compact feedback entry. These are compiler and QA requirements,
not manual edits to the pilot.

## Why this belongs in OWOS

The live OWOS homepage already organizes the first user job as "I need to understand something" and
routes people to Ask the Graph, Droobi, and the One Water Dictionary. Concept Briefs fill the missing
depth between a term definition and a complete course:

| Surface | User question | Appropriate depth |
| --- | --- | --- |
| Dictionary | What does this term mean? | Short governed definition |
| Concept Brief | How does this concept work, what breaks, and why does it matter? | Focused explanation with evidence and interaction |
| Course | Can I learn and demonstrate this capability? | Sequenced instruction, practice, assessment, and work product |
| Graph | What does the evidence say about my question? | Contextual answer with provenance and access controls |
| Work | What should I create or decide? | Governed applied output |

This initiative supports the OWOS operating loop: capture, govern, connect, apply, and strengthen.

## Value by audience

| Audience | Primary value | Product proof required |
| --- | --- | --- |
| Operator | Safe practice with failure modes that are hard to demonstrate on a live plant | Scenario or simulation, plant-floor interpretation, runnable protocol, and consequence feedback |
| Designer and engineer | Fast access to contested assumptions, design basis, and correction history | Primary sources, jurisdiction, design context, limitations, and professional review |
| Consultant | Attributed expertise, reusable staff development, and governed contribution | Contributor record, authorship role, review history, and tenant-safe reuse |
| Utility executive | Aggregated capability, risk, readiness, and operational consequence | Dashboard roll-up, not a requirement to read every brief |
| Vendor | Topic-relevant visibility and a governed way to contribute useful knowledge | Verified directory identity, labeled commercial relationship, and editorial firewall |
| Regulator and government | Traceable explanation of requirements and practice boundaries | Effective date, jurisdiction, official source, and no implication that one rule is universal |
| Researcher and educator | A path from evidence to practice questions and learning | Citation lineage, contested viewpoints, research gaps, and contributor credit |

## Framework ruling on the nine blocks

The proposed nine blocks are valuable as a coverage model:

1. concept anchors or monument figures;
2. why it matters;
3. an interactive or worked mechanism;
4. key terms in plain English;
5. system fit and downstream consequences;
6. corrections and contested claims;
7. a runnable protocol when the topic supports one;
8. do and do-not decisions with consequences; and
9. self-diagnostic, role takeaways, and a next action.

They must not become nine mandatory sections in the same order on every brief. That would violate
the Course Production Contract, Course Design System, Course Experience Architecture, and the
portfolio distinctiveness requirement.

For each brief, the authoring package must select and order the needed teaching moves from the
learning problem. A protocol does not belong in a purely conceptual topic. Monument numbers do not
belong where numeric anchors would create false precision. The signature interaction, visual
language, opening, assessment, and work connection must vary deliberately across adjacent briefs.

## Proposed graph contract

Each published brief should have a stable identifier and explicit, reviewable edges:

| Edge | Target | Rule |
| --- | --- | --- |
| `DEFINES` | Lexicon term | Reciprocal link from the term to the brief |
| `TEACHES_INTO` | Course module or pathway | Names the exact learning use, not a generic course link |
| `ANSWERS` | Governed question pattern | Carries the sections or claims that support the answer |
| `CITES` | Source or claim record | Includes authority tier, locator, date, and review state |
| `CORRECTS` | Prior claim, graphic, or version | Preserves the original error and correction history |
| `ADJACENT_TO` | Related concept | Requires a stated relationship such as upstream, downstream, prerequisite, or contrast |
| `APPLIES_TO_ROLE` | Role or competency | States the decision or action affected |
| `SPONSORED_BY` | Organization relationship | Kept structurally separate from evidence and editorial edges |

`SPONSORED_BY` must never be traversed as evidence for a claim. A sponsor may not receive claim
approval, correction removal, tier selection, source suppression, or editorial veto rights.

## Navigation recommendation

Add **Concept Briefs** to the "I need to understand something" entry card after Dictionary. Add it to
the site map and the learning or knowledge footer group.

Do not add another permanent item to an already crowded global header until navigation testing shows
that users need it there. The prototype's long horizontal nav is useful as an information
architecture sketch, but it is not the recommended public navigation pattern.

Use these reciprocal routes:

- Dictionary term -> relevant Concept Briefs
- Concept Brief -> Dictionary terms, exact course modules, related questions, sources, corrections,
  adjacent concepts, and verified practice organizations
- Course module -> prerequisite or remediation briefs
- Graph answer -> brief sections and claim records
- Role dashboard -> saved briefs, assigned briefs, competency evidence, and aggregate results

The live route check on 2026-07-25 returned HTTP 200 for `/briefs`, but it served the homepage
fallback rather than a distinct Concept Briefs experience. The route should not be treated as
implemented merely because it returns 200.

## Commercial model and editorial firewall

Use three commercial layers:

1. **Verified directory relevance**: eligible organizations can appear because their governed
   capabilities match the topic.
2. **Attributed contribution**: qualified practitioners can contribute cases, sources, review, or
   teaching, with their role and disposition visible.
3. **Private tenant briefs**: a utility, consultant, or vendor can use the engine for governed
   internal methods and SOPs without converting private material into public editorial content.

Public placement should be priced around qualified topic engagement and verified capability, not
undifferentiated banner impressions. Launch public paid placement only after there is enough
inventory and audience activity to make the offer credible.

Required controls:

- commercial relationships are labeled at the point of display;
- editorial contributors and sponsors are different roles;
- no sponsored technical claim;
- no sponsor review or veto rights;
- no suppression of corrections or contested evidence;
- sponsor edges remain separate from citation and evidence edges;
- directory verification has an owner, renewal date, and removal process;
- ranking logic is disclosed at an appropriate level;
- conflicts of interest are recorded for authors and reviewers; and
- accessibility and reduced-motion behavior apply to any scrolling partner rail.

## Prototype assessment

The attached `owf-concept-001-v4_2.html` is a strong direction prototype. Its best decisions are:

- black, blue, white, and structural gold create a distinct concept-product identity;
- blue bands make the long page scannable;
- motion has an instructional purpose on dark surfaces;
- the jar interaction teaches underdose, overdose, restabilization, and floc shear;
- the correction layer is more valuable than a simple definition page;
- the graph section demonstrates the intended reciprocal connections; and
- the commercial rail includes an explicit editorial firewall.

It is not ready to publish. Material blockers include:

- the file name says v4.2 while the footer and correction history report v3.0;
- "verified 25 July 2026" and exact evidence-tier totals have not been backed by a stored review
  record;
- slider thresholds such as 88 and 78 are interface trigger values but visually resemble plant
  operating limits;
- simulated zeta potential, particle size, and turbidity values need to be labeled as illustrative
  or derived from a documented model;
- several technical claims require claim-level locators and practitioner review;
- one cited practice source is commercial and must not support a standard-tier claim;
- the unnamed Aktas reference is not reproducible as written;
- all three timers use one generic countdown pattern even though actual jar-test procedures are
  source-, objective-, and facility-dependent;
- the canvas needs a meaningful non-canvas alternative and a reduced-motion state;
- the auto-scrolling partner rail needs pause, keyboard, focus, and reduced-motion behavior;
- reveal animations can leave content initially hidden when JavaScript fails;
- the adjacent brief links are placeholders;
- links point to category pages rather than stable term, module, claim, and organization identifiers;
  and
- no browser, phone, keyboard, screen-reader, contrast, practitioner, learner, or factual review has
  been recorded.

## Required authoring package

Before a pilot brief is implemented in OWOS, define a versioned `owos-concept-brief/2` contract. It
should keep these records separately reviewable:

- brief identity, audience, status, owner, and version;
- concept promise and use cases;
- storyboard and selected teaching moves;
- narrative blocks;
- visual and interaction manifests;
- claims and source locators;
- corrections and contested positions;
- glossary and reciprocal graph edges;
- role applications and course connections;
- contributor, reviewer, sponsor, and conflict records;
- accessibility, mobile, and reduced-motion treatments;
- quality report and release approvals; and
- compiled delivery checksum.

The course compiler contract must not be silently extended or reinterpreted. Concept Briefs may share
governed components with courses, but they need their own explicit schema and release gate.

## Pilot recommendation

Use **Coagulation vs Flocculation** as the first design and governance pilot, not as a production
benchmark for every future brief.

Before implementation:

1. approve this initiative boundary and the public/internal naming;
2. complete claim-level source verification and water-practitioner review;
3. approve the first brief storyboard;
4. define the concept-brief schema, editorial states, and graph edge ownership;
5. distinguish illustrative simulation controls from operational values;
6. define the directory and sponsorship policy with conflict controls;
7. render and test desktop, tablet, phone, keyboard, screen reader, reduced motion, and no-JavaScript
   behavior; and
8. obtain explicit publication approval.

After the first three briefs, run a concept-portfolio distinctiveness review before scaling.

## Approval record

Hardeep approved the recommendations and authorized implementation on 2026-07-25:

- **Product boundary**: Concept Briefs are a governed layer between Dictionary and Courses.
- **Naming**: Concept Briefs publicly, Concept Engine internally.
- **Pilot**: Coagulation vs Flocculation is the first pilot.
- **Commercial boundary**: verified relevance, attributed contribution, and private tenant briefs,
  with a strict editorial firewall.
- **Visual direction**: Graphite is the standard OWOS identity for new public knowledge and learning
  products. It does not make the Coagulation vs Flocculation page structure a universal template.

The approval covers the versioned contract, compiler, skill, working pilot package, Graph and
Community connection contracts, commercial-integrity controls, and fail-closed QA.

No publication, credential claim, sponsor placement, technical-accuracy approval, Community
release, or Graph publication is approved by this implementation decision.
