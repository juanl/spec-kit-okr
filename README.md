# OKR Impact Framing — a Spec Kit extension

Scope features by the **impact they must produce**, not by the list of things someone wants built.

This extension adds an OKR step around `/speckit.specify`. Before (or after) the spec is written, it walks you through the questions OKRs force you to answer:

- **Objective**: what will be different, and for whom?
- **Key Results**: how will we know? From what baseline to what target, by when?
- **Hypothesis**: why do we believe this feature moves that number?
- **Guardrails**: what must not get worse?
- **Measurement**: can we actually read these numbers on launch day?

The answers end up in the spec as **initiatives** (user stories ranked by the Key Results they move), in the plan as instrumentation work, and after launch in a scored check-in.

```text
Objective  (okr.md)       what changes, for whom
└─ Key Results (okr.md)   how we will know: baseline → target by date
   └─ Initiatives (spec.md user stories)   the bets we make to move each KR
```

## Workflow

```text
           ┌──────────────────┐
  idea ──▶ │ /speckit.okr.frame│  OKR interview → .specify/okr/<slug>/okr.md
           └────────┬─────────┘     (before_specify hook, optional)
                    ▼
           ┌──────────────────┐
           │ /speckit.specify  │  spec.md, written against the KRs
           └────────┬─────────┘
                    ▼
           ┌──────────────────┐
           │ /speckit.okr.align│  user stories → ranked initiatives per KR, SC ↔ KR coverage
           └────────┬─────────┘     (after_specify hook; post-hoc interview if no framing exists)
                    ▼
           ┌──────────────────┐
           │ /speckit.plan     │
           └────────┬─────────┘
                    ▼
           ┌───────────────────┐
           │/speckit.okr.measure│ metric definitions, instrumentation, baseline capture,
           └────────┬──────────┘ attribution → "Measurement & Instrumentation" in plan.md
                    ▼               (after_plan hook)
        /speckit.tasks → /speckit.implement
                    ▼
           ┌──────────────────┐
           │/speckit.okr.review│  post-launch: score KRs, read leading signals,
           └──────────────────┘  diagnose each initiative, persevere / iterate / pivot / stop
```

You can enter at either point:

- **OKR-first** (recommended): `frame` → `specify` → `align`. The spec is scoped by the KRs from the beginning.
- **Spec-first**: `specify` → `align`. `align` drafts the OKRs from the spec and interviews you only about what the spec cannot answer, usually baselines, targets, owners, and guardrails.

## Commands

| Command | Hook | Writes |
|---------|------|--------|
| `/speckit.okr.frame` | `before_specify` (optional) | `.specify/okr/<slug>/okr.md` |
| `/speckit.okr.align` | `after_specify` (optional) | `specs/<feature>/okr.md`; `spec.md` edits (only with your approval) |
| `/speckit.okr.measure` | `after_plan` (optional) | `specs/<feature>/measurement-plan.md`; a section in `plan.md` |
| `/speckit.okr.review` | — | `specs/<feature>/okr-reviews/<date>.md`; check-in history in `okr.md` |

All hooks are **optional**. Spec Kit offers to run them, and you can always run the commands by hand.

### After launch: why did it (not) work?

`review` reads each initiative's leading signal against its KR. *Signal moved but KR flat* means the hypothesis is wrong, so pivot. *Signal flat* means users are not adopting the initiative, so iterate on it. This way a check-in tells you **where** the bet failed, not only **that** it did.

### What the interview feels like

Questions come one at a time, each with a recommended answer derived from what is already known:

```text
Q2 — Key Results: What is 7-day activation today, and where does that number come from?

Recommended: "Unknown. Capture it from the `onboarding_completed` event for 2 weeks
before rollout." No baseline appears in the input or the codebase, and the event
already exists.

Reply "yes" to accept, or give your own answer.
```

Weak Key Results get coached rather than accepted, for example "Launch the new onboarding" → *that's an output; what should it change?* → "Raise 7-day activation from 32% to 45% by 2026-12-31".

### What lands in the spec

After `align`, each user story is an initiative with a KR, a hypothesis, and a leading signal. Its priority reflects impact × confidence, and when confidence is low, P1 is the story that validates the riskiest assumption:

```markdown
### User Story 1 - Guided first-project checklist (Priority: P1)
...
**Initiative → KR-1** · Hypothesis: teams that reach a first shared project see value before the
trial ends · Leading signal: % of new teams completing the checklist by day 3 · Confidence: low
```

Success Criteria point at the KR they provide evidence for, and the spec gains one section:

```markdown
- **SC-002**: 80% of new users finish setup in their first session *(→ KR-1)*

## Impact & Objectives (OKR)

**Objective**: New teams get to their first useful result without help
**Framing**: [okr.md](./okr.md)

| KR | Target | Initiatives | Evidenced by |
|----|--------|-------------|--------------|
| KR-1 | 32% → 45% 7-day activation by 2026-12-31 | US-1 (P1), US-3 (P2) | SC-002 |

**Guardrails**: G-1 setup-related support tickets must not exceed 40/week
**Out of scope (no KR impact this horizon)**: theming, SSO
```

## Example

See [examples/self-serve-guided-onboarding](examples/self-serve-guided-onboarding/) for a full run (frame → specify → align → plan → measure → tasks → review) on a fictional SaaS.

## Installation

Requires Spec Kit `>= 0.9.0`.

```bash
# from a local checkout
specify extension add --dev /path/to/spec-kit-okr

# from a release archive
specify extension add okr --from https://github.com/jladetto/spec-kit-okr/archive/refs/tags/v0.1.0.zip
```

Check it is installed:

```bash
specify extension list
```

## Configuration

Optional. Copy `okr-config.template.yml` to `.specify/extensions/okr/okr-config.yml`:

| Key | Default | Purpose |
|-----|---------|---------|
| `alignment.parent_okrs_file` | `""` | Team/company OKRs the feature must ladder up to. When set, parent Objectives are chosen from this file only |
| `alignment.horizon` | `quarter` | Default KR deadline horizon |
| `key_results.min` / `max` | `2` / `4` | KR count bounds. More than `max` usually means two features |
| `key_results.require_*` | `true` | Baseline, deadline, owner, and counter-metric requirements for the quality gate |
| `scoring.aspirational_target` | `0.7` | Expected score for aspirational KRs |
| `scoring.thresholds.persevere` / `iterate` | `0.7` / `0.4` | Default decision thresholds for `review` |
| `initiatives.require_leading_signal` | `true` | Every user story needs an early, observable behavior |
| `interview.max_questions` | `8` | Cap on primary questions (follow-ups don't count) |
| `interview.follow_ups_per_question` | `1` | Clarifications allowed per answer |
| `output.artifact_language` | `en` | Body language of the artifacts (`auto` = the conversation's). Headings and IDs stay in English |

## Works well with

- **`assess`** (bundled): if `.specify/assessments/<slug>/problem.md` exists, `frame` reuses its problem statement, users, goals, and metrics instead of asking for them again.
- **`/speckit.clarify`**: open OKR questions are marked `[NEEDS CLARIFICATION]` in the spec, so clarify picks them up.

## Design principles

- **Outcomes over outputs.** "Ship X" is an initiative, not a Key Result.
- **No invented numbers.** An unknown baseline is recorded as unknown, along with how it will be obtained.
- **Measurement is part of the Definition of Done.** Instrumentation and baseline capture become tasks, not afterthoughts.
- **The human decides.** Spec edits need approval. Review decisions record what the user chose, not what the agent recommended.

## Resumen en español

Extensión de Spec Kit que acota el alcance de una feature con la lógica de los OKRs, antes o después de `/speckit.specify`. `frame` hace una entrevista guiada (Objetivo, Key Results con línea base y meta, hipótesis, guardrails, alcance). `align` convierte las user stories del spec en iniciativas: cada una con el KR que mueve, su hipótesis y su señal leading, priorizadas por impacto × confianza. `measure` agrega al plan la instrumentación y la captura de la línea base. `review` puntúa los KRs después del lanzamiento, cruza las señales de cada iniciativa con su KR para diagnosticar dónde falló la apuesta, y registra la decisión. Los comandos responden en el idioma del usuario.

## License

MIT
