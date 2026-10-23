# Measurement Plan: Onboarding guiado para equipos self-serve

- **Feature directory**: specs/001-self-serve-guided-onboarding
- **OKR framing**: [okr.md](./okr.md)
- **Created**: 2026-10-22

## Metric Definitions

### KR-1: Más equipos self-serve deciden que el producto vale la pena pagarlo

- **Metric**: conversión a pago en 14 días
- **Definition**: orgs con `subscription_started` ≤ 14 días después de `trial_started` / orgs con `trial_started`, filtrado por `plan = self_serve`
- **Population**: trials self-serve iniciados después del lanzamiento, comparando el brazo `treatment` contra `control` del experimento `guided-onboarding`
- **Window**: por cohorte semanal de inicio de trial; una cohorte se puede leer recién 14 días después de cerrar
- **Baseline**: 9% (últimos 90 días, Stripe + PostHog)
- **Target**: 15% en el brazo treatment al 2027-03-31
- **Data source**: PostHog (eventos existentes)
- **Instrumentation needed**: ninguna para el KR; agregar `experimentVariant` a `trial_started` para segmentar
- **Owner**: Growth PM
- **Review cadence**: quincenal

### KR-2: Los equipos nuevos llegan a su primer resultado útil en la primera semana

- **Metric**: activación en 7 días
- **Definition**: orgs self-serve que, dentro de los 7 días posteriores a `trial_started`, tienen ≥1 `project_created`, ≥2 `member_joined` y ≥3 `task_completed` / orgs con `trial_started`
- **Population**: igual que KR-1
- **Window**: por cohorte semanal; lectura a los 7 días del cierre
- **Baseline**: [NEEDS CLARIFICATION: el 22% medía invitaciones *enviadas*; recalcular con miembros que se unieron. `member_joined` no existe, así que la línea base histórica no se puede reconstruir y se mide en el brazo control a partir del lanzamiento]
- **Target**: 45% en el brazo treatment al 2027-01-31
- **Data source**: PostHog
- **Instrumentation needed**: evento nuevo `member_joined`
- **Owner**: PM Onboarding
- **Review cadence**: quincenal

## Initiative Signals

| Initiative | Moves | Leading signal | Definition | Exposure | Event | Expected direction |
|------------|-------|----------------|------------|----------|-------|--------------------|
| US-1 Checklist | KR-2 | Checklist completada en 3 días | orgs con `onboarding_checklist_completed` ≤ 3 días / orgs expuestas | orgs treatment | `onboarding_checklist_completed` (nuevo) | up (SC-002: 60%) |
| US-2 Wizard | KR-2 | ≥2 invitaciones desde el wizard en el día 1 | orgs con ≥2 `member_invited{source=wizard}` el día 1 / orgs que abrieron el wizard | orgs treatment | `member_invited.source` (prop nueva) | up |
| US-3 Plantillas | KR-2 | Primer proyecto desde plantilla | primeros `project_created` con `fromTemplate != null` / primeros proyectos | orgs treatment | `project_created.fromTemplate` (existe) | up |
| US-4 Tours | KR-2 | Tour del tablero terminado | usuarios con `tour_completed{tour=board}` / usuarios nuevos | usuarios de orgs treatment | `tour_completed` (nuevo, **requiere userId**) | up |
| US-6 Por rol | KR-2 | Activación por rol | activación a 7 días por `role` | orgs treatment | `role` en `team_created` (prop nueva) | up vs. sin rol |
| US-7 Invitación masiva | KR-2 | Invitaciones por lista/CSV | `member_invited{source=bulk}` / `member_invited` | orgs treatment | `member_invited.source` (prop nueva) | up |

## Guardrails

| ID | Metric | Definition | Limit | Alerting |
|----|--------|------------|-------|----------|
| G-1 | Churn D30 | `subscription_canceled` ≤ 30 días después de `subscription_started` / convertidas, por brazo | treatment ≤ control | Alerta semanal si treatment > control + 2 pp |
| G-2 | Tickets cada 100 trials | tickets con tag `trial:true` / trials activos × 100, por brazo | treatment ≤ control | Alerta semanal si treatment > control × 1.2 |

## Instrumentation Inventory

| Event / Signal | Properties | Fires when | Feeds | Exists? |
|----------------|------------|------------|-------|---------|
| trial_started | plan, trialDays, **experimentVariant** | Alta | KR-1, KR-2, attribution | yes (+ prop) |
| subscription_started | plan | Webhook de Stripe | KR-1 | yes |
| subscription_canceled | plan | Webhook de Stripe | G-1 | yes |
| project_created | fromTemplate | Proyecto creado | KR-2, US-3 | yes |
| task_completed | projectId | Tarea completada | KR-2 | yes |
| member_invited | **source** (wizard / checklist / bulk / settings) | Invitación enviada | US-2, US-7 | yes (+ prop) |
| **member_joined** | invitedVia | Un invitado acepta y entra | KR-2 | no |
| **onboarding_exposed** | variant | La org entra al flujo (o al control) | attribution | no |
| **onboarding_checklist_step_completed** | step | Se completa un paso | US-1 | no |
| **onboarding_checklist_completed** | daysSinceSignup | Se completan los 4 pasos | US-1, SC-002 | no |
| **onboarding_checklist_dismissed** | stepsDone | El admin la descarta | US-1 (diagnóstico) | no |
| **tour_completed** | tour, **userId** | Termina un tour | US-4 | no |
| team_created | plan, **role** | Alta | US-6 | yes (+ prop) |
| Zendesk tag **trial:true** | — | Ticket de una org en trial | G-2 | no |

**Identity gap**: `track()` usa `orgId` como `distinctId`. Las señales por usuario (US-4, US-6) necesitan `userId` como propiedad. Se agrega `userId` opcional a `track()` sin cambiar el `distinctId`, para no romper los funnels existentes.

**Privacy**: no se mandan emails a PostHog. `member_invited` y `member_joined` llevan solo IDs. La importación por CSV (US-7) procesa emails solo del lado del servidor.

## Baseline Capture

- [ ] KR-2: no hay línea base histórica con `member_joined`; se usa el brazo control desde el día 1 como línea base contemporánea.
- [ ] G-1: calcular el churn D30 de los últimos 90 días (Stripe) antes del lanzamiento.
- [ ] G-2: empezar a etiquetar `trial:true` al menos 2 semanas antes del lanzamiento para tener línea base.

## Rollout & Attribution

- **Strategy**: experimento A/B 50/50 en GrowthBook (`guided-onboarding`), solo orgs `self_serve` en trial
- **Why this strategy**: aísla el efecto del onboarding de la estacionalidad y de otros lanzamientos; con ~150 trials por semana, ~460 por brazo tarda ~6 semanas, que es lo necesario para detectar 9% → 15%
- **Minimum observation period**: 6 semanas de cohortes + 14 días para la última cohorte (KR-1); 7 días para KR-2
- **After**: escalar al 100% después de la primera lectura positiva de KR-1, con un holdout del 10% hasta el deadline

## Dashboard / Report

- **Where**: PostHog, dashboard "Guided onboarding — OKR"
- **Shows**: KR-1 y KR-2 por brazo y cohorte; señales de iniciativas; G-1 y G-2 con umbrales
