---
contract: owos-qaqc-certificate/1
document_id: owos:concept-brief:003
document_title: Detention, Retention, and Infiltration
document_version: b.3.0
artifact_checksum_sha256: 14681e4c439237011451f9d0f257e73e28d476111e3068ae5f2a18b197250864
source_checksum_sha256: 6892875718303d2205c78c18f1c2497f86c4561ad4c1b47531cc58207e909d42
published_url: https://claude.ai/code/artifact/6b5d2166-828d-4d4d-b94e-aead2b987d03
certificate_version: 2
reviewer: Claude (Opus 5), under owner direction
date: 2026-07-27
supersedes: b.2.1, retained at qa-qc/QA-QC-b.2.1.md
publication_state: review_only_archived_citation_blocker_cleared
---

# Quality Control Certificate

## 1. Identification

| Field | Value |
| --- | --- |
| Document | Detention, Retention, and Infiltration |
| Identifier | `owos:concept-brief:003` |
| Version | b.3.0 |
| Governing evidence | `white-paper.md` 0.8, `research/added-terminology-source-dossier.md`, `research/ii-authority-verification.md` |
| Contract | `owos-concept-brief/2` version 2.3.0 |
| Publication state | Review only. Not released. |

## 2. Graphics

Test applied to every graphic: does it stay true with its caption removed, does it contradict the
white paper or dossier, is every physical relationship it draws consistent with the governing
mechanism rather than merely plausible in shape, does it show any quantity mistakable for a design
value, and does it say what it does not prove.

| # | Graphic | Caption-free | Contradiction | Physics | Design values | Non-claim | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Detention: wide inlet, narrow outlet | Pass | **Defect, corrected** | Pass | None | Pass | Corrected |
| 2 | Retention: one word, two pictures | Pass | Pass | Pass | None | Pass | Pass |
| 3 | Infiltration: doorway with four exits | Pass | **Defect, corrected** | Pass | None | Pass | Corrected |
| 4 | Permanent pool: capacity above the water | Pass | **Defect, corrected** | Pass | None | Pass | Corrected |
| 5 | Outlet and overflow at two heights | Pass | **Defect, corrected** | Pass | None | Pass | Corrected |
| 6 | Tailwater: same outlet, two creeks | Pass | Pass | Pass | None | Pass | Pass |
| 7 | Route cross-section, four states | Pass | **Defect, corrected** | Pass | None | Pass | Corrected |
| 8 | Paired hydrograph with shaded volume | Pass | Pass | **Defect, corrected** | None | Pass | Corrected |

Accessibility: all eight carry `role="img"` with `aria-labelledby` resolving to a title and a
description. All render with JavaScript disabled. Graphics 7 and 8 are learner-driven; both have
static reachable states and neither depends on motion to be understood. Reduced motion removes the
hydrograph animation and renders the final state directly.

Individual findings are in `GRAPHICS-QA.md`. Summary of the two material ones is in section 3 and
section 8.

## 3. Analysis and physics

| Element | Governing relationship | Check | Result |
| --- | --- | --- | --- |
| Paired hydrograph | Reservoir routing: storage rises while inflow exceeds outflow and falls once it does not, so peak outflow occurs where the curves cross on the inflow recession | Evaluated inflow at the outflow peak and compared | **Failed initially.** Outflow peaked at 0.460 while concurrent inflow was 0.081. Corrected: outflow peak 0.476 at t=0.40, inflow at t=0.40 is 0.476. Crossing satisfied to three decimals. |
| Hydrograph volume | Detention delays rather than removes, so outflow volume is close to inflow volume | Numeric integration of both curves over the plotted domain, 2000 intervals | Inflow area 0.1980, outflow area 0.1961. Volume reduction 1 percent. Consistent with detention as a delay device. |
| Hydrograph peak claim | Peak reduction and volume reduction are different quantities | Computed both and compared in the readout | Peak reduction 45 percent, volume reduction 1 percent. The 44 point gap is the teaching point and is stated. |
| Route diagram water levels | Storm storage occupies the space above the permanent pool; overflow activates when stage reaches the notch | Compared each state's water level against pool elevation and notch elevation in the drawing | Consistent. Blocked state level 167 against notch at 168. |
| Tailwater panels | A higher receiving level reduces the difference in level across the outlet and slows release | Compared creek surface elevation against outlet invert in both panels | Low creek surface below outlet gives free discharge; high creek surface above outlet submerges it. Correct in both. |
| Permanent pool proportions | Storm storage is provided above the permanent pool | Compared filled and unfilled bands against the caption | **Failed initially.** Storm storage was drawn filled while the caption called it empty space. Corrected to an unfilled band. |

No element presents a modelled result. Every curve is qualitative, unitless, and labelled as such.

## 4. Factual accuracy

| Claim area | Basis | State |
| --- | --- | --- |
| Detention delays rather than removes | EPA/600/R-04/121 | Verified against source text |
| Downstream peak coincidence | EPA/600/R-04/121, near-verbatim | Verified, with EPA's own counterweight included |
| Permanent pool and storage above it | EPA wet ponds guidance | Verified |
| What sets the normal water level | EPA wet ponds guidance, EPA's wording used | Verified. The state term "control elevation" is deliberately not adopted |
| Peak against volume against load | EPA Three Keys | Verified |
| Infiltration and inflow definitions | 40 CFR 35.2005(b)(20) and (21), verified independently against govinfo XML | Verified from regulation |
| Why response shape cannot separate them | EPA/600/R-07/111 and EPA/600/R-15/162A, live | Verified from EPA research reporting |
| Tailwater effect on outlet release | Source dossier item 7 | Verified, qualified stormwater review outstanding |

No numeric threshold, drawdown time, infiltration rate, separation distance, or removal percentage
appears anywhere in the document. This was checked by search, not by recollection.

## 5. Citations

| Source | Authority tier | Live URL | Used for |
| --- | --- | --- | --- |
| EPA/600/R-04/121 Stormwater BMP Design Guide Vol 1 | 3, federal technical reference | nepis.epa.gov, live | Peak coincidence, detention as delay |
| EPA NPDES BMP: Wet Ponds | 2, federal agency guidance | www.epa.gov, live | Permanent pool, normal water level |
| EPA Three Keys to BMP Performance | 2, federal agency guidance | www.epa.gov, live | Peak, volume, concentration, load |
| USGS runoff and streamflow science | 3, federal technical reference | www.usgs.gov, live | Runoff generation, hydrograph shape |
| 40 CFR 35.2005(b)(20), (21), (29) Definitions | **1, federal regulation** | govinfo.gov CFR 2025 annual edition, live | What infiltration and inflow are, that each is distinct from the other, and that chronic operational problems include surcharging, backups, bypasses, and overflows |
| EPA/600/R-07/111 Computer Tools for Sanitary Sewer Capacity Analysis | 3, federal technical reference | nepis.epa.gov, live | A system may experience a fast infiltration response, a slow one, or both |
| EPA/600/R-15/162A SWMM Reference Manual Vol I | 3, federal technical reference | nepis.epa.gov, live | Rainfall-derived inflow and infiltration is estimated as one aggregate from flow records |

**Archived-citation blocker: CLEARED.** The previous certificate at b.2.1 recorded a publication
blocker because the I&I material rested on EPA's frozen January 2017 web archive. That source is now
dropped entirely. The definitions come from current regulation, which is a higher tier than the
guidance it replaced, and the reason response shape cannot separate the two comes from live EPA
Office of Research and Development reporting. No citation in this document now relies on an archived
URL. Verification recorded in `research/ii-authority-verification.md`.

**A prediction I made was wrong, and it is recorded here rather than quietly corrected.** Before the
search I expected 40 CFR 35.2005 to define a combined "Infiltration/Inflow" term as the total
"without distinguishing the source", which would have supported the claim as originally written. The
regulation says the opposite: infiltration "does not include, and is distinguished from, inflow", and
inflow likewise. The claim as written was definitionally wrong and has been rewritten. I confirmed
this directly against the govinfo XML rather than accepting the search result.

## 6. Editorial and instructional

- Orientation renders before any mechanism: subject, audience, prior knowledge, why it matters,
  objectives, time, scope boundary. Present.
- Define before use: all six dependent terms defined with plain meaning, concrete example, and an
  explicit statement of what the term does not establish, ahead of first use in any graphic. Present.
- Scope boundary stated in the orientation and repeated in section 5 of the page. Present.
- Prohibited phrases: zero occurrences.
- Em dashes and en dashes: zero occurrences.
- Variant and internal governance language in learner-facing copy: zero occurrences.
- Reading and participation estimate shown persistently in the rail. Present.

## 7. Rendered quality

`node tools/audit-concept-brief-rendering.cjs artifact.html`

| Viewport | Content inset | Contrast | Gutter | Layout | Tap | H-overflow |
| --- | --- | --- | --- | --- | --- | --- |
| desktop 1440 | 180px | 0 | 0 | 0 | 0 | 0px |
| tablet 820 | 32px | 0 | 0 | 0 | 0 | 0px |
| phone 390 | 16px | 0 | 0 | 0 | 0 | 0px |

Manual and scripted:

- Keyboard: all controls reachable, flip cards operate on Enter and Space, drawers trap focus, Escape
  closes, focus returns to the trigger. Pass.
- History: browser Back closes an open drawer. Pass.
- Reduced motion: hydrograph renders final state directly, flip transition removed, typewriter
  resolves instantly. Pass.
- No JavaScript: 19,058 characters of readable content, all six definition graphics present. Pass.
- External requests: zero. Fully self-contained. Pass.
- Console errors across a full interaction pass: zero. Pass.

## 8. Defects found and disposition

Eleven defects found across this pass. All corrected and re-verified.

| # | Defect | Severity | Disposition | Re-verified by |
| --- | --- | --- | --- | --- |
| 1 | Hydrograph outflow peaked above concurrent inflow, violating reservoir routing | **Material, taught something false** | Curves recomputed to satisfy the crossing; volume held | Numeric evaluation, crossing equal to three decimals |
| 2 | Permanent pool graphic filled the storm storage its caption calls empty | **Material, drew the misconception** | Band redrawn unfilled | Visual re-inspection |
| 3 | Route diagram showed a red outlet between storms, reading as blocked | Correctness | `blocked` separated from `flowing` | Scripted state assertion |
| 4 | Detention graphic drew a dry basin full with no time state | Correctness | Time state labelled | Visual re-inspection |
| 5 | Infiltration plant route had no return to air | Completeness | Evapotranspiration return added | Visual re-inspection |
| 6 | Overflow arrow began beside the riser, not at the notch | Clarity | Path re-anchored | Visual re-inspection |
| 7 | Flip card inner element computed `display:inline`, collapsing the card to zero height | **Material, component destroyed** | Rebuilt as a grid stack | Rendered audit layout check, both directions |
| 8 | Brand mark broken across three lines by an orphaned first-version rule setting `display:block` on every span inside it | Presentation | Dead rule removed | Computed style assertion |
| 9 | Brand accent failed contrast at 2.6:1 on ivory | Accessibility | Darkened to 5.34:1 | Rendered audit |
| 10 | Two hydrograph labels collided at the crossing point | Clarity | One label repositioned below | Visual re-inspection |
| 11 | Variant and evidence scaffolding present in learner-facing copy and title | Editorial | Removed | Search, zero occurrences |
| 12 | I&I passage rested on an archived EPA regional document, and its central sentence was contradicted by current regulation | **Material, publication blocker and a factual error** | Archive dropped; definitions moved to 40 CFR 35.2005; the reason shape fails moved to live EPA research reporting; passage rewritten in both the white paper and the page | Regulation text confirmed directly against govinfo XML by the author, not accepted from the search agent |

What was examined to reach this: all eight graphics individually against the white paper and dossier;
every quantitative relationship recomputed rather than eyeballed; the full page at three viewports
through the automated audit; a scripted interaction pass over four route states, the hydrograph, six
flip cards, four work questions, both drawers, and the export; keyboard and reduced-motion paths; and
a JavaScript-disabled render.

## 9. Open items and limitations

1. **Resolved.** The I&I citation blocker is cleared. See section 5.
2. **New conflict for a qualified reviewer.** EPA technical references place foundation drains under
   inflow. The regulation's own parenthetical places them under infiltration. This is a real
   inconsistency in the federal record, not an editorial choice, and a qualified collection-system
   reviewer must resolve it. The page currently follows EPA technical practice.
3. Independent source verification is not complete for the remaining claims.
4. Qualified stormwater, wastewater, and permitting practitioner review is not complete.
5. Community, Graph, and sponsorship routes are inert in the published preview and resolve inside the
   OWOS platform.
6. Learning events are emitted but no recorder is attached in the published build, so nothing is
   recorded.

**A reader must not conclude from this document** that any real asset is adequate, compliant,
suitable for infiltration, or protective against flooding, or that any quantity shown is a design
value.

## 10. Correction and version history

| Version | Date | Change | Trigger | Certificate |
| --- | --- | --- | --- | --- |
| b.1.0 | 2026-07-27 | First build of the alternative curriculum reading | Owner request for a second variant | none |
| b.1.1 | 2026-07-27 | Flip cards rebuilt as a grid stack | Owner reported flip cards not working | none |
| b.2.0 | 2026-07-27 | Definition graphics, reading rail, cross-sector section, sources surface, connected learning, community and value plane | Owner review | none |
| b.2.1 | 2026-07-27 | Six graphics defects corrected, brand plane rebuilt, Graph and Community drawers wired, learning events instrumented, Droobi attribution removed | Owner review and graphics QA/QC | `qa-qc/QA-QC-b.2.1.md` |
| **b.3.0** | **2026-07-27** | **I&I passage rewritten on 40 CFR 35.2005 and live EPA research reporting; archived source dropped; a factual error in the previous version corrected** | **Owner required a defensible regulatory basis; verification found the previous claim was definitionally wrong** | **this certificate** |

Certificates from b.2.1 forward are retained under `qa-qc/`. Versions before b.2.1 predate this
standard and have no certificate, which is recorded here rather than backfilled.
