#!/usr/bin/env python3
"""Download two CC BY land/planning layers from Institut Cartogràfic Valencià.

Sources:
- SU-SUZ urban/developable land inventory (GeoPackage via WFS)
- COSCV 2025 land-cover cartography (complete GeoPackage ZIP)

These are Valencian regional datasets, not nationwide Spain coverage.
SU-SUZ is explicitly informational; authoritative planning instruments prevail.
Requires Python 3.10+ and requests.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

SOURCES = {
    "dic": {
        "url": (
            "https://terramapas.icv.gva.es/0702_Planeamiento"
            "?outputformat=gpkg&request=GetFeature&service=WFS"
            "&typename=DeclaracionInteresComunitario&version=2.0.0"
        ),
        "filename": "gva_declaraciones_interes_comunitario.gpkg",
        "dataset": "Declaraciones de Interés Comunitario de la Comunitat Valenciana",
        "license": "Creative Commons Attribution (CC BY)",
        "update_note": "Catalogue says update frequency depends on source records",
        "limitations": [
            "Features represent non-urban parcels with a recorded declaration of community interest.",
            "The publisher states that the layer is informative and derives from administrative case files.",
            "A DIC record is not a blanket permission for a new energy project; verify the specific declaration, conditions and municipal licence.",
        ],
    },
    "su_suz": {
        "url": (
            "https://terramapas.icv.gva.es/0702_Planeamiento"
            "?outputformat=gpkg&request=GetFeature&service=WFS"
            "&typename=InventarioSuSuz&version=2.0.0"
        ),
        "filename": "gva_su_suz_inventory.gpkg",
        "signature": b"SQLite format 3\x00",
        "dataset": "Inventario de suelo urbano y urbanizable (SU-SUZ)",
        "license": "Creative Commons Attribution (CC BY)",
        "update_note": "Portal reports bianual update frequency",
        "limitations": [
            "The publisher states that the information is informative.",
            "The inventory describes urban land under development and developable sectors, not all parcels.",
            "Use the authoritative planning instrument and competent authority for legally valid status.",
        ],
    },
    "zoning": {
        "url": (
            "https://terramapas.icv.gva.es/0702_Planeamiento"
            "?outputformat=gpkg&request=GetFeature&service=WFS"
            "&typename=Planeamiento.Zonificacion&version=2.0.0"
        ),
        "filename": "gva_planning_zoning.gpkg",
        "signature": b"SQLite format 3\x00",
        "dataset": "Planeamiento Urbanístico de la Comunitat Valenciana: Zonificación urbanística",
        "license": "Creative Commons Attribution (CC BY)",
        "update_note": "Portal reports bianual update frequency",
        "limitations": [
            "The publisher states that the published planning layer is informative.",
            "For legally valid zoning status, consult the actual planning instruments and competent authority.",
            "Coverage is regional: Comunitat Valenciana.",
        ],
    },
    "coscv_2025": {
        "url": (
            "https://descargas.icv.gva.es/dcd/04_cubierta_usosuelo/COSCV/"
            "04_2025COSCV_25830_GPKG.zip"
            "?formato=CV%28GPKG%29&tipo=directa"
        ),
        "filename": "gva_coscv_2025_25830_gpkg.zip",
        "signature": b"PK\x03\x04",
        "dataset": "Cartografía de Ocupación del Suelo de la Comunitat Valenciana (COSCV), edition 2025",
        "license": "Creative Commons Attribution (CC BY)",
        "update_note": "2025 historical edition; catalogue marks frequency as historical data",
        "limitations": [
            "Regional coverage only: Comunitat Valenciana.",
            "The 2025 edition integrates ICV 1:5,000 topographic cartography, SIGPAC2025 in agricultural areas and PATFOR data dated 2025 in forest areas.",
            "Land cover is not a legal zoning or planning determination.",
        ],
    },
}


def build_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=4,
        connect=4,
        read=4,
        backoff_factor=2,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update(
        {"User-Agent": "GridIntelligenceResearch/0.1 (ICV public data acquisition)"}
    )
    return session


def validate_file_signature(path: Path, expected: bytes) -> None:
    with path.open("rb") as stream:
        actual = stream.read(len(expected))
    if actual != expected:
        path.unlink(missing_ok=True)
        raise RuntimeError(
            f"Unexpected file signature for {path.name}; download may be an HTML error page"
        )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("data/raw/gva"))
    parser.add_argument(
        "--sources",
        nargs="+",
        choices=tuple(SOURCES),
        default=list(SOURCES),
        help="Select one or more source IDs",
    )
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    manifest = {
        "publisher": "Institut Cartogràfic Valencià, Generalitat Valenciana",
        "retrieved_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "records": [],
    }

    with build_session() as session:
        for source_id in args.sources:
            source = SOURCES[source_id]
            response = session.get(source["url"], timeout=(30, 300), stream=True)
            response.raise_for_status()
            path = args.out / source["filename"]
            digest = hashlib.sha256()
            byte_count = 0
            with path.open("wb") as output:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        output.write(chunk)
                        digest.update(chunk)
                        byte_count += len(chunk)
            validate_file_signature(path, source["signature"])
            record = {
                "source_id": source_id,
                "dataset": source["dataset"],
                "source_url": source["url"],
                "file": path.name,
                "bytes": byte_count,
                "sha256": digest.hexdigest(),
                "content_type": response.headers.get("Content-Type"),
                "license": source["license"],
                "commercial_use_not_cleared": False,
                "reuse_terms_status": "permitted_with_cc_by_attribution",
                "update_note": source["update_note"],
                "limitations": source["limitations"],
            }
            manifest["records"].append(record)

    (args.out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
