from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from scripts.validate_governance import (
    CLAIM_CLASSIFICATIONS,
    CLAIM_HEADER,
    REQUIRED_HEADINGS,
    REQUIRED_PATHS,
    validate,
    validate_csv,
)


ROOT = Path(__file__).resolve().parents[1]


class GovernanceValidationTests(unittest.TestCase):
    def test_repository_snapshot_passes(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_scientific_decision_artifacts_are_governed(self) -> None:
        expected = {
            "docs/research/M1C_CANDIDATE_REGISTER.md",
            "docs/research/M1C_SCOPING_LOG.md",
            "docs/research/decisions/0005-stop-distinct-object-discovery.md",
            "docs/research/M1D_CANDIDATE_REGISTER.md",
            "docs/research/M1D_SCOPING_LOG.md",
            "docs/research/decisions/0006-stop-nonfactorizing-state-compute-discovery.md",
            "docs/research/handoffs/2026-07-15-m1d-bibliographic-audit.md",
            "docs/research/handoffs/2026-07-15-m1d-final-cross-review.md",
        }

        self.assertTrue(expected.issubset(REQUIRED_PATHS))
        self.assertTrue(expected.issubset(REQUIRED_HEADINGS))

    def test_duplicate_identifier_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "claims.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=CLAIM_HEADER)
                writer.writeheader()
                row = {field: "" for field in CLAIM_HEADER}
                row.update(
                    {
                        "claim_id": "CLM-001",
                        "claim_text": "candidate claim",
                        "classification": "UNSUPPORTED",
                    }
                )
                writer.writerow(row)
                writer.writerow(row)

            errors = validate_csv(
                path,
                CLAIM_HEADER,
                "claim_id",
                {"classification": CLAIM_CLASSIFICATIONS},
            )

        self.assertTrue(any("duplicate claim_id" in error for error in errors))

    def test_invalid_classification_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "claims.csv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=CLAIM_HEADER)
                writer.writeheader()
                row = {field: "" for field in CLAIM_HEADER}
                row.update(
                    {
                        "claim_id": "CLM-001",
                        "claim_text": "candidate claim",
                        "classification": "PROVEN",
                    }
                )
                writer.writerow(row)

            errors = validate_csv(
                path,
                CLAIM_HEADER,
                "claim_id",
                {"classification": CLAIM_CLASSIFICATIONS},
            )

        self.assertTrue(any("invalid classification" in error for error in errors))

    def test_missing_csv_column_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "claims.csv"
            path.write_text(
                "claim_id,claim_text,classification,evidence_ids,scope,owner,"
                "last_reviewed,notes\n"
                "CLM-001,candidate claim,UNSUPPORTED,,,,\n",
                encoding="utf-8",
            )

            errors = validate_csv(
                path,
                CLAIM_HEADER,
                "claim_id",
                {"classification": CLAIM_CLASSIFICATIONS},
            )

        self.assertTrue(any("missing columns" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
