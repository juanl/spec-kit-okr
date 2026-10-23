# Interview rules and Key Result quality (shared)

Used by `/speckit.okr.set`, `/speckit.okr.frame`, and the post-hoc mode of `/speckit.okr.align`.

## Interview rules

- Before asking anything, extract every answer already present: the input, existing OKR sets, the bet file, the spec, `/memory/constitution.md`, and the code (read-only). Ask **only** about what is still missing.
- One question at a time. Never reveal the queue of upcoming questions.
- `interview.max_questions` (default 8; `mode=lite`: 3) caps **primary** questions. Each one may have up to `interview.follow_ups_per_question` (default 1) follow-ups, and follow-ups do not count toward the cap.
- Each question comes with a **recommended answer** derived from context:

  ```markdown
  **Q<n> — <stage>**: <question>

  **Recommended:** <answer> — <one-line reason>

  | Option | Answer |
  |--------|--------|
  | A | … |
  | B | … |
  | Custom | Your own answer |

  Reply with a letter, "yes" to accept the recommendation, or your own answer.
  ```
- After every answer, write it to the artifact immediately (within the level's write policy), so progress survives an interruption.
- "skip", "done", or "enough" ends the interview. Mark what is left `[NEEDS CLARIFICATION]`.

### Handling answers

- **Ambiguous** (two readings produce different artifacts): ask one follow-up that offers the readings as options, before writing anything.
- **Partial** (required fields missing): record what was given, then ask once for the rest as a follow-up. Whatever is still missing after that becomes `[NEEDS CLARIFICATION]`.
- **Override after coaching**: record exactly what the user said, add an Open Question that states the concern in one line, and don't raise it again.

## KR card

Ask for a Key Result as a single pre-filled card, so that one answer can settle every field:

```markdown
**Recommended card:**
- **Outcome**: <behavior change, not an output>
- **Metric**: <exact name and window>
- **Baseline**: <value + source, or "unknown — capture from <source> before <date>">
- **Target / deadline**: <value> by <date>
- **Type**: committed | aspirational
- **Leading / lagging**: <…>
- **Drives**: <for a leading KR: the lagging KR it predicts>
- **Contributes to**: <company C-KR-n, for team KRs>
- **Owner**: <role>

Reply "yes", edit any line, or replace the card.
```

## Coaching smells

Correct weak KRs instead of accepting them silently. Explain the problem in one line, and offer a rewrite as the recommended answer:

| Smell | Example | Rewrite toward |
|-------|---------|----------------|
| Output, not outcome | "Launch the new onboarding" | "Raise 7-day activation from 32% to 45%" |
| No baseline | "Increase retention to 60%" | "Increase D30 retention from [current] to 60%" |
| Implausible target | "80% trial-to-paid in 14 days" | State the usual range; ask whether it is aspirational, or whether it is really another metric |
| Lagging only | Every KR moves in months | Add a leading KR that moves within weeks, with `Drives` |
| Solution adoption as the outcome | "% of managers using the new export" (baseline 0% by construction) | Keep it as a **leading** KR or a bet signal. The outcome is what that adoption is meant to change |
| Tiny or noisy sample | Win rate over ~15 deals per quarter | Show how much one unit moves the metric. Propose a more attributable metric, or label it directional |
| Vanity metric | "Reach 10k page views" | A metric tied to the behavior the Objective names |
| Unmeasurable | "Users love the feature" | "CSAT for the flow ≥ 4.3/5 (n ≥ 200)" |
| Not attributable | "Grow company revenue 20%" | A metric the team can move, with a rollout that isolates the effect |
| Too many KRs | 7 KRs | Keep `key_results.max` (default 4); the rest become guardrails or get dropped |

## Ladder check

Re-run this check every time an Objective, a KR, or a `Contributes to` link changes. A team KR must plausibly move the **company KR** it names, not just sound related to that company Objective. For example, winning new enterprise deals does not move a net-revenue-retention KR, which measures existing customers.

When the link is weak, say so in one line. Then offer three options: a closer company KR, "none — team-local", or a **proposal** to the company level (see `agent_writes`) to add the missing KR. A weak ladder is worth surfacing to whoever owns the company OKRs.

## Statistics

Whenever you state a sample size, power, or significance, show the inputs and the formula on one line (e.g. `p1=0.09, p2=0.15, α=0.05, power=0.8 → n≈460/arm`), and label the result an estimate.
