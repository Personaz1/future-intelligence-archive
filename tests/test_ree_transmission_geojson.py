"""Offline tests for the REE transmission extractor."""
import unittest

from experiments.ree_transmission_geojson import COUNTRY_FILTER, REGIONS, feature_key


class ExtractorTests(unittest.TestCase):
    def test_region_envelopes_cover_mainland_and_canaries(self):
        mainland = [float(value) for value in REGIONS["mainland_balearics_ceuta_melilla"].split(",")]
        canaries = [float(value) for value in REGIONS["canary_islands"].split(",")]
        self.assertLessEqual(mainland[0], -9.5)
        self.assertGreaterEqual(mainland[2], 4.5)
        self.assertLessEqual(mainland[1], 34.5)
        self.assertGreaterEqual(mainland[3], 44.5)
        self.assertLessEqual(canaries[0], -18.0)
        self.assertGreaterEqual(canaries[2], -13.0)
        self.assertLessEqual(canaries[1], 27.5)
        self.assertGreaterEqual(canaries[3], 29.5)

    def test_extractor_filters_to_spanish_records(self):
        self.assertEqual(COUNTRY_FILTER, "PAIS = 'ES'")

    def test_objectid_is_preferred_for_deduplication(self):
        feature = {"properties": {"OBJECTID": 42, "ID": 7}, "geometry": None}
        self.assertEqual(feature_key(feature), "OBJECTID:42")

    def test_geometry_fallback_is_stable(self):
        feature = {"properties": {}, "geometry": {"type": "Point", "coordinates": [1, 2]}}
        self.assertEqual(feature_key(feature), feature_key(feature))


if __name__ == "__main__":
    unittest.main()
