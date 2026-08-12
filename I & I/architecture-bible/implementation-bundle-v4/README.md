# PumpOS and I&I Intelligence Version 4 Implementation Bundle

## Start here

This folder is the separately demarcated, agent-portable implementation instance derived from the
Version 3 technical Bible.

If you are using Claude, Kimi, Codex, or another development agent, begin with:

1. [`COPY-PASTE-AGENT-HANDOFF.md`](COPY-PASTE-AGENT-HANDOFF.md)
2. [`AGENTS.md`](AGENTS.md)
3. [`implementation-edition.md`](implementation-edition.md)
4. [`work-packages.yaml`](work-packages.yaml)
5. [`acceptance-matrix.yaml`](acceptance-matrix.yaml)

The first build target is intentionally bounded:

> Analyze one rainfall event for one sanitary-sewer basin, calculate the receiving pump-station
> consequence, preserve complete lineage, optionally reconcile SWMM and EPANET results, display the
> evidence, and prepare a human-reviewable recommendation.

## Relationship to Version 3

Version 3 explains the complete technical and architectural system. Version 4 does not replace it.
Version 4 converts the first operational slice into implementation contracts, work packages, API
shapes, test fixtures, and acceptance gates.

The governing source is:

- [`../ii-intelligence-system-bible-v3.md`](../ii-intelligence-system-bible-v3.md)

The Version 4 bundle must not be used to:

- certify any formula as production-ready;
- invent facility data;
- issue a compliance determination;
- operate a pump or control system;
- silently modify a SWMM or EPANET model;
- dispatch work without human approval;
- expand into drinking-water PipeOS work without a separately approved scope.

## Bundle map

| File or folder | Purpose |
| --- | --- |
| `AGENTS.md` | Binding instructions for any coding agent working in this folder |
| `COPY-PASTE-AGENT-HANDOFF.md` | Self-contained launch prompt for Claude, Kimi, Codex, or another agent |
| `implementation-edition.md` | Human-readable Version 4 product and technical specification |
| `work-packages.yaml` | Ordered engineering work with dependencies and definitions of done |
| `acceptance-matrix.yaml` | Requirement-to-test and requirement-to-evidence map |
| `openapi.yaml` | First-slice HTTP API contract |
| `agent-tools.yaml` | Bounded agent tool definitions and authority rules |
| `formula-contract-template.yaml` | Required shape for executable deterministic formula contracts |
| `schemas/` | JSON Schemas for requests, snapshots, results, model runs, findings, and approvals |
| `examples/` | Synthetic examples that exercise the contracts without claiming facility truth |
| `golden-cases/` | Golden-case structure and test-case register |
| `intake.yaml` | Owner direction and scope boundary |
| `sources.yaml` | Governed source inventory |
| `claims.yaml` | Material implementation claims and unresolved questions |
| `decisions.yaml` | Locked, proposed, and unresolved architecture decisions |
| `qa.yaml` | Automated and manual review record |
| `approvals.yaml` | Approval and release state |
| `tools/build_implementation_edition.py` | Deterministic compiled-document builder |
| `tools/validate_bundle.py` | Cross-file, schema, identifier, and completeness validator |

## Status

This is an internal implementation candidate. It is designed to let a development agent begin
bounded work without reinterpreting the whole Version 3 paper. Production engineering, model,
security, operator, regulatory, and owner approvals remain blocked.
