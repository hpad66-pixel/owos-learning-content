#!/usr/bin/env python3
"""Build the narrative-first Version 2 I&I Intelligence System Bible."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

import build_integrated_system_bible as v1


HERE = Path(__file__).resolve().parent
PACKAGE = HERE.parent
ROOT = PACKAGE.parent


FORMULA_STORIES: dict[str, tuple[str, str, str]] = {
    "F-UNIT-001": (
        "How much rain fell over the declared basin?",
        "The formula converts rainfall depth and basin area into a physical rainfall volume. It creates the common volume basis needed before any rainfall-capture or RTK calculation can be interpreted.",
        "The result conveys the storm volume available over the basin. It does not say that the same volume entered the sewer.",
    ),
    "F-FLOW-001": (
        "How much volume passed when the measured flow rate changed over time?",
        "The formula connects adjacent flow observations with trapezoids and adds their areas. It respects unequal time intervals instead of pretending every sample represents the same duration.",
        "The result conveys integrated volume over the accepted window. Its accuracy depends on the clock, gaps, units, and event boundaries.",
    ),
    "F-DWF-001": (
        "What flow rate represents the accepted dry-weather period?",
        "The formula calculates a time-weighted mean, giving each observation influence in proportion to the time it represents. This becomes the ordinary-flow baseline used to separate event response.",
        "The result conveys the selected baseline under the approved days and exclusions. It is not proof that dry-weather flow contains no infiltration.",
    ),
    "F-RDII-001": (
        "At each time step, how much observed flow remains after expected dry-weather flow is removed?",
        "The formula subtracts the expected dry-weather hydrograph from the observed wet-weather hydrograph on the same clock. The remainder is the observed rainfall-related residual under that baseline method.",
        "The result conveys a time series that can be integrated and compared with a model. It does not identify the physical entry defect.",
    ),
    "F-RDII-002": (
        "How many gallons of event-related residual flow occurred?",
        "The formula integrates the accepted RDII residual over the approved event window. It turns a changing residual rate into the event volume used by storage, capture, and rehabilitation analyses.",
        "The result conveys event-related volume above the selected baseline. A different baseline or event window can change it.",
    ),
    "F-RDII-003": (
        "What fraction of basin rainfall volume appeared as RDII?",
        "The formula divides integrated RDII volume by rainfall volume over the matching basin. It creates a dimensionless event-response measure that can support comparison and RTK calibration.",
        "The result conveys the event's modeled or observed capture relationship. It does not establish a universal rate for future storms.",
    ),
    "F-NORM-001": (
        "How large is the selected flow relative to the declared sewer inventory?",
        "The formula divides flow by inch-diameter-miles so differently sized inventories can be screened on a common basis when their boundaries and asset classes match.",
        "The result conveys a normalized comparison value. It is not a national pass or fail criterion.",
    ),
    "F-PEAK-001": (
        "How large was the wet-weather peak compared with ordinary average flow?",
        "The formula divides peak wet-weather flow by average dry-weather flow. It compresses two flow conditions into a screening ratio that helps identify unusually strong event response.",
        "The result conveys relative peak intensity. It does not separate RDII, diagnose a defect, or establish available station capacity.",
    ),
    "F-RTK-001": (
        "How much volume belongs to each RTK component, and how long does that component last?",
        "The formula uses R to allocate rainfall volume, T to place the peak in time, and K to extend the recession. It creates the volume and duration that define each triangular response component.",
        "The result conveys the size and time span of an assumed or calibrated response component. It does not prove a physical defect type.",
    ),
    "F-RTK-002": (
        "What flow does one RTK triangle contribute at each elapsed time?",
        "The formula converts component volume and duration into a peak rate, then describes the linear rise to T and linear recession over K times T. The triangle's area closes to its component volume.",
        "The result conveys one component hydrograph. It becomes useful only when its units, time step, and parameter basis are controlled.",
    ),
    "F-RTK-003": (
        "What complete RDII hydrograph results from the full rainfall time series?",
        "The formula shifts every short, medium, and long component response to the time of its rainfall increment and adds all concurrent contributions. This is the superposition step that turns a storm into a continuous modeled response.",
        "The result conveys the modeled timing and magnitude of RDII through the event. It must be calibrated and checked against accepted observations before predictive use.",
    ),
    "F-MASS-001": (
        "Where did the water inside the declared control volume go?",
        "The formula enforces conservation: inflow plus locally generated flow minus outflow equals the rate of storage change. It prevents the application from creating or losing unexplained volume.",
        "The result conveys accumulation or depletion inside the boundary. The boundary and every crossing flow must be explicit.",
    ),
    "F-MANNING-001": (
        "What steady uniform gravity flow can the represented conduit carry?",
        "The formula relates area, hydraulic radius, slope, and roughness under Manning's assumptions. It supports bounded gravity-capacity screening where uniform-flow conditions are defensible.",
        "The result conveys an idealized gravity-flow capacity. It does not replace dynamic modeling under surcharge, backwater, controls, or complex transitions.",
    ),
    "F-COST-001": (
        "What annual avoidable marginal cost is associated with the selected I&I volume?",
        "The formula multiplies annual I&I volume by an approved marginal cost per million gallons. It connects hydraulic volume with the cost that may actually change if that volume is avoided.",
        "The result conveys a narrow gross direct-cost screen. Average treatment cost and marginal avoidable cost are not automatically interchangeable.",
    ),
    "F-PV-001": (
        "What is a future benefit or cost worth on the declared base-date basis?",
        "The formula discounts each future cash flow by the approved rate and timing convention. It allows costs and benefits occurring in different years to be compared on one time basis.",
        "The result conveys present value under the declared real or nominal assumptions. It does not prove that the forecast cash flows will occur.",
    ),
    "F-BCR-001": (
        "How many dollars of included present benefit exist per dollar of included present cost?",
        "The formula divides present benefits by present costs. It provides a scale-independent economic comparison when both sides use the same scope and discount basis.",
        "The result conveys the relationship between included benefits and costs. Omitted benefits, transfers, and risk terms remain omitted.",
    ),
    "F-UNC-001": (
        "How does uncertainty in the inputs affect uncertainty in the calculated output?",
        "The formula uses local sensitivities and the input covariance matrix to approximate output covariance. It carries both individual input uncertainty and declared correlation into the result.",
        "The result conveys a first-order uncertainty estimate near the evaluation point. It can be unreliable for strong nonlinearity, discontinuities, or poorly described input distributions.",
    ),
    "F-VERIFY-001": (
        "Did measured performance improve relative to what would likely have happened without the work?",
        "The method compares observed post-work response with a weather-normalized counterfactual. It prevents a smaller storm, seasonal change, or different groundwater condition from being mistaken for project success.",
        "The result conveys estimated change under the verification design. It is not a simple before-and-after subtraction.",
    ),
    "F-CONV-001": (
        "Are all connected calculations using the same flow unit?",
        "The formula applies registry-controlled conversion constants among gpm, gpd, MGD, and cfs. It prevents silent unit mismatches from propagating through the system.",
        "The result conveys the same physical flow in a different unit. Conversion changes representation, not the underlying quantity or evidence quality.",
    ),
    "F-GWI-001": (
        "How much measured dry-weather flow remains after supported base wastewater is removed?",
        "The formula subtracts estimated base wastewater flow from measured dry-weather flow for the same period and service boundary. The remainder is the method-dependent groundwater-infiltration estimate.",
        "The result conveys a dry-weather decomposition. It does not locate defects and is sensitive to the base-wastewater method.",
    ),
    "F-IDM-001": (
        "What sewer inventory denominator represents both pipe size and length?",
        "The formula sums nominal diameter in inches multiplied by length in miles for every included segment. It creates the denominator used by inch-diameter-mile normalization.",
        "The result conveys the declared inventory scale. It is meaningful only with explicit asset classes, duplicates, abandoned segments, and effective date.",
    ),
    "F-HYD-001": (
        "At a trial flow, what are the force-main area, velocity, and Reynolds number?",
        "The formula converts internal diameter into area, divides flow by area to obtain mean velocity, and combines velocity, diameter, and viscosity to determine flow regime.",
        "The result conveys the hydraulic state needed by friction calculations. Wrong diameter or fluid-property assumptions affect every downstream head result.",
    ),
    "F-HYD-002": (
        "What Darcy friction factor represents the trial hydraulic condition?",
        "The formula selects or solves the appropriate friction relationship using Reynolds number and relative roughness. The friction factor translates flow regime and pipe condition into resistance.",
        "The result conveys a dimensionless resistance term. Transition flow, roughness uncertainty, and extrapolation policy must remain visible.",
    ),
    "F-HYD-003": (
        "How much head is lost through straight force-main length?",
        "The Darcy-Weisbach formula combines friction factor, length-to-diameter ratio, and velocity head. Because velocity is squared, higher flow can raise loss rapidly.",
        "The result conveys major friction head loss at one flow. It feeds the system curve and changes when diameter, roughness, length, or flow changes.",
    ),
    "F-HYD-004": (
        "How much head is lost through fittings, valves, entrances, and exits?",
        "The formula multiplies the total applicable loss coefficient by velocity head. It captures localized resistance not represented by straight-pipe friction.",
        "The result conveys minor head loss at one flow. The word minor does not mean negligible; the total coefficient must represent the actual lineup.",
    ),
    "F-HYD-005": (
        "How much total head must the station overcome at each flow?",
        "The formula adds static head, major loss, minor loss, and any other approved head terms. Repeating it across trial flows produces the system head curve.",
        "The result conveys the connected system's demand on the pumps. It changes with levels, valve state, geometry, roughness, and configuration.",
    ),
    "F-PUMP-001": (
        "At what flow and head do the operating pumps and connected system balance?",
        "The method finds the intersection of the applicable pump curve and system curve. For parallel identical pumps, total flow is divided among operating pumps under the stated assumptions.",
        "The result conveys a modeled operating point for one lineup and condition. It is not the pump's nameplate capacity or a universal station capacity.",
    ),
    "F-PUMP-002": (
        "How much available capacity remains above inflow, and what fraction is being used?",
        "The formula subtracts inflow from named available capacity and divides inflow by capacity. Margin and utilization describe the same comparison in absolute and relative terms.",
        "The result conveys the capacity position for one event and configuration. A favorable normal margin does not resolve outage or derating resilience.",
    ),
    "F-PUMP-003": (
        "How long will usable storage last while inflow exceeds pumping?",
        "The formula divides usable storage by the positive flow deficit. It turns a volume reserve into a response-time screen.",
        "The result conveys time to the declared storage boundary under constant represented conditions. Changing inflow, controls, or storage geometry changes the answer.",
    ),
    "F-PUMP-004": (
        "How much storage is required for a stated response interval?",
        "The formula multiplies the positive flow deficit by the response duration. It asks how much volume accumulates before an operator, standby system, or other response is expected.",
        "The result conveys required storage for the named interval. It is a constant-condition screen, not dynamic routing.",
    ),
    "F-PUMP-007": (
        "How does storage and possible overflow change through a time-varying event?",
        "The method integrates interval inflow minus available capacity, updates stored volume, applies the usable-storage boundary, and records routed overflow when the boundary is exceeded.",
        "The result conveys dynamic storage history and modeled overflow under the declared controls. Initial storage, time step, and capacity schedule are load-bearing inputs.",
    ),
    "F-PUMP-005": (
        "How often would a constant-speed pump cycle under the simplified wet-well condition?",
        "The formula combines wet-well working volume, constant inflow, and constant pump capacity to calculate fill time, drawdown time, cycle time, and cycles per hour.",
        "The result conveys a screening estimate for one control pattern. Variable speed, multiple levels, delays, and changing inflow require a different model.",
    ),
    "F-PUMP-006": (
        "What equivalent pump operating time corresponds to the pumped volume?",
        "The formula divides volume by representative single-pump or firm capacity. It expresses hydraulic duty as equivalent hours for comparison and downstream rule calculations.",
        "The result conveys a capacity-normalized time measure. It is not automatically the same as measured motor runtime or a jurisdictional metric.",
    ),
    "F-MDC-NAPOT-001": (
        "What Miami-Dade NAPOT value results under the applicable rule-pack basis?",
        "The method applies the current reviewed Miami-Dade definition to the required average operating-hours basis and installed-pump count, including any applicable speed or power provisions.",
        "The result conveys a jurisdiction-specific illustration. It must never be presented as a universal United States formula or a compliance determination without current applicability review.",
    ),
    "F-ENERGY-001": (
        "How much electrical input power is required at the operating point?",
        "The formula converts flow and total dynamic head into hydraulic power, then divides by pump and motor efficiency. It connects station hydraulics with electrical burden.",
        "The result conveys modeled input power for the represented point. Efficiency, specific gravity, and operating-point validity directly affect it.",
    ),
    "F-ENERGY-002": (
        "How much energy and energy cost accumulated over the represented period?",
        "The formula integrates input power over time and applies the approved tariff treatment. It turns a sequence of operating states into kilowatt-hours and cost.",
        "The result conveys event or period energy burden under the tariff scope. Demand charges and time-of-use terms must be included when material.",
    ),
    "F-ECON-002": (
        "What annual volume corresponds to an average flow or modeled reduction?",
        "The formula multiplies average million gallons per day by the explicit number of days in the analysis year. It connects a daily hydraulic rate with annual planning volume.",
        "The result conveys annualized volume under the representativeness assumption. A single event cannot be annualized without an approved frequency basis.",
    ),
    "F-ECON-003": (
        "After discounting, do included benefits exceed included costs?",
        "The formula subtracts present costs from present benefits. The sign and magnitude summarize the net economic position of the declared scenario.",
        "The result conveys net present value under included cash flows. It does not make the project decision or value omitted safety, compliance, reliability, and environmental effects.",
    ),
    "F-ECON-004": (
        "How many years of positive annual net benefit would recover initial capital cost?",
        "The formula divides initial capital cost by annual net benefit only when that annual benefit is positive. It fails closed when simple payback has no valid positive recovery meaning.",
        "The result conveys an undiscounted recovery screen when calculable. A nonpositive benefit correctly produces no payback value rather than a misleading number.",
    ),
}


SOURCE_ROLES = {
    "DS-01": "This source class is the observed hydraulic backbone. It tells the system what the sewer or station actually recorded over time.",
    "DS-02": "This source class supplies the forcing event. Without accepted rainfall on the same clock and geography, rainfall response cannot be separated defensibly.",
    "DS-03": "This source class defines the physical and geographic denominator. It tells calculations which basin and sewer assets the observations represent.",
    "DS-04": "This source class supports the sanitary-flow estimate that must be separated from groundwater and rainfall response.",
    "DS-05": "This source class describes what the installed pumps can produce under the represented condition, speed, impeller, and revision.",
    "DS-06": "This source class describes the connected hydraulic resistance and static lift that the pumps must overcome.",
    "DS-07": "This source class defines how level becomes volume and how controls change available pumping and response time.",
    "DS-08": "This source class connects hydraulic operation with measured or modeled electrical burden and the applicable price structure.",
    "DS-09": "This source class gives the economic scenario its price year, cost scope, assumed reduction, and discount basis.",
    "DS-10": "This source class supplies current jurisdiction-specific authority without contaminating the universal formula layer.",
    "DS-11": "This source class connects approved manufacturer and utility knowledge with the exact asset, requirement, task, and completion evidence.",
}


CHAIN_CONNECTIONS = {
    "F-UNIT-001": "Its rainfall-volume output becomes the denominator for capture fraction and the volume basis for RTK component allocation.",
    "F-FLOW-001": "Its integrated volume is used wherever a changing flow series must become gallons, including RDII event volume, storage routing, and energy-time integration.",
    "F-DWF-001": "Its baseline feeds RDII residual calculation, wet-weather ratios, peak-total composition, and the station inflow story.",
    "F-RDII-001": "Its residual time series feeds event-volume integration and provides the observed hydrograph against which RTK response can be calibrated.",
    "F-RDII-002": "Its event volume feeds rainfall capture, storage consequence, rehabilitation scenarios, and event comparison.",
    "F-RDII-003": "Its capture fraction feeds event comparison and RTK calibration review while remaining separate from defect diagnosis.",
    "F-NORM-001": "Its normalized result feeds basin screening and prioritization, but no station hydraulic calculation should use it as an inflow.",
    "F-PEAK-001": "Its ratio feeds event-strength screening and comparison, while actual peak flow continues separately into hydraulic analysis.",
    "F-RTK-001": "Its component volume and duration are derived inputs to F-RTK-002, which builds each triangular component hydrograph.",
    "F-RTK-002": "Its component ordinates are derived inputs to F-RTK-003, which shifts and adds them across the rainfall series.",
    "F-RTK-003": "Its complete RDII hydrograph is added to expected dry-weather flow on the same clock, creating total station inflow for pump and storage analysis.",
    "F-MASS-001": "Its conservation rule is the foundation for dynamic storage routing, overflow accounting, and reconciliation of unexplained volume.",
    "F-MANNING-001": "Its gravity-capacity estimate can support bounded upstream screening or external model checks before flow reaches the station analysis.",
    "F-COST-001": "Its annual gross marginal benefit becomes a cash-flow input to present-value, net-present-value, benefit-cost, and payback screens.",
    "F-PV-001": "Its discounted benefit and cost totals feed net present value and benefit-cost ratio.",
    "F-BCR-001": "Its ratio feeds the economic comparison presented to engineering, finance, and capital planning.",
    "F-UNC-001": "Its covariance estimate attaches uncertainty to selected outputs so dashboards and decisions do not present false precision.",
    "F-VERIFY-001": "Its weather-normalized result closes the loop by comparing post-work evidence with the counterfactual used to judge outcome.",
    "F-CONV-001": "Its converted values allow otherwise compatible formulas to exchange flow without silently mixing gpm, gpd, MGD, and cfs.",
    "F-GWI-001": "Its groundwater-infiltration estimate feeds normalization, annualization, rehabilitation scenarios, and dry-weather investigation.",
    "F-IDM-001": "Its inventory denominator combines with selected flow in F-NORM-001 to create an inch-diameter-mile screening value.",
    "F-HYD-001": "Its velocity and Reynolds number feed friction-factor, major-loss, minor-loss, system-curve, power, and operating-point calculations.",
    "F-HYD-002": "Its Darcy friction factor feeds F-HYD-003 major head loss and therefore the system head curve.",
    "F-HYD-003": "Its major head-loss result is added to static and minor head in F-HYD-005.",
    "F-HYD-004": "Its localized head-loss result is added to static and major head in F-HYD-005.",
    "F-HYD-005": "Its system curve is intersected with the pump curve in F-PUMP-001 and supplies total dynamic head to energy calculations.",
    "F-PUMP-001": "Its operating-point capacity feeds margin, utilization, storage deficit, cycling, operating-time, and power calculations.",
    "F-PUMP-002": "Its margin and utilization feed the station condition review and determine whether contingency analysis deserves attention.",
    "F-PUMP-003": "Its time-to-exhaust result feeds contingency response planning and the Action and Approval Center.",
    "F-PUMP-004": "Its required-storage screen is compared with usable storage to produce the contingency shortfall used in action review.",
    "F-PUMP-007": "Its routed storage and overflow series feed dynamic resilience review, rather than being confused with the simpler constant-peak screens.",
    "F-PUMP-005": "Its cycle result is compared with reviewed control or manual requirements and may initiate maintenance or control investigation.",
    "F-PUMP-006": "Its equivalent hours feed operating-duty comparison and, only under the applicable rule pack, the Miami-Dade NAPOT calculation.",
    "F-MDC-NAPOT-001": "Its jurisdiction-specific output feeds a reviewed Miami-Dade operating-time finding, never the universal formula library.",
    "F-ENERGY-001": "Its power result becomes the time-varying input to F-ENERGY-002.",
    "F-ENERGY-002": "Its energy and cost results feed operating-burden review and rehabilitation economics when the cost scope permits.",
    "F-ECON-002": "Its annual volume feeds marginal-cost benefit and the declared annual rehabilitation scenario.",
    "F-ECON-003": "Its net present value feeds the economic screen presented alongside benefit-cost ratio and excluded benefits.",
    "F-ECON-004": "Its payback result or fail-closed refusal feeds the economic dashboard without forcing a misleading recovery period.",
}


def quality_explanation(requirement: str) -> str:
    text = requirement.lower()
    rules = [
        (("identity", "association"), "A wrong identity attaches valid data to the wrong meter, basin, station, or asset."),
        (("time-zone", "clock alignment", "interval alignment"), "Misaligned clocks move peaks, distort integration, and break cause-and-response comparison."),
        (("unit",), "An unresolved unit can change a result by orders of magnitude while leaving the arithmetic syntactically valid."),
        (("gap", "duplicate", "rate-of-change"), "Gaps and duplicates bias integrated volume, while implausible rates can signal sensor or ingestion failure."),
        (("surcharge", "backwater", "fouling", "low-depth"), "These conditions can violate the measurement assumptions and bias the recorded flow."),
        (("coordinates",), "Coordinates are needed to decide whether the rainfall observation represents the study basin."),
        (("missing-period",), "Missing rainfall can understate storm forcing and overstate apparent capture."),
        (("spatial-representativeness",), "A gauge outside the effective storm pattern may not represent rainfall over the basin."),
        (("abandoned",), "Unresolved active and abandoned segments corrupt the inventory denominator."),
        (("diameter basis", "internal-diameter"), "Diameter controls normalization, area, velocity, Reynolds number, and head loss."),
        (("included asset classes",), "The included classes define what the denominator represents and whether comparison is fair."),
        (("boundary match", "same service boundary"), "A numerator and denominator from different service boundaries create a meaningless ratio or remainder."),
        (("non-domestic", "transferred flows"), "Omitted industrial, commercial, or transferred flow is easily mislabeled as groundwater infiltration."),
        (("seasonal", "day-type"), "Customer use and groundwater conditions vary, so the baseline period must represent the analysis purpose."),
        (("installed pump", "curve applicability"), "The wrong pump, speed, impeller, or revision produces the wrong operating point."),
        (("speed and impeller",), "Pump performance changes with configuration, so the selected curve must match the installed condition."),
        (("interpolation boundary",), "Uncontrolled extrapolation can invent pump performance outside the evidence in the curve."),
        (("current configuration", "valve state"), "The system curve changes when the hydraulic lineup changes."),
        (("elevation datum",), "Mixed elevation datums produce a false static head."),
        (("roughness", "fluid-property"), "These assumptions control friction and can materially move the operating point."),
        (("current settings", "effective date"), "An obsolete control setting describes a station that no longer exists operationally."),
        (("level-sensor",), "A biased level reading changes storage, controls, alarms, and response time."),
        (("usable-storage",), "Storage must be measured between the actual starting and limiting levels used by the scenario."),
        (("demand and time-of-use",), "Energy-only pricing can omit material demand or time-of-use cost."),
        (("tariff effective date",), "A stale tariff produces a cost result for the wrong period."),
        (("price year",), "Costs from different price years cannot be compared until they share a declared basis."),
        (("real or nominal",), "The discount rate and cash flows must use the same inflation basis."),
        (("marginal versus average",), "Only avoidable marginal cost belongs in a direct savings calculation unless another scope is approved."),
        (("excluded-benefit",), "Visible exclusions prevent a narrow cost screen from being mistaken for total public value."),
        (("legal-status",), "A superseded or withdrawn instrument cannot support a current requirement."),
        (("applicability review",), "A valid rule still cannot be applied to the wrong geography, entity, asset, or fact pattern."),
        (("universal mathematics",), "Jurisdiction-specific rules must not be presented as universal engineering formulas."),
        (("passage locator",), "The exact passage lets a reviewer verify that the requirement was extracted without changing its meaning."),
        (("asset applicability",), "A real requirement from the wrong model or asset is still the wrong requirement."),
        (("qualified review",), "Machine extraction remains a proposal until an accountable reviewer accepts it."),
        (("supersession",), "A superseded manual must remain historical evidence, not current operating authority."),
    ]
    for needles, explanation in rules:
        if any(needle in text for needle in needles):
            return explanation
    return "Resolving this condition prevents an ambiguous record from becoming a confident downstream result."


def master_front() -> str:
    return """# I&I Intelligence System Bible

## Version 2, narrative-first engineering, application, and decision standard

**Document identifier:** OWOS-IISB-001

**Version:** 0.2.0, integrated explanatory candidate

**Date:** July 28, 2026

**Owner:** Hardeep Anand

**Engineering source volume:** `../white-paper.md`, included completely in Book V

**Architecture source volume:** `white-paper.md`, included completely in Book VI

**Formula authority:** `../formula-register.yaml` version 0.2.0

**Worked example:** `../sample-basin.yaml` and `../generated/sample-basin-results.json`

**Release state:** Not approved for production calculations, facility use, or public release

---

## Why Version 2 exists

Version 1 proved that the engineering paper and the application Architecture Bible could be joined
without losing their technical contents. It also wired 39 formulas, 11 source classes, 34 dashboard
values, six decisions, and nine mock dashboards.

Version 2 changes the reading experience. It does not assume that a list, table, equation, or
architecture label explains itself. It begins with the physical event and tells the connected story
through data, mathematics, station consequence, dashboard, agent, human decision, and measured
outcome. It then explains every formula and every displayed value through the same questions:

1. What question is being answered?
2. What does the formula or value mean in ordinary language?
3. Why is it calculated?
4. What inputs does it consume and where do they come from?
5. What does the method do?
6. What does the result convey?
7. Where does it feed the larger calculation and decision chain?
8. How may the agent and human reviewer use it?
9. What must never be inferred from it?

## Master table of contents

### Book I. The connected story

1. Start with the rain, not the software
2. The boundary gives every number its meaning
3. Data becomes evidence only after it is qualified
4. Establish the ordinary flow before explaining the storm
5. **RTK explained: R, T, K, the three triangular components, and the complete RDII hydrograph**
6. The basin hydrograph becomes the station's inflow
7. Capacity alone does not answer resilience
8. Operating burden becomes energy, maintenance, and cost
9. Economics must preserve an unfavorable answer
10. The dashboard is the visible end of the calculation chain
11. The agent connects evidence but does not become the calculator
12. The loop closes only when the outcome is measured

### Book II. Every formula explained

1. Rainfall, integration, and dry-weather baseline formulas
2. RDII residual, event volume, and capture formulas
3. Normalization and peak-screening formulas
4. **RTK formula family**
   1. `F-RTK-001`, component volume and duration
   2. `F-RTK-002`, triangular component peak and ordinate
   3. `F-RTK-003`, event superposition
5. Mass balance and gravity hydraulics
6. Force-main hydraulics and system head
7. Pump operating point, capacity, storage, and cycling
8. Operating time and Miami-Dade NAPOT
9. Energy
10. Economics
11. Uncertainty and rehabilitation verification

### Book III. Every source and input explained

1. Flow observations
2. Rainfall observations
3. Basin and sewer inventory
4. Population, customer, and sanitary-flow basis
5. Pump performance
6. Force-main and hydraulic geometry
7. Wet-well and control data
8. Electrical energy and tariff
9. Cost and rehabilitation scenario
10. Jurisdiction and regulatory evidence
11. Manual and maintenance evidence

### Book IV. Every dashboard value and decision explained

1. M-01 through M-10, basin and I&I
2. M-11 through M-21, station hydraulics and resilience
3. M-22 through M-26, operations, energy, and Miami-Dade operating time
4. M-27 through M-34, rehabilitation economics
5. DEC-01 through DEC-06, governed decisions
6. DASH-01 through DASH-09, populated dashboard views

### Book V. Complete engineering source volume

The full engineering calculation paper is included after heading normalization. Its original table
of contents, universal calculation library, RTK derivation, complete sample basin and pump-station
calculation, architecture contract, Miami-Dade rule boundary, formula wiring matrix, glossary,
references, and reproducibility package remain present.

### Book VI. Complete operational Architecture Bible source volume

The full PumpOS and I&I operational Architecture Bible is included after heading normalization. Its
mega architecture, sub-diagrams, bounded contexts, ingestion pipelines, manuals, GraphDB,
dashboards, agent authority, deployment, security, versioning, and implementation workstreams
remain present.

### Book VII. Machine-readable operational contracts

1. Input and output contract
2. Formula-by-formula registry catalog
3. Source-system catalog
4. Numbered dashboard lineage catalog
5. Fully populated dashboard mockups
6. Validation, limitations, and release gates

---
"""


def formula_inputs(formula: dict[str, Any], related_metrics: list[dict[str, Any]]) -> list[tuple[str, str, str, list[str]]]:
    fid = formula["id"]
    inputs: list[tuple[str, str, str, list[str]]] = []
    if formula.get("inputs"):
        for item in formula["inputs"]:
            symbol = str(item.get("symbol", ""))
            source_ids = v1.EXPLICIT_INPUT_SOURCES.get(fid, {}).get(symbol)
            if source_ids is None:
                source_ids = sorted({sid for metric in related_metrics for sid in metric.get("source_classes", [])})
            inputs.append((symbol, str(item.get("meaning", "")), str(item.get("unit", "formula-specific")), source_ids))
    else:
        inputs = v1.MANUAL_INPUTS.get(fid, [])
    return inputs


def explanatory_formula_book(registry: dict[str, Any], manifest: dict[str, Any]) -> str:
    source_map = {item["id"]: item for item in manifest["source_classes"]}
    metrics = manifest["dashboard_metrics"]
    formulas = registry["formulae"]
    out = [
        "# Book II. Every formula explained",
        "",
        "A formula is a controlled answer to one question. It is not an isolated line of mathematics. "
        "Each section below explains the physical meaning, calculation purpose, input lineage, result meaning, "
        "larger dependency, agent use, and inference boundary before preserving the registry expression.",
        "",
    ]
    for index, formula in enumerate(formulas, start=1):
        fid = formula["id"]
        question, meaning, conveys = FORMULA_STORIES[fid]
        related = [metric for metric in metrics if fid in metric.get("formula_ids", [])]
        inputs = formula_inputs(formula, related)
        out.extend(
            [
                f"## Formula {index}. {fid}: {formula['name'].replace('_', ' ')}",
                "",
                f"### The question it answers",
                "",
                question,
                "",
                "### What it means and why it is calculated",
                "",
                meaning,
                "",
                "The application calculates this value because a later interpretation, comparison, or engineering "
                "calculation needs this physical quantity on a controlled basis. Leaving it implicit would force a "
                "developer, spreadsheet, or agent to recreate the method without a shared contract.",
                "",
                "### Inputs, meaning, and origin",
                "",
                "| Input | What the input means in this calculation | Unit or type | Where it originates |",
                "| --- | --- | --- | --- |",
            ]
        )
        if inputs:
            for symbol, input_meaning, unit, source_ids in inputs:
                origin = v1.source_names(source_ids, source_map)
                out.append(f"| `{symbol}` | {input_meaning.replace('_', ' ')} | {unit} | {origin} |")
        else:
            out.append(
                "| Unresolved input contract | The formula registry does not yet enumerate every operational input. "
                "This method must remain blocked from production until that contract is complete. | Unresolved | Unresolved |"
            )
        out.extend(
            [
                "",
                "The presence of an input in a source system does not make it acceptable. Identity, unit, time, "
                "boundary, quality, applicability, and source version must pass before the input snapshot is frozen.",
                "",
                "### What the calculation does",
                "",
                "```text",
                v1.display_expression(formula),
                "```",
                "",
                "The expression above is the executable mathematical core. The surrounding method contract controls "
                "units, domains, time alignment, interpolation, failure behavior, and numerical tolerance. Those "
                "controls are part of the calculation even when they are not visible in the equation.",
                "",
                "### What the result conveys",
                "",
                conveys,
                "",
                "### How it connects to the larger equation",
                "",
            ]
        )
        dependencies = formula.get("dependencies", [])
        if dependencies:
            dependency_phrase = "an upstream dependency" if len(dependencies) == 1 else "upstream dependencies"
            out.append(
                f"The registry explicitly declares {', '.join(dependencies)} as {dependency_phrase}. Those upstream "
                "results become controlled derived inputs. Their full precision and provenance must be retained."
            )
        else:
            out.append(
                "The current registry declares no formal upstream formula dependency for this record. That does not "
                "mean the calculation is isolated; the larger method connection is stated next and must become an "
                "explicit dependency wherever production orchestration requires it."
            )
        out.extend(["", CHAIN_CONNECTIONS[fid]])
        if related:
            out.append("")
            out.append(
                "Its worked-example results appear on the dashboard through "
                + ", ".join(f"`{metric['id']}` ({metric['label']}: **{metric['sample_display']}**)" for metric in related)
                + "."
            )
            out.append("")
            out.append(
                "Those displayed values carry the formula forward into these decisions: "
                + " ".join(dict.fromkeys(metric["decision_use"] for metric in related))
            )
        else:
            out.append("")
            out.append(
                "The worked dashboard does not expose this formula as a standalone numbered value. It remains an "
                "intermediate, supporting, uncertainty, verification, or alternative-method calculation."
            )
        out.extend(
            [
                "",
                "### How the agent and human reviewer use it",
                "",
                "The deterministic service runs the formula. Droobi may retrieve the result, explain the inputs and "
                "assumptions, compare it with other governed results, identify missing evidence, and draft a next "
                "step. A qualified person decides whether the result is fit for the intended engineering, operating, "
                "financial, or jurisdictional use.",
                "",
                "### What must not be inferred",
                "",
            ]
        )
        prohibited = formula.get("prohibited_inferences", [])
        if prohibited:
            for item in prohibited:
                out.append(f"- {item}")
        else:
            out.append(
                "- Do not treat the output as a broader diagnosis, design approval, operating command, compliance "
                "finding, or project authorization unless a separate approved method and reviewer establish that claim."
            )
        out.extend(["", "---", ""])
    return "\n".join(out)


def explanatory_source_book(manifest: dict[str, Any]) -> str:
    out = [
        "# Book III. Every source and input explained",
        "",
        "A source class explains where evidence originates before it becomes an input. Each class has a different "
        "physical meaning, authority, failure mode, and downstream consequence.",
        "",
    ]
    for source in manifest["source_classes"]:
        out.extend(
            [
                f"## {source['id']}. {source['name']}",
                "",
                SOURCE_ROLES[source["id"]],
                "",
                "### Why the application needs it",
                "",
                f"Without qualified {source['name'].lower()}, every formula that consumes this class either fails "
                "closed or becomes limited to a clearly labeled hypothetical scenario. A substitute is acceptable "
                "only when the method contract names it and preserves the substitution.",
                "",
                "### Where it comes from",
                "",
                "The supported systems are " + ", ".join(source["systems"]) + ". These systems remain the original "
                "record authorities. PumpOS and I&I Intelligence preserve locators and snapshots rather than "
                "relabeling derived copies as original evidence.",
                "",
                "### What is wrangled",
                "",
                "The pipeline resolves these fields: " + ", ".join(f"`{field}`" for field in source["raw_fields"]) + ".",
                "",
                "Wrangling means more than changing a column name. It establishes identity, unit, time, boundary, "
                "effective date, quality, and provenance so the record can be judged for a named method.",
                "",
                "### What must pass before use",
                "",
            ]
        )
        for requirement in source["quality_requirements"]:
            out.append(
                f"- **{requirement}.** {quality_explanation(requirement)}"
            )
        consumers = [m for m in manifest["dashboard_metrics"] if source["id"] in m["source_classes"]]
        out.extend(
            [
                "",
                "### What it feeds and what the reader eventually sees",
                "",
                (
                    "This source class feeds "
                    + ", ".join(f"`{m['id']}` {m['label']}" for m in consumers)
                    + "."
                    if consumers
                    else "No numbered sample dashboard metric currently consumes this source class directly."
                ),
                "",
                "A source record never becomes a conclusion by itself. It becomes one accepted input in a named "
                "calculation, and the output retains the source reference so the dashboard can explain its origin.",
                "",
                "---",
                "",
            ]
        )
    return "\n".join(out)


def explanatory_dashboard_book(manifest: dict[str, Any]) -> str:
    out = [
        "# Book IV. Every dashboard value and decision explained",
        "",
        "The dashboard is the visible end of a calculation, not a separate truth. Each numbered value below explains "
        "what the reader sees, why it matters, where it comes from, what it feeds, and what decision boundary remains.",
        "",
    ]
    for metric in manifest["dashboard_metrics"]:
        formula_text = " -> ".join(metric["formula_ids"]) or "Direct accepted input"
        source_text = ", ".join(metric["source_classes"])
        out.extend(
            [
                f"## {metric['id']} / #{metric['number']}. {metric['label']}",
                "",
                f"The worked dashboard displays **{metric['sample_display']}**. This is classified as "
                f"`{metric['evidence_class']}` rather than being shown as an unexplained number.",
                "",
                "### Where the value begins",
                "",
                f"The lineage begins with {source_text}. The exact stored result is "
                f"`{metric['result_path']}`. The formula chain is {formula_text}.",
                "",
                "This source-to-result path matters because the display may be rounded, reformatted, or combined with "
                "a label. The application must always be able to return to the stored result and the frozen input snapshot.",
                "",
                "### What the value means and why it matters",
                "",
                metric["importance"],
                "",
                "The value is calculated or displayed at this point in the story because a downstream reader needs "
                "to understand either the event forcing, the separated I&I response, the pump-station consequence, "
                "the operating burden, or the economic scenario.",
                "",
                "### What it feeds",
                "",
                metric["decision_use"],
                "",
                "The agent may explain this value and assemble its evidence. It may not promote the value into a "
                "broader claim than its evidence class and decision use allow.",
                "",
                "---",
                "",
            ]
        )
    out.extend(
        [
            "# The six governed decision stories",
            "",
            "A calculation becomes operationally useful only when the application states what decision it may support, "
            "which values are required, who must review the result, and what kind of output is allowed.",
            "",
        ]
    )
    for decision in manifest["decision_bindings"]:
        out.extend(
            [
                f"## {decision['id']}. {decision['name']}",
                "",
                f"This decision consumes {', '.join(decision['metric_ids'])}. Those values are assembled because no "
                "single metric carries the whole decision. The reviewer needs the connected condition, not one isolated tile.",
                "",
                f"The required roles are {', '.join(decision['required_roles'])}. The allowed output is "
                f"`{decision['output']}`. Naming the output prevents the application from silently turning analysis "
                "into a work order, compliance determination, or capital authorization.",
                "",
                "Droobi may prepare the evidence packet and draft the allowed output. The named human role remains "
                "responsible for acceptance, revision, rejection, and any consequential dispatch.",
                "",
            ]
        )
    return "\n".join(out)


def source_completeness_note() -> str:
    return """# Source-volume completeness statement

Books V and VI are generated directly from the two governed Markdown source volumes. The builder
changes heading depth only so each source can sit under the Version 2 hierarchy. It does not
summarize, excerpt, or delete their paragraphs, formulas, tables, bullets, diagrams, glossary,
references, or appendices.

The Version 2 validator reconstructs both shifted source texts and requires exact inclusion. It also
checks the presence of all 39 formula stories, all 34 metric stories, all 11 source stories, all
six decision stories, the three RTK formula headings, the explicit RTK master-table-of-contents
entry, and all nine dashboard figures.

---
"""


def status_section() -> str:
    return """# Version 2 status and quality review

Version 2 is an integrated explanatory candidate. The new narrative and repeated explanation
pattern improve comprehension, but they do not convert candidate formulas or illustrative data
into production authority.

## Current white-paper score

| Dimension | Available | Awarded | Evidence for points awarded | Deduction and next work |
| --- | ---: | ---: | --- | --- |
| Teaching thesis and importance | 15 | 15 | One evidence-to-action story now connects rain, sewer response, station, dashboard, agent, decision, and outcome. | None for the candidate thesis. |
| Complete plain-language explanation | 20 | 20 | Every formula, source class, dashboard metric, and decision has a consistent explanatory narrative. | Independent novice-reader review remains a hard gate. |
| Utility-wide and cross-sector value | 15 | 14 | Engineering, operations, asset, compliance, executive, software, and finance uses are connected. | PipeOS and treatment-system product-owner review remains open. |
| Research depth and source quality | 15 | 11 | Both complete source papers and their existing references remain present and mechanically verified. | Active deployment evidence and several formula-source gaps remain unresolved. |
| Technical accuracy and claim verification | 20 | 13 | Registry formulas, dependencies, test results, sample paths, limitations, and six formula-contract gaps remain visible. | Independent numerical implementation, field calibration, and qualified engineering review remain blocked. |
| Diagrams and visual teaching value | 10 | 10 | Architecture diagrams, method chains, nine populated dashboards, and lineage views remain included. | Independent accessibility and usability review remains unresolved. |
| Editorial quality, boundaries, and originality | 5 | 5 | Version 2 replaces specification-first reading with an operator-grounded explanatory story while preserving boundaries. | Public originality review remains required before release. |
| **Total** | **100** | **88** | Complete narrative-first candidate with mechanical source-preservation proof. | Strong, but not eligible for production or public release. |

## Hard gates

- Owner approval of Version 2: blocked.
- Independent source and numerical verification: blocked.
- Complete standalone contracts for six exposed calculation transformations: blocked.
- Qualified I&I, pump-station, operations, regulatory, security, and software review: blocked.
- Field calibration and holdout validation: blocked.
- Mobile, accessibility, usability, executive, and novice review: blocked.
- Production and public release: blocked.
"""


def build() -> Path:
    registry = yaml.safe_load((ROOT / "formula-register.yaml").read_text())
    manifest = yaml.safe_load((PACKAGE / "operationalization-manifest.yaml").read_text())
    engineering = (ROOT / "white-paper.md").read_text()
    architecture = (PACKAGE / "white-paper.md").read_text()
    narrative = (PACKAGE / "explanatory-narrative-v2.md").read_text()
    dashboards = (PACKAGE / "dashboard-mockups.md").read_text()

    sections = [
        master_front(),
        narrative,
        "\n---\n\n",
        explanatory_formula_book(registry, manifest),
        "\n---\n\n",
        explanatory_source_book(manifest),
        "\n---\n\n",
        explanatory_dashboard_book(manifest),
        "\n---\n\n",
        source_completeness_note(),
        "# Book V. Complete engineering source volume\n\n",
        v1.shift_headings(engineering, 1),
        "\n---\n\n# Book VI. Complete operational Architecture Bible source volume\n\n",
        v1.shift_headings(architecture, 1),
        "\n---\n\n# Book VII. Machine-readable operational contracts\n\n",
        v1.operational_input_contract().replace("# Part III.", "## Contract 1."),
        "\n---\n\n",
        v1.formula_catalog(registry, manifest).replace("# Part IV.", "## Contract 2."),
        "\n---\n\n",
        v1.source_catalog(manifest).replace("# Part V.", "## Contract 3."),
        "\n---\n\n",
        v1.dashboard_catalog(manifest).replace("# Part VI.", "## Contract 4."),
        "\n---\n\n",
        dashboards.replace("# Part VII.", "## Contract 5."),
        "\n---\n\n",
        status_section(),
    ]
    content = "".join(sections)
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    output = PACKAGE / "ii-intelligence-system-bible-v2.md"
    output.write_text(content)
    return output


if __name__ == "__main__":
    print(build())
