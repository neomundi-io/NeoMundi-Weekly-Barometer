# NeoMundi Weekly Barometer #13 -- INSUFFICIENT_COVERAGE

**Standard-schema release, honestly incomplete.** 10 of the 12 official systems
were fully measured this week (4800 executions
launched across all 12, 3981 fully scored,
82.9375% real coverage -- below the mandatory 90%
publication threshold). Two systems (see `comparability_report.json`
`removed_profile_ids`) returned zero usable observations across every
collection attempt; they are absent from every per-system file in this
release, not estimated or backfilled. `public_questions_summary.csv` and
`public_regime_distribution.csv` are computed against the true 4,800-execution
denominator (using the two absent systems' real, archived failed attempts,
not fabricated data), so their totals and shares are internally consistent
with `public_overview.json`. Comparability against Barometer #12 is
`NOT_COMPARABLE`: no numeric delta, trend, or ranking is computed or implied.
Full technical detail: see this campaign's editorial and incident materials.
