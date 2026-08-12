#!/usr/bin/env python3

from __future__ import annotations

import json
import math
import subprocess
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "generated" / "sample-basin-results.json"


class SampleBasinGoldenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            ["python3", str(ROOT / "tools" / "run_sample_basin.py")],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        cls.result = json.loads(RESULTS.read_text())

    def assertClose(
        self, actual: float, expected: float, relative: float = 1e-9
    ) -> None:
        self.assertTrue(
            math.isclose(actual, expected, rel_tol=relative, abs_tol=1e-9),
            f"{actual} != {expected}",
        )

    def test_inventory_denominator(self) -> None:
        inventory = self.result["inventory_and_dry_weather"]
        self.assertClose(inventory["inch_diameter_mile"], 412)
        self.assertClose(
            inventory["GWI_gpd_per_inch_diameter_mile"],
            606.7961165048544,
        )

    def test_rtk_mass_closure_and_capture_fraction(self) -> None:
        summary = self.result["hydrograph_summary"]
        self.assertLess(abs(summary["volume_closure_error_fraction"]), 1e-12)
        self.assertClose(summary["capture_fraction_total_R"], 0.032)
        self.assertClose(summary["integrated_RDII_volume_gal"], 1779583.2685714287)

    def test_peak_flow_and_firm_capacity(self) -> None:
        capacity = self.result["pump_station_analysis"]["capacity"]
        self.assertClose(capacity["peak_inflow_gpm"], 2728.2644151404156)
        self.assertClose(
            capacity["conservative_firm_capacity_gpm"], 4129.75, relative=1e-6
        )
        self.assertGreater(capacity["peak_margin_gpm"], 0)
        self.assertLess(capacity["peak_utilization_fraction"], 1)

    def test_contingency_storage_outcomes(self) -> None:
        scenarios = self.result["pump_station_analysis"]["storage"][
            "contingency_results"
        ]
        self.assertClose(
            scenarios["ONE-PUMP-NORMAL"]["required_storage_gal"], 0
        )
        self.assertClose(
            scenarios["ONE-PUMP-DERATED-75"]["required_storage_gal"],
            75311.84486630038,
            relative=1e-8,
        )
        self.assertClose(
            scenarios["COMPLETE-OUTAGE-30-MIN"]["storage_shortfall_gal"],
            36847.93245421247,
            relative=1e-8,
        )

    def test_economics_preserve_negative_result(self) -> None:
        economics = self.result["rehabilitation_and_economics"]
        self.assertLess(economics["NPV_USD"], 0)
        self.assertIsNone(economics["simple_payback_years"])
        self.assertClose(
            economics["benefit_cost_ratio"], 0.03301665724389744
        )

    def test_formula_lineage_resolves(self) -> None:
        registry = yaml.safe_load((ROOT / "formula-register.yaml").read_text())
        known = {item["id"] for item in registry["formulae"]}
        wired = {
            formula_id
            for formula_ids in self.result["calculation_lineage"].values()
            for formula_id in formula_ids
        }
        self.assertFalse(wired - known, f"unknown formula IDs: {wired - known}")
        self.assertEqual(
            self.result["formula_registry"],
            f"formula-register.yaml@{registry['version']}",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
