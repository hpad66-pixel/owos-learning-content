#!/usr/bin/env python3
"""Run an approved EPA SWMM input file and export selected PySWMM results."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from pyswmm import Links, Nodes, Simulation


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run SWMM and export one node and one link time series."
    )
    parser.add_argument("model", type=Path, help="Path to the approved SWMM .inp file")
    parser.add_argument("--node", required=True, help="SWMM node identifier")
    parser.add_argument("--link", required=True, help="SWMM link identifier")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("swmm_results.csv"),
        help="CSV output path",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    model = args.model.resolve()
    if not model.is_file():
        raise FileNotFoundError(f"SWMM model not found: {model}")
    if model.suffix.lower() != ".inp":
        raise ValueError("The model must be a SWMM .inp file")

    rows: list[dict[str, object]] = []
    with Simulation(str(model)) as simulation:
        nodes = Nodes(simulation)
        links = Links(simulation)
        node = nodes[args.node]
        link = links[args.link]

        for _ in simulation:
            rows.append(
                {
                    "timestamp": simulation.current_time.isoformat(),
                    "node_id": args.node,
                    "node_depth": node.depth,
                    "node_total_inflow": node.total_inflow,
                    "node_flooding": node.flooding,
                    "link_id": args.link,
                    "link_flow": link.flow,
                    "link_depth": link.depth,
                }
            )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else [])
        if rows:
            writer.writeheader()
            writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {args.output.resolve()}")


if __name__ == "__main__":
    main()
