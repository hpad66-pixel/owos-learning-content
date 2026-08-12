#!/usr/bin/env python3

from __future__ import annotations

import csv
import html
import json
import math
import sys
from pathlib import Path
from typing import Callable

import yaml


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
sys.path.insert(0, str(ROOT / "tools"))
import run_sample_basin as engine  # noqa: E402


WIDTH = 1200
HEIGHT = 680
PLOT = (110, 120, 1010, 450)
COLORS = {
    "navy": "#12233f",
    "blue": "#176b87",
    "cyan": "#36a9c5",
    "orange": "#ef8354",
    "gold": "#e6b655",
    "green": "#2a9d78",
    "red": "#c94c4c",
    "gray": "#667085",
    "light": "#e9eef3",
    "paper": "#f7f5f0",
}


def svg_document(title: str, description: str, content: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">{html.escape(title)}</title>
<desc id="desc">{html.escape(description)}</desc>
<rect width="1200" height="680" fill="{COLORS['paper']}"/>
<style>
text {{ font-family: Inter, Arial, sans-serif; fill: {COLORS['navy']}; }}
.title {{ font-size: 28px; font-weight: 700; }}
.subtitle {{ font-size: 15px; fill: {COLORS['gray']}; }}
.axis {{ stroke: {COLORS['navy']}; stroke-width: 1.5; }}
.grid {{ stroke: #d6dde4; stroke-width: 1; }}
.tick {{ font-size: 13px; fill: {COLORS['gray']}; }}
.label {{ font-size: 15px; font-weight: 600; }}
.legend {{ font-size: 14px; }}
</style>
{content}
</svg>
"""


def scale(value: float, low: float, high: float, out_low: float, out_high: float) -> float:
    return out_low + (value - low) * (out_high - out_low) / (high - low)


def chart_frame(
    title: str,
    subtitle: str,
    x_label: str,
    y_label: str,
    x_ticks: list[float],
    y_ticks: list[float],
    x_range: tuple[float, float],
    y_range: tuple[float, float],
) -> str:
    x0, y0, plot_w, plot_h = PLOT
    parts = [
        f'<text x="{x0}" y="38" class="title">{html.escape(title)}</text>',
        f'<text x="{x0}" y="61" class="subtitle">{html.escape(subtitle)}</text>',
    ]
    for tick in y_ticks:
        y = scale(tick, *y_range, y0 + plot_h, y0)
        parts.append(f'<line x1="{x0}" y1="{y:.2f}" x2="{x0 + plot_w}" y2="{y:.2f}" class="grid"/>')
        parts.append(f'<text x="{x0 - 12}" y="{y + 5:.2f}" text-anchor="end" class="tick">{tick:g}</text>')
    for tick in x_ticks:
        x = scale(tick, *x_range, x0, x0 + plot_w)
        parts.append(f'<line x1="{x:.2f}" y1="{y0}" x2="{x:.2f}" y2="{y0 + plot_h}" class="grid"/>')
        parts.append(f'<text x="{x:.2f}" y="{y0 + plot_h + 25}" text-anchor="middle" class="tick">{tick:g}</text>')
    parts.extend(
        [
            f'<line x1="{x0}" y1="{y0 + plot_h}" x2="{x0 + plot_w}" y2="{y0 + plot_h}" class="axis"/>',
            f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 + plot_h}" class="axis"/>',
            f'<text x="{x0 + plot_w / 2}" y="{y0 + plot_h + 60}" text-anchor="middle" class="label">{html.escape(x_label)}</text>',
            f'<text x="28" y="{y0 + plot_h / 2}" text-anchor="middle" transform="rotate(-90 28 {y0 + plot_h / 2})" class="label">{html.escape(y_label)}</text>',
        ]
    )
    return "".join(parts)


def polyline(
    xs: list[float],
    ys: list[float],
    x_range: tuple[float, float],
    y_range: tuple[float, float],
    color: str,
    width: float = 4,
    dash: str | None = None,
) -> str:
    x0, y0, plot_w, plot_h = PLOT
    points = " ".join(
        f"{scale(x, *x_range, x0, x0 + plot_w):.2f},{scale(y, *y_range, y0 + plot_h, y0):.2f}"
        for x, y in zip(xs, ys)
    )
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"{dash_attr}/>'


def legend(items: list[tuple[str, str]], x: int = 710, y: int = 30) -> str:
    parts: list[str] = []
    for index, (label, color) in enumerate(items):
        item_x = x + (index % 3) * 160
        item_y = y + (index // 3) * 24
        parts.append(f'<line x1="{item_x}" y1="{item_y}" x2="{item_x + 25}" y2="{item_y}" stroke="{color}" stroke-width="5"/>')
        parts.append(f'<text x="{item_x + 33}" y="{item_y + 5}" class="legend">{html.escape(label)}</text>')
    return "".join(parts)


def write_schematic() -> None:
    boxes = [
        (45, 160, 175, 105, "Rainfall and\nGroundwater", COLORS["cyan"]),
        (260, 160, 175, 105, "Entry\nPathways", COLORS["orange"]),
        (475, 160, 175, 105, "Gravity Basin\nand Meter", COLORS["blue"]),
        (690, 160, 175, 105, "Wet Well and\nPump Station", COLORS["gold"]),
        (905, 160, 220, 105, "Force Main and\nDownstream Node", COLORS["green"]),
    ]
    parts = [
        '<text x="45" y="55" class="title">One-basin calculation boundary</text>',
        '<text x="45" y="83" class="subtitle">The agent follows water, data, formulas, decisions, and verification through one declared control volume.</text>',
        '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#12233f"/></marker></defs>',
    ]
    for x, y, w, h, label, color in boxes:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" opacity="0.18" stroke="{color}" stroke-width="3"/>')
        for line_index, line in enumerate(label.split("\n")):
            parts.append(f'<text x="{x + w / 2}" y="{y + 45 + line_index * 25}" text-anchor="middle" class="label">{html.escape(line)}</text>')
    for left, right in zip(boxes, boxes[1:]):
        x1 = left[0] + left[2]
        x2 = right[0]
        y = left[1] + left[3] / 2
        parts.append(f'<line x1="{x1 + 8}" y1="{y}" x2="{x2 - 8}" y2="{y}" stroke="{COLORS["navy"]}" stroke-width="3" marker-end="url(#arrow)"/>')
    layers = [
        (115, 350, "PHYSICAL LAYER", "Assets, defects, groundwater, rain, flow, head, storage, energy"),
        (115, 420, "COMPUTATION LAYER", "DWF + GWI + RTK RDII + hydraulic operating point + storage routing + economics"),
        (115, 490, "EVIDENCE LAYER", "Source locator + units + data-quality state + applicability + uncertainty + formula version"),
        (115, 560, "DECISION LAYER", "Screen, diagnose, model, rehabilitate, verify, and block unsupported conclusions"),
    ]
    for _x, y, label, text_value in layers:
        parts.append(f'<rect x="45" y="{y - 30}" width="1080" height="52" rx="8" fill="#ffffff" stroke="#d6dde4"/>')
        parts.append(f'<text x="70" y="{y}" class="label">{label}</text>')
        parts.append(f'<text x="300" y="{y}" class="subtitle">{html.escape(text_value)}</text>')
    (FIGURES / "01-basin-calculation-boundary.svg").write_text(
        svg_document(
            "One-basin calculation boundary",
            "A five-stage sanitary sewer basin from water sources through force-main discharge, with physical, computation, evidence, and decision layers.",
            "".join(parts),
        )
    )


def write_hydrograph(rows: list[dict[str, str]]) -> None:
    times = [float(row["time_hr"]) for row in rows]
    dwf = [float(row["DWF_MGD"]) for row in rows]
    rdii = [float(row["RDII_total_MGD"]) for row in rows]
    total = [float(row["total_flow_MGD"]) for row in rows]
    x_range = (0.0, max(times))
    y_range = (0.0, 4.5)
    content = chart_frame(
        "Event hydrograph and flow decomposition",
        "Synthetic 3.2-inch event; 15-minute increments; RTK total R = 0.032",
        "Elapsed time (hr)",
        "Flow (MGD)",
        list(range(0, 67, 12)),
        [0, 1, 2, 3, 4],
        x_range,
        y_range,
    )
    content += polyline(times, total, x_range, y_range, COLORS["navy"], 5)
    content += polyline(times, rdii, x_range, y_range, COLORS["orange"], 4)
    content += polyline(times, dwf, x_range, y_range, COLORS["blue"], 3, "10 7")
    content += legend(
        [("Total flow", COLORS["navy"]), ("RDII", COLORS["orange"]), ("Expected DWF", COLORS["blue"])],
        x=650,
        y=92,
    )
    (FIGURES / "02-event-hydrograph.svg").write_text(
        svg_document(
            "Event hydrograph and flow decomposition",
            "Line chart showing expected dry-weather flow, rainfall-derived inflow and infiltration, and total flow over 66 hours.",
            content,
        )
    )


def write_pump_curves(data: dict, result: dict) -> None:
    station = data["pump_station"]
    curve = station["pump_curve"]["points"]
    x_values = list(range(0, 6501, 50))
    x_range = (0.0, 6500.0)
    y_range = (0.0, 160.0)
    content = chart_frame(
        "Pump and system curves",
        "Operating point is the pump-curve and system-curve intersection; maximum static head governs the firm-capacity screen.",
        "Total station flow (gpm)",
        "Head (ft)",
        [0, 1000, 2000, 3000, 4000, 5000, 6000],
        [0, 25, 50, 75, 100, 125, 150],
        x_range,
        y_range,
    )
    for pumps, color, label in (
        (1, COLORS["blue"], "1 pump"),
        (2, COLORS["cyan"], "2 pumps"),
    ):
        valid_x = [x for x in x_values if x <= curve[-1]["flow_gpm"] * pumps]
        heads = [engine.pump_head(x, pumps, curve) for x in valid_x]
        content += polyline(valid_x, heads, x_range, y_range, color, 4)
    system_items = [
        ("minimum", COLORS["green"]),
        ("nominal", COLORS["gold"]),
        ("maximum", COLORS["red"]),
    ]
    for label, color in system_items:
        valid_x: list[float] = []
        heads: list[float] = []
        for x in x_values:
            try:
                head = engine.system_head(
                    x,
                    station["static_head"][f"{label}_ft"],
                    station["force_main"],
                )["system_head_ft"]
            except engine.CalculationError:
                continue
            if head <= y_range[1]:
                valid_x.append(x)
                heads.append(head)
        content += polyline(valid_x, heads, x_range, y_range, color, 3, "8 6")
    for key in ("1_pump_maximum_static_head", "2_pump_maximum_static_head"):
        point = result["pump_station_analysis"]["operating_points"][key]
        x = scale(point["total_flow_gpm"], *x_range, PLOT[0], PLOT[0] + PLOT[2])
        y = scale(point["head_ft"], *y_range, PLOT[1] + PLOT[3], PLOT[1])
        content += f'<circle cx="{x:.2f}" cy="{y:.2f}" r="8" fill="{COLORS["navy"]}" stroke="#ffffff" stroke-width="3"/>'
    content += legend(
        [
            ("1 pump", COLORS["blue"]),
            ("2 pumps", COLORS["cyan"]),
            ("Min system", COLORS["green"]),
            ("Nominal system", COLORS["gold"]),
            ("Max system", COLORS["red"]),
        ],
        x=590,
        y=90,
    )
    (FIGURES / "03-pump-system-curves.svg").write_text(
        svg_document(
            "Pump and system curves",
            "One-pump and two-pump head curves with minimum, nominal, and maximum static-head system curves and the conservative operating points.",
            content,
        )
    )


def write_storage(rows: list[dict[str, str]], result: dict) -> None:
    times = [float(row["time_hr"]) for row in rows]
    required = [float(row["derated_one_pump_required_storage_gal"]) for row in rows]
    actual = [float(row["derated_one_pump_actual_storage_gal"]) for row in rows]
    available = result["pump_station_analysis"]["storage"]["usable_storage_gal"]
    x_range = (0.0, max(times))
    y_range = (0.0, 85000.0)
    content = chart_frame(
        "Derated one-pump storage routing",
        "Theoretical required storage reaches 75,312 gal; usable high-alarm-to-overflow storage is 45,000 gal.",
        "Elapsed time (hr)",
        "Storage (gal)",
        list(range(0, 67, 12)),
        [0, 15000, 30000, 45000, 60000, 75000],
        x_range,
        y_range,
    )
    content += polyline(times, required, x_range, y_range, COLORS["red"], 5)
    content += polyline(times, actual, x_range, y_range, COLORS["orange"], 3)
    content += polyline([0, max(times)], [available, available], x_range, y_range, COLORS["navy"], 3, "12 8")
    content += legend(
        [("Required", COLORS["red"]), ("Actual capped", COLORS["orange"]), ("Usable volume", COLORS["navy"])],
        x=650,
        y=92,
    )
    (FIGURES / "04-contingency-storage.svg").write_text(
        svg_document(
            "Derated one-pump storage routing",
            "Required and actual wet-well storage for a one-pump capacity derated to 75 percent, including the 45,000-gallon usable storage limit.",
            content,
        )
    )


def write_economics(result: dict) -> None:
    econ = result["rehabilitation_and_economics"]
    values = [
        ("PV benefits", econ["PV_gross_benefits_USD"]),
        ("PV costs", econ["PV_total_costs_USD"]),
        ("NPV", econ["NPV_USD"]),
    ]
    baseline = 0
    center = 350
    scale_value: Callable[[float], float] = lambda value: value / 11_000_000 * 260
    parts = [
        '<text x="75" y="55" class="title">Direct marginal-cost economic screen</text>',
        '<text x="75" y="82" class="subtitle">Capacity, overflow, compliance, reliability, environmental, and public-health benefits are deliberately excluded.</text>',
        f'<line x1="250" y1="{center}" x2="1120" y2="{center}" class="axis"/>',
    ]
    for index, (label, value) in enumerate(values):
        x = 340 + index * 260
        height = abs(scale_value(value))
        y = center - height if value >= 0 else center
        color = COLORS["green"] if value >= 0 else COLORS["red"]
        parts.append(f'<rect x="{x}" y="{y:.2f}" width="150" height="{height:.2f}" rx="5" fill="{color}" opacity="0.82"/>')
        parts.append(f'<text x="{x + 75}" y="{center + 35}" text-anchor="middle" class="label">{html.escape(label)}</text>')
        value_y = y - 12 if value >= 0 else y + height + 25
        parts.append(f'<text x="{x + 75}" y="{value_y:.2f}" text-anchor="middle" class="label">${value / 1_000_000:,.2f}M</text>')
    parts.append('<text x="75" y="655" class="subtitle">Interpretation: the narrow direct-cost screen fails. It is not a complete benefit-cost determination.</text>')
    (FIGURES / "05-economic-screen.svg").write_text(
        svg_document(
            "Direct marginal-cost economic screen",
            "Bar chart comparing present-value gross benefits, costs, and negative net present value for the hypothetical rehabilitation scenario.",
            "".join(parts),
        )
    )


def write_lineage() -> None:
    parts = [
        '<text x="60" y="50" class="title">Calculation lineage for the one-basin engine</text>',
        '<text x="60" y="78" class="subtitle">Every result remains connected to accepted inputs, a versioned formula, tests, and a decision boundary.</text>',
        '<defs><marker id="arrow2" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#667085"/></marker></defs>',
    ]
    nodes = [
        (55, 145, 190, 75, "Asset inventory", COLORS["blue"]),
        (55, 250, 190, 75, "Dry-weather flow", COLORS["cyan"]),
        (55, 355, 190, 75, "Rainfall", COLORS["orange"]),
        (320, 145, 210, 75, "IDM and GWI", COLORS["blue"]),
        (320, 250, 210, 75, "Expected DWF", COLORS["cyan"]),
        (320, 355, 210, 75, "RTK hydrograph", COLORS["orange"]),
        (605, 200, 220, 75, "Total basin inflow", COLORS["navy"]),
        (605, 330, 220, 75, "Pump and system point", COLORS["gold"]),
        (895, 200, 245, 75, "Capacity and storage", COLORS["red"]),
        (895, 330, 245, 75, "Energy and economics", COLORS["green"]),
    ]
    for x, y, w, h, label, color in nodes:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}" opacity="0.17" stroke="{color}" stroke-width="3"/>')
        parts.append(f'<text x="{x + w / 2}" y="{y + 45}" text-anchor="middle" class="label">{html.escape(label)}</text>')
    arrows = [
        (245, 182, 320, 182),
        (245, 287, 320, 287),
        (245, 392, 320, 392),
        (530, 287, 605, 237),
        (530, 392, 605, 237),
        (530, 182, 895, 237),
        (825, 237, 895, 237),
        (825, 367, 895, 367),
        (715, 275, 715, 330),
    ]
    for x1, y1, x2, y2 in arrows:
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{COLORS["gray"]}" stroke-width="3" marker-end="url(#arrow2)"/>')
    checks = [
        ("Units", "declared"),
        ("Domain", "passed"),
        ("Mass balance", "closed"),
        ("Formula", "versioned"),
        ("Sources", "located"),
        ("Review", "gated"),
    ]
    for index, (label, value) in enumerate(checks):
        x = 65 + index * 185
        parts.append(f'<rect x="{x}" y="520" width="165" height="90" rx="8" fill="#ffffff" stroke="#d6dde4"/>')
        parts.append(f'<text x="{x + 82.5}" y="552" text-anchor="middle" class="subtitle">{label}</text>')
        parts.append(f'<text x="{x + 82.5}" y="585" text-anchor="middle" class="label">{value}</text>')
    (FIGURES / "06-calculation-lineage.svg").write_text(
        svg_document(
            "Calculation lineage for the one-basin engine",
            "A directed graph from asset, dry-weather, and rainfall inputs through RTK, pump, storage, energy, and economics, with six validation gates.",
            "".join(parts),
        )
    )


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    data = yaml.safe_load((ROOT / "sample-basin.yaml").read_text())
    result = json.loads(
        (ROOT / "generated" / "sample-basin-results.json").read_text()
    )
    with (ROOT / "generated" / "sample-basin-timeseries.csv").open() as handle:
        rows = list(csv.DictReader(handle))
    write_schematic()
    write_hydrograph(rows)
    write_pump_curves(data, result)
    write_storage(rows, result)
    write_economics(result)
    write_lineage()
    print(f"Wrote 6 SVG figures to {FIGURES}")


if __name__ == "__main__":
    main()
