# Bet: H-1 — Compartir reportes con stakeholders

- **Team**: reporting
- **Period**: 2027-Q1
- **Hypothesis**: H-1 (in .specify/okr/teams/reporting/2027-Q1.md)
- **Key Results**: KR-1 (moved directly), KR-2 via Drives
- **Status**: validated
- **Simulation**: SIMULATED — `validated` viene del ensayo de review 2027-03-31 con datos hipotéticos; el estado real es `in_test` (US-1 no implementada). Revertir antes de usar el bet de verdad.
- **Spec(s)**: specs/001-stakeholder-report-sharing/spec.md
- **Created**: 2026-10-22

## Hypothesis

We believe that **darles a los managers una forma de hacer llegar un reporte a stakeholders sin cuenta en Teamboard** for **managers que informan el estado semanal a sus stakeholders** will cause **que dejen de mandar capturas de pantalla y compartan el reporte cada semana**, which we will see in **KR-1**, because **hoy ya mandan capturas para el estado semanal y CS recibe ~25 tickets/mes preguntando cómo compartir un reporte con alguien sin cuenta**.

- **Confidence**: medium — la evidencia (capturas, ~25 tickets/mes) muestra que la necesidad existe, pero no que vayan a usar una función integrada en lugar de capturas, ni cuántos managers activos mandan estado semanal
- **Riskiest assumption**: que suficientes managers activos envían estado semanal a stakeholders como para llegar al 30%
- **Expected contribution**: ~30 pp de los +30 pp de KR-1 (único bet sobre KR-1). El techo depende del % de managers activos que hoy mandan estado semanal: unknown — medir antes del P1 (p. ej. encuesta in-app a managers o muestra de tickets/entrevistas de CS). Dentro de 2027-Q1, el aporte a KR-1 global se limita a la fracción de managers en el piloto; los ~30 pp aplican tras escalar

## Validation

- **Validation slice (P1)**: un solo medio de compartir (la spec elige entre CI-1 y CI-2) para un solo tipo de reporte (`status`, el del estado semanal), detrás de un flag de GrowthBook para un grupo piloto de managers, con un evento de "reporte compartido" medido por usuario
- **Definición de "compartir"**: el reporte llega a un destinatario sin cuenta (enviado o abierto por él); una descarga sola no cuenta
- **Refuted if**: tras 6 semanas con la función disponible para el piloto, <12% de los managers activos del piloto comparte un reporte fuera de Teamboard por semana (score < 0.4 del target de 30%), o menos de la mitad de los que comparten lo hacen en ≥2 de las últimas 4 semanas
- **Scale slices (P2+)**: built only if the hypothesis holds after the validation slice

## Guardrails

Team guardrails TG-1 (rendimiento de la página de reportes) y TG-2 (exposición de datos de clientes) aplican.

| ID | Metric | Current | Must not cross | Why it matters |
|----|--------|---------|----------------|----------------|
| G-1 | Invitaciones de miembros por org (`member_invited`), piloto vs. control | unknown — medir desde PostHog antes del P1 | Caída relativa >10% vs. control (límite propuesto, sin referencia histórica) | Compartir no debe reemplazar a invitar; perderíamos asientos y expansión (C-KR-3, C-KR-1) |
| G-2 | Tickets/mes sobre compartir (incluida la función nueva) en orgs del piloto | ~25/mes en total (fuente sin confirmar; ver KR-2) | Por encima de la base actual, proporcional al piloto | La solución no debe generar más carga de soporte que el problema; protege KR-2 |

Gaming cubierto por la definición de "compartir": descargas, auto-envíos y envíos programados no abiertos no cuentan para KR-1.

## Candidate Ideas

Solution ideas raised during framing. They are not decisions: the spec chooses among them.

| ID | Idea | Raised by |
|----|------|-----------|
| CI-1 | Exportar los reportes del proyecto a PDF | user |
| CI-2 | Envío programado del reporte por email | user |

## Boundaries

- **Out of scope (this horizon)**: colaboración con stakeholders que ya tienen cuenta en Teamboard; comentarios o edición por destinatarios externos; prospects en el proceso de venta (KR-3, otro bet)
- **Constraints**: el piloto debe estar encendido a más tardar el 2027-02-17 para que las 6 semanas de validación terminen antes del 2027-03-31; TG-2 exige que nada quede expuesto a quien no sea el destinatario

## Measurement Readiness

| ID | Measurable today? | Gap |
|----|-------------------|-----|
| KR-1 | no | No existe evento de "reporte compartido"; además `track()` usa `distinctId: orgId` (src/analytics.ts), así que hoy no se puede contar *managers* individuales, solo organizaciones. Falta también definir "manager activo". |
| KR-2 | partially | Zendesk etiqueta `area:<area>` (src/support/zendesk.ts), pero no hay etiqueta específica para "compartir con alguien sin cuenta"; el ~25/mes no tiene fuente confirmada — unknown, se obtiene creando esa etiqueta (o contando una muestra de tickets `area:` de reportes) antes del primer check-in. |

## Decision Rules

- **Check-in cadence**: bi-weekly (igual que el equipo), con lectura final en la semana 6 del piloto
- **Validated** if: en la semana 6, ≥21% de los managers activos del piloto comparte por semana (score ≥ 0.7), ≥50% de los que comparten repite en ≥2 de las últimas 4 semanas, y ningún guardrail se rompe
- **Iterate** if: 12–21% (score 0.4–0.7), o uso presente pero repetición <50%
- **Refuted / stop** if: <12% semanal (score < 0.4), o se rompe G-1, G-2 o TG-1; **cualquier incidente de TG-2 detiene el piloto de inmediato**

## Stories

Filled by `/speckit.okr.align` from the spec.

| Story | Stage | Role in the bet | Leading signal | Status |
|-------|-------|-----------------|----------------|--------|
| US-1 | validation | Envío por email (puntual o semanal) del reporte `status` a destinatarios sin cuenta; produce el resultado de "Refuted if" | Managers del piloto que hacen su primer envío en los primeros 7 días; % de envíos que llegan a un destinatario sin cuenta | live (SIMULATED) |
| US-2 | scale | Extiende el envío a `burndown` y `workload` | Managers que comparten `burndown` o `workload` en su primera semana con la función | planned |
| US-3 | scale | CI-1: exportar a PDF y adjuntarlo a envíos | % de envíos con PDF adjunto (descargas solas no cuentan) | planned |

## Quality Gate

- [x] Hypothesis names a capability, users, a behavior change, and the KR it should show in
- [x] KR exists in the team set and is not dropped
- [x] Ladder: the KR contributes to a company KR, or is explicitly team-local
- [x] Refutation criterion is observable
- [x] Validation slice is defined (or confidence is high and this is stated)
- [x] At least one guardrail (bet or team)
- [x] Every KR involved has a baseline, or "unknown + how it will be obtained"

## Open Questions

- [NEEDS CLARIFICATION: % de managers activos que hoy mandan estado semanal a stakeholders — define el techo alcanzable de KR-1]
- Un envío manual semanal sigue siendo trabajo manual (O-1); la spec debería tenerlo en cuenta al elegir entre ideas. → Resuelto en la spec: P1 es envío programado por email.
- KR-1 se mide sobre todos los managers activos, pero el piloto (≤ 2027-02-17, solo algunas orgs) termina su lectura justo al cierre del período: aun validada H-1, KR-1 global al 2027-03-31 quedará cerca de (% de managers en el piloto × tasa del piloto). Decidir en el check-in: encender el piloto antes, ampliar el piloto, o ajustar KR-1 (con Change Log).

## Framing Decisions

- 2026-10-22 — KR objetivo: KR-1 (leading, Drives KR-2; team-local, vínculo con C-KR-3 débil) — elegido por el PM; el PDF es una vía para que el reporte llegue a alguien fuera de Teamboard
- 2026-10-22 — Ideas registradas: CI-1 PDF, CI-2 envío programado por email — aportadas por el PM; la spec elige entre ellas
- 2026-10-22 — Hipótesis con confianza media; % de managers con estado semanal desconocido — aceptado por el PM
- 2026-10-22 — "Compartir" = llega a un destinatario sin cuenta (descarga sola no cuenta); refutación <12% semanal o baja repetición tras 6 semanas; P1 = un medio, reporte `status`, piloto con flag — aceptado por el PM
- 2026-10-22 — Guardrails G-1 (canibalización de invitaciones, >10% vs control) y G-2 (tickets de compartir no suben) — aceptados por el PM
- 2026-10-22 — Límites y restricciones (piloto encendido ≤ 2027-02-17); sin ideas nuevas ni descartadas — aceptado por el PM
- 2026-10-22 — Reglas de decisión: bi-weekly, lectura en semana 6, umbrales 0.7/0.4 sobre target 30%, TG-2 = stop inmediato — aceptado por el PM
- 2026-10-23 — (SIMULATED) Review ensayada de semana 6: in_test → validated; US-1 → live; US-2/US-3 desbloqueadas, ampliar el flag condicionado a TG-1 — confirmada por el PM; revertir antes del uso real
- 2026-10-22 — Spec specs/001-stakeholder-report-sharing alineada (P1 = US-1 validación; US-2, US-3 scale); status framed → in_test; aporte a KR-1 global en Q1 acotado al piloto — /speckit-okr-align, aprobado por el PM

## Reviews

| Date | Verdict | KR scores | Guardrails | Decision | Review file |
|------|---------|-----------|------------|----------|-------------|
| 2027-03-31 (SIMULATED) | validated | KR-1 0.8 (piloto; global 0.2), KR-2 0.4 | TG-1 breached a nivel de equipo, no atribuible al bet (+4% piloto vs +3% control; residuo +1 pp sin verificar); G-1, G-2, TG-2 ok | US-1 live; desbloquear US-2 y luego US-3; ampliar el flag condicionado a TG-1 — confirmada por el PM | [okr-reviews/2027-03-31.md](../../../../../specs/001-stakeholder-report-sharing/okr-reviews/2027-03-31.md) |
