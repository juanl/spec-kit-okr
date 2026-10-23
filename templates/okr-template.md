# OKR Framing: [FEATURE TITLE]

- **Slug**: [okr-slug]
- **Status**: draft | aligned | measuring | reviewed
- **Created**: [ISO 8601 date]
- **Horizon**: [quarter / date range]
- **Feature spec**: [path to spec.md, or "pending /speckit.specify"]
- **Parent objective**: [parent OKR id + title, or "none declared"]

## Objective

> [One qualitative, outcome-oriented sentence: what will be different, and for whom, when this succeeds. No metrics, no features.]

**Why now**: [The trigger or cost of waiting.]

## Key Results

| ID | Key Result (outcome) | Metric | Baseline | Target | Deadline | Type | Leading/Lagging | Drives | Owner | Source |
|----|----------------------|--------|----------|--------|----------|------|-----------------|--------|-------|--------|
| KR-1 | [Behavior change, stated as an outcome] | [metric name] | [value @ date, or unknown] | [value] | [date] | committed / aspirational | leading / lagging | [KR-n it predicts, or —] | [role] | [where the number comes from] |

## Impact Hypothesis

We believe that **[capability]** for **[users]** will cause **[behavior change]**, which we will see in **[KR-n]**, because **[evidence or reasoning]**.

- **Confidence**: high | medium | low — [why]
- **Riskiest assumption**: [the assumption that, if false, makes the feature pointless]

## Guardrails (Counter-metrics)

| ID | Metric | Current | Must not cross | Why it matters |
|----|--------|---------|----------------|----------------|
| G-1 | [metric] | [value] | [limit] | [the harm we are protecting against] |

## Boundaries

- **Out of scope (this horizon)**: [item — reason]
- **Constraints**: [deadline, budget, team, compliance…]

## Candidate Initiatives

Solution ideas raised during framing. They are not decisions: the spec turns them into user stories, and alignment ranks them.

| ID | Idea | Expected KR | Raised by |
|----|------|-------------|-----------|
| CI-1 | [idea] | KR-n | [user / research / competitor] |

**Validation first**: [Only when confidence is low: the cheapest initiative that tests the riskiest assumption, e.g. "CI-2 — tests whether teams that reach first value convert more"]

## Measurement Readiness

| ID | Measurable today? | Gap |
|----|-------------------|-----|
| KR-1 | yes / partially / no | [missing event, missing baseline, no data access…] |

## Decision Rules

- **Check-in cadence**: [weekly / bi-weekly / at deadline]
- **Persevere** if: [condition, e.g. KR-1 score ≥ 0.7]
- **Iterate** if: [condition]
- **Pivot / Stop** if: [condition, including any guardrail breach]

## Initiatives

Filled by `/speckit.okr.align` from the spec's user stories.

| Initiative | Priority | Moves | Hypothesis | Leading signal | Confidence | Status |
|------------|----------|-------|------------|----------------|------------|--------|
| [US-n title] | P1 | KR-n / enabling | [one line] | [behavior visible within days of exposure] | high / medium / low | planned / live / validated / iterating / dropped |

## KR Coverage

| KR / Guardrail | Success Criteria | Initiatives |
|----------------|------------------|-------------|
| KR-1 | [SC-00x] | [US-n] |

## Framing Decisions

Dated changes to KRs, deadlines, or targets, with the reason. Targets never change silently.

- [YYYY-MM-DD] — [change] — [reason]

## Quality Gate

- [ ] Objective is qualitative and free of metrics and solutions
- [ ] Every KR is an outcome, not an output ("ship X" is an initiative, not a KR)
- [ ] Every KR has metric, baseline, target, deadline, owner, and source
- [ ] KR count within configured limits
- [ ] At least one leading KR
- [ ] At least one guardrail
- [ ] Hypothesis links the feature to at least one KR
- [ ] Low confidence has a validation-first initiative (or confidence is not low)

## Open Questions

- [NEEDS CLARIFICATION: …]

## Check-in History

| Date | KR scores | Guardrails | Initiative signals | Decision |
|------|-----------|------------|--------------------|----------|
