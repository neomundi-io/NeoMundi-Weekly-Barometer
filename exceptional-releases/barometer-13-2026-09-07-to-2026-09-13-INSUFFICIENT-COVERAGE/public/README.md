# NeoMundi Weekly Barometer #13 — EXCEPTIONAL EDITION (INSUFFICIENT_COVERAGE)

**This is not a standard Barometer release.** The standard, fully-gated release
for Barometer 13 remains blocked: global fully-scored coverage across the 12
official systems is 82.9375%, below the mandatory 90% publication
threshold. That threshold was not lowered, bypassed, or modified to produce
this edition.

## What this edition is

- BAROMETER_13_2026-09-07_2026-09-13, observation period 2026-09-07 to 2026-09-13 (UTC).
- 10 of the 12 official systems were fully, successfully observed (400/400 planned
  executions each, launched and structurally complete).
- 2 systems (see `incident_report.json`) returned zero usable observations across
  every collection attempt and are marked `insufficient_data` — not measured,
  not estimated, not backfilled.
- `public_systems_status.csv` lists all 12 registered profiles with their status.
- `public_profiles_summary.csv`, `public_questions_summary.csv` and
  `public_regime_distribution.csv` are computed **only** over the 10 measured
  systems (4,000 observations). They are descriptive, per-system/per-question
  figures, not a blended global metric.

## What this edition is not

- It is **not** comparable to a standard 12-system release. `comparability_report.json`
  is hardcoded `NOT_COMPARABLE` against Barometer 12; no delta, trend, or ranking is
  computed or implied anywhere in this edition.
- No missing value was imputed, estimated, or replaced by historical data. Absent
  observations for the 2 affected systems are simply absent (null), not zero, not
  averaged, not carried over.
- No global (all-12-systems) aggregate metric (e.g. a single stability mean) is
  published here, precisely because it would misrepresent 2 systems with no data
  as if they contributed a neutral or average signal.

## De-identification

Same method as every standard release: an owner-maintained private registry maps
each system to an opaque `PROFILE-XXXXXX` identifier. The mapping itself is never
published, including for the 2 systems marked `insufficient_data`.

## Files

- `public_manifest.json` — edition metadata and file hashes.
- `public_overview.json` — coverage facts (12-system and 10-system scopes, kept distinct).
- `public_systems_status.csv` — all 12 profiles, `measured` or `insufficient_data`.
- `public_profiles_summary.csv`, `public_questions_summary.csv`, `public_regime_distribution.csv` — 10-system descriptive figures.
- `public_metric_contract.json` — unchanged methodology contract (same as every release).
- `comparability_report.json` — hardcoded `NOT_COMPARABLE`.
- `incident_report.json` — factual record of the `/v1/govern/stream` incident affecting the 2 excluded systems.

## Reading this edition responsibly

Read every figure alongside `public_systems_status.csv` and `incident_report.json`.
Any comparison to a prior Barometer, or any claim of a general trend or provider
ranking, is outside what this edition supports.
