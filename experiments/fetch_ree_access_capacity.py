#!/usr/bin/env python3
"""Acquire REE monthly transmission access-capacity CSV snapshots.

Demand and generation are separate official datasets. Preserve source bytes;
do not infer totals by summing nodes or collapse storage treatment across
regulatory directions.

Example:
  python experiments/fetch_ree_access_capacity.py --out data/raw/ree-capacity

Requires Python 3.10+; standard library only.
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

PUBLICATION_DATE = "2026-11-03"
BASE = "https://www.ree.es/sites/default/files/12_CLIENTES/Documentos"
SOURCES = {
    "demand": (
        f"{BASE}/{PUBLICATION_DATE}_GRT_demanda.csv",
        "demand",
        "transmission",
    ),
    "generation": (
        f"{BASE}/{PUBLICATION_DATE}_GRT_generacion.csv",
        "generation",
        "transmission",
    ),
}


def inspect_csv(data: bytes) -> dict[str, Any]:
    text = data.decode("utf-8-sig", errors="replace")
    sample = text[:8192]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
        delimiter = dialect.delimiter
    except csv.Error:
        delimiter = ";" if sample.count(";") > sample.count(",") else ","
    rows = csv.reader(io.StringIO(text), delimiter=delimiter)
    header = next(rows, [])
    return {
        "encoding": "utf-8-sig (replacement decoding used for inspection)",
        "delimiter": delimiter,
        "header": header,
        "data_row_count": sum(1 for _ in rows),
    }


def download(url: str) -> bytes:
    request = urllib.request.Request(
        url, headers={"User-Agent": "GridIntelligenceResearch/0.1 (public data research)"}
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status} for {url}")
        return response.read()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("data/raw/ree-capacity"))
    parser.add_argument("--source", choices=["all", *SOURCES], default="all")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    selected = SOURCES if args.source == "all" else {args.source: SOURCES[args.source]}
    manifest: dict[str, Any] = {
        "publisher": "Red Eléctrica de España (REE)",
        "network_scope": "transmission",
        "publication_date": PUBLICATION_DATE,
        "retrieved_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "preservation_policy": "Original bytes are retained unchanged; commercial reuse is not cleared by this script.",
        "reuse_terms_status": "unknown",
        "commercial_use_not_cleared": True,
        "sources": {},
        "interpretation_warnings": [
            "Demand and generation publications are distinct and must remain separate.",
            "Node values are interdependent and must not be summed as national capacity.",
            "Published values are informative; project-specific studies prevail.",
            "Storage is represented according to the source publication and regulatory mode.",
        ],
    }

    for key, (url, direction, scope) in selected.items():
        data = download(url)
        filename = url.rsplit("/", 1)[-1]
        path = args.out / filename
        path.write_bytes(data)
        manifest["sources"][key] = {
            "url": url,
            "direction": direction,
            "network_scope": scope,
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
