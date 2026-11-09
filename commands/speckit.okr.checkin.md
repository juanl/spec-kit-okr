---
description: "Team OKR check-in: roll up bet reviews, update KR values and statuses, show the impact on company KRs, flag stale or orphaned work, close a period"
---

# OKR Check-in (team)

Keep the team OKR set alive. This command:

- records current KR values;
- rolls up what the bets learned (from `__SPECKIT_COMMAND_OKR_REVIEW__`);
- proposes a status for each KR;
- shows what the team's results mean for the company KRs they contribute to, and flags orphaned hypotheses and specs.

There is no company check-in: the company OKRs are read-only context (see the shared docs).

`__SPECKIT_COMMAND_OKR_REVIEW__` judges one bet. This command judges the set.

**First, read `.specify/extensions/okr/docs/okr-sources.md` and follow it.**

## User Input

```text
$ARGUMENTS
```

Arguments (all optional): `team=<id>`, `period=<id>`, `close` (final check-in of the period), `dry-run`, current values (`KR-1=34%, KR-2=18`), or a pointer to a report.

## Dry run

With `dry-run` in the arguments (a rehearsal, a demo, or hypothetical numbers), run every step and show exactly what would be written, but **write nothing**: no files, no MCP writes. Simulated values must never reach the real OKR sets, bets, or reviews, because every other command would read them as real.

## Setup

1. Resolve the team, period, source, and write policy. For `mcp` sources, read the set through the `read` tool and refresh the mirror.
2. Read the team set, every bet file under `teams/<team>/bets/`, and the latest review of every spec that references a hypothesis (`okr:<team>/<H-n>`). Also read the company OKRs (read-only), for the ladder and down-propagation.

## Collect

For each KR without a value in the input, ask for it, one at a time, and show its metric definition. Accept "unknown", which is a finding in itself. Never estimate or invent a current value.

## Roll up

For each KR:

1. Compute its score: `clamp((current − baseline) / (target − baseline), 0, 1)`, rounded to one decimal. If the baseline is unknown, report `n/a`.
2. List its hypotheses with their status and their latest bet verdict (*validated*, *refuted*, *inconclusive*, *in_test*).
3. Propose a status:

   | Situation | Proposed status |
   |-----------|-----------------|
   | Target reached | `done` |
   | Score on pace for the deadline (score ≥ share of the period elapsed) | `on_track` |
   | Behind pace, but a bet is in test or validated and scaling, with time left to close the gap | `at_risk` |
   | Behind pace, and every hypothesis is refuted, none exists, or there is no time left to close the gap | `off_track`. Recommend framing a new hypothesis |

   A validated bet never makes a KR `on_track` by itself: the score decides. **At period close (`close`)**, the status is `done` when the target is reached and `missed` otherwise. Record what the validated bets imply for the next period under Period Close.

4. KR chains (`Drives`): if a leading KR is on track but the lagging KR it drives is flat after the observation period, flag the chain. The leading KR may be measuring the wrong thing.

## Propagate

- **Company impact**: for each company KR the team contributes to, one line on what the team's results mean for it ("C-KR-2: the reporting team's KR-1 is off track after H-3 was refuted"). A weak ladder found during the roll-up goes here too. Record these as **Company Impact Notes** in the team set, for the team to take to whoever owns the company OKRs. Never write to the company OKRs.
- **Down**: run the orphan checks from the shared docs, and list each orphan with a recommendation (re-frame it against another KR, pause the spec, or close the bet).

## Decide and record

Present proposed statuses, company impact notes, and orphans in one table. Ask once: **apply all / choose / none**. Then write, according to the level's write policy:

- the KR values, scores, and statuses;
- a row in **Check-in History**;
- `Last check-in: <today>`;
- hypothesis statuses confirmed from bet reviews, never changed beyond what the bet reviews say;
- company impact notes.

**With `close`**: also fill **Period Close**:

- the final score of each KR;
- learnings from validated and refuted hypotheses;
- carry-over: each open hypothesis goes to the next period or gets closed, as the user decides.

Then set `Status: closed`. Do not create the next period's set; recommend `__SPECKIT_COMMAND_OKR_SET__ period=<next>` instead.

## Report

```markdown
## OKR check-in — <team> <period> — <date>

| KR | Score | Status (was → now) | Hypotheses |
|----|-------|--------------------|------------|

**Company impact**: <C-KR-n: one line each> · **Orphans**: <n> · **Stale bets** (no review in > cadence): <n>
**Next check-in**: <date>
```

## Guardrails

- Never modify source code, specs, or bet files. Bets change only through `__SPECKIT_COMMAND_OKR_REVIEW__` and `__SPECKIT_COMMAND_OKR_FRAME__`.
- Never change targets or deadlines here. That is a `__SPECKIT_COMMAND_OKR_SET__` change, with a Change Log entry.
- Never write to the company OKRs, through files or MCP.
