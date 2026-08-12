# Source verification — Coagulation and Flocculation Concept Brief

- Brief: `owos:concept-brief:001`
- Package: `concept-briefs/coagulation-vs-flocculation/`
- Scope of this pass: liveness, authority tier, US-federal scope compliance, verbatim regulatory text, and gap analysis against the rebuild's teaching outline.
- Verification performed: 2026-07-27.
- Verifier note: every source below was fetched during this pass. Nothing here is cited from memory. Where a document could not be retrieved, that is stated as a failure, not papered over.
- Tier scheme: `core/standards/OWOS-QAQC-CERTIFICATE-STANDARD.md` §5. Tier 1 current US federal statute or regulation; tier 2 current federal agency guidance on a live agency URL; tier 3 federal technical reference on a live agency URL; tier 4 peer-reviewed research within its stated scope; tier 5 professional standards and practice references clearly labelled as professional context.

---

## 1. Summary table

| # | source_id | Live / Archived / Dead / Paywalled | Tier | US federal | Verdict |
|---|-----------|-----------------------------------|------|------------|---------|
| 1 | `source-prototype` | LOCAL FILE PRESENT (not a web resource) | none — not an authority | no | **DROP as evidence** (retain as provenance record only) |
| 2 | `source-pnws-awwa` | LIVE | 5 | no (US professional body, not federal) | **KEEP AS CONTEXT ONLY** |
| 3 | `source-pubmed-16752769` | LIVE (abstract) | 4 | no (Republic of Korea) | **KEEP AS CONTEXT ONLY** |
| 4 | `source-aktas-2013` | **DEAD** (404); DOI redirects to a PAYWALLED publisher page | 4 at best, unverifiable | no (Japan) | **DROP** |
| 5 | `source-epa-swtr-turbidity` | LIVE | 2 | yes | **KEEP** (correct the title) |
| 6 | `source-epa-lt1` | LIVE | 3 | yes | **KEEP** (with vintage boundary) |
| 7 | `source-epa-lt2` | LIVE | 3 | yes | **KEEP** (narrow the claims it carries) |
| 8 | `source-epa-pac` | LIVE | 2 | yes | **KEEP** (scope-limited) |
| 9 | `source-ecfr-141-173` | LIVE | 1 | yes | **KEEP** |
| 10 | `source-ecfr-141-551` | LIVE | 1 | yes | **KEEP** |

**Counts.** 9 of 10 locators resolve. 8 of 10 are live retrievable web resources. 1 is a local file. **1 is dead** (`source-aktas-2013`). 0 rely on a web archive or an agency snapshot host — the specific failure mode that broke the companion brief is **not** present here.

**Recommended additions** (retrieved and verified in this pass, see §6):

| new source | Locator | Tier | Why |
|---|---|---|---|
| 40 CFR 141.2 (definitions) | eCFR / govinfo, see §4.3 | 1 | Tier-1 definitions of *coagulation* and *flocculation*. Replaces guidance-tier support for the brief's central conceptual claim. |
| 40 CFR 141.170; 40 CFR 141.550 | eCFR, see §4.1–§4.2 | 1 | Establishes which systems each turbidity rule governs. Currently missing, and the brief cannot state applicability without it. |
| EPA 815-R-99-012, *Enhanced Coagulation and Enhanced Precipitative Softening Guidance Manual* | `http://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=200021WV.txt` (linked from EPA's live guidance index) | 2–3 | The only live federal source found that gives velocity-gradient design ranges, jar-test scale-up limits, and the coagulation → filter-run-length link. |

---

## 2. Per-source retrieval evidence

### 2.1 `source-prototype` — Coagulation vs Flocculation prototype HTML

- Locator: `/Users/apas/Downloads/owf-concept-001-v4_2.html`
- Retrieval: `ls -la` 2026-07-27 → file present, 66,998 bytes, mtime 2025-07-25 14:58.
- Status: **LOCAL FILE PRESENT.** It is not a web resource, has no issuing authority, no publication, and no review. It cannot be assigned tiers 1–5.
- Finding: **23 of 48 claims cite it.** Twenty-one are already `rejected`, which is correct. Two are `pending` and `material: true`: `claim-evidence-boundary` and `claim-no-operating-advice`. Both are self-referential statements about the package's own review status and use boundary — they are not factual assertions about water treatment, and citing the prototype as their "evidence" is a category error.
- Verdict: **DROP as evidence authority.** Keep the file as a provenance artifact recording where the claims came from. For the two pending claims, set `source_ids: []` (as already done for `claim-data-integration`, `claim-role-actions`, `claim-every-number-sourced`) or point them at the repository status record. The prototype must not appear in any published citation.

### 2.2 `source-pnws-awwa` — "Chemical Mixing: Nothing But a G Thing?"

- Locator: `https://www.pnws-awwa.org/wp-content/uploads/2024/06/Chemical-Mixing-Nothing-but-a-G-Thing.pdf`
- Retrieval: HTTP **200**, `application/pdf`, 2,075,294 bytes, no redirect. Text extracted and read in full (27 slides).
- Identification: 2024 PNWS AWWA Annual Conference, May 2, 2024. Author Connor Mancosky, Lead Engineer, Carollo Engineers.
- Status: **LIVE.** Tier **5** — professional practice. US-based (Pacific Northwest Section AWWA), but **not federal authority**.
- Content verified verbatim, slide 7:
  > "Velocity gradient (G), is commonly used in design of water treatment processes."
  > "G is derived from relationship between forces acting on fluid, velocity of fluid, and viscosity (resistance to movement)."
  > "Ratio of power dissipated per unit volume."
  > "Averaged over entire mixing vessel volume (velocity gradient varies over time and space)."
  >
  > `G = sqrt(P / (μV))` — "G = velocity gradient (s-1); P = Power of mixing input (kW / HP); V = Volume of mixing vessel (ft3, m3); µ = Viscosity (N-s/m2, lb-s/ft2)"
- Also verified, slide 11 (hydraulic flash mixing): "No common design criteria for flash mixing." Slide 26 takeaways: "Flash mixing G values range significantly based on selected mixing technology and across plants."
- Equipment-specific design criteria on slides 12–21 (static mixer Gt 350–1,700, t 1–5 s; pumped diffusion Gt 400–1,600; mechanical G = 300, t 10–30 s; in-line G 1,000–2,000, t < 5 s; hydraulic flocculation G 10–50 s⁻¹ tapered, t 30–45 min; horizontal paddlewheel G 10–50 s⁻¹, t 30–40 min; vertical shaft G 20–80 s⁻¹, t 30–40 min).
- Verdict: **KEEP AS CONTEXT ONLY.** See §3.2 for the scope finding.

### 2.3 `source-pubmed-16752769` — Park et al. 2006

- Locator: `https://pubmed.ncbi.nlm.nih.gov/16752769/`
- Retrieval: HTTP **200**. Verbatim abstract also pulled from NCBI E-utilities `efetch` for exactness.
- Identification: Park SM, Jun HB, Jung MS, Koo HM. *Water Science and Technology* 2006;53(7):95-102. DOI 10.2166/wst.2006.212. PMID 16752769.
- **Author affiliation: "Department of Environmental Engineering, Chungbuk National University, Korea."** Confirms `country: Republic of Korea` in `sources.yaml`. **Non-US research.**
- Status: **LIVE.** Tier **4**, abstract only — the full text was not retrieved and the methods were not reviewed.
- Verbatim abstract passage relied on:
  > "Although small particles (microflocs less than 5 microm) were formed within the mixing time of 30 s, macroflocs larger than 8 microm did not increase significantly until the mixing time of 60 s. However, macroflocs larger than 8 microm started to increase after mixing of 75 s and they reached the maximum counts at 150 s. On the other hand, macroflocs larger than 8 microm decreased after mixing time of 180 s due in breaks of the macroflocs, which resulted in resuspension of small particles. The rapid mixing conditions for the maximum growth of macroflocs were the G value of 200 s(-1) and the mixing time of 150 s, which confirmed the best performance of turbidity removal in jar tests."
- `claim-park-study` reproduces these numbers **accurately**: 75 s, 150 s peak, decline after 180 s, at G 200 s⁻¹. The claim is factually right about the study. Its problem is scope, not accuracy — see §3.1.
- Verdict: **KEEP AS CONTEXT ONLY.**

### 2.4 `source-aktas-2013` — Aktas et al. 2013 — **DEAD**

- Locator in `sources.yaml`: `https://www.deswater.com/DWT_articles/vol_51_issues_22-24_papers/51_22-24_2013_4729.pdf`
- Retrieval: HTTP **404**, `text/html`, 5,073 bytes. The file is gone.
- Fallbacks attempted:
  - `https://www.deswater.com/vol.php?vol=51&iss=22-24` → HTTP 200 but **redirects to `https://www.deswater.com/home.php`**. The volume index no longer serves that issue.
  - `https://doi.org/10.1080/19443994.2012.751883` → HTTP 200, redirects to `https://linkinghub.elsevier.com/retrieve/pii/S1944398624188339`. The journal migrated to Elsevier.
  - `https://www.sciencedirect.com/science/article/pii/S1944398624188339` → HTTP **403**. **PAYWALLED / access-blocked.**
- Status: **DEAD at the recorded locator; the surviving publisher copy is PAYWALLED and was not read.**
- **I did not retrieve this paper.** The G 546 s⁻¹ / G 390 s⁻¹ thresholds in `claim-aktas-study` are therefore **unverified by retrieval**. They were not confirmed against any table or figure in the paper during this pass.
- Country: Japan (Fujibayashi, Maruo, Nomura, Nishimura — Tohoku University). **Non-US research.**
- Verdict: **DROP.** A source that cannot be opened cannot support a published claim under the contract. `claim-aktas-study` is already `rejected`; it should now be removed rather than held. `claim-shear` and `claim-energy-audit` must have this source_id struck (see §3.1).

### 2.5 `source-epa-swtr-turbidity` — EPA 815-R-20-004

- Locator: `https://www.epa.gov/sites/default/files/2020-06/documents/swtr_turbidity_gm_final_508.pdf`
- Retrieval: HTTP **200**, `application/pdf`, 3,050,847 bytes, no redirect. Full text extracted and read.
- **Canonicity confirmed independently.** `https://www.epa.gov/dwreginfo/guidance-manuals-surface-water-treatment-rules` (HTTP 200) links this manual via `/dwreginfo/turbidity-provisions`, and that page (HTTP 200) links **exactly this URL**. The locator in `sources.yaml` is EPA's own current link, not a stale deep link.
- **Title correction required.** `sources.yaml` records "Surface Water Treatment Rule Turbidity Guidance Manual". The document's actual cover title is **"Guidance Manual for Compliance with the Surface Water Treatment Rules: Turbidity Provisions," Office of Water (4606M), EPA 815-R-20-004, June 2020.**
- Status: **LIVE.** Tier **2** — current federal agency guidance on a live agency URL.
- Note: this manual covers turbidity provisions across the SWTR, IESWTR, LT1ESWTR and LT2ESWTR (p. 1). It states at p. 1: "The original guidance manual (USEPA, 1999) focused on the requirements of the IESWTR as it relates to turbidity." Where this 2020 manual and the 2004/2010 manuals cover the same ground, **cite the 2020 manual.**
- Verdict: **KEEP.** This is the strongest non-regulatory source in the package.

### 2.6 `source-epa-lt1` — EPA 816-R-04-007

- Locator: `https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=30005ZHV.TXT`
- Retrieval: HTTP 200 → JavaScript `location.replace` to the NEPIS ZyNET viewer → viewer HTTP **200**, 89,192 bytes. Full document text downloaded via the NEPIS "Unformatted Text" action: 498,717 bytes, 254 pages. NEPIS metadata block confirms `<pubnumber>816R04007</pubnumber>`, `<title>Long Term 1 Enhanced Surface Water Treatment Rule Turbidity Provisions Technical Guidance Manual</title>`, `<pubyear>2004</pubyear>`, `<provider>NSCEP</provider>`.
- **Liveness corroborated.** `https://www.epa.gov/dwreginfo/long-term-1-enhanced-surface-water-treatment-rule-documents` (HTTP 200) currently links this manual as EPA 816-R-04-007, August 2004, at `http://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=30005ZHV.txt`.
- Status: **LIVE.** NEPIS is EPA's National Service Center for Environmental Publications on `epa.gov` — a live agency repository, **not** a web archive and **not** an agency snapshot host. Tier **3** (federal technical reference on a live agency URL). Not tier 2, because it is a 2004 rule-implementation manual whose turbidity content has been superseded in practice by the 2020 manual and because EPA's consolidated *guidance manuals* index does not list it.
- Verdict: **KEEP**, with an explicit "August 2004" vintage label wherever it is cited, and with the 2020 manual cited alongside it wherever both cover the topic.
- Retrieval caveat for anyone re-checking: the NEPIS text layer is OCR. "floc" renders as "floe", "PACl" as "PAC1", and "sec⁻¹" as `sec"1`. Quotations below are normalised for those three OCR artefacts and for nothing else.

### 2.7 `source-epa-lt2` — EPA 815-R-09-016

- Locator: `https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1009JLI.TXT`
- Retrieval: HTTP 200 → NEPIS viewer. Full text downloaded, 1,002,881 bytes. Metadata: `<pubnumber>815R09016</pubnumber>`, `<title>Long Term 2 Enhanced Surface Water Treatment Rule Toolbox Guidance Manual</title>`, `<pages>375</pages>`, `<pubyear>2010</pubyear>`. Running footer confirms "April 2010".
- **Liveness corroborated.** `https://www.epa.gov/dwreginfo/long-term-2-enhanced-surface-water-treatment-rule-documents` (HTTP 200) lists "Long Term 2 Enhanced Surface Water Treatment Rule: Toolbox Guidance Manual, EPA 815-R-09-016, April 2010" at `https://nepis.epa.gov/Exe/ZyPDF.cgi/P1009JLI.PDF?Dockey=P1009JLI.PDF`.
- Status: **LIVE.** Tier **3**.
- **Content shortfall found.** Full-text keyword scan of the 375-page document:

  | term | occurrences |
  |---|---|
  | "polymer" | 11 (all about molecular weight and addition point, or unrelated — bacterial extracellular polymers) |
  | "coagulant aid" | 1 |
  | "filter aid" | **0** |
  | "sludge conditioner" | **0** |
  | "settling depth" / "sampling depth" | **0** |
  | "velocity gradient" | **0** |

  This document does **not** support `claim-polymer-role` as written, and does **not** support `claim-jar-sampling` as written. See §5.
- What it *does* support, verbatim (§7.4.1.1, p. 7-11):
  > "To provide the process control necessary for producing consistently low filter water turbidity, systems should establish SOPs for changing chemical additions when raw water quality changes significantly. The SOPs should list the appropriate chemicals to be added and the dose according to specified raw water conditions. Jar tests or other chemical evaluations should be conducted with raw water samples representing conditions from high water quality to the worst-case scenario and should reasonably represent the treatment process."

  §7.4.2 (p. 7-12):
  > "Tapered mixing is most appropriate with variable G values ranging from 70 sec⁻¹ to 15 sec⁻¹."

  §7.4.1.3 (p. 7-12), on electrokinetic instruments:
  > "Streaming current detectors (SCDs) can provide on-line coagulation control, by measuring the net surface charge of the particle and ionic species in a sample of water. Through jar testing or other coagulant studies, the charge measurement is correlated to the optimal coagulation conditions. ... Zeta potential monitors also indicate particle surface charge and can be used in the same manner as SCDs."
  > "AWWA recommends comparing SCD and zeta potential monitoring results to jar tests on a regular basis."
- Verdict: **KEEP**, but narrow what it carries. `claim-polymer-role` and `claim-jar-sampling` must be re-sourced or weakened.

### 2.8 `source-epa-pac` — EPA Office of Pesticide Programs guidance page

- Locator: `https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/finalization-guidance-incorporation-water-treatment`
- Retrieval: HTTP **200**, `text/html`, 208,873 bytes. Page read. No archive notice, no redirect to a snapshot host.
- Identification: "Finalization of Guidance on Incorporation of Water Treatment Effects on Pesticide Removal and Transformations in Drinking Water Exposure Assessments," EPA Office of Pesticide Programs, Environmental Fate and Effects Division; memorandum dated December 2011.
- Verified text:
  > "PAC is added within conventional treatment systems before or during the coagulation/flocculation and sedimentation treatment process."
  > "Coagulation and flocculation is a two-step process to remove inorganic and organic colloidal materials from water."
- Status: **LIVE.** Tier **2**, but **scope-limited**: this is pesticide exposure-assessment guidance, not drinking-water treatment guidance. It establishes that EPA uses "PAC" to mean powdered activated carbon. It says nothing about polyaluminum chloride naming.
- **Better federal support exists for the other half of `claim-pacl-pac`.** EPA 816-R-04-007 (LT1), §7.2.2, p. 121, writes "polyaluminum hydroxychloride (PACl)" while EPA 815-R-99-012 Table 7-1 writes "Polyaluminum chloride (PACl)". Both federal documents use *PACl* for the coagulant and *PAC* for powdered activated carbon. That contrast — inside federal sources — is the evidence the claim actually needs.
- Verdict: **KEEP**, scope-limited to the PAC = powdered activated carbon half of the claim; add the LT1 and 815-R-99-012 locators for the PACl half.

### 2.9 / 2.10 `source-ecfr-141-173` and `source-ecfr-141-551`

- Locators in `sources.yaml`: the eCFR `current/title-40/...` section URLs.
- **Retrieval note.** Direct browser-style fetch of both `www.ecfr.gov/current/...` URLs returned **HTTP 302 to `https://unblock.federalregister.gov/`** — eCFR bot protection. The URLs are not broken; they are gated against automated agents. Text was therefore obtained two independent ways:
  1. **eCFR Versioner API**, point-in-time: `https://www.ecfr.gov/api/versioner/v1/full/2026-07-01/title-40.xml?part=141&section=141.173` (HTTP 200) and `...&section=141.551` (HTTP 200); re-fetched at `2026-07-23` and byte-identical for 141.173.
  2. **govinfo print CFR**: `https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol25/pdf/CFR-2025-title40-vol25-sec141-173.pdf` and `...-sec141-551.pdf` (both HTTP 200). Text matches the eCFR API output.
- Status: **LIVE**, tier **1**. Verbatim text in §4.
- **Recommendation for `sources.yaml`:** keep the human-facing eCFR URL as the reader locator, and add the govinfo print-edition URL as the machine-verifiable locator. A reviewer who hits the eCFR bot gate needs a second door.

---

## 3. Authority-scope violations

The public brief is United States federal and EPA authority only (`CONCEPT-BRIEF-PRODUCTION-CONTRACT.md`, "United States water-sector authority scope"). Non-US research may appear only as clearly bounded research, never as governing authority.

### 3.1 Non-US journal papers

**`source-pubmed-16752769` — Republic of Korea (Chungbuk National University).** Confirmed by author affiliation on the live PubMed record.

Claims that depend on it:

| claim_id | material | status | dependency |
|---|---|---|---|
| `claim-shear` | true | pending | **joint** with `source-epa-swtr-turbidity` and `source-aktas-2013` |
| `claim-park-study` | **true** | pending | **sole** |

- `claim-shear` is fine on the merits — it is fully carried by federal guidance on its own (see §6b). The Korean and Japanese papers add nothing it needs. **Strike both non-US source_ids from `claim-shear`.**
- `claim-park-study` is `material: true` and rests **solely** on non-US bench research. Under the contract, a material teaching claim cannot rest on non-US research. **Violation.**
  - Recommended weakening: set `material: false`, retitle the scope as a bounded research illustration, and require the rendered brief to state on the same visual surface that this is a 2006 Korean laboratory study at a single G value on a synthetic clay/alum system, not a US design basis and not transferable to any plant. If the rebuild cannot carry that boundary visibly, drop the claim.

**`source-aktas-2013` — Japan (Tohoku University).** Non-US, **and the locator is dead**, **and** the surviving publisher copy is paywalled and was not read.

Claims that depend on it:

| claim_id | material | status | dependency |
|---|---|---|---|
| `claim-shear` | true | pending | joint |
| `claim-aktas-study` | false | rejected | sole |
| `claim-energy-audit` | false | rejected | joint with `source-prototype` |

- This is a compound failure: non-US governing-scope problem, dead locator, and unverified numbers. **Drop the source and all three dependencies on it.** `claim-aktas-study` should move from `rejected` to removed. `claim-energy-audit` already carries a `remove_diagnosis` disposition and should be removed outright — it is built on a study threshold nobody in this pass could open.

### 3.2 AWWA professional context

**`source-pnws-awwa`** is a Pacific Northwest Section AWWA conference presentation by a consulting engineer. AWWA material is tier 5 professional context, explicitly *not* federal authority.

Claims that depend on it:

| claim_id | material | status | dependency |
|---|---|---|---|
| `claim-g-equation` | true | pending | **sole** |

- Is it stated as if governing? **Borderline, and it must be fixed.** `claim_type` is `technical_standard` and `claim_text` says "The conventional mean velocity-gradient parameter **can be expressed as** G equals…". The wording is descriptive rather than mandatory, which helps. But `claim_type: technical_standard` on a sole tier-5 source will read as a standard to a learner, and the brief's evidence chip must not present a Carollo conference slide as a standard.
- Recommended fix: reclassify `claim_type` to `sourced_fact`, and split the support. The **concept** of G as a design and operating parameter has live federal support (LT1 §7.2.2 p. 123, and EPA 815-R-99-012 p. 7-7 — see §6c). The **algebraic form** stays on PNWS AWWA, labelled "professional practice reference, 2024 PNWS AWWA conference presentation, not a federal standard," alongside the deck's own caveat that G is "averaged over entire mixing vessel volume (velocity gradient varies over time and space)."
- Verdict stands: **KEEP AS CONTEXT ONLY.**

### 3.3 Prototype as evidence authority

**`source-prototype`** must not be an evidence authority for anything. It is cited by **23 claims**.

Twenty-one are already `rejected` and need no action beyond ensuring they never render with a citation:
`claim-universal-nonsettling`, `claim-us-credit-at-coagulation`, `claim-sludge-factor`, `claim-consent-order`, `claim-negative-charge-universal`, `claim-restabilization`, `claim-simulator-thresholds`, `claim-colloid-range`, `claim-zeta-range`, `claim-polymer-never-replaces`, `claim-jar-only-defensible`, `claim-cross-sector-same-physics`, `claim-ro-fouling`, `claim-design-ranges-universal`, `claim-energy-audit`, `claim-alum-reaction`, `claim-ferric-reaction`, `claim-jar-rpm-universal`, `claim-streaming-current-proxy`, `claim-watershed-prediction`, `claim-no-capital`.

**Two are `pending` and `material: true` and must be fixed before the rebuild:**

- `claim-evidence-boundary` — "The working pilot has complete supplied-claim inventory but incomplete independent and qualified review…"
- `claim-no-operating-advice` — "The working brief does not authorize a facility dose, mixing, chemical, or process change."

Both are governance statements about this package. Neither is a factual assertion the prototype could evidence. **Set `source_ids: []`** for both, matching the pattern already used for `claim-data-integration`, `claim-role-actions` and `claim-every-number-sourced`.

### 3.4 Snapshot-host trap encountered (not in the package — recorded as a warning)

While searching for a federal source on treatment-plant optimization, results surfaced `19january2017snapshot.epa.gov` and `19january2021snapshot.epa.gov` copies of EPA's optimization pages. **These are exactly the class of URL that broke the companion brief.** They were not used and must not enter the package. The live equivalent is `https://www.epa.gov/sdwa/optimization-program-drinking-water-systems`, which redirects (HTTP 200) to `https://www.epa.gov/sdwa/drinking-water-optimization-program`.

---

## 4. Verbatim regulatory text

**CFR edition and revision.** Two independent retrievals:

- **eCFR (electronic, point-in-time).** Title 40 `up_to_date_as_of` and `latest_amended_on`: **2026-07-23** (`https://www.ecfr.gov/api/versioner/v1/titles.json`). Section text pulled at `2026-07-01` and again at `2026-07-23`; byte-identical for § 141.173. Per the eCFR Versioner versions index, neither § 141.173 nor § 141.551 has been amended since the eCFR baseline of 2016-12-28.
- **Print CFR (govinfo).** **Title 40, Volume 25, revised as of July 1, 2025** — `CFR-2025-title40-vol25`. Text identical to the eCFR output.

### 4.1 40 CFR 141.173 — Filtration (Subpart P)

Section source note: **[63 FR 69516, Dec. 16, 1998, as amended at 65 FR 20313, Apr. 14, 2000; 66 FR 3779, Jan. 16, 2001]**

Full verbatim text:

> **§ 141.173 Filtration.**
>
> A public water system subject to the requirements of this subpart that does not meet all of the criteria in this subpart and subpart H of this part for avoiding filtration must provide treatment consisting of both disinfection, as specified in § 141.72(b), and filtration treatment which complies with the requirements of paragraph (a) or (b) of this section or § 141.73 (b) or (c) by December 31, 2001.
>
> (a) *Conventional filtration treatment or direct filtration.* (1) For systems using conventional filtration or direct filtration, the turbidity level of representative samples of a system's filtered water must be less than or equal to 0.3 NTU in at least 95 percent of the measurements taken each month, measured as specified in § 141.74(a) and (c).
>
> (2) The turbidity level of representative samples of a system's filtered water must at no time exceed 1 NTU, measured as specified in § 141.74(a) and (c).
>
> (3) A system that uses lime softening may acidify representative samples prior to analysis using a protocol approved by the State.
>
> (b) *Filtration technologies other than conventional filtration treatment, direct filtration, slow sand filtration, or diatomaceous earth filtration.* A public water system may use a filtration technology not listed in paragraph (a) of this section or in § 141.73(b) or (c) if it demonstrates to the State, using pilot plant studies or other means, that the alternative filtration technology, in combination with disinfection treatment that meets the requirements of § 141.72(b), consistently achieves 99.9 percent removal and/or inactivation of *Giardia lamblia* cysts and 99.99 percent removal and/or inactivation of viruses, and 99 percent removal of *Cryptosporidium* oocysts, and the State approves the use of the filtration technology. For each approval, the State will set turbidity performance requirements that the system must meet at least 95 percent of the time and that the system may not exceed at any time at a level that consistently achieves 99.9 percent removal and/or inactivation of *Giardia lamblia* cysts, 99.99 percent removal and/or inactivation of viruses, and 99 percent removal of *Cryptosporidium* oocysts.

**Which systems it applies to** — 40 CFR 141.170(a), same edition, retrieved in this pass:

> "The requirements of this subpart P constitute national primary drinking water regulations. … The requirements of this subpart are applicable to subpart H systems serving at least 10,000 people, beginning January 1, 2002 unless otherwise specified in this subpart."

So: **§ 141.173 governs Subpart H (surface water / GWUDI) systems serving at least 10,000 people.**

### 4.2 40 CFR 141.551 — Strengthened combined filter effluent turbidity limits (Subpart T)

Section source note: **[67 FR 1839, Jan. 14, 2002, as amended at 69 FR 38856, June 29, 2004]**

Full verbatim text:

> **§ 141.551 What strengthened combined filter effluent turbidity limits must my system meet?**
>
> Your system must meet two strengthened combined filter effluent turbidity limits.
>
> (a) The first combined filter effluent turbidity limit is a "95th percentile" turbidity limit that your system must meet in at least 95 percent of the turbidity measurements taken each month. Measurements must continue to be taken as described in § 141.74(a) and (c). Monthly reporting must be completed according to § 141.570. The following table describes the required limits for specific filtration technologies.
>
> | If your system consists of * * * | Your 95th percentile turbidity value is * * * |
> |---|---|
> | (1) Conventional Filtration or Direct Filtration | 0.3 NTU. |
> | (2) All other "Alternative" Filtration | A value determined by the State (not to exceed 1 NTU) based on the demonstration described in § 141.552. |
>
> (b) The second combined filter effluent turbidity limit is a "maximum" turbidity limit which your system may at no time exceed during the month. Measurements must continue to be taken as described in § 141.74(a) and (c). Monthly reporting must be completed according to § 141.570. The following table describes the required limits for specific filtration technologies.
>
> | If your system consists of * * * | Your maximum turbidity value is * * * |
> |---|---|
> | (1) Conventional Filtration or Direct Filtration | 1 NTU. |
> | (2) All other "Alternative Filtration" | A value determined by the State (not to exceed 5 NTU) based on the demonstration as described in § 141.552. |

**Which systems it applies to** — 40 CFR 141.550, same edition, retrieved in this pass:

> "All subpart H systems which serve populations fewer than 10,000, are required to filter, and utilize filtration other than slow sand filtration or diatomaceous earth filtration must meet the combined filter effluent turbidity requirements of §§ 141.551-141.553. If your system uses slow sand or diatomaceous earth filtration you are not required to meet the combined filter effluent turbidity limits of subpart T, but you must continue to meet the combined filter effluent turbidity limits in § 141.73."

### 4.3 40 CFR 141.2 — Definitions (retrieved in this pass; recommended addition)

> **Coagulation** means a process using coagulant chemicals and mixing by which colloidal and suspended materials are destabilized and agglomerated into flocs.
>
> **Flocculation** means a process to enhance agglomeration or collection of smaller floc particles into larger, more easily settleable particles through gentle stirring by hydraulic or mechanical means.
>
> **Conventional filtration treatment** means a series of processes including coagulation, flocculation, sedimentation, and filtration resulting in substantial particulate removal.
>
> **Direct filtration** means a series of processes including coagulation and filtration but excluding sedimentation resulting in substantial particulate removal.
>
> **Sedimentation** means a process for removal of solids before filtration by gravity or separation.

### 4.4 Verdict on `claim-us-filtered-water-turbidity`

Claim text: *"Under applicable United States Surface Water Treatment Rules, conventional and direct filtration systems must meet combined filter effluent turbidity limits of 0.3 NTU in at least 95 percent of measurements each month and 1 NTU as the maximum."*

**VERIFIED.** Every number and percentile matches both sections exactly:

| element | § 141.173 | § 141.551 | claim |
|---|---|---|---|
| 95-percent limit, conventional/direct | ≤ 0.3 NTU in at least 95 percent of measurements each month | 0.3 NTU (95th percentile) | 0.3 NTU / 95 percent ✅ |
| maximum | at no time exceed 1 NTU | 1 NTU | 1 NTU ✅ |
| systems | Subpart H, ≥ 10,000 people | Subpart H, < 10,000 people, filtering, not slow sand or DE | "conventional and direct filtration systems" ✅ |

**Required additions to the claim's `limitations`, all now evidenced:**

1. Slow sand and diatomaceous earth systems are **not** covered by these limits; they meet § 141.73 instead (§ 141.550, verbatim above).
2. Alternative filtration systems get a State-set 95th-percentile value **not to exceed 1 NTU** and a State-set maximum **not to exceed 5 NTU** (§ 141.551 tables). The brief must not present 0.3/1 as universal.
3. Lime-softening systems may acidify samples before analysis under a State-approved protocol (§ 141.173(a)(3)).
4. The 0.3/1 pair is a **combined filter effluent** standard, measured per § 141.74(a) and (c). It is not an individual-filter standard.

**Also confirmed as correctly rejected:** `claim-us-credit-at-coagulation` ("turbidity and log-removal credit is earned in coagulation rather than at the filter"). Nothing in § 141.170, § 141.173, § 141.500 or § 141.551 locates credit at coagulation. § 141.170(a)(1) requires "At least 99 percent (2-log) removal of *Cryptosporidium* between a point where the raw water is not subject to recontamination by surface water runoff and a point downstream before or at the first customer" — a **treatment-train** boundary, not a coagulation-basin boundary. The rejection is correct and the reason should be recorded against the regulation, not against the guidance manual.

---

## 5. Claims that depend on non-federal or prototype sources

Flagged by claim id.

### A. Depends on a **non-US** source

| claim_id | material | non-US source(s) | country | sole or joint | action |
|---|---|---|---|---|---|
| `claim-park-study` | **true** | `source-pubmed-16752769` | Republic of Korea | **sole** | **Scope violation.** Set `material: false`, bound visibly as 2006 Korean bench research, or drop. |
| `claim-aktas-study` | false | `source-aktas-2013` | Japan | **sole** | **Remove.** Source is dead and unverified. |
| `claim-shear` | true | `source-pubmed-16752769`, `source-aktas-2013` | Korea, Japan | joint with EPA 815-R-20-004 | Strike both non-US source_ids. Federal support is sufficient on its own — see §6b. |
| `claim-energy-audit` | false | `source-aktas-2013` | Japan | joint with prototype | **Remove.** Already `rejected`; both its sources are now disqualified. |

### B. Depends on a **non-federal US professional** source

| claim_id | material | source | sole or joint | action |
|---|---|---|---|---|
| `claim-g-equation` | true | `source-pnws-awwa` (AWWA/Carollo, tier 5) | **sole** | Reclassify from `technical_standard` to `sourced_fact`; add federal support for the concept (LT1 p. 123; EPA 815-R-99-012 p. 7-7); label the equation as professional practice, not a standard. |

### C. Depends on `source-prototype`

**Pending and material — must be fixed:** `claim-evidence-boundary`, `claim-no-operating-advice`. Set `source_ids: []`.

**Rejected, must never render a citation (21):** `claim-universal-nonsettling`, `claim-us-credit-at-coagulation`, `claim-sludge-factor`, `claim-consent-order`, `claim-negative-charge-universal`, `claim-restabilization`, `claim-simulator-thresholds`, `claim-colloid-range`, `claim-zeta-range`, `claim-polymer-never-replaces`, `claim-jar-only-defensible`, `claim-cross-sector-same-physics`, `claim-ro-fouling`, `claim-design-ranges-universal`, `claim-energy-audit`, `claim-alum-reaction`, `claim-ferric-reaction`, `claim-jar-rpm-universal`, `claim-streaming-current-proxy`, `claim-watershed-prediction`, `claim-no-capital`.

### D. Claims whose cited federal source does not actually contain the content

These are not scope violations. They are **source-trace failures** found by reading the cited documents in full. Each is `material: true` and `pending`.

| claim_id | cited source | what full-text retrieval shows | action |
|---|---|---|---|
| **`claim-pin-floc`** | `source-epa-lt1` | EPA 816-R-04-007 contains **zero** occurrences of "pin floc" or "microfloc". The claim is not in its cited source. See §6f — the one live federal usage found says something close to the opposite. | **Re-source and reverse the framing.** |
| `claim-polymer-role` | `source-epa-lt2` | EPA 815-R-09-016 contains **zero** occurrences of "filter aid" or "sludge conditioner". It does not enumerate polymer roles. | Re-source to EPA 815-R-99-012 §7.3.4 p. 7-9 and EPA 815-R-20-004 §4.3.1 p. 58, and narrow the role list to what those say. |
| `claim-jar-sampling` | `source-epa-lt2` | EPA 815-R-09-016 contains **zero** occurrences of "settling depth" or "sampling depth". | Re-source to EPA 815-R-99-012 §7.2.2 p. 7-3, which does say it — see §6d. |
| `claim-turbidity-proxy` | `source-epa-swtr-turbidity`, `source-epa-lt1` | Supported, but the strongest wording is elsewhere in the 2020 manual than the pages currently recorded. | Update the passage locator — see §6e. |

---

## 6. Gap analysis

Each rebuild idea below is assessed against sources actually opened in this pass.

### (a) Coagulation and flocculation are different mechanisms operating on different timescales

**SUPPORTED — and upgradeable to tier 1.**

Currently `claim-distinct-jobs` rests on `source-epa-lt1` (tier 3). It can be lifted to **tier 1**, because 40 CFR 141.2 defines both terms and the definitions carry the mechanism distinction explicitly (§4.3 above): coagulation "destabilized and agglomerated into flocs" by "coagulant chemicals and mixing"; flocculation "enhance agglomeration or collection of smaller floc particles into larger, more easily settleable particles through gentle stirring."

The **timescale** half needs guidance, and it is there. EPA 816-R-04-007, §7.2.2, p. 123:

> "The time needed to achieve efficient coagulation varies depending on the coagulation mechanism involved. When the mechanism is charge neutralization, the detention time needed may be one second or less. When the mechanism is sweep floc or entrapment, longer detention times on the order of 1 to 30 seconds may be appropriate."

And p. 125 for the other end of the scale:

> "Overall detention time in the flocculation process typically ranges from 10 to 30 minutes and is generally provided in several different basins or basin segments so the mixing intensity can be varied through the process."

Seconds versus tens of minutes — the contrast the brief wants, from live federal guidance.

**Bonus finding that should be taught.** EPA 816-R-04-007, p. 124:

> "Coagulation by itself does not reduce turbidity. In fact, turbidity may increase during the coagulation process due to additional insoluble compounds that are generated by chemical addition."

And p. 125:

> "As with coagulation, the purpose of flocculation is not to directly reduce turbidity or suspended solids, but to prepare the solids for subsequent removal."

**Action:** re-source `claim-distinct-jobs` to 40 CFR 141.2 (primary) + EPA 816-R-04-007 pp. 123–125 (timescale). Add a new claim for "coagulation does not itself reduce turbidity", which is both federally sourced and pedagogically load-bearing.

### (b) Rapid mix intensity and duration affect floc formation

**SUPPORTED by live federal authority. No non-US research is needed.**

EPA 816-R-04-007, §7.2.2, p. 123:

> "When alum or ferric chloride is used to achieve destabilization through charge neutralization, it is extremely important that the coagulant chemical be distributed quickly and efficiently because the intermediate products of the coagulant reaction are the destabilizing agents. These intermediate species are short-lived and they must contact the solids particles in the water if destabilization is to be achieved."
>
> "In some cases, excessive mixing may serve to break up coagulant molecules or floc particles, thereby reducing the effectiveness of subsequent solids removal processes."

EPA 815-R-20-004, §4.3.2, p. 59:

> "Proper flocculation requires long, gentle mixing. Mixing energy should be high enough to bring coagulated particles constantly into contact with each other, but not so high as to break up those particles already flocculated."
>
> "If the speed of the paddles is too slow in the earlier stages of the flocculation process, the result can be insufficient floc formation. If the speed of the paddles is too fast in the later stages, the floc that is formed could shear or break apart."

**Action:** `claim-shear` is fully carried by these two federal passages. Strike `source-pubmed-16752769` and `source-aktas-2013` from it.

### (c) Velocity gradient G as a design and operating concept

**SUPPORTED by live federal guidance — this was the largest recoverable gap.**

EPA 816-R-04-007, §7.2.2 sidebar, p. 123:

> "Mixing intensity is typically quantified with a number known as the 'velocity gradient' or 'G' value. The G value is a function of the power input into the mixing process and the volume of the reaction basin. Typical G values for coagulation mixing range from 300 to 8,000 sec⁻¹ (Hudson, 1981)."

Same document, §7.2.3, p. 124:

> "Often, optimum performance is achieved by reducing the intensity of mixing as the water proceeds through flocculation (known as tapered or staged flocculation). Engineers have developed methods of determining appropriate stir rates, called 'mixing intensity values,' abbreviated as the letter 'G.' Generally, slow mixing should start out relatively fast (G values of 60 to 70 sec⁻¹) to promote clumping, and end up slower to prevent the larger clumps from breaking apart (G values of 10 to 30 sec⁻¹) (Kawamura, 2000)."

**EPA 815-R-99-012, *Enhanced Coagulation and Enhanced Precipitative Softening Guidance Manual*, §7.3.2, p. 7-7** — newly retrieved this pass, live via EPA's own guidance index:

> "The purpose of rapid mixing is to obtain instantaneous, uniform dispersion of the coagulant through the raw water, since the most efficient use of the coagulant is achieved with instantaneous dispersion. … Conventional rapid-mixing chambers, which have a 10 to 30 second retention time and use 0.25 to 1.0 hp/mgd of mechanical mixing, have velocity gradients in the range of 300 to 1000 sec⁻¹."
>
> "The aggregation of optimum-size flocs (0.1 to 2.0 mm effective size) requires gentle mixing in the energy gradient range of 20 to 70 s⁻¹ for a period of approximately 20 minutes (Hudson, 1981). For settling, a larger visible floc is normally required, and lower energy levels are applied. Smaller, more dense floc is formed at the high end of the energy range."

EPA 815-R-09-016, §7.4.2, p. 7-12: "Tapered mixing is most appropriate with variable G values ranging from 70 sec⁻¹ to 15 sec⁻¹."

EPA 815-R-20-004, §4.3.2, p. 59: "Tapered mixing (i.e., decreasing velocity gradient through the basin) is most appropriate." And on floc breakup at basin transitions, p. 60: "The velocity gradient at any point from the flocculation basin to the sedimentation basin should be less than the velocity gradient in the last flocculation stage."

**This has a sharp consequence for `claim-design-ranges-universal`,** which is currently `rejected` for lacking support. The rejection is correct, but for a stronger reason than recorded: **live federal guidance gives ranges, and the prototype's numbers disagree with them.**

| parameter | prototype (rejected) | EPA 815-R-99-012 p. 7-7 | EPA 816-R-04-007 pp. 123–124 |
|---|---|---|---|
| rapid-mix G | 600–1000 s⁻¹ | **300–1000 s⁻¹** | 300–8,000 s⁻¹ (coagulation mixing) |
| rapid-mix duration | 30–60 s | **10–30 s retention** | ≤1 s (charge neutralization) to 1–30 s (sweep floc) |
| flocculation G | 20–80 s⁻¹ | **20–70 s⁻¹** | 60–70 s⁻¹ tapering to 10–30 s⁻¹ |
| flocculation duration | 20–60 min | **~20 min** | 10–30 min overall detention |

The prototype's rapid-mix **duration** is wrong by roughly a factor of two to three against every federal source read. Note also that the Korean study's own optimum was 150 s at G 200 s⁻¹ — a third answer again, and a good illustration of why a single bench study is not a design basis.

**Action:** the rebuild can teach G properly, with (i) the qualitative definition from LT1 p. 123 (tier 3 federal), (ii) an attributed range table from EPA 815-R-99-012 p. 7-7 (tier 2–3 federal, dated 1999, sourced to Hudson 1981), (iii) the algebraic form from PNWS AWWA labelled professional context, and (iv) an explicit statement — supported by both the PNWS deck ("No common design criteria for flash mixing"; "Flash mixing G values range significantly based on selected mixing technology and across plants") and by the spread in the table above — that **there is no single national operating range**.

### (d) What a jar test can and cannot establish

**SUPPORTED — and better sourced than the package currently records.**

*What it is.* EPA 815-R-20-004 glossary:

> "**jar test.** A laboratory procedure that simulates a water treatment plant's coagulation/flocculation units with differing chemical doses and also energy of rapid mix, energy of slow mix, and settling time. The purpose of this procedure is to estimate the minimum or ideal coagulant dose required to achieve certain water quality goals. … When evaluating the results of a jar test, the operator should also consider the floc quality in the flocculation area and the floc loading on the filter."

*What it can do.* EPA 815-R-99-012, §7.2.1, p. 7-2:

> "Coagulation/flocculation is a physical/chemical process that can usually be adequately simulated through jar testing, and the effectiveness of a coagulant can often be determined using jar tests (Amirtharajah and O'Melia, 1990). … Therefore, as long as the energy input and detention times are simulated accurately during jar testing, full-scale performance of flocculation can be relatively well-simulated."

*What it cannot do* — the passage the brief most needs. EPA 815-R-99-012, §6, p. 6-25:

> "Settling performance can be judged with jar testing if the existing process is used as the control, but **filtration must be studied at either pilot- or full-scale**."

Same manual, §3, p. 3-11:

> "Due to inherent differences between full-scale and jar testing mixing conditions (which result in differences in carbon dioxide dissolution), jar testing may not always accurately predict full-scale behavior. Consequently, an adequate margin of safety should be incorporated into translating jar testing results to the full-scale application."

§7.2.1, p. 7-2:

> "Short-circuiting does not occur during jar testing. Thus, results from jar-test trials of flocculation may be superior to those in plants where short-circuiting in the mixing and flocculating processes occurs."
>
> "The jar test results may overestimate particle removal and underestimate TOC removal."

§7.2.2, p. 7-3:

> "Care should be taken in projecting jar test settling data to full-scale plant operation due to the longer detention time at full-scale compared to jar tests. For a given settling velocity, the detention time in the jar test procedure is about 1/60 of that in a conventional plant."
>
> "For these reasons, jar test results may underestimate the settling performance that may be achieved at full-scale."

*Comparability of technique* — this replaces the LT2 citation on `claim-jar-sampling`. §7.2.2, p. 7-3:

> "Settling velocity distribution curves are used to analyze floc settling characteristics during jar testing by collecting samples at a given depth over discrete time intervals."
>
> "Given these considerations, the recommended period for settling during jar testing is between 30 and 60 minutes. This duration has been shown to produce a clear supernatant for floc that will settle adequately at full-scale."

*Governance.* EPA 815-R-20-004, §4.3.1, p. 57: "Relying exclusively on past practice is not always good practice." And: "PWSs should develop SOPs that may include decision trees or flow-charts, that establish a decision-making and testing method that is suited to the plant and personnel." EPA 816-R-04-007, §8.3.1: "If a process change is made to the plant based on the results of jar testing, systems should remember to update the pertinent SOPs."

**Action:** `claim-jar-purpose` is well supported. `claim-jar-sampling` must be re-sourced from LT2 to EPA 815-R-99-012 §7.2.2 p. 7-3. The "cannot" side is strong enough to carry a dedicated teaching block, and it kills `claim-jar-only-defensible` and `claim-jar-rpm-universal` on federal evidence rather than on editorial judgment.

### (e) Why filtered water turbidity is a regulated performance measure rather than a process measure

**SUPPORTED at tier 1 plus tier 2.**

*It is a treatment-technique performance standard, not a contaminant measurement.* 40 CFR 141.170(a): "The regulations in this subpart establish or extend treatment technique requirements **in lieu of maximum contaminant levels** for the following contaminants: *Giardia lamblia*, viruses, heterotrophic plate count bacteria, *Legionella*, *Cryptosporidium*, and turbidity. … The treatment technique requirements consist of installing and properly operating water treatment processes which reliably achieve: (1) At least 99 percent (2-log) removal of *Cryptosporidium* between a point where the raw water is not subject to recontamination by surface water runoff and a point downstream before or at the first customer…" (40 CFR 141.500 states the same for Subpart T.)

*It is measured at the combined filter effluent, at the end of the train.* § 141.173(a)(1), § 141.551(a) — §4 above.

*It is an optical property, not a solids measurement.* EPA 815-R-20-004 glossary:

> "**turbidity.** The cloudy appearance of water caused by the presence of suspended and colloidal matter. In the waterworks field, a turbidity measurement is used to indicate the clarity of water. Technically, turbidity is an optical property of the water based on the amount of light reflected by suspended particles. Turbidity cannot be directly equated to suspended solids because white particles reflect more light than dark-colored particles and many small particles will reflect more light than an equivalent large particle."

*And its link to pathogen removal is a documented correlation, not an identity — EPA says so where the correlation fails.* EPA 815-R-20-004, §2.2.4, p. 21:

> "States may not grant this credit to PWSs with membrane, bag/cartridge, slow sand, or DE plants, **due to the lack of documented correlation between filter effluent turbidity and *Cryptosporidium* removal** for these processes."

That sentence is the single best federal evidence in the package that turbidity is a performance surrogate whose validity is technology-dependent. It supports `claim-turbidity-proxy` far more directly than the currently recorded passages, and it independently reinforces the rejection of `claim-us-credit-at-coagulation`.

*Upstream of that, coagulation is not where turbidity is measured for compliance.* EPA 816-R-04-007, p. 124: "Coagulation by itself does not reduce turbidity."

**Action:** re-source `claim-turbidity-proxy` to 40 CFR 141.170(a) + EPA 815-R-20-004 §2.2.4 p. 21 and glossary. Add the § 141.170(a) "in lieu of maximum contaminant levels" language as the spine of the regulatory teaching block.

### (f) What "pin floc" indicates

**NOT SUPPORTED AS CURRENTLY WRITTEN. The one live federal usage points the other way.**

`claim-pin-floc` reads: *"Small microfloc or pin floc after coagulation can be an intended intermediate before further aggregation and separation."* Cited to `source-epa-lt1`.

Full-text search of all four federal documents opened in this pass:

| document | "pin floc" | "microfloc" |
|---|---|---|
| EPA 816-R-04-007 (LT1, 254 pp.) — **the cited source** | **0** | **0** |
| EPA 815-R-09-016 (LT2, 375 pp.) | 0 | 0 |
| EPA 815-R-99-012 (Enhanced Coagulation, 237 pp.) | 0 | 0 |
| EPA 815-R-20-004 (SWTR Turbidity, 2020) | **1** | 0 |

The single occurrence, EPA 815-R-20-004, Chapter 6 CPE case study, p. 101:

> "A review of the plant's operation procedures revealed that the poor performance was caused by the operator adding coagulants at excessive dosages, leading to formation of a pin floc that was difficult to settle and filter. The operators did not have an adequate process control program or equipment to allow them to identify and set the proper chemical doses."

So the only place live federal authority uses the term, it names pin floc as **the diagnostic signature of a coagulant overdose** — the opposite of "an intended intermediate."

This is the same failure pattern that broke the companion brief: a claim attributed to a federal document that does not contain it, teaching something current federal authority contradicts. It should be treated as a blocking defect, not a wording nit.

**Recommended weakening** (this is the honest outcome, not a workaround): replace `claim-pin-floc` with a claim the retrieved record supports —

> *Pin floc — small, poorly settling floc — is described in EPA guidance as a symptom of a coagulation problem, in one documented case excessive coagulant dosage, and as difficult to settle and filter. Floc appearance alone does not establish process success; EPA directs operators to judge floc quality together with floc loading on the filter and with settled and filtered water turbidity.*

Support: EPA 815-R-20-004 p. 101 (the case study), plus the glossary jar-test entry ("the operator should also consider the floc quality in the flocculation area and the floc loading on the filter"), plus EPA 816-R-04-007 p. 125 on the legitimate direct-filtration case where "smaller floc particles may be the most desirable since they tend to be stronger and less susceptible to breaking up from the shear forces within the filters" — which is the *only* federally supported sense in which small floc is intended, and it is process-specific to direct filtration, not general.

If the rebuild wants to teach pin floc as a benign intermediate anywhere, it needs a source nobody found in this pass. **Recommend not teaching it that way.**

### (g) Relationship between coagulation performance and downstream filter run length

**SUPPORTED by live federal guidance.**

EPA 815-R-99-012, §7.2.2, p. 7-3:

> "Efficient settling is extremely important because it minimizes the floc loading onto the filters. **Shorter filter runs and a reduction in treatment capacity can result from poor sedimentation.**"

Same manual, §7.3.4, p. 7-9 — the clearest causal chain found:

> "If the implementation of a modified chemical treatment strategy affects the settled water quality in a treatment plant, the performance of the filters can also be affected. This may manifest itself by early particle or turbidity breakthrough in the filters, which may ultimately result in shorter filter runs. Utilities may need to evaluate alternatives to improve filter performance or to plan for shorter filter runs. One impact of shorter filter runs is an increase in the amount of filter backwash water."
>
> "The use of a filter-aid polymer can result in improved particle capture, better filtrate quality, longer filter runs, and higher headloss prior to turbidity breakthrough."
>
> "Because the viscosity of water increases with decreasing temperature, breakthrough as a result of floc shearing is more likely at lower water temperatures. Consequently, increased polymer doses may be required in cold weather."

EPA 815-R-20-004, §5, p. 65:

> "Overdosing either an inorganic coagulant or a polymer could have a negative effect on the filter. … if excessive alum is added to the influent settled water, mudballs might develop in the filter. Excess polymer dosages can also result in short filter runs and mudball formation. PWSs should start at very low coagulant or polymer dosages and gradually increase the dose until positive effects are seen in the filtered effluent quality."

Same manual, Chapter 5 sidebar, p. 66: "Performance limitations observed at the start of a filter run are most often attributed to improper chemical conditioning of the filter."

**Action:** `claim-downstream` is supported and can be sharpened from "influences … filtration" to the specific, federally sourced chain: coagulation dose and settled-water quality → floc loading on the filter → early breakthrough → shorter runs → more backwash volume → recycle-stream load. Re-source from LT1 to EPA 815-R-99-012 §7.3.4 p. 7-9 and EPA 815-R-20-004 §5 p. 65.

**Bonus for the polymer claims.** The same page, EPA 815-R-99-012 p. 7-9, resolves `claim-polymer-charge-roles` on federal evidence:

> "Polymers used as filter aids are generally categorized into cationic, anionic, and nonionic groups. **The most appropriate choice will be site-specific, and typically will be verified through trial and error.** Many plants, however, have had greater success with nonionic and anionic polymer filter aids. Cationic polymers have shown superior performance as coagulant aids rather than as filter aids. **The molecular weight of the polymer must also be considered.**"

Corroborated by EPA 815-R-20-004, §4.3.1, p. 58: "Metal salts should be introduced at the point of maximum energy input. Low molecular weight cationic polymers can be fed with metal salts at the rapid mix or to second stage mixing following the metal salt. High molecular weight nonionic/anionic floc/filter aids should be introduced to the process stream at a point of gentle mixing."

Together these support `claim-polymer-charge-roles` and a narrowed `claim-polymer-role` limited to **primary coagulant, coagulant aid, and filter aid** — the three roles federal sources actually name. "Settling aid" and "sludge conditioner" were **not** found in any federal document read in this pass and should be dropped from the claim.

### Gap summary

| # | Rebuild idea | Existing sources sufficient? | Live federal authority found? |
|---|---|---|---|
| a | different mechanisms, different timescales | partially | **yes — upgradeable to tier 1** (40 CFR 141.2; LT1 pp. 123–125) |
| b | rapid mix intensity and duration | yes (federal half); non-US half unnecessary | yes (LT1 p. 123; 815-R-20-004 p. 59) |
| c | velocity gradient G | **no** — sole tier-5 source | **yes** (LT1 p. 123; **EPA 815-R-99-012 p. 7-7**) |
| d | jar test can / cannot | partially; `claim-jar-sampling` mis-sourced | **yes** (**EPA 815-R-99-012 pp. 3-11, 6-25, 7-2, 7-3**) |
| e | turbidity as regulated performance measure | partially | **yes — tier 1** (40 CFR 141.170(a), 141.500; 815-R-20-004 p. 21, glossary) |
| f | what pin floc indicates | **no — cited source contains the term zero times** | **only as a failure indicator** (815-R-20-004 p. 101). Claim must be reversed or dropped. |
| g | coagulation ↔ filter run length | no | **yes** (**EPA 815-R-99-012 pp. 7-3, 7-9**; 815-R-20-004 pp. 65–66) |

Also confirmed, on searching for it and not finding it: **no federal source read in this pass contains a sludge-production factor of 0.26 mg/L per mg/L alum**, or any equivalent. `claim-sludge-factor` stays rejected. EPA 815-R-99-012 discusses residuals qualitatively (§6.7, §7.3.5) and gives coagulant equivalence stoichiometry (alum as Al₂(SO₄)₃·14H₂O, MW 594; ferric chloride as FeCl₃·6H₂O, MW 270, p. B-2 and §7) but no sludge yield factor. Likewise **no federal source read contains the teaching reaction equations** behind `claim-alum-reaction` or `claim-ferric-reaction`; those stay withheld.

---

## 7. Retrieval log

Every URL attempted in this pass, with outcome. Retrievals performed 2026-07-27.

### Regulatory

| URL | Result |
|---|---|
| `https://www.ecfr.gov/current/title-40/chapter-I/subchapter-D/part-141/subpart-P/section-141.173` | **302 → `https://unblock.federalregister.gov/`** (bot gate; not a dead link) |
| `https://www.ecfr.gov/current/title-40/chapter-I/subchapter-D/part-141/subpart-T/section-141.551` | **302 → `https://unblock.federalregister.gov/`** (bot gate) |
| `https://www.ecfr.gov/api/versioner/v1/titles.json` | 200 — title 40 `up_to_date_as_of` **2026-07-23** |
| `https://www.ecfr.gov/api/versioner/v1/full/2026-07-01/title-40.xml?part=141&section=141.173` | 200, 2,631 bytes — full text obtained |
| `…/2026-07-23/…&section=141.173` | 503 twice (rate limit), then **200 — byte-identical to 2026-07-01** |
| `…/2026-07-01/…&section=141.551` | 200, 2,978 bytes — full text obtained |
| `…/2026-07-23/…&section=141.551` | 503 (rate limit); currency confirmed instead via versions index |
| `…&section=141.170` | 200, 3,124 bytes |
| `…&section=141.500` | 200, 1,406 bytes |
| `…&section=141.550` | 200, 849 bytes |
| `…&section=141.552` | 200, 1,112 bytes |
| `…&section=141.553` | 503 (rate limit) — not needed |
| `…/2026-07-23/title-40.xml?part=141&section=141.2` | 200, 42,668 bytes — definitions obtained |
| `https://www.ecfr.gov/api/versioner/v1/versions/title-40.json?issue_date[gte]=2000-01-01&part=141` | 200 — no amendment to § 141.173 or § 141.551 since the 2016-12-28 baseline |
| `https://www.govinfo.gov/content/pkg/CFR-2024-title40-vol26/xml/CFR-2024-title40-vol26-sec141-173.xml` | **404** (wrong volume) |
| `https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol24/pdf/CFR-2025-title40-vol24-sec141-173.pdf` | redirect to `/error` |
| `https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol25/pdf/CFR-2025-title40-vol25-sec141-173.pdf` | **200**, 196,543 bytes — print text matches eCFR |
| `https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol25/pdf/CFR-2025-title40-vol25-sec141-551.pdf` | **200** — print text matches eCFR |
| `https://www.govinfo.gov/content/pkg/CFR-2025-title40-vol26/…` and `vol27/…` | redirect to `/error` |

### Package sources

| URL | Result |
|---|---|
| `/Users/apas/Downloads/owf-concept-001-v4_2.html` | present, 66,998 bytes |
| `https://www.pnws-awwa.org/wp-content/uploads/2024/06/Chemical-Mixing-Nothing-but-a-G-Thing.pdf` | **200**, PDF, 2,075,294 bytes — read |
| `https://pubmed.ncbi.nlm.nih.gov/16752769/` | **200**, 125,186 bytes — read |
| `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=16752769&rettype=abstract&retmode=text` | 200 — verbatim abstract |
| `https://www.deswater.com/DWT_articles/vol_51_issues_22-24_papers/51_22-24_2013_4729.pdf` | **404 — DEAD** |
| `https://www.deswater.com/vol.php?vol=51&iss=22-24` | 200 but redirects to `https://www.deswater.com/home.php` — issue index gone |
| `https://www.deswater.com/` | 200 → `home.php` |
| `https://doi.org/10.1080/19443994.2012.751883` | 200 → `https://linkinghub.elsevier.com/retrieve/pii/S1944398624188339` |
| `https://www.sciencedirect.com/science/article/pii/S1944398624188339` | **403 — PAYWALLED / blocked. Not read.** |
| `https://www.epa.gov/sites/default/files/2020-06/documents/swtr_turbidity_gm_final_508.pdf` | **200**, PDF, 3,050,847 bytes — full text extracted and read |
| `https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=30005ZHV.TXT` | 200 (980 bytes, JS redirect stub) |
| NEPIS ZyNET viewer for `30005ZHV` | **200**, 89,192 bytes — 254 pages, EPA 816-R-04-007 |
| NEPIS `ZyActionW=Download` text for `30005ZHV` | **200**, 498,717 bytes — full text read |
| `https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1009JLI.TXT` | 200 (980 bytes, JS redirect stub) |
| NEPIS `ZyActionW=Download` text for `P1009JLI` | **200**, 1,002,881 bytes — 375 pages, EPA 815-R-09-016, full text read |
| `https://www.epa.gov/pesticide-science-and-assessing-pesticide-risks/finalization-guidance-incorporation-water-treatment` | **200**, 208,873 bytes — read |

### Corroboration and gap-filling

| URL | Result |
|---|---|
| `https://www.epa.gov/dwreginfo/surface-water-treatment-rules` | 200 |
| `https://www.epa.gov/dwreginfo/guidance-manuals-surface-water-treatment-rules` | **200** — confirms EPA currently publishes 815-R-20-004 and 815-R-99-012 |
| `https://www.epa.gov/dwreginfo/turbidity-provisions` | **200** — links exactly the `swtr_turbidity_gm_final_508.pdf` URL in `sources.yaml` |
| `https://www.epa.gov/dwreginfo/long-term-1-enhanced-surface-water-treatment-rule-documents` | **200** — currently links EPA 816-R-04-007 |
| `https://www.epa.gov/dwreginfo/long-term-2-enhanced-surface-water-treatment-rule-documents` | **200** — currently links EPA 815-R-09-016 |
| `http://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=200021WV.txt` | **200**, PDF, 603,467 bytes, 237 pages — EPA 815-R-99-012, May 1999. Full text extracted and read. |
| `https://www.epa.gov/dwreginfo/drinking-water-treatment-plant-residuals-management` | **404** |
| `https://www.epa.gov/sdwa/optimization-program-drinking-water-systems` | 200 → `https://www.epa.gov/sdwa/drinking-water-optimization-program` |

### Search queries run (results used only to locate candidate URLs, never cited)

- `Aktas "polysilica iron" "polyaluminum chloride" velocity gradient rapid mixing time flocs Desalination and Water Treatment 2013`
- `EPA "pin floc" water treatment coagulation site:epa.gov` — surfaced no federal source; results were vendor and encyclopedia pages, none used
- `nepis.epa.gov "Optimizing Water Treatment Plant Performance Using the Composite Correction Program" 625/6-91/027` — surfaced `19january2017snapshot.epa.gov` and `19january2021snapshot.epa.gov` copies, **rejected as snapshot hosts** per §3.4

---

## 8. What a reader must not conclude from this document

- This is a source-verification pass. It is **not** the qualified technical or practitioner review required by gate 4 of the production contract, and it is not a legal or regulatory review.
- The Aktas 2013 paper was **not read**. Nothing here should be taken as confirming or refuting its contents.
- The Park 2006 paper was read **at abstract only**. Its methods, water matrix, and coagulant conditions were not reviewed.
- Recommended weakenings in §5 and §6 are recommendations. They have not been applied — no file in this package was modified by this pass.
- The § 141.173 / § 141.551 applicability findings are the federal frame only. State primacy requirements are out of scope for a public Concept Brief per the production contract and were not researched.
