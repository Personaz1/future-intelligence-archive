"""Offline tests for the OSM power-infrastructure fetcher."""
import unittest

from experiments.fetch_osm_power_infrastructure import build_query, parse_bbox


class OSMFetcherTests(unittest.TestCase):
    def test_bbox_parsing(self):
        self.assertEqual(parse_bbox("37.3,-1.5,39.0,0.3"), (37.3, -1.5, 39.0, 0.3))

    def test_bbox_rejects_reversed_coordinates(self):
        with self.assertRaises(ValueError):
            parse_bbox("39.0,-1.5,37.3,0.3")

    def test_query_requests_power_features_and_geometry(self):
        query = build_query((37.3, -1.5, 39.0, 0.3))
        self.assertIn('nwr["power"', query)
        self.assertIn("out geom", query)
        self.assertIn("37.3,-1.5,39.0,0.3", query)


if __name__ == "__main__":
    unittest.main()
