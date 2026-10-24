---
id: "F0-51"
tipo: "tarea"
title: "F0-51 Registro de hilos narrativos y cabos sueltos"
aliases: ["F0-51"]
fase: "[[F0 Diseño]]"
hito: "[[F0.12 Limpieza y coherencia del diseño]]"
prio: "P1"
est: 6
status: "done"
version: "MVP"
etapas: ["ideacion: omitida", "analisis: omitida", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Narrador]]"
docs: ["[[15 Flujo de trabajo y calidad]]", "[[18 Biblia narrativa]]"]
arriba: "[[F0.12 Limpieza y coherencia del diseño]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:557"
generado: true
---

# F0-51 Registro de hilos narrativos y cabos sueltos

> Cada pista, promesa o secreto con dónde se siembra, dónde se resuelve y qué cambia. El build marca lo sembrado sin resolver y lo resuelto…

Cada pista, promesa o secreto con dónde se siembra, dónde se resuelve y qué cambia. El build marca lo sembrado sin resolver y lo resuelto sin sembrar, y los personajes que desaparecen de un acto. Parte de la biblia narrativa (F0.11).

## Hecha cuando

Registro cargado con los hilos de la biblia y comprobaciones activas en el hub.

## Flujo por etapas

Especialista de producción: [[Narrador]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | omitida |  |  | El esquema del registro lo fijó el coordinador siguiendo el de las decisiones |
| [[Etapa Análisis\|analisis]] | omitida |  |  | La extracción de hilos la hace el narrador al cargar el registro y deja las preguntas al autor |
| [[Etapa Producción\|produccion]] | hecha | [[Narrador]] | 2026-10-13 | El narrador cargó los hilos y el desarrollador de herramientas construyó la validación y la vista; el coordinador añadió la fila «En escena», ajustó C18 y añadió sus pruebas; el autor decidió cinco hilos; limpieza 71 % y coherencia 94 % |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-13 | QA aprobó el build, el esquema, los datos y el código del hub; las pruebas que faltaban de C18 se añadieron y el autor decidió la deuda familiar, que quedó según el estatus al cerrar (77 pruebas, limpieza 71 %, coherencia 94 %) |
| [[Etapa Revisión del autor\|autor]] | hecha | [[Fran (autor)]] | 2026-10-13 | El autor revisó el registro y la vista #/hilos y aprobó desde /equipo |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-13 | Tarea cerrada y PR #45 fusionado |

### Hallazgos

- [[QA técnico]] (qa, resuelto):  → resuelto por [[Coordinador (Claude)]]: Se añadieron tres pruebas de la regla de C18 y el autor decidió que la deuda familiar depende del estatus al cerrar, sin mecánica nueva

## Traspasos

- 2026-10-13 · [[Coordinador (Claude)]] → [[Narrador]] (entrega): Cargar en hilos.json cada pista, promesa y secreto con dónde se siembra y dónde se resuelve
- 2026-10-13 · [[Coordinador (Claude)]] → [[Desarrollador de herramientas]] (entrega): Construir la validación en el build, las comprobaciones de coherencia y la vista #/hilos del hub sobre el esquema de hilos.json
- 2026-10-13 · [[Narrador]] → [[Coordinador (Claude)]] (entrega): Hilos cargados y cuatro decisiones del autor aplicadas
- 2026-10-13 · [[Desarrollador de herramientas]] → [[Coordinador (Claude)]] (entrega): Validación, chequeos C16 a C19 y vista #/hilos terminadas
- 2026-10-13 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar hilos.json, el código del hub, las pruebas y los documentos tocados
- 2026-10-13 · [[QA técnico]] → [[Fran (autor)]] (entrega): Entrega para tu revisión: el registro de hilos y la vista #/hilos
- 2026-10-13 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobado: pasa al cierre

## Historial

- 2026-10-13 · backlog → doing · claude: Se empieza el registro de hilos narrativos y cabos sueltos con el flujo de especialistas. (rama studio/F0-51-registro-de-hilos)
- 2026-10-13 · doing → review · claude: Registro de 45 hilos, validación y chequeos C16 a C19 en el build, vista #/hilos y fila En escena; QA aprobado y coherencia 94 %. (rama studio/F0-51-registro-de-hilos)
- 2026-10-13 · review → done · claude: El autor aprobó el registro de hilos desde la bandeja de /equipo. (aprobación del autor con el botón «Terminé mi parte»)

## Relaciones

- **Hito:** [[F0.12 Limpieza y coherencia del diseño]]
- **Documentos:** [[15 Flujo de trabajo y calidad]], [[18 Biblia narrativa]]
- **Citada en:** [[15 §Limpieza del diseño]], [[18 §Pendiente]]

## Fuente

`studio/data/roadmap.json:557`
