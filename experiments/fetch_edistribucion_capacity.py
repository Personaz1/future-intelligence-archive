#!/usr/bin/env python3
"""Acquire official e-distribución monthly access-capacity CSV snapshots.

The source CSVs are preserved byte-for-byte. This tool does not normalize
operator-specific columns or combine demand and generation capacity.

Example:
  python experiments/fetch_edistribucion_capacity.py --out data/raw/edistribucion

Requires Python 3.10+; uses only the standard library.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import time
import urllib.request
from pathlib import Path
from typing import Any

MONTH = "202611"
PUBLICATION_DATE = "2026-11-04"
BASE = (
    "https://www.edistribucion.com/content/dam/edistribucion/"
    "conexion-a-la-red/descargables/nodos"
)

SOURCES = {
    "demand_edistribucion": (
        f"{BASE}/demanda/{MONTH}/{PUBLICATION_DATE}_R1299_demanda.csv",
        "demand",
        "e-distribucion",
    ),
    "generation_edistribucion": (
        f"{BASE}/generacion/{MONTH}/{PUBLICATION_DATE}_R1299_generaci%C3%B3n.csv",
        "generation",
        "e-distribucion",
    ),
}


def inspect_csv(data: bytes) -> dict[str, Any]:
    """Best-effort structural inspection; never rewrites source bytes."""
    text = data.decode("utf-8-sig", errors="replace")
    sample = text[:8192]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
        delimiter = dialect.delimiter
    except csv.Error:
        delimiter = ";" if sample.count(";") > sample.count(",") else ","

    rows = csv.reader(io.StringIO(text), delimiter=delimiter)
    header = next(rows, [])
    row_count = sum(1 for _ in rows)
    return {
        "encoding": "utf-8-sig (replacement decoding used for inspection)",
        "delimiter": delimiter,
        "header": header,
        "data_row_count": row_count,
    }


def download(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "GridIntelligenceResearch/0.1 (public data research)"},
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status} for {url}")
        return response.read()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("data/raw/edistribucion"))
    parser.add_argument(
        "--source",
        choices=["all", *SOURCES.keys()],
        default="all",
        help="Download one source or both demand and generation.",
    )
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    selected = SOURCES if args.source == "all" else {args.source: SOURCES[args.source]}
    manifest: dict[str, Any] = {
        "publisher": "e-distribución Redes Digitales, S.L.U.",
        "publication_month": MONTH,
        "publication_date_in_filename": PUBLICATION_DATE,
        "retrieved_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "preservation_policy": "Original bytes are retained unchanged; do not redistribute without rights-holder authorization.",
        "reuse_terms_status": "restricted",
        "commercial_use_not_cleared": True,
        "sources": {},
    }

    for key, (url, capacity_type, operator) in selected.items():
        data = download(url)
        filename = url.rsplit("/", 1)[-1]
        path = args.out / filename
        path.write_bytes(data)
        manifest["sources"][key] = {
            "url": url,
            "operator": operator,
            "capacity_type": capacity_type,
            "file": filename,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "inspection": inspect_csv(data),
        }
        print(
            f"{key}: bytes={len(data)} "
            f"sha256={manifest['sources'][key]['sha256']}"
        )

    (args.out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
