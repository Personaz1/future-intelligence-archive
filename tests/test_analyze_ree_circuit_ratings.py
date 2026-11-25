"""Offline tests for REE circuit rating analysis."""
import unittest

from experiments.analyze_ree_circuit_ratings import summarize


class CircuitRatingAnalysisTests(unittest.TestCase):
    def test_statistics_preserve_mva_semantics_and_do_not_sum(self):
        features = [
            {"properties": {"TENSION": "220", "ESTADO": "S", "PAIS": "ES",
                            "CAP_ENE": 100, "ELEM_LIM_ENE": "C"}},
            {"properties": {"TENSION": "220", "ESTADO": "S", "PAIS": "ES",
                            "CAP_ENE": 200, "ELEM_LIM_ENE": "C"}},
            {"properties": {"TENSION": "220", "ESTADO": "S", "PAIS": "ES",
                            "CAP_ENE": 0, "ELEM_LIM_ENE": "Cab"}},
            {"properties": {"TENSION": "220", "ESTADO": "S", "PAIS": "ES",
                            "CAP_ENE": None}},
        ]
        result = summarize(features)
        self.assertEqual(result["unit"], "MVA")
        self.assertIn("No sum is calculated", result["aggregation_policy"])
        group = result["groups"][0]
        january = group["monthly"]["January"]
        self.assertEqual(january["valid_values"], 3)
        self.assertEqual(january["missing_or_invalid"], 1)
        self.assertEqual(january["zero_values"], 1)
        self.assertEqual(january["median"], 100)
        self.assertEqual(january["limiting_elements"]["C"], 2)

    def test_empty_input_is_valid(self):
        result = summarize([])
        self.assertEqual(result["feature_count"], 0)
        self.assertEqual(result["groups"], [])


if __name__ == "__main__":
    unittest.main()
