"""Offline tests for the Generalitat Valenciana land-layer fetcher."""
import unittest

from experiments.fetch_gva_land_layers import SOURCES, sha256_file


class GVALandLayerTests(unittest.TestCase):
    def test_both_sources_have_explicit_cc_by_metadata(self):
        self.assertEqual(set(SOURCES), {"su_suz", "coscv_2025"})
        for source in SOURCES.values():
            self.assertIn("CC BY", source["license"])

    def test_su_suz_is_the_published_inventory_layer(self):
        source = SOURCES["su_suz"]
        self.assertIn("InventarioSuSuz", source["url"])
        self.assertIn("gpkg", source["url"])
        self.assertTrue(any("informative" in item for item in source["limitations"]))

    def test_coscv_2025_is_not_mislabelled_as_legal_zoning(self):
        source = SOURCES["coscv_2025"]
        self.assertIn("2025COSCV", source["url"])
        self.assertTrue(any("not a legal zoning" in item for item in source["limitations"]))

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
