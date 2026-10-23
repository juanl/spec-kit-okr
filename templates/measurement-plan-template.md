# Measurement Plan: [FEATURE TITLE]

- **Feature directory**: [FEATURE_DIR]
- **OKR framing**: [FEATURE_DIR/okr.md]
- **Created**: [ISO 8601 date]

## Metric Definitions

### KR-1: [Key Result]

- **Metric**: [name]
- **Definition**: [exact formula: numerator / denominator, filters, unit]
- **Population**: [who is counted, who is excluded]
- **Window**: [rolling 7 days, per cohort, per month…]
- **Baseline**: [value, date, and how it was obtained — or the task that will capture it before launch]
- **Target**: [value by date]
- **Data source**: [table, analytics tool, log, survey]
- **Instrumentation needed**: [events/properties to add, or "none — already tracked"]
- **Owner**: [role]
- **Review cadence**: [weekly / bi-weekly / at deadline]

## Initiative Signals

| Initiative | Moves | Leading signal | Definition | Exposure | Event | Expected direction |
|------------|-------|----------------|------------|----------|-------|--------------------|
| [US-n] | KR-n | [signal] | [formula] | [who counts as exposed] | [event_name] | up / down |

## Guardrails

| ID | Metric | Definition | Limit | Alerting |
|----|--------|------------|-------|----------|
| G-1 | | | | |

## Instrumentation Inventory

| Event / Signal | Properties | Fires when | Feeds | Exists? |
|----------------|------------|------------|-------|---------|
| [event_name] | [prop: type] | [trigger] | KR-1 / US-n signal | yes / no |

## Baseline Capture

- [ ] [KR-n]: [how and when the baseline is captured — must happen before the feature reaches users]

## Rollout & Attribution

- **Strategy**: [A/B test, feature flag cohort, staged rollout, before/after]
- **Why this strategy**: [what it lets us attribute to the feature]
- **Minimum observation period**: [duration before the first scored check-in]

## Dashboard / Report

- **Where**: [link or location]
- **Shows**: [KRs vs. targets, guardrails, segments]
