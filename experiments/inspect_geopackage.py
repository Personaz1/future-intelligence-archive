#!/usr/bin/env python3
"""Inspect GeoPackage structure without requiring GDAL/QGIS.

Reports feature tables, geometry types, SRS IDs, feature counts, extents and
attribute columns. It does not validate geometry topology or legal meaning.

Usage:
  python experiments/inspect_geopackage.py file.gpkg
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
import sys
from pathlib import Path
from typing import Any


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def table_exists(connection: sqlite3.Connection, table_name: str) -> bool:
    row = connection.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,),
    ).fetchone()
    return row is not None


def inspect_geopackage(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(path)

    with path.open("rb") as stream:
        if stream.read(16) != b"SQLite format 3\x00":
            raise ValueError(f"{path} is not a SQLite/GeoPackage file")

    connection = sqlite3.connect(f"file:{path.resolve()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        required = ("gpkg_contents", "gpkg_geometry_columns", "gpkg_spatial_ref_sys")
        missing = [name for name in required if not table_exists(connection, name)]
        if missing:
            raise ValueError(f"Missing GeoPackage metadata tables: {missing}")

        contents = connection.execute(
            "SELECT table_name, data_type, identifier, srs_id, "
            "min_x, min_y, max_x, max_y FROM gpkg_contents ORDER BY table_name"
        ).fetchall()
        geometries = {
            row["table_name"]: dict(row)
            for row in connection.execute(
                "SELECT table_name, column_name, geometry_type_name, "
                "srs_id, z, m FROM gpkg_geometry_columns"
            ).fetchall()
        }
        spatial_refs = {
            row["srs_id"]: {
                "organization": row["organization"],
                "organization_coordsys_id": row["organization_coordsys_id"],
                "definition": row["definition"],
                "description": row["description"],
            }
            for row in connection.execute(
                "SELECT srs_id, organization, organization_coordsys_id, "
                "definition, description FROM gpkg_spatial_ref_sys"
            ).fetchall()
        }

        layers = []
        for item in contents:
            name = item["table_name"]
            columns = [
                row["name"]
                for row in connection.execute(f'PRAGMA table_info("{name}")')
            ]
            geometry = geometries.get(name)
            count = None
            if item["data_type"] == "features":
                count = connection.execute(
                    f'SELECT COUNT(*) FROM "{name}"'
                ).fetchone()[0]
            srs_id = (
                geometry["srs_id"]
                if geometry is not None
                else item["srs_id"]
            )
            layers.append(
                {
                    "table_name": name,
                    "data_type": item["data_type"],
                    "identifier": item["identifier"],
                    "feature_count": count,
                    "geometry": geometry,
                    "srs_id": srs_id,
                    "spatial_reference": spatial_refs.get(srs_id),
                    "extent": {
                        "min_x": item["min_x"],
                        "min_y": item["min_y"],
                        "max_x": item["max_x"],
                        "max_y": item["max_y"],
                    },
                    "columns": columns,
                }
            )

        return {
            "file": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "layers": layers,
            "limitations": [
                "Metadata inspection does not validate geometry topology or coordinate values.",
                "SRS IDs must be interpreted from the embedded spatial reference metadata.",
                "A feature count and extent do not establish completeness or legal authority.",
            ],
        }
    finally:
        connection.close()


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        raise SystemExit("Usage: inspect_geopackage.py file.gpkg")
    result = inspect_geopackage(Path(argv[1]))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
