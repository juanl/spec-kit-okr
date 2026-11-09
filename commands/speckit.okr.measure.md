---
description: "Make the bet readable on launch day: turn the bet's verification contract into sources, instrumentation, baselines, attribution, and a check-in calendar fed into plan.md (or a readiness check before the plan exists)"
scripts:
  sh: ../../scripts/bash/check-prerequisites.sh --json --paths-only
  ps: ../../scripts/powershell/check-prerequisites.ps1 -Json -PathsOnly
handoffs:
  - label: Generate Tasks
    agent: speckit.tasks
    prompt: Break the plan into tasks, including the measurement and instrumentation work
---

# Plan the Measurement of a Bet

A hypothesis that can't be read on launch day can't be validated or refuted. The bet's **Verification Contract** (written by `__SPECKIT_COMMAND_OKR_FRAME__`) already says *what* to read: the definition, source, baseline, and thresholds of every number the verdict depends on. This command plans *how* to read each one:

- where the number is captured, and the instrumentation still missing;
- how the baseline is captured before exposure;
- how the effect is attributed to the change;
- whether the verdict fits before the KR deadline;
- the calendar of reviews.

It writes `measurement-plan.md` and adds a section to `plan.md`, so that `__SPECKIT_COMMAND_TASKS__` generates the tasks.

**First, read `.specify/extensions/okr/docs/okr-sources.md` and follow it.** The verification card and statistics rules in `.specify/extensions/okr/docs/interview-and-kr-quality.md` also apply.

## User Input

```text
$ARGUMENTS
```

Optional: `bet=H-n` (readiness mode without a spec), `team=<id>`.

## Setup

1. Run `{SCRIPT}` from the repo root and parse `FEATURE_DIR`, `FEATURE_SPEC`, and `IMPL_PLAN`. If there is no feature yet but `bet=H-n` is given, use **readiness mode** (below).
2. Find the bet via the `okr:<team>/H-n` token in the spec. If there is none, stop and point to `__SPECKIT_COMMAND_OKR_ALIGN__`. Read the bet file (its **Verification Contract** first), the team set (KR definitions, `Drives`, team guardrails), and `plan.md`.
3. **No Verification Contract, or rows without definitions?** (bets framed before it existed). Fill it now with the verification card from the shared docs, at most 5 questions, and write it to the bet file. This is the only case where this command defines numbers.
4. If the plan already defines analytics or observability contracts (e.g. `contracts/analytics-events.md`), **extend them rather than creating a parallel definition**.

## Readiness mode

Without `plan.md` (or without a spec, with `bet=H-n`), plan only what does not depend on the solution: sources, baselines, attribution, verdict window, and blockers. Write `measurement-plan.md` next to the spec, or `teams/<team>/bets/H-n-<slug>.measurement.md` when there is no spec. Recommend re-running this command after `__SPECKIT_COMMAND_PLAN__` to add the instrumentation.

## Discover (read-only)

Look for where each number can already be read, not only in product analytics:

- **Product analytics**: SDKs and event calls (`track(`, `logEvent(`, PostHog, Segment, Amplitude, Mixpanel, GA), event catalogs and tracking plans.
- **Observability**: APM and tracing (OpenTelemetry spans and metrics, Datadog, New Relic, Grafana, Prometheus), structured logs, dashboards and alert definitions in the repo.
- **Data**: database tables and queries, BI models, data-lake jobs.
- **Third parties**: APIs, webhooks, or reports from a vendor the number depends on. A third-party row is a **dependency** in the plan (who provides it, by when), not an instrumentation task.
- **Experimentation**: feature-flag and rollout tooling, which decides the attribution options.
- **Identity**: what the events or spans use as the unit (account, user, merchant, transaction). A KR measured per user needs per-user data.

Reuse the existing naming conventions.

## Build the plan

For each row of the Verification Contract:

1. **Definition**: take it from the contract. If the code or the data shows that the definition can't be computed as written (wrong unit, missing field, ambiguous population), say so, propose the closest computable definition, and record the change as a Framing Decision in the bet file once the user agrees. A changed definition invalidates the recorded baseline: mark it for re-measurement, or declare a control group as a *contemporaneous baseline*.
2. **Capture**: the event, span, metric, query, or report that produces the number, or "already captured at <file:line | system>". For `blocked` rows, the dependency, its owner, and the date it is needed by.
3. **Baseline capture**: how and when it gets captured. It must happen **before** exposure.
4. **Attribution**: recommend the strongest strategy the existing tooling supports (A/B, holdout by account, staged rollout, or before/after with a caveat). Size it to the volume (ask for the volume if unknown), show the inputs and the formula, and state the observation period this implies.
5. **Deadline check**: `rollout start + baseline lead time + observation period ≤ KR deadline`. A **deadline conflict** is a finding: propose moving the deadline (a team-set Change Log entry, under its write policy) or changing the rollout. If the rollout date is unknown, compute **the latest rollout date that keeps each KR readable**.
6. **Refutation readability**: the bet's **Refuted if** must be computable from the planned data. If it is not, say so, and name the row that breaks it.

Update **Measurable today?** in the contract when this changes it (e.g. `instrument` → `yes` once the plan covers it). Never change a threshold here: that is a Framing Decision.

Resolve `measurement-plan-template` through the template stack, and write `measurement-plan.md`. Put each story's leading signal in its **Initiative Signals** table, using the contract's `S-n` IDs.

## Feed the plan

Add or update this section in `plan.md`:

```markdown
## Measurement & Instrumentation

See [measurement-plan.md](./measurement-plan.md). Part of the Definition of Done; the validation slice cannot ship before the baselines exist.

- **Instrumentation**: <events, spans, metrics, or queries, each with the contract ID it feeds>
- **Dependencies**: <blocked rows: who provides the number, by when>
- **Baseline capture**: <what, how, deadline before exposure>
- **Rollout / attribution**: <strategy, size, observation period>
- **Guardrail monitoring**: <G-n → limit → action>
- **Check-in calendar**: <dated list, or one relative to the rollout date:>
  - baseline-capture deadline;
  - rollout;
  - each bet review;
  - any one-time recalibration;
  - holdout end;
  - the KR deadline;
  - the team check-in that will consume the verdict.
```

## Report

```markdown
## Measurement plan — <feature or bet> (okr:<team>/H-n)

**Mode**: full | readiness
**Readable at launch**: <n>/<n> contract rows (S: <n>/<n> · KR: <n>/<n> · G: <n>/<n>)
**Blocked**: <ID — who unblocks it — by when>, or none
**Refutation criterion computable**: yes | no (<row that breaks it>)
**Attribution**: <strategy> · **Observation**: <duration> at <volume>/week (<formula>)
**Deadline conflicts**: <n> · **Latest rollout date**: <date>
**plan.md updated**: yes | no

**Next**: __SPECKIT_COMMAND_TASKS__. After launch, run __SPECKIT_COMMAND_OKR_REVIEW__ on each date in the check-in calendar.
```

## Guardrails

- Never modify source code. This command plans instrumentation; implementing it is the job of `__SPECKIT_COMMAND_IMPLEMENT__`.
- Never change a contract threshold; definitions change only as a Framing Decision the user agreed to.
- Flag any personal data in event properties or log fields, and any consent or retention implications.
- Never mark a number as readable if its baseline cannot be captured before exposure.
