---
title: Added Terminology Source Dossier
brief_id: owos:concept-brief:003
version: 0.1.0
status: prepared_for_independent_and_qualified_review
scope: The twelve terms and explanations listed in white-paper.md section 19 as not yet source-anchored
evidence_cutoff: 2026-07-27
retrieval_date: 2026-07-27
public_release_authority: none
verification_status_of_everything_below: pending
---

# Added Terminology Source Dossier

## Purpose and standing

`white-paper.md` section 19 quarantines twelve terms and explanations that were added during the
instructional expansion and that do not yet resolve to a cited entry in the reference list. This
dossier proposes a source for each of them.

Nothing in this dossier is verified. Every source named below was actually retrieved and read on
2026-07-27, and every supporting passage is quoted or closely paraphrased from the retrieved text so
that an independent verifier can re-find it quickly. The author is not the verifier. All proposed
records enter `sources.yaml` and `claims.yaml` with `verification_status: pending`.

This dossier does not edit `white-paper.md`, `sources.yaml`, or `claims.yaml`.

### Authority rules applied

Only United States federal authority was accepted: current federal statute and regulation, current
federal agency guidance and technical references tied to that authority (EPA, USGS, USDA NRCS,
USACE, FHWA, NOAA, FEMA), and peer-reviewed research kept inside its stated scope. State
requirements were excluded. One promising hit was rejected on this ground and is recorded in
"Rejected sources" below so the exclusion is auditable rather than invisible.

### Verdict definitions used here

- **FOUND** — a retrieved federal source states the term and the substance of the white-paper
  sentence it must support.
- **PARTIAL** — a retrieved federal source supports the underlying mechanism or one half of the
  statement, but not the term as written, or not the specific distinction claimed.
- **NOT FOUND** — no federal source was located.

---

## Summary table

| # | Item | Verdict | Proposed claim type | Proposed authority tier |
| --- | --- | --- | --- | --- |
| 1 | Detention time and residence time distinction | PARTIAL | technical_standard | epa_technical_reference |
| 2 | Control elevation | PARTIAL | technical_standard | epa_guidance (mechanism only; term unsourced) |
| 3 | Littoral zone | FOUND | technical_standard | epa_guidance |
| 4 | Infiltration rate vs infiltration capacity, and runoff generation | FOUND | sourced_fact | epa_technical_reference |
| 5 | Hydraulic conductivity distinct from infiltration capacity | FOUND | sourced_fact | epa_technical_reference |
| 6 | Freeboard | FOUND | technical_standard | us_federal_primary_authority + epa_technical_reference |
| 7 | Tailwater and its effect on outlet release | FOUND | sourced_fact | epa_technical_reference |
| 8 | Time of concentration, and the effect of development | FOUND | sourced_fact | usda_nrcs_technical_standard |
| 9 | Downstream peak coincidence from combined delayed releases | FOUND | sourced_fact (was expert_interpretation) | epa_technical_reference |
| 10 | Event mean concentration as the concentration term in load | FOUND | sourced_fact | epa_technical_reference |
| 11 | First flush as a variable phenomenon, not a rule | FOUND | sourced_fact | epa_technical_reference |
| 12 | Wet-weather response shape as an inflow/infiltration signature | PARTIAL | expert_interpretation | epa_guidance (archived snapshot) |

**Count: 9 of 12 fully anchored to a retrieved federal source. 3 partial. 0 not found. 0 fabricated.**

Two of the twelve carry a correction, not just a source. See item 1 and item 12.

---

## Source register (proposed entries for `sources.yaml`)

Schema fields match the existing `sources.yaml` records. `verification_status: pending` for all.
Three proposed `authority_tier` values (`usda_nrcs_technical_standard`, `fema_nfip_regulation`,
`epa_regional_guidance_archived`) are new to this brief and are proposals, not decisions.

```yaml
  - source_id: source-epa-bmp-design-guide-v1
    title: Stormwater Best Management Practice Design Guide, Volume 1, General Considerations
    source_type: federal_agency_technical_report
    authority_tier: epa_technical_reference
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: United States Environmental Protection Agency, Office of Research and Development
    locator: https://nepis.epa.gov/Exe/ZyPDF.cgi/901X0A00.PDF?Dockey=901X0A00.PDF
    published_or_effective: 2004-09, EPA/600/R-04/121
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: Published 2004. Used only for terminology definitions and for generalizations the report itself states. Design values, removal percentages, and state practice summaries in the report are excluded. Current EPA usage must be compared before publication.

  - source_id: source-epa-swmm-hydrology
    title: Storm Water Management Model Reference Manual, Volume I, Hydrology (Revised)
    source_type: federal_agency_technical_reference
    authority_tier: epa_technical_reference
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: United States Environmental Protection Agency, Office of Research and Development
    locator: https://nepis.epa.gov/Exe/ZyPDF.cgi/P100NYRA.PDF?Dockey=P100NYRA.PDF
    published_or_effective: 2016-01, EPA/600/R-15/162A
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: Describes how a model represents infiltration. It is a modeling reference, not a field-measurement standard, and does not establish an acceptable infiltration rate for any site.

  - source_id: source-epa-swmm-hydraulics
    title: Storm Water Management Model Reference Manual, Volume II, Hydraulics
    source_type: federal_agency_technical_reference
    authority_tier: epa_technical_reference
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: United States Environmental Protection Agency, Office of Research and Development
    locator: https://nepis.epa.gov/Exe/ZyPDF.cgi/P100S9AS.PDF?Dockey=P100S9AS.PDF
    published_or_effective: 2017, EPA/600/R-17/111
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: Documents the hydraulic equations a model uses. It supports the direction and mechanism of the tailwater effect, not a prediction for any real outlet.

  - source_id: source-epa-swmm-water-quality
    title: Storm Water Management Model Reference Manual, Volume III, Water Quality
    source_type: federal_agency_technical_reference
    authority_tier: epa_technical_reference
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: United States Environmental Protection Agency, Office of Research and Development
    locator: https://nepis.epa.gov/Exe/ZyPDF.cgi/P100P2NY.PDF?Dockey=P100P2NY.PDF
    published_or_effective: 2016-07, EPA/600/R-16/093
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: Modeling reference. Its EMC and residence-time definitions are model definitions and must not be presented as monitoring or permit definitions.

  - source_id: source-nrcs-time-of-concentration
    title: Title 210, National Engineering Handbook, Part 630 Hydrology, Subpart F, Time of Concentration
    source_type: federal_agency_technical_standard
    authority_tier: usda_nrcs_technical_standard
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: United States Department of Agriculture, Natural Resources Conservation Service
    locator: https://directives.nrcs.usda.gov/sites/default/files2/1749749287/Subpart%20F%20%E2%80%93%20Time%20of%20Concentration.pdf
    published_or_effective: Amended June 2025 (210 H 630 Subpart F)
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: An agricultural and watershed hydrology handbook. It supports the definition and the direction of urbanization effects. It does not establish a stormwater permit requirement or a design method for a specific site.

  - source_id: source-cfr-freeboard
    title: 44 CFR 59.1, Definitions, National Flood Insurance Program general provisions
    source_type: federal_regulation
    authority_tier: us_federal_primary_authority
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: Federal Emergency Management Agency
    locator: https://www.govinfo.gov/content/pkg/CFR-2024-title44-vol1/xml/CFR-2024-title44-vol1-sec59-1.xml
    published_or_effective: CFR 2024 edition
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: Defines freeboard for National Flood Insurance Program floodplain management. It is not a stormwater-pond embankment standard and does not set a freeboard value for any practice.

  - source_id: source-epa-ii-estimating-guide
    title: Guide for Estimating Infiltration and Inflow
    source_type: federal_agency_guidance
    authority_tier: epa_regional_guidance_archived
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: United States Environmental Protection Agency, New England (Region 1)
    locator: https://19january2017snapshot.epa.gov/www3/region1/sso/pdfs/Guide4EstimatingInfiltrationInflow.pdf
    published_or_effective: 2014-06
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: Retrieved only from EPA's archived web snapshot. No live www.epa.gov copy was located on 2026-07-27. It is regional outreach guidance for New England conditions, including snowmelt and soil thaw, and is not a national standard. A live current EPA replacement must be sought before publication.
```

Two sources already in `sources.yaml` are reused and need no new record: `source-epa-wet-ponds`
(items 2 and 3) and `source-epa-swmm` (context for the three SWMM reference manuals).

---

## Item 1. Detention time and residence time distinction

**White-paper sentences it must support** (section 2, "Detention time and residence time"):

> **Detention time** is how long water stays in a practice before leaving. Where a distinction is
> drawn, **residence time** usually describes the average time a parcel of water spends in the
> system, while detention time is often used for the interval between inflow and its associated
> outflow. Usage varies between design guides and permits, so the honest instruction is to ask which
> definition the document in front of you is using.

**Proposed claim type:** `technical_standard`

**Sources**

1. EPA, *Stormwater Best Management Practice Design Guide, Volume 1, General Considerations*,
   EPA/600/R-04/121, September 2004. Retrieved 2026-07-27 from
   `https://nepis.epa.gov/Exe/ZyPDF.cgi/901X0A00.PDF?Dockey=901X0A00.PDF`.
   Locator: Glossary, alphabetical entry "Detention Time".
2. EPA, *SWMM Reference Manual Volume III, Water Quality*, EPA/600/R-16/093, July 2016. Retrieved
   2026-07-27 from `https://nepis.epa.gov/Exe/ZyPDF.cgi/P100P2NY.PDF?Dockey=P100P2NY.PDF`.
   Locator: Chapter 5, treatment-expression hydraulic variables, the paragraph defining `HRT`
   immediately before Equation 5-12.

**Supporting passages**

> "Detention Time: The theoretical time required to displace the contents of a stormwater treatment
> facility at a given rate of discharge (volume divided by rate of discharge)." (EPA/600/R-04/121,
> Glossary)

> "The hydraulic residence time is the average time that water has spent within a completely mixed
> storage node." (EPA/600/R-16/093, Chapter 5)

**Scope and limitations**

Both are EPA technical references, not permits or regulations. The 2004 design guide is old enough
that current EPA usage must be checked. The SWMM definition is a model definition for a completely
mixed storage node.

**Verdict: PARTIAL — and it contains a correction the author must act on.**

The two terms are each federally defined, and the fact that usage varies is supportable. But the
white paper assigns the meanings in the opposite direction from EPA's own design-guide glossary. EPA
defines *detention time* as volume divided by discharge rate — a theoretical mean displacement time,
which is the meaning the white paper attributes to *residence time*. Meanwhile SWMM defines
*hydraulic residence time* as an average time in a mixed storage unit, which is nearly the same
quantity under a different name.

So the retrieved federal evidence supports the white paper's honest instruction ("ask which
definition the document in front of you is using") **more strongly** than it supports the specific
distinction the sentence draws. The sentence "detention time is often used for the interval between
inflow and its associated outflow" was not found in any retrieved federal source.

**What a qualified reviewer must confirm**

- Whether to rewrite the sentence so the distinction is presented as unsettled rather than as a rule
  with an assigned direction.
- Whether EPA's `volume / discharge rate` definition should be quoted directly in learner content,
  and whether it needs the word "theoretical" preserved.
- Whether current EPA usage has moved since 2004.

---

## Item 2. Control elevation

**White-paper sentences it must support** (section 3, "Control elevation and littoral zone"):

> The **control elevation** is the water-surface elevation set by the outlet arrangement, the level
> the pond returns toward between storms. It is the reason the pond has a normal appearance at all.
> When people say a pond "looks low" or "looks high," they are making an unstated comparison against
> a control elevation they have not actually seen documented.

**Proposed claim type:** `technical_standard`

**Source**

EPA, *NPDES Stormwater Best Management Practice, Wet Ponds*, Office of Water 4203M, December 2021.
Retrieved 2026-07-27 from
`https://www.epa.gov/system/files/documents/2021-11/bmp-wet-ponds.pdf`.
Locator: page 3, "Maintenance" column, second paragraph. Already registered as
`source-epa-wet-ponds`.

**Supporting passage**

> "A reverse-slope pipe draws from below the permanent pool, extending in a reverse angle up to the
> riser, and establishes the water elevation of the permanent pool."

**Scope and limitations**

This supports the *mechanism* — the outlet arrangement sets the standing water elevation the pond
returns toward — for one specific outlet type in a wet pond. It does not use, define, or endorse the
phrase "control elevation."

**Verdict: PARTIAL. The mechanism is federally anchored. The term is not.**

No federal source defining "control elevation" was located. The only retrieved document using the
term in this sense is a state water management district regulation hosted on epa.gov, which is
excluded by the authority scope (see "Rejected sources"). The term appears to be state regulatory
vocabulary, most prominently Florida's, rather than federal vocabulary.

**What a qualified reviewer must confirm**

- Whether to keep the phrase "control elevation" at all in a national brief, or to teach the
  mechanism using EPA's own words ("the water elevation of the permanent pool") and name "control
  elevation" only as a term the learner may encounter in some jurisdictions.
- If the term is kept, whether it must carry an explicit statement that it is not a federally defined
  term.
- Whether the "looks low / looks high" instructional framing survives the rewrite.

---

## Item 3. Littoral zone

**White-paper sentences it must support** (section 3):

> The **littoral zone** is the shallow, vegetated margin around the edge of a pond. It is sometimes
> provided deliberately for habitat, shoreline stability, or treatment. From a distance it can look
> like a maintenance failure, and a well-intentioned decision to clear it can remove a designed
> feature.

**Proposed claim type:** `technical_standard`

**Source**

EPA, *NPDES Stormwater Best Management Practice, Wet Ponds*, Office of Water 4203M, December 2021.
Retrieved 2026-07-27 from
`https://www.epa.gov/system/files/documents/2021-11/bmp-wet-ponds.pdf`. Already registered as
`source-epa-wet-ponds`.

**Supporting passages**

Locator: page 2, "Design Considerations", right column:

> "Vegetated littoral zones (i.e., nearshore and shallow environments that receive enough sunlight
> to support vegetative growth) can increase vegetation uptake of pollutants and generate greater
> aesthetic appeal."

Locator: page 3, top of right column:

> "In addition, a planted littoral zone or an aquatic bench (i.e., a shallow shelf with wetland
> plants) around the edge can help stabilize the soil at the edge of the pond, enhances habitat and
> aesthetic value, and possibly provide some pollutant uptake."

Locator: maintenance activity table near the end of the fact sheet, annual inspection row:

> "Check for 50% plant survival in the littoral" [zone]

**Scope and limitations**

Federal fact-sheet-level conceptual description. It does not establish a required littoral area, a
required plant list, or a performance credit.

**Verdict: FOUND.**

All three purposes the white paper names — habitat, shoreline stability, treatment — appear
explicitly in the EPA text ("enhances habitat", "help stabilize the soil at the edge of the pond",
"pollutant uptake"). The maintenance table's plant-survival check independently supports the white
paper's teaching point that the littoral zone is a designed feature that can be destroyed by
well-intentioned clearing.

**What a qualified reviewer must confirm**

- That the learner-facing wording does not imply a littoral zone is always present or always
  required.
- That "aquatic bench" is either introduced alongside "littoral zone" or deliberately omitted, since
  EPA presents them together.

---

## Item 4. Infiltration rate vs infiltration capacity, and the runoff-generation comparison

**White-paper sentences it must support** (section 4):

> **Infiltration rate** is the rate at which water is actually entering the surface right now.
> ... **Infiltration capacity** is the maximum rate the surface and the material below it *could*
> accept at that moment if enough water were available. It is a property of the ground and its
> current condition, not of the storm.
> ... When rainfall intensity is below the infiltration capacity, essentially everything can enter
> the ground and little runoff forms. When rainfall intensity exceeds the infiltration capacity, the
> surplus becomes runoff.
> ... Infiltration capacity is not a fixed label for a site. It generally declines during a storm as
> the soil wets up ...

**Proposed claim type:** `sourced_fact`

**Source**

EPA, *SWMM Reference Manual Volume I, Hydrology (Revised)*, EPA/600/R-15/162A, January 2016.
Retrieved 2026-07-27 from
`https://nepis.epa.gov/Exe/ZyPDF.cgi/P100NYRA.PDF?Dockey=P100NYRA.PDF`.

**Supporting passages**

Locator: Chapter 4, Section 4.2.1, the sentence introducing Equation 4-2, and Figure 4-2:

> "Note that actual infiltration will be the lesser of actual rainfall and infiltration capacity:
> f(t) = min(fp(t), i(t))"
> where "f = actual infiltration into the soil" and "i = rainfall intensity".

Figure 4-2, "The Horton infiltration curve", plots the rainfall hyetograph against the declining
`fp` curve and labels the area where rainfall exceeds capacity as "Runoff (shaded areas)".

Locator: Chapter 4, Section 4.2.1, first sentence:

> "Horton (1933, 1940) proposed the following exponential equation to predict the reduction in
> infiltration capacity over time as observed from field measurements".

Locator: Chapter 4, Section 4.1:

> "Engineers have developed several simpler algebraic infiltration models that capture the general
> dependence of infiltration capacity on soil characteristics and the volume of previously
> infiltrated water during the course of a storm event."

Locator: Chapter 4, Section 4.2.2 heading, "Recovery of Infiltration Capacity" — the manual models
capacity regenerating during dry periods, confirming that capacity is a state, not a fixed label.

**Scope and limitations**

This is a modeling reference. It documents how a widely used federal model represents infiltration
and cites the field basis (Horton) for the declining-capacity form. It does not establish a
measurement protocol or an acceptable rate for any site, which is consistent with the white paper's
own refusal to give a universal acceptable rate.

**Verdict: FOUND.**

Every element is covered: the rate-versus-capacity distinction (`f = min(fp, i)`), the
runoff-generation comparison (Figure 4-2 shaded runoff areas), and the declining-capacity statement
(Horton's exponential reduction, and the dependence on previously infiltrated water).

**What a qualified reviewer must confirm**

- That presenting a model formulation as a physical explanation is acceptable for a concept brief,
  and that the learner-facing text says so.
- That the white paper's longer list of things that change capacity over months and years
  (compaction, sediment accumulation, construction disturbance, groundwater level, vegetation,
  maintenance) is either separately sourced or is clearly marked as practitioner framing. SWMM
  Volume I covers within-storm decline and between-storm recovery; it does not enumerate that
  multi-year list.

---

## Item 5. Hydraulic conductivity as distinct from infiltration capacity

**White-paper sentences it must support** (section 4):

> **Hydraulic conductivity** describes how readily a saturated material transmits water through
> itself. It is a property of the material rather than a description of a surface accepting water,
> so it is not a synonym for infiltration capacity even though the two are related and are often
> measured to support the same decision.

**Proposed claim type:** `sourced_fact`

**Source**

EPA, *SWMM Reference Manual Volume I, Hydrology (Revised)*, EPA/600/R-15/162A, January 2016.
Retrieved 2026-07-27 from
`https://nepis.epa.gov/Exe/ZyPDF.cgi/P100NYRA.PDF?Dockey=P100NYRA.PDF`.

**Supporting passages**

Locator: Chapter 4, Section 4.4, the paragraph introducing Equation 4-26:

> "The water velocity within the wetted zone is given by Darcy's Law as a function of the saturated
> hydraulic conductivity Ks, the capillary suction head along the wetting front ψs, the depth of
> ponded water at the surface d, and the depth of the saturated layer below the surface Ls".

Locator: Chapter 4, Equation 4-27, the Green-Ampt equation:

> `fp = Ks (1 + ψs θd / F)`

which makes infiltration capacity `fp` a *function of* `Ks` together with the soil's current moisture
state, and therefore not the same quantity.

Locator: Chapter 4, parameter-estimation discussion, "Minimum Infiltration Capacity (f∞)":

> "The Horton parameter f∞ is essentially equal to saturated hydraulic conductivity, Ks, that is,
> f∞ ≈ Ks."

Locator: same discussion, immediately preceding:

> "Note that saturated hydraulic conductivity is the more appropriate word for parameter Ks, also
> termed 'permeability' on older soil survey interpretation tables."

**Scope and limitations**

Modeling reference, not a soil-testing standard. It establishes the relationship between the two
quantities inside two named infiltration models.

**Verdict: FOUND.**

The distinction the white paper draws is exactly what the equations show: `Ks` is the material's
saturated transmission property and the *limiting* value that infiltration capacity decays toward;
`fp` is the surface's current acceptance capacity. "Related but not synonymous" is precisely the
relationship `f∞ ≈ Ks` and `fp = Ks(1 + ψs θd / F)` describe.

**What a qualified reviewer must confirm**

- Whether the brief should also carry a soil-science definition from USDA NRCS or USGS rather than
  resting on a modeling reference alone. A USGS Circular 1186 page was attempted on 2026-07-27 and
  returned HTTP 403; no USGS definition was retrieved, so none is claimed here.
- Whether the learner-facing text should mention that older soil survey tables call this
  "permeability", since practitioners will encounter that word.

---

## Item 6. Freeboard

**White-paper sentences it must support** (section 6):

> **Freeboard** is the vertical distance between the highest water surface expected under a stated
> condition and the top of a containing structure such as an embankment or wall. It is deliberate
> margin. Its purpose is to absorb the difference between what was analyzed and what actually
> happens: wave action, settlement, debris at an outlet, a storm larger than the one evaluated, or an
> assumption that turned out to be optimistic.

**Proposed claim type:** `technical_standard`

**Sources**

1. 44 CFR 59.1, Definitions (National Flood Insurance Program general provisions), FEMA. Retrieved
   2026-07-27 from
   `https://www.govinfo.gov/content/pkg/CFR-2024-title44-vol1/xml/CFR-2024-title44-vol1-sec59-1.xml`.
   Locator: alphabetical definition "Freeboard".
2. EPA, *Stormwater BMP Design Guide, Volume 1*, EPA/600/R-04/121, September 2004. Retrieved
   2026-07-27 from `https://nepis.epa.gov/Exe/ZyPDF.cgi/901X0A00.PDF?Dockey=901X0A00.PDF`.
   Locator: Glossary, entry "Freeboard (Hydraulics)".

**Supporting passages**

> "Freeboard means a factor of safety usually expressed in feet above a flood level for purposes of
> flood plain management." (44 CFR 59.1, retrieved verbatim from the govinfo XML)

The published regulation continues, per the same definition: freeboard "tends to compensate for the
many unknown factors that could contribute to flood heights greater than the height calculated for a
selected size flood and floodway conditions, such as wave action, bridge openings, and the
hydrological effect of urbanization of the watershed." **Verifier note:** the govinfo fetch returned
the first sentence verbatim; the second sentence was returned by web search rather than by the
retrieval, so the verifier must open 44 CFR 59.1 directly and confirm the full text before it is
quoted in learner content.

> "Freeboard (Hydraulics): The distance between the maximum water surface elevation anticipated in
> design and the top of retaining banks or structures. Freeboard is provided to prevent overtopping
> due to unforeseen conditions." (EPA/600/R-04/121, Glossary)

**Scope and limitations**

44 CFR 59.1 is current federal regulation but defines freeboard for NFIP floodplain management, not
for stormwater pond embankments. EPA/600/R-04/121 gives the hydraulic-structure definition the white
paper actually uses, but is a 2004 technical report. Neither sets a freeboard value for any practice,
and the white paper does not assert one.

**Verdict: FOUND.**

The EPA glossary definition is close to word-for-word what the white paper says, including the
containing-structure framing and the "unforeseen conditions" purpose. 44 CFR 59.1 supplies the
current-regulation anchor for "deliberate margin" as a factor of safety compensating for unknown
factors, and names wave action and urbanization explicitly.

**What a qualified reviewer must confirm**

- Whether pairing a floodplain-management regulation with a stormwater technical glossary is
  acceptable, or whether the brief should rest on the EPA glossary alone with 44 CFR 59.1 as context.
- The full verbatim text of 44 CFR 59.1 "Freeboard" (see verifier note above).
- Whether the white paper's added examples — settlement, debris at an outlet — need their own source
  or should be marked as practitioner illustration. Neither source names those two.

---

## Item 7. Tailwater and its effect on outlet release

**White-paper sentences it must support** (section 6):

> **Tailwater** is the water level in the receiving system just downstream of an outlet. It matters
> because an outlet does not discharge into empty air. It discharges into whatever is already there.
>
> When the downstream water level rises, the difference in level across the outlet shrinks, and the
> outlet releases water more slowly than it would into a low downstream condition.

**Proposed claim type:** `sourced_fact`

**Sources**

1. EPA, *Stormwater BMP Design Guide, Volume 1*, EPA/600/R-04/121, September 2004. Retrieved
   2026-07-27 from `https://nepis.epa.gov/Exe/ZyPDF.cgi/901X0A00.PDF?Dockey=901X0A00.PDF`.
   Locator: Glossary, entry "Tailwater". *(definition)*
2. EPA, *SWMM Reference Manual Volume II, Hydraulics*, EPA/600/R-17/111, 2017. Retrieved 2026-07-27
   from `https://nepis.epa.gov/Exe/ZyPDF.cgi/P100S9AS.PDF?Dockey=P100S9AS.PDF`.
   Locator: Section 6.2 (Orifices), Section 6.2.2 "Effective Head (He)" including Equations 6-5 and
   6-6 and Figure 6-2; Section 6.2.3 subheading "Tailwater Submergence Correction" with Equation
   6-13; Section 6.3.4 "Submerged Weir Flow" with Equation 6-26 and Figure 6-6. *(mechanism)*

**Supporting passages**

> "Tailwater: Water, in a river or channel, immediately downstream from a structure."
> (EPA/600/R-04/121, Glossary)

> "Orifices are regularly shaped, submerged openings through which flow is proportional to the square
> root of the head across the opening. Orifices are typically used to: regulate flow out of detention
> ponds and other storage facilities ..." (EPA/600/R-17/111, Section 6.2)

> "The effective head across the orifice depends on whether the water level on its outflow side is
> below the orifice opening or not." (EPA/600/R-17/111, Section 6.2.2)

Equations 6-5 and 6-6 then set the effective head to `H1 − H2` — upstream head minus downstream head
— whenever the downstream level `H2` is above the orifice, rather than to the upstream head alone.
Because flow is proportional to the square root of that effective head (Equation 6-3, Torricelli),
a rising downstream level directly reduces the release rate.

> "As shown in Figure 6-6, submerged weir flow occurs when the water level on the downstream side of
> the weir (H2) is above the crest elevation (ZW). Under this condition weir flow is related not only
> to the head on the upstream side of the weir (H1) but also to H2 and ZW ..."
> (EPA/600/R-17/111, Section 6.3.4)

The Villemonte submergence factor `fS = [1 − (H2/H1)^n]^0.385` (Equation 6-26, and Equation 6-13 for
orifices behaving as weirs) is a multiplier less than one, so submergence reduces computed discharge.

**Scope and limitations**

The definition is from a 2004 technical report; the mechanism is from a current EPA modeling
reference and is stated as model formulation, not as a prediction for a real outlet. Neither source
addresses the white paper's diagnostic advice about inspection.

**Verdict: FOUND.**

The direction and mechanism are exactly as the white paper states, for both of the outlet types a
storage practice actually uses (orifice and weir), and SWMM explicitly names "flow out of detention
ponds" as the use case.

**What a qualified reviewer must confirm**

- That the learner-facing explanation stops at direction and mechanism and does not imply a
  predictable magnitude.
- The white paper's operational advice — "Before concluding that an outlet is blocked, it is worth
  asking what the receiving water was doing at the same time" — is a practitioner inference. Neither
  retrieved source states it. A qualified stormwater practitioner must accept or reject it, and it
  should probably be classified separately as `expert_interpretation`.
- Whether a current FHWA hydraulic source should be added. FHWA HEC-22 4th edition (FHWA-HIF-24-006,
  2024) could not be retrieved on 2026-07-27 because the file exceeds the fetch size limit; the 3rd
  edition was retrieved but is stamped "Archival Superseded by HEC-22 4th Edition" and is therefore
  not proposed as a source.

---

## Item 8. Time of concentration, and the effect of development on travel time

**White-paper sentences it must support** (section 7):

> **Time of concentration** is the time it takes for water to travel from the most hydraulically
> distant part of a drainage area to the point being studied. It is the reason a hydrograph has a
> shape at all rather than being a single spike.
>
> ... Development often shortens this travel time, because water moves faster over pavement and
> through smooth pipes than across grass and soil. When water from the whole area arrives at the
> outlet in a shorter window, it arrives more concentrated in time, and the peak rises even if the
> total amount of water had not changed.

**Proposed claim type:** `sourced_fact`

**Source**

USDA NRCS, *Title 210, National Engineering Handbook, Part 630 Hydrology, Subpart F, Time of
Concentration*, amended June 2025. Retrieved 2026-07-27 from
`https://directives.nrcs.usda.gov/sites/default/files2/1749749287/Subpart%20F%20%E2%80%93%20Time%20of%20Concentration.pdf`.

**Supporting passages**

Locator: paragraph D.1 ("Time of Concentration"):

> "Time of concentration (Tc) is the time required for runoff to travel from the hydraulically most
> distant point in the watershed to the outlet. The hydraulically most distant point is the point
> with the longest travel time to the watershed outlet, and not necessarily the point with the
> longest flow distance to the outlet."

Locator: 630.70 Introduction:

> "This subpart contains information on the watershed characteristics called travel time, lag, and
> time of concentration. These watershed characteristics influence the shape and peak of the runoff
> hydrograph."

Locator: paragraph F ("Effects of Urbanization"), F.1 "Surface Roughness":

> "One of the most significant effects of urban development on overland flow is the lowering of
> retardance to flow causing higher velocities. Undeveloped areas with very slow and shallow overland
> flow (sheet flow and shallow concentrated flow) through vegetation become modified by urban
> development. Flow is then delivered to streets, gutters, and storm sewers that transport runoff
> downstream more rapidly. Travel time through the watershed is generally decreased."

Locator: paragraph F.2 "Channel Shape and Flow Patterns":

> "Typically, urbanization reduces overland flow lengths by conveying storm runoff into a channel as
> soon as possible. Since constructed channel designs have efficient hydraulic characteristics,
> runoff flow velocity increases and travel time decreases."

A secondary corroborating definition is available in EPA/600/R-04/121's glossary: "Time of
Concentration: The time period necessary for surface runoff to reach the outlet of a subbasin from
the most remote point hydraulically in the tributary drainage area."

**Scope and limitations**

An agricultural and watershed hydrology handbook. It supports the definition, the hydrograph-shaping
role, and the direction of the urbanization effect. It does not establish a stormwater permit
requirement and does not authorize a computation for any particular site.

**Verdict: FOUND. This is the strongest and most current anchor in the dossier.**

Note the handbook adds a useful precision the white paper currently lacks: the hydraulically most
distant point is the one with the *longest travel time*, "not necessarily the point with the longest
flow distance."

**What a qualified reviewer must confirm**

- Whether to adopt the travel-time-not-distance precision into the learner text.
- The white paper's final clause — "the peak rises even if the total amount of water had not changed"
  — is a reasonable consequence of shorter travel time, but paragraph F states the travel-time
  decrease, not that specific peak statement. A reviewer should confirm whether it needs its own
  source (NRCS Subpart G, "Hydrographs", is the likely place) or should be softened.
- That using an NRCS agricultural-hydrology handbook in an urban stormwater brief is acceptable, and
  that the brief says which document it is drawing on.

---

## Item 9. Downstream peak coincidence from combined delayed releases

**White-paper sentences it must support** (section 8, "When delay is not a benefit"):

> Detention delays a discharge. Downstream, flows from many contributing areas combine, and each one
> arrives on its own schedule. If a site's release is delayed into the moment when flow from the rest
> of the watershed is already passing, the delayed release can add to a peak instead of missing it.
> Each individual basin can meet its own release condition at its own outlet while the combined
> effect at a downstream point is no better, and in some arrangements worse, than it would have been
> without the delay.

**Proposed claim type:** `sourced_fact` — proposed **upgrade** from the white paper's current
`expert_interpretation`, with qualified review still required.

**Source**

EPA, *Stormwater Best Management Practice Design Guide, Volume 1, General Considerations*,
EPA/600/R-04/121, September 2004. Retrieved 2026-07-27 from
`https://nepis.epa.gov/Exe/ZyPDF.cgi/901X0A00.PDF?Dockey=901X0A00.PDF`.

**Supporting passages**

Locator: Chapter 4, page 4-18, the bulleted generalizations immediately following Figures 4-5 and
4-6:

> "Enough studies have been conducted and reported that the following generalizations can be drawn
> from them:
> - Some watershed-wide systems of detention basins help, in the sense that they keep downstream peak
>   discharges during a given storm lower than it would be without them.
> - Other individual basins do the opposite of lessening the discharge; they actually increase
>   downstream peak discharges as a result of the overlapping of their detained volumes with
>   mainstream peaks.
> - No watershed-wide system of uniform basins works to the extent for which they were designed. ...
>   their aggregate effect, although it may result in a reduction in peak discharge, is usually not a
>   reduction to the designed degree because of the accumulation of runoff volumes downstream."

Locator: Chapter 4, page 4-19, "Channel Instability, Bank Erosion and Sediment Transport":

> "Peak discharge control strategies using detention ponds do not eliminate runoff, they simply delay
> it. The volume discharging from a detention basin is the same as the inflow. When the post
> development volumes from different tributaries join downstream, there is nothing to prevent them
> from combining to produce inadvertently high peak rates."

The same chapter also supports the white paper's remedy — that the question is answered with
watershed-scale analysis, not by inspecting a basin — in its "Downstream Analysis" subsection.

**Scope and limitations**

EPA states these as generalizations drawn from a body of studies, not as a universal rule, and
explicitly notes that selectively located detention basins *can* reduce flood peaks (citing the Miami
Conservancy District example). The report is from 2004. Its Figures 4-5 and 4-6 are reproduced from
Ferguson (1998) with permission, so those figures are copyrighted third-party material and must not
be reproduced in OWOS visuals.

**Verdict: FOUND. This was flagged as the highest-review-priority item and it turns out to be
directly and almost word-for-word supported by an EPA technical report.**

**What a qualified reviewer must confirm**

- That the learner-facing text preserves EPA's balance. EPA says *some* systems help and *others* do
  the opposite; it does not say detention generally worsens downstream peaks. The white paper's
  framing ("This is not an argument against detention") is consistent with EPA, and must stay.
- Whether 2004 EPA generalizations are current enough to teach, or whether a newer federal source
  should be sought.
- FHWA HEC-22 3rd edition Section 8.2.1 "Release Timing" states the same mechanism in almost
  identical terms, but that edition is stamped archival and superseded; the 4th edition
  (FHWA-HIF-24-006, 2024) exceeded the retrieval size limit on 2026-07-27 and was not read. A
  verifier with direct PDF access should confirm the equivalent 4th-edition section and consider
  adding it as a current corroborating source.
- Qualified stormwater and watershed review is still required. The upgrade to `sourced_fact` covers
  the mechanism, not the white paper's instructional advice about which question a non-designer
  should ask.

---

## Item 10. Event mean concentration as the concentration term in the load relationship

**White-paper sentences it must support** (section 8, "Concentration, volume, and load"):

> `Pollutant load = discharged water volume x event mean concentration`
>
> The qualifier matters. Concentration is not constant during a storm, so a single number multiplied
> by a volume has to be a concentration that represents the event as a whole. That flow-weighted
> average is what practitioners call an **event mean concentration**, usually shortened to EMC. A
> single grab sample taken at one moment is not an EMC ...

**Proposed claim type:** `sourced_fact`

**Sources**

1. EPA, *Stormwater BMP Design Guide, Volume 1*, EPA/600/R-04/121, September 2004. Retrieved
   2026-07-27 from `https://nepis.epa.gov/Exe/ZyPDF.cgi/901X0A00.PDF?Dockey=901X0A00.PDF`.
   Locator: Glossary, entry "Event Mean Concentration (EMC)"; and Appendix D, subsection "Event Mean
   Concentrations", page D-3.
2. EPA, *SWMM Reference Manual Volume III, Water Quality*, EPA/600/R-16/093, July 2016. Retrieved
   2026-07-27 from `https://nepis.epa.gov/Exe/ZyPDF.cgi/P100P2NY.PDF?Dockey=P100P2NY.PDF`.
   Locator: Section 4.2.3 "EMC Washoff".

**Supporting passages**

> "Event Mean Concentration (EMC): The EMC is a statistical parameter used to represent the
> flow-proportional average concentration of a given parameter during a storm event. It is defined as
> the total constituent mass divided by the total runoff volume. When combined with flow measurement
> data, the EMC can be used to estimate the pollutant loading from a given storm."
> (EPA/600/R-04/121, Glossary)

> "Because of the variability of measurements within storms, among different storms at one site and
> among sites it was desirable to use a measure that tended to reduce this variability somewhat. The
> measure of the magnitude of urban runoff pollution chosen is termed the Event Mean Concentration
> (EMC)." (EPA/600/R-04/121, Appendix D, page D-3)

> "EMC values are usually measured by laboratory analysis of flow- and time-weighted composite
> samples. EMCs are often the only samples available, in order to save on laboratory costs that would
> be involved in measurements of several points along the storm hydrograph ..."
> (EPA/600/R-16/093, Section 4.2.3)

**Scope and limitations**

Both are EPA technical references. The 2004 glossary definition is the load-relationship anchor; the
2016 SWMM manual is the anchor for how EMCs are physically obtained. Neither is a monitoring
regulation, and neither authorizes a load estimate for any real site — consistent with the white
paper's own "Where this stops" boundary.

**Verdict: FOUND.**

The glossary definition supplies all three parts of the white-paper sentence: EMC is a
flow-proportional average over the event, it equals total mass divided by total runoff volume, and
combining it with flow data estimates load. That is the load relationship stated in reverse.

**What a qualified reviewer must confirm**

- The white paper's negative claim — "a single grab sample taken at one moment is not an EMC" — is a
  correct logical consequence of "flow-proportional average ... total constituent mass divided by the
  total runoff volume", but is not stated as such in either source. Confirm whether it needs its own
  source or can be presented as a restatement.
- Whether to note EPA's own reason for choosing the measure (reducing within-storm and between-storm
  variability), which strengthens the white paper's teaching point.
- Whether the existing `source-epa-performance` (Three Keys to BMP Performance) should still carry the
  load explanation. That page was re-read on 2026-07-27 and does **not** use the term "event mean
  concentration"; it says only that total load can be calculated from discharged volume multiplied by
  "the mean or average concentration". The EMC term itself must come from the sources above.

---

## Item 11. First flush as a variable phenomenon rather than a universal rule

**White-paper sentences it must support** (section 8, "First flush"):

> The idea is intuitive and it is genuinely useful for explaining why capturing early runoff can be
> valuable. It is also frequently overstated. Whether a meaningful first flush occurs depends on the
> pollutant, the surface, the drainage area size, the antecedent dry period, and the storm itself.
> Some sites and some pollutants show it clearly. Others do not. Treat it as a phenomenon that may be
> present rather than a rule that always applies.

**Proposed claim type:** `sourced_fact`

**Sources**

1. EPA, *Stormwater BMP Design Guide, Volume 1*, EPA/600/R-04/121, September 2004. Retrieved
   2026-07-27 from `https://nepis.epa.gov/Exe/ZyPDF.cgi/901X0A00.PDF?Dockey=901X0A00.PDF`.
   Locator: Chapter 4, page 4-10, subsection "First Flush".
2. EPA, *SWMM Reference Manual Volume III, Water Quality*, EPA/600/R-16/093, July 2016. Retrieved
   2026-07-27 from `https://nepis.epa.gov/Exe/ZyPDF.cgi/P100P2NY.PDF?Dockey=P100P2NY.PDF`.
   Locator: Chapter 2, the paragraph accompanying Table 2-12 on required temporal detail.

**Supporting passages**

> "The tendency for solids and associated constituents to be washed off of paved areas during the
> initial portion of the storm event is referred to as the first flush ... In general, the potential
> for first flush is determined by the storm characteristics, the size of the subwatershed and the
> partitioning characteristics of the pollutants of concern." (EPA/600/R-04/121, page 4-10)

> "Working with a very small (300 m2) highway segment, Sansalone, et al. (1994) found a pronounced
> first flush for solids, dissolved zinc and dissolved copper, but not dissolved lead. The first
> flush for the particulate-bound fractions of these metals was not well defined."
> (EPA/600/R-04/121, page 4-10)

> "For example, a storage device may need to trap the 'first flush' of pollutants, if one exists."
> (EPA/600/R-16/093, Chapter 2 — note the conditional clause)

**Scope and limitations**

EPA/600/R-04/121 is a 2004 technical report and the Sansalone result is a single very small highway
site, which is itself an argument for treating first flush as site-dependent rather than universal.
Neither source says first flush "does not occur"; both say its occurrence is determined by
conditions.

**Verdict: FOUND.**

EPA names three of the five dependencies the white paper lists — storm characteristics, subwatershed
size, and pollutant partitioning — and then gives a worked instance where the effect was pronounced
for three constituents and absent for a fourth in the same runoff. SWMM's "if one exists" is an
independent federal statement of conditionality. Together they support "a phenomenon that may be
present rather than a rule that always applies".

**What a qualified reviewer must confirm**

- The white paper also names "the surface" and "the antecedent dry period" as dependencies. Neither
  retrieved source states those two. Confirm whether to source them separately or drop them.
- Whether a single 1994 highway study is an appropriate illustration for a national concept brief, or
  whether the brief should state the variability without the specific example.
- Whether more recent federal monitoring evidence exists. A targeted search of usgs.gov on 2026-07-27
  did not return a USGS report making this finding directly; the search returned an unrelated US
  patent whose background text stated it, which was rejected as not being federal technical
  authority.

---

## Item 12. Wet-weather response shape as a signature separating inflow from infiltration

> **SUPERSEDED 2026-07-27.** This item's verdict has been overtaken by
> `ii-authority-verification.md`. The archived Region 1 source below is dropped entirely and is
> retained here only as the record of what was first attempted. The claim as originally written was
> definitionally wrong: 40 CFR 35.2005(b)(20) and (21) state that infiltration and inflow are each
> distinguished from the other. The reason response shape cannot separate them is different and
> better sourced, and is set out in the verification file. Do not cite anything in this item.

**White-paper sentences it must support** (section 10, worked example "separating two things that
arrive together"):

> The two mechanisms have different signatures in time. Inflow is a surface connection, so it appears
> while it is raining and it falls away quickly once the rain stops. Infiltration comes from water
> that first entered the ground, so it tends to build more slowly, to persist for days after the
> rain, and to track seasonal groundwater conditions. A flow record plotted against rainfall will
> therefore look different in the two cases: a sharp response that ends with the storm points one
> way, and an elevated baseline that decays over days points the other.

**Proposed claim type:** `expert_interpretation` — retained, not upgraded.

**Source**

EPA New England (Region 1), *Guide for Estimating Infiltration and Inflow*, June 2014. Retrieved
2026-07-27 from
`https://19january2017snapshot.epa.gov/www3/region1/sso/pdfs/Guide4EstimatingInfiltrationInflow.pdf`.

**Supporting passages**

Locator: "Background", definitions list, page 4 area, entries "Direct Inflow Volume" and "Delayed
Inflow volume":

> "Direct Inflow Volume - The portion of total inflow volume which is from direct connections to the
> collection system such as catch basins, roof leaders, manhole covers, etc. These inflow sources
> allow stormwater runoff to rapidly impact the collection system."

> "Delayed Inflow volume - The portion of total inflow which is generated from indirect connections
> to the collection system or connections which produce inflow after a significant time delay from
> the beginning of a storm. Delayed inflow sources include: sump pumps, foundation drains, indirect
> sewer/drain cross-connections, etc. **Rainfall-induced infiltration cannot be distinguished from
> delayed inflow and is therefore included as part of delayed inflow.** Delayed inflow sources have a
> gradual impact on the collection system and flow decreases gradually upon conclusion of the rainfall
> event, and after peak inflow caused by direct connections." (emphasis added)

Locator: main text, "Estimating Wet Weather Inflow" section:

> "Direct inflow is the portion of the inflow which rapidly increases soon after the start of the
> storm and decreases swiftly upon conclusion of the event."

> "Delayed inflow is the portion of the inflow which decreases gradually upon conclusion of the storm
> and after the peak inflow caused by direct connections."

Locator: definitions list:

> "Groundwater Infiltration (GWI) – Measured during average dry weather flow period ... The average
> of the low nighttime flows (midnight to 6 am) per day"; "Peak Infiltration - The highest nighttime
> (midnight to 6 am) flow during high groundwater (usually in early spring)."

Locator: main text: "During seasonal high groundwater, which usually occurs after snow melt and soil
thaw, infiltration [is] at its highest."

The document also contains "Figure 1: Hydrograph helps visualize inflow as the response to wet
weather flow (from MassDEP 1993)" — note that the figure is credited to a **state** agency and is
therefore excluded from OWOS use.

**Scope and limitations**

- Retrieved only from EPA's archived web snapshot. No live www.epa.gov copy was found on 2026-07-27.
- Regional outreach guidance written for New England, with seasonal reasoning built on snowmelt and
  soil thaw. Not a national standard, and its seasonal framing does not transfer cleanly to warm
  climates.
- Its purpose is estimating I&I volumes from treatment-plant influent records, not diagnosing which
  defect to fix.

**Verdict: PARTIAL — and, like item 1, it carries a correction.**

EPA does support the substance: a rapid response that ends with the storm versus a gradual response
that decays afterward, plus a separately measured groundwater-infiltration baseline that peaks with
seasonal high groundwater. Those are exactly the two shapes the white paper describes.

But EPA draws the line in a different place. EPA's sharp-versus-gradual distinction separates
**direct inflow** from **delayed inflow**, and states explicitly that *rainfall-induced infiltration
cannot be distinguished from delayed inflow*. In the white paper, the gradual, days-long response is
attributed to **infiltration**. On EPA's terms, that gradual response is delayed inflow — which
includes rainfall-induced infiltration but also includes sump pumps, foundation drains, and indirect
cross-connections, all of which are inflow sources with different remedies.

This matters directly to the worked example's premise. The white paper's two competing hypotheses are
"direct connections such as roof leaders and area drains" versus "groundwater entering through pipe
defects". EPA's framing implies a third possibility sitting in the middle — sump pumps and foundation
drains — that produces the slow, persistent signature while still being an inflow problem.

**What a qualified reviewer must confirm**

- Whether the worked example must be rewritten so the shape distinction separates *direct* from
  *delayed* response rather than *inflow* from *infiltration*, and so delayed inflow sources are named.
- Whether the white paper's conclusion — "The shape of the wet-weather response over time is evidence
  that helps separate the two" — survives that rewrite, or must be weakened to "helps narrow the
  question".
- Whether the brief can rely on an archived regional EPA document at all, or whether a live, current,
  national EPA source must be found first. This is a gating question for publication.
- The existing `claim_type: expert_interpretation` should be kept. Qualified collection-system review
  remains required, and this item should not move to `sourced_fact`.

---

## Rejected sources

Recorded so the exclusions are auditable.

| Candidate | Why it surfaced | Why rejected |
| --- | --- | --- |
| "Regulation of Stormwater Management Systems", hosted at `https://www.epa.gov/sites/default/files/2015-12/documents/nps-ordinanceuments-st-johns-wmdfl.pdf` | The only retrieved document that uses "control elevation" in the white paper's sense, including the littoral-zone-to-surface-area ratio "at the control elevation" | It is a Florida water management district rule reproduced on epa.gov. State requirements are excluded from public Concept Brief authority statements, claims, citations, comparisons, and Graph evidence. Hosting on epa.gov does not convert a state rule into federal authority. |
| FHWA HEC-22, *Urban Drainage Design Manual*, Third Edition, FHWA-NHI-10-009 (2009, rev. 2013) | Section 8.2.1 "Release Timing" states the downstream peak-coincidence mechanism almost exactly as the white paper does; Section 5.2.4 defines channel freeboard; Chapter 8 covers tailwater submergence of weirs and orifices | The retrieved PDF is stamped "Archival Superseded by HEC-22 4th Edition - February 2024" on its first page. Superseded guidance is not current federal authority. Retained here only as a lead for the verifier. |
| FHWA HEC-22 Fourth Edition, FHWA-HIF-24-006 (2024) | The current edition, and the correct source if it retains the sections above | Could not be retrieved on 2026-07-27: the PDF (12.3 MB per FHWA's own library page) exceeds the fetch size limit, and FHWA offers no chapter-level or HTML version. The DOT ROSAP mirror returned HTTP 403. **Nothing from the 4th edition is cited anywhere in this dossier**, because nothing from it was read. |
| US patent background text asserting first-flush variability | Appeared in search results with wording close to the white paper's claim | Patent background sections are not federal technical authority. |
| "Stormwater Wet Pond and Wetland Management Guidebook" (`https://www.epa.gov/sites/default/files/2015-11/documents/pondmgmtguide.pdf`) | Uses both "residence time" and "detention time" | Authored by the Center for Watershed Protection under EPA contract. It uses both terms but defines neither, so it adds nothing to item 1. Its authorship also needs a tier decision before it is used at all. |
| USGS Circular 1186, "General Facts and Concepts about Ground Water" | Candidate plain-language hydraulic conductivity definition for item 5 | `https://pubs.usgs.gov/circ/circ1186/html/gen_facts.html` returned HTTP 403 on 2026-07-27. Not read, therefore not cited. |
| USGS Water Science School, "Infiltration and the Water Cycle" | Candidate anchor for item 4 | Retrieved and read on 2026-07-27. It supports the wet-soil effect ("soil already saturated from previous rainfall can't absorb much more ... thus more rainfall will become surface runoff") but does **not** define infiltration capacity or state the rainfall-intensity-exceeds-capacity comparison. Kept out of the item 4 record to avoid over-claiming; may be added as a plain-language supplement if the reviewer wants one. |

---

## Retrieval log

Every URL below was fetched and its content read on **2026-07-27**.

| Source | URL | Outcome |
| --- | --- | --- |
| EPA Stormwater BMP Design Guide Vol 1 (EPA/600/R-04/121) | `https://nepis.epa.gov/Exe/ZyPDF.cgi/901X0A00.PDF?Dockey=901X0A00.PDF` | Read; used for items 1, 6, 7, 8, 9, 10, 11 |
| EPA SWMM Reference Manual Vol I Hydrology (EPA/600/R-15/162A) | `https://nepis.epa.gov/Exe/ZyPDF.cgi/P100NYRA.PDF?Dockey=P100NYRA.PDF` | Read; used for items 4, 5 |
| EPA SWMM Reference Manual Vol II Hydraulics (EPA/600/R-17/111) | `https://nepis.epa.gov/Exe/ZyPDF.cgi/P100S9AS.PDF?Dockey=P100S9AS.PDF` | Read; used for item 7 |
| EPA SWMM Reference Manual Vol III Water Quality (EPA/600/R-16/093) | `https://nepis.epa.gov/Exe/ZyPDF.cgi/P100P2NY.PDF?Dockey=P100P2NY.PDF` | Read; used for items 1, 10, 11 |
| EPA NPDES BMP fact sheet, Wet Ponds | `https://www.epa.gov/system/files/documents/2021-11/bmp-wet-ponds.pdf` | Read; used for items 2, 3 |
| EPA NPDES BMP fact sheet, Dry Detention Ponds | `https://www.epa.gov/system/files/documents/2021-11/bmp-dry-detention-ponds.pdf` | Read; uses "detention time" but does not define it; not cited |
| EPA Three Keys to BMP Performance | `https://www.epa.gov/npdes/three-keys-bmp-performance-concentration-volume-and-total-load` | Re-read; confirmed it does **not** contain "event mean concentration" or "first flush" |
| EPA New England, Guide for Estimating Infiltration and Inflow (2014) | `https://19january2017snapshot.epa.gov/www3/region1/sso/pdfs/Guide4EstimatingInfiltrationInflow.pdf` | Read; used for item 12; archived snapshot only |
| EPA Urban Storm Water Preliminary Data Summary, part B | `https://www.epa.gov/sites/default/files/2015-10/documents/usw_b.pdf` | Read; contains EMC tables but no first-flush variability statement; not cited |
| EPA Stormwater Wet Pond and Wetland Management Guidebook | `https://www.epa.gov/sites/default/files/2015-11/documents/pondmgmtguide.pdf` | Read; rejected (see above) |
| USDA NRCS 210-NEH Part 630 Subpart F, Time of Concentration (June 2025) | `https://directives.nrcs.usda.gov/sites/default/files2/1749749287/Subpart%20F%20%E2%80%93%20Time%20of%20Concentration.pdf` | Read; used for item 8 |
| 44 CFR 59.1 Definitions (CFR 2024 edition, govinfo) | `https://www.govinfo.gov/content/pkg/CFR-2024-title44-vol1/xml/CFR-2024-title44-vol1-sec59-1.xml` | Read; used for item 6 (first sentence verbatim; see verifier note) |
| USGS Water Science School, Infiltration and the Water Cycle | `https://www.usgs.gov/water-science-school/science/infiltration-and-water-cycle` | Read; not cited (see rejected sources) |
| FHWA HEC-22 3rd edition (FHWA-NHI-10-009) | `https://www.fhwa.dot.gov/engineering/hydraulics/pubs/10009/10009.pdf` | Read; rejected as superseded/archival |
| FHWA HDS-4, Introduction to Highway Hydraulics | `https://www.fhwa.dot.gov/engineering/hydraulics/pubs/08090/HDS4_608.pdf` | Read; tailwater content is storm-drain-outfall specific and adds nothing beyond SWMM Vol II; not cited |
| FHWA HEC-22 4th edition (FHWA-HIF-24-006) | `https://www.fhwa.dot.gov/engineering/hydraulics/pubs/hif24006.pdf` | **Not retrieved** — exceeds fetch size limit. Nothing from it is cited. |
| FHWA HDS-5 3rd edition (FHWA-HIF-12-026) | `https://www.fhwa.dot.gov/engineering/hydraulics/pubs/12026/hif12026.pdf` | **Not retrieved** — exceeds fetch size limit. Nothing from it is cited. |
| USGS Circular 1186, General Facts and Concepts about Ground Water | `https://pubs.usgs.gov/circ/circ1186/html/gen_facts.html` | **Not retrieved** — HTTP 403. Nothing from it is cited. |
| eCFR 44 CFR 59.1 | `https://www.ecfr.gov/current/title-44/chapter-I/subchapter-B/part-59/subpart-A/section-59.1` | **Not retrieved** — redirected off-host to an access-control page; not followed. The govinfo copy was used instead. |
| NRCS Conservation Practice Standard 378, Pond | `https://www.nrcs.usda.gov/sites/default/files/2022-09/Pond_378_NHCP_CPS_2022.pdf` | **Not retrieved** — repeated timeouts. Nothing from it is cited. |
| NRCS Conservation Practice Standard 587, Structure for Water Control | `https://www.nrcs.usda.gov/sites/default/files/2022-10/Structure_for_Water_Control_587_CPS_Oct_2017.pdf` | **Not retrieved** — timeout. Nothing from it is cited. |

---

## Open work for the owner

1. Decide the direction of the detention-time / residence-time distinction (item 1). The retrieved
   EPA definition runs against the sentence as written.
2. Decide whether "control elevation" stays in a national brief at all (item 2).
3. Decide whether the item 12 worked example is rewritten around direct versus delayed response, and
   whether an archived regional EPA guide is an acceptable source for it.
4. Decide whether items 9 and 11 may move from `expert_interpretation` to `sourced_fact` now that EPA
   text supports them, or whether qualified review must land first.
5. Resolve the three unread large federal PDFs (HEC-22 4th ed, HDS-5 3rd ed, NRCS CPS 378) if
   corroboration from FHWA or NRCS is wanted for items 6, 7, and 9.
6. Approve or rename the three proposed new `authority_tier` values.
7. Route every item to the reviewer roles already named in `research/verification-dossier.md`.
   Nothing here is verified.
