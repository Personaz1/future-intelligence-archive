#!/usr/bin/env python3
"""Summarize REE circuit transport ratings without mislabelling them as MW.

Input: the FeatureCollection written by ree_transmission_geojson.py.
Output: descriptive statistics in original MVA units. No capacity totals,
network-flow inference, or connection-hosting-capacity estimate is produced.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

MONTHS = {
    "ENE": "January", "FEB": "February", "MAR": "March", "ABR": "April",
    "MAY": "May", "JUN": "June", "JUL": "July", "AGO": "August",
    "SEP": "September", "OCT": "October", "NOV": "November", "DIC": "December",
}


def percentile(values: list[float], p: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    position = (len(ordered) - 1) * p
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (position - lower)


def summarize(features: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for feature in features:
        props = feature.get("properties") or {}
        key = (
            str(props.get("TENSION") or "unknown"),
            str(props.get("ESTADO") or "unknown"),
            str(props.get("PAIS") or "unknown"),
        )
        groups[key].append(props)

    output: dict[str, Any] = {
        "unit": "MVA",
        "metric": "REE circuit transport rating",
        "aggregation_policy": (
            "Descriptive distributions only. No sum is calculated because "
            "circuit ratings are not independent connection capacity."
        ),
        "feature_count": len(features),
        "groups": [],
    }

    for (voltage, status, country), records in sorted(groups.items()):
        monthly = {}
        for code, month in MONTHS.items():
            field = f"CAP_{code}"
            raw = [record.get(field) for record in records]
            numeric = []
            for value in raw:
                if value is None or value == "":
                    continue
                try:
                    numeric.append(float(value))
                except (TypeError, ValueError):
                    continue
            limits = Counter(
                str(record.get(f"ELEM_LIM_{code}"))
                for record in records
                if record.get(f"ELEM_LIM_{code}") not in (None, "")
            )
            monthly[month] = {
                "field": field,
                "records": len(records),
                "valid_values": len(numeric),
                "missing_or_invalid": len(records) - len(numeric),
                "zero_values": sum(value == 0 for value in numeric),
                "min": min(numeric) if numeric else None,
                "p10": percentile(numeric, 0.10),
                "median": statistics.median(numeric) if numeric else None,
                "p90": percentile(numeric, 0.90),
                "max": max(numeric) if numeric else None,
                "limiting_elements": dict(limits.most_common()),
            }
        output["groups"].append({
            "voltage_kv": voltage,
            "status_code": status,
            "country_code": country,
            "circuit_records": len(records),
            "monthly": monthly,
        })
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="circuits.geojson")
    parser.add_argument("--out", type=Path, default=Path("circuit-rating-summary.json"))
    args = parser.parse_args()

    collection = json.loads(args.input.read_text(encoding="utf-8"))
    if collection.get("type") != "FeatureCollection":
        raise ValueError("Input is not a GeoJSON FeatureCollection")
    result = summarize(collection.get("features", []))
    args.out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        f"features={result['feature_count']} groups={len(result['groups'])} "
        f"output={args.out}"
    )


if __name__ == "__main__":
    main()
