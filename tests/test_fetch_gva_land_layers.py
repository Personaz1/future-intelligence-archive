"""Offline tests for the Generalitat Valenciana land-layer fetcher."""
import unittest

from experiments.fetch_gva_land_layers import SOURCES, sha256_file, validate_file_signature


class GVALandLayerTests(unittest.TestCase):
    def test_both_sources_have_explicit_cc_by_metadata(self):
        self.assertEqual(set(SOURCES), {"su_suz", "coscv_2025", "zoning"})
        for source in SOURCES.values():
            self.assertIn("CC BY", source["license"])

    def test_su_suz_is_the_published_inventory_layer(self):
        source = SOURCES["su_suz"]
        self.assertIn("InventarioSuSuz", source["url"])
        self.assertIn("gpkg", source["url"])
        self.assertTrue(any("informative" in item for item in source["limitations"]))

    def test_zoning_is_informational_and_cc_by(self):
        source = SOURCES["zoning"]
        self.assertIn("Planeamiento.Zonificacion", source["url"])
        self.assertIn("CC BY", source["license"])
        self.assertTrue(any("informative" in item for item in source["limitations"]))

    def test_coscv_2025_is_not_mislabelled_as_legal_zoning(self):
        source = SOURCES["coscv_2025"]
        self.assertIn("2025COSCV", source["url"])
        self.assertTrue(any("not a legal zoning" in item for item in source["limitations"]))

    def test_download_file_signatures(self):
        self.assertEqual(SOURCES["su_suz"]["signature"], b"SQLite format 3\x00")
        self.assertEqual(SOURCES["zoning"]["signature"], b"SQLite format 3\x00")
        self.assertEqual(SOURCES["coscv_2025"]["signature"], b"PK\x03\x04")

    def test_invalid_signature_deletes_bad_download(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.gpkg"
            path.write_bytes(b"<html>error</html>")
            with self.assertRaises(RuntimeError):
                validate_file_signature(path, b"SQLite format 3\x00")
            self.assertFalse(path.exists())

    def test_sha256_file(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.bin"
            path.write_bytes(b"abc")
            self.assertEqual(
                sha256_file(path),
                "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
            )


if __name__ == "__main__":
    unittest.main()
