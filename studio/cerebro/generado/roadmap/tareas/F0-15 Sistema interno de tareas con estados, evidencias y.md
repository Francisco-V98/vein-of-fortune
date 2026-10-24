---
id: "F0-15"
tipo: "tarea"
title: "F0-15 Sistema interno de tareas con estados, evidencias y comentarios"
aliases: ["F0-15"]
fase: "[[F0 Diseño]]"
hito: "[[F0.4 Proceso y herramientas]]"
prio: "P1"
est: 10
status: "done"
version: "MVP"
docs: []
arriba: "[[F0.4 Proceso y herramientas]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:184"
generado: true
---

# F0-15 Sistema interno de tareas con estados, evidencias y comentarios

> Reemplaza a Trello. El tablero vive dentro del hub; los estados se guardan en el código y los cambia Claude. Cada tarea tiene historial de…

Reemplaza a Trello. El tablero vive dentro del hub; los estados se guardan en el código y los cambia Claude. Cada tarea tiene historial de estados, comentarios y evidencias.

## Hecha cuando

El hub muestra el tablero con historial, evidencias y comentarios por tarea, y el build valida la coherencia.

## Historial

- 2026-10-11 · backlog → doing · claude: Se descarta Trello. Se rediseña el tablero como sistema interno del estudio.
- 2026-10-11 · doing → review · claude: Implementado: historial por tarea, evidencias, comentarios, detalle de tarea, actividad reciente y validación de coherencia en el build.
- 2026-10-11 · review → done · claude: El autor aprobó la tarea. (aprobación del autor en la conversación)

## Comentarios

- 2026-10-11 · autor: Los estados y los movimientos los hace Claude al 100%. Si una tarea pasa de backlog a en proceso es porque se editaron líneas de código.
- 2026-10-11 · claude: El build compara el estado del roadmap con el último movimiento del historial y avisa si no coinciden. El hub no tiene botones que cambien estados.

## Evidencias

- image: Detalle de tarea en el hub
- file: Validación y generación de datos
- file: Explicación del sistema
- note: Prueba de la validación

## Relaciones

- **Hito:** [[F0.4 Proceso y herramientas]]

## Fuente

`studio/data/roadmap.json:184`
