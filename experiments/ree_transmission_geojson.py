#!/usr/bin/env python3
"""Download public REE transmission substations and circuits as GeoJSON.

Uses the official REE ArcGIS REST query service. This extracts transmission
assets only; it is NOT a complete Spanish distribution-grid dataset.

Usage:
  python experiments/ree_transmission_geojson.py --out data/raw/ree

Requires Python 3.10+ and requests.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any

import requests

BASE = (
    "https://georedservices.ree.es/arcgis_ags1/rest/services/"
    "WEBREE/Instalaciones_RdT_WEBREE/MapServer"
)
LAYERS = {"substations": 3, "circuits": 11}
# Broad Iberian/Spanish envelope in WGS84; includes Balearics and Canaries only
# partially, so this first utility is a mainland/nearby pilot, not national coverage.
BBOX = "-10,34,5,45"


def fetch_layer(session: requests.Session, layer_id: int) -> dict[str, Any]:
    url = f"{BASE}/{layer_id}/query"
    offset = 0
    features: list[dict[str, Any]] = []
    while True:
        params = {
            "where": "1=1",
            "geometry": BBOX,
            "geometryType": "esriGeometryEnvelope",
            "inSR": 4326,
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": "*",
            "returnGeometry": "true",
            "outSR": 4326,
            "f": "geojson",
            "resultOffset": offset,
            "resultRecordCount": 1500,
        }
        response = session.get(url, params=params, timeout=90)
        response.raise_for_status()
        payload = response.json()
        if "error" in payload:
            raise RuntimeError(f"ArcGIS error for layer {layer_id}: {payload['error']}")
        batch = payload.get("features", [])
        features.extend(batch)
        print(f"layer={layer_id} offset={offset} received={len(batch)} total={len(features)}")
        if not payload.get("exceededTransferLimit") and len(batch) < 1500:
            break
        if not batch:
            break
        offset += len(batch)
        time.sleep(0.15)
    return {
        "type": "FeatureCollection",
        "name": f"ree_layer_{layer_id}",
        "features": features,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("data/raw/ree"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "GridIntelligenceResearch/0.1 (public data research)"})

    manifest = {
        "publisher": "Red Eléctrica de España (REE)",
        "service": BASE,
        "retrieved_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "coverage_note": "BBOX -10,34,5,45; mainland/nearby pilot, not full Spain",
        "layers": {},
    }
    for name, layer_id in LAYERS.items():
        collection = fetch_layer(session, layer_id)
        path = args.out / f"{name}.geojson"
        path.write_text(json.dumps(collection, ensure_ascii=False), encoding="utf-8")
        manifest["layers"][name] = {
            "layer_id": layer_id,
            "feature_count": len(collection["features"]),
            "file": path.name,
        }

    (args.out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
