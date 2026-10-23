# Transcript — /speckit-okr-frame Onboarding guiado para equipos nuevos self-serve

**Contexto extraído antes de preguntar**
- `parent_okrs_file` = docs/okrs/2026-Q4.md → objetivos padre válidos: O1 (self-serve rentable), O2 (expansión enterprise).
- Código (solo lectura): trials de 14 días sin tarjeta (`src/billing/stripe.ts`); eventos `trial_started`, `team_created`, `member_invited`, `project_created`, `task_completed`, `subscription_started`, `subscription_canceled`; flags con GrowthBook.
- Sin `problem.md` de assess. Constitution sin completar (se ignora).
- Slug: `self-serve-guided-onboarding`.

---

**Q1 — Objective**: Cuando esto funcione, ¿qué va a ser distinto y para quién? ¿De qué objetivo de empresa cuelga?
Recomendado: A + padre O1 — el onboarding self-serve es palanca directa de "self-serve rentable".
| A | Los equipos self-serve nuevos llegan a su primer resultado útil sin ayuda de soporte ni ventas (→ O1) |
| B | Los admins logran que todo su equipo use el producto en la primera semana (→ O1) |
| C | Reducir el costo de CS en cuentas chicas (→ O1 KR2) |
**PM**: A

**Q2 — Objective (why now)**
Recomendado: B — el padre O1 habla de canal self-serve nuevo.
**PM**: Entramos al segmento self-serve donde el onboarding asistido no se paga solo, y no queremos que un competidor lo tenga antes. Lanzamiento antes del 15-01-2027.

**Q3 — Key Result (primary card)**: Si mirás un solo número al cierre, ¿cuál te dice que funcionó?
Recomendado:
- Outcome: más equipos self-serve deciden que el producto vale la pena pagarlo
- Metric: % de la cohorte de trials self-serve que paga dentro de los 14 días (`trial_started` → `subscription_started`)
- Baseline: unknown — capturar de Stripe/PostHog (últimos 90 días) antes del lanzamiento
- Target / deadline: +5 pp sobre baseline al 2027-03-31
- Type: aspirational · Lagging · Owner: Growth PM
**PM**: baseline 9% (Stripe, últimos 90 días), meta 80%.

↳ *Follow-up (coaching: implausible target; no cuenta para el tope)*: 80% está muy por encima del rango habitual de trials B2B sin tarjeta (≈15–25%). ¿Es aspiracional, o te referís a otra métrica (p. ej. activación)?
| A | Mantener 80% como aspiracional |
| B | Ajustar a 15% al 2027-03-31, aspiracional (≈ +6 pp, en el rango alto) |
| C | El 80% era de activación → lo tomamos como KR-2 |
**PM**: B, owner Growth PM.

**Q4 — Key Result (leading)**: KR-1 es lagging; el primer check-in no tendría señal. ¿Qué comportamiento temprano anticipa la conversión?
Recomendado card:
- Outcome: los equipos nuevos llegan a su primer resultado útil en la primera semana
- Metric: % de equipos self-serve nuevos que en 7 días tienen ≥1 proyecto, ≥2 miembros invitados y ≥3 tareas completadas (eventos existentes)
- Baseline: computable hoy desde PostHog con eventos existentes
- Target / deadline: 45% al 2027-01-31 · Type: committed · Leading · Owner: Product Manager Onboarding
**PM**: sí; baseline 22% según el funnel de PostHog.

**Q5 — Impact hypothesis**: ¿Por qué el onboarding guiado movería KR-1 y KR-2? ¿Qué evidencia hay?
| A | Las cuentas acompañadas por CS convierten más |
| B | Sin evidencia: apuesta por lo que hace la competencia |
| C | Datos de embudo / entrevistas |
**PM**: B. Ideas que tenemos: checklist guiada, plantillas de proyecto, wizard de configuración, tours por pantalla, videos, onboarding por rol, invitación masiva.
→ registradas como CI-1…CI-7. Confianza baja → *Validation first*: CI-1 (checklist hasta el primer resultado útil) — el modo más barato de probar si llegar a activación sube la conversión.

**Q6 — Guardrails**
| A | Churn D30 de cuentas convertidas |
| B | Tickets de soporte de trials |
| C | Ambos |
**PM**: C — no superar la línea base actual.

**Q7 — Boundaries**: ¿Qué queda explícitamente afuera y qué restricciones hay?
Recomendado: fuera cuentas sales-led y cambios de pricing/duración del trial (si cambian a la vez, no se puede atribuir el efecto).
**PM**: sí, y somos un solo squad.

**Q8 — Decision rules**
Recomendado: check-in quincenal; persevere ≥ 0.7, iterate 0.4–0.7, pivot/stop < 0.4 o guardrail roto.
**PM**: sí.

*8/8 preguntas primarias + 1 follow-up.*
