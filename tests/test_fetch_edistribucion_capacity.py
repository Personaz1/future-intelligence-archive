"""Offline tests for the e-distribución snapshot fetcher."""
import unittest

from experiments.fetch_edistribucion_capacity import SOURCES, inspect_csv


class CapacityFetcherTests(unittest.TestCase):
    def test_sources_keep_demand_and_generation_separate(self):
        self.assertEqual(SOURCES["demand_edistribucion"][1], "demand")
        self.assertEqual(SOURCES["generation_edistribucion"][1], "generation")
        self.assertNotEqual(
            SOURCES["demand_edistribucion"][0],
            SOURCES["generation_edistribucion"][0],
        )

    def test_semicolon_csv_is_inspected_without_normalizing_it(self):
        result = inspect_csv("node;voltage;available_mw\nA;66;12.5\n".encode())
        self.assertEqual(result["delimiter"], ";")
        self.assertEqual(result["header"], ["node", "voltage", "available_mw"])
        self.assertEqual(result["data_row_count"], 1)

    def test_comma_csv_is_inspected(self):
        result = inspect_csv(b"node,mw\nA,3\nB,4\n")
        self.assertEqual(result["delimiter"], ",")
        self.assertEqual(result["data_row_count"], 2)


if __name__ == "__main__":
    unittest.main()
