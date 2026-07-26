# Perplexity Candidate-Evidence Review

Brief: `owos:concept-brief:001`  
Review date: 2026-07-25  
Stage: candidate research completed; original-source verification in progress  
Publication effect: none

## Research run

Thirty-two pending material claims were divided into four traceable Deep Research jobs:

| Cluster | Perplexity job | Cost (USD) |
|---|---|---:|
| Foundational mechanisms | `ac2287b4-5a69-4a12-a06c-4124c0f59de1` | 0.73541 |
| Regulation, design, and control | `00bbaec4-c565-455d-bb02-4d8e0230f342` | 0.79433 |
| Chemicals, measurement, and material balance | `84514734-c951-4196-b91e-82d7a395128f` | 0.77736 |
| Studies, operations, and boundaries | `c050651b-1cc2-420f-84ff-ff307071564b` | 0.78025 |
| **Recorded total** |  | **3.08735** |

The raw receipts are retained under `research/perplexity/`. They are candidate-source discovery
records. They do not verify a claim.

## Source screening

Useful United States original or official candidates include:

- U.S. EPA, *Guidance Manual for Compliance with the Surface Water Treatment Rules: Turbidity
  Provisions*, EPA 815-R-20-004, June 2020.
- Current electronic Code of Federal Regulations provisions in 40 CFR Part 141.
- Virginia Administrative Code 12VAC5-590-871.
- California State Water Resources Control Board, *Jar Testing Made Easy*.
- Kentucky Department for Environmental Protection, *Surface Water Treatment Operator
  Certification Manual*.
- U.S. EPA enhanced-coagulation, cyanotoxin-optimization, and comprehensive-performance-evaluation
  material.
- PubMed records and original papers for the Park and Aktas experiments, treated as research only.

The following candidate classes are quarantined from governing evidence:

- Canadian, Australian, Irish, United Kingdom, Indian, and other non-United States standards,
  government guidance, design guides, and operator guidance;
- vendor and equipment-manufacturer pages;
- Facebook, Quizlet, Scribd, generic study sites, and commercial explainers;
- snippets that do not resolve to the original paper or authority; and
- Perplexity's own synthesized wording.

## Claim-level research disposition

These are research dispositions, not final verification decisions.

| Claim | Candidate disposition | Required next action |
|---|---|---|
| `claim-distinct-jobs` | Supported in principle | Verify exact coagulation and flocculation definitions in US official and professional sources. |
| `claim-particle-stability` | Supported in principle | Retain the bounded word “some”; verify colloid and settling language. |
| `claim-charge` | Supported with qualification | Retain “many common colloids”; do not universalize particle charge. |
| `claim-restabilization` | Plausible but not adequately traced | Find and inspect an original professional or peer-reviewed source. |
| `claim-coagulant-mechanisms` | Supported in principle | Verify hydrolysis, adsorption, charge neutralization, and sweep-floc mechanisms separately. |
| `claim-alkalinity` | Supported | Verify exact EPA or state-manual locators and avoid universal pH ranges. |
| `claim-pin-floc` | Weakly supported | Define the term and verify that the described condition is intentionally intermediate in the stated process. |
| `claim-downstream` | Supported | Map each downstream consequence to an exact official locator. |
| `claim-us-filtered-water-turbidity` | Supported only with applicability language | Cite the controlling 40 CFR provisions and distinguish covered technologies and system-size rules. |
| `claim-turbidity-proxy` | Supported with careful wording | Describe turbidity as a treatment-performance indicator, not a pathogen measurement or complete microbial-risk proxy. |
| `claim-g-equation` | Perplexity output contains a technical error | Reject the synthesized linear formula. Verify the square-root form, variables, units, and bulk-average limitation from original engineering sources. |
| `claim-tapered-flocculation` | Supported | Use EPA June 2020 manual page 60 and Virginia 12VAC5-590-871(B)(2)(e), with Virginia clearly state-specific. |
| `claim-virginia-design-basis` | Directly supported | Use exact Virginia subsections A(3) and A(3)(a); retain Virginia-only applicability. |
| `claim-us-flocculation-design-context` | Supported | Separate federal guidance from state requirements and professional recommendations. |
| `claim-jar-purpose` | Partly supported | Verify claims about source variation, full-scale representation, filterability, and pilot confirmation independently. |
| `claim-jar-sampling` | Supported | Use the California procedure's explicit settling and sampling steps without presenting its example settings as universal. |
| `claim-sludge-factor` | Not supported by the returned original source | Do not publish 0.26 mg/L per mg/L as a universal factor. Locate the exact stoichiometric basis or remove it. |
| `claim-zeta-range` | Numeric range not adequately supported | Remove or sharply bound the minus 15 to minus 30 mV range unless a suitable original source and application scope are found. |
| `claim-polymer-role` | Partly supported | Verify each claimed role and distinguish drinking-water, wastewater, residuals, and product-specific uses. |
| `claim-alum-reaction` | Chemically plausible, authority weak | Verify hydration convention, stoichiometry, units, and teaching limitations in an authoritative US source. |
| `claim-ferric-reaction` | Unsupported synthesis | Perplexity proposed a reaction without an adequate original citation. Independently verify or omit. |
| `claim-pacl-pac` | Distinction supported | Use unambiguous terms such as `PACl` and “powdered activated carbon”; explain that industry abbreviations vary. |
| `claim-polymer-charge-roles` | Supported by research | Inspect the original paper and retain molecular weight, charge density, dose, water, and particle limitations. |
| `claim-streaming-current-proxy` | Current wording is not supportable | Streaming current is not automatically a direct substitute for zeta potential. Rewrite as distinct, potentially correlated electrokinetic measurements with application-specific calibration. |
| `claim-shear` | Supported with application-specific limits | Use EPA and original research; do not convert experimental thresholds into plant setpoints. |
| `claim-park-study` | Abstract supports the reported sequence | Verify the exact title, particle-size definitions, alum dose, G, timing, and experimental boundary. |
| `claim-aktas-study` | Specific numbers not yet verified | Inspect the full original paper before retaining 546 or 390 per second. |
| `claim-energy-audit` | Overstated interpretation | A PACl rapid-mix G of 900 per second does not by itself prove wasted energy or floc shearing. Reframe as a diagnostic question requiring site evidence. |
| `claim-dose-year-round` | Supported in principle | Tie reassessment to documented changes in source water, temperature, pH, alkalinity, flow, chemical, or treatment objectives. |
| `claim-dose-change-sop` | Governance position, not established external fact | Label as OWOS recommended governance and support it with facility authority, monitoring, rollback, and approval boundaries. |
| `claim-evidence-boundary` | Internally demonstrable | Verify against the package's actual evidence and review state, not Perplexity. |
| `claim-no-operating-advice` | Internally demonstrable | Keep the boundary visible until site-specific authority and qualified approval exist. |

## Confirmed research quality issue

The regulation/design Perplexity report stated one version of the mean velocity-gradient equation as
`G = P / (μV)`. That is dimensionally inconsistent with the conventional square-root expression
declared in the claim register. This candidate wording is rejected. It demonstrates why Perplexity
is a discovery service and why original-source technical verification remains mandatory.

## Current gate

No cited HTML may be generated from these findings yet. The next gate requires:

1. direct retrieval and preservation of each used original source;
2. exact page, section, table, figure, or paragraph locators;
3. bounded claim wording aligned to those originals;
4. an independent source trace;
5. qualified United States technical review; and
6. approval of the evidence-backed narrative and storyboard.
