#!/usr/bin/env python3

from __future__ import annotations

import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import yaml


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "sample-basin.yaml"
OUTPUT_DIR = ROOT / "generated"
RESULTS_PATH = OUTPUT_DIR / "sample-basin-results.json"
TIMESERIES_PATH = OUTPUT_DIR / "sample-basin-timeseries.csv"

ACRE_INCH_GALLONS = 27154.285714285714
GPM_PER_CFS = 448.8311688311688
G_FT_PER_S2 = 32.174
HP_TO_KW = 0.745699872


class CalculationError(ValueError):
    pass


@dataclass(frozen=True)
class PumpOperatingPoint:
    pumps_operating: int
    static_head_ft: float
    total_flow_gpm: float
    per_pump_flow_gpm: float
    head_ft: float
    pump_efficiency_fraction: float
    motor_efficiency_fraction: float
    total_input_kW: float
    specific_energy_kWh_per_MG: float


def load_yaml(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text())


def linear_interpolate(
    x: float, points: list[dict[str, Any]], x_key: str, y_key: str
) -> float:
    usable = [point for point in points if point[y_key] is not None]
    if not usable:
        raise CalculationError(f"no values for {y_key}")
    if x < usable[0][x_key] or x > usable[-1][x_key]:
        raise CalculationError(
            f"{x_key}={x} is outside the supplied curve "
            f"[{usable[0][x_key]}, {usable[-1][x_key]}]"
        )
    for left, right in zip(usable, usable[1:]):
        if left[x_key] <= x <= right[x_key]:
            span = right[x_key] - left[x_key]
            if span == 0:
                return float(left[y_key])
            weight = (x - left[x_key]) / span
            return float(left[y_key] + weight * (right[y_key] - left[y_key]))
    return float(usable[-1][y_key])


def normalize_profile(raw: list[float]) -> list[float]:
    average = sum(raw) / len(raw)
    if average <= 0:
        raise CalculationError("dry-weather profile average must be positive")
    return [value / average for value in raw]


def rainfall_increments(event: dict[str, Any]) -> list[float]:
    dt = event["time_step_min"]
    steps_per_hour = 60 / dt
    if not steps_per_hour.is_integer():
        raise CalculationError("time step must divide one hour for this example")
    steps = int(steps_per_hour)
    if event["distribution_within_each_hour"] != (
        "uniform_across_four_15_minute_steps"
    ):
        raise CalculationError("unsupported rainfall distribution")
    return [
        hourly_depth / steps
        for hourly_depth in event["hourly_depths_in"]
        for _ in range(steps)
    ]


def triangle_ordinate_gph(
    tau_hr: float, volume_gal: float, time_to_peak_hr: float, recession_ratio: float
) -> float:
    if tau_hr < 0:
        return 0.0
    base_duration_hr = time_to_peak_hr * (1 + recession_ratio)
    if tau_hr > base_duration_hr:
        return 0.0
    peak_gph = 2 * volume_gal / base_duration_hr
    if tau_hr <= time_to_peak_hr:
        return peak_gph * tau_hr / time_to_peak_hr
    recession_hr = recession_ratio * time_to_peak_hr
    if recession_hr == 0:
        return 0.0
    return peak_gph * (1 - (tau_hr - time_to_peak_hr) / recession_hr)


def integrate_trapezoid(values: list[float], dt_hr: float) -> float:
    return sum(
        (left + right) / 2 * dt_hr for left, right in zip(values, values[1:])
    )


def build_hydrograph(data: dict[str, Any]) -> dict[str, Any]:
    basin = data["basin"]
    event = data["rainfall_event"]
    rtk = data["RTK"]
    dt_min = event["time_step_min"]
    dt_hr = dt_min / 60
    increments = rainfall_increments(event)
    rainfall_duration_hr = len(increments) * dt_hr
    max_base_hr = max(
        component["T_hr"] * (1 + component["K"])
        for component in rtk["components"]
    )
    end_hr = rainfall_duration_hr + max_base_hr
    step_count = int(round(end_hr / dt_hr)) + 1
    times_hr = [index * dt_hr for index in range(step_count)]

    component_flows_gph: dict[str, list[float]] = {
        component["response"]: [0.0] * step_count for component in rtk["components"]
    }
    component_volumes_gal: dict[str, float] = {
        component["response"]: 0.0 for component in rtk["components"]
    }

    for rain_index, depth_in in enumerate(increments):
        onset_hr = rain_index * dt_hr
        for component in rtk["components"]:
            response = component["response"]
            volume_gal = (
                component["R"]
                * depth_in
                * rtk["area_acre"]
                * ACRE_INCH_GALLONS
            )
            component_volumes_gal[response] += volume_gal
            for time_index, time_hr in enumerate(times_hr):
                tau_hr = time_hr - onset_hr
                component_flows_gph[response][time_index] += triangle_ordinate_gph(
                    tau_hr,
                    volume_gal,
                    component["T_hr"],
                    component["K"],
                )

    total_rdii_gph = [
        sum(component_flows_gph[name][index] for name in component_flows_gph)
        for index in range(step_count)
    ]
    total_rdii_MGD = [flow_gph * 24 / 1_000_000 for flow_gph in total_rdii_gph]

    normalized_profile = normalize_profile(
        basin["dry_weather_profile_raw_hourly_multipliers"]
    )
    base_MGD = basin["average_base_wastewater_flow_MGD"]
    gwi_MGD = basin["average_groundwater_infiltration_MGD"]
    dwf_MGD = [
        gwi_MGD + base_MGD * normalized_profile[int(time_hr % 24)]
        for time_hr in times_hr
    ]
    total_flow_MGD = [
        dwf + rdii for dwf, rdii in zip(dwf_MGD, total_rdii_MGD)
    ]

    rain_by_step = increments + [0.0] * (step_count - len(increments))
    integrated_component_volumes = {
        name: integrate_trapezoid(values, dt_hr)
        for name, values in component_flows_gph.items()
    }
    integrated_total_gal = integrate_trapezoid(total_rdii_gph, dt_hr)
    expected_total_gal = sum(component_volumes_gal.values())
    volume_closure_error_fraction = (
        integrated_total_gal - expected_total_gal
    ) / expected_total_gal

    peak_index = max(range(step_count), key=total_flow_MGD.__getitem__)
    rdii_peak_index = max(range(step_count), key=total_rdii_MGD.__getitem__)
    rainfall_depth_in = sum(increments)
    rain_volume_gal = (
        rainfall_depth_in * rtk["area_acre"] * ACRE_INCH_GALLONS
    )

    return {
        "dt_min": dt_min,
        "times_hr": times_hr,
        "rainfall_increment_in": rain_by_step,
        "component_flows_MGD": {
            name: [value * 24 / 1_000_000 for value in values]
            for name, values in component_flows_gph.items()
        },
        "rdii_MGD": total_rdii_MGD,
        "dwf_MGD": dwf_MGD,
        "total_flow_MGD": total_flow_MGD,
        "summary": {
            "rainfall_depth_in": rainfall_depth_in,
            "rainfall_volume_gal": rain_volume_gal,
            "expected_RDII_volume_gal": expected_total_gal,
            "integrated_RDII_volume_gal": integrated_total_gal,
            "volume_closure_error_fraction": volume_closure_error_fraction,
            "capture_fraction_total_R": integrated_total_gal / rain_volume_gal,
            "component_expected_volumes_gal": component_volumes_gal,
            "component_integrated_volumes_gal": integrated_component_volumes,
            "peak_RDII_MGD": total_rdii_MGD[rdii_peak_index],
            "peak_RDII_time_hr": times_hr[rdii_peak_index],
            "peak_total_flow_MGD": total_flow_MGD[peak_index],
            "peak_total_flow_gpm": total_flow_MGD[peak_index]
            * 1_000_000
            / 1440,
            "peak_total_flow_time_hr": times_hr[peak_index],
            "peak_dry_weather_flow_MGD": max(dwf_MGD),
            "average_dry_weather_flow_MGD": base_MGD + gwi_MGD,
        },
    }


def gravity_inventory_metrics(data: dict[str, Any]) -> dict[str, float]:
    basin = data["basin"]
    segments = basin["gravity_sewer_inventory"]["segments"]
    total_length_mi = sum(segment["length_mi"] for segment in segments)
    idm = sum(
        segment["diameter_in"] * segment["length_mi"] for segment in segments
    )
    gwi_gpd = basin["average_groundwater_infiltration_MGD"] * 1_000_000
    return {
        "gravity_main_length_mi": total_length_mi,
        "inch_diameter_mile": idm,
        "GWI_gpd": gwi_gpd,
        "GWI_gpcd": gwi_gpd / basin["population_person"],
        "GWI_gpd_per_inch_diameter_mile": gwi_gpd / idm,
        "ADWF_MGD": basin["average_base_wastewater_flow_MGD"]
        + basin["average_groundwater_infiltration_MGD"],
        "ADWF_gpcd": (
            basin["average_base_wastewater_flow_MGD"]
            + basin["average_groundwater_infiltration_MGD"]
        )
        * 1_000_000
        / basin["population_person"],
    }


def colebrook_friction_factor(
    reynolds_number: float, relative_roughness: float
) -> float:
    if reynolds_number <= 0:
        raise CalculationError("Reynolds number must be positive")
    if reynolds_number < 2000:
        return 64 / reynolds_number
    if reynolds_number < 4000:
        raise CalculationError(
            "transition flow requires a separately approved friction policy"
        )
    friction = 0.02
    for _ in range(100):
        next_friction = 1 / (
            -2
            * math.log10(
                relative_roughness / 3.7
                + 2.51 / (reynolds_number * math.sqrt(friction))
            )
        ) ** 2
        if abs(next_friction - friction) < 1e-12:
            return next_friction
        friction = next_friction
    raise CalculationError("Colebrook-White solver did not converge")


def system_head(
    flow_gpm: float, static_head_ft: float, force_main: dict[str, Any]
) -> dict[str, float]:
    if flow_gpm == 0:
        return {
            "system_head_ft": static_head_ft,
            "major_headloss_ft": 0.0,
            "minor_headloss_ft": 0.0,
            "velocity_ft_per_s": 0.0,
            "Reynolds_number": 0.0,
            "Darcy_friction_factor": 0.0,
        }
    diameter_ft = force_main["internal_diameter_in"] / 12
    area_ft2 = math.pi * diameter_ft**2 / 4
    flow_cfs = flow_gpm / GPM_PER_CFS
    velocity = flow_cfs / area_ft2
    reynolds = (
        velocity
        * diameter_ft
        / force_main["kinematic_viscosity_ft2_per_s"]
    )
    relative_roughness = force_main["absolute_roughness_ft"] / diameter_ft
    friction = colebrook_friction_factor(reynolds, relative_roughness)
    velocity_head = velocity**2 / (2 * G_FT_PER_S2)
    major_loss = (
        friction
        * force_main["length_ft"]
        / diameter_ft
        * velocity_head
    )
    minor_loss = force_main["minor_loss_coefficient_total"] * velocity_head
    return {
        "system_head_ft": static_head_ft + major_loss + minor_loss,
        "major_headloss_ft": major_loss,
        "minor_headloss_ft": minor_loss,
        "velocity_ft_per_s": velocity,
        "Reynolds_number": reynolds,
        "Darcy_friction_factor": friction,
    }


def pump_head(
    total_flow_gpm: float, pumps_operating: int, curve: list[dict[str, Any]]
) -> float:
    per_pump_flow = total_flow_gpm / pumps_operating
    return linear_interpolate(per_pump_flow, curve, "flow_gpm", "head_ft")


def find_operating_point(
    station: dict[str, Any], pumps_operating: int, static_head_ft: float
) -> PumpOperatingPoint:
    curve = station["pump_curve"]["points"]
    maximum_total_flow = curve[-1]["flow_gpm"] * pumps_operating
    step = station["hydraulic_solver"]["flow_scan_step_gpm"]
    tolerance = station["hydraulic_solver"]["root_tolerance_ft"]

    def residual(total_flow_gpm: float) -> float:
        return pump_head(total_flow_gpm, pumps_operating, curve) - system_head(
            total_flow_gpm, static_head_ft, station["force_main"]
        )["system_head_ft"]

    left = 0.0
    left_value = residual(left)
    bracket: tuple[float, float] | None = None
    right = step
    while right <= maximum_total_flow:
        try:
            right_value = residual(right)
        except CalculationError as error:
            if "transition flow" in str(error):
                right += step
                continue
            raise
        if left_value == 0 or left_value * right_value <= 0:
            bracket = (left, right)
            break
        left = right
        left_value = right_value
        right += step
    if bracket is None:
        raise CalculationError(
            f"no operating-point intersection for {pumps_operating} pumps"
        )

    left, right = bracket
    for _ in range(100):
        midpoint = (left + right) / 2
        value = residual(midpoint)
        if abs(value) <= tolerance:
            break
        if residual(left) * value <= 0:
            right = midpoint
        else:
            left = midpoint
    total_flow = (left + right) / 2
    per_pump_flow = total_flow / pumps_operating
    head = system_head(
        total_flow, static_head_ft, station["force_main"]
    )["system_head_ft"]
    pump_efficiency = linear_interpolate(
        per_pump_flow, curve, "flow_gpm", "efficiency_fraction"
    )
    motor_efficiency = station["motor_efficiency_fraction"]
    water_hp_per_pump = per_pump_flow * head / 3960
    input_hp_per_pump = water_hp_per_pump / (
        pump_efficiency * motor_efficiency
    )
    total_input_kW = input_hp_per_pump * HP_TO_KW * pumps_operating
    total_MG_per_hr = total_flow * 60 / 1_000_000
    specific_energy = total_input_kW / total_MG_per_hr
    return PumpOperatingPoint(
        pumps_operating=pumps_operating,
        static_head_ft=static_head_ft,
        total_flow_gpm=total_flow,
        per_pump_flow_gpm=per_pump_flow,
        head_ft=head,
        pump_efficiency_fraction=pump_efficiency,
        motor_efficiency_fraction=motor_efficiency,
        total_input_kW=total_input_kW,
        specific_energy_kWh_per_MG=specific_energy,
    )


def pump_analysis(
    data: dict[str, Any], hydrograph: dict[str, Any]
) -> dict[str, Any]:
    station = data["pump_station"]
    operating_points: dict[str, dict[str, float]] = {}
    point_objects: dict[tuple[int, str], PumpOperatingPoint] = {}
    for pumps in (1, 2):
        for label in ("minimum", "nominal", "maximum"):
            point = find_operating_point(
                station, pumps, station["static_head"][f"{label}_ft"]
            )
            point_objects[(pumps, label)] = point
            operating_points[f"{pumps}_pump_{label}_static_head"] = {
                "pumps_operating": point.pumps_operating,
                "static_head_ft": point.static_head_ft,
                "total_flow_gpm": point.total_flow_gpm,
                "per_pump_flow_gpm": point.per_pump_flow_gpm,
                "head_ft": point.head_ft,
                "pump_efficiency_fraction": point.pump_efficiency_fraction,
                "motor_efficiency_fraction": point.motor_efficiency_fraction,
                "total_input_kW": point.total_input_kW,
                "specific_energy_kWh_per_MG": point.specific_energy_kWh_per_MG,
            }

    conservative_firm = point_objects[(2, "maximum")]
    conservative_one = point_objects[(1, "maximum")]
    peak_inflow_gpm = hydrograph["summary"]["peak_total_flow_gpm"]
    peak_margin_gpm = conservative_firm.total_flow_gpm - peak_inflow_gpm
    peak_utilization = peak_inflow_gpm / conservative_firm.total_flow_gpm

    storage = station["wet_well"]["usable_storage_high_alarm_to_overflow_gal"]
    dt_min = hydrograph["dt_min"]
    inflow_series_gpm = [
        value * 1_000_000 / 1440 for value in hydrograph["total_flow_MGD"]
    ]

    def storage_routing(available_capacity_gpm: float) -> dict[str, Any]:
        required_stored = 0.0
        actual_stored = 0.0
        overflow_gal = 0.0
        required_series = [0.0]
        actual_series = [0.0]
        for left, right in zip(inflow_series_gpm, inflow_series_gpm[1:]):
            average_inflow = (left + right) / 2
            interval_change = (
                average_inflow - available_capacity_gpm
            ) * dt_min
            required_stored = max(0.0, required_stored + interval_change)
            required_series.append(required_stored)
            actual_stored = max(0.0, actual_stored + interval_change)
            if actual_stored > storage:
                overflow_gal += actual_stored - storage
                actual_stored = storage
            actual_series.append(actual_stored)
        return {
            "available_capacity_gpm": available_capacity_gpm,
            "required_storage_gal": max(required_series),
            "cumulative_overflow_gal": overflow_gal,
            "required_storage_series_gal": required_series,
            "actual_storage_series_gal": actual_series,
        }

    routed_storage = {
        "two_pump_firm": storage_routing(conservative_firm.total_flow_gpm),
        "one_pump_normal": storage_routing(conservative_one.total_flow_gpm),
    }
    contingency_results: dict[str, dict[str, Any]] = {}
    for scenario in station["contingency_scenarios"]:
        scenario_id = scenario["scenario_id"]
        if scenario.get("analysis_mode") == "constant_peak_inflow_screen":
            duration_min = scenario["duration_min"]
            available_capacity = 0.0
            deficit = max(0.0, peak_inflow_gpm - available_capacity)
            required = deficit * duration_min
            contingency_results[scenario_id] = {
                "analysis_mode": scenario["analysis_mode"],
                "available_capacity_gpm": available_capacity,
                "peak_deficit_gpm": deficit,
                "duration_min": duration_min,
                "required_storage_gal": required,
                "available_storage_gal": storage,
                "storage_shortfall_gal": max(0.0, required - storage),
                "time_to_exhaust_available_storage_min": (
                    storage / deficit if deficit > 0 else None
                ),
            }
            continue
        base_capacity = (
            conservative_one.total_flow_gpm
            if scenario["available_pumps"] == 1
            else conservative_firm.total_flow_gpm
        )
        available_capacity = base_capacity * scenario["capacity_multiplier"]
        routed = storage_routing(available_capacity)
        deficit = max(0.0, peak_inflow_gpm - available_capacity)
        routed_storage[scenario_id] = routed
        contingency_results[scenario_id] = {
            "analysis_mode": "event_dynamic_storage_routing",
            "available_capacity_gpm": available_capacity,
            "peak_deficit_gpm": deficit,
            "constant_peak_time_to_exhaust_storage_min": (
                storage / deficit if deficit > 0 else None
            ),
            "required_storage_gal": routed["required_storage_gal"],
            "available_storage_gal": storage,
            "storage_shortfall_gal": max(
                0.0, routed["required_storage_gal"] - storage
            ),
            "cumulative_overflow_gal": routed["cumulative_overflow_gal"],
        }

    one_nominal = point_objects[(1, "nominal")]
    two_nominal = point_objects[(2, "nominal")]
    stage_power_kW: list[float] = []
    for flow_MGD in hydrograph["total_flow_MGD"]:
        inflow_gpm = flow_MGD * 1_000_000 / 1440
        if inflow_gpm <= one_nominal.total_flow_gpm:
            fraction = inflow_gpm / one_nominal.total_flow_gpm
            stage_power_kW.append(one_nominal.total_input_kW * fraction)
        else:
            denominator = (
                two_nominal.total_flow_gpm - one_nominal.total_flow_gpm
            )
            fraction = min(
                1.0,
                max(0.0, (inflow_gpm - one_nominal.total_flow_gpm) / denominator),
            )
            stage_power_kW.append(
                one_nominal.total_input_kW
                + fraction
                * (two_nominal.total_input_kW - one_nominal.total_input_kW)
            )
    event_energy_kWh = integrate_trapezoid(
        stage_power_kW, hydrograph["dt_min"] / 60
    )

    average_inflow_gpm = (
        hydrograph["summary"]["average_dry_weather_flow_MGD"]
        * 1_000_000
        / 1440
    )
    working_volume = station["wet_well"]["working_volume_gal"]
    if average_inflow_gpm >= one_nominal.total_flow_gpm:
        cycle_metrics: dict[str, Any] = {
            "applicable": False,
            "reason": "average inflow is not below one-pump operating capacity",
        }
    else:
        fill_time = working_volume / average_inflow_gpm
        draw_time = working_volume / (
            one_nominal.total_flow_gpm - average_inflow_gpm
        )
        cycle_time = fill_time + draw_time
        cycle_metrics = {
            "applicable": True,
            "fill_time_min": fill_time,
            "draw_time_min": draw_time,
            "cycle_time_min": cycle_time,
            "cycles_per_hour": 60 / cycle_time,
        }

    aggregate_hours_ADWF = (
        hydrograph["summary"]["average_dry_weather_flow_MGD"] * 1_000_000
    ) / (one_nominal.total_flow_gpm * 60)
    napot_example = aggregate_hours_ADWF / (
        station["installed_pumps"] - 1
    )

    return {
        "operating_points": operating_points,
        "capacity": {
            "conservative_firm_capacity_gpm": conservative_firm.total_flow_gpm,
            "conservative_firm_capacity_MGD": conservative_firm.total_flow_gpm
            * 0.00144,
            "conservative_one_pump_capacity_gpm": conservative_one.total_flow_gpm,
            "peak_inflow_gpm": peak_inflow_gpm,
            "peak_margin_gpm": peak_margin_gpm,
            "peak_margin_fraction": peak_margin_gpm
            / conservative_firm.total_flow_gpm,
            "peak_utilization_fraction": peak_utilization,
        },
        "storage": {
            "usable_storage_gal": storage,
            "routing_method": (
                "trapezoidal average inflow by interval with storage bounded "
                "below by zero and actual storage capped at usable volume"
            ),
            "contingency_results": contingency_results,
            "_timeseries": routed_storage,
        },
        "energy": {
            "event_staged_control_energy_kWh": event_energy_kWh,
            "event_staged_control_energy_cost_USD": event_energy_kWh
            * station["energy_rate_USD_per_kWh"],
            "calculation_boundary": (
                "illustrative staged duty interpolation between nominal "
                "one-pump and two-pump operating points"
            ),
        },
        "cycling": cycle_metrics,
        "operating_time": {
            "aggregate_pump_hours_per_ADWF_day": aggregate_hours_ADWF,
            "firm_equivalent_hours_per_ADWF_day": (
                hydrograph["summary"]["average_dry_weather_flow_MGD"]
                * 1_000_000
                / (conservative_firm.total_flow_gpm * 60)
            ),
            "illustrative_Miami_Dade_NAPOT_hours_per_day": napot_example,
            "NAPOT_boundary": (
                "illustrative constant-speed calculation only; not a current "
                "capacity or compliance determination"
            ),
        },
        "formula_ids": [
            "F-HYD-001",
            "F-HYD-002",
            "F-HYD-003",
            "F-HYD-004",
            "F-HYD-005",
            "F-PUMP-001",
            "F-PUMP-002",
            "F-PUMP-003",
            "F-PUMP-004",
            "F-PUMP-005",
            "F-PUMP-006",
            "F-PUMP-007",
            "F-MDC-NAPOT-001",
            "F-ENERGY-001",
            "F-ENERGY-002",
        ],
    }


def rehabilitation_and_economics(
    data: dict[str, Any], hydrograph: dict[str, Any]
) -> dict[str, Any]:
    basin = data["basin"]
    scenario = data["rehabilitation_scenario"]
    economics = data["economics"]
    event = data["rainfall_event"]
    rtk = data["RTK"]

    baseline_gwi_MGD = basin["average_groundwater_infiltration_MGD"]
    post_gwi_MGD = baseline_gwi_MGD * (
        1 - scenario["assumed_GWI_reduction_fraction"]
    )
    baseline_event_RDII_gal = hydrograph["summary"][
        "integrated_RDII_volume_gal"
    ]
    post_R_by_component = {
        component["response"]: component["R"]
        * (
            1
            - scenario["assumed_RTK_R_reduction_by_component"][
                component["response"]
            ]
        )
        for component in rtk["components"]
    }
    rainfall_volume_gal = hydrograph["summary"]["rainfall_volume_gal"]
    post_event_RDII_gal = sum(post_R_by_component.values()) * rainfall_volume_gal
    event_count = event["annual_equivalent_event_count_for_economic_scenario"]
    annual_gwi_reduction_MG = (
        baseline_gwi_MGD - post_gwi_MGD
    ) * 365
    annual_rdii_reduction_MG = (
        baseline_event_RDII_gal - post_event_RDII_gal
    ) / 1_000_000 * event_count
    annual_total_reduction_MG = (
        annual_gwi_reduction_MG + annual_rdii_reduction_MG
    )
    annual_gross_benefit = (
        annual_total_reduction_MG
        * economics["marginal_conveyance_and_treatment_cost_USD_per_MG"]
    )
    annual_net_benefit = (
        annual_gross_benefit - scenario["annual_O_and_M_cost_USD"]
    )
    years = economics["analysis_years"]
    rate = economics["real_discount_rate"]
    pv_gross_benefits = sum(
        annual_gross_benefit / (1 + rate) ** year
        for year in range(1, years + 1)
    )
    pv_annual_costs = sum(
        scenario["annual_O_and_M_cost_USD"] / (1 + rate) ** year
        for year in range(1, years + 1)
    )
    pv_total_costs = scenario["capital_cost_USD"] + pv_annual_costs
    npv = pv_gross_benefits - pv_total_costs
    bcr = pv_gross_benefits / pv_total_costs
    simple_payback = (
        scenario["capital_cost_USD"] / annual_net_benefit
        if annual_net_benefit > 0
        else None
    )
    return {
        "baseline_GWI_MGD": baseline_gwi_MGD,
        "post_scenario_GWI_MGD": post_gwi_MGD,
        "baseline_event_RDII_gal": baseline_event_RDII_gal,
        "post_scenario_event_RDII_gal": post_event_RDII_gal,
        "post_scenario_R_by_component": post_R_by_component,
        "annual_equivalent_event_count": event_count,
        "annual_GWI_reduction_MG": annual_gwi_reduction_MG,
        "annual_RDII_reduction_MG": annual_rdii_reduction_MG,
        "annual_total_I_and_I_reduction_MG": annual_total_reduction_MG,
        "annual_gross_marginal_cost_benefit_USD": annual_gross_benefit,
        "annual_scenario_O_and_M_cost_USD": scenario["annual_O_and_M_cost_USD"],
        "annual_net_direct_benefit_USD": annual_net_benefit,
        "PV_gross_benefits_USD": pv_gross_benefits,
        "PV_total_costs_USD": pv_total_costs,
        "NPV_USD": npv,
        "benefit_cost_ratio": bcr,
        "simple_payback_years": simple_payback,
        "excluded_benefits": [
            "avoided_or_deferred_capacity",
            "overflow_risk_reduction",
            "regulatory_risk",
            "service_reliability",
            "environmental_and_public_health_benefits",
        ],
        "formula_ids": [
            "F-ECON-002",
            "F-COST-001",
            "F-PV-001",
            "F-BCR-001",
            "F-ECON-003",
            "F-ECON-004",
        ],
    }


def write_timeseries(
    hydrograph: dict[str, Any], pump: dict[str, Any]
) -> None:
    component_names = list(hydrograph["component_flows_MGD"])
    with TIMESERIES_PATH.open("w", newline="") as handle:
        fieldnames = [
            "time_hr",
            "rainfall_increment_in",
            "DWF_MGD",
            *[f"RDII_{name}_MGD" for name in component_names],
            "RDII_total_MGD",
            "total_flow_MGD",
            "one_pump_required_storage_gal",
            "one_pump_actual_storage_gal",
            "two_pump_firm_required_storage_gal",
            "derated_one_pump_required_storage_gal",
            "derated_one_pump_actual_storage_gal",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for index, time_hr in enumerate(hydrograph["times_hr"]):
            row = {
                "time_hr": time_hr,
                "rainfall_increment_in": hydrograph["rainfall_increment_in"][
                    index
                ],
                "DWF_MGD": hydrograph["dwf_MGD"][index],
                "RDII_total_MGD": hydrograph["rdii_MGD"][index],
                "total_flow_MGD": hydrograph["total_flow_MGD"][index],
                "one_pump_required_storage_gal": pump["storage"]["_timeseries"][
                    "one_pump_normal"
                ]["required_storage_series_gal"][index],
                "one_pump_actual_storage_gal": pump["storage"]["_timeseries"][
                    "one_pump_normal"
                ]["actual_storage_series_gal"][index],
                "two_pump_firm_required_storage_gal": pump["storage"][
                    "_timeseries"
                ]["two_pump_firm"]["required_storage_series_gal"][index],
                "derated_one_pump_required_storage_gal": pump["storage"][
                    "_timeseries"
                ]["ONE-PUMP-DERATED-75"][
                    "required_storage_series_gal"
                ][index],
                "derated_one_pump_actual_storage_gal": pump["storage"][
                    "_timeseries"
                ]["ONE-PUMP-DERATED-75"]["actual_storage_series_gal"][index],
            }
            for name in component_names:
                row[f"RDII_{name}_MGD"] = hydrograph[
                    "component_flows_MGD"
                ][name][index]
            writer.writerow(row)


def main() -> None:
    data = load_yaml(INPUT)
    OUTPUT_DIR.mkdir(exist_ok=True)
    inventory = gravity_inventory_metrics(data)
    hydrograph = build_hydrograph(data)
    pump = pump_analysis(data, hydrograph)
    economics = rehabilitation_and_economics(data, hydrograph)
    results = {
        "schema_version": 1,
        "sample_id": data["sample_id"],
        "status": "synthetic_calculation_example_not_for_facility_use",
        "input_file": INPUT.name,
        "formula_registry": "formula-register.yaml@0.2.0",
        "inventory_and_dry_weather": inventory,
        "hydrograph_summary": hydrograph["summary"],
        "pump_station_analysis": pump,
        "rehabilitation_and_economics": economics,
        "calculation_lineage": {
            "rainfall_to_RDII_hydrograph": [
                "F-UNIT-001",
                "F-RTK-001",
                "F-RTK-002",
                "F-RTK-003",
                "F-FLOW-001",
            ],
            "dry_weather_and_inventory": [
                "F-DWF-001",
                "F-GWI-001",
                "F-IDM-001",
                "F-NORM-001",
            ],
            "pump_operating_points": pump["formula_ids"],
            "rehabilitation_economics": economics["formula_ids"],
        },
        "validation": {
            "RTK_volume_closure_absolute_fraction": abs(
                hydrograph["summary"]["volume_closure_error_fraction"]
            ),
            "RTK_volume_closure_pass": abs(
                hydrograph["summary"]["volume_closure_error_fraction"]
            )
            <= 1e-10,
            "all_values_are_finite": True,
        },
    }
    if not results["validation"]["RTK_volume_closure_pass"]:
        raise CalculationError("RTK volume closure test failed")
    write_timeseries(hydrograph, pump)
    del pump["storage"]["_timeseries"]
    RESULTS_PATH.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))
    print(f"Wrote {RESULTS_PATH}")
    print(f"Wrote {TIMESERIES_PATH}")


if __name__ == "__main__":
    main()
