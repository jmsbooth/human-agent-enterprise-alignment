import json
import tempfile
import unittest
from pathlib import Path

from experimental.mismatch_exploration import (
    MISMATCH_TYPES,
    STATUSES,
    MismatchCase,
    catalog,
    filter_cases,
    main,
    summarize,
)


class MismatchExplorationTests(unittest.TestCase):
    def test_catalog_covers_the_paper_mismatch_types(self):
        cases = catalog()
        self.assertEqual(len(cases), len(MISMATCH_TYPES))
        self.assertEqual({case.mismatch_type for case in cases}, set(MISMATCH_TYPES))
        self.assertEqual({case.status for case in cases}, {"unknown"})

    def test_catalog_fields_are_non_empty_and_status_is_explicit(self):
        for case in catalog():
            for field in (
                "case_id",
                "mismatch_type",
                "representations_compared",
                "disagreement",
                "possible_evidence",
                "potential_consequence",
                "caveat",
                "status",
            ):
                self.assertTrue(getattr(case, field))
            self.assertIn(case.status, STATUSES)

    def test_statuses_remain_distinct(self):
        cases = (
            MismatchCase(
                "A",
                "semantic_process",
                "semantic and process representations",
                "definitions disagree",
                "versioned mapping review",
                "routing error",
                "context may explain the difference",
                "misalignment",
            ),
            MismatchCase(
                "B",
                "process_governance",
                "process and governance representations",
                "evidence is incomplete",
                "missing policy decision record",
                "classification is deferred",
                "instrumentation is needed",
                "unknown",
            ),
            MismatchCase(
                "C",
                "architecture_ownership",
                "architecture and ownership representations",
                "owners agree for the scoped service",
                "reviewed service catalog",
                "clear escalation",
                "scope is bounded",
                "alignment",
            ),
        )
        self.assertEqual(
            {case.status for case in cases},
            {"alignment", "misalignment", "unknown"},
        )
        self.assertEqual(
            summarize(cases)["counts_by_status"],
            {"alignment": 1, "misalignment": 1, "unknown": 1},
        )

    def test_filters_do_not_change_case_content(self):
        cases = catalog()
        selected = filter_cases(cases, mismatch_type="semantic_process")
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0], cases[0])
        self.assertEqual(filter_cases(cases, status="misalignment"), ())

    def test_invalid_case_values_are_rejected(self):
        with self.assertRaises(ValueError):
            MismatchCase(
                "bad",
                "not_a_mismatch",
                "representations",
                "disagreement",
                "evidence",
                "consequence",
                "caveat",
            )
        with self.assertRaises(ValueError):
            MismatchCase(
                "bad",
                "semantic_process",
                "representations",
                "disagreement",
                "evidence",
                "consequence",
                "caveat",
                "not_a_status",
            )

    def test_cli_writes_reproducible_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "nested" / "catalog.json"
            self.assertEqual(main(["--output", str(output)]), 0)
            payload = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(payload["tool_status"], "exploratory research tooling")
            self.assertEqual(len(payload["mismatch_cases"]), len(MISMATCH_TYPES))
            self.assertNotIn("alignment_score", json.dumps(payload))


if __name__ == "__main__":
    unittest.main()
