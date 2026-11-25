#!/usr/bin/env python3
"""Download REE transmission substations and circuits as GeoJSON.

Uses the official REE ArcGIS REST query service. This extracts transmission
assets only; it is NOT a complete Spanish distribution-grid dataset.

Coverage is split into mainland/Balearics and Canary Islands envelopes.
Ceuta and Melilla fall inside the mainland envelope. Features are deduplicated
by OBJECTID across envelopes. The source remains authoritative for asset
semantics; this script only transports records and does not infer capacity.

Usage:
  python experiments/ree_transmission_geojson.py --out data/raw/ree

Requires Python 3.10+ and requests.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path
from typing import Any

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE = (
    "https://georedservices.ree.es/arcgis_ags1/rest/services/"
    "WEBREE/Instalaciones_RdT_WEBREE/MapServer"
)
LAYERS = {"substations": 3, "circuits": 11}
PAGE_SIZE = 1500
COUNTRY_FILTER = "PAIS = 'ES'"

# WGS84 envelopes. Separate envelopes avoid pretending the mainland bbox
# covers the Canary Islands. Ceuta and Melilla are inside MAINLAND_BALEARES.
REGIONS = {
    "mainland_balearics_ceuta_melilla": "-10,34,5,45",
    "canary_islands": "-19,27,-12,30",
}


def feature_key(feature: dict[str, Any]) -> str:
    """Stable per-layer deduplication key, with a geometry fallback."""
    properties = feature.get("properties") or {}
    for field in ("OBJECTID", "ObjectId", "objectid", "ID"):
        if properties.get(field) is not None:
            return f"{field}:{properties[field]}"
    canonical = json.dumps(
        feature.get("geometry"), sort_keys=True, separators=(",", ":")
    )
    return "geometry:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def fetch_layer(
    session: requests.Session, layer_id: int
) -> tuple[dict[str, Any], dict[str, int]]:
    url = f"{BASE}/{layer_id}/query"
    seen: dict[str, dict[str, Any]] = {}
    region_counts: dict[str, int] = {}

    for region, bbox in REGIONS.items():
        offset = 0
        region_received = 0
        while True:
            params = {
                "where": COUNTRY_FILTER,
                "geometry": bbox,
                "geometryType": "esriGeometryEnvelope",
                "inSR": 4326,
                "spatialRel": "esriSpatialRelIntersects",
                "outFields": "*",
                "returnGeometry": "true",
                "outSR": 4326,
                "f": "geojson",
                "orderByFields": "OBJECTID ASC",
                "resultOffset": offset,
                "resultRecordCount": PAGE_SIZE,
            }
            response = session.get(url, params=params, timeout=90)
            response.raise_for_status()
            payload = response.json()
            if "error" in payload:
                raise RuntimeError(
                    f"ArcGIS error for layer {layer_id}, region {region}: "
                    f"{payload['error']}"
                )

            batch = payload.get("features", [])
            if not isinstance(batch, list):
                raise RuntimeError(
                    f"Unexpected ArcGIS response for layer {layer_id}: "
                    "features is not a list"
                )

            for feature in batch:
                seen.setdefault(feature_key(feature), feature)
            region_received += len(batch)
            print(
                f"layer={layer_id} region={region} offset={offset} "
                f"received={len(batch)} unique_total={len(seen)}"
            )

            # Continue on a full page even if ArcGIS omits the transfer-limit
            # flag. A final empty page is harmless and avoids silent truncation.
            if not batch or (
                len(batch) < PAGE_SIZE
                and not payload.get("exceededTransferLimit", False)
            ):
                break
            offset += len(batch)
            time.sleep(0.15)

        region_counts[region] = region_received

    return (
        {
            "type": "FeatureCollection",
            "name": f"ree_layer_{layer_id}",
            "features": list(seen.values()),
        },
        region_counts,
    )


def build_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=4,
        connect=4,
        read=4,
        backoff_factor=0.8,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update(
        {"User-Agent": "GridIntelligenceResearch/0.2 (public data research)"}
    )
    return session


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("data/raw/ree"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    manifest = {
        "publisher": "Red Eléctrica de España (REE)",
        "service": BASE,
        "retrieved_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "coverage": {
            "country_filter": COUNTRY_FILTER,
            "crs": "EPSG:4326",
            "regions": REGIONS,
            "note": (
                "Separate mainland/Balearics/Ceuta/Melilla and Canary "
                "envelopes; envelope coverage is not a legal asset boundary."
            ),
        },
        "reuse_terms_status": "unknown",
        "commercial_use_not_cleared": True,
        "limitations": [
            "Transmission assets only; distribution networks are not included.",
            "Published transport ratings in MVA are not available connection "
            "capacity in MW.",
            "No capacity aggregation or engineering inference is performed.",
            "Source reuse/licensing terms must be checked before redistribution.",
        ],
        "layers": {},
    }

    with build_session() as session:
        for name, layer_id in LAYERS.items():
            collection, region_counts = fetch_layer(session, layer_id)
            path = args.out / f"{name}.geojson"
            path.write_text(
                json.dumps(collection, ensure_ascii=False), encoding="utf-8"
            )
            manifest["layers"][name] = {
                "layer_id": layer_id,
                "unique_feature_count": len(collection["features"]),
                "received_by_region": region_counts,
                "file": path.name,
            }

    (args.out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
