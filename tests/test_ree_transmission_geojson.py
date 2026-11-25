"""Offline tests for the REE transmission extractor."""
import unittest

from experiments.ree_transmission_geojson import REGIONS, feature_key


class ExtractorTests(unittest.TestCase):
    def test_national_regions_include_canaries_and_ceuta_melilla(self):
        self.assertIn("canary_islands", REGIONS)
        self.assertIn("ceuta_melilla", next(iter(REGIONS)))

    def test_objectid_is_preferred_for_deduplication(self):
        feature = {"properties": {"OBJECTID": 42, "ID": 7}, "geometry": None}
        self.assertEqual(feature_key(feature), "OBJECTID:42")

    def test_geometry_fallback_is_stable(self):
        feature = {"properties": {}, "geometry": {"type": "Point", "coordinates": [1, 2]}}
        self.assertEqual(feature_key(feature), feature_key(feature))


if __name__ == "__main__":
    unittest.main()
