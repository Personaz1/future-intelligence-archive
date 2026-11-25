"""Tests for the SU-SUZ development-readiness normalizer."""
import json
import tempfile
import unittest
from pathlib import Path

from experiments.normalize_suz_development_readiness import (
    normalize_pai,
    normalize_reparcelation,
    normalize_row,
    normalize_yes_no,
    normalize_csv,
)


class SUZReadinessTests(unittest.TestCase):
    def test_yes_no_normalization_handles_spanish_accents(self):
        self.assertEqual(normalize_yes_no("Sí"), "yes")
        self.assertEqual(normalize_yes_no("NO"), "no")
        self.assertEqual(normalize_yes_no(""), "not_recorded")

    def test_pai_states_are_not_collapsed(self):
        self.assertEqual(normalize_pai("Adjudicado"), "awarded")
        self.assertEqual(normalize_pai("No adjudicado"), "not_awarded")
        self.assertEqual(normalize_pai(None), "not_recorded")

    def test_reparcelation_states_are_distinct(self):
        self.assertEqual(normalize_reparcelation("No iniciado"), "not_started")
        self.assertEqual(normalize_reparcelation("En tramitación"), "processing")
        self.assertEqual(normalize_reparcelation("Adjudicado"), "awarded")

    def test_electrical_installation_does_not_infer_grid_capacity(self):
        row = {
            "municipio": "Elche",
            "cpm": "03065",
            "uso": "industrial",
            "sup": "120000",
            "edif_total": "60000",
            "ord_porm": "Sí",
            "pai": "Adjudicado",
            "Pr_repc": "En tramitación",
            "p_urbaniz": "Sí",
            "f_incio": "2024-03-01",
            "f_recep": "",
            "f1acceso_r": "Sí",
            "f4agua_pot": "Sí",
            "f5electric": "Sí",
        }
        normalized = normalize_row(row)
        self.assertEqual(normalized["readiness"]["services"]["electrical_installation"], "yes")
        self.assertEqual(normalized["readiness"]["grid_capacity"], "not_assessed")
        self.assertEqual(normalized["readiness"]["reparcelation"], "processing")
        self.assertEqual(normalized["readiness"]["urbanisation_works"], "started")
        self.assertEqual(normalized["source_raw"], row)

    def test_csv_normalization_checks_schema_and_writes_jsonl(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "input.csv"
            target = Path(directory) / "output.jsonl"
            source.write_text(
                "municipio,cpm,uso,sup,f5electric\nElche,03065,industrial,1000,Sí\n",
                encoding="utf-8",
            )
            self.assertEqual(normalize_csv(source, target), 1)
            payload = json.loads(target.read_text(encoding="utf-8").strip())
            self.assertEqual(payload["normalized"]["global_land_use"], "industrial")
            self.assertEqual(payload["readiness"]["grid_capacity"], "not_assessed")

    def test_csv_missing_expected_fields_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "input.csv"
            target = Path(directory) / "output.jsonl"
            source.write_text("municipio,uso\nElche,industrial\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                normalize_csv(source, target)


if __name__ == "__main__":
    unittest.main()
