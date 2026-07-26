# OWOS Concept Brief Operating Model

Status: approved product direction, implementation in progress  
Public product name: Concept Briefs  
Internal system name: Concept Engine  
Contract: `owos-concept-brief/2`

## Placement decision

Concept Briefs live inside the same OWOS Learn destination as Master Classes. They are a distinct
content type, not a second learning site and not a Master Class module disguised as a short page.

The public progression is:

```text
Dictionary
-> Concept Brief
-> Master Class or exact course module
-> Work product or private facility procedure
```

- Dictionary answers: What does this term mean?
- Concept Brief answers: How does it work, what can fail, and what should I investigate?
- Master Class answers: Can I learn and demonstrate this capability?
- Work answers: What governed output should I create for my organization?

OWOS Learn provides one search, one topic taxonomy, one saved-items model, one identity, one Graph
entry, and one Community system. The interface exposes content-type filters such as `Concept Brief`,
`Master Class`, `Course`, and `Practice`. Concept Briefs receive their own card treatment and detail
experience without becoming a competing destination in global navigation.

## Complete lifecycle

The Concept Engine preserves the complete path from an initial idea to a controlled release.

| Stage | What happens | Durable record | Gate |
|---:|---|---|---|
| 1 | Spar over the supplied diagram, article, brief, HTML, procedure, or idea. Preserve what is valuable and identify what feels forced, unsafe, incomplete, or commercially useful. | `intake.yaml`, preserved originals, conversation record | Source ownership and visibility known |
| 2 | Define the learner job, audience, product boundary, and public/private use. | `brief.yaml`, `design-brief.md` | Product boundary approved |
| 3 | Extract every material factual, regulatory, technical, quantitative, operational, commercial, and unresolved statement. | `claims.yaml` | Claim inventory complete |
| 4 | Design the research plan and disclosure boundary. | `research-plan.yaml` | External disclosure approved |
| 5 | Use Perplexity Deep Research for candidate-source discovery when approved. Preserve raw receipts and cost. | `research/perplexity/`, candidate-evidence report | Research jobs complete |
| 6 | Retrieve and inspect the original federal regulation, EPA guidance, AWWA reference, paper, dataset, or controlled source. Perplexity wording is never the authority. | `sources.yaml`, exact locators | Original-source trace complete |
| 7 | Run reverse QA/QC with an independent model or reviewer. Challenge every claim, number, equation, inference, and transfer assumption. | claim-review register and technical verdict | Every claim has a disposition |
| 8 | Accept, narrow, relabel, convert to a question, withhold, or reject each claim. Preserve correction history. | `claims.yaml`, correction report | No unsupported claim enters public narrative |
| 9 | Produce the evidence-backed narrative and a deliberately unique storyboard. | `narrative.yaml`, `storyboard.yaml` | Evidence boundary, design, and storyboard approved |
| 10 | Build the learning experience, visuals, interaction, reduced-motion state, and no-JavaScript equivalent. | visual manifest, `interactions.yaml`, compiled preview | Visual and interaction truth pass |
| 11 | Compile cited HTML from governed structured sources. HTML is delivery output, not the authoring source. | `dist/*.html`, build checksum | Deterministic build passes |
| 12 | Run content, source-host, browser, accessibility, responsive, keyboard, touch, qualitative-model, and learner-economy QA. Confirm fast orientation, four-or-fewer primary controls, a three-part close, one end-of-brief comment entry, no inactive vendor filler, and no public governance clutter. Score the result without allowing the score to override a blocked gate. | `qa.yaml`, QA/QC report, rendered evidence | Automated and required human reviews pass |
| 13 | Declare Dictionary, course, question, role, competency, source, and work-product relationships. Remove any edge whose supporting claim was rejected. | `graph.yaml` | Graph review and publication approval |
| 14 | Create or attach the Community space, seed questions, verified-answer policy, privacy warning, moderation owner, and correction escalation. | `community.yaml` | Community, moderation, and accessibility review |
| 15 | Attach APAS house messaging, vendor placement, directory identity, disclosure, controls, and aggregate reporting through the commercial control plane. Commercial records never edit evidence. | `commercial.yaml`, platform campaign registry | Commercial firewall, legal, and conflict review |
| 16 | Approve and publish the exact version, then monitor freshness, corrections, community proposals, and replacement releases. | `approvals.yaml`, release manifest, runtime catalog entry | Owner release and all hard gates pass |

## Reverse QA/QC rule

The second model or reviewer receives the complete claim list, not only the prose that survived the
first draft. Its job is to find:

- unsupported precision;
- incorrect equations or unit treatment;
- regulation versus guidance confusion;
- study results transferred beyond their experimental scope;
- operational diagnoses made from one indicator;
- claims that should be questions;
- statements that are product positions rather than external facts; and
- claims that are true in a narrow context but unsafe as public shorthand.

The return is recorded claim by claim as `accept`, `accept_with_revision`, `convert_to_question`,
`withhold`, or `reject`. A score summarizes the public content. It does not certify engineering,
operations, safety, health, or regulatory compliance.

## Three control planes

### 1. Content control plane

This is the Concept Brief administrator and Author Studio. It edits structured source records, never
compiled HTML directly.

Required controls:

- create a brief from a diagram, concept, article, brief, procedure, or existing page;
- edit narrative, storyboard, visuals, interaction, claims, sources, Graph, Community, and release
  metadata separately;
- view source locators and claim status beside the affected public block;
- rerun research or reverse QA/QC for selected claims;
- preview desktop, tablet, phone, reduced motion, and no JavaScript;
- compare versions and correction impact;
- save draft, research, review, approved, released, superseded, and archived states;
- compile and publish only after the applicable gates pass; and
- roll back the runtime catalog to a prior released artifact without deleting history.

### 2. Connection control plane

This connects a released Concept Brief to the existing OWOS services:

- OWOS Learn catalog and content-type filters;
- Dictionary terms;
- exact Master Class modules and learning pathways;
- Graph nodes and reviewed edges;
- Community space, threads, moderation, and correction proposals;
- saved items, assignments, competency relationships, and work products; and
- analytics events with the brief ID and released version.

For each brief, the connection control plane also reports total views, recent unique viewers,
engaged reads, completion reaches, comments, reviewed comments, consented appreciation, and featured
testimonials. A positive Community comment becomes a public testimonial only through explicit
learner consent and separate moderator approval. Removing it from public display preserves the
governed discussion and moderation record.

### 3. Commercial control plane

This controls APAS and vendor visibility without rebuilding or editing the Concept Brief.

Required controls:

- upload, replace, pause, resume, or remove a logo;
- edit organization, disclosure, copy, link, call to action, start date, and end date;
- target a placement to a Concept Brief ID and slot;
- connect a vendor to its neutral directory profile;
- assign the vendor account that may see aggregate reporting;
- report impressions, clicks, and contact starts;
- record conflicts and editorial-independence attestation; and
- archive a placement while retaining the audit record.

No commercial user can edit claims, sources, corrections, reviewer records, Graph evidence order,
related-learning order, or Community verification status.

## Publication transaction

A production publication is one controlled transaction:

1. validate the governed package;
2. compile and checksum the exact HTML;
3. save the released version and manifest;
4. copy or serve the immutable artifact at the stable Concept Brief route;
5. add or update the OWOS Learn catalog record;
6. ingest only approved Graph nodes and edges;
7. create or attach the Community context;
8. activate approved commercial placements by brief ID;
9. purge the affected runtime caches; and
10. verify the public route, links, drawers, events, and rollback pointer.

If any step fails, the previous released version remains live.

## Current pilot status

For `owos:concept-brief:001`:

- the federal-only current educational edition is compiled and browser-tested locally;
- the reusable compiler enforces the learner-economy contract rather than relying on page cleanup;
- OWOS Learn catalog placement and content-type filtering are implemented in the platform worktree;
- Author Studio, immutable version bundles, feedback review, rollback, Graph projection, Community
  context, and commercial controls are implemented and locally tested;
- the public brief uses a compact feedback entry while the complete Community interface remains in
  its drawer or dedicated route;
- inactive vendor placeholders are hidden; APAS house messaging remains controlled and disclosed;
- Graph, Community, and commercial connections remain separately governed from claim evidence;
- the current educational edition is not an independently verified technical release; and
- independent verifier and qualified practitioner approval remain the binding gates for that
  stronger release state.

The platform repository is a runtime consumer. This learning repository remains the authoritative
source for the package, compiler contract, templates, QA evidence, and compiled artifact.
