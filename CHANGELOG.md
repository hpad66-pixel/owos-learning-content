# Changelog

All notable changes to One Water OS are recorded here, newest first.
Dates are YYYY-MM-DD. Versions follow simple semantic-ish numbering.

## [0.31.0] - 2026-07-27
### Changed: Detention white paper 0.7, source anchoring and three corrections
- Completed a federal source search over the twelve terms quarantined in 0.6 and recorded it in
  `research/added-terminology-source-dossier.md` with retrieved URLs, quoted passages, scope limits,
  a rejected-source log, and a full retrieval log. Nine of twelve anchored to a federal source that
  was actually fetched and read. No citation was invented.
- The search returned three corrections rather than three confirmations, which is the quarantine
  working as designed:
  - detention time and residence time were assigned in the opposite direction from EPA's own
    glossary, which defines detention time as volume divided by discharge rate. Rewritten to present
    them as two names for nearly the same quantity, with the useful question preserved.
  - "control elevation" is state regulatory vocabulary, not federal. The mechanism is now taught in
    EPA's own words and the phrase is named only as a term learners will encounter elsewhere.
  - the wet-weather worked example separated inflow from infiltration. EPA states that
    rainfall-induced infiltration cannot be distinguished from delayed inflow. The example now
    separates direct from delayed response and names the delayed inflow sources, and its conclusion
    is narrowed from separating the two to narrowing the question.
- Downstream peak coincidence moved from expert interpretation to sourced fact on near-verbatim EPA
  language, and now carries EPA's own counterweight that selectively located basins can help.
- Scored 94, recovering one point from 0.6.

### Fixed
- Anchored the full-bleed pullquote to its own edge instead of to parent centring, which is why it
  drifted 2px past the viewport at desktop and tablet. Contained at 1440, 820, and 390.
- Taught the browser suite that content inside a horizontal scroll container is contained by design,
  matching the rendered audit so the two tools agree. Both now report zero.

## [0.30.0] - 2026-07-27
### Added: rendered-quality gate
- Added `tools/audit-concept-brief-rendering.cjs`, a Playwright audit that opens the compiled brief
  at desktop, tablet, and phone and fails on WCAG 2.1 contrast against the real composited
  background, text closer to the viewport edge than the page's own content inset, horizontal
  overflow, and touch targets under 24 pixels.
- Made it a contract gate. Structural validation cannot see the page, so a package could satisfy
  every schema rule and still compile to something unreadable.
- Moved the accessibility rules into `ACCESSIBILITY_FLOOR`, compiled after the package brand
  stylesheet and the shared shell, using literal colour values rather than theme variables. The
  reference package remaps `--blue` to a light cyan, which silently pulled the floor down with it.

### Fixed
- Matching checks were rendering blank. Packages author pairs as `left`/`right`; the renderer read
  `prompt`/`answer`, so every matching row emitted an empty statement and `data-answer=""`. The
  learner saw an unlabeled dropdown and the grader compared against an empty string. The renderer
  now accepts either spelling, and validation rejects a pair with no visible statement, no answer,
  or an answer that is not one of the declared targets.
- Repaired the band header and status bar gutters. Both carried colour and type but no content
  geometry, so their text ran to the viewport edge while every beat body sat inside the wrapper.
- Native form controls inherited the theme's dark `color-scheme`, putting dark dropdowns on light
  assessment cards. Controls now follow the surface they sit on.
- Headings and links inside cards inherit the card's colour instead of being forced to one surface,
  so the light and dark variants of the same component both stay legible.
- Raised the primary and commercial actions to solid fills, the consent checkbox to 24 pixels in the
  shared shell, and gave inline links in cards, tables, and citations a 24 pixel touch target.
- Both briefs now report zero contrast, gutter, overflow, and tap-target defects at all three widths.

## [0.29.0] - 2026-07-27
### Added: instructional orientation contract for the Concept Engine
- Raised the Concept Brief Production Contract to 2.2.0 with an instructional orientation contract.
  A brief may no longer open directly on its topic. Before the first mechanism, diagram, or
  interaction, the rendered page must answer what this is about, who it is for, why it matters,
  what the learner will be able to do, how long it takes, and what it does not cover.
- Added a define-before-use rule. Every dependent term is defined in plain English with a concrete
  example and an explicit statement of what the term does not establish, placed where the learner
  first needs it. An appended glossary does not satisfy the requirement, and a diagram may not
  introduce a label the prose has not already defined.
- Added a wholeness standard: a brief is complete when a learner who knew nothing about the topic
  can, without leaving the page, say what the concept is, explain how it works, recognize where it
  applies, name what commonly goes wrong, distinguish it from what it is confused with, and state
  what they would need to know before acting.
- Added `definition` and `example` narrative block types to the Concept Brief Compiler, with a
  four-part definition record and a four-part worked-example record.
- Rendered the learning objectives. `learning.yaml` had carried `outcomes`, `prior_knowledge`,
  `misconception`, and `cross_sector_connections` as required records that the compiler validated
  and then never rendered, so the learner never saw the promise the package made. The compiler now
  renders them in a START HERE orientation section.
- Added five fail-closed regression gates: missing orientation, no definition block, no worked
  example, definitions placed after first use, and the white-paper presence warning.
- Required the white paper and compiled brief to be the same argument at two depths. A teaching move
  in the paper with no home in the storyboard, or a rendered section with no basis in the paper, is
  now a reported synchronization defect.

### Fixed
- The production contract listed `white-paper.md` in the governed package while the compiler never
  checked for it, so a brief could reach compilation with no teaching source. The compiler now warns
  during working validation and blocks at release.
- A visual declared with `component_id` and no `locator` raised `KeyError` during build despite
  passing validation. Component-backed visuals now render with their reading guide, conclusion, and
  alternative text.
- Added stylesheet coverage for the `heading`, `metric`, `role`, `evidence`, and
  `connected_learning` block types, which had rendered unstyled.
- Visual captions can now carry a `not_established` statement, so a graphic states what it does not
  prove alongside what to notice.
- Repaired four contrast defects found in rendered review. The Graphite theme sets headings and body
  copy light and inverts the `off_white` beat band to charcoal, so components composed for a light
  surface were rendering light text on light panels. Three were pre-existing and shipped in the
  reference brief: every learning-check question was near-invisible on its light card, the beat
  learner question was dark blue on charcoal, and the concept-map drawer kicker was pale cyan on
  ivory. The rendered page now reports zero low-contrast text nodes.

### Changed: Detention, Retention, and Infiltration white paper 0.6
- Added the reader orientation, the situations where the concept becomes consequential, and a
  foundation definition set carrying plain meaning, concrete example, and non-establishment for
  every dependent term.
- Added four worked examples, the distinction between infiltration rate and infiltration capacity,
  hydraulic conductivity, detention and residence time, control elevation, littoral zone, freeboard,
  tailwater, time of concentration, first flush, event mean concentration, downstream peak
  coincidence, three further misconceptions, and six further production visuals.
- Scored 93 of 100, down from 95. The instructional expansion enlarged the set of statements needing
  source anchoring faster than the evidence grew. Twelve added terms are itemized, quarantined from
  learner-facing HTML, and blocked until they carry source records, classified claims, and qualified
  review.
- Reconciled the conversation tool count. Eleven questions plus a closing statement produce the
  twelve-field work product; the design brief had recorded both numbers as though they conflicted.

## [0.28.0] - 2026-07-22
### Added: governed Project Delivery release contract
- Added `apps/project-management/course.yaml` as the machine-readable authority for the 21-chapter,
  60-section Master Class.
- Added a checksum manifest covering the course landing and all 21 native OWOS lessons.
- Added a GitHub workflow that builds and verifies the manifest, preserves it as release evidence,
  and requests a reviewed intake pull request in `hpad66-pixel/onewater-os-platform`.
- Added the same release manifest contract to Data Before AI without replacing its controlled
  research-method provenance.
- Added `course.yaml` to the reusable course template so every future course starts with the same
  ownership, provenance, release, runtime, and assessment boundaries.

### Fixed
- Reconciled course availability at 21 of 21 chapters.
- Restored sequential next-chapter navigation from Chapter 02 through Chapter 20 in the curriculum
  source, then regenerated the affected runtime files.
- Replaced retired repository names in the course deployment instructions.

## [0.27.0] - 2026-07-19
### Added: PM Chapters 19, 20 and 21 (course complete)
- Released Chapter 19, "Program and portfolio management": project versus program versus portfolio,
  benefit realization, prioritization weighting, portfolio resource constraints, and OPM maturity.
- Released Chapter 20, the capstone: the Cypress Creek lift station run gate by gate, ending with a
  sort of which project work is the manager's own and which should be delegated to an agent.
- Released Chapter 21, PMP and CAPM exam preparation: the Examination Content Outline and its three
  domains, predictive versus adaptive framing, the formula sheet, test strategy, and a practice runner.
- Added reusable `program` component: benefit realization gated by the slowest component, so pulling
  the other projects earlier visibly buys nothing.
- Added reusable `examsim` component: a multi-question practice runner with running score and a
  readiness verdict.

### Fixed
- **Answer-order bias across the whole course.** An audit found the correct answer sat in the first
  position in 31 of 32 multiple-choice and practice questions, spanning 19 chapters, so a learner could
  pattern-match position instead of reasoning. Added a `shuffled()` helper and applied it in `mc`,
  `multi` and `examsim`, which fixes every chapter at once and prevents the bias in future authoring.
  Verified uniform distribution over 40,000 shuffles, no options dropped, and scoring still correct.
  All 21 lessons rebuilt so the fix reaches the deployed self-contained pages.
- Corrected Chapter 18 prose that stated a 6 year crossover and a $2M penalty; the simulation computes
  7 years and $1.65M over 30 years.
- Corrected the Chapter 19 `reslevel` config, which used the wrong shape (`bars`/`load` instead of
  `tasks` with start, duration and crew) and would have rendered an empty histogram.

## [0.26.0] - 2026-07-19
### Added: PM Chapter 18
- Released Chapter 18, "Asset management, digital delivery, and resilience," covering life-cycle cost
  and best value procurement, the handover operations actually needs, GIS versus BIM versus SCADA,
  and resilience through firm capacity and the One Water idea.
- Added reusable `tco` component: two options with different capital and annual costs, and a slider for
  the evaluation period. The winner flips at the crossover year, which is the whole life-cycle costing
  argument made visible.
- Added reusable `firmcap` component: installed capacity versus firm capacity. Take the largest unit out
  of service and watch a comfortable-looking system fall short of peak day demand.

## [0.25.0] - 2026-07-19
### Added: PM Chapter 17
- Released Chapter 17, "Safety, locates, and commissioning," covering the hierarchy of controls,
  the one-call locate cycle and tolerance zone, right of way and agency coordination, and
  commissioning, clearance, and the substantial versus final completion distinction.
- Added reusable `controls` component: pick a rung of the hierarchy of controls for a stated hazard
  and see residual risk, showing how little personal protective equipment actually removes.
- Added reusable `clearance` component: step through disinfection and bacteriological clearance and
  watch a single failed sample round cost four days rather than one, against a schedule that allowed two.

### Fixed
- Replaced a `twofig` usage in Chapter 17 that passed the wrong config shape (`twofig` requires
  `left`/`right` objects containing SVG, not point lists) with an interactive `table`.

## [0.24.0] - 2026-07-19
### Added: PM Chapter 16
- Released Chapter 16, "The capital life cycle and the rules that shape it," covering the utility
  capital project life cycle with stage gates, the regulatory landscape (Safe Drinking Water Act,
  Lead and Copper Rule, PFAS, Clean Water Act NPDES and Section 404), and environmental permitting
  as a schedule driver.
- Added reusable `permitsim` component: tick the attributes of a job, see which approvals it triggers,
  and watch whether the longest approval exceeds design and bid duration and therefore lands on the
  critical path.
- Added reusable `backplan` component: work backwards from a fixed compliance deadline through phase
  durations to the latest responsible start date, with a red verdict when that date has already passed.

### Fixed
- Corrected the Chapter 16 life-cycle component config, which used the wrong key names for the
  `process` renderer and silently rendered an empty body.

## [0.23.0] - 2026-07-19
### Added: Data Governance Chapters 06 through 08
- Released Chapter 06 with a backward-and-forward provenance network, governed decision lifecycle,
  formula-impact model, handoff simulation, four varied checks, a deployable decision evidence package,
  and the D04.1 through D04.5 evidence gate.
- Released Chapter 07 with a role handoff simulation, decision-rights table, escalation flow, council
  charter, conflict-of-duty controls, governance calendar, five varied checks, and the D02 operating-model
  evidence gate.
- Released Chapter 08 with a layered scope model, value-driver tree, risk-threshold matrix, decision-rights
  flow, portfolio prioritizer, evidence-gated roadmap, four varied checks, and the full D01.1 through D01.5
  deployment package.

### Changed
- Changed the Data Governance mixed release to nine available lessons and 16 governed content-pending
  destinations, with completion enabled only for Chapters 00 through 08.
- Advanced the canonical course, generator, landing page, manifest, and completion event keys to 0.23.0.


## [0.22.0] - 2026-07-19

### Added
- **PM Chapter 15: Measurement and honest status** (`module-15-measurement-honest-status.html`). Two sections: metrics, KPIs and dashboards; evidence-grounded status and the weekly ritual. Leading vs lagging indicators, the measures worth watching on a capital job, and how to write a status a board can act on.
- **New reusable component: `dashboard`.** A live KPI dashboard: each measure gets a slider and a red/amber/green chip, and the honest overall status takes the **worst** light, not the average. Teaches the watermelon failure (green outside, red at the core) by letting the learner try to average bad news away and watch it refuse.

### Changed
- Chrome marks Chapter 15 live; `tools/build-selfcontained.py` LINK_MAP extended to module-15.
## [0.21.0] - 2026-07-19
### Added: Data Governance Chapters 03 through 05
- Released Chapter 03, "Standards, law, and the applicability record," with an authority stack,
  standards-to-jobs crosswalk, authority classification, legal applicability gate, jurisdiction-change
  cycle, register builder, source-edition review, evidence gate, and completion event for `dga001:03`.
- Released Chapter 04, "Map the utility data estate around decisions," with a filterable physical and
  digital estate network, minimum utility-domain tree, governed interface simulation, decision-priority
  matrix, weighted shortlist, estate-map builder, reconstruction method, and completion event for
  `dga001:04`.
- Released Chapter 05, "Shared identity and minimum governed records," with an evidence-based identity
  bridge, controlled match-rate chart, duplicate-impact model, minimum-record stack and profiles,
  identity-resolution cycle, two deployment builders, change test, and completion event for `dga001:05`.
- Added reusable `applicability`, `estatemap`, and `identitybridge` Academy components, documented and
  rendered in the shared component gallery.

### Changed
- Changed the Data Governance mixed release to six available lessons and 19 governed content-pending
  destinations.
- Bumped governed course metadata, root version, component catalog, build manifest, landing page, and
  release event keys to 0.21.0.

## [0.20.0] - 2026-07-19
### Added: Data Governance Chapter 02
- Released the complete utility deployment lesson, "The language of trustworthy utility data," using
  Riverbend's drinking-water release and the controlled Version 2.3 Chapter 2 and Figure 2.
- Added governance-versus-management comparison and classification, a step-through provenance
  network, minimum-event ordering, a live quality-by-use model, and a governed data-product package.
- Added matching, classification, ordering, true-or-false, multiple-choice, and reflection checks
  with plain explanatory feedback.
- Added evidence-safe provenance-event and data-product builders, a Chapter 02 Launch Pack tracker,
  an evidence gate, and the OWOS Learn completion event for learning object `dga001:02`.
- Added reusable `provnet` and `qualityfit` Academy components for later courses and chapters.

### Changed
- Changed the Data Governance mixed release to three available lessons and 22 governed
  content-pending destinations.
- Bumped the governed course metadata, root version, component catalog, manifest, and landing page to
  0.20.0.

## [0.19.0] - 2026-07-19
### Added: Chapters 10-14 + four reusable simulations
- `coq` (Ch10): cost-of-quality curve, slide prevention and watch failure cost fall and total cost bottom
  at the sweet spot. Verified failBase 400 / K 100 -> optimum at prevention 100, total 300.
- `grid` (Ch11 risk, Ch12 stakeholders): interactive 2x2 probability-impact / power-interest matrix with
  colored quadrants, plotted items, and per-item strategy on click.
- `channels` (Ch12): communication-channels explosion, n(n-1)/2 as a live node graph. Verified 6 -> 15, 12 -> 66.
- `zopa` (Ch13): negotiation zone-of-possible-agreement, seller floor vs buyer ceiling with the overlap band.
- Chapter 10 Quality management (QA/QC, ITP hold/witness points, cost of quality, NCR).
- Chapter 11 Risk & uncertainty (threat/opportunity, probability-impact matrix, EMV, responses & reserves, resilience).
- Chapter 12 Teams, stakeholders & communication (Tuckman, RACI, power-interest grid, comm channels).
- Chapter 13 Leadership, negotiation & ethics (situational leadership, BATNA/ZOPA, conflict modes, ethics).
- Chapter 14 Executing & controlling (process groups, operating rhythm, integrated change control with the ripple).
- All verified in the browser: sim math correct, no data-ac collisions, no dashes.
### Changed
- Masterclass chrome: Chapters 10 to 14 now live; status note "Chapters 01 to 14 are live." (14 live cards.)
### Deployed
- Published Chapters 10-14 + course page to owos.ai.

## [0.18.0] - 2026-07-19
### Added: Data Governance Chapter 01
- Released the complete utility deployment lesson, "The missing layer above utility systems," using
  the Riverbend wet-weather response decision and the controlled Version 2.3 Chapter 1 and Figure 1.
- Added five varied teaching shapes: the governed layered stack, a fragmented-to-governed reveal,
  a step-through handoff simulation, an expandable consequence tree, and a live fragmentation-cost
  planning model.
- Added system-versus-governance classification, utility judgment, true-or-false, multi-select, and
  executive-reflection checks with explanatory feedback.
- Added an evidence-safe executive-case builder, a Chapter 01 Launch Pack tracker, an evidence gate,
  and the OWOS Learn completion event for learning object `dga001:01`.
- Added reusable `layerstack`, `beforeafter`, `handoff`, `fragtax`, and `artifactbuilder` Academy
  components for later courses and chapters.

### Changed
- Changed the Data Governance mixed release to two available lessons and 23 governed
  content-pending destinations.
- Bumped the governed course metadata, root version, component catalog, manifest, and landing page to
  0.18.0.

## [0.17.0] - 2026-07-19
### Added: Chapter 09 + a contract-risk simulator
- `contractrisk` : drag the final actual cost and watch who eats the overrun under Firm Fixed Price,
  cost-plus/T&M, and GMP. Verified at 1200 actual (1000 target): FFP contractor -100, cost-plus +100,
  GMP -50; at 900: FFP +200. Shows risk transfer as a live number.
- Chapter 09 "Procurement, contracts and claims" built on the library (IFB/RFP/RFQ solicitation, NTP,
  contract types and risk, submittals/retainage/pay apps/lien waivers, change orders vs claims,
  liquidated damages, the dispute-resolution ladder).
### Changed
- Masterclass chrome: Chapter 09 now live; status note "Chapters 01 to 09 are live."
### Deployed
- Published Chapter 09 + course page to owos.ai; verified the contract-risk sim computes on the live site.

## [0.16.0] - 2026-07-19
### Added: Chapter 08 + an Earned Value simulator
- `evm` : an interactive Earned Value chart. Drag schedule elapsed, work complete, and actual cost, and
  watch the PV / EV / AC curves, the CPI and SPI indices, and the EAC forecast update live, with a
  plain-language verdict. Verified: t50/w40/a600 on a 1300 BAC -> PV 650, EV 520, AC 600, CPI 0.87,
  SPI 0.80, EAC 1.50M (over budget + behind); w60 flips it green (CPI 1.30, SPI 1.20, EAC 1.00M).
- Fixed a `data-ac` attribute collision in the EVM Actual-Cost cell (renamed to data-acost).
- Chapter 08 "Earned Value and forecasting" built on the library (PV/EV/AC, CPI/SPI, EAC/ETC/VAC/TCPI).
### Changed
- Masterclass chrome: Chapter 08 now live; status note "Chapters 01 to 08 are live." Rebuilt all eight lessons.
### Deployed
- Published all eight lessons + course page to owos.ai; verified the EVM sim computes on the live site.

## [0.15.0] - 2026-07-19
### Added: Data Governance Chapter 00
- Released the complete interactive orientation lesson, "How to use the Master Class," with
  Foundation, Practitioner, and Leader lenses and the Riverbend wet-weather response case.
- Added a six-part course roadmap, four release-decision gates, claim-boundary comparison, capstone
  decision selector, role pathway map, Deployment Studio, evidence gate, and provenance record.
- Added an ungraded entry diagnostic plus classification, ordering, multiple-choice, and reflection
  checks with explanatory feedback.
- Added the reusable `artifacttracker` Academy component with four record states and device-local
  progress persistence, then documented it in the component catalog and gallery.
- Added the Chapter 00 completion control for OWOS Learn while keeping certification, compliance, and
  assurance claims outside the course-completion event.

### Changed
- Changed the Data Governance build from an all-placeholder shell to a mixed release: Chapter 00 is
  available and Chapters 01 through 24 retain governed content-pending destinations.
- Bumped the governed course metadata, root version, manifest, and landing page to 0.15.0.

## [0.14.0] - 2026-07-19

### Added: Chapter 07 + three cost/finance simulations
- `estrange` : AACE estimate-accuracy range, slide design maturity (Class 5 to 1) and watch the low-high
  band narrow around the point estimate. Verified 1300 base -> Class5 910/1950, Class1 1235/1430.
- `cipplan` : fit a multi-year CIP into an annual budget; ranked projects fund or defer as the cap moves.
- `rateimpact` : project cost -> monthly bill per customer via a debt-service amortization. Verified
  1300k / 80% debt / 4% / 20yr / 15k accounts -> 77k/yr -> $5.10/yr -> $0.43/month.
- Chapter 07 "Estimating and budgeting" built on the library (AACE classes, allowances/escalation/
  contingency, cost baseline, capital vs O&M, the CIP, SRF/WIFIA/grants/bonds, Davis-Bacon, rate impact).
### Changed
- Masterclass chrome: Chapter 07 now live; status note "Chapters 01 to 07 are live." Rebuilt all seven lessons.
### Deployed
- Published all seven lessons + course page to owos.ai; verified each new sim computes on the live site.

## [0.13.0] - 2026-07-19
### Added: complete Data Governance curriculum structure and OWOS delivery architecture
- Added `apps/data-ai-governance/` as the governed course-content home for the Data Before AI Master
  Class.
- Added a complete 25-chapter, 75-section syllabus for drinking water, wastewater, stormwater,
  reuse, and integrated One Water utilities.
- Mapped every Version 2.3 assessment criterion from D01.1 through D12.5 and assigned all 21 controlled
  figures a teaching job.
- Added Foundation, Practitioner, and Leader lenses; seven role pathways; the fictional Riverbend
  utility running case; chapter-level utility examples; deployment studios; evidence gates; visual and
  simulation plans; varied checks; and a 20-artifact Utility Data and AI Governance Launch Pack.
- Added the proposed entry diagnostic, chapter checks, part assessments, final scenario assessment,
  capstone, critical-gate pass rule, and course-completion credential boundary.
- Added `course.yaml` with the stable OWOS course ID, pinned Version 2.3 method commit, release gates,
  structure, roles, planning effort, assessment proposal, and credential status.
- Added the canonical ownership, data-flow, release, and version-control contract from `onewater-os`
  through the `2-brain` OWOS.ai runtime, Supabase, Knowledge Graph, and Cloudflare.
- Added Mermaid system and release-flow diagrams, the system-of-record matrix, release gates, stable
  Data Governance identifiers, catalog-preservation rule, and definition of done.
- Added delivery metadata for a native 25-chapter Data Governance shell and its OWOS.ai runtime path.
- Added a generated browser landing page and 25 linked chapter shells, with all lesson content clearly
  marked pending until it passes the governed content acceptance gates.
- Added reproducible self-contained distribution outputs for controlled copy-on-publish into OWOS.ai.

### Changed
- Updated the root and apps indexes to include the new Master Class.
- Synchronized the root README version with `VERSION` at 0.13.0.

## [0.12.0] - 2026-07-19
### Added: Chapter 06 + three quantitative simulations
- `pert` : three-point / PERT estimator, slide optimistic/most-likely/pessimistic and watch the
  distribution and the expected value ((O + 4M + P) / 6). Verified O4 M6 P14 -> expected 7, sigma 1.7.
- `reslevel` : resource histogram with a Before/After leveling toggle; over-allocated weeks are red,
  leveling clears them at the cost of a later finish.
- `montecarlo` : runs the schedule 1,000 times with sampled durations and builds the finish-date
  distribution with plan / P50 / P80 markers. Verified: plan 32 wks < P50 36 < P80 38, ~9% hit the plan.
- Chapter 06 "Advanced scheduling" built on the library (estimating methods, PERT, leveling, crashing vs
  fast-tracking, critical chain, Monte Carlo). Working lens, Millpond thread, recap and leader's bottom line.
### Changed
- Masterclass chrome: Chapter 06 now live; status note "Chapters 01 to 06 are live." Rebuilt all six lessons.
### Deployed
- Published all six lessons + course page to owos.ai; verified each new sim computes on the live site.

## [0.11.1] - 2026-07-19
### Added
- `apps/_course-template/` : a clone-me starter for any new course. Points at `core/` (no copying), with
  a working example module wired to the library, a syllabus template, and a README with the 4-step start.
  Verified the example renders from its apps/ location (spectrum, calculator, flip, classify, reflection).

## [0.11.0] - 2026-07-19
### Added: six new simulations (one+ per chapter), applying the "show it" rule across the course
- `pv` (Ch01): present-value mini-sim, slide years/rate and watch a future dollar shrink to today's value.
- `costcurve` (Ch02): the cost of a change by when it is caught (1x to 100x across the life cycle).
- `scoreboard` (Ch03): weighted project scoring, adjust criteria weights and watch the portfolio re-rank.
- `ripple` (Ch03): integration in action, move scope and watch schedule, cost, and risk all react at once.
- `rollup` (Ch04): the WBS 100% rule, type hours into work packages and watch them roll up the tree.
- `ganttedit` (Ch05): what-if scheduling, crash a task and watch the finish move and the critical path jump.
- All verified for correct math (discounting, weighted ranking, CPM recompute, rollup sums) in the browser.
### Deployed
- Rebuilt all five lessons and published to owos.ai; verified each new sim renders and computes on the live site.

## [0.10.2] - 2026-07-19
### Fixed
- Corrected the cpmsim node width/layout mismatch so the fitted diagram spaces correctly (shipped as v0.10.2).

## [0.10.1] - 2026-07-19
### Fixed
- The `cpmsim` critical-path diagram ran off the right edge of the page. It now scales the fixed-width
  activity-on-node network to fit the card width (with room for the float badges) and re-fits on resize,
  so the whole diagram is visible with nothing cut off. Tightened the node/gap sizing so the fit lands
  at a readable ~76% rather than shrinking too far.

## [0.10.0] - 2026-07-19
### Added: a critical-path simulator + the "show it" principle
- New library `cpmsim` renderer: an interactive activity-on-node simulation that DERIVES the critical
  path step by step. Reset / Back / Step / Play controls walk the forward pass (earliest dates), the
  backward pass (latest dates), float, then light up the critical chain in gold, with live narration at
  each step. Added to Chapter 05, Section 3. Verified: floats compute to permit 5, procurement 0, and
  the critical chain reads survey → procure → pipe → tie-ins → test → close out.
- Standards updated (WRITING-STANDARD, VISUAL-ARSENAL) with the **"simulate, do not just describe"**
  rule: any process, algorithm, or thing-that-unfolds gets an interactive that shows it happening
  (step-through, live model, or reveal), not just prose. Build it into the shared library so every
  future chapter can reuse it. This is now a standing requirement, per Hardeep.
### Deployed
- Rebuilt all five lessons + course page and published to owos.ai; verified live.

## [0.9.0] - 2026-07-18
### Added: Chapter 05 + two scheduling components
- New library `gantt` renderer: an interactive Gantt that runs a real Critical Path Method engine
  (forward and backward pass, float), highlights the critical path in gold, shows slack, and gives
  per-activity dates and float on click. Verified: the Millpond schedule computes to a 30-week
  critical path through survey, long-lead procurement, pipe, tie-ins, test, and closeout, with the
  permit correctly showing 5 weeks of float.
- New library `scurve` renderer: a cost-loaded cash-flow S-curve (period bars plus cumulative line).
- Chapter 05 "Scheduling and the Critical Path" built on the library: the Gantt, dependency-type
  classification, lag and lead, the CPM method, a zero-float slip estimate, a crash-the-critical-path
  judgment, and the S-curve. Working lens, Millpond thread, recap and leader's bottom line.
### Changed
- Masterclass chrome: Chapter 05 now live; status note "Chapters 01 to 05 are live." Rebuilt all five
  lessons + course page self-contained.
### Deployed
- Published all five lessons + the course page to owos.ai and verified each renders on the live,
  authenticated site.

## [0.8.0] - 2026-07-18
### Added: Chapter 04 + a WBS tree component
- New library `tree` renderer: an interactive Work Breakdown Structure (expand/collapse branches, click
  any node for its detail). CSS added for the tree.
- Chapter 04 "Scope and requirements" built fresh on the library: requirement-type classification, a
  vague-vs-testable contrast, a gather-and-lock-down method, a traceability check, the Millpond WBS tree
  (23 nodes to work packages), in/out-of-scope sorting, a scope-change judgment, and myths. Working lens,
  Millpond thread, recap and leader's bottom line.
### Changed
- Masterclass chrome: Chapter 04 now live; status note "Chapters 01 to 04 are live."
- Rebuilt all four lessons + the course page self-contained.
### Process
- New rule: a deploy is not "done" until the LIVE authenticated page is confirmed rendering in the
  browser (not just the local build). Verified Chapters 01 to 04 render on owos.ai before shipping.
### Deployed
- Published all four lessons + the course page to owos.ai via the Cloudflare Pages deploy.

## [0.7.0] - 2026-07-18
### Added: two library components
- `calc` renderer: a reusable business-case calculator (NPV, payback, benefit-cost ratio) with a live
  cash-flow curve and a spend-vs-return bar chart. Config sets the input ranges, labels, and defaults.
- Upgraded the `triangle` renderer to the richer version: a stretching polygon with a live quality dot
  (0 to 100) and a dynamic badge, instead of the simpler static triangle.
### Changed: Chapter 01 migrated onto the library
- "What a project is" rebuilt from hand-rolled markup to the shared library: the one-question test,
  classify, the rich iron triangle, the phase-gate life cycle, the business-case calculator (verified
  identical math: NPV +$2.57M, payback 7.2 years, BCR 2.97 at the defaults), and the mixed quizzes.
- Threaded the Millpond Road job through it, wired the Full/Plain/Leader lens for real, defined NPV and
  BCR on first use, added a closing recap and leader's bottom line.
### Added: Chapter 03 (new)
- "Governance, integration and tailoring" built fresh on the library: a why-gates contrast, a three-kinds
  -of-PMO comparison table, must-do vs scored classification, the charter-to-PM-plan method, subsidiary-plan
  matching, an integration judgment, a tailoring spectrum and recommender, an ordering quiz, and myths.
  Working lens, Millpond program thread, recap and leader's bottom line.
### Changed
- Masterclass chrome: Chapter 03 now live; status note corrected to "Chapters 01 to 03 are live."
- `build-selfcontained.py`: added the Chapter 03 link mapping.
### Deployed
- Rebuilt all three lessons and the course page self-contained and published to the `2-brain` site (owos.ai)
  via the Cloudflare Pages deploy (git push alone does not publish).

## [0.6.0] - 2026-07-18
### Changed: Chapter 02 deepened (it felt thin as a survey)
- Wired the Full / Plain / Leader lens for real. It had zero content variants and did nothing; now
  Full shows the detail, Plain trims it, and Leader shows only the call. Verified across all three modes.
- Threaded one running job through the whole chapter: the Millpond Road lift station rebuild. Every
  component now works that job (spectrum, phase-gate, comparison table, recommender, quizzes).
- Added a numbers moment (a schedule-savings estimate) and an ordering quiz, taking it to eight quiz
  types. Added a closing recap and a leader's bottom line.
- Added the Florida procurement reality: qualifications-based design selection under the Consultants'
  Competitive Negotiation Act (CCNA), and how competitive-bid rules and alternative-delivery authority
  bound the delivery choice. New library styles: `.casebox`, `.leadcall`, `.recap`.
- Grew from ~1,955 to ~2,884 words (depth, not padding), no em/en dashes.
### Deployed
- Rebuilt the self-contained Chapter 02 and republished it to the `2-brain` site (owos.ai).

## [0.5.0] - 2026-07-18
### Added: the shared component library (the real fix)
- `core/components/academy.css` and `core/components/academy.js`: one place that holds every
  polished component and quiz. A module now writes small declarative markup
  (`<div data-ac="spectrum">` with a JSON config) and the library renders the identical, gallery-grade
  component. Fix a component once, every module updates. Renderers: flip, match, mc, multi, classify,
  estimate, truefalse, order, reflect, spectrum, table, recommender, decide, triangle, process, method,
  twofig, plus tooltips, lens, reading progress, goals, and the Droobi cue.
- `tools/build-selfcontained.py`: inlines the library into one distributable HTML file (escapes any
  `</script>` so the inline script parses), rewrites nav links to deployed names, and asserts no dashes.
### Changed: Chapter 02 rebuilt on the library (this was the "shittiest version" complaint)
- Every diagram and quiz is now the real library component, not a hand-rolled version. Twelve components:
  flip cards, a predictive-to-adaptive spectrum, a line-versus-loop contrast, an interactive phase-gate,
  a delivery-method comparison table, matching, a five-step method, a recommender, and classify /
  multiple-choice / true-false / reflection quizzes.
- Every acronym is spelled out on first use (DBB, DB, CMAR, PDB, GMP) with a hover definition.
- Exactly one tooltip element, zero native `title` attributes. The "two tooltips" bug is gone.
- Verified live in the browser: all 12 components render and interact correctly.
### Deployed
- Rebuilt the self-contained Chapter 02 and published it to the `2-brain` site (owos.ai).

## [0.4.1] - 2026-07-18
### Changed (standards, per Hardeep's direction)
- Added hard rules: spell out every acronym in full on first use (short form in parentheses); every
  term and acronym gets ONE hover tooltip (no second `title`-attribute tooltip).
- Added the top rule: a module is ASSEMBLED by copying the exact components out of `component-gallery.html`
  and `quiz-gallery.html` (chosen via the Selection Prompt, content from `SYLLABUS.md`). Never hand-roll
  a simpler diagram or quiz. The galleries are the single source of truth for how components look and work.
- Reinforced the same in `VISUAL-ARSENAL.md` and `QUIZ-TYPES.md`.
### Next
- Build a shared component library (one CSS + one JS) so every module uses the real gallery components,
  then rebuild Chapter 02 on it. Acronyms defined first, tooltip doubling fixed.

## [0.4.0] - 2026-07-18
### Added
- Chapter 02 (Delivery & life cycles), built with a fresh visual palette so it does not echo
  Chapter 01: a predictive-vs-agile spectrum, a linear-vs-loop diagram, an interactive delivery-method
  comparison table and recommender, plus five quiz types (classify, matching, flip cards, multiple
  choice, true/false) and a reflection. Plain voice, no em dashes.
- Native deploy page `dist/site/lesson-pm-02-delivery-life-cycles.html`.
### Changed
- Course chrome: Chapter 02 now live; Chapter 05 set back to "coming soon" until it is deployed
  (we deploy in sequence).
### Deployed
- Published Chapter 02 and the updated course landing to the `2-brain` site (owos.ai).

## [0.3.1] - 2026-07-18
### Added
- Native owos.ai deploy page for the course landing: `dist/site/course-project-management.html`
  (course overview + curriculum), shell-wrapped and verified with the dark-hero and button guards.
### Fixed
- Removed em/en dashes from the course chrome to meet the writing standard.
### Deployed
- Published the course landing and Chapter 01 into the `2-brain` site (owos.ai) as
  `course-project-management.html` and `lesson-pm-01-what-is-a-project.html`.

## [0.3.0] - 2026-07-18
### Added
- Two ship-ready output formats for the PM course, in `apps/project-management/dist/`:
  - `dist/site/` native owos.ai pages that link the shared shell (`/owos-brand.css`, `/owos-shell.js`),
    so they match every other lesson on the site. Chapter 01 built and verified against the real shell.
  - `dist/scorm/ch01/` a SCORM 1.2 package (`pm-ch01-scorm12.zip`) for uploading to any external LMS,
    with `imsmanifest.xml`, `content.html`, and a `scorm-api.js` completion reporter.
- `dist/README.md` explaining the outputs and how to wire the course into owos.ai (git submodule).

### Notes
- Single source of truth stays in `onewater-os`; `dist/` holds the built formats next to the source.

## [0.2.1] - 2026-07-18
### Changed
- Finished Chapter 01 (What a project is) as the full exemplar. It now uses the whole palette:
  a decision framework, an interactive iron-triangle diagram, a clickable life-cycle process, a
  method, a calculator with a cash-flow curve and a bar chart, and seven quiz types (classify,
  multiple choice, estimate, flip cards, matching, true/false, reflection). Plain voice, no em dashes.

## [0.2.0] - 2026-07-18
### Changed
- Restructured into a monorepo so every app can reuse one shared foundation.
  - `core/` now holds the reusable wheel: `brand/`, `standards/` (writing standard + visual arsenal),
    and `components/` (component gallery, quiz gallery, module template, catalogs).
  - The Project Management work moved into `apps/project-management/` (curriculum, playbook, starter kit).
- Renamed the repo from `onewater-pm-system` to `onewater-os`.
- Rewrote the README to document the monorepo and how to add a new app.

## [0.1.0] - 2026-07-18
Initial commit. Everything to date is captured and put under version control.

### Brand
- One Water OS "Clearwater" brand guidelines and extracted assets (Droobi, logo, icons, OG image).

### Playbook
- Utilities & Construction PM field playbook (HTML + print PDF).

### Masterclass framework
- `WRITING-STANDARD.md` — voice rules (plain, conversational, no em dashes, no cliches), required
  learning components, and quiz variety.
- `VISUAL-ARSENAL.md` — catalog of ~35 visual types plus the Selection Prompt.
- `component-gallery.html` — every visual rendered live.
- `quiz-gallery.html` — ten quiz types, all interactive.
- `COMPONENTS.md` and `QUIZ-TYPES.md` — Markdown catalogs of the two galleries.
- `module-template.html` — the reusable empty module scaffold, wired to the files above.

### Masterclass content
- `SYLLABUS.md` — 21 chapters, 60 sections, mapped to PMBOK.
- `masterclass-project-management.html` — the course shell ("chrome").
- `module-01-what-is-a-project.html` — Chapter 01, built with framework, diagram, process, chart,
  curve, method, and four quiz types.
- `module-b3-b6-critical-path.html` — Scheduling & Critical Path, the interactive format mold.

### Starter kit
- Plain-file project scaffold (Brief, Board, Budget, Risks, Permits, Schedule, Compliance,
  Stakeholders, Classification, Notes, Inbox, CLAUDE.md).

<!-- Template for future entries:
## [0.x.0] - YYYY-MM-DD
### Added / Changed / Fixed / Removed
- ...
-->
