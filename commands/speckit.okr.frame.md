---
description: "Frame a feature as a bet before specifying: pick the team KR it should move, state the hypothesis, how it would be refuted, guardrails, and candidate ideas"
handoffs:
  - label: Write the Specification
    agent: speckit.specify
    prompt: Specify the feature as the initiative that tests the framed hypothesis
---

# Frame a Bet

A spec is an initiative, and an initiative is a **bet**: it tests a hypothesis the team holds about how to move one of its Key Results. This command turns a feature idea into that bet before anyone writes requirements. It answers four questions:

1. Which team KR should this move?
2. What do we believe, and why?
3. What result would prove us wrong?
4. What must not break?

The result is a hypothesis `H-n` in the team OKR set and a bet file `teams/<team>/bets/H-n-<slug>.md`. Then `__SPECKIT_COMMAND_SPECIFY__` writes the spec as the initiative that tests it.

Frame **defines the bet; it does not design or choose the solution.** Solution ideas become candidate ideas, and the spec chooses among them. If the input arrives as a solution ("build X"), ask what X is supposed to change and frame that.

**First, read `.specify/extensions/okr/docs/okr-sources.md` and `.specify/extensions/okr/docs/interview-and-kr-quality.md`, and follow them.**

## User Input

```text
$ARGUMENTS
```

The input may be a feature idea or problem statement, `kr=KR-n` to target a KR, `slug=<slug>`, `bet=H-n` to resume a bet, or `mode=lite` (3 questions: KR, hypothesis with refutation, guardrail) for small features.

## Setup

1. Resolve the team, the period, and the team set's source. Read the team set and the company set. Warn if either is stale (see Freshness).
2. **No team set for the period?** Offer two paths:
   - (a) run `__SPECKIT_COMMAND_OKR_SET__` first (recommended);
   - (b) continue with **provisional KRs** defined inside this bet. They get marked `provisional` and are proposed to the team set at the end.
3. **Enabling work?** If the input is compliance, a migration, or tech debt, with no outcome to bet on, say so. Record it as an **enabling initiative**: a one-line entry naming the KR or guardrail it protects, no hypothesis, no bet file. Then hand off to `__SPECKIT_COMMAND_SPECIFY__` with `okr:<team>/enabling:<KR-n|TG-n>`.
4. **Slug** (2–4 words, kebab-case, `[a-z0-9-]` only). Assign the next free `H-n` in the team set. If `bet=H-n` names an existing bet, resume it and ask only about what is missing.
5. If `.specify/assessments/<slug>/problem.md` exists (from the `assess` extension), reuse its problem, users, goals, and metrics.

## Interview

Priority order (full mode: up to `interview.max_questions`; `mode=lite`: questions 1, 2 and 4 only):

1. **Target KR**: which team KR should this move? Offer the team set's KRs that plausibly fit, recommending one with reasons. If none fits, offer to propose a new KR with a KR card. A new KR is written to the team set under its write policy, or kept as `provisional`.
   - When the bet aims at a lagging KR, name the leading KR (or bet signal) that will show progress first.
   - Run the **ladder check** on the KR chosen.
2. **Hypothesis**: *we believe [capability] for [users] causes [behavior change], seen in KR-n, because [evidence]*. Then:
   - **confidence**, with the evidence it rests on;
   - the **riskiest assumption**;
   - the **expected contribution**: how much of the KR this bet should move. Compare it with the other hypotheses on the same KR, and with the gap still left to the target.
3. **Refutation and validation**: what observable result would prove the hypothesis wrong, and what is the smallest slice that would produce that result (the future P1). With low confidence, the validation slice is mandatory.
4. **Guardrails**: what this bet must not break, beyond the team guardrails (`TG-n`), and at what limit it gets stopped. Look for **gaming** (ways the KR could improve without the behavior actually changing) and **cannibalization** (ways the bet could hurt another KR).
5. **Boundaries and ideas**: problem-space boundaries (segments, audiences, adjacent problems), hard constraints, and **the solution ideas the user already has**. Ask for the ideas explicitly, and record each one as `CI-n`. Never recommend putting a solution idea out of scope: choosing among solutions happens in the spec. If the *user* rules a solution out, record it as their decision.
6. **Decision rules**: cadence, and the conditions for validated / iterate / refuted. Recommend the configured `scoring.thresholds` together with the refutation criterion from question 3.

**Measurement readiness is inferred, never asked**: for each KR involved, derive it from whether a baseline and a source exist (and from the code, read-only).

## Write

- **Bet file**: resolve `bet-template` through the template stack (falls back to `.specify/extensions/okr/templates/bet-template.md`) and write `teams/<team>/bets/H-n-<slug>.md` with `Status: framed`. Leave the **Stories** table empty: `__SPECKIT_COMMAND_OKR_ALIGN__` fills it.
- **Team set**: add the `H-n` row to **Hypotheses** (status `framed`, link to the bet file), under the team level's write policy. With `agent_writes: propose` or `none`, record the row as a proposal and note it in the bet file.
- Mark every missing required field `[NEEDS CLARIFICATION: …]`.

## Quality gate and report

Evaluate the bet file's **Quality Gate** and tick what passes. Then:

```markdown
## Bet framed — <team> H-n <slug>

**KR**: KR-n <target> (contributes to C-KR-m | team-local) <⚠ weak ladder?>
**Hypothesis**: <one line> · **Confidence**: <level> · **Expected contribution**: <…>
**Refuted if**: <criterion> · **Validation slice**: <…>
**Guardrails**: <n> bet + <n> team · **Candidate ideas**: <n>
**Gate**: <passed>/<total> — READY | NEEDS WORK
<failing checks / open questions>

**Next**: __SPECKIT_COMMAND_SPECIFY__ <feature description> okr:<team>/H-n
```

The `okr:<team>/H-n` token must appear in the handoff text, so that `__SPECKIT_COMMAND_SPECIFY__` (and the `okr-bet` preset, if installed) and `__SPECKIT_COMMAND_OKR_ALIGN__` can find the bet. After the token, append a one-paragraph bet summary to the description:

- the hypothesis;
- the KR;
- the refutation criterion;
- the validation slice;
- the candidate ideas;
- the boundaries.

## Guardrails

- Never modify source code or existing specs. Only write the bet file and the team set (within its write policy).
- Never invent numbers, evidence, or owners.
- Never drift into the solution space. Ideas are recorded, not decided.
- A failed gate does not block the user. They decide whether to continue, but the report says clearly what is missing.
