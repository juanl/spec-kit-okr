# OKR Framing: Onboarding guiado para equipos self-serve

- **Slug**: self-serve-guided-onboarding
- **Status**: measuring
- **Created**: 2026-10-22
- **Horizon**: 2026-Q4 → 2027-Q1 (lanzamiento antes del 2027-01-15)
- **Feature spec**: specs/001-self-serve-guided-onboarding/spec.md
- **Parent objective**: O1 — Make self-serve a profitable growth channel (docs/okrs/2026-Q4.md)

## Objective

> Los equipos self-serve nuevos llegan a su primer resultado útil sin ayuda de soporte ni de ventas.

**Why now**: Entramos al segmento de cuentas chicas, donde el onboarding asistido no se paga solo, y queremos tener onboarding autoservicio antes que la competencia.

## Key Results

| ID | Key Result (outcome) | Metric | Baseline | Target | Deadline | Type | Leading/Lagging | Owner | Source |
|----|----------------------|--------|----------|--------|----------|------|-----------------|-------|--------|
| KR-1 | Más equipos self-serve deciden que el producto vale la pena pagarlo | % de la cohorte de trials self-serve que paga dentro de los 14 días | 9% (últimos 90 días) | 15% | 2027-03-31 | aspirational | lagging | Growth PM | Stripe + PostHog (`trial_started` → `subscription_started`) |
| KR-2 | Los equipos nuevos llegan a su primer resultado útil en la primera semana | % de equipos self-serve nuevos con ≥1 proyecto, ≥2 miembros que se unieron y ≥3 tareas completadas en 7 días | [NEEDS CLARIFICATION: 22% medía invitaciones enviadas; se re-mide con miembros que se unieron, usando el brazo control] | 45% | 2027-02-28 (was 2027-01-31; moved 2027-01-26, see Framing Decisions) | committed | leading | PM Onboarding | PostHog (`project_created`, `member_invited`, `task_completed`) |

## Impact Hypothesis

Creemos que un **onboarding guiado y autoservicio** para **equipos self-serve nuevos** va a hacer que **más equipos lleguen al primer resultado útil durante el trial** (KR-2), y que eso se traduzca en **más conversión a pago** (KR-1), porque **los competidores del segmento lo ofrecen** (todavía sin evidencia interna).

- **Confidence**: low — sin datos internos; la apuesta se basa en lo que hace la competencia
- **Riskiest assumption**: los trials no convierten porque no llegan a ver valor, y no por precio o fit. Si es falso, subir KR-2 no va a mover KR-1.

## Guardrails (Counter-metrics)

| ID | Metric | Current | Must not cross | Why it matters |
|----|--------|---------|----------------|----------------|
| G-1 | Churn D30 de cuentas self-serve convertidas | [NEEDS CLARIFICATION: medir antes del lanzamiento] | No superar la línea base | Conversión forzada que después se vuelve reembolsos y churn temprano |
| G-2 | Tickets de soporte de cuentas en trial (cada 100 trials) | [NEEDS CLARIFICATION: medir antes del lanzamiento] | No superar la línea base | La feature existe para que no haga falta ayuda; más tickets = falla el Objetivo |

## Boundaries

- **Out of scope (this horizon)**: cuentas sales-led; cambios de pricing o de duración del trial (si cambian en paralelo, no se puede atribuir el efecto al onboarding)
- **Constraints**: lanzamiento antes del 2027-01-15; un solo squad

## Candidate Initiatives

Ideas de solución que surgieron en el framing. No son decisiones: el spec las convierte en user stories y la alineación las rankea.

| ID | Idea | Expected KR | Raised by |
|----|------|-------------|-----------|
| CI-1 | Checklist guiada hasta el primer resultado útil | KR-2 | user |
| CI-2 | Plantillas de proyecto / datos de ejemplo | KR-2 | user |
| CI-3 | Wizard de configuración del equipo (perfil, integraciones, invitaciones) | KR-2 | user |
| CI-4 | Tours interactivos por pantalla | KR-2 | user |
| CI-5 | Videos educativos | KR-2 | user |
| CI-6 | Onboarding personalizado por rol | KR-2 | user |
| CI-7 | Invitación masiva de miembros | KR-2 | user |

**Validation first**: CI-1 — prueba de la forma más barata si llevar a los equipos a la activación (KR-2) sube la conversión (KR-1), que es el supuesto más riesgoso.

## Measurement Readiness

| ID | Measurable today? | Gap |
|----|-------------------|-----|
| KR-1 | yes | — |
| KR-2 | partially | Falta el evento `member_joined`; la línea base sale del brazo control |
| G-1 | yes | `subscription_canceled` existe; la línea base se calcula de los últimos 90 días |
| G-2 | partially | Tag `trial:true` en Zendesk ≥ 2 semanas antes del lanzamiento |

## Decision Rules

- **Check-in cadence**: quincenal
- **Persevere** if: score promedio ≥ 0.7 y sin guardrails rotos
- **Iterate** if: 0.4 ≤ score < 0.7
- **Pivot / Stop** if: score < 0.4 con el período de observación completo, o G-1/G-2 rotos

## Initiatives

Filled by `/speckit.okr.align` from the spec's user stories.

| Initiative | Priority | Moves | Hypothesis | Leading signal | Confidence | Status |
|------------|----------|-------|------------|----------------|------------|--------|
| US-1 Checklist guiada | P1 | KR-2 | Guiar los 4 pasos de activación hace que más equipos los completen | % de equipos que completan la checklist en 3 días | low | live |
| US-2 Wizard (perfil + invitaciones) | P2 | KR-2 | Invitar desde el día 1 acerca al umbral de ≥2 miembros | % de equipos con ≥2 invitaciones desde el wizard en el día 1 | low | iterating |
| US-3 Plantillas | P2 | KR-2 | Las tareas de ejemplo aceleran llegar a 1 proyecto y 3 tareas | % de primeros proyectos creados desde plantilla | low | live |
| US-4 Tours | P3 | KR-2 | Conocer el tablero reduce el abandono en la primera sesión | % de usuarios nuevos que terminan el tour del tablero | low | planned |
| US-6 Por rol | P3 | KR-2 | Pasos relevantes por rol suben la activación de no-admins | Activación a 7 días por rol vs. control | low | planned |
| US-7 Invitación masiva | P3 | KR-2 | Invitar de a muchos sube los miembros por equipo | % de invitaciones por lista/CSV | low | planned |
| ~~US-5 Videos~~ | — | none | — | — | — | dropped (out of scope) |

## KR Coverage

| KR / Guardrail | Success Criteria | Initiatives |
|----------------|------------------|-------------|
| KR-1 | SC-006 | indirecta, vía KR-2 |
| KR-2 | SC-002, SC-003 | US-1, US-2, US-3, US-4, US-6, US-7 |
| G-1 | SC-007 | — |
| G-2 | SC-008 | — |

## Framing Decisions

- 2027-01-26 — KR-2 deadline 2027-01-31 → 2027-02-28. Reason: the measurement plan's observation period (6 weeks from 2027-01-12) ends after the original deadline.

## Quality Gate

- [x] Objective is qualitative and free of metrics and solutions
- [x] Every KR is an outcome, not an output ("ship X" is an initiative, not a KR)
- [x] Every KR has metric, baseline, target, deadline, owner, and source
- [x] KR count within configured limits
- [x] At least one leading KR
- [x] At least one guardrail
- [x] Hypothesis links the feature to at least one KR
- [x] Low confidence has a validation-first initiative (or confidence is not low)

## Open Questions

- [NEEDS CLARIFICATION: línea base de G-1 y G-2 — se mide antes del lanzamiento (ver measurement plan)]

## Check-in History

| Date | KR scores | Guardrails | Initiative signals | Decision |
|------|-----------|------------|--------------------|----------|
| 2027-01-26 | KR-1 n/a (too early); KR-2 0.5 | G-1 unknown; G-2 ok | US-1 moved; US-2 flat; US-3 moved | Wait (feature); persevere US-1, US-3; iterate US-2 — [review](./okr-reviews/2027-01-26.md) |
