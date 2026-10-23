---
description: "Make the bet readable on launch day: metric definitions, leading signals, instrumentation, baselines, attribution, feasibility, and a check-in calendar fed into plan.md"
scripts:
  sh: ../../scripts/bash/check-prerequisites.sh --json --paths-only
  ps: ../../scripts/powershell/check-prerequisites.ps1 -Json -PathsOnly
handoffs:
  - label: Generate Tasks
    agent: speckit.tasks
    prompt: Break the plan into tasks, including the measurement and instrumentation work
---

# Plan the Measurement of a Bet

A hypothesis that can't be read on launch day can't be validated or refuted. This command covers every number the bet depends on:

- the KR it moves, and the KR that one drives;
- the leading signal of each story;
- the guardrails of the bet and of the team.

For each one it produces an exact definition, a data source, the instrumentation still missing, a baseline captured before launch, an attribution strategy, and a calendar. It adds all of that to `plan.md`, so that `__SPECKIT_COMMAND_TASKS__` generates the tasks.

**First, read `.specify/extensions/okr/docs/okr-sources.md` and follow it.** The statistics rule in `.specify/extensions/okr/docs/interview-and-kr-quality.md` also applies.

## User Input

```text
$ARGUMENTS
```

## Setup

1. Run `{SCRIPT}` from the repo root and parse `FEATURE_DIR`, `FEATURE_SPEC`, and `IMPL_PLAN`.
2. Find the bet via the `okr:<team>/H-n` token in the spec. If there is none, stop and point to `__SPECKIT_COMMAND_OKR_ALIGN__`. Read the bet file, the team set (KR definitions, `Drives`, team guardrails), and `plan.md`. Without a plan, write only `measurement-plan.md` and recommend re-running this command after `__SPECKIT_COMMAND_PLAN__`.
3. If the plan already defines analytics contracts (e.g. `contracts/analytics-events.md`), **extend them rather than creating a parallel definition**.

## Discover (read-only)

Look in the codebase for existing measurement capability:

- analytics SDKs and event calls (`track(`, `logEvent(`, PostHog, Segment, Amplitude, Mixpanel, GA, OpenTelemetry metrics);
- event catalogs and tracking plans;
- feature-flag and experimentation tooling;
- identity: what the events use as the distinct id (account vs. user). A KR measured per user needs per-user events.

Reuse the existing naming conventions.

## Build the plan

For each KR, guardrail, and leading signal:

1. **Definition**: exact formula (numerator / denominator, filters, unit, window, population). If two readings are possible, ask which one is meant, with a recommended answer (at most 5 questions in total, in the same format as `__SPECKIT_COMMAND_CLARIFY__`). When the chosen definition differs from the one the recorded baseline used, the baseline is invalid: mark it for re-measurement, or declare a control group as a *contemporaneous baseline*.
2. **Source** and **instrumentation**: the event or property to add, or "already tracked at <file:line>".
3. **Baseline capture**: how and when it gets captured. It must happen **before** exposure.
4. **Attribution**: recommend the strongest strategy the existing tooling supports (A/B, holdout by account, staged rollout, or before/after with a caveat). Size it to the volume (ask for the volume if unknown), show the inputs and the formula, and state the observation period this implies.
5. **Deadline check**: `rollout start + baseline lead time + observation period ≤ KR deadline`. A **deadline conflict** is a finding: propose moving the deadline (a team-set Change Log entry, under its write policy) or changing the rollout. If the rollout date is unknown, compute **the latest rollout date that keeps each KR readable**.
6. **Refutation readability**: the bet's refutation criterion must be computable from the planned data. If it is not, say so.

Resolve `measurement-plan-template` through the template stack, and write `FEATURE_DIR/measurement-plan.md`. Put the leading signals in its **Initiative Signals** table, one row per story.

## Feed the plan

Add or update this section in `plan.md`:

```markdown
## Measurement & Instrumentation

See [measurement-plan.md](./measurement-plan.md). Part of the Definition of Done; the validation slice cannot ship before the baselines exist.

- **Instrumentation**: <events and properties, each with the KR, guardrail, or signal it feeds>
- **Baseline capture**: <what, how, deadline before exposure>
- **Rollout / attribution**: <strategy, size, observation period>
- **Guardrail monitoring**: <metric → limit → action>
- **Check-in calendar**: <dated list, or one relative to the rollout date:>
  - baseline-capture deadline;
  - rollout;
  - each bet review;
  - any one-time recalibration;
  - holdout end;
  - the KR deadline;
  - the team check-in that will consume the verdict.
```

Update the bet file's **Measurement Readiness** table.

## Report

```markdown
## Measurement plan — <feature> (okr:<team>/H-n)

**Readable at launch**: KRs <n>/<n> · signals <n>/<n> · guardrails <n>/<n>
**Refutation criterion computable**: yes | no (<why>)
**Attribution**: <strategy> · **Observation**: <duration> at <volume>/week (<formula>)
**Deadline conflicts**: <n> · **Latest rollout date**: <date>
**plan.md updated**: yes | no

**Next**: __SPECKIT_COMMAND_TASKS__. After launch, run __SPECKIT_COMMAND_OKR_REVIEW__ on each date in the check-in calendar.
```

## Guardrails

- Never modify source code. This command plans instrumentation; implementing it is the job of `__SPECKIT_COMMAND_IMPLEMENT__`.
- Flag any personal data in event properties, and any consent or retention implications.
- Never mark a number as readable if its baseline cannot be captured before exposure.
