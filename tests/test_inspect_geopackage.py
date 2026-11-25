"""Tests for the dependency-free GeoPackage inspector."""
import sqlite3
import tempfile
import unittest
from pathlib import Path

from experiments.inspect_geopackage import inspect_geopackage


class GeoPackageInspectorTests(unittest.TestCase):
    def _make_gpkg(self, path):
        connection = sqlite3.connect(path)
        connection.executescript(
            """
            CREATE TABLE gpkg_contents (
                table_name TEXT, data_type TEXT, identifier TEXT, srs_id INTEGER,
                min_x REAL, min_y REAL, max_x REAL, max_y REAL
            );
            CREATE TABLE gpkg_geometry_columns (
                table_name TEXT, column_name TEXT, geometry_type_name TEXT,
                srs_id INTEGER, z INTEGER, m INTEGER
            );
            CREATE TABLE gpkg_spatial_ref_sys (
                srs_id INTEGER, organization TEXT, organization_coordsys_id INTEGER,
                definition TEXT, description TEXT
            );
            CREATE TABLE sectors (fid INTEGER PRIMARY KEY, geom BLOB, municipio TEXT);
            INSERT INTO gpkg_contents VALUES
                ('sectors', 'features', 'SU-SUZ sectors', 25830, 600000, 4200000, 601000, 4201000);
            INSERT INTO gpkg_geometry_columns VALUES
                ('sectors', 'geom', 'MULTIPOLYGON', 25830, 0, 0);
            INSERT INTO gpkg_spatial_ref_sys VALUES
                (25830, 'EPSG', 25830, 'ETRS89 / UTM zone 30N', 'test CRS');
            INSERT INTO sectors (municipio) VALUES ('Elche');
            """
        )
        connection.commit()
        connection.close()

    def test_inspects_feature_count_crs_extent_and_columns(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.gpkg"
            self._make_gpkg(path)
            result = inspect_geopackage(path)
            layer = result["layers"][0]
            self.assertEqual(layer["feature_count"], 1)
            self.assertEqual(layer["srs_id"], 25830)
            self.assertEqual(layer["geometry"]["geometry_type_name"], "MULTIPOLYGON")
            self.assertIn("municipio", layer["columns"])
            self.assertEqual(layer["extent"]["min_x"], 600000)

    def test_rejects_non_geopackage_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "not.gpkg"
            path.write_text("not a geopackage", encoding="utf-8")
            with self.assertRaises(ValueError):
                inspect_geopackage(path)


if __name__ == "__main__":
    unittest.main()
