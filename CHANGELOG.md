# Changelog

All notable changes to this extension are documented here. This project follows [Semantic Versioning](https://semver.org/).

## [0.1.0] - 2026-10-22

### Added

- `speckit.okr.frame`: OKR interview before specifying (Objective, Key Results, hypothesis, guardrails, scope by impact, decision rules), with Key Result coaching and a quality gate.
- `speckit.okr.align`: binds an OKR framing to `spec.md`, or derives one post-hoc; treats user stories as initiatives (KR moved, hypothesis, leading signal, confidence), ranks them by impact × confidence with a validation-first P1, and traces Success Criteria to KRs.
- `speckit.okr.measure`: metric definitions for KRs and initiative leading signals, instrumentation inventory, baseline capture, and attribution strategy; adds a "Measurement & Instrumentation" section to `plan.md`.
- `speckit.okr.review`: post-launch check-in with 0.0–1.0 scoring, guardrail checks, a leading-signal × KR diagnosis per initiative, and a persevere / iterate / pivot / stop decision.
- Optional hooks on `before_specify`, `after_specify`, and `after_plan`.
- KR cards, bounded follow-ups that don't count toward the question cap, and coaching for implausible targets and lagging-only KR sets in `frame`.
- `output.artifact_language` config option.
- KR chains (`Drives`): a leading KR that predicts a lagging one; `align` credits initiatives through the chain and `review` tests the link.
- `measure` checks feasibility (volume → observation period) and deadline conflicts, and invalidates baselines when a definition changes.
- `review` scores only readable KRs, supports contemporaneous (control-arm) baselines, and diagnoses per initiative and along the KR chain.
- `Framing Decisions` log in `okr.md`.
- From real-agent testing: parent-OKR ladder check, an adoption-as-outcome coaching smell, solution ideas collected in Boundaries (never scoped out by the agent), an `okr:<slug>` handoff token so `align` finds the framing, `protects G-n` initiatives, no inferred KR chains, visible assumptions for statistical claims, and a check-in calendar in the plan. Hook prompts now state their value.
- `okr-template` and `measurement-plan-template`, both overridable via presets.
