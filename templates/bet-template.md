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
- **Refuted if**: [observable result that would show the hypothesis is false, e.g. "signal X moves but KR-n stays flat after 6 weeks"]
- **Scale slices (P2+)**: built only if the hypothesis holds after the validation slice

## Guardrails

| ID | Metric | Current | Must not cross | Why it matters |
|----|--------|---------|----------------|----------------|
| G-1 | [metric] | [value] | [limit] | [harm] |

## Candidate Ideas

Solution ideas raised during framing. They are not decisions: the spec chooses among them.

| ID | Idea | Raised by |
|----|------|-----------|
| CI-1 | [idea] | user / research / competitor |

## Boundaries

- **Out of scope (this horizon)**: [problem-space boundaries: segments, audiences, adjacent problems]
- **Constraints**: [deadline, team, compliance…]

## Measurement Readiness

| ID | Measurable today? | Gap |
|----|-------------------|-----|
| KR-n | yes / partially / no | [missing event, baseline, access…] |

## Decision Rules

- **Check-in cadence**: [weekly / bi-weekly]
- **Validated** if: [condition]
- **Iterate** if: [condition]
- **Refuted / stop** if: [condition, including any guardrail breach]

## Stories

Filled by `/speckit.okr.align` from the spec.

| Story | Stage | Role in the bet | Leading signal | Status |
|-------|-------|-----------------|----------------|--------|
| [US-n] | validation / scale / enabling / protects G-n | [what it contributes to testing or scaling the hypothesis] | [behavior visible within days] | planned / live / done / dropped |

## Quality Gate

- [ ] Hypothesis names a capability, users, a behavior change, and the KR it should show in
- [ ] KR exists in the team set and is not dropped
- [ ] Ladder: the KR contributes to a company KR, or is explicitly team-local
- [ ] Refutation criterion is observable
- [ ] Validation slice is defined (or confidence is high and this is stated)
- [ ] At least one guardrail (bet or team)
- [ ] Every KR involved has a baseline, or "unknown + how it will be obtained"

## Open Questions

- [NEEDS CLARIFICATION: …]

## Framing Decisions

- [YYYY-MM-DD] — [change] — [reason]

## Reviews

| Date | Verdict | KR scores | Guardrails | Decision | Review file |
|------|---------|-----------|------------|----------|-------------|
