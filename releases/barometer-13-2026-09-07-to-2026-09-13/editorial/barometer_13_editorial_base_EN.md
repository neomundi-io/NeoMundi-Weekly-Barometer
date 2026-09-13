# AI Barometer #13 — insufficient-coverage edition

*Exceptional edition — September 7–13, 2026 (UTC) — status: INSUFFICIENT_COVERAGE*

> **This week, 10 of 12 systems were fully observed. Two feeds did not provide usable coverage. NeoMundi publishes the measured state without completing, masking, or extrapolating the missing data.**

## Why this edition is different

The standard NeoMundi AI Barometer only publishes when at least 90% of the planned measurements across all 12 systems are fully scored. This week, real coverage across all 12 systems is **82.9%** (3,981 fully-scored observations out of 4,800 planned). That threshold was not lowered or bypassed: the standard Barometer #13 release stays blocked.

## What was measured

10 of the 12 official systems produced a complete, usable observation: 400/400 planned executions each, with individual coverage between 99.0% and 100%. These 10 systems account for 4,000 of the 4,800 planned observations. All figures below cover **only these 10 measured systems** — no 12-system aggregate is presented as valid in this edition.

| Metric | Value (10 measured systems) |
|---|---|
| Executions launched | 4,000 |
| Fully scored executions | 3,981 |
| Coverage (10 systems) | 99.53% |

Per-system and per-question detail: `public_profiles_summary.csv`, `public_questions_summary.csv`, `public_regime_distribution.csv`.

## What could not be measured

Two official systems produced **zero usable observations** for the entire collection window: every attempt failed with the exact same technical error, on 100% of attempted requests, across four separate collection attempts — including after rotating the API credentials to rule out an expired or invalid key.

These two systems are marked **`insufficient_data`** in the public 12-system table (`public_systems_status.csv`) — not measured, not estimated, not backfilled. No historical value, no average from other systems, and no extrapolation was used to fill the gap: the 800 planned observations for these two systems remain **absent (null)**.

Full factual detail (affected endpoint, exact error message, attempt timeline, resolution status) is in the separate incident note and in `incident_report.json`.

## Comparability with Barometer #12

**Status: `NOT_COMPARABLE`.** Barometer #12 measured 12/12 systems; this edition measures 10/12. No numeric delta, trend, or ranking is computed or implied between the two editions.

## Methodological limits of this edition

- No imputation, no substitute data, no historical carry-over.
- No global (12-system) aggregate metric.
- No conclusion about general reliability or a provider ranking.
- Missing values for the two affected systems stay null, never estimated.
- This edition is structurally separate from the standard release series.

## Next steps

The standard Barometer #13 release stays pending, to be published once 12-system coverage reaches 90% after the technical incident is resolved. Barometer #14 will then follow the normal scientific chain, with the same unmodified 90% threshold.

---

*Read these figures alongside their coverage and the methodological reservations above. Full technical detail: `incident_report.json`, `public_manifest.json`, `public_systems_status.csv`.*
