from __future__ import annotations

import csv
import tempfile
import unittest
from pathlib import Path

from scripts.validate_governance import (
    CLAIM_CLASSIFICATIONS,
    CLAIM_HEADER,
    validate,
    validate_csv,
)


ROOT = Path(__file__).resolve().parents[1]


class GovernanceValidationTests(unittest.TestCase):
    def test_repository_snapshot_passes(self) -> None:
        self.assertEqual(validate(ROOT), [])

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


if __name__ == "__main__":
    unittest.main()
