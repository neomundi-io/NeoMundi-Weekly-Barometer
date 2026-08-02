#!/usr/bin/env python3
"""Build the public, de-identified data release for a NeoMundi weekly barometer.

The script deliberately exports only aggregated, de-identified measurement data.
It does NOT export provider names, model names, prompts, responses, request IDs,
trace IDs, raw payloads, timestamps per response, or diagnostic payloads.

Usage example:
  python build_public_barometer_release.py \
      --input-dir /path/to/private_csvs \
      --output-dir /path/to/public_release \
      --campaign-id neomundi_barometer_2026_w25 \
      --period-start 2026-06-15 \
      --period-end 2026-06-21 \
      --private-mapping-path /secure/private/profile_mapping_registry.csv

The owner-maintained private profile mapping preserves opaque PROFILE-XXXXXX labels
across weekly releases and is never written into the public output directory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import pandas as pd


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

PUBLIC_SCHEMA_VERSION = "1.0.0"

# Published metrics are intentionally limited to the signals needed for the
# weekly barometer. Metrics known to be flat in a campaign are still described
# in the contract, but can be marked non-discriminating in the overview.
PUBLIC_METRICS = [
    "stability_score",
    "v_score",
    "factual_hallucination_score",
    "semantic_instability_score",
    "coherence_score",
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
    """Round floating output to a documented precision while retaining nulls."""
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return None
    return round(float(value), digits)


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


def validate_campaign(df: pd.DataFrame) -> dict:
    # A public release must detect rather than silently hide unexpected campaign shape.
    systems = (
        df[["provider", "requested_model"]]
        .fillna("<missing>")
        .drop_duplicates()
        .sort_values(["provider", "requested_model"])
    )
    prompt_ids = sorted(df["prompt_id"].dropna().astype(str).unique().tolist())
    duplicate_key = ["provider", "requested_model", "prompt_id", "repetition_index"]
    duplicates = int(df.duplicated(duplicate_key, keep=False).sum())

    metric_complete = df[PUBLIC_METRICS].notna().all(axis=1)
    non_error = df["error"].isna() & df["decision"].fillna("").ne("ERROR")
    fully_scorable = metric_complete & non_error

    return {
        "row_count": int(len(df)),
        "system_count": int(len(systems)),
        "prompt_count": int(len(prompt_ids)),
        "prompt_ids_private": prompt_ids,  # never exported
        "duplicate_rows": duplicates,
        "metric_complete_rows": int(metric_complete.sum()),
        "non_error_rows": int(non_error.sum()),
        "fully_scorable_rows": int(fully_scorable.sum()),
        "incomplete_or_error_rows": int((~fully_scorable).sum()),
        "coverage_rate": fmt(float(fully_scorable.mean()), 6),
    }


def canonical_profile_key(provider: object, model: object) -> str:
    """Resolve a private source row to a registry lookup key.

    The public builder contains no provider-specific or model-specific aliases.
    Any exceptional mapping required to preserve a stable logical identity must
    be handled in the private profile registry or in a private preprocessing step
    before this public builder is executed.

    Provider and model values are used only inside the private execution
    environment and are never written to the public release artefacts.
    """
    del model  # Model-specific aliases are deliberately excluded from public code.
    return str(provider).strip().lower()

def anonymise_profiles(
    df: pd.DataFrame, mapping_path: Path
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Apply the owner-maintained private profile registry exactly as supplied.

    Required registry columns: provider, profile_id, created_at.
    `profile_id` values (e.g. PROFILE-59664C) are stable opaque public labels.
    The function never creates labels, reorders profiles, or uses performance.
    """
    required = {"provider", "profile_id", "created_at"}
    if not mapping_path.exists():
        die(f"Private profile mapping does not exist: {mapping_path}")

    registry = pd.read_csv(mapping_path, dtype=str, encoding="utf-8-sig").fillna("")
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
        lambda r: canonical_profile_key(r["provider"], r["requested_model"]), axis=1
    )
    lookup = dict(zip(registry["provider"], registry["profile_id"], strict=True))
    public_df["profile_id"] = public_df["_registry_provider"].map(lookup)

    unresolved = sorted(public_df.loc[public_df["profile_id"].isna(), "_registry_provider"].dropna().unique())
    if unresolved:
        die(f"Current campaign contains logical profiles absent from private mapping: {unresolved}")

    current_profiles = set(public_df["profile_id"].unique())
    if len(current_profiles) != 12:
        die(f"Expected 12 uniquely mapped public profiles; found {len(current_profiles)}.")

    # Return only the supplied private registry (never copied into public output).
    return public_df, registry

def classify_observation(row: pd.Series) -> str:
    # Priority ordering matters: an incomplete row is not reclassified as normal.
    metric_missing = any(pd.isna(row.get(metric)) for metric in PUBLIC_METRICS)
    if bool(pd.notna(row.get("error"))) or str(row.get("decision", "")) == "ERROR" or metric_missing:
        return "INCOMPLETE_MEASUREMENT"

    semantic = safe_float(row.get("semantic_instability_score")) or 0.0
    factual = safe_float(row.get("factual_hallucination_score")) or 0.0
    decision = str(row.get("decision", ""))
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
    # A deterministic tie-breaker avoids ranking / arbitrary choices.
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


def calculate_dependency_note(df: pd.DataFrame) -> dict:
    complete = df.dropna(subset=["stability_score", "v_score", "factual_hallucination_score"]).copy()
    if complete.empty:
        return {"assessable": False}

    x = complete["v_score"].astype(float)
    y = complete["stability_score"].astype(float)
    z = complete["factual_hallucination_score"].astype(float)

    # OLS y = intercept + slope*x, only used to surface score dependency.
    if x.nunique() <= 1:
        slope = None
        intercept = None
        r2 = None
    else:
        slope, intercept = pd.Series(x).cov(pd.Series(y)) / pd.Series(x).var(), y.mean() - (pd.Series(x).cov(pd.Series(y)) / pd.Series(x).var()) * x.mean()
        y_hat = intercept + slope * x
        ss_res = float(((y - y_hat) ** 2).sum())
        ss_tot = float(((y - y.mean()) ** 2).sum())
        r2 = None if ss_tot == 0 else 1 - ss_res / ss_tot

    return {
        "assessable": True,
        "stability_vs_validity_linear_fit": {
            "intercept": fmt(intercept, 9) if intercept is not None else None,
            "slope": fmt(slope, 9) if slope is not None else None,
            "r_squared": fmt(r2, 9) if r2 is not None else None,
        },
        "validity_plus_factual_risk_max_abs_error": fmt(float((x + z - 1.0).abs().max()), 12),
        "publication_interpretation": (
            "The three values must not be presented as independent confirmations in this campaign. "
            "The public release therefore documents their observed dependency explicitly."
        ),
    }


def profile_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict] = []
    for profile_id, g in df.groupby("profile_id", sort=True):
        scorable = g.dropna(subset=PUBLIC_METRICS).copy()
        non_error = g["error"].isna() & g["decision"].fillna("").ne("ERROR")
        full = g.loc[non_error].dropna(subset=PUBLIC_METRICS).copy()
        n = len(g)
        rows.append(
            {
                "profile_id": profile_id,
                "executions_total": int(n),
                "executions_fully_scored": int(len(full)),
                "coverage_rate": fmt(len(full) / n if n else 0.0),
                "stability_mean": fmt(full["stability_score"].mean() if not full.empty else None),
                "validity_signal_mean": fmt(full["v_score"].mean() if not full.empty else None),
                "factual_risk_mean": fmt(full["factual_hallucination_score"].mean() if not full.empty else None),
                "semantic_variation_rate": fmt((full["semantic_instability_score"].astype(float) > 0).mean() if not full.empty else None),
                "coherence_mean": fmt(full["coherence_score"].mean() if not full.empty else None),
                "flag_rate": fmt((g["decision"] == "FLAG").mean()),
                "error_rate": fmt((g["decision"] == "ERROR").mean()),
                "dominant_regime": dominant_regime(g["observation_regime"]),
            }
        )
    return pd.DataFrame(rows).sort_values("profile_id").reset_index(drop=True)


def question_summary(df: pd.DataFrame) -> pd.DataFrame:
    # Prompt text is never released. The four private prompt IDs are assigned neutral
    # labels in their stable lexical order. No secret or secondary mapping is required.
    prompt_map: dict[str, str] = {}
    unique_prompts = sorted(df["prompt_id"].dropna().astype(str).unique().tolist())
    for idx, prompt in enumerate(unique_prompts, start=1):
        prompt_map[prompt] = f"Question {idx}"

    out = df.copy()
    out["question_id"] = out["prompt_id"].astype(str).map(prompt_map)
    rows: list[dict] = []
    for question_id, g in out.groupby("question_id", sort=True):
        full = g.loc[g["error"].isna() & g["decision"].fillna("").ne("ERROR")].dropna(subset=PUBLIC_METRICS)
        rows.append(
            {
                "question_id": question_id,
                "executions_total": int(len(g)),
                "executions_fully_scored": int(len(full)),
                "coverage_rate": fmt(len(full) / len(g) if len(g) else 0.0),
                "stability_mean": fmt(full["stability_score"].mean() if not full.empty else None),
                "validity_signal_mean": fmt(full["v_score"].mean() if not full.empty else None),
                "factual_risk_mean": fmt(full["factual_hallucination_score"].mean() if not full.empty else None),
                "semantic_variation_rate": fmt((full["semantic_instability_score"].astype(float) > 0).mean() if not full.empty else None),
                "flag_rate": fmt((g["decision"] == "FLAG").mean()),
                "error_rate": fmt((g["decision"] == "ERROR").mean()),
            }
        )
    return pd.DataFrame(rows).sort_values("question_id").reset_index(drop=True)


def regime_distribution(df: pd.DataFrame) -> pd.DataFrame:
    labels = [
        ("NORMAL_SIGNAL", "Normal signal", "No factual alert, semantic-variation signal or incomplete measurement detected."),
        ("SEMANTIC_VARIATION", "Semantic variation", "Semantic-instability signal detected without factual alert."),
        ("FACTUAL_ALERT", "Factual alert", "Non-zero factual-risk signal or FLAG decision without semantic-variation signal."),
        ("COMBINED_ALERT", "Combined alert", "Both factual-alert and semantic-variation signals detected."),
        ("INCOMPLETE_MEASUREMENT", "Incomplete measurement", "Execution error or missing core metric; excluded from fully-scored aggregates."),
    ]
    counts = df["observation_regime"].value_counts(dropna=False).to_dict()
    total = len(df)
    return pd.DataFrame(
        [
            {
                "regime_id": code,
                "regime_label": label,
                "definition": definition,
                "observations": int(counts.get(code, 0)),
                "share_of_all_executions": fmt(counts.get(code, 0) / total if total else 0.0),
            }
            for code, label, definition in labels
        ]
    )


def global_overview(df: pd.DataFrame, validation: dict, dependency: dict) -> dict:
    full = df.loc[df["observation_regime"] != "INCOMPLETE_MEASUREMENT"].dropna(subset=PUBLIC_METRICS)
    unique_values = {metric: int(full[metric].nunique(dropna=True)) for metric in PUBLIC_METRICS}
    non_discriminating = [metric for metric, n in unique_values.items() if n <= 1]

    return {
        "schema_version": PUBLIC_SCHEMA_VERSION,
        "executions_launched": validation["row_count"],
        "executions_fully_scored": validation["fully_scorable_rows"],
        "coverage_rate": validation["coverage_rate"],
        "systems_observed": validation["system_count"],
        "questions_observed": validation["prompt_count"],
        "duplicate_rows_detected": validation["duplicate_rows"],
        "global_metrics": {
            "stability_mean": fmt(full["stability_score"].mean() if not full.empty else None),
            "validity_signal_mean": fmt(full["v_score"].mean() if not full.empty else None),
            "factual_risk_mean": fmt(full["factual_hallucination_score"].mean() if not full.empty else None),
            "semantic_variation_rate": fmt((full["semantic_instability_score"].astype(float) > 0).mean() if not full.empty else None),
            "coherence_mean": fmt(full["coherence_score"].mean() if not full.empty else None),
        },
        "metric_unique_value_counts": unique_values,
        "non_discriminating_metrics": non_discriminating,
        "score_dependency": dependency,
    }


def metric_contract() -> dict:
    return {
        "schema_version": PUBLIC_SCHEMA_VERSION,
        "scope": "Aggregated, de-identified weekly observations. No prompt text, response content, provider name, model name, or raw payload is published.",
        "metrics": [
            {
                "public_name": "stability_mean",
                "source_field": "stability_score",
                "meaning": "Measurement output labelled stability in the source campaign.",
                "unit": "0 to 1",
                "warning": "For this campaign, stability is empirically dependent on v_score. Do not treat both as independent evidence.",
            },
            {
                "public_name": "validity_signal_mean",
                "source_field": "v_score",
                "meaning": "Measurement output labelled v_score in the source campaign.",
                "unit": "0 to 1",
                "warning": "Published as a validity signal, not as an independent certified truth score.",
            },
            {
                "public_name": "factual_risk_mean",
                "source_field": "factual_hallucination_score",
                "meaning": "Measurement output for factual-risk / hallucination signal.",
                "unit": "0 to 1",
                "warning": "For this campaign, factual risk is the observed inverse of v_score.",
            },
            {
                "public_name": "semantic_variation_rate",
                "source_field": "semantic_instability_score",
                "meaning": "Share of fully-scored observations with a non-zero semantic-instability signal.",
                "unit": "proportion",
                "warning": "A semantic variation signal is not itself a factual-error finding.",
            },
            {
                "public_name": "coherence_mean",
                "source_field": "coherence_score",
                "meaning": "Measurement output labelled internal coherence.",
                "unit": "0 to 1",
                "warning": "If the field is flat for a campaign, it is disclosed as non-discriminating rather than interpreted.",
            },
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
    df.to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def write_json(payload: object, path: Path) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_readme(output_dir: Path, campaign_id: str, period_start: str, period_end: str) -> None:
    text = f"""# NeoMundi Weekly Barometer — Public Data Release

**Campaign:** `{campaign_id}`  
**Observation period:** {period_start} to {period_end}  
**Publication form:** aggregated and de-identified

## What this release contains

- `public_overview.json` — campaign totals, global metrics, data-quality and dependency disclosures.
- `public_profiles_summary.csv` — one aggregated row per de-identified profile (`PROFILE-XXXXXX`).
- `public_questions_summary.csv` — one aggregate row per de-identified question.
- `public_regime_distribution.csv` — observation-level regime shares and definitions.
- `public_metric_contract.json` — published metric definitions, limitations and excluded private fields.
- `public_manifest.json` — file inventory and release provenance.

## What is deliberately not released

Provider/model identifiers, prompts, response content, request IDs, trace IDs, raw payloads,
per-response timestamps and debugging material are not included.

## Important interpretation constraint

For this campaign, the release documents an observed dependency among `stability_score`,
`v_score` and `factual_hallucination_score`. These figures must not be treated as independent
confirmations. The purpose of the release is to expose this limitation rather than conceal it.

## Anonymisation

Each observed system is mapped internally to a stable opaque profile identifier (`PROFILE-XXXXXX`)
using an owner-maintained private profile registry. Identifiers are not assigned by performance, score, alphabetical order,
or rank. The mapping file is private and excluded from this release.

## Reproducibility boundary

The public artefacts can be checked for internal consistency. Reproduction from source requests
access to the private campaign exports under the Observatory's governance process.
"""
    (output_dir / "README.md").write_text(text, encoding="utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def prepare_output_dir(output_dir: Path, overwrite: bool) -> None:
    if output_dir.exists():
        if not overwrite:
            die(f"Output directory already exists: {output_dir}. Use --overwrite to replace it.")
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a de-identified public NeoMundi barometer release.")
    parser.add_argument("--input-dir", required=True, type=Path, help="Directory holding private result CSV files.")
    parser.add_argument("--output-dir", required=True, type=Path, help="Empty/new public release directory.")
    parser.add_argument("--campaign-id", required=True, help="Public campaign identifier, e.g. neomundi_barometer_2026_w25.")
    parser.add_argument("--period-start", required=True, help="Public campaign period start, YYYY-MM-DD.")
    parser.add_argument("--period-end", required=True, help="Public campaign period end, YYYY-MM-DD.")
    parser.add_argument("--private-mapping-path", required=True, type=Path, help="Owner-maintained private profile registry (provider, profile_id, created_at), outside output-dir.")
    parser.add_argument("--overwrite", action="store_true", help="Replace output-dir when it already exists.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.private_mapping_path.resolve().is_relative_to(args.output_dir.resolve()):
        die("--private-mapping-path must be outside --output-dir to prevent accidental public release.")
    if not args.input_dir.exists() or not args.input_dir.is_dir():
        die(f"Input directory does not exist or is not a directory: {args.input_dir}")

    prepare_output_dir(args.output_dir, args.overwrite)
    raw, inventory = load_campaign(args.input_dir)
    validation = validate_campaign(raw)

    # Guardrail: fail early rather than accidentally publish a malformed campaign.
    if validation["system_count"] != 12:
        die(f"Expected 12 systems; found {validation['system_count']}.")
    if validation["prompt_count"] != 4:
        die(f"Expected 4 questions; found {validation['prompt_count']}.")
    if validation["row_count"] != 4800:
        die(f"Expected 4,800 rows; found {validation['row_count']}.")
    if validation["duplicate_rows"]:
        die(f"Duplicate provider/model/prompt/repetition rows detected: {validation['duplicate_rows']}.")

    public_df, private_mapping = anonymise_profiles(raw, args.private_mapping_path)
    public_df["observation_regime"] = public_df.apply(classify_observation, axis=1)

    dep = calculate_dependency_note(public_df)
    overview = global_overview(public_df, validation, dep)
    profiles = profile_summary(public_df)
    questions = question_summary(public_df)
    regimes = regime_distribution(public_df)

    # Public files only.
    write_json(overview, args.output_dir / "public_overview.json")
    write_csv(profiles, args.output_dir / "public_profiles_summary.csv")
    write_csv(questions, args.output_dir / "public_questions_summary.csv")
    write_csv(regimes, args.output_dir / "public_regime_distribution.csv")
    write_json(metric_contract(), args.output_dir / "public_metric_contract.json")
    write_readme(args.output_dir, args.campaign_id, args.period_start, args.period_end)

    # The supplied private mapping is authoritative and is never modified or copied.

    # Manifest hashes only public release files, and never source names or provider identities.
    public_files = sorted(p for p in args.output_dir.iterdir() if p.is_file())
    manifest = {
        "schema_version": PUBLIC_SCHEMA_VERSION,
        "campaign_id": args.campaign_id,
        "observation_period": {"start": args.period_start, "end": args.period_end},
        "release_generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "de-identification": {
            "method": "Owner-maintained private profile registry; opaque PROFILE-XXXXXX identifiers. Explicit model-family aliases resolve logical system identities.",
            "mapping_published": False,
            "ranking_used": False,
            "private_mapping_location": "not published",
        },
        "campaign_validation": {
            key: value for key, value in validation.items() if key != "prompt_ids_private"
        },
        "source_inventory_private": {
            "file_count": len(inventory),
            "row_total": int(sum(item["rows"] for item in inventory)),
            "source_file_names_published": False,
        },
        "public_files": [
            {"name": p.name, "sha256": sha256_file(p), "bytes": p.stat().st_size}
            for p in public_files
        ],
    }
    write_json(manifest, args.output_dir / "public_manifest.json")

    print(f"Public release written to: {args.output_dir}")
    print(f"Private mapping registry used (unchanged): {args.private_mapping_path}")
    print(json.dumps({
        "executions": validation["row_count"],
        "fully_scored": validation["fully_scorable_rows"],
        "coverage_rate": validation["coverage_rate"],
        "systems": validation["system_count"],
        "questions": validation["prompt_count"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
