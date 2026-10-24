---
id: "doc-20-modelo-y-esfuerzo-por-rol"
tipo: "seccion"
title: "Modelo y esfuerzo por rol ✅"
aliases: ["doc-20-modelo-y-esfuerzo-por-rol"]
documento: "[[20 Equipo y flujo de agentes]]"
limpieza: 100
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[20 §El equipo]]"
siguiente: "[[20 §Cómo se registra el avance]]"
arriba: "[[20 Equipo y flujo de agentes]]"
fuente: "studio/docs/20-equipo-y-flujo-de-agentes.md:59"
generado: true
---

# Modelo y esfuerzo por rol ✅

> Decisión del autor (2026-10-23, ADR-0010): cada agente tiene un modelo y un esfuerzo por defecto en studio/data/equipo.json (roles[].modelo…

← [[20 §El equipo]] · [[20 Equipo y flujo de agentes|↑ 20]] · [[20 §Cómo se registra el avance]] →

Decisión del autor (2026-10-23, [[ADR-0010 Política de modelos por rol y autorización de Fable 5.1|ADR-0010]]): cada agente tiene un modelo y un esfuerzo por defecto en `studio/data/equipo.json` (`roles[].modelo` y `roles[].esfuerzo`). Al lanzar un subagente, el coordinador fija esos valores en la llamada a `Agent`.

| Rol | Agente | Modelo | Esfuerzo |
|---|---|---|---|
| Ideador e investigador | `ideador` | opus | high |
| Arquitecto de software | `arquitecto` | opus | high |
| Asesor legal y de licencias | `asesor-legal` | sonnet | high |
| Economista y balance | `economista` | sonnet | high |
| Analista de coherencia | `analista` | sonnet | medium |
| Responsable de lanzamiento | `responsable-lanzamiento` | sonnet | medium |
| Diseñador de sistemas | `disenador-sistemas` | sonnet | medium |
| Diseñador de contenido | `disenador-contenido` | sonnet | medium |
| Diseñador UI/UX | `disenador-ui-ux` | sonnet | medium |
| Narrador | `narrador` | sonnet | medium |
| Director de arte | `director-arte` | sonnet | medium |
| Diseñador de sonido | `disenador-sonido` | sonnet | medium |
| Desarrollador de juego | `desarrollador-juego` | sonnet | medium |
| Desarrollador de herramientas | `desarrollador-herramientas` | sonnet | medium |
| Ingeniero de seguridad | `ingeniero-seguridad` | sonnet | medium |
| Revisor de código | `revisor-codigo` | sonnet | medium |
| Localizador ES/EN | `localizador` | sonnet | low |
| QA técnico | `qa` | sonnet | low |
| Diseñador de pruebas | `disenador-pruebas` | sonnet | low |

Reglas ✅:
- **Ajuste por tarea:** el coordinador puede subir o bajar el modelo o el esfuerzo en una tarea concreta, con el motivo en una línea dentro del encargo. Los valores válidos son los de `politica_modelos` en `equipo.json` (modelos `haiku`, `sonnet`, `opus` y `fable`; esfuerzos `low`, `medium`, `high`, `xhigh` y `max`).
- **Fable 5.1 solo con autorización del autor:** nadie lo usa por defecto. Cuando una tarea lo pide, el mod `vf-equipo` abre un diálogo en `/equipo` en dos pasos: primero **aprobar para esta tarea**, **aprobar solo este** o **usar otro modelo**, y si eliges cambiar, Opus, Sonnet, Haiku u otro modelo escrito (el diálogo admite de 2 a 4 opciones por paso). La aprobación vale para esa tarea, no para las siguientes. Si el coordinador no está seguro, usa el siguiente modelo más barato y avisa.
- **Modo conciso:** los agentes y los encargos siguen la skill `.claude/skills/modo-conciso` y las reglas de [[15 Flujo de trabajo y calidad|15]]: encargo mínimo e informes cortos.

## Fuente

`studio/docs/20-equipo-y-flujo-de-agentes.md:59`
