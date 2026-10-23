# Tasks: Onboarding guiado para equipos self-serve

**Input**: plan.md, spec.md (measurement detail in measurement-plan.md)

## Phase 1: Setup

- [ ] T001 Create `src/onboarding/` module structure per plan
- [ ] T002 [P] Add migrations for `onboarding_progress`, `project_templates`, `tour_views`

## Phase 2: Foundational — measurement baseline & attribution (blocks rollout)

- [ ] T003 Add optional `userId` to `track()` in src/analytics.ts without changing `distinctId`
- [ ] T004 Create GrowthBook experiment `guided-onboarding` (50/50, `plan=self_serve` in trial) in src/flags.ts
- [ ] T005 Emit `onboarding_exposed{variant}` and add `experimentVariant` to `trial_started` in src/teams/signup.ts
- [ ] T006 [P] Emit `member_joined{invitedVia}` when an invite is accepted in src/teams/signup.ts
- [ ] T007 [P] Add `source` to `member_invited` (wizard / checklist / bulk / settings) in src/teams/signup.ts
- [ ] T008 [P] Tag Zendesk tickets with `trial:true` for orgs in trial in src/support/zendesk.ts — **ship ≥ 2 weeks before rollout** (G-2 baseline)
- [ ] T009 [P] Compute G-1 baseline (D30 churn, last 90 days) from Stripe and record it in okr.md
- [ ] T010 Update docs/tracking-plan.md with all new events and properties
- [ ] T011 Build PostHog dashboard "Guided onboarding — OKR" (KR-1, KR-2 by arm and cohort; G-1, G-2 alerts)

**Checkpoint**: the experiment and the events are live in the control arm before any user sees the onboarding.

## Phase 3: User Story 1 - Checklist guiada (P1) 🎯 MVP / validation first

- [ ] T012 [US1] Derive checklist step state from `project_created`, `member_joined`, `task_completed` in src/onboarding/checklist.ts
- [ ] T013 [US1] Checklist UI with dismiss / reopen from help menu
- [ ] T014 [US1] Emit `onboarding_checklist_step_completed`, `onboarding_checklist_completed{daysSinceSignup}`, `onboarding_checklist_dismissed{stepsDone}`
- [ ] T015 [US1] Hide for sales-led orgs and non-admins (FR-001, FR-010)

**Checkpoint**: US-1 can run in the experiment by itself. First check-in reads its leading signal (SC-002).

## Phase 4: User Story 2 - Wizard (P2)

- [ ] T016 [US2] Two-step wizard (profile, invitations) in src/onboarding/wizard.ts; invitations sent with `source=wizard`
- [ ] T017 [US2] Offer integrations after first project

## Phase 5: User Story 3 - Plantillas (P2)

- [ ] T018 [P] [US3] Seed 3 templates in src/projects/templates.ts; pass `fromTemplate` (already tracked)

## Phase 6: User Story 4 - Tours (P3)

- [ ] T019 [US4] Tours per screen in src/onboarding/tours.ts; emit `tour_completed{tour, userId}`

## Phase 7: User Story 6 - Por rol (P3)

- [ ] T020 [US6] Role question at signup; add `role` to `team_created`; adapt checklist/tours in src/onboarding/roles.ts

## Phase 8: User Story 7 - Invitación masiva (P3)

- [ ] T021 [US7] Bulk invite by list/CSV in src/teams/bulkInvite.ts with `source=bulk`; emails never sent to analytics

## Phase 9: Rollout

- [ ] T022 Start experiment after T008 has ≥ 2 weeks of data; schedule check-ins (bi-weekly) per okr.md

## Dependencies

Phase 2 → all stories. US-1 is independent of US-2..US-7. US-6 depends on US-1 and US-4.
