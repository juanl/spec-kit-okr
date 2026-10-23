---
description: "Check that the spec is the initiative that tests its bet: hypothesis section, validation slice as P1, scale stories gated, guardrails covered; frames the bet post-hoc if none exists"
scripts:
  sh: ../../scripts/bash/check-prerequisites.sh --json --paths-only
  ps: ../../scripts/powershell/check-prerequisites.ps1 -Json -PathsOnly
handoffs:
  - label: Clarify Spec Requirements
    agent: speckit.clarify
    prompt: Clarify the open questions raised by the OKR alignment
  - label: Build Technical Plan
    agent: speckit.plan
    prompt: Create a plan for the spec. I am building with...
---

# Align the Spec with its Bet

The spec is the **initiative that tests a hypothesis** (`H-n`) about how to move a team Key Result. This command checks that the spec does that:

- it states the hypothesis, the KR, and the refutation criterion;
- its **P1** is the slice that can confirm or refute the hypothesis;
- the stories that scale the bet are gated on validation;
- every guardrail is protected;
- every Success Criterion has a reason to exist.

When no bet exists yet, it frames one post-hoc.

**First, read `.specify/extensions/okr/docs/okr-sources.md` and follow it.** For post-hoc framing, also read `.specify/extensions/okr/docs/interview-and-kr-quality.md`.

## User Input

```text
$ARGUMENTS
```

Optional: `bet=H-n`, `team=<id>`.

## Setup

1. Run `{SCRIPT}` from the repo root and parse `FEATURE_DIR` and `FEATURE_SPEC`. If the script cannot resolve a feature, or `FEATURE_SPEC` does not exist, stop and point to `__SPECKIT_COMMAND_SPECIFY__`.
2. Resolve the team, the period, and the sources. Read the team set and the company set (warn if stale).

## Locate the bet

In order:

1. Explicit `bet=H-n`.
2. An `okr:<team>/H-n` token in the spec's `**Input**` line or its **Hypothesis & Bet** section.
3. An `okr:<team>/enabling:<id>` token → **enabling mode**: check only that the spec states what it protects and why, and that no story claims a KR it cannot move. Then skip to *Report*.
4. A `framed` bet in `teams/<team>/bets/` whose slug or title matches the spec. Propose it and ask for confirmation.
5. None → **post-hoc mode**.

## Post-hoc mode

1. From the spec, draft the hypothesis it implicitly tests: which behavior change, for whom, and which team KR (from the team set) it should show in. Most Success Criteria are acceptance thresholds, not outcomes. Say so where it applies.
2. Run the `__SPECKIT_COMMAND_OKR_FRAME__` interview, limited to what the spec cannot answer. That usually means the target KR, confidence and evidence, the refutation criterion, guardrails, and baselines.
3. If the spec's stories **cannot move** the outcome the user wants, say so plainly, and propose the missing initiative as a new story. For example, a reminder sent *after* the due date cannot raise on-time completion, so the bet needs an earlier reminder.
4. Write the bet file and the team-set hypothesis row, as `__SPECKIT_COMMAND_OKR_FRAME__` would.

## Check the spec against the bet

1. **Hypothesis & Bet section**: present, and consistent with the bet file (the same `H-n`, KR, refutation criterion, and validation slice). If the `okr-bet` preset is installed, the section comes from the spec template and should already be filled. Otherwise, propose inserting it after `## Success Criteria`:

   ```markdown
   ## Hypothesis & Bet

   **Bet**: okr:<team>/H-n — [bet file](<relative path>)
   **Hypothesis**: <one line>
   **Moves**: KR-n (<baseline> → <target> by <date>)<; drives KR-m>
   **Expected contribution**: <…>
   **Refuted if**: <criterion>
   **Validation slice**: User Story <n> (P1)
   **Scale stories (built only if validated)**: User Story <n>, …
   **Guardrails**: G-1 …; team TG-1 …
   **Out of scope (this horizon)**: …
   ```

2. **Stages**: classify each user story as one of:
   - `validation`: part of the slice that tests the hypothesis;
   - `scale`: amplifies the effect, worth building only if the hypothesis holds;
   - `enabling`: needed by another story, moves nothing by itself;
   - `protects G-n`: keeps a guardrail within its limit;
   - `none`.

   Then:
   - P1 must be the validation slice. When it is not, that is a **priority contradiction**.
   - With low confidence, any `scale` story at P1 is a contradiction.
   - `enabling` and `protects` stories take the priority of what they serve.
   - `none` stories are proposed for out-of-scope.
3. **Leading signals**: every `validation` story needs a behavior that can be observed within days, so the first review has something to read. `scale` stories need one only if `initiatives.require_leading_signal` is `true`.
4. **Candidate ideas**: each `CI-n` either became a story or has a recorded reason for being dropped.
5. **Success Criteria**:
   - Each SC maps to a KR, a guardrail, a story's leading signal, or is explicitly an acceptance threshold.
   - The KR the bet moves needs at least one SC.
   - So does every guardrail.
6. **Chains**: use only the `Drives` links declared in the team set. Never infer new chains.
7. **Feasibility**: compare the bet's expected contribution with what the stories can plausibly reach. When the spec is much smaller than the claim, flag it.

## Findings

Present a single table. Each row gives the finding, the evidence, and the proposed spec change. Use these types:

- priority contradiction;
- missing validation slice;
- spec cannot move the KR;
- missing leading signal;
- dropped candidate;
- orphan SC;
- unmeasured guardrail;
- inconsistent bet section;
- inferred chain.

Ask once: **apply all / choose / none**. Do not edit the spec without approval.

## Update

With approval:

- **In `spec.md`**, make minimal edits:
  - priorities;
  - one line per story with `**Stage**: <stage> · Leading signal: <…>`;
  - SC tags `*(→ KR-n | G-n | signal US-n | acceptance threshold)*`, plus any accepted new SCs;
  - the Hypothesis & Bet section.

  Never renumber stories, FRs, or SCs.
- **In the bet file**:
  - fill the **Stories** table (status `planned`);
  - set `Spec(s)` to the spec path;
  - set `Status: in_test` once the spec is accepted.
- **In the team set**, under its write policy:
  - add the spec to the hypothesis row's **Specs** column;
  - set the hypothesis status to `in_test`.
- **In `FEATURE_DIR/checklists/requirements.md`**, if it exists: add `- [x] Spec is the initiative that tests okr:<team>/H-n (validation slice is P1)`.

## Report

```markdown
## OKR alignment — <feature>

**Mode**: bind | post-hoc | enabling
**Bet**: okr:<team>/H-n — <hypothesis> → KR-n <(contributes to C-KR-m)>
**Stories**: <n> validation, <n> scale, <n> enabling, <n> protects, <n> none · **P1**: US-<n> <(validation slice ✓ | ⚠)>
**Coverage**: KR has SC <✓/✗>; guardrails protected <n>/<n>
**Findings**: <counts> · **Spec updated**: yes (<n> edits) | no

**Next**: __SPECKIT_COMMAND_CLARIFY__ if open questions remain; otherwise __SPECKIT_COMMAND_PLAN__, then __SPECKIT_COMMAND_OKR_MEASURE__.
```

## Guardrails

- Never modify source code.
- Only write `spec.md` (with approval), the requirements checklist, the bet file, and the team set (within its write policy).
- Never invent baselines, owners, or evidence.
