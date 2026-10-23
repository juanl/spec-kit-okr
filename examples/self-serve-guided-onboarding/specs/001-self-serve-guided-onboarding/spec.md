# Feature Specification: Onboarding guiado para equipos self-serve

**Feature Branch**: `001-self-serve-guided-onboarding`
**Created**: 2026-10-22
**Status**: Draft
**Input**: User description: "Onboarding guiado para equipos nuevos self-serve. Objective: los equipos self-serve nuevos llegan a su primer resultado útil sin ayuda de soporte ni ventas. KR-1: conversión trial→pago 9% → 15% al 2027-03-31. KR-2: activación en 7 días 22% → 45% al 2027-01-31. Candidate initiatives: checklist guiada, plantillas, wizard de configuración, tours, videos, onboarding por rol, invitación masiva. Validation first: checklist guiada. Out of scope: sales-led, cambios de pricing o de trial."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Checklist guiada hasta el primer resultado (Priority: P1)

Un admin de un equipo self-serve recién registrado ve una checklist de 4 pasos (crear proyecto, invitar a 2 compañeros, crear tareas, completar 3 tareas) que lo lleva al primer resultado útil. Cada paso se marca solo cuando ocurre.

**Why this priority**: Es la propuesta de "validation first" del framing y el camino más corto al primer resultado útil.

**Initiative → KR-2** · Hypothesis: guiar los 4 pasos de activación hace que más equipos los completen · Leading signal: % de equipos que completan la checklist en 3 días · Confidence: low

**Independent Test**: Registrar un equipo self-serve nuevo, seguir la checklist y verificar que cada paso se marca al cumplirse y que la checklist desaparece al completarse.

**Acceptance Scenarios**:

1. **Given** un equipo self-serve recién registrado, **When** el admin entra por primera vez, **Then** ve la checklist con 4 pasos pendientes.
2. **Given** la checklist visible, **When** el equipo completa su tercera tarea, **Then** el último paso se marca y se muestra un mensaje de logro.
3. **Given** la checklist visible, **When** el admin la descarta, **Then** puede reabrirla desde el menú de ayuda.

---

### User Story 2 - Wizard de configuración del equipo (Priority: P2)

Al registrarse, el admin pasa por un wizard corto de 2 pantallas: perfil del equipo e invitaciones. Integraciones y preferencias se ofrecen después del primer proyecto.

**Why this priority**: Solo el paso de invitaciones contribuye a la activación; un wizard largo antes del primer proyecto la demoraría. (Era P1; se bajó en la alineación OKR.)

**Initiative → KR-2** · Hypothesis: invitar desde el día 1 acerca al equipo al umbral de ≥2 miembros · Leading signal: % de equipos con ≥2 invitaciones enviadas desde el wizard en el día 1 · Confidence: low

**Independent Test**: Completar el wizard y verificar que perfil, integraciones e invitaciones quedan guardadas.

**Acceptance Scenarios**:

1. **Given** un registro nuevo, **When** termina el alta, **Then** se abre el wizard en la pantalla de perfil.
2. **Given** el wizard abierto, **When** el admin saltea las invitaciones, **Then** llega igual a su tablero.
3. **Given** un equipo que creó su primer proyecto, **When** vuelve al tablero, **Then** se le ofrece configurar integraciones.

---

### User Story 3 - Plantillas de proyecto (Priority: P2)

Al crear su primer proyecto, el equipo puede elegir una plantilla (lanzamiento de producto, sprint, campaña) que trae tareas de ejemplo.

**Why this priority**: Reduce la página en blanco.

**Initiative → KR-2** · Hypothesis: empezar con tareas de ejemplo acelera llegar a 1 proyecto y 3 tareas completadas · Leading signal: % de primeros proyectos creados desde plantilla · Confidence: low

**Independent Test**: Crear un proyecto desde una plantilla y verificar que trae tareas editables.

**Acceptance Scenarios**:

1. **Given** un equipo sin proyectos, **When** crea un proyecto, **Then** se ofrecen al menos 3 plantillas.

---

### User Story 4 - Tours interactivos por pantalla (Priority: P3)

La primera vez que un usuario entra a una pantalla principal (tablero, proyecto, reportes) ve un tour de 3–5 pasos.

**Why this priority**: Ayuda a descubrir funcionalidades, pero su efecto en la activación es indirecto. (Era P2; se bajó en la alineación OKR.)

**Initiative → KR-2** · Hypothesis: conocer el tablero reduce el abandono en la primera sesión · Leading signal: % de usuarios nuevos que terminan el tour del tablero · Confidence: low

**Independent Test**: Entrar por primera vez a cada pantalla y verificar que el tour aparece una sola vez.

**Acceptance Scenarios**:

1. **Given** un usuario nuevo, **When** abre el tablero por primera vez, **Then** ve el tour.

---

### User Story 6 - Onboarding personalizado por rol (Priority: P3)

En el alta, el usuario indica su rol (manager, colaborador, externo) y la checklist y los tours se adaptan.

**Why this priority**: Mejora la relevancia una vez que el onboarding base existe.

**Initiative → KR-2** · Hypothesis: pasos relevantes por rol suben la activación de quienes no son admins · Leading signal: activación a 7 días por rol vs. grupo sin personalización · Confidence: low

**Independent Test**: Registrarse con dos roles distintos y comparar los pasos que se muestran.

**Acceptance Scenarios**:

1. **Given** un usuario con rol "colaborador", **When** entra por primera vez, **Then** su checklist no incluye pasos de administración.

---

### User Story 7 - Invitación masiva de miembros (Priority: P3)

El admin puede pegar una lista de emails o importar un CSV para invitar a varios miembros a la vez.

**Why this priority**: Ahorra tiempo en equipos más grandes; en el segmento self-serve los equipos son chicos.

**Initiative → KR-2** · Hypothesis: invitar de a muchos sube la cantidad de miembros por equipo · Leading signal: % de invitaciones hechas por lista o CSV · Confidence: low

**Independent Test**: Importar un CSV de 10 emails y verificar que se envían 10 invitaciones.

**Acceptance Scenarios**:

1. **Given** un CSV con emails válidos e inválidos, **When** se importa, **Then** se invitan los válidos y se informan los inválidos.

---

### Edge Cases

- ¿Qué pasa si el equipo completa los pasos fuera de orden? La checklist los marca igual.
- ¿Qué ve un miembro invitado (no admin)? No ve la checklist de admin.
- ¿Qué pasa si una cuenta sales-led entra al flujo? No se le muestra el onboarding guiado.
- ¿Qué pasa si la integración de Slack falla en el wizard? Se puede reintentar o saltear.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El sistema MUST mostrar la checklist guiada solo a admins de equipos self-serve en trial.
- **FR-002**: El sistema MUST marcar cada paso de la checklist automáticamente cuando ocurre la acción correspondiente.
- **FR-003**: Los usuarios MUST poder descartar y reabrir la checklist.
- **FR-004**: El sistema MUST ofrecer un wizard de configuración al finalizar el alta (perfil e invitaciones), con pasos opcionales, y ofrecer integraciones recién después del primer proyecto.
- **FR-005**: El sistema MUST ofrecer al menos 3 plantillas de proyecto con tareas de ejemplo.
- **FR-006**: El sistema MUST mostrar cada tour una sola vez por usuario y pantalla.
- **FR-008**: El sistema MUST adaptar la checklist y los tours según el rol declarado.
- **FR-009**: Los admins MUST poder invitar miembros por lista de emails o CSV.
- **FR-010**: El sistema MUST NOT mostrar el onboarding guiado a cuentas sales-led.

### Key Entities

- **Onboarding progress**: estado de cada paso de la checklist por equipo (pendiente / completado / descartado).
- **Project template**: plantilla con nombre, descripción y tareas de ejemplo.
- **Tour view**: registro de qué tours vio cada usuario.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Un equipo nuevo puede crear su primer proyecto desde una plantilla en menos de 3 minutos. *(acceptance threshold)*
- **SC-002**: El 60% de los equipos self-serve nuevos completa la checklist dentro de los primeros 3 días. *(→ KR-2, leading signal US-1)*
- **SC-003**: El 45% de los equipos self-serve nuevos alcanza la activación (≥1 proyecto, ≥2 miembros, ≥3 tareas completadas) en 7 días. *(→ KR-2)*
- **SC-004**: El 90% de los admins completa el wizard en menos de 5 minutos. *(acceptance threshold)*
- **SC-006**: La conversión a pago dentro de los 14 días de los equipos que reciben el onboarding guiado supera la de un grupo comparable que no lo recibe. *(→ KR-1)*
- **SC-007**: El churn a 30 días de las cuentas convertidas no supera la línea base previa al lanzamiento. *(→ G-1)*
- **SC-008**: Los tickets de soporte cada 100 trials no superan la línea base previa al lanzamiento. *(→ G-2)*

## Impact & Objectives (OKR)

**Objective**: Los equipos self-serve nuevos llegan a su primer resultado útil sin ayuda de soporte ni de ventas.
**Framing**: [okr.md](./okr.md)

| KR | Target | Initiatives | Evidenced by |
|----|--------|-------------|--------------|
| KR-1 | 9% → 15% conversión a pago en 14 días, al 2027-03-31 | vía KR-2 (todas) | SC-006 |
| KR-2 | 22% → 45% activación en 7 días, al 2027-01-31 | US-1 (P1), US-2 (P2), US-3 (P2), US-4 (P3), US-6 (P3), US-7 (P3) | SC-002, SC-003 |

**Guardrails**: G-1 churn D30 de convertidas no supera la línea base; G-2 tickets cada 100 trials no superan la línea base.
**Out of scope (no KR impact this horizon)**: videos educativos (ex US-5); cuentas sales-led; cambios de pricing o de duración del trial.

## Assumptions

- Solo aplica a cuentas self-serve en trial; las sales-led quedan fuera.
- El pricing y la duración del trial (14 días, sin tarjeta) no cambian durante el horizonte.
- Se reutilizan los eventos de analytics existentes cuando sea posible.
- Los videos educativos (ex US-5, SC-005) quedan fuera de este horizonte: no se identificó un KR que movieran (alineación OKR, 2026-10-22).
