---
description: "Create or update a company or team OKR set for a period: objectives, Key Results with baselines, ladder to company KRs, team guardrails"
---

# Set OKRs (company or team)

Create or update the OKR set of one level (company or team) for one period. Feature bets (`__SPECKIT_COMMAND_OKR_FRAME__`) hang from the team set, and the team set ladders up to the company set. Both sets are living documents: check-ins update them (`__SPECKIT_COMMAND_OKR_CHECKIN__`), and this command changes their content.

**First, read `.specify/extensions/okr/docs/okr-sources.md` and `.specify/extensions/okr/docs/interview-and-kr-quality.md`, and follow them.**

## User Input

```text
$ARGUMENTS
```

Arguments (all optional): `level=team|company` (default `team`), `team=<id>`, `period=<id>`, `from=<path>` (import an existing OKR document), or free text describing the OKRs.

## Setup

1. Resolve `level`, `team`, and `period` from the arguments and the config. If `team` is unknown, ask once and suggest saving it in `okr-config.yml`.
2. Resolve the level's source and write policy:
   - **`level=company` with `agent_writes` other than `confirm`**: you may not author the company set. Offer to **import** it instead (`from=`, pasted text, or an MCP read), so the mirror reflects what leadership decided. Any change beyond a faithful import goes to **Proposals**.
   - **`source: mcp`**: read the current set through the `read` tool first. Writes go through `update_kr` / `propose`, as allowed.
3. Read the existing set if there is one: resume it, and interview only for what is missing or `[NEEDS CLARIFICATION]`. For a team set, also read the company set of the same period, since it is the only valid source of `Contributes to` links.
4. If the previous period's set exists and is `closed`, read its **Period Close**. Offer the carried-over hypotheses and KRs as starting options.

## Import (`from=…` or pasted text)

Map the document onto the template faithfully: objectives, KRs, baselines, targets, owners. **Do not improve the content while importing.** List the quality problems you see (using the coaching smells) in a short report, and offer to fix them in an interview afterwards. For company sets with `agent_writes: propose`, those fixes become Proposals.

## Interview (team set)

Priority order. The rules for interviews, KR cards, follow-ups, and coaching are in the shared docs.

1. **Objectives** (1–3): what will be different for whom this period, and why now.
2. **KR cards** per objective (between `key_results.min` and `key_results.max` per objective, defaults 2 and 4). Each card includes `Contributes to`. Run the **ladder check** on each card.
3. **At least one leading KR** in the set, with `Drives` pointing to the lagging KR it predicts.
4. **Team guardrails** (`TG-n`): health metrics no bet may break, e.g. performance, support load, data exposure.
5. **Cadence**: check-in frequency (default `levels.team.cadence_days`).

Do not ask about solutions, features, or hypotheses here. Hypotheses come from `__SPECKIT_COMMAND_OKR_FRAME__`. If the user volunteers ideas, record them in the report as possible bets.

## Write

Resolve `team-okrs-template` or `company-okrs-template` through the template stack (equivalent to `specify preset resolve <name>`; falls back to `.specify/extensions/okr/templates/`), and write the set according to the level's source and write policy:

- New set: `Status: draft`. It becomes `active` when the user confirms that the set is final for the period.
- Every change to an existing objective, KR, target, or deadline gets a dated **Change Log** entry with its reason. Never change a target silently.
- After changing a team KR that has hypotheses, list those hypotheses and their specs: they may need re-framing.

## Report

```markdown
## OKR set — <level> <team?> <period>

**Status**: draft | active
**Objectives**: <n> · **KRs**: <n> (<leading>/<lagging>; <n> with baseline)
**Ladder**: <n>/<n> team KRs contribute to a company KR; <n> team-local; <n> weak links flagged
**Guardrails**: <n>
**Proposals to company**: <n>
**Orphans found**: <n> (see down-propagation)

**Next**: __SPECKIT_COMMAND_OKR_FRAME__ to frame a bet against one of these KRs, or __SPECKIT_COMMAND_OKR_STATUS__ to see the tree.
```

## Guardrails

- Never modify source code or specs.
- Never author company OKRs unless the company level's `agent_writes` is `confirm`.
- Never invent baselines or owners.
