---
contract: owos-qaqc-certificate/1
document_id: owos:concept-brief:001
document_title: Coagulation and Flocculation
document_version: rebuild.1.0
artifact_checksum_sha256: 5d8db1c58763ff19cd35dedddeb6308409325b1d37e7ebe451eb00e47366d107
source_checksum_sha256: 2498a43b133c6a04801b2ecc15ffc723c9f15ddea60bfee78075666ac9eda5d5
published_url: https://claude.ai/code/artifact/e989801b-9aff-42b5-a678-852c76e05005
certificate_version: 1
reviewer: Claude (Opus 5), under owner direction
date: 2026-07-27
supersedes: none. The pre-rebuild brief published without a certificate, which predates this standard.
publication_state: review_only_not_released
---

# Quality Control Certificate

## 1. Identification

| Field | Value |
| --- | --- |
| Document | Coagulation and Flocculation |
| Identifier | `owos:concept-brief:001` |
| Version | rebuild.1.0 |
| Governing evidence | `white-paper.md` rebuild-0.4 (scored 90), `research/source-verification-2026.md` |
| Contract | `owos-concept-brief/2` version 2.3.0 |
| Publication state | Review only. Not released. |

## 2. Graphics

Test applied to every graphic: does it stay true with its caption removed, does it contradict the
white paper or the verification record, is every relationship it draws consistent with the governing
mechanism rather than merely plausible, does it show any quantity mistakable for a design value, and
does it say what it does not prove.

| # | Graphic | Caption-free | Contradiction | Mechanism | Design values | Non-claim | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Coagulation: repelling, destabilised, starting | Pass | Pass | Pass | None | Pass | Pass |
| 2 | Flocculation: small floc grown to settleable | Pass | Pass | Pass | None | Pass | Pass |
| 3 | Mixing intensity stepping down through the train | Pass | Pass | Pass | None | Pass | Pass |
| 4 | Pin floc suspended against floc settling | Pass | Pass | Pass | None | Pass | Pass |
| 5 | What the jar contains and what the basin also has | Pass | Pass | Pass | None | Pass | Pass |
| 6 | Dose window, learner driven | Pass | Pass | Pass | None, axes deliberately unlabelled | Pass | Pass |
| 7 | Three causes converging on one appearance, learner driven | Pass | Pass | Pass | None | Pass | Pass |

One defect found and corrected during the pass: two labels in graphic 1 collided at the panel
boundary. Repositioned and re-inspected.

Accessibility: all seven carry `role="img"` with `aria-labelledby` resolving to a title and a
description, verified by assertion. Graphics 6 and 7 are learner driven; both have static reachable
states and neither depends on motion. All render with JavaScript disabled.

**Deliberate absence.** No graphic carries a numeric axis, a dose, a mixing intensity, a time, or a
turbidity figure. Graphic 3 shows intensity falling with no values, and graphic 6 shows a window with
unlabelled axes. This is a decision recorded in section 9, not an omission.

## 3. Analysis and physics

| Element | Governing relationship | Check | Result |
| --- | --- | --- | --- |
| Dose window curve | Performance falls on both sides of an effective condition. Below it particles remain stable; above it, in the charge neutralisation regime, restabilisation occurs | Curve is a single-peaked function failing symmetrically on both sides, with the two failure zones labelled by cause rather than by value | Correct. The shape is the teaching point and carries no units. |
| Dose marker positions | Four states must sit at qualitatively distinct points: below, in, past, and well past | Marker computed from the same function that draws the curve, so it cannot drift off it | Correct by construction. |
| Mixing intensity profile | EPA directs that velocity gradient must fall from the last flocculation stage onward so formed floc is not broken | Profile steps down monotonically through rapid mix, flocculation stages, and onward to sedimentation. No step rises | Correct and consistent with the retrieved EPA direction. |
| Pin floc convergence | Three distinct causes produce one indistinguishable appearance, and two worsen with added coagulant | Each path terminates at the same node; the verdict field is driven per cause and reads WOULD HELP, WOULD NOT HELP, WOULD MAKE IT WORSE | Correct. Verified by assertion that the excessive-dose state returns WOULD MAKE IT WORSE. |
| Coagulation panel sequence | Repulsion, then destabilisation, then initial aggregation, in that order | Panels ordered and labelled; particles drawn apart, then apart without repulsion marks, then joined | Correct. |

No element presents a modelled or measured result. Every graphic is qualitative and unitless.

## 4. Factual accuracy

| Claim area | Basis | State |
| --- | --- | --- |
| Definitions of coagulation and flocculation | 40 CFR 141.2, retrieved from eCFR and quoted verbatim by the author | Verified from regulation, tier 1 |
| Pin floc as a documented consequence of excessive dosing | EPA 815-R-20-004 p.101, PDF retrieved and text extracted by the author, passage read in context | Verified |
| Optimal coagulant dosage is critical to filter performance | EPA 815-R-20-004 §4.3.1 | Verified, quoted |
| Inadequate mixing or addition at the wrong point limits performance | EPA 815-R-20-004 §4.3.1 | Verified, quoted |
| Velocity gradient must fall from the last flocculation stage onward | EPA 815-R-20-004, flocculation evaluation questions | Verified, quoted |
| Short circuiting as a basin failure mode | EPA 815-R-20-004, flocculation basin evaluation | Verified |
| Filtered water turbidity is a regulated performance measure | 40 CFR 141.173 and 141.551 | Verified as existing. **No figure is reproduced in this brief.** |
| Restabilisation at high dose, alkalinity consumption, sludge production | Mechanism stated at the level the package claim set supports | Not independently verified. Standard practice knowledge. |
| Coagulation and flocculation timescales | **Not verified. Source unreadable.** | **Excluded from the brief entirely.** See section 9. |

No dose, mixing intensity, mixing time, velocity gradient value, or turbidity figure appears anywhere
in the document. Confirmed by search, not by recollection.

## 5. Citations

| Source | Authority tier | Live URL | Used for |
| --- | --- | --- | --- |
| 40 CFR 141.2, Definitions | **1, federal regulation** | ecfr.gov, live, current as of 2026-07-23 | Both central definitions |
| EPA 815-R-20-004 Turbidity Provisions guidance | 2, federal agency guidance | www.epa.gov, live | Pin floc case, dosage and filter performance, mixing adequacy, velocity gradient direction, short circuiting |
| 40 CFR 141.173, 40 CFR 141.551 | **1, federal regulation** | ecfr.gov, live | That filtered water turbidity is regulated |

**No archived URL is relied on anywhere in this document.** The verification pass confirmed that no
source in this package depends on a web archive, which is the failure that blocked the companion
brief.

**Sources removed from the evidence basis during this rebuild**, recorded because their removal is
part of the quality claim: one non-United States paper whose locator returns 404 and which was never
retrieved; the brief's own pre-research prototype, which was cited by 23 claims and cannot be
evidence for anything; and an AWWA conference paper reclassified from technical standard to
professional context.

## 6. Editorial and instructional

- Orientation renders before any mechanism: subject, audience, prior knowledge, why it matters,
  objectives, time, scope boundary. Present.
- Define before use: five dependent terms, each with plain meaning, a concrete picture, an explicit
  statement of what the term does not establish, and its own graphic, all ahead of first use.
- Two definitions quote federal regulation directly rather than paraphrasing it.
- Scope boundary stated in the orientation and repeated in the sources section.
- Prohibited phrases: zero. Em dashes and en dashes: zero.
- Reading and participation estimate shown persistently in the rail.
- Three worked examples exist in the white paper. The page carries the reasoning as a four-question
  work product that can be watched rather than typed.

## 7. Rendered quality

`node tools/audit-concept-brief-rendering.cjs artifact.html`

| Viewport | Content inset | Contrast | Gutter | Layout | Tap | H-overflow |
| --- | --- | --- | --- | --- | --- | --- |
| desktop 1440 | 180px | 0 | 0 | 0 | 0 | 0px |
| tablet 820 | 32px | 0 | 0 | 0 | 0 | 0px |
| phone 390 | 16px | 0 | 0 | 0 | 0 | 0px |

Scripted interaction pass: five definition figures, six flip cards, four work questions, four dose
states, three pin floc causes, both drawers, keyboard flip and Escape close, and the Markdown export.
Zero console errors. Fifteen learning events emitted across the pass. Readable with JavaScript
disabled at 13,453 characters. Zero external requests.

Clean on the first audit run, which is attributable to reusing the shell proven on Concept Brief 003
rather than to this page being checked less.

## 8. Defects found and disposition

| # | Defect | Severity | Disposition | Re-verified by |
| --- | --- | --- | --- | --- |
| 1 | Two labels collided at a panel boundary in the coagulation graphic | Presentation | Repositioned | Visual re-inspection |

**What was examined to reach a single defect.** All seven graphics individually against the white
paper and the verification record. Every relationship each graphic draws, checked against the
governing mechanism rather than against whether it looked plausible. The dose curve and its marker,
confirmed to be driven by one function so the marker cannot drift off the curve. The pin floc verdict
field, asserted per cause. The full page at three viewports through the automated audit, including
the contrast, gutter, layout-integrity, overflow, and touch-target checks. A scripted pass over every
interactive control and the export. Keyboard and reduced-motion paths. A JavaScript-disabled render.
A search for any numeric operating value, which returned none.

Two defect classes were absent by construction rather than by luck: the page reuses a shell whose
contrast, layout, and touch-target defects were found and fixed on Concept Brief 003, and it carries
no numbers, so the entire class of quantitative errors has no surface here.

**Defects found in the underlying package during this rebuild, and corrected before this page was
built**, are the substantive quality finding and are recorded in the white paper and the verification
file: a claim teaching pin floc as an intended intermediate when current EPA guidance uses it as an
overdose signature; a dead non-United States source; a material claim resting solely on non-United
States bench research; a professional-context source classified as a technical standard; and the
brief's own prototype cited as evidence by 23 claims.

## 9. Open items and limitations

1. **Independent claim verification is not complete.** No claim carries an independent verifier.
2. **Qualified drinking water treatment practitioner review is not complete.** This is the gate that
   matters most for a process brief and it cannot be closed here.
3. **Timescale figures are deliberately excluded, permanently.** The federal guidance stating them is
   a scanned PDF with no text layer whose text endpoint returns a viewer shell. It could not be read.
   The brief teaches the contrast between vigorous brief mixing and gentle sustained mixing through
   EPA's velocity gradient direction, which was read directly. This is a standing decision, not an
   outstanding item.
4. **Regulatory turbidity figures are deliberately excluded.** The regulation is cited as establishing
   that filtered water turbidity is regulated. No number is reproduced, because a number a reader
   could act on belongs quoted at its citation with its covered systems stated.
5. The rapid mix energy disagreement in the literature is carried as a contested area rather than
   resolved by the author.
6. Community, Graph, and sponsorship routes are inert in the published preview.
7. Learning events are emitted but no recorder is attached in the published build.

**A reader must not conclude from this document** that any dose, mixing intensity, mixing time, or
chemical change is warranted at any plant, or that any observation described here diagnoses a real
process.

## 10. Correction and version history

| Version | Date | Change | Trigger | Certificate |
| --- | --- | --- | --- | --- |
| pre-rebuild | before 2026-07-27 | Original brief, comparison framing | Original build | none, predates this standard |
| rebuild-0.1 | 2026-07-27 | White paper rebuilt on a one-idea spine. Scored 71 and returned to sparring | Owner directed a rebuild rather than a revision | none |
| rebuild-0.2 | 2026-07-27 | Thesis corrected against 40 CFR 141.2. Pin floc claim reversed against verified EPA text. Scored 76 | Source verification returned errors including one in the author's own draft | none |
| rebuild-0.3 | 2026-07-27 | All nine package edits applied. Scored 86 | Verification findings actioned | none |
| rebuild-0.4 | 2026-07-27 | Three worked examples written out, cross-sector and finance sections built out. Scored 90 and eligible | Owner approved the corrected thesis | none |
| **rebuild.1.0** | **2026-07-27** | **Page built: orientation, five defined terms each with a graphic, two learner-driven interactives, six flip cards, watchable four-question work product, cross-sector, sources, connected learning, community and value plane** | **Owner directed the build** | **this certificate** |
