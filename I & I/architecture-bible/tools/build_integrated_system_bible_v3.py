#!/usr/bin/env python3
"""Build Version 3 of the PumpOS and I&I Intelligence System Bible."""

from __future__ import annotations

import hashlib
from pathlib import Path

import yaml

import build_integrated_system_bible as v1
import build_integrated_system_bible_v2 as v2


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
ROOT = PACKAGE.parent


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def master_front() -> str:
    return """# PumpOS and I&I Intelligence System Bible

## Version 3: deterministic calculations, EPA SWMM, EPANET, dashboards, and governed agent behavior

**Owner:** APAS / One Water Operating System  
**Geographic scope:** Universal United States methods, with Miami-Dade examples kept in a separate jurisdiction-specific layer  
**Document class:** Technical development-grade white paper and governed implementation candidate  
**Version:** 3.0 candidate  
**Date:** July 28, 2026  
**Release state:** Internal candidate. Not approved for design, compliance, autonomous control, or public release.

---

# Executive orientation

Version 3 answers one architectural question: how should PumpOS combine transparent calculations with
network models without turning either one into an unexplained oracle?

The answer is a three-part method. PumpOS first performs the governed deterministic calculations in
the formula registry. EPA SWMM may then represent the rainfall, sewer, storage, surcharge, and
overflow behavior across time. EPANET may independently represent the pressurized pump and force-main
network. A reconciliation service compares observed, calculated, and modeled values before any result
is allowed onto a decision dashboard.

The models add system context. They do not erase the calculations. They do not repair bad source data.
They do not calibrate themselves. They do not approve their own results. Every model run must retain
its input snapshot, engine version, model-file hash, settings, quality findings, output lineage, and
review state.

# Master table of contents

## Book I. The connected story of I&I Intelligence

1. Start with the rain, not the software
2. The boundary gives every number its meaning
3. Data becomes evidence only after it is qualified
4. Establish ordinary flow before explaining the storm
5. RTK explains the shape of rainfall response
6. EPA SWMM routes the response through the represented sewer
7. The basin hydrograph becomes the station inflow
8. EPANET independently checks the pump and force-main operating point
9. Capacity, resilience, operations, energy, economics, and verification
10. The dashboard, agent, human decision, and measured outcome

## Book II. EPA SWMM, EPANET, and the governed model layer

1. Terms and architecture
2. EPA SWMM in detailed plain English
3. Installing and running EPA SWMM through PySWMM
4. EPANET in detailed plain English
5. Installing and running EPANET through WNTR
6. Formula-to-model wiring
7. With-model and without-model scenarios
8. Model outputs on the dashboards
9. Model services, agent authority, implementation, and acceptance

## Book III. Every formula explained

All 39 registered transformations, including RTK, RDII, mass balance, system curves, operating
points, capacity, storage, cycling, energy, economics, uncertainty, and verification.

## Book IV. Every source and input explained

All 11 governed source classes, their provenance, qualification, consumers, and limits.

## Book V. Every dashboard value and decision explained

All 34 worked-example metrics, six governed decisions, and the nine numbered dashboard mockups.

## Books VI through IX. Complete source and implementation record

- Book VI preserves the complete engineering source paper.
- Book VII preserves the complete operational Architecture Bible source paper.
- Book VIII preserves the complete 62-repository open-source landscape.
- Book IX preserves the machine-readable input, formula, source, dashboard, and mockup contracts.

---
"""


def narrative_with_model_bridges() -> str:
    narrative = (PACKAGE / "explanatory-narrative-v2.md").read_text()
    basin_marker = "## 6. The basin hydrograph becomes the station's inflow"
    resilience_marker = "## 7. Capacity alone does not answer resilience"
    swmm_bridge = """## 5A. EPA SWMM routes the response through the represented sewer

The RTK calculation creates a rainfall-derived response hydrograph at a declared boundary. A real
collection system may contain branches, trunks, manholes, storage, regulators, pumps, controls,
surcharged conduits, and possible overflow points. EPA SWMM adds that network-and-time context. It
can route runoff, sanitary flow, groundwater-related inflow, and RDII through a represented drainage
or sewer network and report how depth, flow, storage, surcharge, flooding, and continuity change
through the event.

In simple English, the deterministic calculation answers, "What response did the accepted inputs and
formula contract produce?" SWMM answers, "If that response moves through this represented network
under these declared conditions, what happens where and when?" PumpOS keeps both answers and compares
them with observations. It does not let a model output silently replace an accepted meter value or a
registered calculation.

The detailed installation, execution, calibration, output, assurance, and dashboard contracts appear
in Book II. At this point in the story, the important connection is that SWMM receives governed input
snapshots and returns governed model results. A result is not decision-eligible until the system knows
which model version ran, whether the run completed, whether continuity and calibration checks passed,
and what use the model was approved to support.

"""
    epanet_bridge = """## 6A. EPANET independently checks the pressurized pump and force-main problem

The PumpOS formula chain constructs a system curve and intersects it with the applicable pump curve.
EPANET adds a network solver for the pressurized side of the problem. It can represent pumps, pipes,
junctions, tanks, reservoirs, valves, demands, heads, flows, pressures, and energy behavior across a
connected pressure network. For a lift-station force main, that makes EPANET a useful independent
cross-check when the pressure system contains branches, multiple stations, changing boundary heads,
or controls that are difficult to reduce to one hand calculation.

EPANET does not calculate rainfall-derived I&I and does not replace SWMM's gravity-sewer routing. It
also does not make an unverified pump curve, roughness value, valve state, or elevation correct. Its
value is the ability to solve the connected pressure-network equations consistently and expose where
the simpler PumpOS calculation agrees or disagrees with the larger represented network.

Book II defines the exact adapter, result, reconciliation, and dashboard fields. The operating-point
comparison remains visible: PumpOS calculated flow and head, EPANET modeled flow and head, the
difference between them, and the assurance state that controls how the comparison may be used.

"""
    if narrative.count(basin_marker) != 1 or narrative.count(resilience_marker) != 1:
        raise ValueError("Version 2 narrative markers changed; model bridges cannot be inserted safely")
    narrative = narrative.replace(basin_marker, swmm_bridge + basin_marker)
    narrative = narrative.replace(resilience_marker, epanet_bridge + resilience_marker)
    return narrative


def source_completeness_note() -> str:
    return """# Version 3 source-volume completeness statement

Books VI, VII, and VIII are generated directly from the governed engineering paper, operational
Architecture Bible, and open-source repository landscape. The builder changes heading depth only.
It does not summarize, excerpt, or delete their paragraphs, formulas, tables, diagrams, glossary,
references, or appendices.

Book II is generated directly from the governed EPA SWMM and EPANET integration chapter. The Version
3 validator reconstructs and requires exact inclusion of all four source volumes. It also checks the
39 formula stories, 11 source stories, 34 worked-example dashboard metrics, six governed decisions,
ten new model-assurance metric contracts, both model bridges, the PySWMM and WNTR runbooks, and all
nine populated dashboard figures.

---
"""


def status_section() -> str:
    return """# Version 3 status and quality review

Version 3 is an integrated explanatory and implementation candidate. It adds governed model services,
not production authority. No model result in this document is presented as an observed field fact.
No SWMM or EPANET model has been calibrated or executed for the synthetic worked basin because an
approved `.inp` model, calibration record, and validation record are not part of the source package.

## Current white-paper score

| Dimension | Available | Awarded | Evidence for points awarded | Deduction and next work |
| --- | ---: | ---: | --- | --- |
| Thesis and importance | 15 | 15 | One story connects rainfall, RTK, SWMM, station inflow, PumpOS, EPANET, dashboards, decisions, and outcomes. | None for the candidate thesis. |
| Complete plain-language explanation | 20 | 20 | Formulas, sources, metrics, decisions, model engines, installation, execution, and failure modes are explained. | Independent novice-reader review remains a hard gate. |
| Utility-wide and product value | 15 | 14 | Engineering, operations, asset, executive, software, finance, and agent uses are connected. | Product-owner and operator acceptance remain open. |
| Research depth and source quality | 15 | 13 | Complete source papers, 62-repository landscape, and official SWMM, PySWMM, EPANET, and WNTR sources are connected. | Repository freshness and dependency security review remain recurring obligations. |
| Technical accuracy and claim verification | 20 | 14 | Deterministic and model responsibilities, run manifests, reconciliation, eligibility, and result paths are explicit. | Independent numerical implementation, calibration, holdout validation, and qualified engineering review remain blocked. |
| Diagrams and visual value | 10 | 10 | System, model-service, execution, scenario, dashboard, lineage, and nine populated dashboard views remain included. | Independent accessibility and usability review remains unresolved. |
| Editorial quality and boundaries | 5 | 5 | Observed, calculated, modeled, and reconciled results are kept separate and model limitations remain visible. | Public originality review remains required. |
| **Total** | **100** | **91** | Development-grade Version 3 candidate with mechanical source-preservation and coverage checks. | Not eligible for production or public release. |

## Hard gates

- Owner approval of Version 3: blocked.
- Independent source, formula, and numerical verification: blocked.
- Qualified I&I, collection-system, pump-station, hydraulic-modeling, operations, regulatory, cybersecurity, and software review: blocked.
- Basin-specific SWMM model construction, calibration, and holdout validation: blocked.
- Station-specific EPANET or WNTR model construction and field verification: blocked.
- Dependency scanning, model-worker isolation, and production threat review: blocked.
- Mobile, accessibility, usability, executive, and novice review: blocked.
- Production and public release: blocked.
"""


def write_manifest(output: Path, inputs: list[tuple[Path, str]]) -> None:
    content = output.read_text()
    manifest = {
        "artifact": "ii_intelligence_system_bible_v3_build_manifest",
        "version": "0.4.0",
        "status": "candidate",
        "generated_at": "2026-07-28",
        "builder": {
            "path": str((PACKAGE / "tools/build_integrated_system_bible_v3.py").relative_to(ROOT)),
            "sha256": sha256(PACKAGE / "tools/build_integrated_system_bible_v3.py"),
        },
        "validator": {
            "path": str((PACKAGE / "tools/validate_system_bible_v3.py").relative_to(ROOT)),
            "sha256": sha256(PACKAGE / "tools/validate_system_bible_v3.py"),
        },
        "inputs": [
            {
                "path": str(path.relative_to(ROOT)),
                "role": role,
                "sha256": sha256(path),
            }
            for path, role in inputs
        ],
        "output": {
            "path": str(output.relative_to(ROOT)),
            "sha256": sha256(output),
            "lines": len(content.splitlines()),
            "words": len(content.split()),
            "bytes": len(output.read_bytes()),
        },
        "validation": {
            "command": "python3 architecture-bible/tools/validate_system_bible_v3.py",
            "status": "pending",
            "complete_source_volumes": 4,
            "formula_explanations": 39,
            "source_class_explanations": 11,
            "worked_dashboard_metric_explanations": 34,
            "model_assurance_metric_contracts": 10,
            "decision_explanations": 6,
            "populated_dashboard_figures": 9,
        },
        "release": {
            "approved": False,
            "reason": (
                "Owner, qualified engineering and modeling, source, security, regulatory, "
                "accessibility, usability, calibration, and field-validation reviews remain open."
            ),
        },
    }
    (PACKAGE / "build-manifest-v3.yaml").write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=False)
    )


def build() -> Path:
    registry = yaml.safe_load((ROOT / "formula-register.yaml").read_text())
    manifest = yaml.safe_load((PACKAGE / "operationalization-manifest.yaml").read_text())
    engineering_path = ROOT / "white-paper.md"
    architecture_path = PACKAGE / "white-paper.md"
    model_path = PACKAGE / "model-integration-v3.md"
    landscape_path = PACKAGE / "open-source-repository-landscape.md"
    narrative_path = PACKAGE / "explanatory-narrative-v2.md"
    dashboards_path = PACKAGE / "dashboard-mockups.md"

    formula_book = v2.explanatory_formula_book(registry, manifest).replace(
        "# Book II. Every formula explained",
        "# Book III. Every formula explained",
        1,
    )
    source_book = v2.explanatory_source_book(manifest).replace(
        "# Book III. Every source and input explained",
        "# Book IV. Every source and input explained",
        1,
    )
    dashboard_book = v2.explanatory_dashboard_book(manifest).replace(
        "# Book IV. Every dashboard value and decision explained",
        "# Book V. Every dashboard value and decision explained",
        1,
    )

    sections = [
        master_front(),
        narrative_with_model_bridges(),
        "\n---\n\n",
        model_path.read_text(),
        "\n---\n\n",
        formula_book,
        "\n---\n\n",
        source_book,
        "\n---\n\n",
        dashboard_book,
        "\n---\n\n",
        source_completeness_note(),
        "# Book VI. Complete engineering source volume\n\n",
        v1.shift_headings(engineering_path.read_text(), 1),
        "\n---\n\n# Book VII. Complete operational Architecture Bible source volume\n\n",
        v1.shift_headings(architecture_path.read_text(), 1),
        "\n---\n\n# Book VIII. Complete open-source repository landscape\n\n",
        v1.shift_headings(landscape_path.read_text(), 1),
        "\n---\n\n# Book IX. Machine-readable operational contracts\n\n",
        v1.operational_input_contract().replace("# Part III.", "## Contract 1."),
        "\n---\n\n",
        v1.formula_catalog(registry, manifest).replace("# Part IV.", "## Contract 2."),
        "\n---\n\n",
        v1.source_catalog(manifest).replace("# Part V.", "## Contract 3."),
        "\n---\n\n",
        v1.dashboard_catalog(manifest).replace("# Part VI.", "## Contract 4."),
        "\n---\n\n",
        dashboards_path.read_text().replace("# Part VII.", "## Contract 5."),
        "\n---\n\n",
        status_section(),
    ]
    content = "".join(sections)
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    output = PACKAGE / "ii-intelligence-system-bible-v3.md"
    output.write_text(content)

    write_manifest(
        output,
        [
            (engineering_path, "complete_engineering_source_volume"),
            (architecture_path, "complete_operational_architecture_source_volume"),
            (narrative_path, "connected_narrative_spine"),
            (model_path, "swmm_epanet_model_integration_volume"),
            (landscape_path, "complete_open_source_repository_landscape"),
            (ROOT / "formula-register.yaml", "formula_authority"),
            (PACKAGE / "operationalization-manifest.yaml", "source_metric_and_decision_authority"),
            (dashboards_path, "populated_dashboard_appendix"),
        ],
    )
    return output


if __name__ == "__main__":
    print(build())
