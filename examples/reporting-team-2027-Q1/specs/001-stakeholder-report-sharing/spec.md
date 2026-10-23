# Feature Specification: Compartir reportes con stakeholders sin cuenta

**Feature Branch**: `001-stakeholder-report-sharing`

**Created**: 2026-10-22

**Status**: Draft

**Input**: User description: "Los managers comparten reportes con stakeholders sin cuenta en Teamboard. okr:reporting/H-1. Bet: creemos que darles a los managers una forma de hacer llegar un reporte a stakeholders sin cuenta hará que dejen de mandar capturas de pantalla y compartan el reporte cada semana, visto en KR-1 (0% → 30% de managers activos que comparten fuera de Teamboard cada semana al 2027-03-31; anticipa a KR-2). Se refuta si tras 6 semanas de piloto menos del 12% de los managers activos del piloto comparte cada semana, o si menos de la mitad repite en 2 o más de 4 semanas. \"Compartir\" significa que el reporte llega a un destinatario sin cuenta; una descarga sola no cuenta. Validation slice (P1): un solo medio para compartir, aplicado al reporte status, detrás de un flag de GrowthBook para un grupo piloto, con un evento de \"reporte compartido\" medido por usuario. Ideas candidatas: CI-1 exportar a PDF, CI-2 envío programado por email; la spec elige entre ellas. Fuera de alcance: colaboración con stakeholders que ya tienen cuenta, comentarios o edición por destinatarios externos, y prospects en venta. Restricciones: piloto encendido a más tardar el 2027-02-17; cero exposición de datos (TG-2)."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Enviar el reporte de estado por email a stakeholders sin cuenta (Priority: P1)

Un manager de un proyecto quiere que sus stakeholders reciban el estado semanal sin tener que sacar capturas de pantalla. Desde el reporte `status` del proyecto, indica las direcciones de email de los destinatarios (personas sin cuenta en Teamboard) y elige enviarlo ahora o programarlo para que salga automáticamente cada semana. Los destinatarios reciben el reporte de estado actualizado en su email y pueden leerlo sin crear una cuenta.

**Why this priority**: Es el slice de validación de H-1 (CI-2, envío programado por email). Es el único medio candidato en el que se puede observar que el reporte *llegó* a un destinatario sin cuenta, que es lo que exige la definición de "compartir" de KR-1; y el envío programado elimina el trabajo manual semanal que O-1 quiere quitar. El PM confirmó el email como medio del P1 y el PDF como scale story.

**Stage**: validation · Leading signal: managers del piloto que hacen su primer envío en los primeros 7 días; % de envíos que llegan a un destinatario sin cuenta

**Independent Test**: Con la función activa para una organización piloto, un manager programa el envío semanal del reporte `status` a una dirección externa; se verifica que el email llega con el contenido vigente del reporte, que se registra un "reporte compartido" atribuido a ese manager, y que una organización fuera del piloto no ve la opción.

**Acceptance Scenarios**:

1. **Given** un manager de una organización piloto en el reporte `status` de su proyecto, **When** ingresa una o más direcciones de email de destinatarios y elige "enviar ahora", **Then** cada destinatario recibe el reporte de estado con los datos vigentes en ese momento, sin necesidad de cuenta.
2. **Given** el mismo manager, **When** programa un envío semanal (día y hora) a esos destinatarios, **Then** el reporte con los datos vigentes sale automáticamente cada semana en ese horario hasta que el manager lo detenga.
3. **Given** un envío programado activo, **When** el manager lo edita (destinatarios, día u hora) o lo detiene, **Then** los envíos siguientes reflejan el cambio y, si lo detuvo, no sale ningún envío más.
4. **Given** un destinatario que recibió un reporte, **When** elige darse de baja desde el email, **Then** deja de recibir envíos de ese manager para ese proyecto y el manager ve que ese destinatario se dio de baja.
5. **Given** una organización piloto cuyo admin restringió los envíos a dominios aprobados, **When** un manager ingresa una dirección fuera de esos dominios, **Then** el sistema no la acepta y le explica por qué.
6. **Given** un manager de una organización fuera del piloto, **When** abre el reporte `status`, **Then** no ve ninguna opción de envío por email y la página se comporta como hoy.
7. **Given** cualquier envío, **When** el email llega o es abierto por al menos un destinatario sin cuenta, **Then** se registra un "reporte compartido" atribuido al manager individual (no solo a la organización), con el proyecto, el tipo de reporte y si fue envío puntual o programado.

---

### User Story 2 - Compartir los demás reportes del proyecto (Priority: P2)

El manager puede usar el mismo envío (puntual o programado) para los reportes `burndown` y `workload`, no solo para `status`.

**Why this priority**: Amplía el alcance del comportamiento ya probado en el P1 a más reportes. *(scale — built only if H-1 is validated)*

**Stage**: scale · Leading signal: managers que comparten `burndown` o `workload` en su primera semana con la función disponible

**Independent Test**: Con la función activa, un manager programa el envío del reporte `burndown` a un destinatario externo y este lo recibe con datos vigentes; se registra un "reporte compartido" con el tipo de reporte correcto.

**Acceptance Scenarios**:

1. **Given** un manager de una organización con la función habilitada, **When** programa el envío del reporte `burndown` o `workload`, **Then** los destinatarios lo reciben con la misma frecuencia, control de baja y registro que el reporte `status`.

---

### User Story 3 - Exportar el reporte a PDF (Priority: P3)

El manager puede descargar el reporte del proyecto como PDF, y los envíos por email pueden incluir el reporte como PDF adjunto para que el destinatario lo reenvíe o lo archive.

**Why this priority**: Corresponde a CI-1. Una descarga sola no cuenta como "compartir" para KR-1 porque no se puede observar que el reporte llegó a alguien, así que no sirve como slice de validación; como adjunto de un envío sí suma valor una vez validada la hipótesis. *(scale — built only if H-1 is validated)*

**Stage**: scale · Leading signal: % de envíos con PDF adjunto (las descargas solas no cuentan)

**Independent Test**: Un manager descarga el PDF del reporte `status` y su contenido coincide con lo que ve en pantalla; un envío con PDF adjunto llega con el archivo.

**Acceptance Scenarios**:

1. **Given** un manager en un reporte del proyecto, **When** elige exportar a PDF, **Then** obtiene un archivo con el contenido vigente del reporte.
2. **Given** un envío por email configurado, **When** el manager activa "adjuntar PDF", **Then** los destinatarios reciben el reporte también como PDF adjunto.
3. **Given** una descarga de PDF sin envío, **When** se calculan los "reportes compartidos", **Then** esa descarga no cuenta como compartir.

---

### Edge Cases

- El manager ingresa una dirección que pertenece a un miembro de la organización con cuenta: el envío se permite, pero no cuenta como "compartir" con alguien sin cuenta para KR-1 (la colaboración con usuarios con cuenta está fuera de alcance).
- El manager se envía el reporte a sí mismo: no cuenta como "compartir".
- Un email rebota o la dirección es inválida: el manager ve el error y ese envío no cuenta como compartido.
- El manager pierde acceso al proyecto o deja la organización: sus envíos programados se detienen.
- El proyecto se archiva o elimina: los envíos programados se detienen.
- La organización sale del piloto (se apaga la función): los envíos programados dejan de salir y no se borran datos del manager.
- Un envío programado no es abierto por nadie en una semana: esa semana no cuenta como "compartir" para ese manager.
- Hay muchos destinatarios en un envío: existe un límite razonable por envío para evitar uso como lista de correo masiva.
- El reporte no tiene datos todavía (proyecto nuevo): el envío sale con un estado vacío explícito, no con un error.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Los managers de organizaciones piloto MUST poder enviar el reporte `status` de un proyecto por email a una o más direcciones, ya sea en el momento o programado semanalmente (día y hora).
- **FR-002**: El email MUST mostrar el contenido vigente del reporte en el momento del envío y MUST poder leerse sin cuenta en Teamboard.
- **FR-003**: Los managers MUST poder ver, editar y detener sus envíos programados.
- **FR-004**: Cada email MUST incluir una forma de darse de baja; una baja MUST detener los envíos de ese manager y proyecto a esa dirección, y el manager MUST verla.
- **FR-005**: La función MUST estar disponible solo para el grupo piloto de organizaciones; fuera del piloto, el reporte se comporta exactamente como hoy.
- **FR-006**: El sistema MUST registrar un evento de "reporte compartido" atribuido al manager individual (además de su organización), con proyecto, tipo de reporte, tipo de envío (puntual/programado), cantidad de destinatarios sin cuenta y si fue entregado y abierto.
- **FR-007**: Un envío MUST contar como "compartir" para KR-1 solo si al menos un destinatario sin cuenta lo recibió o lo abrió; descargas, envíos a uno mismo y envíos a miembros con cuenta MUST NOT contar.
- **FR-008**: El sistema MUST permitir identificar a los "managers activos" del piloto por semana, para calcular el % de KR-1 (denominador).
- **FR-009**: El email MUST incluir solo el contenido de ese reporte de ese proyecto; MUST NOT incluir datos de otros proyectos, otras organizaciones ni información personal de miembros más allá de lo que el reporte ya muestra al manager.
- **FR-010**: Por defecto, los managers MUST poder enviar a cualquier dirección de email. El admin de la organización MUST poder restringir los envíos a una lista de dominios aprobados; con la restricción activa, el sistema MUST rechazar direcciones fuera de esos dominios al configurar el envío y MUST detener los envíos programados existentes a direcciones que dejen de estar permitidas.
- **FR-011**: Los envíos programados MUST detenerse si el manager pierde acceso al proyecto, si el proyecto se archiva o elimina, o si la organización sale del piloto.
- **FR-012**: Cada envío MUST tener un límite de destinatarios (por defecto 20) para evitar uso masivo.
- **FR-013**: Agregar la opción de envío MUST NOT hacer más lenta la carga de la página de reportes.
- **FR-014** *(P2, scale)*: El envío MUST extenderse a los reportes `burndown` y `workload` con el mismo comportamiento.
- **FR-015** *(P3, scale)*: Los managers MUST poder exportar un reporte a PDF y adjuntarlo a los envíos; una descarga de PDF sola MUST NOT contar como "compartir".

### Key Entities

- **Envío de reporte**: un envío puntual o programado de un reporte de un proyecto; tiene manager que lo creó, proyecto, tipo de reporte, destinatarios, frecuencia (día y hora) y estado (activo/detenido).
- **Destinatario**: una dirección de email que recibe envíos; marca si pertenece a alguien con cuenta en la organización y si se dio de baja.
- **Política de destinatarios de la organización**: ajuste del admin; abierta (cualquier dirección, por defecto) o restringida a una lista de dominios aprobados.
- **Reporte compartido**: el registro de que un envío llegó (o fue abierto) por al menos un destinatario sin cuenta; atribuido a un manager individual y a una semana, base de KR-1.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001 (KR-1)**: En la semana 6 del piloto, ≥21% de los managers activos de las organizaciones piloto comparte un reporte fuera de Teamboard por semana (score ≥ 0.7 del target 30%). Entre 12% y 21% = iterar; <12% = H-1 refutada. *(→ KR-1)*
- **SC-002 (KR-1, repetición)**: ≥50% de los managers que comparten lo hacen en ≥2 de las últimas 4 semanas del piloto. *(→ KR-1)*
- **SC-003 (KR-2)**: Los tickets sobre cómo compartir un reporte con alguien sin cuenta bajan en las organizaciones piloto respecto de su línea base (camino hacia ≤10/mes en total al 2027-03-31). *(→ KR-2)*
- **SC-004 (G-1)**: Las invitaciones de miembros por organización en el piloto no caen más de 10% relativo frente a las organizaciones de control. *(→ G-1)*
- **SC-005 (G-2)**: Los tickets sobre compartir (incluida la función nueva) en organizaciones piloto no superan su línea base proporcional (~25/mes en total). *(→ G-2)*
- **SC-006 (TG-1)**: El tiempo de carga de la página de reportes no empeora frente a su valor actual. *(→ TG-1)*
- **SC-007 (TG-2)**: Cero incidentes de datos de clientes expuestos a alguien que no sea el destinatario previsto. *(→ TG-2)*
- **SC-008**: Un manager programa su primer envío semanal en menos de 2 minutos sin ayuda. *(acceptance threshold)*

## Hypothesis & Bet *(mandatory when the input has an `okr:` token)*

**Bet**: okr:reporting/H-1 — [bet file](../../.specify/okr/teams/reporting/bets/H-1-stakeholder-report-sharing.md)
**Hypothesis**: Creemos que darles a los managers una forma de hacer llegar un reporte a stakeholders sin cuenta en Teamboard, para managers que informan el estado semanal, hará que dejen de mandar capturas de pantalla y compartan el reporte cada semana, visto en KR-1
**Moves**: KR-1 (0% → 30% de managers activos que comparten fuera de Teamboard cada semana al 2027-03-31); drives KR-2 (~25 → ≤10 tickets/mes)
**Expected contribution**: ~30 pp de los +30 pp de KR-1 (único bet sobre KR-1); el techo depende del % de managers que hoy mandan estado semanal (desconocido). Dentro de 2027-Q1, el aporte a KR-1 global se limita a la fracción de managers en el piloto; los ~30 pp aplican tras escalar
**Refuted if**: tras 6 semanas con la función disponible para el piloto, <12% de los managers activos del piloto comparte por semana, o menos de la mitad de los que comparten repite en ≥2 de las últimas 4 semanas
**Validation slice**: User Story 1 (P1)
**Scale stories (built only if validated)**: User Story 2, User Story 3
**Guardrails**: G-1 invitaciones de miembros no caen >10% vs. control · G-2 tickets sobre compartir no superan la base · TG-1 la página de reportes no se vuelve más lenta · TG-2 cero exposición de datos de clientes
**Out of scope (this horizon)**: colaboración con stakeholders que ya tienen cuenta; comentarios o edición por destinatarios externos; prospects en el proceso de venta

## Assumptions

- **Destinatarios** (decisión del PM, 2026-10-22): abierto por defecto, con restricción opcional por dominios aprobados a cargo del admin; equilibra adopción en el piloto y TG-2.
- **Elección entre ideas** (confirmada por el PM, 2026-10-22): CI-2 (envío programado por email) es el medio del P1 porque permite observar que el reporte llegó a un destinatario sin cuenta y elimina el trabajo manual semanal. CI-1 (PDF) no se descarta: queda como User Story 3 (scale), porque una descarga no se puede atribuir a un "compartir" y seguiría siendo trabajo manual semanal.
- "Manager" es un usuario con acceso de gestión a un proyecto y a sus reportes; "manager activo" en una semana es un manager que abrió al menos un reporte o editó su proyecto esa semana. La definición final se fija en `/speckit-okr-measure`.
- El piloto se asigna por organización (no por usuario), con un grupo de control de organizaciones comparables, para poder leer G-1 por organización.
- El piloto debe estar encendido a más tardar el 2027-02-17 para que las 6 semanas de validación terminen antes del 2027-03-31.
- KR-1 se mide sobre todos los managers activos, pero dentro de 2027-Q1 solo los managers del piloto tienen la función; aun validada H-1, KR-1 global al 2027-03-31 quedará cerca de (% de managers en el piloto × tasa del piloto). Se recomienda encender el piloto antes del 2027-02-17 para dejar margen de escalar dentro del período; la decisión sobre KR-1 se toma en el check-in del equipo.
- La apertura de un email es una señal imperfecta (algunos clientes de correo la bloquean o la simulan); la entrega confirmada también cuenta como "compartir" según la definición del bet.
- El límite de 20 destinatarios por envío es un valor por defecto razonable; se puede ajustar en el plan.
- Hoy la analítica registra eventos por organización; medir por manager individual es requisito (FR-006) y se planifica en `/speckit-okr-measure`.
- Los envíos y bajas cumplen la normativa habitual de email comercial/transaccional (identificación del remitente, baja en un clic).
