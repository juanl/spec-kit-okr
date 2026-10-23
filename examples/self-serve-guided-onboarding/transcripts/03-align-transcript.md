# Transcript — /speckit-okr-align (after_specify hook)

**Mode**: bind — `.specify/okr/self-serve-guided-onboarding/okr.md` (draft) matches the feature short name.

## Proposed initiative ranking

| Story | Current | Moves | Hypothesis | Leading signal | Impact | Conf. | Proposed |
|-------|---------|-------|------------|----------------|--------|-------|----------|
| US-1 Checklist guiada | P1 | KR-2 | Guiar los 4 pasos de activación hace que más equipos los completen | % equipos que completan la checklist en 3 días | high | low | **P1** (validation first) |
| US-2 Wizard | P1 | KR-2 | Solo el paso de invitaciones mueve la activación; perfil e integraciones no forman parte de ella | % equipos con ≥2 invitaciones enviadas desde el wizard en el día 1 | medium | low | **P2** ⚠ |
| US-3 Plantillas | P2 | KR-2 | Empezar con tareas de ejemplo acelera proyecto + 3 tareas | % de primeros proyectos creados desde plantilla | high | low | P2 |
| US-4 Tours | P2 | KR-2 | Descubrir funcionalidades no es lo mismo que activarse; el efecto es indirecto | % de usuarios que terminan el tour del tablero | low | low | **P3** ⚠ |
| US-5 Videos | P2 | none | No hay comportamiento de activación asociado; "útil" es una métrica de vanidad | — | low | low | **Out of scope** ⚠ |
| US-6 Por rol | P3 | KR-2 | Pasos relevantes por rol suben la activación de no-admins | Activación por rol vs. control | medium | low | P3 |
| US-7 Invitación masiva | P3 | KR-2 | Los equipos self-serve son chicos; impacto bajo en el segmento | % de invitaciones hechas por CSV | low | low | P3 |

## Findings

| # | Finding | Detail | Proposal |
|---|---------|--------|----------|
| 1 | Priority contradiction | US-2 está en P1 pero no es la validación del supuesto más riesgoso, y además un wizard largo antes del primer proyecto puede *demorar* la activación | Bajar a P2; en el spec, el wizard solo pide perfil + invitaciones, e integraciones pasa a "después" |
| 2 | Priority contradiction | US-4 en P2 con impacto bajo | P3 |
| 3 | Unmotivated story | US-5 no mueve ningún KR | Pasar a Out of scope (este horizonte) |
| 4 | Orphan SC | SC-005 ("90% califica los videos como útiles") | Se elimina junto con US-5 (queda registrado en Assumptions) |
| 5 | Orphan SC | SC-001 y SC-004 son umbrales de aceptación, no evidencia de KR | Confirmar como acceptance thresholds (sin tag de KR) |
| 6 | Uncovered KR | KR-1 no tiene ningún SC | Agregar SC-006: la conversión a 14 días del grupo con onboarding supera la del grupo de control |
| 7 | Unmeasured guardrail | G-1 y G-2 sin SC | Agregar SC-007 (churn D30) y SC-008 (tickets cada 100 trials) |

Candidates: CI-1…CI-7 → US-1…US-7 (CI-5 → US-5, propuesta para out of scope).

**¿Apply all / choose / none?**
**PM**: apply all.
