# Final Federal Publication QA/QC

Brief: `owos:concept-brief:001`  
Edition: `1.0.0 current educational edition`
Evidence cutoff: 2026-07-26  
HTML: `dist/final-federal-publication.html`  
HTML SHA-256: recorded in `dist/final-federal-publication.build.json`

## Final verdict

The learner-facing content is approved as the current federal-only educational edition. Its
governing frame is limited to current United States federal requirements and EPA guidance. The AWWA
presentation is retained only as clearly labeled professional engineering context. No state
regulation, state training source, or state-specific requirement appears in the published HTML.

Technical/editorial confidence for the intended educational use: **95/100**.

This score is not a statistical probability or a substitute for a licensed engineer, operator,
chemist, regulatory counsel, or facility authority.

## Disposition of the 36 reviewed claims

| # | Claim topic | Final federal-publication action |
|---:|---|---|
| 1 | Different jobs of coagulation and flocculation | Retained with multiple-mechanism boundary. |
| 2 | Fine and colloidal particle stability | Retained with particle- and water-specific scope. |
| 3 | Federal filtered-water turbidity limits | Retained with exact 40 CFR source links and applicability warning. |
| 4 | 0.26 alum solids factor | Removed. It is too easy to misuse as total plant sludge production. |
| 5 | Turbidity as performance indicator | Retained; explicitly not described as a pathogen measurement. |
| 6 | Common negative colloid charge | Retained as common, not universal. |
| 7 | Charge reversal or restabilization | Removed from the narrative and interaction readout. |
| 8 | Floc breakage under excessive energy | Retained as a bounded EPA-supported principle without thresholds. |
| 9 | Universal zeta-potential range | Numeric claim rejected; only a nonnumeric facility-specific explanation remains. |
| 10 | Metal-coagulant mechanisms | Retained with chemistry and product limitations. |
| 11 | Polymer roles | Retained as application-specific, not a universal product rule. |
| 12 | Mean G equation | Equation withheld from the learner page; qualitative G explanation and AWWA context retained. |
| 13 | Tapered flocculation | Retained from EPA guidance without a state design rule. |
| 14 | Alkalinity and pH | Retained from EPA guidance with conditional wording. |
| 15 | Jar-test purpose | Retained as comparative evidence, not change authority. |
| 16 | Downstream consequences | Retained as a systems relationship, not a single-cause diagnosis. |
| 17 | Virginia rapid-mix requirement | Removed completely from claims, sources, narrative, and HTML. |
| 18 | United States flocculation context | Rewritten to EPA guidance only. |
| 19 | Park experimental timing | Omitted from the public lesson; retained only in the internal research record. |
| 20 | Aktas numeric values | Rejected and omitted. |
| 21 | G = 900 energy and shear diagnosis | Rejected and replaced by an evidence question. |
| 22 | Alum teaching equation | Detailed equation withheld. |
| 23 | Ferric teaching equation | Detailed equation withheld. |
| 24 | Pin floc as an intermediate | Retained with sample-location and downstream-result boundary. |
| 25 | PACl versus powdered activated carbon | Retained with first-use definition requirement. |
| 26 | Polymer charge class | Retained as insufficient by itself to assign product function. |
| 27 | Consistent jar-test sampling | Retained without presenting the outline as a complete SOP. |
| 28 | Reassessing dose after meaningful change | Retained without authorizing a dose change. |
| 29 | Written change procedure | Retained as OWOS recommended governance, not federal regulation. |
| 30 | Streaming current as direct zeta substitute | Rejected and omitted. |
| 31 | Time-aligned process dataset | Retained as a product and data-design recommendation. |
| 32 | Storm data predicting dose | Categorical claim rejected; page uses rainfall and intake data only as investigation evidence. |
| 33 | Role-specific actions | Retained as learning design. |
| 34 | Source visibility promise | Retained as publication governance. |
| 35 | Evidence boundary | Retained visibly. |
| 36 | No operating authorization | Retained visibly. |

## Public-source boundary

The public source manifest contains only:

- 40 CFR 141.173;
- 40 CFR 141.551;
- EPA Surface Water Treatment Rule Turbidity Guidance Manual;
- EPA Long Term 1 Enhanced Surface Water Treatment Rule guidance;
- EPA Long Term 2 Toolbox guidance; and
- Pacific Northwest Section AWWA and Carollo professional mixing context, labeled as neither a
  regulation nor a standard.

## Automated QA

- Structured package validation: passed.
- Deterministic compiler regression: passed.
- Public-output content and source-host audit: passed.
- Portfolio distinctiveness: passed.
- Rejected-phrase and state-authority scan: passed with zero matches.
- Desktop browser: passed at 1440 pixels with no page overflow.
- Tablet browser: passed at 820 pixels with no page overflow.
- Phone reduced-motion browser: passed at 390 pixels with no page overflow.
- Keyboard focus and drawer focus return: passed.
- Live interaction update: passed.
- Reduced-motion behavior: passed.
- No-JavaScript text equivalent and containment: passed.
- Community, related-learning, SOP-outline, and commercial mounts: present.
- Guided decision rehearsal: four authored steps rendered and operated successfully.
- Optional practice: clearly labeled, expandable, keyboard reachable, and excluded from completion.
- Rehearsal contrast: visually inspected after the pale comparison text was corrected.
- Direct course route: not connected because no governed coagulation or water-treatment course
  currently exists in the repository.

## Hard release boundary

The file is complete as the current owner-directed federal-only educational edition. The governed
release manifest cannot be issued yet because the repository still lacks a named independent
verifier, a qualified technical practitioner signoff, and the remaining required human
accessibility and release reviews. The compiler correctly reports zero formal verification coverage
until those records are supplied. This does not change the 95/100 educational-content verdict.
