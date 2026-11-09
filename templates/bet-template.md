# Bet: [H-n] — [SHORT TITLE]

- **Team**: [team id]
- **Period**: [2027-Q1]
- **Hypothesis**: [H-n] (in [team OKR file])
- **Key Results**: [KR-n (moved directly)], [KR-m via Drives]
- **Status**: framed | in_test | validated | refuted | inconclusive | dropped
- **Spec(s)**: [specs/…, or "pending /speckit.specify"]
- **Created**: [ISO date]

## Hypothesis

We believe that **[capability]** for **[users]** will cause **[behavior change]**, which we will see in **[KR-n]**, because **[evidence or reasoning]**.

- **Confidence**: high | medium | low — [why]
- **Riskiest assumption**: [the assumption that, if false, makes the bet pointless]
- **Expected contribution**: [how much of KR-n this bet is expected to move, e.g. "+8 pp of the +15 pp target"]

## Validation

- **Validation slice (P1)**: [the smallest part of the spec that confirms or refutes the hypothesis]
- **Refuted if**: [observable result that would show the hypothesis is false, stated with Verification Contract IDs, e.g. "S-1 moves but KR-n stays flat after 6 weeks". A signal that does not move means iterate, not refuted]
- **Scale slices (P2+)**: built only if the hypothesis holds after the validation slice

## Guardrails

Definitions, limits, and sources are in the **Verification Contract**.

| ID | Metric | Why it matters |
|----|--------|----------------|
| G-1 | [metric] | [harm] |

## Candidate Ideas

Solution ideas raised during framing. They are not decisions: the spec chooses among them.

| ID | Idea | Raised by |
|----|------|-----------|
| CI-1 | [idea] | user / research / competitor |

## Boundaries

- **Out of scope (this horizon)**: [problem-space boundaries: segments, audiences, adjacent problems]
- **Constraints**: [deadline, team, compliance…]

## Verification Contract

Every number the verdict depends on: the bet's leading signals (`S-n`), the KRs, and the guardrails. Written by `/speckit.okr.frame`; `/speckit.okr.measure` turns it into instrumentation and `/speckit.okr.review` reads the verdict from it. Definitions live here and nowhere else.

| ID | Role | Definition | Source (owner) | Baseline | Validated if | Refuted if | Measurable today? |
|----|------|------------|----------------|----------|--------------|------------|-------------------|
| S-1 | leading signal | [exact formula: what, unit, window, population, what is included/excluded] | [APM / logs / DB / analytics / survey / third party] ([own team / other team / vendor]) | [value + date + how, or "capture from <source> before <date>"] | [threshold] | [threshold] | yes / instrument / blocked: [who unblocks it] / unknown: [who knows the source] |
| KR-n | key result | | | | [threshold] | [threshold] | |
| G-1 | guardrail | | | | — | [limit that stops the bet] | |

- **Verdict window**: [how long after exposure the first verdict can be read, and why]
- **Attribution**: [how we will tell the change caused the effect: control group, staged rollout, before/after with a caveat]
- **Blockers**: [each "blocked" row: who unblocks it, by when; or "none"]

## Decision Rules

- **Check-in cadence**: [weekly / bi-weekly]
- **Validated** if: [condition]
- **Iterate** if: [condition]
- **Refuted / stop** if: [condition, including any guardrail breach]

## Stories

Filled by `/speckit.okr.align` from the spec.

| Story | Stage | Role in the bet | Signal (S-n) | Status |
|-------|-------|-----------------|----------------|--------|
| [US-n] | validation / scale / enabling / protects G-n | [what it contributes to testing or scaling the hypothesis] | [S-n from the Verification Contract] | planned / live / done / dropped |

## Quality Gate

- [ ] Hypothesis names a capability, users, a behavior change, and the KR it should show in
- [ ] KR exists in the team set and is not dropped
- [ ] Ladder: the KR contributes to a company KR, or is explicitly team-local
- [ ] Refutation criterion is observable
- [ ] Validation slice is defined (or confidence is high and this is stated)
- [ ] At least one guardrail (bet or team)
- [ ] Every KR involved has a baseline, or "unknown + how it will be obtained"
- [ ] Verification contract: every row has a definition, a source, and thresholds; **Refuted if** is computable from its rows
- [ ] **Blocking**: the verdict can be computed: no row it depends on is `unknown`, or `blocked` without an owner and a date

## Open Questions

- [NEEDS CLARIFICATION: …]

## Framing Decisions

- [YYYY-MM-DD] — [change] — [reason]

## Reviews

| Date | Verdict | KR scores | Guardrails | Decision | Review file |
|------|---------|-----------|------------|----------|-------------|
