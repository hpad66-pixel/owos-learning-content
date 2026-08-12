---
title: Detention, Retention, and Infiltration Verification Dossier
brief_id: owos:concept-brief:003
version: 0.1.0
status: prepared_for_independent_and_qualified_review
evidence_cutoff: 2026-07-26
public_release_authority: none
---

# Verification Dossier

## Purpose

This dossier routes every material national claim to the review it needs before learner-facing
production or release. It does not verify its own claims. The author has assembled the original
source relationships and review questions. An independent verifier and qualified practitioners
must complete and sign their own records.

The separate Florida jurisdiction-specific claim register remains under
`research/florida-claims.yaml`. Florida claims require their own current legal, regulatory,
stormwater, hydrogeology, wastewater, and permitting reviews and cannot approve the public national
brief.

## Required reviewers

| Review role | Required scope | Independence boundary |
| --- | --- | --- |
| Independent source verifier | Open each original federal source, confirm the exact statement, locator, current status, jurisdiction, limitation, and freshness date | Must not rely on this dossier as the source |
| Qualified stormwater practitioner | Detention, wet ponds, permanent pools, infiltration, outlets, overflows, hydrographs, routing, maintenance, receiving waters, and performance measures | Records name, qualifications, date, comments, and disposition |
| Qualified wastewater collection practitioner | I&I terminology, separate-system boundary, hydraulic capacity consequences, and limits of the cross-sector explanation | Records name, qualifications, date, comments, and disposition |
| Qualified federal stormwater permitting reviewer | NPDES permit purpose, municipal separate storm sewer system responsibilities, construction and industrial stormwater context, and evidence boundaries | Confirms current federal scope without adding state requirements |
| Visual truth reviewer | Every visual statement, arrow, elevation relationship, sequence, quantity, caption, tooltip, alternative text, and nonclaim boundary | Must review rendered output as well as source claims |
| Editorial and novice reviewer | Plain-language understanding, term order, misconception repair, cognitive load, and usefulness of the final work product | Cannot approve technical accuracy |

## Claim group A: terminology and pathways

| Claim | Original sources | Author trace | Required review question |
| --- | --- | --- | --- |
| `claim-name-not-pathway` | `source-epa-bmp-terminology`, `source-epa-national-bmp-menu` | Prepared | Does the synthesis fairly state that a name alone cannot establish full pathway, objective, suitability, or condition? |
| `claim-detention-temporary-release` | `source-epa-flow-control`, `source-epa-bmp-terminology` | Prepared | Does the public explanation accurately describe temporary storage and later release without turning typical conditions into a universal definition? |
| `claim-retention-varies` | `source-epa-bmp-terminology`, `source-epa-flow-control` | Prepared | Do the sources support the stated terminology variation, and is the limitation sufficiently visible? |
| `claim-infiltration-pathway` | `source-epa-groundwater`, `source-ecfr-small-ms4` | Prepared | Does the explanation separate surface entry, soil movement, treatment, underdrain discharge, and groundwater interaction? |
| `claim-infiltration-final-destination` | `source-epa-groundwater`, `source-epa-types-green-infrastructure`, `source-epa-infiltration-trench` | Prepared | Does the claim avoid promising recharge or one final destination? |
| `claim-wet-pond-permanent-pool` | `source-epa-wet-ponds`, `source-epa-flow-control` | Prepared | Does the national conceptual description support a normally wet pool plus additional temporary storage without importing a state definition? |
| `claim-green-infrastructure-definition` | `source-uscode-green-infrastructure` | Prepared | Does the learner wording match the current federal statutory definition and keep its statutory scope visible? |

Required qualified reviewer: Stormwater practitioner.  
Additional review: Independent source verifier and visual truth reviewer.

## Claim group B: time, models, and performance

| Claim | Original sources | Author trace | Required review question |
| --- | --- | --- | --- |
| `claim-hydrograph-peak-volume-distinction` | `source-usgs-hydrograph`, `source-epa-performance` | Prepared | Does the qualitative hydrograph correctly separate peak, timing, and event volume? |
| `claim-volume-load-performance` | `source-epa-performance` | Prepared | Does the instruction accurately distinguish concentration, discharged volume, and total pollutant load? |
| `claim-model-boundary` | `source-epa-swmm` | Prepared | Does the narrative explain model capability and uncertainty without suggesting that a conceptual model predicts a real system? |
| `claim-illustrative-storm` | Instructional scenario, no external source | Prepared | Are every value, route, state, and outcome visibly labeled illustrative and nonpredictive? |

Required qualified reviewer: Stormwater practitioner with hydrologic and hydraulic competence.  
Additional review: Independent source verifier, visual truth reviewer, and novice reviewer.

## Claim group C: groundwater and maintenance

| Claim | Original sources | Author trace | Required review question |
| --- | --- | --- | --- |
| `claim-groundwater-protection` | `source-epa-groundwater` | Prepared | Does the claim present potential recharge and groundwater risk without deciding site suitability? |
| `claim-ms4-maintenance` | `source-ecfr-small-ms4` | Prepared | Is the current federal small municipal separate storm sewer system requirement represented accurately and within scope? |
| `claim-maintenance-pathway` | `source-epa-maintenance`, `source-ecfr-small-ms4` | Prepared | Does the synthesis connect condition to possible pathway consequences while separating observation from diagnosis and authorized action? |

Required qualified reviewer: Stormwater practitioner.  
Additional review: Federal stormwater permitting reviewer for the regulatory claim and visual truth
reviewer for the failure trace.

## Claim group D: wastewater I&I

| Claim | Original sources | Author trace | Required review question |
| --- | --- | --- | --- |
| `claim-ii-definition` | `source-epa-sso-faq`, `source-epa-sso` | Prepared | Does the explanation distinguish infiltration and inflow in a separate sanitary sewer without creating a false absolute boundary? |
| `claim-ii-capacity-consequence` | `source-epa-peak-flows`, `source-epa-sso-faq`, `source-epa-sso` | Prepared | Are conveyance, pumping, treatment, storage, overflow-risk, operating, and capital consequences stated as bounded system effects rather than calculated outcomes? |

Required qualified reviewer: Wastewater collection-system practitioner.  
Additional review: Independent source verifier and visual truth reviewer.

## Claim group E: permits and public value

| Claim | Original sources | Author trace | Required review question |
| --- | --- | --- | --- |
| `claim-npdes-permit-function` | `source-epa-npdes-permit-basics` | Prepared | Does the simple permit explanation accurately describe federal authorization and responsibility without implying site applicability? |
| `claim-ms4-program-responsibility` | `source-ecfr-small-ms4`, `source-epa-ms4-program` | Prepared | Are municipal separate storm sewer system responsibilities current, correctly scoped, and not generalized beyond regulated programs? |
| `claim-construction-stormwater-connection` | `source-epa-construction-stormwater` | Prepared | Is construction stormwater described accurately without supplying compliance guidance? |
| `claim-industrial-stormwater-context` | `source-epa-industrial-stormwater` | Prepared | Is industrial stormwater context accurate and bounded? |
| `claim-permit-value-synthesis` | `source-epa-npdes-permit-basics`, `source-epa-ms4-program`, `source-ecfr-small-ms4` | Prepared | Does the permit-to-value chain fairly distinguish authorization, responsibility, funded work, evidence, and correction from proof of actual performance? |

Required qualified reviewer: Federal stormwater permitting reviewer.  
Additional review: Independent source verifier, stormwater practitioner, and editorial reviewer.

## Claim group F: owner direction and connected learning

| Claim | Original sources | Author trace | Required review question |
| --- | --- | --- | --- |
| `claim-connected-learning-proposal` | `source-portfolio-seed` | Prepared | Does the connection reflect approved product direction without presenting a Graph relationship as technical evidence? |

Required reviewer: Owner and Graph steward.

## Visual review map

| Visual or interaction | Claims that must pass before production signoff |
| --- | --- |
| Connected storm route and storm tracer | Name not pathway, detention, infiltration, I&I, illustrative storm |
| Dry-basin timeline | Detention, hydrograph peak and volume, illustrative storm |
| Wet-pond elevation cutaway | Wet-pond permanent pool, retention variation |
| Practice-family and subsurface cutaways | Infiltration pathway, final destination, groundwater protection, green infrastructure definition |
| Hydrograph | Hydrograph peak and volume, model boundary, illustrative storm |
| Water and pollutant ledger | Volume and load performance, illustrative storm |
| Condition failure trace | Maintenance pathway, municipal maintenance context |
| Stormwater and wastewater split | I&I definition and capacity consequence |
| Permit-to-value handoff | Permit function, municipal responsibility, construction and industrial context, permit-value synthesis |
| Five ledgers and role evidence map | Permit-value synthesis, maintenance pathway, I&I consequence, owner direction |

## Independent verification record template

For each claim, the independent verifier records:

1. Claim identifier.
2. Original source opened directly.
3. Exact section, paragraph, page, or heading.
4. Current authority and publication status.
5. Jurisdiction and applicability boundary.
6. Whether the claim is supported, supported with revision, unsupported, or unresolved.
7. Required wording change.
8. Freshness date.
9. Verifier name and independence statement.
10. Date and signature or governed approval record.

## Qualified-review record template

For each applicable claim and visual, the qualified reviewer records:

1. Reviewer name and relevant qualification.
2. Scope reviewed.
3. Technical accuracy decision.
4. Missing condition, failure mode, or misleading implication.
5. Required correction.
6. Whether the revised wording and visual resolve the comment.
7. Remaining uncertainty.
8. Review date and governed approval record.

## Current decision

The author source-trace dossier is prepared. No claim has received independent verification or
qualified signoff. Verification coverage therefore remains 0 percent for release purposes. Design
and storyboard review may continue, but replacement learner-facing HTML and release remain blocked.
