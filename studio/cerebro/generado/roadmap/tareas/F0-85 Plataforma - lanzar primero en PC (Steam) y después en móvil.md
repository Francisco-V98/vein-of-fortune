---
id: "F0-85"
tipo: "tarea"
title: "F0-85 Plataforma: lanzar primero en PC (Steam) y después en móvil"
aliases: ["F0-85"]
fase: "[[F0 Diseño]]"
hito: "[[F0.14 Mods y equipo de agentes]]"
prio: "P0"
est: 8
status: "done"
version: "MVP"
etapas: ["ideacion: omitida", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Arquitecto de software]]"
docs: []
arriba: "[[F0.14 Mods y equipo de agentes]]"
tags: ["estado/hecho", "prio/P0", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:875"
generado: true
---

# F0-85 Plataforma: lanzar primero en PC (Steam) y después en móvil

> Cambio de plataforma decidido por el autor: el juego se lanza primero en PC, compatible y preparado para Steam, y solo después de…

Cambio de plataforma decidido por el autor: el juego se lanza primero en PC, compatible y preparado para Steam, y solo después de terminarlo en PC se lleva a móvil. Revisa todo lo que dependía de Android primero: visión, controles y interfaz, resolución, motor y exportación, legal y tiendas, QA, arte, hoja de ruta y fases.

## Hecha cuando

Los documentos y el roadmap reflejan PC primero con Steam y móvil como una fase posterior, y el autor ha decidido las plataformas, los controles y el modelo de venta.

## Flujo por etapas

Especialista de producción: [[Arquitecto de software]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | omitida |  |  | La decisión de plataforma la tomó el autor |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-15 | Inventario de lo que dependía de Android primero, 12 decisiones y riesgos; el autor decidió 8 puntos el 2026-10-15 |
| [[Etapa Producción\|produccion]] | hecha | [[Arquitecto de software]] | 2026-10-15 | Diseñador de sistemas, arquitecto y asesor legal terminaron; la coordinación movió a F4 las tareas de Steam que necesita la página «Próximamente» y añadió 4 tareas nuevas |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-15 | QA devolvió 5 grupos de fallos (menciones móviles, horas de F5, privacidad y EULA para la página, texto obsoleto del doc 11, dos ✅ sin respaldo); se corrigieron y el build estricto y las 77 pruebas pasan |
| [[Etapa Revisión del autor\|autor]] | hecha |  | 2026-10-15 | El autor revisó y aprobó el entregable el 2026-10-15 |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-15 | Tarea cerrada y PR fusionado |

### Hallazgos

- [[QA técnico]] (qa, resuelto): Criterios done_when de F1-07, F1-21, F1-26, F2-14, F2-15, F2-19, F2-20 y F2-25 seguían hablando de táctil, teléfono y APK → resuelto por [[Coordinador (Claude)]]: Se reescribieron los criterios
- [[QA técnico]] (qa, resuelto): Doc 18 §1.9 «Diálogo en móvil», doc 20, equipo.json y asesor-legal.md mencionaban móvil o Google Play → resuelto por [[Coordinador (Claude)]]: Se actualizaron a PC y Steam Deck
- [[QA técnico]] (qa, resuelto): F5-23 (privacidad) y F5-24 (EULA) debían estar en F4.19 antes de F4-240 → resuelto por [[Coordinador (Claude)]]: F5-23 y F5-24 se movieron a F4.19
- [[QA técnico]] (qa, resuelto): Doc 11 describía el orden del roadmap como pendiente de corregir → resuelto por [[Coordinador (Claude)]]: Se actualizó el texto del doc 11
- [[QA técnico]] (qa, resuelto): Horas de F5 desfasadas 2 h; cifra de presentation.json de 2.500 h → resuelto por [[Coordinador (Claude)]]: Se corrigieron las horas y la cifra
- [[QA técnico]] (qa, resuelto): Dos ✅ del doc 11 sin decisión del autor (v1 sin IA en vivo y sin azar) pasan a 🟡 → resuelto por [[Coordinador (Claude)]]: Pasan a 🟡

## Traspasos

- 2026-10-15 · [[Coordinador (Claude)]] → [[Analista de coherencia]] (entrega): Encargo: inventario de todo lo que cambia al lanzar primero en PC con Steam y después en móvil, con las decisiones para el autor
- 2026-10-15 · [[Analista de coherencia]] → [[Coordinador (Claude)]] (entrega): Entrega: inventario, 12 decisiones y riesgos
- 2026-10-15 · [[Coordinador (Claude)]] → [[Diseñador de sistemas]] (entrega): Visión, hoja de ruta, controles de minijuegos y sesiones para PC
- 2026-10-15 · [[Diseñador de sistemas]] → [[Coordinador (Claude)]] (entrega): Entrega: docs 00, 01, 02, 04, 06, 09, 26, config, README y agentes; 8 decisiones de diseño abiertas
- 2026-10-15 · [[Coordinador (Claude)]] → [[Arquitecto de software]] (entrega): ADR-0009, enmiendas a ADR-0001 y 0007, docs 10, 14, 15, 16, 12 y casos de prueba para PC
- 2026-10-15 · [[Arquitecto de software]] → [[Coordinador (Claude)]] (entrega): Entrega: ADR-0009 y documentos técnicos; casos TC-050 a TC-055; build estricto en verde
- 2026-10-15 · [[Coordinador (Claude)]] → [[Asesor legal y de licencias]] (entrega): Verificar requisitos de Steam y actualizar el documento 11
- 2026-10-15 · [[Asesor legal y de licencias]] → [[Coordinador (Claude)]] (entrega): Entrega: documento 11 reescrito para Steam con fuentes verificadas el 2026-10-15; tareas por mover y por crear
- 2026-10-15 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar F0-85: build estricto, pruebas, enlaces, coherencia y que ningún ✅ carezca de decisión del autor
- 2026-10-15 · [[QA técnico]] → [[Coordinador (Claude)]] (devolucion): Devolución: 5 grupos de fallos corregidos por la coordinación
- 2026-10-15 · [[Coordinador (Claude)]] → [[Fran (autor)]] (entrega): Revisión de F0-85: PC primero, Steam y móvil después, con las decisiones de diseño abiertas
- 2026-10-15 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobación de F0-85

## Historial

- 2026-10-15 · backlog → doing · claude: El autor decidió lanzar primero en PC (Steam) y llevar el juego a móvil después de terminarlo en PC. (rama studio/F0-85-lanzamiento-en-pc-primero)
- 2026-10-15 · doing → review · claude: Pasa a revisión del autor tras QA (PR de F0-85)
- 2026-10-15 · review → done · claude: El autor aprobó la tarea (PR #49)

## Relaciones

- **Hito:** [[F0.14 Mods y equipo de agentes]]

## Fuente

`studio/data/roadmap.json:875`
