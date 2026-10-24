---
id: "F0-81"
tipo: "tarea"
title: "F0-81 Mod de consumo de tokens (vf-consumo)"
aliases: ["F0-81"]
fase: "[[F0 Diseño]]"
hito: "[[F0.14 Mods y equipo de agentes]]"
prio: "P2"
est: 4
status: "done"
version: "MVP"
etapas: ["ideacion: omitida", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: hecha", "cierre: hecha"]
especialista: "[[Desarrollador de herramientas]]"
docs: []
arriba: "[[F0.14 Mods y equipo de agentes]]"
tags: ["estado/hecho", "prio/P2", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:839"
generado: true
---

# F0-81 Mod de consumo de tokens (vf-consumo)

> Mod de Claude Code con el comando /consumo: ventana de cinco horas y semanal, tokens por prompt e historial por día, modelo y subagentes…

Mod de Claude Code con el comando /consumo: ventana de cinco horas y semanal, tokens por prompt e historial por día, modelo y subagentes, para ver en qué y cuándo se va el consumo.

## Hecha cuando

El mod valida, pasa sus pruebas, el autor lo revisa y lo instala y el panel muestra el consumo real de una sesión.

## Flujo por etapas

Especialista de producción: [[Desarrollador de herramientas]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | omitida |  |  |  |
| [[Etapa Análisis\|analisis]] | hecha | [[Coordinador (Claude)]] | 2026-10-13 | El coordinador comprobó en la API de los mods que existen los tokens por turno, los porcentajes de las ventanas y el texto del prompt |
| [[Etapa Producción\|produccion]] | hecha | [[Coordinador (Claude)]] | 2026-10-13 | El coordinador escribió el mod, corrigió lo que halló el revisor de código y añadió las pruebas que pidió QA; 16 pruebas |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-13 | QA aprobó la validación, las pruebas, la privacidad y los arreglos; las pruebas que faltaban se añadieron y pasan (16 pruebas) |
| [[Etapa Revisión del autor\|autor]] | hecha | [[Fran (autor)]] | 2026-10-13 | El autor revisó el código del mod y lo aprobó desde /equipo |
| [[Etapa Prueba del autor\|playtest]] | hecha | [[Fran (autor)]] | 2026-10-13 | El autor instaló el mod y lo probó en una sesión real |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-13 | Tarea cerrada y PR #43 fusionado |

### Hallazgos

- [[Revisor de código]] (qa, resuelto):  → resuelto por [[Coordinador (Claude)]]: Subagente tardío, carreras de escritura, prompts solapados, error que no se limpiaba, ventana vencida, reinicio de ventana, turno sin respuesta, cambio de horario y formato de millones corregidos y probados

## Traspasos

- 2026-10-13 · [[Coordinador (Claude)]] → [[Revisor de código]] (entrega): Revisar el código del mod de consumo antes de la prueba del autor
- 2026-10-13 · [[Revisor de código]] → [[Coordinador (Claude)]] (devolucion): Nueve fallos reales y mejoras de claridad en el mod de consumo
- 2026-10-13 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Comprobar la validación, las 12 pruebas y los arreglos del mod de consumo
- 2026-10-13 · [[QA técnico]] → [[Fran (autor)]] (entrega): Entrega para tu revisión y prueba: el mod de consumo, con las instrucciones de instalación en el README
- 2026-10-13 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobado: pasa al cierre

## Historial

- 2026-10-13 · backlog → doing · claude: El autor pidió un mod para ver su consumo de tokens y los porcentajes de las ventanas. (rama studio/F0-81-mod-consumo)
- 2026-10-13 · doing → review · claude: Mod vf-consumo con tres pestañas, historial propio y 16 pruebas; revisión de código y QA aprobados. (rama studio/F0-81-mod-consumo)
- 2026-10-13 · review → done · claude: El autor revisó el mod, lo instaló y lo aprobó desde la bandeja de /equipo. (aprobación del autor con el botón «Terminé mi parte»)

## Relaciones

- **Hito:** [[F0.14 Mods y equipo de agentes]]

## Fuente

`studio/data/roadmap.json:839`
