from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


EVIDENCE_HEADER = [
    "evidence_id",
    "source_id",
    "title",
    "authors",
    "year",
    "identifier",
    "version",
    "primary_url",
    "accessed_at",
    "supports_claim_ids",
    "locator",
    "verification_status",
    "notes",
]

CLAIM_HEADER = [
    "claim_id",
    "claim_text",
    "classification",
    "evidence_ids",
    "scope",
    "owner",
    "last_reviewed",
    "notes",
]

LITERATURE_HEADER = [
    "property_id",
    "proposed_property",
    "prior_work_id",
    "prior_work",
    "overlap",
    "difference",
    "evidence_ids",
    "discriminating_experiment",
    "status",
    "notes",
]

REQUIRED_PATHS = [
    "docs/research/CHARTER.md",
    "docs/research/STATE.md",
    "docs/research/NOVELTY.md",
    "docs/research/PROTOCOL.md",
    "docs/research/RISK_REGISTER.md",
    "docs/research/EVIDENCE_LEDGER.csv",
    "docs/research/CLAIM_LEDGER.csv",
    "docs/research/LITERATURE_MATRIX.csv",
    "docs/research/decisions/README.md",
    "docs/research/handoffs/README.md",
    "experiments/registry.yaml",
    "benchmarks",
    "configs",
    "paper",
    "src/wian",
    "tests",
]

REQUIRED_HEADINGS = {
    "docs/research/CHARTER.md": [
        "## Scientific question",
        "## Operational definitions",
        "## Required invariants",
        "## Decision gates",
        "## Governance",
    ],
    "docs/research/STATE.md": [
        "## Current milestone",
        "## Current gate",
        "## Active issues",
        "## Active agents",
        "## Decisions",
        "## Blockers",
        "## Last valid experiment",
        "## Next authorized action",
    ],
    "docs/research/NOVELTY.md": [
        "## Review question",
        "## Preregistered search plan",
        "## Inclusion criteria",
        "## Exclusion criteria",
        "## Decision rule",
    ],
    "docs/research/PROTOCOL.md": [
        "## Required baselines",
        "## Primary endpoints",
        "## Resource-matching regimes",
        "## Statistical policy",
        "## Reproducibility manifest",
    ],
}

CLAIM_CLASSIFICATIONS = {
    "VERIFIED",
    "PARTIAL",
    "INFERENCE",
    "DISPUTED",
    "UNSUPPORTED",
}

EVIDENCE_STATUSES = {
    "VERIFIED",
    "PARTIAL",
    "UNREAD",
    "UNAVAILABLE",
    "DISPUTED",
}

LITERATURE_STATUSES = {
    "PENDING",
    "INCLUDED",
    "EXCLUDED",
    "DISPUTED",
}


def validate_csv(
    path: Path,
    expected_header: list[str],
    id_field: str,
    enum_fields: dict[str, set[str]] | None = None,
) -> list[str]:
    errors: list[str] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_header:
            return [
                f"{path}: unexpected header {reader.fieldnames!r}; "
                f"expected {expected_header!r}"
            ]
        seen: set[str] = set()
        for line_number, row in enumerate(reader, start=2):
            record_id = (row.get(id_field) or "").strip()
            if not record_id:
                errors.append(f"{path}:{line_number}: missing {id_field}")
            elif record_id in seen:
                errors.append(
                    f"{path}:{line_number}: duplicate {id_field} {record_id!r}"
                )
            seen.add(record_id)
            for field, allowed in (enum_fields or {}).items():
                value = (row.get(field) or "").strip()
                if value not in allowed:
                    errors.append(
                        f"{path}:{line_number}: invalid {field} {value!r}; "
                        f"expected one of {sorted(allowed)!r}"
                    )
    return errors


def validate_markdown(path: Path, headings: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [f"{path}: missing heading {heading!r}" for heading in headings if heading not in text]


def validate_registry(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    required_patterns = {
        "schema_version": r"(?m)^schema_version:\s*1\s*$",
        "project": r"(?m)^project:\s*workspace-is-all-u-need\s*$",
        "status": r"(?m)^status:\s*[a-z][a-z0-9_-]*\s*$",
        "last_updated": r"(?m)^last_updated:\s*\d{4}-\d{2}-\d{2}\s*$",
        "experiments": r"(?m)^experiments:\s*(?:\[\]|$)",
    }
    for field, pattern in required_patterns.items():
        if re.search(pattern, text) is None:
            errors.append(f"{path}: missing or invalid {field}")
    return errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_PATHS:
        if not (root / relative).exists():
            errors.append(f"missing required path: {relative}")

    for relative, headings in REQUIRED_HEADINGS.items():
        path = root / relative
        if path.is_file():
            errors.extend(validate_markdown(path, headings))

    evidence_path = root / "docs/research/EVIDENCE_LEDGER.csv"
    if evidence_path.is_file():
        errors.extend(
            validate_csv(
                evidence_path,
                EVIDENCE_HEADER,
                "evidence_id",
                {"verification_status": EVIDENCE_STATUSES},
            )
        )

    claim_path = root / "docs/research/CLAIM_LEDGER.csv"
    if claim_path.is_file():
        errors.extend(
            validate_csv(
                claim_path,
                CLAIM_HEADER,
                "claim_id",
                {"classification": CLAIM_CLASSIFICATIONS},
            )
        )

    literature_path = root / "docs/research/LITERATURE_MATRIX.csv"
    if literature_path.is_file():
        errors.extend(
            validate_csv(
                literature_path,
                LITERATURE_HEADER,
                "prior_work_id",
                {"status": LITERATURE_STATUSES},
            )
        )

    registry_path = root / "experiments/registry.yaml"
    if registry_path.is_file():
        errors.extend(validate_registry(registry_path))

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("governance validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
