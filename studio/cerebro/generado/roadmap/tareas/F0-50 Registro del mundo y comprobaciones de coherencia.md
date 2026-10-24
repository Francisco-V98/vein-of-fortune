---
id: "F0-50"
tipo: "tarea"
title: "F0-50 Registro del mundo y comprobaciones de coherencia"
aliases: ["F0-50"]
fase: "[[F0 Diseño]]"
hito: "[[F0.12 Limpieza y coherencia del diseño]]"
prio: "P0"
est: 8
status: "done"
version: "MVP"
docs: []
arriba: "[[F0.12 Limpieza y coherencia del diseño]]"
tags: ["estado/hecho", "prio/P0", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:548"
generado: true
---

# F0-50 Registro del mundo y comprobaciones de coherencia

> Registro de minerales, zonas, minijuegos, mecánicas, recetas, facciones y personajes como fuente de verdad, con comprobaciones contra las…

Registro de minerales, zonas, minijuegos, mecánicas, recetas, facciones y personajes como fuente de verdad, con comprobaciones contra las reglas del diseño y el mapa de historia, y vista de coherencia en el hub.

## Hecha cuando

Registro validado en el build y vista de coherencia con sus hallazgos en el hub.

## Historial

- 2026-10-11 · backlog → doing · claude: El autor pide que el diseño sea decidido y coherente: sin cabos sueltos ni números que rompan la economía. (rama studio/F0-50-registro-del-mundo)
- 2026-10-11 · doing → review · claude: Registro del mundo, 11 reglas de coherencia con 92 comprobaciones, vista en el hub y 11 pruebas. (rama studio/F0-50-registro-del-mundo)
- 2026-10-11 · review → done · claude: El autor revisó y aprobó el PR y se fusionó en main. (PR #11)

## Comentarios

- 2026-10-11 · autor: Necesito que sea tanto decidido como coherente. Todo se irá ajustando según vayamos definiendo, pero la idea es llegar al final con todo lo más alto posible.
- 2026-10-11 · claude: El punto de partida es 68 % de coherencia con 29 hallazgos reales: el detector necesita cuarzo y llega antes que él, el oro, el cuarzo y el diamante aparecen antes en las zonas de lo que dice el mapa de historia, y Salitre y Aetherita aparecen en una sola zona contra la regla de 2–3. Ninguno se corrigió: son decisiones del autor. Los números base de los 10 minerales están sin definir (F0-52).

## Evidencias

- image: Vista Coherencia del diseño
- file: Registro del mundo
- note: Verificación

## Relaciones

- **Hito:** [[F0.12 Limpieza y coherencia del diseño]]

## Fuente

`studio/data/roadmap.json:548`
