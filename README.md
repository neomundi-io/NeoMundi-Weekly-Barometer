## 🌐 Choose your language

**[🇬🇧 English](README.md)** · **[🇫🇷 Lire la version française](README.fr.md)**

# NeoMundi Weekly Barometer — Baseline V1

This directory contains the public quantitative reference release for the NeoMundi Weekly Barometer.

It is an anonymized baseline: a fixed starting photograph of observed runtime behaviour across a panel of 12 generative AI systems under repeated measurement conditions. It is **not** a weekly editorial report, a leaderboard, a certification, or a global ranking.

## What this baseline enables

The release fixes recurring indicators that can be compared in subsequent barometers:

- stability;
- factual hallucination signal;
- coherence;
- semantic instability;
- decision behaviour (`ALLOW`, `FLAG`, `ERROR`);
- inter-run variability;
- latency band;
- `delta_g`, reported as an advanced observable runtime-variation signal.

## Files

- `public_profiles_summary.csv` — one quantitative record per pseudonymized profile.
- `public_question_profiles.csv` — quantitative results by profile and question.
- `public_regimes_totals.csv` — direct decision-outcome distribution only. It does not contain artificial rank bins.
- `public_manifest.json` — release metadata and field policy.
- `public_exclusions_and_limitations.csv` — excluded fields and limits of interpretation.
- `METHODOLOGY.md` — concise methodological note.

## Interpretation boundary

A `complete` cell means the planned execution set was completed. Metric-level coverage is reported separately and can be below 100% where an individual metric could not be computed for every observation.

A score of `0.0` is a measured zero when its metric-level `n` is positive. `not_scored` means no valid score was available.

`delta_g` is an observable derived runtime signal. Its publication does not disclose the internal composition, thresholds, weighting logic, or proprietary calculation rules of the NeoMundi measurement framework.

## Anonymization and residual re-identification risk

Provider names, model names, endpoints, prompts, raw responses, detailed traces, precise timestamps and the private mapping are not published.

The protocol and prompt families are reproducible in principle. A third party with comparable API access and experimental conditions may attempt to infer identities. NeoMundi does not publish the mapping and documents this as a residual risk rather than claiming irreversible anonymity.
