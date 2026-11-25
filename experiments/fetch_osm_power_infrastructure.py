#!/usr/bin/env python3
"""Acquire an OpenStreetMap power-infrastructure snapshot for a pilot area.

OSM data is licensed under ODbL 1.0. Commercial use is possible, but a
distributed derivative database must comply with ODbL share-alike obligations.
This is volunteered mapping, not an authoritative network register.

Example (Alicante province-scale pilot envelope):
  python experiments/fetch_osm_power_infrastructure.py --out data/raw/osm \
      --bbox 37.3,-1.5,39.0,0.3

Requires Python 3.10+ and requests.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from collections import Counter
from pathlib import Path
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

DEFAULT_ENDPOINT = "https://overpass-api.de/api/interpreter"
DEFAULT_BBOX = (37.3, -1.5, 39.0, 0.3)
POWER_VALUES = (
    "substation|transformer|plant|line|minor_line|cable|"
    "tower|pole|switch|generator|connection"
)


def parse_bbox(value: str) -> tuple[float, float, float, float]:
    parts = tuple(float(part.strip()) for part in value.split(","))
    if len(parts) != 4:
        raise ValueError("bbox must be south,west,north,east")
    south, west, north, east = parts
    if not (-90 <= south < north <= 90 and -180 <= west < east <= 180):
        raise ValueError("bbox coordinates are invalid or reversed")
    return south, west, north, east


def build_query(bbox: tuple[float, float, float, float]) -> str:
    south, west, north, east = bbox
    return (
        "[out:json][timeout:180];("
        f'nwr["power"~"^({POWER_VALUES})"]'
        f"({south},{west},{north},{east});"
        ");out geom;"
    )


def build_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=3,
        connect=3,
        read=3,
        backoff_factor=2,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET", "POST"}),
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update(
        {"User-Agent": "GridIntelligenceResearch/0.1 (OSM public data research)"}
    )
    return session


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("data/raw/osm"))
    parser.add_argument(
        "--bbox",
        default=",".join(str(value) for value in DEFAULT_BBOX),
        help="south,west,north,east in WGS84",
    )
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    args = parser.parse_args()

    bbox = parse_bbox(args.bbox)
    query = build_query(bbox)
    args.out.mkdir(parents=True, exist_ok=True)

    with build_session() as session:
        response = session.post(
            args.endpoint,
            data={"data": query},
            timeout=240,
        )
        response.raise_for_status()
        payload: dict[str, Any] = response.json()

    elements = payload.get("elements")
    if not isinstance(elements, list):
        raise RuntimeError("Overpass response has no elements array")

    counts_by_type = Counter(str(element.get("type", "unknown")) for element in elements)
    counts_by_power = Counter(
        str((element.get("tags") or {}).get("power", "untagged"))
        for element in elements
    )

    data_path = args.out / "power-infrastructure-overpass.json"
    raw_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    data_path.write_bytes(raw_bytes)

    manifest = {
        "publisher": "OpenStreetMap contributors",
        "source_endpoint": args.endpoint,
        "retrieved_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "bbox_wgs84_south_west_north_east": bbox,
        "query": query,
        "element_count": len(elements),
        "counts_by_osm_element_type": dict(counts_by_type),
        "counts_by_power_tag": dict(counts_by_power),
        "file": data_path.name,
        "bytes": len(raw_bytes),
        "sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "licence": "Open Database Licence (ODbL) 1.0",
        "attribution": "© OpenStreetMap contributors",
        "reuse_terms_status": "permitted_with_odbl_share_alike",
        "commercial_use_not_cleared": False,
        "limitations": [
            "OSM is volunteered geographic information, not an official operator register.",
            "Completeness, voltage tagging, geometry and positional accuracy vary by area.",
            "Do not infer available connection capacity or electrical connectivity from proximity.",
            "Distributed derivative databases must comply with ODbL 1.0 share-alike terms.",
        ],
    }
    (args.out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
