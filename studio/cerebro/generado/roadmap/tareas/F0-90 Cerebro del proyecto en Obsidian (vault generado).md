---
id: "F0-90"
tipo: "tarea"
title: "F0-90 Cerebro del proyecto en Obsidian (vault generado)"
aliases: ["F0-90"]
fase: "[[F0 Diseño]]"
hito: "[[F0.14 Mods y equipo de agentes]]"
prio: "P2"
est: 12
status: "review"
version: "MVP"
etapas: ["ideacion: hecha", "analisis: omitida", "produccion: hecha", "qa: hecha", "autor: activa", "playtest: omitida", "cierre: pendiente"]
especialista: "[[Desarrollador de herramientas]]"
docs: []
arriba: "[[F0.14 Mods y equipo de agentes]]"
tags: ["estado/en-curso", "prio/P2", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:920"
generado: true
---

# F0-90 Cerebro del proyecto en Obsidian (vault generado)

> Vault de Obsidian generado desde el repo, solo lectura y regenerado con cada build, en una carpeta ignorada por git (studio/cerebro)…

Vault de Obsidian generado desde el repo, solo lectura y regenerado con cada build, en una carpeta ignorada por git (studio/cerebro). Contiene todo lo que se pueda del proyecto en notas atómicas bien fragmentadas y enlazadas (documentos y ADR por secciones, tareas, equipo y memoria, mundo y economía, narrativa) con propiedades, etiquetas, notas índice y una configuración de la vista de grafo que separe por tipo; se sigue la forma habitual de organizar un «segundo cerebro» (notas atómicas, mapas de contenido, propiedades en el encabezado y consultas). Decisión del autor del 2026-10-23.

## Hecha cuando

Al abrir studio/cerebro en Obsidian se ve el grafo del proyecto con todas las entidades como notas individuales y enlazadas, el build lo regenera sin intervención y las pruebas lo comprueban.

## Flujo por etapas

Especialista de producción: [[Desarrollador de herramientas]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | hecha | [[Ideador e investigador]] | 2026-10-23 | El ideador investigó la forma habitual de organizar un vault y propuso la estructura; el autor decidió nombres legibles, notas por sección y entidad, todas las tareas como nodos y todos los extras |
| [[Etapa Análisis\|analisis]] | omitida |  |  | El diseño ya cubre los datos disponibles y sus límites |
| [[Etapa Producción\|produccion]] | hecha | [[Desarrollador de herramientas]] | 2026-10-23 | Núcleo y módulos de documentos, tareas, equipo, memoria, mundo, economía, narrativa, glosario, QA, simulador y arte; build.py lo regenera |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-23 | QA aprobó lo mecánico (322 pruebas, 0 enlaces sin resolver, 0 huérfanas, idempotente); su único fallo era el ⏳ F0-88 inexistente, resuelto al apilar la rama sobre F0-87 |
| [[Etapa Revisión del autor\|autor]] | activa |  | 2026-10-23 | Esperando la revisión del autor |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | pendiente |  |  |  |

### Hallazgos

- [[QA técnico]] (qa, resuelto): El documento 10 cita ⏳ F0-88, que no existía en la rama → resuelto por [[Coordinador (Claude)]]: La rama se apila sobre la de F0-87, que crea F0-88 y F0-89

## Traspasos

- 2026-10-23 · [[Coordinador (Claude)]] → [[Ideador e investigador]] (entrega): Encargo: investigar buenas prácticas de organización de un vault (notas atómicas, mapas de contenido, propiedades, grafo) y proponer estructura para este proyecto
- 2026-10-23 · [[Ideador e investigador]] → [[Coordinador (Claude)]] (entrega): Entrega: buenas prácticas de vault, estructura, estimación de notas y 4 preguntas
- 2026-10-23 · [[Coordinador (Claude)]] → [[Desarrollador de herramientas]] (entrega): Núcleo del generador y módulos de documentos, tareas, equipo y memoria
- 2026-10-23 · [[Desarrollador de herramientas]] → [[Coordinador (Claude)]] (entrega): Entrega: parte 1 con 1.151 notas
- 2026-10-23 · [[Desarrollador de herramientas]] → [[Coordinador (Claude)]] (entrega): Entrega: mundo, economía, QA, simulador y arte; narrativa y glosario (1.961 notas)
- 2026-10-23 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar F0-90
- 2026-10-23 · [[QA técnico]] → [[Coordinador (Claude)]] (entrega): Aprobado tras resolver el ⏳ F0-88
- 2026-10-23 · [[Coordinador (Claude)]] → [[Fran (autor)]] (entrega): Revisión de F0-90: vault de Obsidian generado con unas 2.000 notas

## Historial

- 2026-10-23 · backlog → doing · claude: Se empieza el cerebro del proyecto en Obsidian (rama studio/F0-90-cerebro-en-obsidian)
- 2026-10-23 · doing → review · claude: Pasa a revisión del autor tras QA (PR de F0-90)

## Relaciones

- **Hito:** [[F0.14 Mods y equipo de agentes]]

## Fuente

`studio/data/roadmap.json:920`
