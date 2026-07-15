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

PREDICTION_HEADER = [
    "prediction_id",
    "status",
    "claim",
    "unit",
    "target_workload",
    "pre_outcome_observables",
    "intervention_or_comparison",
    "eligible_implementation_classes",
    "matching_regime",
    "primary_outcome",
    "expected_ordering",
    "falsification_margin",
    "counterexample",
    "decisive_falsifier",
    "minimum_design_id",
    "closest_prior_art",
    "novelty_disposition",
    "registry_role",
]

COUNTEREXAMPLE_HEADER = [
    "counterexample_id",
    "target_kind",
    "target_prediction_or_thesis",
    "related_prediction_ids",
    "support_relation",
    "pre_outcome_regime",
    "intervention_or_comparison",
    "expected_failure_of_shift",
    "decisive_observation",
    "evidence_ids",
    "evidence_locators",
    "status",
    "novelty_disposition",
]

M1B_SEARCH_HEADER = [
    "search_id",
    "source",
    "exact_query",
    "executed_at",
    "result_count",
    "count_scope",
    "screened",
    "included",
    "excluded",
    "adaptation",
    "discovery_path",
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
    "docs/research/M1B_SEARCH_PROTOCOL.md",
    "docs/research/M1B_SEARCH_LOG.csv",
    "docs/research/M1C_CANDIDATE_REGISTER.md",
    "docs/research/M1C_SCOPING_LOG.md",
    "docs/research/M1D_CANDIDATE_REGISTER.md",
    "docs/research/M1D_SCOPING_LOG.md",
    "docs/research/TRANSITION_CONTRACT.md",
    "docs/research/PREDICTION_REGISTER.csv",
    "docs/research/COUNTEREXAMPLE_REGISTER.csv",
    "docs/research/MINIMUM_DISCRIMINATING_DESIGNS.md",
    "docs/research/decisions/README.md",
    "docs/research/decisions/0005-stop-distinct-object-discovery.md",
    "docs/research/decisions/0006-stop-nonfactorizing-state-compute-discovery.md",
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
    "docs/research/M1C_CANDIDATE_REGISTER.md": [
        "## Gate",
        "## Candidate register",
        "## Strongest-composite result",
        "## Minimum-design decision",
        "## Decision",
    ],
    "docs/research/M1C_SCOPING_LOG.md": [
        "## Scope",
        "## Recorded discovery queries",
        "## Exact primary-record resolutions",
        "## Resolution notes",
        "## Search outcome",
    ],
    "docs/research/decisions/0005-stop-distinct-object-discovery.md": [
        "## Context",
        "## Findings",
        "## Decision",
        "## Anti-rewrite determination",
        "## Alternatives considered",
        "## Evidence",
        "## Consequences",
    ],
    "docs/research/M1D_CANDIDATE_REGISTER.md": [
        "## Gate",
        "## Candidate register",
        "## Strongest-composite result",
        "## Minimum-design decision",
        "## Decision",
    ],
    "docs/research/M1D_SCOPING_LOG.md": [
        "## Scope",
        "## Recorded discovery queries",
        "## Exact primary-record resolutions",
        "## Resolution notes",
        "## Search outcome",
    ],
    "docs/research/decisions/0006-stop-nonfactorizing-state-compute-discovery.md": [
        "## Context",
        "## Findings",
        "## Decision",
        "## Anti-rewrite determination",
        "## Alternatives considered",
        "## Evidence",
        "## Consequences",
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

M1B_STATUSES = {
    "ANTICIPATED",
    "PARTIAL",
    "DISTINCT_CANDIDATE",
    "UNSUPPORTED",
}

COUNTEREXAMPLE_TARGET_KINDS = {
    "PREDICTION",
    "THESIS",
}

COUNTEREXAMPLE_RELATIONS = {
    "WITHIN_SUPPORT_FALSIFIER",
    "OUT_OF_SUPPORT_NEGATIVE_REGIME",
    "ORTHOGONAL_INSTANTIATION",
    "INDEPENDENT_CONTRACT_FALSIFIER",
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
            if None in row:
                errors.append(
                    f"{path}:{line_number}: extra columns {row[None]!r}"
                )
            missing_columns = [
                field for field in expected_header if row.get(field) is None
            ]
            if missing_columns:
                errors.append(
                    f"{path}:{line_number}: missing columns {missing_columns!r}"
                )
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


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def validate_m1b_cross_references(root: Path) -> list[str]:
    errors: list[str] = []
    prediction_path = root / "docs/research/PREDICTION_REGISTER.csv"
    counterexample_path = root / "docs/research/COUNTEREXAMPLE_REGISTER.csv"
    evidence_path = root / "docs/research/EVIDENCE_LEDGER.csv"
    claim_path = root / "docs/research/CLAIM_LEDGER.csv"
    literature_path = root / "docs/research/LITERATURE_MATRIX.csv"
    designs_path = root / "docs/research/MINIMUM_DISCRIMINATING_DESIGNS.md"

    if not all(
        path.is_file()
        for path in [
            prediction_path,
            counterexample_path,
            evidence_path,
            claim_path,
            literature_path,
            designs_path,
        ]
    ):
        return errors

    predictions = read_csv_rows(prediction_path)
    counterexamples = read_csv_rows(counterexample_path)
    evidence_rows = read_csv_rows(evidence_path)
    claim_rows = read_csv_rows(claim_path)
    literature_rows = read_csv_rows(literature_path)
    evidence_ids = {
        (row.get("evidence_id") or "").strip() for row in evidence_rows
    }
    claim_ids = {
        (row.get("claim_id") or "").strip() for row in claim_rows
    }
    prediction_ids = {
        (row.get("prediction_id") or "").strip() for row in predictions
    }
    design_ids = set(
        re.findall(
            r"(?m)^## (M1B-D\d{2}):",
            designs_path.read_text(encoding="utf-8"),
        )
    )

    for line_number, row in enumerate(evidence_rows, start=2):
        for claim_id in split_ids(row.get("supports_claim_ids") or ""):
            if claim_id not in claim_ids:
                errors.append(
                    f"{evidence_path}:{line_number}: unknown claim id "
                    f"{claim_id!r}"
                )

    for line_number, row in enumerate(claim_rows, start=2):
        for evidence_id in split_ids(row.get("evidence_ids") or ""):
            if evidence_id not in evidence_ids:
                errors.append(
                    f"{claim_path}:{line_number}: unknown evidence id "
                    f"{evidence_id!r}"
                )

    for line_number, row in enumerate(literature_rows, start=2):
        for evidence_id in split_ids(row.get("evidence_ids") or ""):
            if evidence_id not in evidence_ids:
                errors.append(
                    f"{literature_path}:{line_number}: unknown evidence id "
                    f"{evidence_id!r}"
                )

    referenced_design_ids: set[str] = set()
    for line_number, row in enumerate(predictions, start=2):
        design_id = (row.get("minimum_design_id") or "").strip()
        referenced_design_ids.add(design_id)
        if design_id not in design_ids:
            errors.append(
                f"{prediction_path}:{line_number}: unknown minimum_design_id "
                f"{design_id!r}"
            )
        for evidence_id in split_ids(row.get("closest_prior_art") or ""):
            if evidence_id not in evidence_ids:
                errors.append(
                    f"{prediction_path}:{line_number}: unknown evidence id "
                    f"{evidence_id!r}"
                )

    for design_id in sorted(design_ids - referenced_design_ids):
        errors.append(f"{designs_path}: unreferenced design {design_id!r}")

    covered_prediction_ids: set[str] = set()
    for line_number, row in enumerate(counterexamples, start=2):
        target_kind = (row.get("target_kind") or "").strip()
        target = (row.get("target_prediction_or_thesis") or "").strip()
        if target_kind == "PREDICTION" and target not in prediction_ids:
            errors.append(
                f"{counterexample_path}:{line_number}: unknown prediction target "
                f"{target!r}"
            )
        for prediction_id in split_ids(row.get("related_prediction_ids") or ""):
            covered_prediction_ids.add(prediction_id)
            if prediction_id not in prediction_ids:
                errors.append(
                    f"{counterexample_path}:{line_number}: unknown related "
                    f"prediction {prediction_id!r}"
                )
        for evidence_id in split_ids(row.get("evidence_ids") or ""):
            if evidence_id not in evidence_ids:
                errors.append(
                    f"{counterexample_path}:{line_number}: unknown evidence id "
                    f"{evidence_id!r}"
                )

    for prediction_id in sorted(prediction_ids - covered_prediction_ids):
        errors.append(
            f"{counterexample_path}: no counterexample covers {prediction_id!r}"
        )

    return errors


def validate_m1b_search_log(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return errors

    for line_number, row in enumerate(read_csv_rows(path), start=2):
        included = (row.get("included") or "").strip()
        excluded = (row.get("excluded") or "").strip()
        if included == "PENDING" or excluded == "PENDING":
            errors.append(
                f"{path}:{line_number}: unresolved inclusion/exclusion status"
            )
        if included == "NON DISPONIBLE" or excluded == "NON DISPONIBLE":
            if included != excluded:
                errors.append(
                    f"{path}:{line_number}: inclusion and exclusion must both be "
                    "NON DISPONIBLE"
                )
            continue
        try:
            screened = int((row.get("screened") or "").strip())
            included_count = int(included)
            excluded_count = int(excluded)
        except ValueError:
            errors.append(
                f"{path}:{line_number}: invalid screening counts"
            )
            continue
        if included_count + excluded_count > screened:
            errors.append(
                f"{path}:{line_number}: included plus excluded exceeds screened"
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

    prediction_path = root / "docs/research/PREDICTION_REGISTER.csv"
    if prediction_path.is_file():
        errors.extend(
            validate_csv(
                prediction_path,
                PREDICTION_HEADER,
                "prediction_id",
                {"status": M1B_STATUSES},
            )
        )

    counterexample_path = root / "docs/research/COUNTEREXAMPLE_REGISTER.csv"
    if counterexample_path.is_file():
        errors.extend(
            validate_csv(
                counterexample_path,
                COUNTEREXAMPLE_HEADER,
                "counterexample_id",
                {
                    "target_kind": COUNTEREXAMPLE_TARGET_KINDS,
                    "support_relation": COUNTEREXAMPLE_RELATIONS,
                    "status": M1B_STATUSES,
                },
            )
        )

    search_log_path = root / "docs/research/M1B_SEARCH_LOG.csv"
    if search_log_path.is_file():
        errors.extend(
            validate_csv(
                search_log_path,
                M1B_SEARCH_HEADER,
                "search_id",
            )
        )
        errors.extend(validate_m1b_search_log(search_log_path))

    errors.extend(validate_m1b_cross_references(root))

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
