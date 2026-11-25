"""Offline tests for REE access-capacity snapshot acquisition."""
import unittest

from experiments.fetch_ree_access_capacity import SOURCES, inspect_csv


class REEAccessCapacityFetcherTests(unittest.TestCase):
    def test_demand_and_generation_are_distinct(self):
        self.assertEqual(SOURCES["demand"][1], "demand")
        self.assertEqual(SOURCES["generation"][1], "generation")
        self.assertIn("2026_11_03_GRT_demanda.csv", SOURCES["demand"][0])
        self.assertIn("2026_11_03_GRT_generacion.csv", SOURCES["generation"][0])

    def test_csv_header_and_rows(self):
        result = inspect_csv(b"node;voltage;available_mw\nX;220;50\n")
        self.assertEqual(result["header"], ["node", "voltage", "available_mw"])
        self.assertEqual(result["data_row_count"], 1)


if __name__ == "__main__":
    unittest.main()
