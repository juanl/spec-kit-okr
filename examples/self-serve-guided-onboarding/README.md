# Example: guided onboarding for self-serve teams

End-to-end run of the extension on a fictional B2B SaaS ("Teamboard": PostHog, Stripe, GrowthBook, Zendesk), with `output.artifact_language: es`.

| Step | Command | Output |
|------|---------|--------|
| 1 | `/speckit.okr.frame` | [transcript](transcripts/01-frame-transcript.md): 8 primary questions + 1 coaching follow-up; parent objective taken from [parent-okrs-2026-Q4.md](parent-okrs-2026-Q4.md) |
| 2 | `/speckit.specify` | [spec.md](specs/001-self-serve-guided-onboarding/spec.md) with 7 user stories |
| 3 | `/speckit.okr.align` | [transcript](transcripts/03-align-transcript.md): user stories ranked as initiatives; wizard P1→P2, tours P2→P3, videos dropped; SCs added for KR-1 and the guardrails |
| 4 | `/speckit.plan` | [plan.md](specs/001-self-serve-guided-onboarding/plan.md) (abbreviated) |
| 5 | `/speckit.okr.measure` | [transcript](transcripts/05-measure-transcript.md) → [measurement-plan.md](specs/001-self-serve-guided-onboarding/measurement-plan.md): identity gap, missing `member_joined`, 50/50 A/B sized to the volume |
| 6 | `/speckit.tasks` | [tasks.md](specs/001-self-serve-guided-onboarding/tasks.md): instrumentation as Phase 2, gating the rollout |
| 7 | `/speckit.implement` | not run (core command) |
| 8 | `/speckit.okr.review` | [check-in 2027-01-26](specs/001-self-serve-guided-onboarding/okr-reviews/2027-01-26.md) with simulated data: Wait at feature level, iterate on US-2 |

The resulting OKR framing is [okr.md](specs/001-self-serve-guided-onboarding/okr.md).

This run was produced with v0.1.0 before the last round of fixes (KR chains, deadline checks, readable-only scoring). Some sections differ slightly from what the current commands produce; for example, the `Drives` column is missing from the KR table.
