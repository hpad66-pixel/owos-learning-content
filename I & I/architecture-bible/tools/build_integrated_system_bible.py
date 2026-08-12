#!/usr/bin/env python3
"""Build the integrated I&I Intelligence System Bible from governed sources."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
ROOT = PACKAGE.parent


MANUAL_INPUTS: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "F-RDII-002": [
        ("Q_observed_t", "accepted wet-weather flow series", "declared flow unit", ["DS-01"]),
        ("Q_expected_DWF_t", "expected dry-weather flow series on the same clock", "same flow unit", ["DS-01"]),
        ("t_start, t_end", "approved event integration window", "timestamp", ["DS-01", "DS-02"]),
    ],
    "F-RDII-003": [
        ("V_RDII_gal", "integrated rainfall-derived event volume", "gal", ["DS-01"]),
        ("V_rain_gal", "rainfall volume over the matching area", "gal", ["DS-02", "DS-03"]),
    ],
    "F-PEAK-001": [
        ("Q_peak_wet_weather", "accepted or modeled peak wet-weather flow", "flow", ["DS-01", "DS-02"]),
        ("ADWF", "average dry-weather flow for the same boundary", "flow", ["DS-01"]),
    ],
    "F-RTK-002": [
        ("V_i", "rainfall-derived volume assigned to RTK component i", "volume", ["DS-02", "DS-03"]),
        ("T_i", "time from rainfall onset to component peak", "time", ["DS-01", "DS-02"]),
        ("K_i", "recession duration divided by time to peak", "dimensionless", ["DS-01", "DS-02"]),
        ("tau", "elapsed time since the rainfall increment", "time", ["DS-02"]),
    ],
    "F-RTK-003": [
        ("Q_i_m", "component hydrograph produced for component i and rainfall increment m", "flow", ["DS-01", "DS-02"]),
        ("t_m", "timestamp of rainfall increment m", "timestamp", ["DS-02"]),
        ("time_step", "approved convolution time step", "time", ["DS-01", "DS-02"]),
    ],
    "F-MASS-001": [
        ("sum(Q_in)", "all accepted inflows crossing the control boundary", "volume/time", ["DS-01"]),
        ("Q_local", "local flow generated inside the boundary", "volume/time", ["DS-01", "DS-03", "DS-04"]),
        ("sum(Q_out)", "all accepted outflows crossing the boundary", "volume/time", ["DS-01"]),
        ("S", "stored volume within the boundary", "volume", ["DS-07"]),
    ],
    "F-COST-001": [
        ("V_I_and_I_annual_MG", "annual I&I volume selected for the cost screen", "MG/year", ["DS-01", "DS-02", "DS-09"]),
        ("c_marginal_per_MG", "avoidable marginal conveyance and treatment cost", "currency/MG", ["DS-09"]),
    ],
    "F-PV-001": [
        ("CF_t", "benefit or cost cash flow in period t", "currency", ["DS-09"]),
        ("r", "discount rate on the declared real or nominal basis", "fraction/year", ["DS-09"]),
        ("t", "cash-flow period index", "year or declared period", ["DS-09"]),
        ("N", "analysis horizon", "periods", ["DS-09"]),
    ],
    "F-BCR-001": [
        ("PV_benefits", "present value of included benefits", "base-year currency", ["DS-09"]),
        ("PV_costs", "present value of included costs", "base-year currency", ["DS-09"]),
    ],
    "F-UNC-001": [
        ("J", "Jacobian of outputs with respect to uncertain inputs at the evaluation point", "output unit/input unit", ["DS-01", "DS-02", "DS-03", "DS-05", "DS-06", "DS-07", "DS-09"]),
        ("Sigma_x", "input covariance matrix", "squared input units and cross-covariances", ["DS-01", "DS-02", "DS-03", "DS-05", "DS-06", "DS-07", "DS-09"]),
    ],
    "F-VERIFY-001": [
        ("predicted_counterfactual", "modeled post-period response expected without rehabilitation", "flow or volume", ["DS-01", "DS-02", "DS-03", "DS-09"]),
        ("observed_post_response", "measured post-rehabilitation response", "same flow or volume unit", ["DS-01", "DS-02"]),
        ("hydrologic_covariates", "rainfall, antecedent, groundwater, seasonal, and operating controls used for comparability", "mixed", ["DS-01", "DS-02", "DS-03"]),
    ],
    "F-CONV-001": [
        ("Q", "flow value to convert", "gpm, gpd, MGD, or cfs", ["DS-01"]),
        ("conversion_constant", "registry-controlled exact conversion factor", "unit-specific", []),
    ],
    "F-GWI-001": [
        ("Q_DWF_measured", "measured dry-weather flow for the selected boundary and period", "flow", ["DS-01"]),
        ("Q_BWF_estimated", "estimated sanitary and process wastewater for the same boundary and period", "flow", ["DS-04"]),
    ],
    "F-IDM-001": [
        ("D_nominal_in", "declared diameter for each included sewer segment", "in", ["DS-03"]),
        ("L_mi", "included length of each sewer segment", "mi", ["DS-03"]),
        ("inventory_scope", "approved asset classes and effective boundary", "record", ["DS-03"]),
    ],
    "F-HYD-001": [
        ("D_in", "force-main internal diameter", "in", ["DS-06"]),
        ("Q_gpm", "trial or operating flow", "gpm", ["DS-01", "DS-05"]),
        ("nu_ft2_per_s", "kinematic viscosity for the represented fluid and temperature", "ft2/s", ["DS-06"]),
    ],
    "F-HYD-002": [
        ("Re", "Reynolds number", "dimensionless", ["DS-06"]),
        ("epsilon", "absolute internal roughness", "length", ["DS-06"]),
        ("D", "internal pipe diameter in the same length unit as roughness", "length", ["DS-06"]),
        ("transition_policy", "approved treatment for transition flow", "configuration", []),
    ],
    "F-HYD-003": [
        ("f", "Darcy friction factor", "dimensionless", ["DS-06"]),
        ("L", "force-main length", "ft", ["DS-06"]),
        ("D", "internal diameter", "ft", ["DS-06"]),
        ("v", "mean velocity", "ft/s", ["DS-01", "DS-06"]),
        ("g", "gravitational acceleration constant", "ft/s2", []),
    ],
    "F-HYD-004": [
        ("K_total", "sum of applicable fitting, valve, entrance, and exit loss coefficients", "dimensionless", ["DS-06"]),
        ("v", "mean velocity", "ft/s", ["DS-01", "DS-06"]),
        ("g", "gravitational acceleration constant", "ft/s2", []),
    ],
    "F-HYD-005": [
        ("H_static", "static head for the selected wet-well and discharge condition", "ft", ["DS-06", "DS-07"]),
        ("h_f(Q)", "major friction loss at trial flow Q", "ft", ["DS-06"]),
        ("h_m(Q)", "minor loss at trial flow Q", "ft", ["DS-06"]),
        ("H_other(Q)", "other approved flow-dependent or fixed head terms", "ft", ["DS-06"]),
    ],
    "F-PUMP-001": [
        ("pump_curve", "applicable single-pump head-versus-flow curve", "head by flow", ["DS-05"]),
        ("system_curve", "system head at each trial total flow", "head by flow", ["DS-06"]),
        ("N_operating", "number of hydraulically equivalent pumps operating", "count", ["DS-05", "DS-07"]),
        ("speed_and_configuration", "pump speed, impeller, and lineup represented", "record", ["DS-05", "DS-07"]),
    ],
    "F-PUMP-002": [
        ("Q_available", "available capacity under the named normal or contingency scenario", "flow", ["DS-05", "DS-06", "DS-07"]),
        ("Q_inflow", "accepted or modeled inflow under the same scenario", "flow", ["DS-01", "DS-02"]),
    ],
    "F-PUMP-003": [
        ("V_usable_gal", "usable storage between declared starting and limiting levels", "gal", ["DS-07"]),
        ("Q_inflow_gpm", "inflow used by the screen", "gpm", ["DS-01"]),
        ("Q_available_gpm", "available pumping capacity", "gpm", ["DS-05", "DS-06", "DS-07"]),
    ],
    "F-PUMP-004": [
        ("Q_inflow_gpm", "inflow used by the response-interval screen", "gpm", ["DS-01"]),
        ("Q_available_gpm", "available pumping capacity", "gpm", ["DS-05", "DS-06", "DS-07"]),
        ("t_response_min", "declared response interval", "min", ["DS-07"]),
    ],
    "F-PUMP-007": [
        ("Q_in_i, Q_in_i_plus_1", "inflow at the start and end of interval i", "flow", ["DS-01", "DS-02"]),
        ("Q_available_i", "available capacity during interval i", "flow", ["DS-05", "DS-06", "DS-07"]),
        ("delta_t_i", "interval duration", "time", ["DS-01"]),
        ("V_usable", "usable storage before the overflow boundary", "volume", ["DS-07"]),
        ("S_initial", "initial occupied or available storage state", "volume", ["DS-07"]),
    ],
    "F-PUMP-005": [
        ("V_working", "working storage between pump-off and pump-on levels", "gal", ["DS-07"]),
        ("Q_in", "constant inflow represented by the screen", "gpm", ["DS-01"]),
        ("Q_pump", "constant pump capacity", "gpm", ["DS-05", "DS-06"]),
    ],
    "F-PUMP-006": [
        ("V_pumped_gal", "pumped volume for the selected period", "gal", ["DS-01"]),
        ("Q_single_gpm", "representative single-pump capacity", "gpm", ["DS-05", "DS-06"]),
        ("Q_firm_gpm", "representative firm capacity", "gpm", ["DS-05", "DS-06"]),
    ],
    "F-MDC-NAPOT-001": [
        ("average_monthly_daily_average_aggregate_pump_operating_hours", "source-compliant operating-hour basis over the required period", "hr/day", ["DS-01", "DS-05", "DS-10"]),
        ("N_installed", "installed pump count under the applicable rule", "count", ["DS-05", "DS-10"]),
        ("rule_pack", "current applicable Miami-Dade instrument and special speed/power rules", "versioned record", ["DS-10"]),
    ],
    "F-ENERGY-001": [
        ("Q_gpm", "pump operating flow", "gpm", ["DS-01", "DS-05"]),
        ("H_ft", "total dynamic head at the operating point", "ft", ["DS-05", "DS-06"]),
        ("eta_pump", "pump efficiency at the operating point", "fraction", ["DS-05"]),
        ("eta_motor", "motor efficiency at the operating point", "fraction", ["DS-05"]),
        ("specific_gravity", "fluid specific gravity when materially different from one", "dimensionless", ["DS-06"]),
    ],
    "F-ENERGY-002": [
        ("kW_input(t)", "input-power time series or staged operating estimate", "kW", ["DS-05", "DS-06", "DS-08"]),
        ("time_intervals", "durations represented by each power value", "time", ["DS-08"]),
        ("tariff_USD_per_kWh", "applicable energy price for the declared tariff period", "currency/kWh", ["DS-08"]),
        ("demand_and_time_of_use_terms", "material non-energy tariff components", "currency basis", ["DS-08"]),
    ],
    "F-ECON-002": [
        ("Q_average_MGD", "average flow or modeled average reduction", "MGD", ["DS-01", "DS-09"]),
        ("days_in_analysis_year", "explicit 365- or 366-day basis", "day/year", ["DS-09"]),
    ],
    "F-ECON-003": [
        ("PV_benefits", "present value of included benefits", "base-year currency", ["DS-09"]),
        ("PV_costs", "present value of included costs", "base-year currency", ["DS-09"]),
    ],
    "F-ECON-004": [
        ("initial_capital_cost", "initial project capital cost", "currency", ["DS-09"]),
        ("annual_net_benefit", "annual included benefits less annual included costs", "currency/year", ["DS-09"]),
    ],
}


EXPLICIT_INPUT_SOURCES: dict[str, dict[str, list[str]]] = {
    "F-UNIT-001": {"P_in": ["DS-02"], "A_ac": ["DS-03"]},
    "F-FLOW-001": {"Q_i": ["DS-01"], "delta_t_i": ["DS-01"]},
    "F-DWF-001": {"Q_i": ["DS-01"], "delta_t_i": ["DS-01"]},
    "F-RDII-001": {"Q_observed_t": ["DS-01"], "Q_expected_DWF_t": ["DS-01"]},
    "F-NORM-001": {
        "Q_gpd": ["DS-01", "DS-04"],
        "D_in_segment": ["DS-03"],
        "L_mi_segment": ["DS-03"],
    },
    "F-RTK-001": {
        "R_i": ["DS-01", "DS-02"],
        "P_in": ["DS-02"],
        "A_ac": ["DS-03"],
        "T_i": ["DS-01", "DS-02"],
        "K_i": ["DS-01", "DS-02"],
    },
    "F-MANNING-001": {
        "A": ["DS-03"],
        "R_h": ["DS-03"],
        "S": ["DS-03"],
        "n": ["DS-03"],
        "k_n": [],
    },
}


CATEGORY_PURPOSE = {
    "unit_conversion": "Places unlike measurements on one declared unit basis so downstream mathematics compares the same physical quantity.",
    "time_series_integration": "Converts a sequence of time-stamped rates into a volume while preserving the actual interval lengths.",
    "baseline": "Builds the accepted dry-weather comparison condition used by later residual and screening calculations.",
    "RDII": "Separates or summarizes the part of wet-weather flow attributed to rainfall under the selected method.",
    "normalization": "Divides a selected flow or volume by an explicit inventory basis so comparable boundaries can be screened.",
    "screening": "Creates a comparison indicator that can flag a record for review but cannot make a design or compliance determination alone.",
    "RTK_unit_hydrograph": "Transforms rainfall into one or more timed response hydrographs using the approved RTK parameter set.",
    "mass_balance": "Enforces conservation of volume across a declared control boundary.",
    "gravity_hydraulics": "Estimates steady uniform open-channel flow under the formula's limited assumptions.",
    "force_main_hydraulics": "Builds the pressurized-pipe loss terms required by the station system curve.",
    "pump_station_hydraulics": "Finds the operating relationship between pump curves and the connected system.",
    "pump_station_capacity": "Compares named available pumping capacity with named inflow.",
    "pump_station_storage": "Calculates how a flow deficit consumes storage and may create modeled overflow.",
    "pump_station_controls": "Screens pump cycling for the specific control pattern stated by the formula.",
    "pump_station_operations": "Converts pumped volume into equivalent operating-time measures.",
    "jurisdiction_specific_pump_station_rule": "Applies a versioned Miami-Dade rule-pack method without turning it into a national formula.",
    "pump_station_energy": "Converts operating flow, head, efficiency, time, and tariff into power, energy, and cost.",
    "economics": "Places stated project costs and included benefits on a declared time and price basis.",
    "uncertainty": "Carries input uncertainty into an output uncertainty estimate within the method's mathematical limits.",
    "rehabilitation_verification": "Compares observed post-work performance with a defensible counterfactual rather than a raw before-and-after difference.",
    "dry_weather_decomposition": "Separates estimated base wastewater from measured dry-weather flow to estimate groundwater infiltration.",
}


def shift_headings(markdown: str, levels: int = 1) -> str:
    """Shift Markdown headings outside fenced code blocks."""
    output: list[str] = []
    in_fence = False
    for line in markdown.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            output.append(line)
            continue
        if not in_fence and line.startswith("#"):
            count = len(line) - len(line.lstrip("#"))
            if line[count : count + 1] == " ":
                line = "#" * min(6, count + levels) + line[count:]
        output.append(line)
    return "\n".join(output).strip() + "\n"


def display_expression(formula: dict[str, Any]) -> str:
    expression = formula.get("expression")
    expressions = formula.get("expressions")
    if expression:
        return str(expression)
    if isinstance(expressions, dict):
        return "\n".join(f"{name}: {value}" for name, value in expressions.items())
    return "No expression is recorded."


def source_names(source_ids: list[str], sources: dict[str, dict[str, Any]]) -> str:
    if not source_ids:
        return "Registry constant, approved configuration, or derived result"
    return "; ".join(f"{sid}, {sources[sid]['name']}" for sid in source_ids)


def formula_catalog(
    registry: dict[str, Any],
    manifest: dict[str, Any],
) -> str:
    sources = {item["id"]: item for item in manifest["source_classes"]}
    metrics = manifest["dashboard_metrics"]
    formulas = registry["formulae"]
    downstream: dict[str, list[str]] = {item["id"]: [] for item in formulas}
    for item in formulas:
        for dependency in item.get("dependencies", []):
            downstream.setdefault(dependency, []).append(item["id"])

    out = [
        "# Part IV. Formula-by-formula operational catalog",
        "",
        "This catalog is generated from `formula-register.yaml` and the operationalization manifest. "
        "The registry remains the formula authority. This section explains how each formula enters the application.",
        "",
    ]

    for index, formula in enumerate(formulas, start=1):
        fid = formula["id"]
        related_metrics = [m for m in metrics if fid in m.get("formula_ids", [])]
        registry_inputs = formula.get("inputs", [])
        inputs: list[tuple[str, str, str, list[str]]] = []
        if registry_inputs:
            for item in registry_inputs:
                symbol = str(item.get("symbol", ""))
                source_ids = EXPLICIT_INPUT_SOURCES.get(fid, {}).get(symbol)
                if source_ids is None:
                    source_ids = sorted(
                        {sid for m in related_metrics for sid in m.get("source_classes", [])}
                    )
                inputs.append(
                    (
                        symbol,
                        str(item.get("meaning", "")),
                        str(item.get("unit", "formula-specific")),
                        source_ids,
                    )
                )
        else:
            inputs = MANUAL_INPUTS.get(fid, [])

        out.extend(
            [
                f"## Formula {index}: {fid}, {formula['name'].replace('_', ' ')}",
                "",
                f"**Status:** `{formula['status']}`",
                "",
                f"**Category:** `{formula['category']}`",
                "",
                "**Why it exists:** "
                + CATEGORY_PURPOSE.get(
                    formula["category"],
                    "Produces a named intermediate or final result under the formula's recorded assumptions.",
                ),
                "",
                "**Equation or algorithm:**",
                "",
                "```text",
                display_expression(formula),
                "```",
                "",
                "### Inputs and where they come from",
                "",
                "| Symbol or record | Meaning | Unit or type | Operational source |",
                "| --- | --- | --- | --- |",
            ]
        )
        if inputs:
            for symbol, meaning, unit, source_ids in inputs:
                out.append(
                    f"| `{symbol}` | {meaning.replace('_', ' ')} | {unit or 'formula-specific'} | "
                    f"{source_names(source_ids, sources)} |"
                )
        else:
            out.append(
                "| Registry gap | The current formula registry does not enumerate operational inputs for this method. "
                "The formula cannot advance to production until the input contract is completed. | Not established | Not established |"
            )

        output = formula.get("output")
        if output:
            output_text = json.dumps(output, ensure_ascii=False)
        elif formula.get("expressions"):
            output_text = ", ".join(formula["expressions"].keys())
        else:
            output_text = "Not explicitly enumerated"

        out.extend(
            [
                "",
                "### Output and downstream use",
                "",
                f"**Output contract:** `{output_text}`",
                "",
                f"**Formula dependencies:** {', '.join(formula.get('dependencies', [])) or 'None. It starts from accepted inputs or configuration.'}",
                "",
                f"**Feeds downstream formulas:** {', '.join(downstream.get(fid, [])) or 'No dependency is declared in the current registry.'}",
                "",
            ]
        )
        if related_metrics:
            out.append(
                "**Numbered dashboard fields:** "
                + ", ".join(f"{m['id']} [{m['number']}] {m['label']}" for m in related_metrics)
            )
            out.append("")
            out.append(
                "**Decision uses:** "
                + " ".join(dict.fromkeys(m["decision_use"] for m in related_metrics))
            )
        else:
            out.append(
                "**Numbered dashboard fields:** None in the current sample. This is a supporting, optional, uncertainty, "
                "or verification formula and must not be displayed as if it ran."
            )

        for heading, key in (
            ("Assumptions and applicability", "assumptions"),
            ("Fail-closed conditions", "fail_closed_when"),
            ("What the result does not establish", "does_not_establish"),
        ):
            values = formula.get(key, [])
            if values:
                out.extend(["", f"### {heading}", ""])
                for value in values:
                    out.append(f"- {str(value).replace('_', ' ')}")

        source_basis = formula.get("source_basis")
        if source_basis:
            out.extend(
                [
                    "",
                    "### Formula provenance",
                    "",
                    "```yaml",
                    yaml.safe_dump(source_basis, sort_keys=False).strip(),
                    "```",
                ]
            )
        out.extend(
            [
                "",
                "**Production boundary:** The formula's registry status controls execution. "
                "A dashboard or agent cannot promote a candidate formula to production.",
                "",
            ]
        )
    return "\n".join(out).strip() + "\n"


def source_catalog(manifest: dict[str, Any]) -> str:
    out = [
        "# Part V. Source-to-input catalog",
        "",
        "An input is a measured value, approved record, model parameter, configuration, or prior calculation result "
        "consumed by a named formula. It is not merely a number typed into a box. Every input needs identity, units, "
        "time, boundary, quality, provenance, and an acceptance state.",
        "",
    ]
    for source in manifest["source_classes"]:
        out.extend(
            [
                f"## {source['id']}. {source['name']}",
                "",
                "**Possible systems of origin:** " + "; ".join(source["systems"]) + ".",
                "",
                "**Raw fields:** " + ", ".join(f"`{field}`" for field in source["raw_fields"]) + ".",
                "",
                "**Required quality controls:**",
                "",
            ]
        )
        out.extend(f"- {item.replace('_', ' ')}" for item in source["quality_requirements"])
        out.extend(
            [
                "",
                "**Wrangling rule:** The source adapter preserves the raw record, resolves identity, units, time, and "
                "boundary, assigns a quality state, and creates a canonical accepted observation or an explicit quarantine record.",
                "",
            ]
        )
    return "\n".join(out).strip() + "\n"


def dashboard_catalog(manifest: dict[str, Any]) -> str:
    out = [
        "# Part VI. Numbered dashboard values and complete lineage",
        "",
        "The number in square brackets is permanent within this candidate sample. It connects the dashboard mockup, "
        "sample result path, formula set, source class, evidence class, and decision use.",
        "",
        "## Numbered sample Basin and I&I dashboard",
        "",
        "```text",
        "┌────────────────────────────────────────────────────────────────────────────────────────────┐",
        "│ BASIN B-101 | SYNTHETIC EVENT EVENT-01 | NOT FACILITY DATA                                │",
        "├────────────────────────────────────────────────────────────────────────────────────────────┤",
        "│ [01] Rainfall depth             3.20 in      [02] Rainfall volume             55.612 MG     │",
        "│ [03] Average dry-weather flow   1.250 MGD    [04] Groundwater infiltration    0.250 MGD    │",
        "│ [05] Pipe inventory             412 in-mi    [06] Normalized GWI               606.8 gpd/IDM│",
        "│ [07] RDII event volume          1.780 MG     [08] Rainfall capture fraction    3.20%        │",
        "│ [09] Peak RDII                  2.704 MGD    [10] Peak total inflow             2,728.3 gpm │",
        "└────────────────────────────────────────────────────────────────────────────────────────────┘",
        "```",
        "",
        "## Numbered sample Station dashboard",
        "",
        "```text",
        "┌────────────────────────────────────────────────────────────────────────────────────────────┐",
        "│ STATION PS-SYNTH-01 | MAXIMUM STATIC-HEAD BASIS | SYNTHETIC                               │",
        "├────────────────────────────────────────────────────────────────────────────────────────────┤",
        "│ [11] One-pump capacity          2,994.3 gpm  [12] Two-pump firm capacity       4,129.8 gpm │",
        "│ [13] Peak margin                1,401.5 gpm  [14] Peak utilization             66.06%      │",
        "│ [15] One-pump normal storage    0 gal        [16] Derated capacity              2,245.7 gpm │",
        "│ [17] Derated required storage   75,312 gal   [18] Derated storage shortfall    30,312 gal  │",
        "│ [19] Outage required storage    81,848 gal   [20] Outage storage shortfall     36,848 gal  │",
        "│ [21] Time to exhaust storage    16.49 min    [22] Illustrative cycles           2.475/hr    │",
        "│ [23] Event energy               1,589.9 kWh  [24] Event energy cost             $190.79     │",
        "│ [25] Aggregate pump hours       6.892 hr/d   [26] Illustrative NAPOT            3.446 hr/d │",
        "└────────────────────────────────────────────────────────────────────────────────────────────┘",
        "```",
        "",
        "## Numbered sample Program and Economics dashboard",
        "",
        "```text",
        "┌────────────────────────────────────────────────────────────────────────────────────────────┐",
        "│ REHABILITATION SCENARIO REHAB-01 | HYPOTHETICAL | EXCLUDED BENEFITS SHOWN                 │",
        "├────────────────────────────────────────────────────────────────────────────────────────────┤",
        "│ [27] Annual modeled reduction   35.116 MG/yr [28] Gross marginal benefit       $22,826/yr  │",
        "│ [29] Annual net direct benefit -$97,174/yr [30] PV gross benefits              $339,586     │",
        "│ [31] PV total costs            $10,285,297 [32] NPV                           -$9,945,711   │",
        "│ [33] Benefit-cost ratio         0.033       [34] Simple payback                Not calculable│",
        "└────────────────────────────────────────────────────────────────────────────────────────────┘",
        "```",
        "",
        "## Metric-by-metric traceability",
        "",
        "| No. | Metric ID and dashboard label | Sample display | Result path | Source classes | Formula chain | Evidence class | Why and decision use |",
        "| ---: | --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for metric in manifest["dashboard_metrics"]:
        out.append(
            f"| {metric['number']} | `{metric['id']}` {metric['label']} | {metric['sample_display']} | "
            f"`{metric['result_path']}` | {', '.join(metric['source_classes'])} | "
            f"{', '.join(metric['formula_ids']) or 'Direct accepted input'} | {metric['evidence_class']} | "
            f"{metric['importance']} {metric['decision_use']} |"
        )
    out.extend(["", "## Decision wiring", ""])
    for decision in manifest["decision_bindings"]:
        out.extend(
            [
                f"### {decision['id']}. {decision['name']}",
                "",
                f"**Consumes:** {', '.join(decision['metric_ids'])}.",
                "",
                f"**Required human roles:** {', '.join(decision['required_roles'])}.",
                "",
                f"**Allowed output:** `{decision['output']}`.",
                "",
            ]
        )
    gaps = manifest.get("lineage_gaps", [])
    if gaps:
        out.extend(
            [
                "## Formula and lineage gaps exposed by dashboard wiring",
                "",
                "The dashboard binding audit found calculations or transformations used by the sample code that do "
                "not yet have a complete formula-registry contract. These are blockers, not documentation trivia.",
                "",
                "| Gap | Affected metrics | Missing contract | Required resolution |",
                "| --- | --- | --- | --- |",
            ]
        )
        for gap in gaps:
            out.append(
                f"| `{gap['id']}` | {', '.join(gap['metric_ids'])} | {gap['missing_contract']} | "
                f"{gap['required_resolution']} |"
            )
    return "\n".join(out).strip() + "\n"


def integration_spine() -> str:
    return """# I&I Intelligence System Bible

## Engineering calculation, operational architecture, data lineage, dashboard, and decision standard

**Document identifier:** OWOS-IISB-001

**Version:** 0.1.0, integrated governed candidate

**Date:** July 28, 2026

**Owner:** Hardeep Anand

**Engineering volume:** `../white-paper.md`

**Operational architecture volume:** `white-paper.md`

**Formula authority:** `../formula-register.yaml` version 0.2.0

**Sample calculation:** `../sample-basin.yaml` and `../generated/sample-basin-results.json`

**Release state:** Not approved for production calculations, facility use, or public release

---

## Executive integration thesis

This document joins the engineering paper and the operational Architecture Bible into one controlled
explanation. The engineering volume establishes how I&I and pump-station consequences are calculated.
The architecture volume establishes how accepted evidence reaches those calculations, how results enter
PumpOS, how GraphDB and manuals supply context, how Droobi assists, and how accountable people approve
action.

The new operationalization parts remove the gap between the papers. They define every source class,
every formula's inputs and outputs, every downstream dependency, and every numbered sample dashboard
value.

## The one traceability rule

Every dashboard value must resolve backward and forward:

```text
source system and source record
  -> raw preserved value
  -> identity, unit, time, and boundary normalization
  -> data-quality acceptance or quarantine
  -> calculation input snapshot
  -> formula and method version
  -> calculation output
  -> numbered dashboard field
  -> finding or comparison
  -> recommendation or draft
  -> human approval
  -> action
  -> completion and outcome evidence
```

If any link is absent, PumpOS must show the gap. Droobi may explain the gap. Neither may invent the
missing link.

## Canonical object lifecycle

```mermaid
flowchart LR
    REQ["AnalysisRequest"]
    SELECT["MethodSelectionDecision"]
    RUN["CalculationRun"]
    RESULT["CalculationResult"]
    FIND["Finding"]
    REC["Recommendation"]
    DRAFT["DraftAction"]
    APPROVE["ApprovalDecision"]
    ACTION["AuthorizedAction"]
    OUTCOME["OutcomeVerification"]

    REQ --> SELECT --> RUN --> RESULT --> FIND --> REC --> DRAFT --> APPROVE --> ACTION --> OUTCOME
```

An `AnalysisRequest` states the decision purpose and boundary. A `MethodSelectionDecision` records
why a method may run. A `CalculationRun` freezes inputs and versions. A `CalculationResult` contains
outputs and uncertainty. A `Finding` applies a named comparison or rule. A `Recommendation` is advice.
A `DraftAction` is not yet authorized. An `ApprovalDecision` records human authority. An
`AuthorizedAction` may reach a controlled downstream system. `OutcomeVerification` tests what happened.

## How to read this integrated Bible

- Part I contains the complete PumpOS and I&I operational Architecture Bible.
- Part II contains the complete I&I engineering calculation paper.
- Part III explains the operational input contract across all method chains.
- Part IV explains all 39 registered formulas one by one.
- Part V explains every source class and its wrangling requirements.
- Part VI numbers the sample dashboard values and traces each to source, formula, output, and decision.

The two original volumes remain governed sources. This integrated file is rebuilt from them so their
contents do not drift through manual copying.

---
"""


def operational_input_contract() -> str:
    return """# Part III. Complete operational input and output contract

## What is an input?

An input is anything a calculation consumes. It can be a direct measurement, an approved asset fact,
a model parameter, a versioned configuration, a rule-pack value, or an output from an upstream
formula. A value is not ready merely because it is numeric.

Every accepted input requires:

- a stable source and record identifier;
- a canonical asset, station, basin, event, or project identity;
- an explicit unit and physical dimension;
- a timestamp or effective period;
- a geographic and hydraulic boundary;
- a quality state;
- provenance and correction history;
- the method-specific acceptance decision; and
- an immutable snapshot hash for the calculation run.

## What is an output?

An output is a value, series, state, interval, warning, or refusal produced by a named formula or
method. An output can become an input to another formula only through a declared dependency. Display
rounding never becomes the downstream input.

## The major method chains

### Chain A. Rainfall to RDII

```text
rain-gauge increments + basin area
  -> F-UNIT-001 rainfall volume
  -> F-RTK-001 component volumes and durations
  -> F-RTK-002 component ordinates
  -> F-RTK-003 superposed RDII hydrograph
  -> F-FLOW-001 integrated RDII volume
  -> F-RDII-003 rainfall capture fraction
```

### Chain B. Measured flow to observed event residual

```text
accepted dry-weather flow series
  -> F-DWF-001 average dry-weather flow
wet-weather flow - expected dry-weather flow
  -> F-RDII-001 residual flow
  -> F-RDII-002 event volume
```

The observed residual and calibrated RTK hydrograph are related analytical paths. They are not
automatically interchangeable. Calibration compares the modeled hydrograph with accepted observations.

### Chain C. Dry-weather flow to groundwater infiltration and normalization

```text
measured dry-weather flow - estimated base wastewater
  -> F-GWI-001 groundwater infiltration
pipe diameters and lengths
  -> F-IDM-001 inch-diameter-mile inventory
groundwater infiltration / inventory
  -> F-NORM-001 normalized screening value
```

### Chain D. Pump and force-main operating point

```text
diameter + trial flow + viscosity
  -> F-HYD-001 area, velocity, Reynolds number
Reynolds number + roughness + diameter
  -> F-HYD-002 friction factor
friction factor + length + diameter + velocity
  -> F-HYD-003 major head loss
loss coefficients + velocity
  -> F-HYD-004 minor head loss
static head + losses
  -> F-HYD-005 system head curve
pump curve intersected with system curve
  -> F-PUMP-001 operating point
available capacity compared with event inflow
  -> F-PUMP-002 margin and utilization
```

### Chain E. Storage and contingency

```text
event inflow - available pumping
  -> F-MASS-001 storage rate
  -> F-PUMP-007 dynamic required storage and overflow

constant deficit + response time
  -> F-PUMP-004 required storage screen

usable storage / constant deficit
  -> F-PUMP-003 time-to-exhaust screen
```

### Chain F. Cycling, energy, and operating time

```text
working volume + inflow + pump capacity
  -> F-PUMP-005 cycling screen

operating flow + head + pump and motor efficiency
  -> F-ENERGY-001 input power
power over time + tariff
  -> F-ENERGY-002 energy and cost

pumped volume / representative capacity
  -> F-PUMP-006 equivalent operating hours
  -> F-MDC-NAPOT-001 only when the Miami-Dade rule pack applies
```

### Chain G. Rehabilitation economics

```text
modeled average reduction
  -> F-ECON-002 annual volume
annual volume × marginal cost
  -> F-COST-001 annual gross benefit
cash flows and discount rate
  -> F-PV-001 present values
present benefits - present costs
  -> F-ECON-003 net present value
present benefits / present costs
  -> F-BCR-001 benefit-cost ratio
initial cost / positive annual net benefit
  -> F-ECON-004 simple payback or fail-closed result
```

## Decision classes

The same output can support different decisions only when its method and evidence fit:

1. **Measurement acceptance:** Is the source record fit for this use?
2. **Screening:** Does the value justify more investigation?
3. **Engineering analysis:** Does a reviewed method support the stated comparison?
4. **Operations:** Is an approved response needed?
5. **Capital planning:** Is a scenario mature enough for alternatives analysis?
6. **Compliance support:** Does the current applicable instrument support the evaluated finding?

No dashboard color can promote a screening value into a design or compliance result.

---
"""


def build() -> Path:
    registry = yaml.safe_load((ROOT / "formula-register.yaml").read_text())
    manifest = yaml.safe_load((PACKAGE / "operationalization-manifest.yaml").read_text())
    architecture = (PACKAGE / "white-paper.md").read_text()
    engineering = (ROOT / "white-paper.md").read_text()
    dashboard_mockups = (PACKAGE / "dashboard-mockups.md").read_text()

    sections = [
        integration_spine(),
        "# Part I. PumpOS and I&I operational architecture\n\n",
        shift_headings(architecture, 1),
        "\n---\n\n# Part II. I&I engineering calculation standard\n\n",
        shift_headings(engineering, 1),
        "\n---\n\n",
        operational_input_contract(),
        "\n---\n\n",
        formula_catalog(registry, manifest),
        "\n---\n\n",
        source_catalog(manifest),
        "\n---\n\n",
        dashboard_catalog(manifest),
        "\n---\n\n",
        dashboard_mockups,
        "\n---\n\n# Integrated document status\n\n"
        "This is a governed candidate assembled from two candidate volumes and machine-readable registries. "
        "It does not change the production status of any formula, approve a jurisdiction rule, certify a "
        "facility, authorize autonomous action, or complete the unresolved independent and qualified reviews.\n\n"
        "## Current integrated white-paper score\n\n"
        "| Dimension | Available | Awarded | Evidence for points awarded | Deduction and next work |\n"
        "| --- | ---: | ---: | --- | --- |\n"
        "| Teaching thesis and importance | 15 | 15 | The engineering-to-operation thesis and reader consequences are explicit. | None for the candidate argument. |\n"
        "| Complete plain-language explanation | 20 | 20 | Both full source volumes, all method chains, 39 formula explanations, 11 source classes, 34 dashboard traces, and nine populated dashboard mockups are present. | Independent novice-reader review remains required as a hard gate. |\n"
        "| Utility-wide and cross-sector value | 15 | 14 | Operations, engineering, asset, compliance, executive, security, and capital decisions are connected. | PipeOS and treatment-system product-owner review remains open. |\n"
        "| Research depth and source quality | 15 | 11 | The integrated paper preserves federal and technical sources from the engineering volume and internal architecture sources from the operational volume. | Active PumpOS branch, live deployment, and several formula-source gaps remain unresolved. |\n"
        "| Technical accuracy and claim verification | 20 | 13 | Formula registry, test vectors, result paths, fail-closed boundaries, and six explicit lineage gaps are visible. | Candidate formulas, independent implementation, field calibration, and qualified engineering review remain blocked. |\n"
        "| Diagrams and visual teaching value | 10 | 10 | Mega architecture, sub-diagrams, method chains, nine populated dashboard mockups, and numbered traceability views are included. | Independent accessibility and usability review remains unresolved. |\n"
        "| Editorial quality, boundaries, and originality | 5 | 4 | Evidence classes, scope, prohibited conclusions, versioning, and release boundary are explicit. | Independent editorial and originality review remain unresolved. |\n"
        "| **Total** | **100** | **87** | Complete integrated candidate with machine-tested internal wiring. | Strong but not eligible for release or production approval. |\n\n"
        "- Previous integrated score: None\n"
        "- Score change: Initial integrated score\n"
        "- Decision band: 80 to 89, strong but revision and review required\n"
        "- Advancement decision: Candidate for owner and multidisciplinary technical review\n\n"
        "### Hard gates\n\n"
        "- Owner approval of the integrated thesis: blocked.\n"
        "- Complete formula contracts for six exposed lineage gaps: blocked.\n"
        "- Independent source and numerical verification: blocked.\n"
        "- Qualified I&I, pump-station, operations, regulatory, security, and software reviews: blocked.\n"
        "- Field calibration and holdout validation: blocked.\n"
        "- Rendered dashboard, accessibility, mobile, and novice review: blocked.\n"
        "- Production and public release: blocked.\n",
    ]
    output = PACKAGE / "ii-intelligence-system-bible.md"
    content = "".join(sections)
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    output.write_text(content)
    return output


if __name__ == "__main__":
    path = build()
    print(path)
