---
description: "Bet review after launch: score the KRs, read leading signals and guardrails, and give a verdict on the hypothesis — validated, refuted, or inconclusive — that gates the scale stories"
scripts:
  sh: ../../scripts/bash/check-prerequisites.sh --json --paths-only
  ps: ../../scripts/powershell/check-prerequisites.ps1 -Json -PathsOnly
---

# Bet Review

The spec was built to test a hypothesis. This command reads the evidence and gives the **verdict**: *validated*, *refuted*, *inconclusive*, or *too early*. It then decides what happens next for the spec:

- **scale** the bet (unlock the P2+ stories);
- **iterate** on the validation slice;
- **stop** it.

The verdict feeds the team check-in (`__SPECKIT_COMMAND_OKR_CHECKIN__`).

Run it on each date in the check-in calendar from `measurement-plan.md`.

**First, read `.specify/extensions/okr/docs/okr-sources.md` and follow it.**

## User Input

```text
$ARGUMENTS
```

Current values (e.g. `KR-1=12%, G-3=+14%, US-1=31%`), a pointer to a report, or nothing (then ask). Optional: `feature=<dir>`, `dry-run`.

## Dry run

With `dry-run` in the arguments (a rehearsal, a demo, or hypothetical numbers), run every step and show exactly what would be written, but **write nothing**: no files, no MCP writes. Simulated values must never reach the real OKR sets, bets, or reviews, because every other command would read them as real.

## Setup

1. Run `{SCRIPT}`, or use `feature=…` after validating that it is a real directory under `specs/`. Find the bet via `okr:<team>/H-n`. Read the bet file (its **Verification Contract** holds the definitions and thresholds), `measurement-plan.md`, the team set (KRs, `Drives`, team guardrails), and earlier reviews in `FEATURE_DIR/okr-reviews/`.
2. **No Verification Contract or no `measurement-plan.md`?** Without definitions, thresholds, and observation periods, numbers can't be read consistently. Say so, recommend `__SPECKIT_COMMAND_OKR_MEASURE__`, and only continue if the user provides the missing definitions in the conversation. Record them in the review file. Also check that the instrumentation the numbers need exists in the code (read-only). If it doesn't, ask where the numbers came from before recording anything.
3. Load the scoring config: `scoring.aspirational_target` (0.7), and `scoring.thresholds.persevere` (0.7) / `iterate` (0.4).

## Collect

For each contract row (KR, guardrail, and the signal of each **live** story) without a value, ask for it, one at a time, and show its definition and thresholds from the Verification Contract. Accept "unknown", which means the measurement is broken. Never estimate or invent values.

## Score

- **KR**: `clamp((current − baseline) / (target − baseline), 0, 1)`, rounded to one decimal.
  - **Baseline**: use the recorded one, or the control group when the plan declares a contemporaneous baseline. If neither exists, report `n/a — baseline missing`.
  - **Scorable only when readable**: before the observation period of `measurement-plan.md` has elapsed for at least one full sample, report `n/a — too early`, even if partial numbers exist.
- **Guardrails** (bet and team): **breached** if the limit is crossed. When there is a control group, also compare against it, to tell whether the breach is caused by the feature.
- **Leading signals**: **moved**, **flat**, or **unknown**, against the contract's thresholds (**Validated if** / **Refuted if**) and against the control group if there is one.
- **Thresholds come from the contract.** Never loosen or tighten one during a review. If the user wants to, it becomes a Framing Decision in the bet file, recorded as made *after* seeing the data.

## Verdict on the hypothesis

| Evidence | Verdict |
|----------|---------|
| Validation signals moved, **and** the KR moved directly is scorable and moving (and the KR it drives, once that is readable) | **validated** |
| The bet's **refutation criterion**, computed from the contract rows, is met. For example: the signals moved but the KR stayed flat after the observation period, so the behavior changed without changing the outcome | **refuted** |
| The signals stayed flat after the observation period. This is an adoption or execution problem: the hypothesis wasn't really tested | **inconclusive**. Iterate on the validation slice |
| The KRs needed are not scorable yet | **too early** |
| Measurement is broken | **inconclusive**. Fix the instrumentation first |

**Guardrails override**: any breach (caused by the feature, as far as the control group can tell) means stopping or rolling back the affected stories before anything else, whatever the verdict.

**Per story**: each live story's signal tells whether *that* story does its job. A moved signal means keep it live. A flat one means iterate on it (placement, discoverability, UX). Unknown means fix the measurement first. Because several stories share one KR, a moving KR does not credit any single story.

## Decide

Recommend a decision, give the reasoning, and let the user confirm or override it. Record their decision, not yours.

| Verdict | Spec | Bet / team set |
|---------|------|----------------|
| validated | Unlock the scale stories (P2+), in priority order | Bet `validated`; propose the H-n status update in the team set |
| refuted | Stop the scale stories; decide whether to keep or roll back the validation slice | Bet `refuted`. The learning goes to `__SPECKIT_COMMAND_OKR_FRAME__` for a new hypothesis on the same KR |
| inconclusive | Iterate on the validation slice (a spec change); scale stories stay gated | Bet stays `in_test` |
| too early | No change | No change; schedule the next review |

Also ask once: *What did we learn about the riskiest assumption?*

Check the calendar for commitments that came due without being recorded, such as a one-time recalibration or the end of a holdout. Also look for **deadline conflicts** that appeared because the rollout date slipped. Surface them as decisions. Changing a target is never part of a review: if the user wants to, it becomes a team-set Change Log entry.

## Record

1. Write `FEATURE_DIR/okr-reviews/<YYYY-MM-DD>.md`, and never overwrite one (add `-2` if needed). Include:
   - the scorecard: KRs, guardrails, signals;
   - the verdict and its reasoning;
   - the decision;
   - the learning;
   - follow-ups.
2. **In the bet file**:
   - append a row to **Reviews**;
   - update the **Stories** statuses (`planned` → `live` → `done` / `dropped`);
   - update `Status` for a final verdict.
3. **In the team set**, under its write policy: propose or apply the hypothesis status (`validated` / `refuted`), and add the current KR values for the next team check-in to use.

## Report

A short scorecard, the verdict, the decision, and the next step:

- **validated** → `__SPECKIT_COMMAND_IMPLEMENT__` for the scale stories;
- **refuted** → `__SPECKIT_COMMAND_OKR_FRAME__ kr=KR-n`;
- **inconclusive** → a spec change to the validation slice;
- in every case → the next review date, and `__SPECKIT_COMMAND_OKR_CHECKIN__` if the team check-in is due.

## Guardrails

- Never modify source code or `spec.md`.
- Never change KR targets or deadlines.
- Never write to the team or company set beyond its write policy.
