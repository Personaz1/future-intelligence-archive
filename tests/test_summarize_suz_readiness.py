"""Tests for the descriptive SU-SUZ readiness summary."""
import unittest

from experiments.summarize_suz_readiness import province_code, summarize


class SUZSummaryTests(unittest.TestCase):
    def test_province_code_accepts_zero_padded_and_numeric_codes(self):
        self.assertEqual(province_code("03065"), "03")
        self.assertEqual(province_code(3065), "03")
        self.assertEqual(province_code(None), "")

    def test_summary_filters_alicante_and_never_claims_grid_capacity(self):
        records = [
            {
                "normalized": {"municipality_ine_code": "03065", "global_land_use": "industrial"},
                "readiness": {
                    "partial_plan_approved": "yes", "PAI_award": "awarded",
                    "reparcelation": "processing", "urbanisation_works": "started",
                    "grid_capacity": "not_assessed",
                    "services": {"electrical_installation": "yes", "potable_water": "no"},
                },
            },
            {
                "normalized": {"municipality_ine_code": "46001", "global_land_use": "industrial"},
                "readiness": {"grid_capacity": "not_assessed", "services": {}},
            },
            {
                "normalized": {"municipality_ine_code": "03014", "global_land_use": "residential"},
                "readiness": {"grid_capacity": "not_assessed", "services": {}},
            },
        ]
        result = summarize(records)
        self.assertEqual(result["scope"]["province_record_count"], 2)
        self.assertEqual(result["scope"]["industrial_record_count"], 1)
        self.assertEqual(
            result["industrial_sector_distributions"]["grid_capacity"],
            {"not_assessed": 1},
        )
        self.assertEqual(
            result["industrial_service_distributions"]["electrical_installation"],
            {"yes": 1},
        )
        self.assertTrue(any("not grid-access capacity" in note for note in result["interpretation_limits"]))


if __name__ == "__main__":
    unittest.main()
