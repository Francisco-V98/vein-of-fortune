---
id: "F0-72"
tipo: "tarea"
title: "F0-72 Equipo de agentes: etapas, roles y especialistas (documento 20)"
aliases: ["F0-72"]
fase: "[[F0 Diseño]]"
hito: "[[F0.14 Mods y equipo de agentes]]"
prio: "P2"
est: 4
status: "done"
version: "MVP"
etapas: ["ideacion: hecha", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Diseñador de sistemas]]"
docs: ["[[20 Equipo y flujo de agentes]]"]
arriba: "[[F0.14 Mods y equipo de agentes]]"
tags: ["estado/hecho", "prio/P2", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:767"
generado: true
---

# F0-72 Equipo de agentes: etapas, roles y especialistas (documento 20)

> Definir las etapas del flujo, los roles del equipo (ideador, analista, diseñador, narrador, director de arte, desarrollador, QA, autor y…

Definir las etapas del flujo, los roles del equipo (ideador, analista, diseñador, narrador, director de arte, desarrollador, QA, autor y coordinador) y los siete subagentes, con el registro del avance por tarea.

## Hecha cuando

Documento 20 y definiciones de los agentes acordados con el autor.

## Flujo por etapas

Especialista de producción: [[Diseñador de sistemas]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | hecha | [[Ideador e investigador]] | 2026-10-12 | Etapas y roles pensados a partir de tu petición |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-12 | Cruzado con el flujo del documento 15 |
| [[Etapa Producción\|produccion]] | hecha | [[Diseñador de sistemas]] | 2026-10-12 | Documento 20, equipo.json y siete agentes |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-12 | Build estricto sin avisos |
| [[Etapa Revisión del autor\|autor]] | hecha |  | 2026-10-12 | Aprobado por el autor con «Todo bien» y «Terminé mi parte» |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha |  | 2026-10-12 | Tarea cerrada y PR #32 fusionado |

### Hallazgos

- [[Analista de coherencia]] (analisis, resuelto):  → resuelto por [[Diseñador de sistemas]]: Los estados del roadmap no cambian y el documento 20 explica la correspondencia

## Traspasos

- 2026-10-12 · [[Ideador e investigador]] → [[Analista de coherencia]] (entrega): Siete etapas y nueve roles
- 2026-10-12 · [[Analista de coherencia]] → [[Diseñador de sistemas]] (entrega): El flujo no debe cambiar los estados del roadmap
- 2026-10-12 · [[Diseñador de sistemas]] → [[QA técnico]] (entrega): Documento 20, equipo.json y siete agentes
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): QA aprobado: build estricto sin avisos
- 2026-10-12 · [[Fran (autor)]] → [[Diseñador de sistemas]] (devolucion): Los empleados no son los reales que necesitamos: analiza y crea todos
- 2026-10-12 · [[Diseñador de sistemas]] → [[QA técnico]] (entrega): 21 roles en 7 departamentos y 19 agentes
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): QA aprobado: build estricto sin avisos
- 2026-10-12 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobado: «Terminé mi parte» sin ajustes

## Historial

- 2026-10-12 · backlog → doing · claude: Se empieza tras la petición del autor de crear mods para el proyecto. (rama studio/F0-71-mods-panel-y-equipo)
- 2026-10-12 · doing → review · claude: Documento 20, equipo.json y siete subagentes escritos; build.py valida el flujo. (rama studio/F0-71-mods-panel-y-equipo)
- 2026-10-12 · review → done · claude: El autor aprobó la tarea desde la bandeja de /equipo. (aprobación del autor con el botón «Terminé mi parte»)

## Comentarios

- 2026-10-12 · autor: Quiero un segundo mod con diferentes agentes o empleados (ideador, analista, diseñador, desarrollador, QA y los que convengan) para ver cómo uno le pasa el trabajo al otro hasta que la tarea queda cerrada, sin cabos sueltos, y donde yo también esté para revisar y probar el juego.
- 2026-10-12 · claude: Propuesta de siete etapas (ideación, análisis, producción, QA técnico, revisión del autor, prueba del autor y cierre) y nueve roles: siete agentes en .claude/agents, el autor y el coordinador. El flujo de cada tarea va en un bloque pipeline de su archivo de actividad y build.py lo valida. Las etapas y los roles están en 🟡 hasta que el autor los confirme; los agentes aún no se han usado en una tarea real.
- 2026-10-12 · autor: No siento que estos sean los empleados reales que necesitamos. Quiero que analices y crees todos los que vamos a utilizar; tienes libertad para proponerlo todo.
- 2026-10-12 · claude: Se revisó el roadmap fase por fase y el equipo pasa a 21 roles en 7 departamentos: se añaden economista, diseñador de contenido, diseñador UI/UX, localizador, diseñador de sonido, arquitecto, desarrollador de herramientas, ingeniero de seguridad, asesor legal, responsable de lanzamiento, revisor de código y diseñador de pruebas. Cada rol tiene su fase de incorporación y su agente en .claude/agents (19 agentes). Los que aún no se incorporan quedan en reserva en el plano.
- 2026-10-12 · autor: Terminé mi parte: revisé el entregable y está aprobado. Pásala a la siguiente etapa del flujo.

## Relaciones

- **Hito:** [[F0.14 Mods y equipo de agentes]]
- **Documentos:** [[20 Equipo y flujo de agentes]]

## Fuente

`studio/data/roadmap.json:767`
