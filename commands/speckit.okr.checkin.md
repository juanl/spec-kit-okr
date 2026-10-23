---
description: "Team or company OKR check-in: roll up bet reviews, update KR values and statuses, flag stale or orphaned work, close a period"
---

# OKR Check-in (team or company)

Keep a team or company OKR set alive. This command:

- records current KR values;
- rolls up what the bets learned (from `__SPECKIT_COMMAND_OKR_REVIEW__`);
- proposes a status for each KR;
- propagates changes up (team → company proposals) and down (orphaned hypotheses and specs).

`__SPECKIT_COMMAND_OKR_REVIEW__` judges one bet. This command judges the set.

**First, read `.specify/extensions/okr/docs/okr-sources.md` and follow it.**

## User Input

```text
$ARGUMENTS
```

Arguments (all optional): `level=team|company` (default `team`), `team=<id>`, `period=<id>`, `close` (final check-in of the period), `dry-run`, current values (`KR-1=34%, KR-2=18`), or a pointer to a report.

## Dry run

With `dry-run` in the arguments (a rehearsal, a demo, or hypothetical numbers), run every step and show exactly what would be written, but **write nothing**: no files, no MCP writes. Simulated values must never reach the real OKR sets, bets, or reviews, because every other command would read them as real.

## Setup

1. Resolve the level, team, period, source, and write policy. For `mcp` sources, read the set through the `read` tool and refresh the mirror.
2. **Team level**: read the team set, every bet file under `teams/<team>/bets/`, and the latest review of every spec that references a hypothesis (`okr:<team>/<H-n>`). Also read the company set, for the ladder and down-propagation.
3. **Company level**: read the company set and every team set of the same period that names it (their `Company OKRs` header).

## Collect

For each KR without a value in the input, ask for it, one at a time, and show its metric definition. Accept "unknown", which is a finding in itself. Never estimate or invent a current value.

## Roll up

**Team level**, for each KR:

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

**Company level**: fill **Team Contributions** from the team sets. Propose a status for each company KR from its own numbers and its team contributions. When teams disagree with the number, say so.

## Propagate

- **Up**:
  - A team KR that is `off_track` or `done` and contributes to a company KR gets a **Proposal** to the company level ("C-KR-2 at risk: the reporting team's KR-1 is off track after H-3 was refuted").
  - The same goes for a weak ladder found during the roll-up.
  - Write proposals according to the company level's `agent_writes`.
- **Down**: run the orphan checks from the shared docs, and list each orphan with a recommendation (re-frame it against another KR, pause the spec, or close the bet).

## Decide and record

Present proposed statuses, proposals, and orphans in one table. Ask once: **apply all / choose / none**. Then write, according to the level's write policy:

- the KR values, scores, and statuses;
- a row in **Check-in History**;
- `Last check-in: <today>`;
- hypothesis statuses confirmed from bet reviews, never changed beyond what the bet reviews say;
- proposals.

**With `close`**: also fill **Period Close**:

- the final score of each KR;
- learnings from validated and refuted hypotheses;
- carry-over: each open hypothesis goes to the next period or gets closed, as the user decides.

Then set `Status: closed`. Do not create the next period's set; recommend `__SPECKIT_COMMAND_OKR_SET__ period=<next>` instead.

## Report

```markdown
## OKR check-in — <level> <team?> <period> — <date>

| KR | Score | Status (was → now) | Hypotheses |
|----|-------|--------------------|------------|

**Proposals to company**: <n> · **Orphans**: <n> · **Stale bets** (no review in > cadence): <n>
**Next check-in**: <date>
```

## Guardrails

- Never modify source code, specs, or bet files. Bets change only through `__SPECKIT_COMMAND_OKR_REVIEW__` and `__SPECKIT_COMMAND_OKR_FRAME__`.
- Never change targets or deadlines here. That is a `__SPECKIT_COMMAND_OKR_SET__` change, with a Change Log entry.
- Never write to the company level beyond its `agent_writes` policy.
