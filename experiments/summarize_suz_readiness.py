#!/usr/bin/env python3
"""Summarize SU-SUZ normalized records for the province of Alicante.

Input: JSONL from normalize_suz_development_readiness.py.
Output: descriptive counts only; no legal buildability or grid-capacity score.

Usage:
  python experiments/summarize_suz_readiness.py normalized.jsonl summary.json
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


def province_code(value: Any) -> str:
    text = "" if value is None else str(value).strip()
    if text.isdigit():
        return text.zfill(5)[:2]
    return text[:2]


def summarize(records: list[dict[str, Any]], province: str = "03") -> dict[str, Any]:
    selected = [
        record for record in records
        if province_code(record.get("normalized", {}).get("municipality_ine_code")) == province
    ]
    industrial = [
        record for record in selected
        if str(record.get("normalized", {}).get("global_land_use") or "").strip().casefold()
        in {"industrial", "industria", "industrial"}
    ]

    def distribution(items: list[dict[str, Any]], path: tuple[str, ...]) -> dict[str, int]:
        counts: Counter[str] = Counter()
        for item in items:
            value: Any = item
            for key in path:
                value = value.get(key) if isinstance(value, dict) else None
            label = "not_recorded" if value in (None, "") else str(value)
            counts[label] += 1
        return dict(sorted(counts.items()))

    return {
        "scope": {
            "province_ine_prefix": province,
            "province_name": "Alicante / Alacant",
            "input_record_count": len(records),
            "province_record_count": len(selected),
            "industrial_record_count": len(industrial),
        },
        "industrial_sector_distributions": {
            "partial_plan_approved": distribution(industrial, ("readiness", "partial_plan_approved")),
            "PAI_award": distribution(industrial, ("readiness", "PAI_award")),
            "reparcelation": distribution(industrial, ("readiness", "reparcelation")),
            "urbanisation_works": distribution(industrial, ("readiness", "urbanisation_works")),
            "grid_capacity": distribution(industrial, ("readiness", "grid_capacity")),
        },
        "industrial_service_distributions": {
            service: distribution(industrial, ("readiness", "services", service))
            for service in (
                "road_access", "potable_water", "electrical_installation",
                "sewerage", "stormwater_collection",
            )
        },
        "interpretation_limits": [
            "Counts describe the supplied SU-SUZ snapshot only; they do not establish completeness.",
            "The inventory is informative, not a binding planning determination.",
            "Electrical installation presence is not grid-access capacity or a connection right.",
            "No parcel geometry is present in this normalized CSV summary.",
            "The source CSV may represent an inventory of development sectors, not all industrial land.",
        ],
    }


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise ValueError(f"Invalid JSON on line {line_number}: {error}") from error
    return records


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        raise SystemExit("Usage: summarize_suz_readiness.py normalized.jsonl summary.json")
    result = summarize(read_jsonl(Path(argv[1])))
    output = Path(argv[2])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
