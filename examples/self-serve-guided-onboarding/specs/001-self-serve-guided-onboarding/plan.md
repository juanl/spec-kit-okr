# Implementation Plan: Onboarding guiado para equipos self-serve

**Branch**: `001-self-serve-guided-onboarding` | **Date**: 2026-10-22 | **Spec**: [spec.md](./spec.md)

## Summary

Checklist guiada (P1) sobre los eventos de dominio existentes, wizard corto e invitaciones (P2), plantillas (P2), y tours, onboarding por rol e invitación masiva (P3). Todo detrás de un flag de GrowthBook, restringido a organizaciones self-serve en trial.

## Technical Context

**Language/Version**: TypeScript 5 / Node 20
**Primary Dependencies**: Express 4, posthog-node, stripe, @growthbook/growthbook
**Storage**: Postgres (tablas nuevas: `onboarding_progress`, `project_templates`, `tour_views`)
**Testing**: vitest
**Target Platform**: web (SPA + API)
**Constraints**: lanzamiento antes del 2027-01-15; un squad

## Constitution Check

Constitution sin completar en este repo de ejemplo: no hay gates para evaluar.

## Project Structure

```text
src/
├── onboarding/
│   ├── checklist.ts      # US-1: derive step state from domain events
│   ├── wizard.ts         # US-2
│   ├── tours.ts          # US-4
│   └── roles.ts          # US-6
├── projects/templates.ts # US-3
└── teams/bulkInvite.ts   # US-7
```

## Phases

1. **Foundation**: flag `guided-onboarding` (GrowthBook), solo para `plan=self_serve` y en trial; tabla `onboarding_progress`.
2. **US-1 Checklist**: suscribir el estado de los pasos a `project_created`, `member_invited`, `task_completed`; UI de checklist; descartar/reabrir.
3. **US-2 Wizard** (perfil + invitaciones) y **US-3 Plantillas**.
4. **US-4 Tours**, **US-6 Roles**, **US-7 Invitación masiva**.

## Complexity Tracking

Ninguna.

## Measurement & Instrumentation

See [measurement-plan.md](./measurement-plan.md). This work is part of the feature's Definition of Done.

- **Instrumentation**: `experimentVariant` en `trial_started` (atribución); `member_joined` (KR-2); `source` en `member_invited` (US-2, US-7); eventos `onboarding_checklist_*` (US-1); `tour_completed` + `userId` opcional en `track()` (US-4); `role` en `team_created` (US-6); actualizar `docs/tracking-plan.md`
- **Baseline capture**: tag `trial:true` en Zendesk ≥ 2 semanas antes del lanzamiento (G-2); churn D30 de los últimos 90 días (G-1); control contemporáneo para KR-2
- **Rollout / attribution**: experimento GrowthBook `guided-onboarding` 50/50 en trials self-serve, ~6 semanas, después 100% con holdout del 10%
- **Guardrail monitoring**: G-1 treatment ≤ control + 2 pp; G-2 treatment ≤ control × 1.2; alerta semanal
- **Dashboard**: PostHog "Guided onboarding — OKR"
