# Real-agent transcript (Claude Code, headless)

PM answers came from a fixed fact sheet; the agent ran the installed okr commands. Company OKRs were served by the mock MCP server in `tools/mock-okr-mcp`.


## >>> USER (19:04:10)

/speckit-okr-review Hoy es 2027-03-31, semana 6 del piloto (arrancó 2027-02-17, ~300 managers en el piloto, holdout de control comparable). Datos del piloto: 24% de los managers activos compartió el reporte status por email cada semana (promedio últimas 4 semanas); 58% de los que comparten repitió en 2 o más de las últimas 4 semanas. Control: 0%. G-1 invitaciones: -3% vs control. G-2 tickets sobre compartir en orgs piloto: bajaron 30% vs su base. TG-1 p75 reportes: +4%. TG-2: 0 incidentes. KR-1 global (todos los managers): 6%.

## <<< AGENT

No escribí nada todavía. Antes de registrar un veredicto, hay algo que no cierra entre tus datos y el repo.

## El repo no muestra que el piloto se haya lanzado

- **Fecha**: decís que hoy es 2027-03-31, pero el entorno marca 2026-10-22, el mismo día en que se crearon el set, el bet y la spec.
- **No existe el pipeline de lanzamiento**: no hay `plan.md`, `tasks.md` ni `measurement-plan.md` en `specs/001-stakeholder-report-sharing/`. La spec sigue en `Draft` y US-1 está `planned` en el bet.
- **No hay forma de medir por manager**: `src/analytics.ts:7` sigue mandando `distinctId: orgId` y no hay ningún evento de "reporte compartido". Con el código actual no se puede calcular "24% de los managers activos". El bet ya lo marcaba como bloqueante de KR-1.
- **Faltan las definiciones**: sin `measurement-plan.md` no hay definición de "manager activo", ni período de observación, ni percentil de TG-1.

Registrar un veredicto con estos números dejaría en el bet y en el set del equipo resultados que nada en el repo respalda.

**¿Qué es esto?**
1. **Un ensayo o simulación**: hago la lectura completa en el chat y no escribo nada. O la escribo marcada como `simulated`, si querés.
2. **Un piloto real cuyos artefactos están en otro repo o rama**: pasame el `FEATURE_DIR` o el `measurement-plan.md` y hago la review formal.

## Lectura provisional (tomando tus números tal cual, sin registrar nada)

| Ítem | Valor | Lectura |
|---|---|---|
| KR-1 en el piloto (baseline = control 0%) | 24% | score **0.8**, por encima del umbral de 21% |
| Repetición (≥2 de 4 semanas) | 58% | ✅ cumple el ≥50% |
| G-1 invitaciones vs control | −3% | ✅ dentro del límite de −10% |
| G-2 tickets de compartir en el piloto | −30% vs su base | ✅ |
| **TG-1 carga de la página de reportes (p75)** | **+4%** | ⚠️ **se rompe**: el límite es "sin regresión" |
| TG-2 incidentes | 0 | ✅ |
| KR-1 global | 6% | score 0.2 al cierre del período |

Por las señales, H-1 quedaría **validated**. Pero **TG-1 tiene prioridad sobre el veredicto**: las reglas de decisión del bet dicen que si se rompe TG-1 se para. Para saber si esa regresión la causa la función, necesito el p75 del grupo de control en el mismo período. Además, el set pide un percentil (sugiere p95) que nunca se fijó, y vos reportás p75.

Si el +4% es propio del piloto, la recomendación sería arreglar el rendimiento de US-1 antes de escalar. US-2 y US-3 quedarían bloqueadas hasta que TG-1 vuelva a la línea base, aunque las señales validen la hipótesis.

**Decisiones de calendario que vencen hoy**, aunque se resuelven en el check-in y no en esta review:
- **El deadline de KR-1 es hoy**. El 6% global cierra el período en 0.2. Era previsible, porque solo el piloto tenía la función, y el bet pedía decidirlo en el check-in.
- **KR-2** necesita el valor absoluto de tickets/mes de todas las orgs, no solo el −30% del piloto.
- **El holdout de control**: falta decidir si sigue o termina.

**Para avanzar necesito:**
1. ¿Ensayo, o piloto real con artefactos en otro lado?
2. El p75 (o p95) de TG-1 en el grupo de control.
3. Tickets/mes totales para KR-2.
4. ¿Qué aprendieron sobre el supuesto más riesgoso, es decir, cuántos managers activos mandan estado semanal?


## >>> USER (19:05:32)

1: es un ensayo, escribilo marcado simulated. 2: el p75 del control subió 3% en el mismo período. 3: 19 tickets/mes en total. 4: una encuesta dice que 35% de los managers activos manda estado semanal.

## <<< AGENT

La review ensayada quedó escrita en `specs/001-stakeholder-report-sharing/okr-reviews/2027-03-31.md`, marcada **SIMULATED** al principio. No toqué el bet ni el set del equipo: para no mezclar datos simulados con los reales, los cambios que se harían quedaron solo como propuesta al final del archivo.

## Scorecard

| | Valor | Score / estado |
|---|---|---|
| KR-1 en el piloto | 24% vs control 0% | **0.8** |
| KR-1 en todos los managers | 6% | 0.2 |
| KR-2 | 25 → 19 tickets/mes | **0.4** |
| Repetición | 58% | ✅ (≥50%) |
| G-1 (invitaciones) / G-2 (tickets sobre compartir) / TG-2 (incidentes) | −3% / −30% / 0 | ok |
| TG-1 (p75 de la página de reportes) | piloto +4%, control +3% | **roto a nivel de equipo**; la función explica ≈ +1 pp |

## Veredicto: **validated**, con TG-1 como condición

- **El bet pasa:** se cumplen sus dos criterios de validación y ninguno de refutación.
- **TG-1 no frena:** el control subió +3% en el mismo período, así que la mayor parte de la regresión viene de la plataforma y no de la función. Queda un residuo de ≈ +1 pp que no está verificado: puede ser ruido o un costo real de la opción de envío. Por eso no aplico la regla de stop del bet, pero sí condiciono el escalado.

## Decisión recomendada (falta tu confirmación)

1. Mantener US-1 live en el piloto.
2. Desbloquear US-2 y después US-3.
3. Antes de ampliar el flag fuera del piloto, verificar o eliminar el +1 pp de TG-1.
4. Pasar H-1 a `validated`.

En el archivo la decisión figura como `[NEEDS CLARIFICATION]` hasta que la confirmes o la cambies.

## Aprendizaje

El supuesto más riesgoso se sostiene, pero con poco margen. Si el 35% de los managers activos manda estado semanal, el techo queda apenas sobre el target de 30%. En el piloto ya comparte cerca del 69% de ese grupo; llegar a 30% de todos los managers exigiría que lo haga ≈ 86%. US-2 (más tipos de reporte) es lo que puede ampliar esa base.

## Pendientes

- **Señales de US-1 sin datos:** primer envío en los primeros 7 días y % de envíos que llegan a un destinatario sin cuenta. Hasta medirlas, US-1 no se puede acreditar por sí sola.
- **Percentil de TG-1:** sigue sin fijarse en el set. Sugiere p95 y vos reportaste p75.
- **Check-in del equipo vencido:** el set no tiene ninguno y la cadencia es de 14 días. Hoy vencen KR-1 y KR-2, se cierra el período y hay que decidir si el holdout de control sigue durante el escalado. Ahí también se lleva la regresión de plataforma de TG-1. La review no cambia ningún target.

**Siguiente paso:** con tu confirmación, `/speckit-implement` para US-2. Antes, en un caso real, faltarían `/speckit-plan` y `/speckit-okr-measure`, que todavía no existen para esta spec. Próxima review: **2027-04-14**. Además corresponde `/speckit-okr-checkin`, que ya está vencido.

¿Confirmás la decisión, o la cambiás?


## >>> USER (14:07:58)

Confirmo la decisión. Para seguir el ensayo aplicá los cambios al bet y al set del equipo, marcados como simulated.

## <<< AGENT

Apliqué los cambios al bet y anoté tu decisión en la review. El set del equipo todavía no lo toqué: su write policy es `confirm`, así que tengo que mostrarte el cambio exacto y esperar tu sí.

## Cambios aplicados al bet (`bets/H-1-stakeholder-report-sharing.md`)

- **Status**: `in_test` → `validated`, más una línea `Simulation` justo abajo. Esa línea aclara que es un ensayo, que el estado real es `in_test` y que hay que revertirlo antes del uso real.
- **US-1**: `planned` → `live (SIMULATED)`. US-2 y US-3 siguen `planned`: quedan desbloqueadas, pero todavía no se construyeron.
- **Reviews**: agregué la fila `2027-03-31 (SIMULATED)` con el veredicto, los scores, TG-1 y tu decisión, enlazada a la review.
- **Framing Decisions**: agregué la entrada del 2026-10-23 marcada SIMULATED.

Dejé el valor `validated` sin marca dentro del campo para que los comandos lo sigan leyendo bien; la marca va en la línea de al lado. La contra es que `/speckit-okr-status` y `/speckit-okr-checkin` lo van a tomar como validado.

## Cambios propuestos para el set del equipo (`teams/reporting/2027-Q1.md`), pendientes de tu sí

**Hypotheses**, fila H-1, columna Status:
```diff
- | ... | specs/001-stakeholder-report-sharing | in_test |
+ | ... | specs/001-stakeholder-report-sharing | validated |
```

**Key Results**, columna Current (no cambio Score ni Status: eso lo hace el check-in):
```diff
KR-1  Current: 0%      →  6% (SIMULATED; piloto 24%)
KR-2  Current: ~25/mes →  19/mes (SIMULATED)
```

**Change Log**, entrada nueva:
```
- 2026-10-23 — (SIMULATED) H-1 in_test → validated; KR-1 Current 6% (piloto 24%), KR-2 Current 19/mes — ensayo de /speckit-okr-review 2027-03-31 con datos hipotéticos, confirmado por el PM; revertir antes del uso real
```

No toco targets, deadlines, guardrails ni el set de la compañía, que está en MCP con policy `propose` y no tiene nada que proponer desde esta review.

Ojo: después de aplicarlo, el set real del equipo va a mostrar valores ensayados. Si lo vas a usar de verdad, convendría hacer el ensayo en una rama, para descartarlo con `git` en vez de revertirlo a mano.

¿Aplico estos tres cambios al set del equipo?


## >>> USER (14:08:51)

Sí, aplicalos.

## <<< AGENT

Apliqué los tres cambios en `.specify/okr/teams/reporting/2027-Q1.md`, tal como te los mostré:

- **H-1**: `in_test` → `validated`.
- **KR-1 Current**: `6% (SIMULATED; piloto 24%)`. **KR-2 Current**: `19/mes (SIMULATED)`. Score y Status siguen igual, porque eso lo actualiza el check-in.
- **Change Log**: agregué la entrada del 2026-10-23 marcada SIMULATED.

En la review también dejé anotado que los cambios al set se aplicaron con tu confirmación.

Con esto el ensayo de la review está completo en los tres archivos: la review, el bet y el set del equipo. Todo lo que viene de datos hipotéticos está marcado SIMULATED. Nada de esto está commiteado: el set y el bet siguen sin trackear en git. Si querés un punto para volver atrás antes de seguir con el ensayo, convendría commitearlos o pasarlos a una rama.

Para seguir con el ensayo:
- **`/speckit-okr-checkin`**: está vencido. Ese check-in cierra KR-1 y KR-2, que vencen el 2027-03-31, y ahí entran la regresión de plataforma de TG-1 y la decisión sobre el holdout de control.
- **Próxima review: 2027-04-14**, para verificar el residuo de +1 pp de TG-1 antes de ampliar el flag fuera del piloto.

Guardé en memoria que hacés ensayos con datos hipotéticos y que preferís marcar todo como SIMULATED.


## >>> USER (14:10:08)

/speckit-okr-checkin close KR-3 = 2 deals perdidos con reporting en Q1 (SIMULATED). El resto de valores ya los tenés.

## <<< AGENT

Este es el check-in de cierre ensayado. Los valores salen de la review simulada, más el KR-3 que me pasaste. Todavía no escribí nada en el set del equipo. Lo único que actualicé es el espejo local de los OKRs de la compañía, que el check-in exige refrescar cada vez que se lee okr-tool.

## OKR check-in — team reporting 2027-Q1 — 2027-03-31 (SIMULATED, close)

| KR | Current | Score | Status (was → now) | Hypotheses |
|----|---------|-------|--------------------|------------|
| KR-1 | 6% global (24% en el piloto) | **0.2** | not_started → **at_risk** | H-1 `validated`; US-2 desbloqueada, el escalado todavía no empezó |
| KR-2 (committed) | 19/mes | **0.4** | not_started → **at_risk** | Ninguna propia; depende de H-1 vía Drives |
| KR-3 | 2 deals/trimestre | **0.5** | not_started → **off_track** | Ninguna. Recomiendo hacer frame de una para 2027-Q2 |

**Sobre los estados que propongo:**
- **KR-1**: la tabla de la skill daría `on_track`, porque hay un bet validado con el escalado en marcha. No la sigo: el período cierra con 0.2, el target no se alcanzó y las scale stories ni empezaron. `on_track` quedaría registrado como un éxito que no fue. `at_risk` deja constancia de que no se llegó, aunque haya un camino validado.
- **KR-2**: es committed, así que se esperaba 1.0. La cadena con KR-1 está sana: los dos se movieron (−30% de tickets en las orgs del piloto). La fuente del baseline (~25/mes) sigue sin confirmarse.
- **KR-3**: con n≈3 es direccional, y 2 contra 3 no es una señal. No hay ninguna hipótesis detrás, así que `off_track`.

**Guardrails** (para el registro, sin cambio de estado):
- TG-1: roto a nivel de equipo. El piloto subió +4% y el control +3%; casi toda la regresión viene de la plataforma. El percentil sigue sin fijarse.
- TG-2: 0 incidentes.

**Cambios en la compañía (vistos en okr-tool):**
- La propuesta de reporting quedó **accepted**: ahora existe **C-KR-4 "New enterprise ARR"** ($90k de $250k, `at_risk`).
- KR-3 sigue figurando como `team-local`. Vincularlo con C-KR-4 es un cambio del set que va por `/speckit-okr-set`, no por el check-in.

**Proposals to company**: 0. Ningún KR del equipo contribuye hoy a un KR de la compañía, así que no hay nada que subir. · **Orphans**: 0. · **Stale bets**: 0. La review de H-1 es del 2027-03-31.

## Lo que escribiría en `teams/reporting/2027-Q1.md` (policy `confirm`)

1. **Key Results**:
   - KR-3 Current pasa a `2/trimestre (SIMULATED)`.
   - Los scores quedan 0.2 / 0.4 / 0.5 y los estados como en la tabla de arriba.
2. **Check-in History**: una fila con fecha `2027-03-31 (SIMULATED)`, con scores, hipótesis, guardrails y decisiones.
3. **Proposals to Company**: la propuesta del 2026-10-22 pasa de `open` a `accepted` (C-KR-4).
4. **Period Close**: sección nueva según el template.
   - Scores finales.
   - Aprendizajes: H-1 validada en el piloto (24%, 58% de repetición). El techo es de alrededor de 35% de los managers, poco margen sobre el target de 30%. TG-1 se degrada a nivel de plataforma.
   - Carry-over (ver la pregunta de abajo).
5. **Header**:
   - `Last check-in: 2027-03-31`.
   - `Status: active → closed`.
   - Una línea `Simulation` que aclara que es un ensayo con fecha real 2026-10-23.
6. **Change Log**: una entrada (SIMULATED) con el cierre.

No toco targets, deadlines, bets ni specs, y no hay nada para escribir en la compañía.

**Dos decisiones:**
1. **¿Aplico todo, elijo algunos cambios o ninguno?** Si querés `on_track` en KR-1, como dice la tabla literal, decímelo.
2. **Carry-over de H-1**: recomiendo pasarla a **2027-Q2** para escalar US-2, con la condición de TG-1. La alternativa es cerrarla en Q1.


## >>> USER (14:11:02)

Aplicá todo, con at_risk en KR-1. H-1 pasa a 2027-Q2.

## <<< AGENT

Apliqué todo en `.specify/okr/teams/reporting/2027-Q1.md`, con KR-1 en `at_risk`. El período 2027-Q1 quedó **cerrado** en el ensayo.

## OKR check-in — team reporting 2027-Q1 — 2027-03-31 (SIMULATED, close)

| KR | Score | Status (was → now) | Hypotheses |
|----|-------|--------------------|------------|
| KR-1 | 0.2 | not_started → at_risk | H-1 validated → 2027-Q2 |
| KR-2 | 0.4 | not_started → at_risk | Ninguna propia (depende de KR-1 vía Drives) |
| KR-3 | 0.5 | not_started → off_track | Ninguna |

**Proposals to company**: 0 · **Orphans**: 0 · **Stale bets**: 0
**Next check-in**: ninguno en 2027-Q1, porque el set está cerrado. La próxima fecha es la review de H-1 del 2027-04-14, dentro del set de Q2.

**Cambios en el set:**
- **Encabezado**: `Status: closed`, `Last check-in: 2027-03-31` y una línea `Simulation` que aclara que es un ensayo y que el estado real es `active` sin check-ins.
- **Key Results**: valores actuales, scores y estados. KR-3 quedó en `2/trimestre (SIMULATED)`.
- **Check-in History**: una fila con la decisión de poner KR-1 en `at_risk` en vez de `on_track`.
- **Proposals to Company**: la propuesta del 2026-10-22 quedó `accepted`, porque la compañía agregó C-KR-4.
- **Period Close**: scores finales, aprendizajes y carry-over. H-1 pasa a 2027-Q2 y KR-3 necesita una hipótesis y el vínculo con C-KR-4.
- **Change Log**: una entrada SIMULATED.

No hubo escrituras en la compañía, porque no había nada que proponer. No toqué el bet ni la spec. El status de H-1 sigue en `validated`, como dejó la review, y su paso a Q2 quedó registrado en Period Close.

**Siguientes pasos:**
1. **`/speckit-okr-set period=2027-Q2`**: crea el set nuevo. Ahí se agregan H-1 para seguir con el escalado, el vínculo de KR-3 con C-KR-4 y el percentil de TG-1, que todavía falta fijar.
2. **`/speckit-okr-frame`** sobre el KR de Q2 que reemplace a KR-3.

Todos los cambios del ensayo siguen sin commitear: la review, el bet, el set del equipo y el espejo de la compañía. Si los commiteás en una rama aparte, después podés descartar el ensayo de una vez en vez de revertir a mano las entradas marcadas SIMULATED.


## >>> USER (14:11:35)

/speckit-okr-status

## <<< AGENT

Esta vista es solo de lectura. Lo único que escribí fue la marca `Synced at` del espejo de la compañía, después de leer okr-tool; los datos no cambiaron.

```text
2027-Q1 · team reporting · status closed (SIMULATED) · last team check-in 2027-03-31 (SIMULATED; fecha real 2026-10-23)
company · mcp:okr-tool · last company check-in 2026-10-20 (OK, cadence 30d) · mirror synced 2026-10-23T17:11Z

C-KR-1 Self-serve new MRR $18k → $40k               at_risk    (sin contribuciones de reporting)
C-KR-2 Self-serve CAC payback 9 → <6 meses          at_risk    (sin contribuciones de reporting)
C-KR-3 NRR enterprise 108% → ≥115%                  on_track   (sin contribuciones; KR-1 tiene un vínculo débil)
C-KR-4 New enterprise ARR $0 → $250k                at_risk    (KR nuevo; KR-3 todavía no está vinculado)

KR-1 Managers comparten cada semana 0% → 30%       at_risk   score 0.2   (team-local) [SIMULATED]
   └─ H-1 Envío por email reemplaza capturas        validated  review: validated (2027-03-31, SIMULATED) · pasa a 2027-Q2
      └─ specs/001-stakeholder-report-sharing       spec Draft · sin plan.md · sin tasks.md · P1 "live" (SIMULATED) · P2/P3 desbloqueadas, no empezadas
KR-2 Tickets sobre compartir ~25 → ≤10/mes          at_risk   score 0.4   (team-local) [SIMULATED]
   └─ (sin hipótesis propia; depende de KR-1 vía Drives)
KR-3 Deals enterprise perdidos 3 → ≤1/trimestre     off_track score 0.5   (team-local) [SIMULATED]
   └─ (no hypothesis)                                ⚠ KR without a bet
```

## Findings

**Ensayo contra estado real.** Esto es lo más importante.
- El árbol muestra H-1 `validated` y US-1 `live`, pero la spec sigue en Draft, sin `plan.md`, sin `tasks.md` y sin instrumentación. En el código, `src/analytics.ts` todavía mide por organización.
- El set del equipo figura `closed`, con un check-in de una fecha futura.
- Todo eso viene del ensayo. Cualquier comando que lea estos archivos, incluido este, lo toma como real.
- → Commitear el ensayo en una rama y volver al estado real en la principal (`git` a mano; no hay un comando okr para esto).

**Stale**
- Ningún set está vencido. La compañía tuvo check-in hace 3 días (cadencia 30) y el espejo está al día.
- Dentro de la línea de tiempo simulada (2027-03-31), el check-in de la compañía tendría 162 días: → `/speckit-okr-checkin level=company`.

**Orphans**: ninguno.

**Gaps**
- **Falta el set de 2027-Q2**: H-1 pasa a 2027-Q2, pero ese set todavía no existe. → `/speckit-okr-set period=2027-Q2`
- **KR-3 sin hipótesis**: cerró `off_track` y no hay ningún bet sobre él. → `/speckit-okr-frame kr=KR-3`, una vez creado el set de Q2.
- **La spec no tiene plan ni medición**: sin `measurement-plan.md` no hay definiciones (por ejemplo, "manager activo"), ni evento por manager, ni calendario de reviews. → `/speckit-plan`, seguido de `/speckit-okr-measure`.
- **KR-2 sin hipótesis propia**: es aceptable mientras dependa de KR-1, pero es committed y cerró en 0.4. → Decidirlo en `/speckit-okr-set period=2027-Q2`.
- **Escalar antes de validar**: no aplica. P2 y P3 no están implementadas.

**Ladder**
- KR-3 sigue como `team-local`, aunque ya existe C-KR-4 (New enterprise ARR). → Vincularlo en `/speckit-okr-set period=2027-Q2`.
- KR-1 tiene un vínculo débil con C-KR-3 y KR-2 es team-local. Ningún KR de reporting contribuye hoy a un KR de la compañía, por eso la tabla Team Contributions de la compañía está vacía.

