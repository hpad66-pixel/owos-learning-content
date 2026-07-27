---
title: Infiltration and Inflow Authority Verification
brief_id: owos:concept-brief:003
version: 0.1.0
status: prepared_for_independent_and_qualified_review
scope: Replacing the archived EPA Region 1 snapshot behind dossier item 12 with current live United States federal authority
evidence_cutoff: 2026-07-27
retrieval_date: 2026-07-27
public_release_authority: none
verification_status_of_everything_below: pending
---

# Infiltration and Inflow Authority Verification

## Purpose

`added-terminology-source-dossier.md` item 12 rests on a single source retrieved only from EPA's
frozen January 2017 web snapshot: EPA New England, *Guide for Estimating Infiltration and Inflow*
(June 2014). That is a regional outreach document, on an archive host, with no live `www.epa.gov`
copy. This file records an attempt to replace it with current, live, defensible United States
federal authority.

Only United States federal sources were accepted. Every source cited below was retrieved on
2026-07-27 and read in full or in the named section. Where a source was retrieved but rejected, the
rejection is recorded. Nothing here is verified. Nothing here edits `white-paper.md`,
`variant-b/index.html`, `sources.yaml`, or `claims.yaml`.

---

## Summary verdict

**Claim 3, that infiltration and inflow cannot always be separated from one another: PARTIAL.**

It splits cleanly into two different statements, and the evidence runs in opposite directions for
each one.

**As a matter of federal regulatory definition, the claim is wrong and must not be made.** Current
regulation says the opposite in as many words. 40 CFR 35.2005(b)(20) ends with "Infiltration does
not include, and is distinguished from, inflow." 40 CFR 35.2005(b)(21) ends with "Inflow does not
include, and is distinguished from, infiltration." The regulation defines two separate categories
and says each excludes the other.

**As a matter of measurement from a flow record, the claim is well supported by live current EPA
authority, and can be stated more strongly than the white paper currently states it.** EPA's own
Office of Research and Development reports say directly: "It is difficult to quantify and identify
if the RDII problems are caused by inflow, infiltration or both." EPA does not treat the storm
response as two separable quantities at all. It treats the entire rainfall driven excess as one
lumped quantity, rainfall derived infiltration and inflow (RDII), estimated from wastewater flow
records rather than by separating the physical mechanisms. EPA also states that a system may show a
fast infiltration response, a slow infiltration response, or both, which is exactly what defeats a
clean shape based separation. And EPA's own pathway figure labels foundation drains as
"(Inflow/infiltration)", one source in both categories at once.

**The specific sentence the white paper and the variant B page currently carry cannot survive.** The
words "rainfall-induced infiltration cannot be distinguished from delayed inflow" and the term
"delayed inflow" appear in no live federal source retrieved on 2026-07-27. That vocabulary is EPA
Region 1's, and it exists only on the archive. Both pages must be rewritten. Recommended replacement
prose is in section "Recommended replacement paragraphs" below.

**Claims 1, 2, and 4 are all fully defensible from live federal authority, and claims 1, 2, and part
of claim 4 are defensible from regulation.**

| Claim | Verdict | Best authority tier available |
| --- | --- | --- |
| 1. Definition of infiltration in a sanitary sewer | YES | Federal regulation, 40 CFR 35.2005(b)(20) |
| 2. Definition of inflow | YES | Federal regulation, 40 CFR 35.2005(b)(21) |
| 3. Cannot always be separated | PARTIAL, see split above | Regulation contradicts the definitional reading; current EPA ORD technical reports support the measurement reading |
| 4. I&I consumes capacity and contributes to overflows and backups | YES | Federal regulation, 40 CFR 35.2005(b)(29), plus current live EPA guidance page updated 2026-01-05 |

**The archived Region 1 document can be dropped entirely, on one condition:** that the white paper
and variant B stop using the "direct inflow versus delayed inflow" framing and the "cannot be
distinguished" sentence. Everything the brief actually needs to teach is now available from live,
current, EPA authored federal sources, some of it from regulation. Detail in section "Can the
archive be dropped".

---

## Claim 1. Definition of infiltration in a sanitary sewer context

**Proposed primary source:** 40 CFR 35.2005(b)(20), Definitions, Part 35 Subpart I, Grants for
Construction of Treatment Works.

**Live URL retrieved 2026-07-27:**
`https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol1/xml/CFR-2025-title40-vol1-sec35-2005.xml`

**Edition and locator:** CFR 2025 annual edition, revised as of 2025-07-01. Title 40, Protection of
Environment, volume 1. Section heading "§ 35.2005 Definitions." Paragraph (b) opens "As used in this
subpart, the following words and terms mean:". The definition is item (20) in that numbered list.

**Verbatim passage:**

> "(20) *Infiltration.* Water other than wastewater that enters a sewer system (including sewer
> service connections and foundation drains) from the ground through such means as defective pipes,
> pipe joints, connections, or manholes. Infiltration does not include, and is distinguished from,
> inflow."

**Defensibility rating: REGULATION.** This is the strongest tier available and it is current. The
2024 and 2025 govinfo XML files for this section are byte identical, 26,354 bytes each, so the text
has not changed between editions.

**Corroborating live EPA guidance, agency guidance tier:** EPA, *Guide for Evaluating Capacity,
Management, Operation, and Maintenance (CMOM) Programs at Sanitary Sewer Collection Systems*, EPA
305-B-05-002, Office of Enforcement and Compliance Assurance, January 2005. Retrieved 2026-07-27
from `https://www.epa.gov/sites/default/files/2020-02/documents/cmom_guide_for_collection_systems.pdf`.
Locator: section 2.4.1 "Flow Monitoring", page 2-37.

> "Infiltration is the seepage of groundwater into pipes or manholes through defects such as cracks,
> broken joints, etc."

**Scope note the reviewer must act on.** The regulation puts foundation drains inside the
*infiltration* parenthetical. Every EPA technical reference retrieved puts foundation drains under
*inflow*. See "Conflicts a reviewer must resolve" below. The white paper currently lists foundation
drains under inflow, which matches EPA technical practice and does not match the regulation's
parenthetical.

---

## Claim 2. Definition of inflow

**Proposed primary source:** 40 CFR 35.2005(b)(21).

**Live URL retrieved 2026-07-27:** same govinfo XML as claim 1.

**Verbatim passage:**

> "(21) *Inflow.* Water other than wastewater that enters a sewer system (including sewer service
> connections) from sources such as, but not limited to, roof leaders, cellar drains, yard drains,
> area drains, drains from springs and swampy areas, manhole covers, cross connections between storm
> sewers and sanitary sewers, catch basins, cooling towers, storm waters, surface runoff, street wash
> waters, or drainage. Inflow does not include, and is distinguished from, infiltration."

**Defensibility rating: REGULATION.**

**Corroborating live EPA guidance:** CMOM guide, EPA 305-B-05-002, section 2.4.1, page 2-37,
retrieved 2026-07-27 from the URL above.

> "Inflow is the water which enters the sewer through direct connections such as roof leaders, direct
> connections from storm drains or yard, area, and foundation drains, the holes in and around the rim
> of manhole covers, etc."

**Second corroborating live EPA source, technical reference tier:** EPA, *Computer Tools for
Sanitary Sewer System Capacity Analysis and Planning*, EPA/600/R-07/111, Office of Research and
Development, October 2007. Retrieved 2026-07-27 from
`https://nepis.epa.gov/Adobe/PDF/P1008BBP.pdf`. Locator: Chapter 2, the paragraph introducing
Figure 2-2, page 2-5.

> "'Inflow' is the water that enters the sanitary sewer system directly via depressed manhole lids
> and frames, downspouts, sump pumps, foundation drains, area way drains and cross-connections with
> storm sewers. Although direct connections such as downspouts, sump pumps, foundation drains, and
> areaway drains are no longer common design practices, they still exist and contribute to inflow in
> many older sanitary systems. Inflow typically occurs shortly after a rainfall starts and stops
> quickly once it stops. Inflow is typically the major component of the RDII peak flow."

This is the source that gives the brief sump pumps and foundation drains as inflow sources, in a live
current EPA authored report, which the regulation's list does not supply.

---

## Claim 3. Infiltration and inflow cannot always be separated from one another

This is the claim the owner needs to hang his hat on, so it is set out at length.

### 3a. What the regulation actually says, and why it cuts against the claim as written

**Source:** 40 CFR 35.2005(b)(20) and (b)(21), quoted verbatim above. Both definitions end with an
explicit separation clause. There is no combined "Infiltration/Inflow" definition anywhere in
40 CFR 35.2005. The full paragraph (b) list was read end to end and the terms present are:
"Excessive infiltration/inflow" at (b)(16), "Infiltration" at (b)(20), "Inflow" at (b)(21),
"Nonexcessive infiltration" at (b)(28), and "Nonexcessive inflow" at (b)(29).

**The wording the task memo expected was not found in current regulation.** The phrase "the total
quantity of water from both infiltration and inflow without distinguishing the source" is **not** in
40 CFR 35.2005 and is **not** in 40 CFR 35.2120. 40 CFR 35.905, the older construction grants
definitions section that historically carried it, no longer exists in the CFR: govinfo returned HTTP
302 with a zero byte body for both the 2024 and 2025 editions of that section. **Do not cite that
sentence to the CFR.** It could not be confirmed in any current federal regulation on 2026-07-27.

That phrase does exist on a live `www.epa.gov` URL, and it is rejected as authority. See "Rejected"
below.

**Defensibility rating of the regulation on this point: REGULATION, and it contradicts the
definitional reading of claim 3.** Any sentence in the brief that reads as "federal rules treat
infiltration and inflow as inseparable" is unsupportable and must be removed.

### 3b. What live EPA technical authority says, and why it supports the measurement reading

**Source A:** EPA, *Review of Sewer Design Criteria and RDII Prediction Methods*, EPA/600/R-08/010,
Office of Research and Development, January 2008. Retrieved 2026-07-27 from
`https://nepis.epa.gov/Adobe/PDF/P1008BP3.pdf`. Locator: Chapter 4, the comparison of RDII
prediction methods, page 4-17, the paragraph immediately before the paragraph beginning "On the
other hand, the RTK method".

> "It is difficult to quantify the individual contributing flow components and identify if the RDII
> problems are caused by inflow, infiltration or both."

**Source B, the same statement in the companion report:** EPA, *Computer Tools for Sanitary Sewer
System Capacity Analysis and Planning*, EPA/600/R-07/111, October 2007. Retrieved 2026-07-27 from
`https://nepis.epa.gov/Adobe/PDF/P1008BBP.pdf`. Locator: the regression method discussion in the
RDII methodology comparison, the paragraph immediately before the paragraph beginning "On the other
hand, the RTK method".

> "It is difficult to quantify and identify if the RDII problems are caused by inflow, infiltration
> or both."

**Scope limit the reviewer must preserve.** Both sentences sit inside a discussion of the
rainfall and flow *regression* method specifically. They are not stated as a universal impossibility.
The very next paragraph in both reports says the unit hydrograph method does give an indication. That
indication is quoted in 3c.

**Source C, the statement that defeats a clean shape based separation:** EPA/600/R-07/111, Chapter 2,
the paragraph immediately following the inflow paragraph quoted under claim 2, page 2-5.

> "Rainfall-derived infiltration (RDI) refers to rainfall runoff that filters through the soil before
> entering a sanitary sewer system through damaged pipe sections, leaky joints or poor manhole
> connections. These defects can occur in both the public right-of-way portions of the sanitary sewer
> system or in individual service laterals on private property. Infiltration processes typically
> extend beyond the end of rainfall and takes some time to recede to zero after the storm event. **A
> system may experience a fast RDI response, a slow RDI response, or both.**"

Emphasis added. That last sentence is the single most useful line found. It is EPA, live, current,
and it says infiltration is not confined to the slow signature. A fast response therefore does not
prove inflow.

**Source D, EPA's own figure classifying one source as both:** EPA/600/R-07/111, Figure 2-2,
"Pathways of infiltration and inflow into sanitary sewer systems", page 2-5. The figure's callout for
foundation drains reads:

> "Foundation drains
> (Inflow/infiltration)"

**Source E, EPA lumping the two into one measured quantity:** EPA, *Storm Water Management Model
Reference Manual Volume I, Hydrology (Revised)*, EPA/600/R-15/162A, January 2016. Retrieved
2026-07-27 from `https://nepis.epa.gov/Exe/ZyPDF.cgi/P100NYRA.PDF?Dockey=P100NYRA.PDF`. Locator:
Chapter 7, "Rainfall Dependent Inflow and Infiltration", section 7.1 Introduction, page 196.

> "Rainfall dependent (or rainfall-derived) inflow and infiltration (RDII) are stormwater flows that
> enter sanitary or combined sewers due to 'inflow' from direct connections of downspouts, sump
> pumps, foundation drains, etc. as well as 'infiltration' of subsurface water through cracked pipes,
> leaky joints, poor manhole connections, etc."

And, in section 7.2, page 197:

> "Quantitative estimates of RDII are almost always derived from actual wastewater flow records as
> opposed to attempting to model the distributed set of small scale physical processes directly
> responsible for RDII."

That is EPA saying, in a current modeling reference, that the rainfall driven portion is estimated as
one aggregate from flow records rather than by resolving which mechanism produced it.

### 3c. What live EPA authority says the shape *can* tell you

This is what the white paper's worked example should be rebuilt on, because it is more honest than
either "you can tell" or "you cannot tell".

**Source F:** EPA/600/R-07/111, the paragraph beginning "On the other hand, the RTK method".
Retrieved 2026-07-27 from `https://nepis.epa.gov/Adobe/PDF/P1008BBP.pdf`.

> "On the other hand, the RTK method (one kind of the SUH method) uses up to three triangular unit
> hydrographs to represent the various ways that precipitation contributes to RDII. The RDII volumes
> of three unit hydrographs are designated as R1, R2 and R3. A high R1 value indicates that the RDII
> is rapidly responding and **presumably** inflow driven. If more of the total R-value is allocated to
> R2 and R3, this indicates that the RDII is more slowly responding and **presumably** infiltration
> driven. This knowledge is useful during a sewer system evaluation survey (SSES) to determine the
> best SSES approach to use in a particular area, as well as whether a point repair or a
> comprehensive rehabilitation approach may be more suitable."

Emphasis added. EPA's own hedge word is "presumably", twice. The same statement appears without the
hedge on EPA's live SSOAP Toolbox page, under the heading "Methodology", retrieved 2026-07-27 from
`https://www.epa.gov/water-research/sanitary-sewer-overflow-analysis-and-planning-ssoap-toolbox`:

> "A high R1 value indicates that the RDII is primarily inflow driven. If more of the total R value is
> allocated to R2 and R3, this will indicate that the RDII is primarily infiltration driven."

Caveat that must travel with the SSOAP page: the page opens with "Note: SSOAP is no longer being
maintained. Legacy codes and binaries will be archived on EPA's Enterprise GitHub. The functionality
in SSOAP will be integrated into the new graphical user interface being developed for the Stormwater
Management Model (SWMM)." The page is live and current, the tool is retired. Prefer the report
wording, which carries the hedge.

**Source G, the third category that sits between them:** CMOM guide, EPA 305-B-05-002, section 2.4.1,
page 2-37.

> "Many collection system owners or operators add a third classification: rainfall induced
> infiltration (RII). RII is stormwater that enters the collection system through defects that lie so
> close to the ground surface that they are easily reached. Although not from piped sources, RII tends
> to act more like inflow than infiltration."

This is the live, national, EPA authored equivalent of the point the archived Region 1 guide was being
used for. It says the middle category behaves like the other one. It does not say the two cannot be
told apart.

### 3d. Verdict on claim 3

**PARTIAL, with a required rewrite.**

Supportable from live federal authority, at technical reference tier:

- The rainfall driven portion of sewer flow is treated by EPA as one combined quantity, RDII,
  estimated from flow records rather than by separating mechanisms.
- It is difficult to quantify and identify whether an RDII problem is caused by inflow, infiltration,
  or both.
- Infiltration is not confined to a slow response. A system may show a fast one, a slow one, or both.
- At least one common entry point, the foundation drain, is classified by EPA as inflow and
  infiltration together.
- Response shape gives a presumption about which mechanism dominates. It does not give a finding.

Not supportable from any live federal source retrieved:

- The words "delayed inflow" as a named category. Region 1 vocabulary only, archive only.
- The sentence "rainfall-induced infiltration cannot be distinguished from delayed inflow". Archive
  only.
- Any claim that federal regulation treats the two as inseparable. Regulation says the opposite.

---

## Claim 4. I&I consumes conveyance, pumping, storage, and treatment capacity, and can contribute to overflows and backups

**Proposed primary source, regulation:** 40 CFR 35.2005(b)(29), same govinfo XML URL and edition as
claims 1 and 2.

> "(29) *Nonexcessive inflow.* The maximum total flow rate during storm events which does not result
> in chronic operational problems related to hydraulic overloading of the treatment works or which
> does not result in a total flow of more than 275 gallons per capita per day (domestic base flow plus
> infiltration plus inflow). Chronic operational problems may include surcharging, backups, bypasses,
> and overflows. (See §§ 35.2005(b)(16) and 35.2120)."

That single paragraph gives, in regulation, the hydraulic overloading of treatment works, the additive
treatment of base flow plus infiltration plus inflow, and the named consequences of surcharging,
backups, bypasses, and overflows.

**Companion regulation, showing the same consequence is an actual federal requirement trigger:**
40 CFR 35.2120, "Infiltration/Inflow", retrieved 2026-07-27 from
`https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol1/xml/CFR-2025-title40-vol1-sec35-2120.xml`.
Paragraph (a):

> "The applicant shall demonstrate to the Regional Administrator's satisfaction that each sewer system
> discharging into the proposed treatment works project is not or will not be subject to excessive
> infiltration/inflow. For combined sewers, inflow is not considered excessive in any event."

**Proposed primary source, current live agency guidance:** EPA, *Peak Flows at Sewage Treatment
Plants*, NPDES Municipal Wastewater. Retrieved 2026-07-27 from
`https://www.epa.gov/npdes/peak-flows-sewage-treatment-plants`. The page footer reads "Last updated on
January 5, 2026." Locator: heading "Wet Weather at Treatment Plants", first and second paragraphs.

> "Some municipalities currently experience high influent flows during periods of wet weather,
> referred to as peak flows, that exceed the treatment capacity of existing treatment units. This is
> typically a result of inflow and infiltration (I/I) into the sanitary sewers. The additional flow
> from I/I can increase the frequency and volume of sewer overflows, including backups of sewage into
> buildings, as well as the flows conveyed to the treatment plant."

> "Peak flows can overwhelm critical biological treatment units, such as those often used for
> secondary treatment, because they can be sensitive to the large changes in flow rate and wastewater
> characteristics. This can cause short-term operational challenges and long-term damage to the plant,
> both of which reduce treatment effectiveness."

This is already cited in the white paper as EPA 2025c and it holds up. It is live, it is current, and
it says the whole chain in EPA's own words.

**Corroborating EPA report to Congress:** EPA, *Report to Congress on the Impacts and Control of CSOs
and SSOs*, EPA 833-R-04-001, August 2004, Chapter 2 Background, section 2.1.2 "Sanitary Sewers and
SSOs", page 2-4. Retrieved 2026-07-27 from
`https://www.epa.gov/sites/default/files/2015-10/documents/csossortc2004_chapter02.pdf`.

> "In addition, high levels of infiltration and inflow (I/I) during wet weather can cause SSOs. Many
> SSSs that were designed according to industry standards experience wet weather SSOs because levels
> of I/I may exceed levels originally expected; removal of I/I has proven more difficult and costly
> than anticipated; or the capacity of the system has become inadequate due to an increase in service
> population without corresponding system upgrades."

**Corroborating current CMOM guidance:** EPA 305-B-05-002, Chapter 1, "Overview of Underlying Issues",
page 1-3, retrieved 2026-07-27:

> "Additionally, high levels of inflow and infiltration (I/I) during wet weather can cause SSOs."

**Corroborating current EPA modeling reference:** EPA/600/R-15/162A, section 7.1, page 196:

> "RDII can be a significant cause of sanitary sewer overflows (SSOs) of untreated wastewater into
> basements, streets and other properties, as well as receiving streams. It can also cause significant
> flow increases to wastewater treatment plants resulting in hydraulic overloading and disruption of
> plant processes."

**Defensibility rating: REGULATION plus current agency guidance.** This is the best supported of the
four claims. Claim 4 needs no weakening.

---

## Conflicts a reviewer must resolve

1. **Foundation drains are classified inconsistently by EPA itself.** 40 CFR 35.2005(b)(20) puts
   foundation drains inside the *infiltration* definition's parenthetical. The CMOM guide, EPA/600/R-07/111,
   and EPA/600/R-15/162A all list foundation drains under *inflow*. EPA/600/R-07/111 Figure 2-2 labels
   them "(Inflow/infiltration)". The white paper currently lists them under inflow, which matches EPA
   technical practice. That is defensible, but the brief should not present the classification as
   settled. Reading the regulation carefully, its parenthetical modifies "a sewer system", so the
   regulation is saying groundwater entering the sewer system by way of a foundation drain is
   infiltration. That reading is arguable, not obvious, and a qualified collection system reviewer
   should settle it before publication.

2. **Regulation says distinguished, practice says difficult to distinguish.** These are not actually
   in conflict, because one is a definitional statement and the other is a measurement statement, but
   the brief must say which one it is talking about in every sentence that touches the point. The
   current sentences do not.

3. **The white paper's phrase "delayed inflow" has no live federal home.** It must go or be
   explicitly marked as regional vocabulary from an archived source.

---

## Recommended replacement paragraphs

Written to be exactly supportable by what was actually retrieved. Plain language, no em dashes or en
dashes. These are drafts for the owner to accept, edit, or reject. This file does not apply them.

### For `white-paper.md` section 10, the worked example

Replace the "Working it through", "What you conclude", and "Where this stops" text with the
following. The "The situation" paragraph can stand as written.

> **Working it through.** The shape of the response carries information, but it does not settle the
> question, and the reason is more interesting than most people expect.
>
> EPA describes inflow as water that enters the sanitary sewer directly through openings and
> connections such as manhole lids and frames, downspouts, sump pumps, foundation drains, area drains,
> and cross connections with storm sewers, and notes that inflow typically occurs shortly after
> rainfall starts and stops quickly once it stops. EPA describes rainfall derived infiltration as
> rainfall that filters through the soil first and then enters through damaged pipe sections, leaky
> joints, or poor manhole connections, and notes that it typically extends beyond the end of rainfall.
> So far this matches the intuition (EPA, 2007).
>
> Then EPA adds the sentence that breaks the intuition. A system may show a fast infiltration
> response, a slow infiltration response, or both. A sharp response therefore does not prove inflow.
>
> EPA also does not treat the storm response as two separately measured quantities. It treats the
> whole rainfall driven excess as one lumped quantity called rainfall dependent, or rainfall derived,
> inflow and infiltration, shortened to RDII, and it estimates that quantity from wastewater flow
> records rather than by modelling which mechanism produced it (EPA, 2016). Where EPA compares methods
> for doing that estimate, it says plainly that it is difficult to quantify and identify whether an
> RDII problem is caused by inflow, infiltration, or both (EPA, 2007; EPA, 2008).
>
> Where the shape does help, it helps as a presumption rather than a finding. EPA's unit hydrograph
> method splits the response into fast, medium, and slow components, and says a large fast component
> indicates the response is presumably inflow driven, while more volume in the slower components
> indicates it is presumably infiltration driven. EPA uses that word twice. It is knowledge that helps
> choose where to send a field investigation, not knowledge that replaces one.
>
> **What you conclude.** The response shape narrows the question rather than answering it. It sorts
> fast from slow and gives a presumption about which mechanism dominates. It does not apportion the
> flow. Several of the sources that produce a slow tail, including sump pumps and foundation drains,
> are inflow sources whose remedy is nothing like sealing a pipe joint. Sealing pipe defects does
> nothing about a sump pump plumbed into the sanitary sewer.
>
> **A definition point worth carrying separately.** Federal regulation defines infiltration and inflow
> as two distinct categories and says each one is distinguished from the other, and does not include
> the other (40 CFR 35.2005(b)(20) and (b)(21)). That is a statement about definitions, not about
> measurement. The difficulty described above is a measurement difficulty. Both are true at once, and
> mixing them up is the fastest way to sound wrong in front of a wastewater engineer. It is also worth
> knowing that even the classification of a single entry point is not always tidy. EPA's own diagram of
> entry pathways labels foundation drains as inflow and infiltration together.
>
> **Where this stops.** This does not locate a defect, size a rehabilitation program, or apportion flow
> between mechanisms. Flow monitoring, field investigation, and qualified collection system assessment
> remain required.

Reference list entries the above would need, all live and all retrieved 2026-07-27:

- EPA. (2007). *Computer tools for sanitary sewer system capacity analysis and planning*
  (EPA/600/R-07/111). https://nepis.epa.gov/Adobe/PDF/P1008BBP.pdf
- EPA. (2008). *Review of sewer design criteria and RDII prediction methods* (EPA/600/R-08/010).
  https://nepis.epa.gov/Adobe/PDF/P1008BP3.pdf
- EPA. (2016). *Storm water management model reference manual volume I, hydrology (revised)*
  (EPA/600/R-15/162A), chapter 7.
  https://nepis.epa.gov/Exe/ZyPDF.cgi/P100NYRA.PDF?Dockey=P100NYRA.PDF
- 40 CFR 35.2005(b)(20) and (b)(21) (2025).
  https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol1/xml/CFR-2025-title40-vol1-sec35-2005.xml

The existing `(EPA, 2014)` citation to the archived Region 1 guide is no longer needed anywhere in
this passage.

### For `variant-b/index.html`, the "same rain, the wrong pipe" section

Replace the two paragraphs currently beginning "One correction worth carrying" with:

> **One correction worth carrying,** because it is commonly got wrong. People try to tell inflow from
> infiltration by the shape of the wet weather response: a sharp rise that ends with the storm, or a
> slow rise that decays over days. The shape is a clue, not an answer. EPA's own analysis reports say a
> fast response is presumably inflow driven and a slower one presumably infiltration driven, and then
> say plainly that it is difficult to quantify and identify whether the problem is caused by inflow,
> infiltration, or both. EPA also states that a system can show a fast infiltration response, a slow
> one, or both, and its own diagram of entry paths labels foundation drains as inflow and infiltration
> together.
>
> So the shape narrows the question. It does not answer it. The slow tail covers sump pumps, foundation
> drains, and indirect cross connections as well as pipe defects, and sealing pipe defects does nothing
> about a sump pump plumbed into the wrong pipe.

The paragraph in the "Into the sanitary sewer" card can stay as written. It is now backed by
regulation rather than by an archived regional guide, and the wording already matches 40 CFR
35.2005(b)(20) and (b)(21) closely enough: roof leaders, area drains, and manhole covers are all named
in the inflow definition, and cracks and defective joints are named in the infiltration definition.

Suggested addition to the variant B source table, one row:

| Source | Authority | What it supports here |
| --- | --- | --- |
| 40 CFR 35.2005(b)(20) and (b)(21), Definitions | Federal regulation | The definitions of infiltration and inflow in a sanitary sewer, and the fact that federal regulation treats them as distinct categories |
| Computer Tools for Sanitary Sewer System Capacity Analysis and Planning (EPA/600/R-07/111) | EPA technical reference | That response shape gives a presumption rather than a finding, and that infiltration can respond fast as well as slow |

---

## Can the archive be dropped

**Yes, it can be dropped entirely, provided the rewrites above are made.**

Reasoning:

1. Everything the archived Region 1 guide was carrying is now available from live sources, and at a
   better authority tier for three of the four claims. The definitions move from regional guidance up
   to federal regulation. The capacity and overflow chain moves up to regulation plus a current EPA
   page updated in January 2026. The separability point moves from regional guidance to two EPA Office
   of Research and Development reports and one current EPA modeling reference.
2. The only thing that is lost is the Region 1 vocabulary "direct inflow" and "delayed inflow", and
   the flat sentence "rainfall-induced infiltration cannot be distinguished from delayed inflow". That
   sentence is stronger than what any live federal source says, and the recommended rewrite is
   deliberately weaker in exactly that place.
3. Dropping it also removes three problems that came bundled with it: an archive host as a citation, a
   regional document standing in for national practice, and a seasonal argument built on snowmelt and
   soil thaw that does not transfer to warm climates.
4. It also removes the figure credited to a state agency, which was already excluded from OWOS use.

**If the owner decides to keep the "direct inflow versus delayed inflow" framing, the archive is still
needed and cannot be dropped**, because no live federal source retrieved on 2026-07-27 uses that
vocabulary. In that case it must be labelled in the text as an archived regional EPA document, not as
current EPA guidance. The recommendation of this file is not to keep it.

No live `www.epa.gov` copy of the Region 1 guide exists as far as this search could determine. A
targeted search restricted to the document title and EPA New England returned only the
`19january2017snapshot.epa.gov` copy and third party mirrors.

---

## Rejected sources

| Candidate | Where it surfaced | Why rejected |
| --- | --- | --- |
| *Optimizing Operation, Maintenance, and Rehabilitation of Sanitary Sewer Collection Systems*, December 2003, at `https://www.epa.gov/sites/default/files/2015-10/documents/sso_optimizing_enitre_doc.pdf` | Linked from EPA's own NPDES SSO technical reports page. Its Appendix A glossary contains the exact phrase the task memo was looking for: "INFILTRATION/INFLOW: The total quantity of water from both infiltration and inflow without distinguishing the source. Abbreviated I&I or I/I." | Three disqualifying facts, all read in the document itself on 2026-07-27. It is authored by the New England Interstate Water Pollution Control Commission, a not for profit interstate agency, not by EPA. Page 42 of the extracted text states "This manual was made possible by a grant from the U.S. Environmental Protection Agency (EPA) ... The contents do not necessarily reflect the views and policies of EPA". And the glossary itself opens "This glossary is primarily adopted from material that is copyrighted by the Office of Water Programs, California State University, Sacramento". So the one sentence that says what the owner hoped the CFR said is non federal, EPA disclaimed, and third party copyrighted. Hosting on epa.gov does not fix any of that. **Do not cite it as federal authority, and do not reproduce the glossary text.** |
| 40 CFR 35.905 | Historic home of the "without distinguishing the source" definition | Section no longer exists. govinfo returned HTTP 302 with a zero byte body for both the 2024 and 2025 editions. Not retrieved, not cited. |
| `https://www.ecfr.gov/current/title-40/chapter-I/subchapter-D/part-35/subpart-I/section-35.2005` | First attempt at the regulation | HTTP 302 redirect off host to `https://unblock.federalregister.gov/`. Not followed. The path was also wrong: part 35 sits in subchapter B, not D. The govinfo annual edition XML was used instead and is the better citation anyway because it is edition stamped. |
| `https://cfpub.epa.gov/si/si_public_file_download.cfm?p_download_id=472299&Lab=NRMRL` (SSOAP conference paper) | Search result for RDII | Retrieved but returned as unreadable binary. Nothing from it was read, therefore nothing is cited. |
| Wikipedia, "Infiltration and inflow" | Search result stating that inflow and infiltration may be hard to tell apart | Not federal authority. Not cited. |
| WEF fact sheet, "RDII Modeling" (wef.org) | Search result | Professional association, not federal. Not retrieved and not cited. Available as clearly labelled professional context if the owner wants it, which this file does not recommend, since EPA's own reports already say the same thing. |

---

## Retrieval log

Every row was attempted on **2026-07-27**. "Read" means the full text or the named section was
extracted and read. Where a PDF was fetched, the WebFetch tool confirmed the URL is live and returned
the file, but its summarizer could not decode the PDF, so the text was extracted locally and read.
That is noted per row.

| # | URL | Outcome |
| --- | --- | --- |
| 1 | `https://www.ecfr.gov/current/title-40/chapter-I/subchapter-D/part-35/subpart-I/section-35.2005` | **Not retrieved.** HTTP 302 off host to `unblock.federalregister.gov`. Not followed. |
| 2 | `https://www.govinfo.gov/content/pkg/CFR-2024-title40-vol1/xml/CFR-2024-title40-vol1-sec35-2005.xml` | Read in full. 26,354 bytes. Source for claims 1, 2, 3a, 4. |
| 3 | `https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol1/xml/CFR-2025-title40-vol1-sec35-2005.xml` | Read in full. 26,354 bytes, byte identical to row 2. Confirms the definitions are unchanged in the current annual edition, revised as of 2025-07-01. This is the URL recommended for citation. |
| 4 | `https://www.govinfo.gov/content/pkg/CFR-2024-title40-vol1/xml/CFR-2024-title40-vol1-sec35-905.xml` | **Not retrieved.** HTTP 302, zero bytes. Section does not exist in the 2024 edition. |
| 5 | `https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol1/xml/CFR-2025-title40-vol1-sec35-905.xml` | **Not retrieved.** HTTP 302, zero bytes. Section does not exist in the 2025 edition. |
| 6 | `https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol1/xml/CFR-2025-title40-vol1-sec35-2120.xml` | Read in full. 40 CFR 35.2120 "Infiltration/Inflow". Confirms no combined definition there either. Paragraph (a) cited under claim 4. |
| 7 | `https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol1/xml/CFR-2025-title40-vol1-sec122-2.xml` | **Not retrieved.** Returned a govinfo HTML error page. 40 CFR part 122 is not in title 40 volume 1. The correct volume was not located and part 122 was not checked further. Recorded as an open item, not as a negative finding. |
| 8 | `https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol1/xml/CFR-2025-title40-vol1-sec403-3.xml` | **Not retrieved.** Same govinfo HTML error page, same volume problem. 40 CFR part 403 was not checked. Recorded as an open item. |
| 9 | `https://www.epa.gov/npdes/sanitary-sewer-overflow-sso-frequent-questions` | Read. Live. Contains "Leaky sewers, stormwater, ground water and snowmelt entering the sanitary sewer from cracks and faults in the sewer or leaky sewer joints can overload a sanitary sewer" under "Why do sewers overflow?". **Does not define infiltration or inflow and does not use the term I/I.** Weaker than expected. Not proposed as a primary source. |
| 10 | `https://www.epa.gov/npdes/peak-flows-sewage-treatment-plants` | Read in full. Live, footer "Last updated on January 5, 2026". Primary live guidance source for claim 4. |
| 11 | `https://www.epa.gov/sites/default/files/2020-02/documents/cmom_guide_for_collection_systems.pdf` | Read in full, 2.7 MB, EPA 305-B-05-002, January 2005. WebFetch confirmed the URL is live and returned the PDF but could not decode it; text extracted locally and read. Source for claims 1, 2, 3b, 4. |
| 12 | `https://www.epa.gov/npdes/npdes-sso-technical-reports-and-materials` | Read. Live index page. Confirms the CMOM guide URL used in row 11 as EPA's own current link. |
| 13 | `https://www.epa.gov/npdes/sanitary-sewer-overflow-sso-additional-resources` | Read. Live index page used to enumerate candidate documents. |
| 14 | `https://www.epa.gov/npdes/2004-npdes-cso-report-congress` | Read. Live landing page for the 2004 Report to Congress. |
| 15 | `https://www.epa.gov/sites/default/files/2015-10/documents/csossortc2004_chapter02.pdf` | Read. Chapter 2 Background, section 2.1.2. Source of the corroborating quote under claim 4. |
| 16 | `https://www.epa.gov/sites/default/files/2015-10/documents/csossortc2004_chapter04.pdf` | Read. Chapter 4 Characterization. Contains "SSOs can be induced by rainfall or snowmelt when excess I/I causes the conveyance capacity of the SSS to be exceeded" but no definitions. Not cited, chapter 2 is the better locator. |
| 17 | `https://www.epa.gov/sites/default/files/2015-10/documents/csossortc2004_chapter01.pdf` | Read. No I&I definitions. Not cited. |
| 18 | `https://www.epa.gov/sites/default/files/2015-10/documents/csossortc2004_chapter03.pdf` | Read. No I&I definitions. Not cited. |
| 19 | `https://www.epa.gov/sites/default/files/2015-10/documents/sso_optimizing_enitre_doc.pdf` | Read in full. **Rejected as authority**, see Rejected sources. This is where the "without distinguishing the source" sentence actually lives on a live epa.gov URL. |
| 20 | `https://www.epa.gov/water-research/sanitary-sewer-overflow-analysis-and-planning-ssoap-toolbox` | Read in full. Live EPA page. Source F secondary quote. Carries a retirement notice for the tool. |
| 21 | `https://nepis.epa.gov/Adobe/PDF/P1008BP3.pdf` | Read in full. EPA/600/R-08/010, January 2008. Source A for claim 3b. |
| 22 | `https://nepis.epa.gov/Adobe/PDF/P1008BBP.pdf` | Read in full. EPA/600/R-07/111, October 2007. WebFetch confirmed live and returned the PDF but could not decode it; text extracted locally and read. Sources B, C, D, F for claim 3. Also source for claim 2. |
| 23 | `https://nepis.epa.gov/Exe/ZyPDF.cgi/P100NYRA.PDF?Dockey=P100NYRA.PDF` | Read, chapter 7 and glossary. EPA/600/R-15/162A, January 2016. Source E for claim 3. Already registered in the dossier as `source-epa-swmm-hydrology`. |
| 24 | `https://cfpub.epa.gov/si/si_public_file_download.cfm?p_download_id=472299&Lab=NRMRL` | **Not read.** Returned undecodable binary. Nothing cited. |
| 25 | `https://19january2017snapshot.epa.gov/www3/region1/sso/pdfs/Guide4EstimatingInfiltrationInflow.pdf` | Not re-fetched this session. Previously retrieved 2026-07-27 for the terminology dossier. Retained here only as the source of record for the sentence this file recommends removing. |
| 26 | Web search, `"infiltration/inflow" "without distinguishing the source" 40 CFR definition` | Returned only secondary and commercial dictionary sites plus 40 CFR 35.2120. No current CFR section carrying the phrase. |
| 27 | Web search, `"Guide for Estimating Infiltration and Inflow" EPA New England site:epa.gov 2014` | Returned only the `19january2017snapshot.epa.gov` copy and third party mirrors. **No live `www.epa.gov` copy exists.** |
| 28 | Web search, EPA RDII "difficult to distinguish" / "cannot be distinguished" | Returned WEF, a state agency, and Wikipedia. No federal hit. The federal wording was found by reading the EPA reports directly, not by search. |
| 29 | Web search, EPA CMOM 305-B-05-002 | Located the live CMOM PDF URL used in row 11. |

---

## Proposed source register entries

Schema fields match `sources.yaml`. All `verification_status: pending`. The proposed
`epa_regional_guidance_archived` tier from the terminology dossier becomes unnecessary if the
recommendation in "Can the archive be dropped" is accepted.

```yaml
  - source_id: source-cfr-40-35-2005-ii
    title: 40 CFR 35.2005, Definitions, Grants for Construction of Treatment Works
    source_type: federal_regulation
    authority_tier: us_federal_primary_authority
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: United States Environmental Protection Agency
    locator: https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol1/xml/CFR-2025-title40-vol1-sec35-2005.xml
    published_or_effective: CFR 2025 annual edition, revised as of 2025-07-01
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: Definitions apply to the construction grants subpart. They define infiltration, inflow, excessive infiltration/inflow, nonexcessive infiltration, and nonexcessive inflow, and they state that infiltration and inflow are distinguished from each other. They do not describe how the two are measured or separated in a flow record, and they do not establish an NPDES permit requirement.

  - source_id: source-epa-computer-tools-ssoap
    title: Computer Tools for Sanitary Sewer System Capacity Analysis and Planning
    source_type: federal_agency_technical_report
    authority_tier: epa_technical_reference
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: United States Environmental Protection Agency, Office of Research and Development
    locator: https://nepis.epa.gov/Adobe/PDF/P1008BBP.pdf
    published_or_effective: 2007-10, EPA/600/R-07/111
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: Documents a retired EPA software toolbox. Its RDII definitions and its statements about what response shape can and cannot indicate are used here as EPA technical description, not as a current recommended method. Its difficulty statement is scoped to regression based estimation.

  - source_id: source-epa-rdii-methods-review
    title: Review of Sewer Design Criteria and RDII Prediction Methods
    source_type: federal_agency_technical_report
    authority_tier: epa_technical_reference
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: United States Environmental Protection Agency, Office of Research and Development
    locator: https://nepis.epa.gov/Adobe/PDF/P1008BP3.pdf
    published_or_effective: 2008-01, EPA/600/R-08/010
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: A methods review published 2008. Used only for its statement about the difficulty of identifying whether an RDII problem is caused by inflow, infiltration, or both, which is scoped in the source to regression based estimation.

  - source_id: source-epa-cmom-guide
    title: Guide for Evaluating Capacity, Management, Operation, and Maintenance (CMOM) Programs at Sanitary Sewer Collection Systems
    source_type: federal_agency_guidance
    authority_tier: epa_guidance
    country: United States
    governing_use: us_governing_or_context
    issuer_or_author: United States Environmental Protection Agency, Office of Enforcement and Compliance Assurance
    locator: https://www.epa.gov/sites/default/files/2020-02/documents/cmom_guide_for_collection_systems.pdf
    published_or_effective: 2005-01, EPA 305-B-05-002
    accessed_on: 2026-07-27
    permission_status: public
    verification_status: pending
    limitations: An inspector and self assessment guide, published 2005 and still linked from EPA's current NPDES SSO technical reports page. It describes evaluation criteria. It does not set a numeric I&I limit and is not a regulation.
```

---

## Open work for the owner

1. Accept, edit, or reject the two replacement passages in "Recommended replacement paragraphs".
   Nothing in this file has been applied to `white-paper.md` or `variant-b/index.html`.
2. Decide the foundation drain classification question in "Conflicts a reviewer must resolve", item 1.
   This one needs a qualified collection system practitioner, not an editorial decision.
3. Decide whether to drop `source-epa-ii-estimating-guide` and the proposed
   `epa_regional_guidance_archived` authority tier entirely. This file recommends dropping both.
4. Close the two open CFR checks in retrieval log rows 7 and 8. Parts 122 and 403 were not reached
   because the govinfo volume number was wrong. Neither is expected to carry an I&I definition, but
   the check is incomplete and should not be reported as a negative finding.
5. Keep item 12's `claim_type: expert_interpretation`. The rewrite makes the passage more defensible,
   but the instructional conclusion, that the shape narrows rather than answers, is still an
   interpretation of what EPA says rather than a sentence EPA writes.
6. Route this file to the qualified wastewater collection system reviewer already named in
   `research/verification-dossier.md`. Nothing here is verified.
