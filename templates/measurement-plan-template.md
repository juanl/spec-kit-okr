# Measurement Plan: [FEATURE OR BET TITLE]

- **Feature directory**: [FEATURE_DIR, or "none — readiness mode"]
- **Bet**: okr:[team]/[H-n] — [bet file path]
- **Mode**: full | readiness
- **Created**: [ISO 8601 date]

Definitions and thresholds come from the bet's **Verification Contract** and are not repeated or changed here. This plan says how each contract row gets read.

## Capture

| ID | Captured by | Where | Unit counted | Exists? | Gap |
|----|-------------|-------|--------------|---------|-----|
| [S-n / KR-n / G-n] | event / span / metric / query / vendor report | [file:line, system, or vendor] | [account / user / merchant / transaction] | yes / no | [what to add, or "none"] |

## Dependencies

Rows that depend on another team or a vendor.

| ID | Provided by | Needed by (date) | Status | Fallback if late |
|----|-------------|------------------|--------|------------------|
| [KR-n] | [team or vendor] | [date] | agreed / asked / not asked | [what the verdict can still say without it] |

## Initiative Signals

| Initiative | Signal (S-n) | Moves | Exposure | Expected direction |
|------------|--------------|-------|----------|--------------------|
| [US-n] | [S-n] | KR-n | [who counts as exposed] | up / down |

## Instrumentation Inventory

| Event / span / metric | Properties | Fires when | Feeds | Exists? |
|-----------------------|------------|------------|-------|---------|
| [name] | [prop: type] | [trigger] | [S-n / KR-n / G-n] | yes / no |

## Baseline Capture

- [ ] [ID]: [how and when the baseline is captured — must happen before the change reaches users]

## Rollout & Attribution

- **Strategy**: [A/B test, feature flag cohort, staged rollout, before/after]
- **Why this strategy**: [what it lets us attribute to the change]
- **Sizing**: [inputs and formula, labeled an estimate]
- **Minimum observation period**: [duration before the first scored review]

## Guardrail Monitoring

| ID | Limit (from contract) | Alerting | Action when crossed |
|----|-----------------------|----------|---------------------|
| [G-n] | [limit] | [where, who is paged] | [stop / roll back / review] |

## Dashboard / Report

- **Where**: [link or location]
- **Shows**: [contract rows vs. thresholds, segments]
