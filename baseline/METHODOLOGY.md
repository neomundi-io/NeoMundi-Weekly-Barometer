# Methodology — Baseline V1

## Design

- 12 pseudonymized profiles;
- 4 fixed questions;
- 3 execution runs;
- 100 planned repetitions per profile × question × run;
- 14,400 planned observations in the private baseline corpus.

The public release reports aggregate quantitative measurements and observed coverage. It excludes direct identities and sensitive raw execution artefacts.

## Public indicator families

1. **Stability** — observed repeatability under repeated measurement.
2. **Factual hallucination signal** — protocol-specific factual fragility signal; not a universal truth score.
3. **Coherence** — observed internal coherence signal.
4. **Semantic instability** — variation observed across repeated outputs.
5. **Decision behaviour** — `ALLOW`, `FLAG`, and `ERROR` distribution.
6. **Inter-run variability** — mean standard deviation of run-level stability means across the four questions.
7. **Latency band** — coarse operational category; exact latency statistics remain outside this public release.
8. **delta_g** — advanced observable runtime-variation signal; internal calculation composition is not disclosed.

## Coverage and remediation

`complete` means the planned execution count was reached.
`remediated_complete` means missing planned observations were later re-executed and the remediation count is reported.
`partial` means fewer observations than planned were available.
`not_scored` applies to a metric with no valid score.

Metric-level `n` and coverage are published independently from execution-level coverage.

## No ranking policy

This release does not order profiles from best to worst. It publishes observed measurements and distributional information only.
