#!/usr/bin/env python3
"""Build the canonical public, de-identified release for a NeoMundi weekly barometer.

Version 2.1.0 consolidates the canonical public release workflow:
- strict campaign-shape and repetition validation;
- stable de-identification through a private profile registry;
- clear separation between internal scoring fields and public aggregates;
- automatic release snapshot and regime summary;
- canonical public metric contract and README generation;
- builder provenance and file-integrity hashes in the manifest;
- cleanup of partial output on failure.

The script deliberately exports only aggregated, de-identified measurement data.
It never exports provider names, model names, prompts, responses, request IDs,
trace IDs, raw payloads, per-response timestamps, private profile mappings,
or diagnostic payloads.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import re
import shutil
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


BUILDER_NAME = "build_public_barometer_release"
BUILDER_VERSION = "2.1.0"
PUBLIC_SCHEMA_VERSION = "1.2.0"

EXPECTED_SYSTEMS = 12
EXPECTED_QUESTIONS = 4
EXPECTED_REPETITIONS = 100
EXPECTED_ROWS_PER_SYSTEM = EXPECTED_QUESTIONS * EXPECTED_REPETITIONS
EXPECTED_ROWS_PER_QUESTION = EXPECTED_SYSTEMS * EXPECTED_REPETITIONS
EXPECTED_ROWS_TOTAL = EXPECTED_SYSTEMS * EXPECTED_QUESTIONS * EXPECTED_REPETITIONS

REQUIRED_COLUMNS = {
    "provider",
    "requested_model",
    "prompt_id",
    "repetition_index",
    "decision",
    "stability_score",
    "v_score",
    "factual_hallucination_score",
    "semantic_instability_score",
    "coherence_score",
    "error",
}

INTERNAL_SCORING_METRICS = [
    "stability_score",
    "v_score",
    "factual_hallucination_score",
    "semantic_instability_score",
    "coherence_score",
]

PUBLIC_AGGREGATE_METRICS = [
    "stability_score",
    "semantic_instability_score",
]

DOCUMENTATION_LINKS = [
    ("Public methodology — English", "../../docs/methodology_public_en.md"),
    ("Méthodologie publique — Français", "../../docs/methodology_public_fr.md"),
    ("Public baseline", "../../docs/public_baseline.md"),
    ("Repository overview", "../../README.md"),
]

REGIME_DEFINITIONS = [
    (
        "NORMAL_SIGNAL",
        "Normal signal",
        "No factual alert, semantic-variation signal or incomplete measurement detected.",
    ),
    (
        "SEMANTIC_VARIATION",
        "Semantic variation",
        "Semantic-instability signal detected without factual alert.",
    ),
    (
        "FACTUAL_ALERT",
        "Factual alert",
        "Non-zero factual-risk signal or FLAG decision without semantic-variation signal.",
    ),
    (
        "COMBINED_ALERT",
        "Combined alert",
        "Both factual-alert and semantic-variation signals detected.",
    ),
    (
        "INCOMPLETE_MEASUREMENT",
        "Incomplete measurement",
        "Execution error or missing core metric; excluded from fully-scored aggregates.",
    ),
]


def die(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(2)


def safe_float(value: object) -> float | None:
    if pd.isna(value):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(result) or math.isinf(result):
        return None
    return result


def fmt(value: float | int | None, digits: int = 6) -> float | None:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return None
    return round(float(value), digits)


def percent(value: float | None, digits: int = 2) -> str:
    if value is None:
        return "n/a"
    return f"{value * 100:.{digits}f}%"


def readable_date(value: str) -> str:
    normalized = value.strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(normalized).date().isoformat()
    except ValueError:
        try:
            return datetime.strptime(value.strip(), "%Y-%m-%d").date().isoformat()
        except ValueError as exc:
            raise ValueError(
                f"Invalid date or datetime '{value}'. Use YYYY-MM-DD or ISO-8601."
            ) from exc


def extract_barometer_number(campaign_id: str) -> int:
    patterns = [
        r"BAROMETER[_-](\d+)",
        r"barometer[_-](\d+)",
        r"barometer[_-]0*(\d+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, campaign_id, flags=re.IGNORECASE)
        if match:
            return int(match.group(1))
    die(
        "Unable to extract the barometer number from --campaign-id. "
        "Use a value such as BAROMETER_7_2026-07-27_2026-08-02."
    )


def find_csvs(input_dir: Path) -> list[Path]:
    files = sorted(input_dir.rglob("*.csv"))
    if not files:
        die(f"No CSV files found under: {input_dir}")
    return files


def load_campaign(input_dir: Path) -> tuple[pd.DataFrame, list[dict]]:
    frames: list[pd.DataFrame] = []
    inventory: list[dict] = []

    for path in find_csvs(input_dir):
        try:
            frame = pd.read_csv(path, low_memory=False)
        except Exception as exc:  # noqa: BLE001
            die(f"Could not read {path.name}: {exc}")

        if frame.empty:
            die(f"Source CSV is empty: {path.name}")

        missing = REQUIRED_COLUMNS - set(frame.columns)
        if missing:
            die(f"{path.name} is missing required columns: {sorted(missing)}")

        frame = frame.copy()
        frame["_source_file"] = path.name
        frames.append(frame)
        inventory.append(
            {
                "source_file": path.name,
                "rows": int(len(frame)),
                "columns": int(len(frame.columns) - 1),
                "provider_count": int(frame["provider"].nunique(dropna=True)),
                "model_count": int(frame["requested_model"].nunique(dropna=True)),
            }
        )

    campaign = pd.concat(frames, ignore_index=True, sort=False)
    return campaign, inventory


def validate_repetition_indices(df: pd.DataFrame) -> dict:
    issues: list[dict] = []
    expected = set(range(1, EXPECTED_REPETITIONS + 1))

    for (provider, model, prompt_id), group in df.groupby(
        ["provider", "requested_model", "prompt_id"], dropna=False, sort=True
    ):
        raw_values = pd.to_numeric(group["repetition_index"], errors="coerce")
        actual = set(raw_values.dropna().astype(int).tolist())
        missing = sorted(expected - actual)
        extras = sorted(actual - expected)

        if len(group) != EXPECTED_REPETITIONS or missing or extras or raw_values.isna().any():
            issues.append(
                {
                    "provider": str(provider),
                    "requested_model": str(model),
                    "prompt_id": str(prompt_id),
                    "rows": int(len(group)),
                    "missing_repetitions": missing,
                    "unexpected_repetitions": extras,
                    "non_numeric_repetition_values": int(raw_values.isna().sum()),
                }
            )

    return {
        "groups_checked": EXPECTED_SYSTEMS * EXPECTED_QUESTIONS,
        "groups_with_issues": len(issues),
        "issues_private": issues,
    }


def validate_campaign(df: pd.DataFrame, inventory: list[dict]) -> dict:
    systems = (
        df[["provider", "requested_model"]]
        .fillna("<missing>")
        .drop_duplicates()
        .sort_values(["provider", "requested_model"])
    )
    prompt_ids = sorted(df["prompt_id"].dropna().astype(str).unique().tolist())
    duplicate_key = ["provider", "requested_model", "prompt_id", "repetition_index"]
    duplicates = int(df.duplicated(duplicate_key, keep=False).sum())

    metric_complete = df[INTERNAL_SCORING_METRICS].notna().all(axis=1)
    non_error = df["error"].isna() & df["decision"].fillna("").ne("ERROR")
    fully_scorable = metric_complete & non_error

    rows_per_system = (
        df.groupby(["provider", "requested_model"], dropna=False)
        .size()
        .astype(int)
        .to_dict()
    )
    rows_per_question = (
        df.groupby("prompt_id", dropna=False).size().astype(int).to_dict()
    )
    repetition_validation = validate_repetition_indices(df)

    validation = {
        "row_count": int(len(df)),
        "source_file_count": int(len(inventory)),
        "system_count": int(len(systems)),
        "prompt_count": int(len(prompt_ids)),
        "prompt_ids_private": prompt_ids,
        "duplicate_rows": duplicates,
        "metric_complete_rows": int(metric_complete.sum()),
        "non_error_rows": int(non_error.sum()),
        "fully_scorable_rows": int(fully_scorable.sum()),
        "incomplete_or_error_rows": int((~fully_scorable).sum()),
        "coverage_rate": fmt(float(fully_scorable.mean()), 6),
        "rows_per_system_private": {
            f"{provider}::{model}": count
            for (provider, model), count in rows_per_system.items()
        },
        "rows_per_question_private": {
            str(prompt_id): count for prompt_id, count in rows_per_question.items()
        },
        "repetition_validation_private": repetition_validation,
    }

    if validation["source_file_count"] != EXPECTED_SYSTEMS:
        die(
            f"Expected exactly {EXPECTED_SYSTEMS} source CSV files; "
            f"found {validation['source_file_count']}."
        )
    if validation["system_count"] != EXPECTED_SYSTEMS:
        die(f"Expected {EXPECTED_SYSTEMS} systems; found {validation['system_count']}.")
    if validation["prompt_count"] != EXPECTED_QUESTIONS:
        die(
            f"Expected {EXPECTED_QUESTIONS} questions; found {validation['prompt_count']}."
        )
    if validation["row_count"] != EXPECTED_ROWS_TOTAL:
        die(
            f"Expected {EXPECTED_ROWS_TOTAL:,} rows; found {validation['row_count']:,}."
        )
    if validation["duplicate_rows"]:
        die(
            "Duplicate provider/model/prompt/repetition rows detected: "
            f"{validation['duplicate_rows']}."
        )

    bad_system_counts = {
        key: count
        for key, count in validation["rows_per_system_private"].items()
        if count != EXPECTED_ROWS_PER_SYSTEM
    }
    if bad_system_counts:
        die(
            f"Each system must have {EXPECTED_ROWS_PER_SYSTEM} rows. "
            f"Invalid private counts: {bad_system_counts}"
        )

    bad_question_counts = {
        key: count
        for key, count in validation["rows_per_question_private"].items()
        if count != EXPECTED_ROWS_PER_QUESTION
    }
    if bad_question_counts:
        die(
            f"Each question must have {EXPECTED_ROWS_PER_QUESTION} rows. "
            f"Invalid private counts: {bad_question_counts}"
        )

    if repetition_validation["groups_with_issues"]:
        first_issues = repetition_validation["issues_private"][:5]
        die(
            "Repetition indices are incomplete, duplicated, non-numeric or outside "
            f"1..{EXPECTED_REPETITIONS}. First issues: {first_issues}"
        )

    return validation


def canonical_profile_key(provider: object, model: object) -> str:
    """Resolve a private source row to a registry lookup key.

    The public builder contains no provider-specific or model-specific aliases.
    Any exceptional identity mapping required to preserve a stable logical identity
    must be handled in the private profile registry or in a private preprocessing
    step before this public builder is executed.

    Provider and model values are used only inside the private execution environment
    and are never written to the public release artefacts.
    """
    del model  # Model-specific aliases are deliberately excluded from public code.
    return str(provider).strip().lower()


def anonymise_profiles(df: pd.DataFrame, mapping_path: Path) -> pd.DataFrame:
    required = {"provider", "profile_id", "created_at"}
    if not mapping_path.exists():
        die(f"Private profile mapping does not exist: {mapping_path}")

    registry = pd.read_csv(
        mapping_path, dtype=str, encoding="utf-8-sig"
    ).fillna("")
    missing = required - set(registry.columns)
    if missing:
        die(f"Private profile mapping is missing columns: {sorted(missing)}")

    registry["provider"] = registry["provider"].str.strip().str.lower()
    registry["profile_id"] = registry["profile_id"].str.strip()

    if registry["provider"].duplicated().any():
        die("Private profile mapping contains duplicate provider keys.")
    if registry["profile_id"].duplicated().any():
        die("Private profile mapping contains duplicate profile_id values.")
    if not registry["profile_id"].str.fullmatch(r"PROFILE-[A-F0-9]{6}").all():
        die("Each profile_id must follow the opaque format PROFILE-XXXXXX.")

    public_df = df.copy()
    public_df["_registry_provider"] = public_df.apply(
        lambda row: canonical_profile_key(
            row["provider"], row["requested_model"]
        ),
        axis=1,
    )

    lookup = dict(zip(registry["provider"], registry["profile_id"], strict=True))
    public_df["profile_id"] = public_df["_registry_provider"].map(lookup)

    unresolved = sorted(
        public_df.loc[
            public_df["profile_id"].isna(), "_registry_provider"
        ]
        .dropna()
        .unique()
    )
    if unresolved:
        die(
            "Current campaign contains logical profiles absent from private mapping: "
            f"{unresolved}"
        )

    if public_df["profile_id"].nunique() != EXPECTED_SYSTEMS:
        die(
            f"Expected {EXPECTED_SYSTEMS} uniquely mapped public profiles; "
            f"found {public_df['profile_id'].nunique()}."
        )

    return public_df


def classify_observation(row: pd.Series) -> str:
    metric_missing = any(pd.isna(row.get(metric)) for metric in INTERNAL_SCORING_METRICS)
    has_error = pd.notna(row.get("error"))
    decision = str(row.get("decision", ""))

    if has_error or decision == "ERROR" or metric_missing:
        return "INCOMPLETE_MEASUREMENT"

    semantic = safe_float(row.get("semantic_instability_score")) or 0.0
    factual = safe_float(row.get("factual_hallucination_score")) or 0.0
    factual_alert = factual > 0.0 or decision == "FLAG"
    semantic_alert = semantic > 0.0

    if factual_alert and semantic_alert:
        return "COMBINED_ALERT"
    if factual_alert:
        return "FACTUAL_ALERT"
    if semantic_alert:
        return "SEMANTIC_VARIATION"
    return "NORMAL_SIGNAL"


def dominant_regime(series: pd.Series) -> str:
    precedence = [
        "COMBINED_ALERT",
        "FACTUAL_ALERT",
        "SEMANTIC_VARIATION",
        "INCOMPLETE_MEASUREMENT",
        "NORMAL_SIGNAL",
    ]
    counts = Counter(series.astype(str).tolist())
    max_count = max(counts.values()) if counts else 0
    return next(label for label in precedence if counts.get(label, 0) == max_count)


def profile_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []

    for profile_id, group in df.groupby("profile_id", sort=True):
        non_error = (
            group["error"].isna()
            & group["decision"].fillna("").ne("ERROR")
        )
        full = group.loc[non_error].dropna(subset=INTERNAL_SCORING_METRICS).copy()
        total = len(group)

        rows.append(
            {
                "profile_id": profile_id,
                "executions_total": int(total),
                "executions_fully_scored": int(len(full)),
                "coverage_rate": fmt(len(full) / total if total else 0.0),
                "stability_mean": fmt(
                    full["stability_score"].mean() if not full.empty else None
                ),
                "semantic_variation_rate": fmt(
                    (
                        full["semantic_instability_score"].astype(float) > 0
                    ).mean()
                    if not full.empty
                    else None
                ),
                "flag_rate": fmt((group["decision"] == "FLAG").mean()),
                "error_rate": fmt((group["decision"] == "ERROR").mean()),
                "dominant_regime": dominant_regime(
                    group["observation_regime"]
                ),
            }
        )

    return (
        pd.DataFrame(rows)
        .sort_values("profile_id")
        .reset_index(drop=True)
    )


def question_summary(df: pd.DataFrame) -> pd.DataFrame:
    prompt_map: dict[str, str] = {}
    unique_prompts = sorted(
        df["prompt_id"].dropna().astype(str).unique().tolist()
    )
    for index, prompt in enumerate(unique_prompts, start=1):
        prompt_map[prompt] = f"Question {index}"

    out = df.copy()
    out["question_id"] = out["prompt_id"].astype(str).map(prompt_map)
    rows: list[dict] = []

    for question_id, group in out.groupby("question_id", sort=True):
        full = group.loc[
            group["error"].isna()
            & group["decision"].fillna("").ne("ERROR")
        ].dropna(subset=INTERNAL_SCORING_METRICS)

        rows.append(
            {
                "question_id": question_id,
                "executions_total": int(len(group)),
                "executions_fully_scored": int(len(full)),
                "coverage_rate": fmt(
                    len(full) / len(group) if len(group) else 0.0
                ),
                "stability_mean": fmt(
                    full["stability_score"].mean() if not full.empty else None
                ),
                "semantic_variation_rate": fmt(
                    (
                        full["semantic_instability_score"].astype(float) > 0
                    ).mean()
                    if not full.empty
                    else None
                ),
                "flag_rate": fmt((group["decision"] == "FLAG").mean()),
                "error_rate": fmt((group["decision"] == "ERROR").mean()),
            }
        )

    return (
        pd.DataFrame(rows)
        .sort_values("question_id")
        .reset_index(drop=True)
    )


def regime_distribution(df: pd.DataFrame) -> pd.DataFrame:
    counts = df["observation_regime"].value_counts(dropna=False).to_dict()
    total = len(df)

    return pd.DataFrame(
        [
            {
                "regime_id": code,
                "regime_label": label,
                "definition": definition,
                "observations": int(counts.get(code, 0)),
                "share_of_all_executions": fmt(
                    counts.get(code, 0) / total if total else 0.0
                ),
            }
            for code, label, definition in REGIME_DEFINITIONS
        ]
    )


def global_overview(
    df: pd.DataFrame, validation: dict
) -> dict:
    full = df.loc[
        df["observation_regime"] != "INCOMPLETE_MEASUREMENT"
    ].dropna(subset=INTERNAL_SCORING_METRICS)

    return {
        "schema_version": PUBLIC_SCHEMA_VERSION,
        "executions_launched": validation["row_count"],
        "executions_non_error": validation["non_error_rows"],
        "executions_fully_scored": validation["fully_scorable_rows"],
        "incomplete_or_error_rows": validation["incomplete_or_error_rows"],
        "coverage_rate": validation["coverage_rate"],
        "systems_observed": validation["system_count"],
        "questions_observed": validation["prompt_count"],
        "duplicate_rows_detected": validation["duplicate_rows"],
        "global_metrics": {
            "stability_mean": fmt(
                full["stability_score"].mean() if not full.empty else None
            ),
            "semantic_variation_rate": fmt(
                (
                    full["semantic_instability_score"].astype(float) > 0
                ).mean()
                if not full.empty
                else None
            ),
        },
    }

def metric_contract() -> dict:
    return {
        "schema_version": PUBLIC_SCHEMA_VERSION,
        "scope": (
            "Aggregated, de-identified weekly observations. No prompt text, "
            "response content, provider name, model name, or raw payload is published."
        ),
        "metrics": [
            {
                "public_name": "stability_mean",
                "source_field": "stability_score",
                "meaning": (
                    "Mean runtime stability measurement across fully scored observations."
                ),
                "unit": "0 to 1",
                "warning": (
                    "This is an observed runtime measurement, not a quality ranking, "
                    "truth guarantee or deployment certification."
                ),
            },
            {
                "public_name": "semantic_variation_rate",
                "source_field": "semantic_instability_score",
                "meaning": (
                    "Share of fully scored observations with a non-zero "
                    "semantic-instability signal."
                ),
                "unit": "proportion",
                "warning": (
                    "A semantic-variation signal is not itself a factual-error finding."
                ),
            },
        ],
        "published_operational_fields": [
            "coverage_rate",
            "flag_rate",
            "error_rate",
            "dominant_regime",
            "observation_regime_distribution",
        ],
        "excluded_private_fields": [
            "provider",
            "requested_model",
            "observed_model",
            "prompt_id",
            "llm_response",
            "llm_response_raw",
            "request_id",
            "trace_id",
            "raw_stream_payload",
            "raw_govern_payload",
            "api_timestamp",
            "governance_reasons",
        ],
    }


def write_csv(df: pd.DataFrame, path: Path) -> None:
    df.to_csv(
        path,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )


def write_json(payload: object, path: Path) -> None:
    path.write_text(
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def write_readme(
    output_dir: Path,
    campaign_id: str,
    period_start: str,
    period_end: str,
    barometer_number: int,
    validation: dict,
    regimes: pd.DataFrame,
    overview: dict,
) -> None:
    docs = "\n".join(
        f"- [{label}]({url})" for label, url in DOCUMENTATION_LINKS
    )

    regime_lines = "\n".join(
        f"- {row.regime_label}: "
        f"{percent(float(row.share_of_all_executions), 2)} "
        f"({int(row.observations):,} observations)"
        for row in regimes.itertuples(index=False)
    )


    text = f"""# NeoMundi Weekly Barometer #{barometer_number} — Public Data Release

**Campaign:** `{campaign_id}`  
**Observation period:** {readable_date(period_start)} to {readable_date(period_end)}  
**Publication form:** Aggregated and de-identified

## Documentation

{docs}

## Release snapshot

- Systems observed: {validation["system_count"]}
- Questions observed: {validation["prompt_count"]}
- Executions launched: {validation["row_count"]:,}
- Fully scored: {validation["fully_scorable_rows"]:,}
- Coverage: {percent(validation["coverage_rate"], 2)}
- Duplicate rows: {validation["duplicate_rows"]}

## Observed regime distribution

{regime_lines}

## What this release contains

- `public_overview.json` — campaign totals, public global metrics and data-quality indicators.
- `public_profiles_summary.csv` — one aggregated row per de-identified profile (`PROFILE-XXXXXX`).
- `public_questions_summary.csv` — one aggregate row per de-identified question.
- `public_regime_distribution.csv` — observation-level regime shares and definitions.
- `public_metric_contract.json` — published metric definitions, limitations and excluded private fields.
- `public_manifest.json` — file inventory, integrity information and release provenance.

## What is deliberately not released

Provider and model identifiers, prompts, response content, request IDs, trace IDs,
raw payloads, per-response timestamps, debugging material and the private
profile-mapping registry are not included.

## Important interpretation constraint

The figures published in this release are measurement outputs. They must not be
interpreted as an overall quality ranking, a safety certification, a truth guarantee
or an authorisation to deploy a system in a particular context.

A semantic-variation signal does not, by itself, establish a factual error.
A factual-risk signal is an observed alert requiring contextual interpretation,
not a standalone final judgement.

## Public Release 2.1.0 improvements

This release strengthens the publication workflow through:

- strict validation of systems, questions, repetitions and duplicate observations;
- explicit separation of launched, non-error and fully scored executions;
- stable de-identification through an owner-maintained private profile registry;
- a canonical public metric contract and harmonised aggregate files;
- automatic generation of the release README, provenance manifest and integrity hashes;
- recorded builder, Python and pandas versions;
- automatic cleanup of partial output if generation fails.

These improvements concern release integrity, traceability and consistency.
They do not alter the source runtime observations.

## De-identification

Each observed system is mapped internally to a stable opaque profile identifier
(`PROFILE-XXXXXX`) using an owner-maintained private profile registry.

Identifiers are not assigned according to performance, score, alphabetical order
or rank. The mapping file remains private and is excluded from this release.

## Reproducibility boundary

The public artefacts can be checked for internal consistency using the published
files and integrity information contained in `public_manifest.json`.

Full reproduction from source requires access to the private campaign exports under
the NeoMundi Observatory governance process.
"""
    (output_dir / "README.md").write_text(text, encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def prepare_output_dir(output_dir: Path, overwrite: bool) -> None:
    if output_dir.exists():
        if not overwrite:
            die(
                f"Output directory already exists: {output_dir}. "
                "Use --overwrite to replace it."
            )
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=False)


def public_validation_payload(validation: dict) -> dict:
    private_keys = {
        "prompt_ids_private",
        "rows_per_system_private",
        "rows_per_question_private",
        "repetition_validation_private",
    }
    payload = {
        key: value
        for key, value in validation.items()
        if key not in private_keys
    }
    payload["protocol_shape"] = {
        "expected_systems": EXPECTED_SYSTEMS,
        "expected_questions": EXPECTED_QUESTIONS,
        "expected_repetitions_per_system_question": EXPECTED_REPETITIONS,
        "expected_rows_per_system": EXPECTED_ROWS_PER_SYSTEM,
        "expected_rows_per_question": EXPECTED_ROWS_PER_QUESTION,
        "expected_rows_total": EXPECTED_ROWS_TOTAL,
        "structure_validated": True,
    }
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create the canonical de-identified public NeoMundi "
            "weekly barometer release."
        )
    )
    parser.add_argument(
        "--input-dir",
        required=True,
        type=Path,
        help="Directory holding the 12 private result CSV files.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        type=Path,
        help="New public release directory.",
    )
    parser.add_argument(
        "--campaign-id",
        required=True,
        help=(
            "Public campaign identifier, e.g. "
            "BAROMETER_7_2026-07-27_2026-08-02."
        ),
    )
    parser.add_argument(
        "--period-start",
        required=True,
        help="Public campaign period start, YYYY-MM-DD or ISO-8601.",
    )
    parser.add_argument(
        "--period-end",
        required=True,
        help="Public campaign period end, YYYY-MM-DD or ISO-8601.",
    )
    parser.add_argument(
        "--private-mapping-path",
        required=True,
        type=Path,
        help=(
            "Owner-maintained private profile registry "
            "(provider, profile_id, created_at), outside output-dir."
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace output-dir when it already exists.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_created = False

    try:
        readable_date(args.period_start)
        readable_date(args.period_end)
        barometer_number = extract_barometer_number(args.campaign_id)

        if args.private_mapping_path.resolve().is_relative_to(
            args.output_dir.resolve()
        ):
            die(
                "--private-mapping-path must be outside --output-dir "
                "to prevent accidental public release."
            )

        if not args.input_dir.exists() or not args.input_dir.is_dir():
            die(
                "Input directory does not exist or is not a directory: "
                f"{args.input_dir}"
            )

        prepare_output_dir(args.output_dir, args.overwrite)
        output_created = True

        raw, inventory = load_campaign(args.input_dir)
        validation = validate_campaign(raw, inventory)

        public_df = anonymise_profiles(raw, args.private_mapping_path)
        public_df["observation_regime"] = public_df.apply(
            classify_observation,
            axis=1,
        )

        overview = global_overview(public_df, validation)
        profiles = profile_summary(public_df)
        questions = question_summary(public_df)
        regimes = regime_distribution(public_df)

        write_json(
            overview,
            args.output_dir / "public_overview.json",
        )
        write_csv(
            profiles,
            args.output_dir / "public_profiles_summary.csv",
        )
        write_csv(
            questions,
            args.output_dir / "public_questions_summary.csv",
        )
        write_csv(
            regimes,
            args.output_dir / "public_regime_distribution.csv",
        )
        write_json(
            metric_contract(),
            args.output_dir / "public_metric_contract.json",
        )
        write_readme(
            output_dir=args.output_dir,
            campaign_id=args.campaign_id,
            period_start=args.period_start,
            period_end=args.period_end,
            barometer_number=barometer_number,
            validation=validation,
            regimes=regimes,
            overview=overview,
        )

        script_path = Path(__file__).resolve()
        public_files_before_manifest = sorted(
            path for path in args.output_dir.iterdir() if path.is_file()
        )

        manifest = {
            "schema_version": PUBLIC_SCHEMA_VERSION,
            "campaign_id": args.campaign_id,
            "barometer_number": barometer_number,
            "observation_period": {
                "start": args.period_start,
                "end": args.period_end,
                "start_date": readable_date(args.period_start),
                "end_date": readable_date(args.period_end),
            },
            "release_generated_at_utc": (
                datetime.now(timezone.utc)
                .replace(microsecond=0)
                .isoformat()
            ),
            "builder": {
                "name": BUILDER_NAME,
                "version": BUILDER_VERSION,
                "script_sha256": sha256_file(script_path),
                "python_version": platform.python_version(),
                "pandas_version": pd.__version__,
            },
            "de-identification": {
                "method": (
                    "Owner-maintained private profile registry using opaque "
                    "PROFILE-XXXXXX identifiers. Any exceptional identity "
                    "normalisation is performed in the private preprocessing workflow."
                ),
                "mapping_published": False,
                "ranking_used": False,
                "private_mapping_location": "not published",
            },
            "campaign_validation": public_validation_payload(validation),
            "source_inventory_private": {
                "file_count": len(inventory),
                "row_total": int(
                    sum(item["rows"] for item in inventory)
                ),
                "source_file_names_published": False,
            },
            "public_files": [
                {
                    "name": path.name,
                    "sha256": sha256_file(path),
                    "bytes": path.stat().st_size,
                }
                for path in public_files_before_manifest
            ],
        }

        write_json(
            manifest,
            args.output_dir / "public_manifest.json",
        )

        print(f"Public release written to: {args.output_dir}")
        print(
            "Private mapping registry used (unchanged): "
            f"{args.private_mapping_path}"
        )
        print(
            json.dumps(
                {
                    "barometer_number": barometer_number,
                    "executions": validation["row_count"],
                    "fully_scored": validation["fully_scorable_rows"],
                    "coverage_rate": validation["coverage_rate"],
                    "systems": validation["system_count"],
                    "questions": validation["prompt_count"],
                    "builder_version": BUILDER_VERSION,
                },
                ensure_ascii=False,
            )
        )

    except BaseException:
        if output_created and args.output_dir.exists():
            shutil.rmtree(args.output_dir, ignore_errors=True)
            print(
                f"Partial output removed: {args.output_dir}",
                file=sys.stderr,
            )
        raise


if __name__ == "__main__":
    main()
