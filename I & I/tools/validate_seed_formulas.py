#!/usr/bin/env python3

from __future__ import annotations

import math
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "calculation-test-vectors.yaml"
ACRE_INCH_GALLONS = 27154.285714285714


class CalculationError(ValueError):
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


def rainfall_volume(inputs: dict) -> dict:
    area = inputs.get("A_ac")
    rainfall = inputs.get("P_in")
    if area is None:
        raise CalculationError("missing_area_boundary")
    if rainfall is None:
        raise CalculationError("missing_rainfall_depth")
    return {"V_rain_gal": rainfall * area * ACRE_INCH_GALLONS}


def trapezoidal_volume(inputs: dict) -> dict:
    average_flow = (inputs["Q_start_gpm"] + inputs["Q_end_gpm"]) / 2
    return {"V_gal": average_flow * inputs["delta_t_min"]}


def weighted_adwf(inputs: dict) -> dict:
    samples = inputs["samples"]
    represented_minutes = sum(row["represented_minutes"] for row in samples)
    if represented_minutes <= 0:
        raise CalculationError("nonpositive_represented_time")
    flow_minutes = sum(
        row["Q_gpm"] * row["represented_minutes"] for row in samples
    )
    return {"ADWF_gpm": flow_minutes / represented_minutes}


def rdii_volume(inputs: dict) -> dict:
    residual = inputs["Q_observed_gpm"] - inputs["Q_expected_DWF_gpm"]
    return {"V_RDII_gal": residual * inputs["duration_min"]}


def capture_fraction(inputs: dict) -> dict:
    if "V_rain_gal" in inputs:
        rain_volume = inputs["V_rain_gal"]
    else:
        rain_volume = rainfall_volume(inputs)["V_rain_gal"]
    if rain_volume <= 0:
        raise CalculationError("nonpositive_rainfall_volume")
    fraction = inputs["V_RDII_gal"] / rain_volume
    return {"R_event": fraction, "R_event_percent": 100 * fraction}


def normalized_flow(inputs: dict) -> dict:
    denominator = sum(row["D_in"] * row["L_mi"] for row in inputs["segments"])
    if denominator <= 0:
        raise CalculationError("nonpositive_inventory_denominator")
    return {
        "denominator_inch_diameter_mile": denominator,
        "q_gpd_per_inch_diameter_mile": inputs["Q_gpd"] / denominator,
    }


def peak_ratio(inputs: dict) -> dict:
    adwf = inputs["ADWF_MGD"]
    if adwf <= 0:
        raise CalculationError("nonpositive_ADWF")
    return {"PWWF_ratio": inputs["Q_peak_wet_weather_MGD"] / adwf}


def rtk_triangle(inputs: dict) -> dict:
    volume = (
        inputs["R_i"] * inputs["P_in"] * inputs["A_ac"] * ACRE_INCH_GALLONS
    )
    base_duration = inputs["T_i_hr"] * (1 + inputs["K_i"])
    peak_gallons_per_hour = 2 * volume / base_duration
    return {
        "V_i_gal": volume,
        "base_duration_hr": base_duration,
        "Q_peak_gal_per_hr": peak_gallons_per_hour,
        "Q_peak_gpm": peak_gallons_per_hour / 60,
    }


def present_value(inputs: dict) -> dict:
    rate = inputs["annual_discount_rate"]
    if rate <= -1:
        raise CalculationError("invalid_discount_rate")
    cash_flows = inputs["cash_flows"]
    value = sum(
        amount / (1 + rate) ** int(year_label.removeprefix("year_"))
        for year_label, amount in cash_flows.items()
    )
    return {"PV": value}


CALCULATORS = {
    "TV-UNIT-001": rainfall_volume,
    "TV-FLOW-001": trapezoidal_volume,
    "TV-DWF-001": weighted_adwf,
    "TV-RDII-001": rdii_volume,
    "TV-R-001": capture_fraction,
    "TV-NORM-001": normalized_flow,
    "TV-PEAK-001": peak_ratio,
    "TV-RTK-001": rtk_triangle,
    "TV-PV-001": present_value,
    "FTV-UNIT-001": rainfall_volume,
    "FTV-R-001": capture_fraction,
    "FTV-NORM-001": normalized_flow,
    "FTV-PEAK-001": peak_ratio,
}


def assert_close(actual: float, expected: float, rel_tol: float, abs_tol: float) -> None:
    if not math.isclose(actual, expected, rel_tol=rel_tol, abs_tol=abs_tol):
        raise AssertionError(f"expected {expected!r}, received {actual!r}")


def main() -> None:
    suite = yaml.safe_load(VECTORS.read_text())
    rel_tol = suite["numeric_policy"]["relative_tolerance_default"]
    abs_tol = suite["numeric_policy"]["absolute_tolerance_default"]
    passed = 0

    for test in suite["tests"]:
        actual = CALCULATORS[test["id"]](test["inputs"])
        for key, expected in test["expected"].items():
            assert_close(actual[key], expected, rel_tol, abs_tol)
        passed += 1
        print(f"PASS {test['id']}")

    for test in suite["failure_tests"]:
        try:
            CALCULATORS[test["id"]](test["inputs"])
        except CalculationError as error:
            if error.code != test["expected_error"]:
                raise AssertionError(
                    f"{test['id']} expected {test['expected_error']}, "
                    f"received {error.code}"
                ) from error
        else:
            raise AssertionError(f"{test['id']} did not fail closed")
        passed += 1
        print(f"PASS {test['id']}")

    print(f"{passed} seed formula tests passed")


if __name__ == "__main__":
    main()
