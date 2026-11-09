## Hypothesis & Bet *(mandatory when the input has an `okr:` token)*

<!--
  This spec is the initiative that tests one hypothesis about moving a team Key Result.
  Fill from the bet file referenced by okr:<team>/H-n. For enabling work (okr:<team>/enabling:<id>),
  state only what it protects and why, and delete the other lines.
-->

**Bet**: okr:[team]/[H-n] — [bet file](../../.specify/okr/teams/[team]/bets/[H-n-slug].md)
**Hypothesis**: We believe [capability] for [users] causes [behavior change], seen in [KR-n]
**Moves**: [KR-n] ([baseline] → [target] by [date]); drives [KR-m, if any]
**Expected contribution**: [how much of the KR this bet should move]
**Refuted if**: [observable result that proves the hypothesis wrong]
**Validation slice**: User Story [n] (P1)
**Scale stories (built only if validated)**: User Story [n], …
**Guardrails**: [G-n / TG-n — metric must not cross limit]
**Out of scope (this horizon)**: [problem-space boundaries]

**Verification contract** (from the bet file; definitions are not changed here):

| ID | Number | Source (owner) | Baseline | Validated / Refuted if | Measurable today? |
|----|--------|----------------|----------|------------------------|-------------------|
| [S-n / KR-n / G-n] | [definition] | [source] ([owner]) | [value, or how it is captured before exposure] | [threshold] / [threshold] | yes / instrument / blocked: [who unblocks it] / unknown: [who knows the source] |
