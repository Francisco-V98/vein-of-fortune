---
id: "F0-87"
tipo: "tarea"
title: "F0-87 Política de modelos y esfuerzo por agente, autorización de Fable y modo conciso"
aliases: ["F0-87"]
fase: "[[F0 Diseño]]"
hito: "[[F0.14 Mods y equipo de agentes]]"
prio: "P1"
est: 8
status: "review"
version: "MVP"
etapas: ["ideacion: omitida", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: activa", "playtest: omitida", "cierre: pendiente"]
especialista: "[[Desarrollador de herramientas]]"
docs: ["[[15 Flujo de trabajo y calidad]]", "[[20 Equipo y flujo de agentes]]", "[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]"]
arriba: "[[F0.14 Mods y equipo de agentes]]"
tags: ["estado/en-curso", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:893"
generado: true
---

# F0-87 Política de modelos y esfuerzo por agente, autorización de Fable y modo conciso

> Fase 1 del plan de ahorro de tokens. Tabla de modelo y esfuerzo por rol en equipo.json (validada por el build y sincronizada con los…

Fase 1 del plan de ahorro de tokens. Tabla de modelo y esfuerzo por rol en equipo.json (validada por el build y sincronizada con los agentes); hook del mod /equipo sobre el lanzamiento de agentes que aplica la tabla y pide autorización antes de usar Fable 5.1 con opciones de otro modelo; botones de cambio en la pestaña «Equipo»; CLAUDE.md del proyecto y skill de modo conciso (informes cortos de formato fijo, encargos mínimos, lectura parcial, lotes de agentes, cortar la sesión al cerrar cada tarea); documentación (documentos 15 y 20, README de los mods, ADR-0010). Decisión del autor del 2026-10-23: optimizar el consumo de tokens con modelo y esfuerzo por agente, autorización de Fable 5.1 y un modo conciso (plan en tres fases).

## Hecha cuando

Un agente lanzado con Fable pide autorización; cada rol usa el modelo y el esfuerzo de la tabla; los informes de los agentes siguen el formato corto; el build estricto y las pruebas pasan.

## Flujo por etapas

Especialista de producción: [[Desarrollador de herramientas]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | omitida |  |  | El plan lo aprobó el autor el 2026-10-23 tras una exploración de los datos de consumo |
| [[Etapa Análisis\|analisis]] | hecha | [[Coordinador (Claude)]] | 2026-10-23 | Dos exploraciones de solo lectura: equipo y mods, y consumo de tokens; plan en tres fases aprobado |
| [[Etapa Producción\|produccion]] | hecha | [[Desarrollador de herramientas]] | 2026-10-23 | Tabla de modelos y sincronía de agentes con validación en el build, hook del mod /equipo con autorización de Fable, CLAUDE.md, skill de modo conciso, documentos 15 y 20 y ADR-0010 |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-23 | QA aprobó con una observación menor (texto del documento 20 alineado con el diálogo en dos pasos) |
| [[Etapa Revisión del autor\|autor]] | activa |  | 2026-10-23 | Esperando la revisión del autor |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | pendiente |  |  |  |

## Traspasos

- 2026-10-23 · [[Coordinador (Claude)]] → [[Desarrollador de herramientas]] (entrega): Encargo: tabla de modelos en equipo.json, sincronización de agentes, validación y hook del mod /equipo
- 2026-10-23 · [[Desarrollador de herramientas]] → [[Coordinador (Claude)]] (entrega): Entrega: tabla de modelos, sincronización de 19 agentes y validación en el build
- 2026-10-23 · [[Desarrollador de herramientas]] → [[Coordinador (Claude)]] (entrega): Entrega: hook del mod /equipo con autorización de Fable y 17 pruebas nuevas
- 2026-10-23 · [[Diseñador de sistemas]] → [[Coordinador (Claude)]] (entrega): Entrega: documentos 15 y 20 y ADR-0010
- 2026-10-23 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar F0-87
- 2026-10-23 · [[QA técnico]] → [[Coordinador (Claude)]] (entrega): Aprobado con una observación menor corregida
- 2026-10-23 · [[Coordinador (Claude)]] → [[Fran (autor)]] (entrega): Revisión de F0-87: política de modelos, autorización de Fable y modo conciso

## Historial

- 2026-10-23 · backlog → doing · claude: Se empieza la política de modelos y esfuerzo por agente y el modo conciso (rama studio/F0-87-politica-de-modelos-y-consumo)
- 2026-10-23 · doing → review · claude: Pasa a revisión del autor tras QA (PR de F0-87)

## Relaciones

- **Hito:** [[F0.14 Mods y equipo de agentes]]
- **Documentos:** [[15 Flujo de trabajo y calidad]], [[20 Equipo y flujo de agentes]], [[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]

## Fuente

`studio/data/roadmap.json:893`
