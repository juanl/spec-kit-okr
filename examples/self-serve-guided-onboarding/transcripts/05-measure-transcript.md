# Transcript — /speckit-okr-measure (after_plan hook)

**Discovery (read-only)**: PostHog via `track(orgId, …)` — distinctId is the org, events snake_case, props camelCase · `docs/tracking-plan.md` · GrowthBook flags · Stripe webhooks emit `subscription_started` / `subscription_canceled` · Zendesk tags `plan:` and `area:`, no trial status.

**Q1 — KR-2 definition**: "≥2 miembros invitados" admite dos lecturas.
| A | Invitaciones enviadas (`member_invited`, ya existe) |
| B | Miembros que aceptaron y entraron (no existe evento) |
Recomendado: B — un equipo de 1 persona con 2 invitaciones pendientes no llegó a "primer resultado útil" como equipo.
**PM**: B.
→ La línea base de 22% se calculó con invitaciones *enviadas*: hay que recalcularla con la definición nueva. Se marca la línea base de KR-2 para re-medir.

**Q2 — Volumen**: ¿Cuántos trials self-serve empiezan por semana?
**PM**: ~150.

**Q3 — Atribución**: KR-1 tiene que detectar 9% → 15%. Con ~150 trials por semana:
| A | A/B 50/50 con GrowthBook: ~460 trials por brazo → ~6 semanas para leer KR-1 |
| B | A/B 80/20 (holdout chico): el control llega a 460 recién en ~15 semanas, después del deadline de KR-2 |
| C | Before/after sin control: rápido, pero no aísla estacionalidad ni otros lanzamientos |
Recomendado: A, y escalar al 100% después de la primera lectura de KR-1.
**PM**: A.
