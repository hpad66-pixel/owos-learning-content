# PumpOS and I&I Intelligence Architecture Bible

This folder is the governed companion architecture package to the I&I technical manual in the
parent directory.

To begin implementation, open
[`implementation-bundle-v4/README.md`](implementation-bundle-v4/README.md). Version 4 is a
separately demarcated, agent-portable implementation instance derived from Version 3. It includes a
copy-paste handoff for Claude, Kimi, Codex, or another development agent, plus binding `AGENTS.md`
instructions, work packages, acceptance criteria, OpenAPI, JSON Schemas, golden-case structures,
security boundaries, and validation tooling.

A portable archive is available at
[`../output/bundles/pumpos-ii-implementation-bundle-v4.zip`](../output/bundles/pumpos-ii-implementation-bundle-v4.zip).

Start with [`ii-intelligence-system-bible-v3.md`](ii-intelligence-system-bible-v3.md). Version 3
preserves the complete Version 2 explanatory system, adds the complete 62-repository landscape, and
wires EPA SWMM and EPANET into the deterministic PumpOS calculation chain. It includes beginner
PySWMM and WNTR installation and execution runbooks, with-model and without-model scenarios,
model-service architecture, agent limits, reconciliation rules, and dashboard contracts `M-35`
through `M-44`.

The paginated PDF edition is available at
[`../output/pdf/ii-intelligence-system-bible-v3.pdf`](../output/pdf/ii-intelligence-system-bible-v3.pdf).
It is a searchable, tagged, 305-page US Letter document with rendered Mermaid diagrams, embedded
dashboard figures, bookmarks, headers, footers, and page numbering.

[`ii-intelligence-system-bible-v2.md`](ii-intelligence-system-bible-v2.md) is retained as the
narrative-first Version 2 candidate. It explains the complete evidence-to-action story, gives all
39 formulas an eight-part explanatory treatment, explains all 11 source classes, explains all 34
worked dashboard values and six decisions, makes RTK explicit in the master contents, and preserves
both source papers completely.

[`ii-intelligence-system-bible.md`](ii-intelligence-system-bible.md) is retained as the Version 1
specification-first candidate.

Open [`dashboard-mockups/index.html`](dashboard-mockups/index.html) to inspect the nine populated
development mockups and select any numbered value to reveal its source, formula chain, exact result
path, importance, and decision boundary.

Open [`open-source-repository-landscape.md`](open-source-repository-landscape.md) for the researched
landscape of 62 GitHub repositories relevant to SWMM, RDII/RTK, pump and system curves, force-main
hydraulics, optimization, GIS, telemetry, data lineage, and the bounded agent layer. It distinguishes
calculation engines from adapters, research code, and supporting infrastructure and maps the strongest
candidates to the Bible's formula families.

The two governed source volumes remain separately reviewable:

- [`../white-paper.md`](../white-paper.md): engineering methods, formulas, worked basin, and pump-station analysis
- [`white-paper.md`](white-paper.md): operational architecture, dashboards, agents, GraphDB, manuals, and implementation

Supporting records:

- `intake.yaml`: owner direction, scope, identity, and evidence boundary
- `sources.yaml`: source inventory and checksums
- `claims.yaml`: candidate material-claim inventory
- `decision-register.yaml`: proposed and inherited architecture decisions
- `diagram-register.yaml`: diagram jobs and truth boundaries
- `approvals.yaml`: approval and release state
- `qa.yaml`: automated and manual review status
- `operationalization-manifest.yaml`: source classes, numbered dashboard values, decisions, and lineage gaps
- `dashboard-mockups.md`: the nine populated dashboard figures and their metric wiring
- `dashboard-mockups/index.html`: selectable development prototype for all dashboard views
- `build-manifest.yaml`: reproducible input, tool, output, and validation hashes
- `build-manifest-v2.yaml`: Version 2 source-preservation, explanation-coverage, and output hashes
- `build-manifest-v3.yaml`: Version 3 model integration, source-preservation, and output hashes
- `explanatory-narrative-v2.md`: governed narrative spine used by the Version 2 builder
- `model-integration-v3.md`: detailed EPA SWMM, PySWMM, EPANET, WNTR, reconciliation, and dashboard chapter
- `examples/run_swmm_model.py`: companion beginner PySWMM command-line runner
- `implementation-bundle-v4/`: separately actionable software implementation specification and agent handoff
- `tools/build_dashboard_mockups.py`: deterministic dashboard and appendix builder
- `tools/capture_dashboard_mockups.cjs`: rendered screenshot and visible-value check
- `tools/build_integrated_system_bible.py`: deterministic integrated-document builder
- `tools/build_integrated_system_bible_v2.py`: narrative-first Version 2 builder
- `tools/build_integrated_system_bible_v3.py`: deterministic and model-layer Version 3 builder
- `tools/build_v3_pdf.cjs`: privacy-safe local HTML, Mermaid, and PDF renderer
- `tools/validate_operationalization.py`: formula, source, result-path, metric, and decision validator
- `tools/validate_system_bible_v2.py`: complete-source, RTK, and explanatory-coverage validator
- `tools/validate_system_bible_v3.py`: four-source, model-runbook, reconciliation, and dashboard validator

This package is an internal candidate. It does not amend the PumpOS Constitution, approve AWS,
authorize I&I production calculations, or authorize public release.
