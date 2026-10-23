---
description: "Read-only view of the OKR tree: company → team KRs → hypotheses → specs, with statuses, staleness, and orphaned work"
---

# OKR Status

Show the whole tree in one view, read-only. The goal is to answer, at a glance: *are our KRs moving, which bets are testing them, and is any work running without a reason?*

**First, read `.specify/extensions/okr/docs/okr-sources.md` and follow it.** This command writes nothing, except refreshing `mcp` mirrors after a read.

## User Input

```text
$ARGUMENTS
```

Optional: `team=<id>`, `period=<id>`, `level=company` (company KRs with every team's contributions).

## Gather

- The company set and the team set(s) for the period, through their sources.
- Every bet file under `teams/<team>/bets/`.
- Every spec under `specs/` whose Input line has `okr:<team>/<H-n>`, plus its progress: `plan.md`, `tasks.md` (count `- [x]` against `- [ ]`), and `okr-reviews/` (latest verdict and date).
- Enabling specs: specs that reference a KR or a guardrail without a hypothesis.

## Show

```text
2027-Q1 · team reporting · last team check-in 2027-02-15 (OK, cadence 14d)

C-KR-1 Net revenue retention ≥ 115%            at_risk   (company check-in 2027-02-01)
└─ KR-1 Managers sharing weekly 0% → 30%       at_risk   score 0.4
   ├─ H-1 Export replaces screenshots          in_test   bet: validated? no — inconclusive (2027-02-15)
   │  └─ specs/001-compartir-reportes          tasks 34/76 · P1 live · P2 gated on H-1
   └─ H-2 Scheduled send builds the habit      framed    no spec yet
KR-2 Tickets about sharing 25 → ≤10/month      on_track  score 0.6   (team-local)
   └─ (no hypothesis)                           ⚠ KR without a bet
```

Then a **Findings** list:

- **Stale**: sets whose last check-in is older than their cadence; bets with no review for longer than their check-in cadence; `mcp` mirrors whose sync is older than 24h.
- **Orphans**: the down-propagation checks from the shared docs.
- **Gaps**: KRs with no hypothesis; hypotheses with no spec; specs without a review after their observation period ended; bets whose P2+ stories are being implemented while the validation verdict is not `validated`. That last one is **scaling before validating**.
- **Ladder**: team KRs whose `Contributes to` is weak or missing; **ladder opportunities**, where a company KR added or changed since the team set was written fits a team-local KR, or an accepted proposal hasn't been reflected in the team set yet. Resolve them with `__SPECKIT_COMMAND_OKR_SET__`.

For each finding, give the single next command that resolves it (e.g. `__SPECKIT_COMMAND_OKR_CHECKIN__ team=reporting`, `__SPECKIT_COMMAND_OKR_FRAME__ kr=KR-2`).

## Guardrails

- Read-only: never modify OKR sets, bets, specs, or code.
- If a source cannot be read (missing file, MCP server unavailable), show that branch as `unavailable` and continue with the rest of the tree.
