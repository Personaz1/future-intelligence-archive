#!/usr/bin/env python3
"""Normalize ICV SU-SUZ planning-sector attributes into readiness evidence.

Input is the ICV WFS CSV export for feature type InventarioSuSuz.
The output preserves every raw source field and adds explicit normalized
states. It does not calculate a legal buildability score or infer grid capacity.

Usage:
  python experiments/normalize_suz_development_readiness.py input.csv output.jsonl

Python 3.10+, standard library only.
"""
from __future__ import annotations

import csv
import json
import sys
import unicodedata
from pathlib import Path
from typing import Any


FIELD_MAP = {
    "municipality": "municipio",
    "municipality_ine_code": "cpm",
    "partial_plan_name": "pp",
    "execution_unit": "ue",
    "global_land_use": "uso",
    "planning_area_m2": "sup",
    "permitted_buildable_floor_area_m2": "edif_total",
    "partial_plan_approval_date": "f_aprob",
    "partial_plan_publication_date": "f_public",
    "approving_authority": "org_res",
    "planning_legal_framework": "legisl",
    "partial_plan_approved": "ord_porm",
    "development_management": "gestion",
    "PAI_awarded": "pai",
    "reparcelation_status": "Pr_repc",
    "reparcelation_registry_date": "f_reparc",
    "urbanisation_project_exists": "p_urbaniz",
    "urbanisation_works_start_date": "f_incio",
    "urbanisation_works_acceptance_date": "f_recep",
    "road_access": "f1acceso_r",
    "sidewalks": "f2aceras",
    "public_lighting": "f3alumbrad",
    "potable_water": "f4agua_pot",
    "electrical_installation": "f5electric",
    "sewerage": "f6alcantar",
    "stormwater_collection": "f7pluviale",
    "collector_connection": "f8colector",
}

SERVICE_FIELDS = {
    "road_access": "f1acceso_r",
    "sidewalks": "f2aceras",
    "public_lighting": "f3alumbrad",
    "potable_water": "f4agua_pot",
    "electrical_installation": "f5electric",
    "sewerage": "f6alcantar",
    "stormwater_collection": "f7pluviale",
    "collector_connection": "f8colector",
}


def _fold(value: Any) -> str:
    text = "" if value is None else str(value).strip().casefold()
    return "".join(
        char for char in unicodedata.normalize("NFKD", text)
        if not unicodedata.combining(char)
    )


def normalize_yes_no(value: Any) -> str:
    folded = _fold(value)
    if folded in {"si", "s", "yes", "true", "1"}:
        return "yes"
    if folded in {"no", "n", "false", "0"}:
        return "no"
    return "not_recorded"


def normalize_pai(value: Any) -> str:
    folded = _fold(value)
    if "adjudicado" in folded and "no" not in folded:
        return "awarded"
    if "no adjudicado" in folded:
        return "not_awarded"
    return "not_recorded"


def normalize_reparcelation(value: Any) -> str:
    folded = _fold(value)
    if "no iniciado" in folded:
        return "not_started"
    if "tramitacion" in folded:
        return "processing"
    if "adjudicado" in folded:
        return "awarded"
    return "not_recorded"


def normalize_service_fields(row: dict[str, Any]) -> dict[str, str]:
    return {
        normalized: normalize_yes_no(row.get(source))
        for normalized, source in SERVICE_FIELDS.items()
    }


def normalize_row(row: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "source_raw": dict(row),
        "normalized": {
            key: row.get(source)
            for key, source in FIELD_MAP.items()
        },
    }
    raw = result["normalized"]
    result["readiness"] = {
        "partial_plan_approved": normalize_yes_no(raw["partial_plan_approved"]),
        "PAI_award": normalize_pai(raw["PAI_awarded"]),
        "reparcelation": normalize_reparcelation(raw["reparcelation_status"]),
        "urbanisation_project": normalize_yes_no(raw["urbanisation_project_exists"]),
        "urbanisation_works": (
            "accepted"
            if raw["urbanisation_works_acceptance_date"]
            else "started"
            if raw["urbanisation_works_start_date"]
            else "not_recorded"
        ),
        "services": normalize_service_fields(row),
    }
    # Presence of an electrical installation is not evidence of spare grid capacity.
    result["readiness"]["grid_capacity"] = "not_assessed"
    return result


def detect_delimiter(sample: str) -> str:
    try:
        return csv.Sniffer().sniff(sample, delimiters=",;\\t|").delimiter
    except csv.Error:
        return ","


def normalize_csv(input_path: Path, output_path: Path) -> int:
    with input_path.open("r", encoding="utf-8-sig", newline="") as source:
        sample = source.read(65536)
        source.seek(0)
        reader = csv.DictReader(source, delimiter=detect_delimiter(sample))
        if not reader.fieldnames:
            raise ValueError("CSV has no header row")
        required = {"municipio", "uso", "sup", "f5electric"}
        present = {name.strip() for name in reader.fieldnames}
        missing = required - present
        if missing:
            raise ValueError(f"CSV is missing expected SU-SUZ fields: {sorted(missing)}")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        count = 0
        with output_path.open("w", encoding="utf-8", newline="") as target:
            for row in reader:
                target.write(json.dumps(normalize_row(row), ensure_ascii=False) + "\n")
                count += 1
    return count


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        raise SystemExit(
            "Usage: normalize_suz_development_readiness.py input.csv output.jsonl"
        )
    count = normalize_csv(Path(argv[1]), Path(argv[2]))
    print(json.dumps({"rows_normalized": count, "output": argv[2]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
