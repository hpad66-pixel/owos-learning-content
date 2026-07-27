---
variant: B
title: Detention, Retention, and Infiltration
subtitle: The pond is not the answer. The route is.
author: Claude (original curriculum interpretation)
status: selected_design_variant_a_retired
html_authorized: review_only
evidence_basis: white-paper.md 0.7 and research/added-terminology-source-dossier.md
date: 2026-07-27
---

# Variant B curriculum rationale

**Owner decision, 2026-07-27: Variant B is the selected design. Variant A is retired.**

The Variant A rendered experience has been removed from `dist/`. Its evidence base is deliberately
kept, because Variant B is built on it and none of it was the problem: `white-paper.md` 0.7, the
claim and source records, the verification dossier, the added-terminology source dossier, and the
Florida research companion all remain the governing evidence. The full Variant A build stays
recoverable at git tag `concept-brief-003-version-a`.

What was rejected was the instructional argument, not the research.

## What I changed and why

### A concept brief should have one reorganizing idea, not twenty sections

Variant A is a survey. Twenty white-paper sections became thirteen beats covering storms, storage,
subsurface routing, hydrographs, performance measures, maintenance, wastewater I&I, permits,
finance, and cross-role conversation. Everything in it is true and most of it is well written. But a
learner finishing it can recite a lot and has not necessarily been *changed*.

A Concept Brief sits between a dictionary entry and a course. Its job is not coverage. Its job is to
install one idea so firmly that the learner cannot look at the subject the old way afterward.

The idea here is one sentence:

> A name tells you a category. Only the route tells you the behaviour.

Everything in Variant B either installs that idea or is cut. Permits, finance, and cross-role
framing are not deleted from the curriculum; they move to their own briefs, which is what the
connected-brief family is for. Trying to teach them here is what made Variant A long.

### Teach through a problem, not through a taxonomy

Variant A opens with definitions and then walks the system. Variant B opens with a puzzle the
learner cannot solve yet: a pond in good condition, a clear outlet, an inspection that passed, and a
street that flooded anyway. Every concept afterward enters because the investigation needs it. The
learner is never told "here is the next topic." They are told "you still cannot explain the street."

That changes retention. A definition supplied on demand to resolve a live question is remembered.
The same definition supplied in advance is skimmed.

### Fix what the Variant A graphics do not do

Three concrete failures in the existing visual set, each addressed here:

1. **The route comparison draws a dry detention basin full of water**, identical to the wet pond
   beside it. The single distinction the graphic exists to teach is erased by its own artwork.
   Variant B shows the dry basin empty at rest and fills it under learner control, so dry and wet
   are visibly different states of a system rather than two blue rectangles.
2. **The hydrograph asserts that area represents volume and never shades the area.** The punchline,
   that a lower peak is not less water, is left in a caption. Variant B animates both curves and
   fills both areas, then reports the two areas so the learner watches a lower peak enclose the same
   quantity.
3. **The graphics stop teaching when you remove the labels.** Oversized arrowheads and an overflow
   arrow that points from nowhere to nowhere are decoration. Variant B's diagrams are driven by
   state: blocking an outlet visibly re-routes water to the overflow, and the learner causes it.

### Make the applied task watchable instead of typeable

The final work product in Variant A is twelve fields the learner must fill in. Most learners will
not finish it, and a brief that ends in an unfinished form has taught nothing at the moment it
mattered most.

Variant B keeps the same rigour and removes the labour. Each question can be answered three ways:

- **Watch it answered.** A model answer types itself in a monospace field at reading speed, so the
  learner sees the reasoning form rather than reading a finished block. Watching is a legitimate
  completion path.
- **Type your own.** The same field is editable at any time.
- **Clear and start fresh.** No penalty, no lost progress elsewhere.

Answers save to the browser and export as Markdown. Nothing is required to reach the end. Completion
comes from clarity, not from data entry.

## Design fingerprint

- **Learner job:** explain why a system behaved the way it did when the name and the inspection both
  said it should not have.
- **Opening pattern:** an unsolved field puzzle presented before any definition.
- **Narrative archetype:** investigation. Evidence accumulates, the first explanation fails, a better
  one survives.
- **Central mental model:** route over label.
- **Signature mechanism:** a learner-driven route diagram where changing one condition visibly moves
  the water somewhere else.
- **Dominant visual:** a single cross-section that persists through the whole brief and gains detail,
  rather than a new diagram per topic.
- **Interaction signature:** cause and consequence. The learner changes a condition and the system
  answers.
- **Closing action:** answer the investigation, by watching or by writing.
- **Deliberately avoided:** a glossary wall, a survey of practice types, a twelve-field form as the
  final gate, decorative arrows, and any graphic that needs its caption to mean anything.
- **Difference from Variant A:** A covers the domain. B changes how one thing is seen and hands the
  rest to the connected briefs.

## What was added after the first owner review

The first build carried the argument but under-served the terms it depends on, and it stopped at the
learning without connecting to anything.

- **A graphic per definition.** Six original diagrams, one for each dependent term, built as a
  consistent cross-section family. Each has to teach with its caption removed, which is the test the
  Variant A visuals failed. Detention is a wide inlet against a narrow outlet. Retention is one word
  drawn as two different pictures. Infiltration is a doorway with four exits below it. The permanent
  pool shows the working capacity as the empty space above the water. Outlet and overflow sit at two
  heights. Tailwater shows the same outlet against a low and a high creek.
- **A reading rail.** Sticky progress bar with the current stage and minutes remaining, so the time
  commitment is visible from the first screen rather than buried in the orientation.
- **The cross-sector connection.** The production contract requires one and the first build had
  none. Rain entering a separate sanitary sewer, carrying the correction that EPA cannot separate
  rainfall-induced infiltration from delayed inflow, so response shape narrows the question rather
  than answering it.
- **A sources and scope surface.** The evidence was traceable in the package and invisible on the
  page. Five federal sources with what each one supports, plus an explicit statement of what review
  is still open.
- **Connected learning.** Four briefs this one deliberately stops short of, which is how the
  one-idea discipline stays honest rather than becoming an excuse for thin coverage.
- **The community and value plane.** Practitioner conversation, a correction path that re-enters
  verification rather than living in a comment thread, the editorial-independence disclosure, APAS.ai
  and Droobi attribution, and the copyright position separating original work from federal material.

## Evidence position

No new technical claims. Every statement traces to `white-paper.md` 0.7 and
`research/added-terminology-source-dossier.md`, including the three corrections that search produced:
detention and residence time are two names for nearly the same quantity, "control elevation" is state
vocabulary and is not used here, and the wet-weather response separates direct from delayed rather
than inflow from infiltration.

Verification status is unchanged and pending. This variant is for instructional comparison and does
not advance any release gate.
