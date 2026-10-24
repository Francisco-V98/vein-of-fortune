---
id: "F0-45"
tipo: "tarea"
title: "F0-45 Árbol de decisiones y consecuencias de los cuatro actos"
aliases: ["F0-45"]
fase: "[[F0 Diseño]]"
hito: "[[F0.11 Biblia narrativa]]"
prio: "P1"
est: 6
status: "done"
version: "MVP"
etapas: ["ideacion: hecha", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Narrador]]"
docs: ["[[18 Biblia narrativa]]", "[[23 Árbol de decisiones y consecuencias]]"]
arriba: "[[F0.11 Biblia narrativa]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:497"
generado: true
---

# F0-45 Árbol de decisiones y consecuencias de los cuatro actos

> Las bifurcaciones grandes (alianza del Acto II, cómo entras al círculo del Acto III y destino de la Aetherita; la facción de Reme del Acto…

Las bifurcaciones grandes (alianza del Acto II, cómo entras al círculo del Acto III y destino de la Aetherita; la facción de Reme del Acto II es un sorteo, no una decisión) y las consecuencias pequeñas de cada acto, con qué las dispara y qué cambia en el mundo, el mercado y los personajes.

## Hecha cuando

Árbol completo acordado y visible en el hub.

## Flujo por etapas

Especialista de producción: [[Narrador]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | hecha | [[Ideador e investigador]] | 2026-10-12 | Recomienda capas con cupo, banderas como datos y cuellos de botella como dibujo; en el hub, una vista nueva más filas en el mapa |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-12 | El bosquejo encaja con los documentos; el análisis encontró huecos de definición, canon de las cintas y trabajo del hub |
| [[Etapa Producción\|produccion]] | hecha | [[Narrador]] | 2026-10-12 | Narrador y herramientas terminaron; el coordinador comprobó los filtros de la vista en el navegador |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-12 | QA aprobó el build, las pruebas, el canon y la vista; sus dos fallos de marcas se corrigieron (el autor confirmó la orden de Reme y la huelga), se creó F0-75 para el dibujo SVG y el coordinador comprobó los filtros en el navegador |
| [[Etapa Revisión del autor\|autor]] | hecha | [[Fran (autor)]] | 2026-10-12 | El autor revisó el documento 23 y la vista #/decisiones y aprobó el PR #36 |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-12 | Tarea cerrada y PR #36 fusionado |

### Hallazgos

- [[Analista de coherencia]] (analisis, resuelto): Los medidores de la Unión, Esteban, Lucía y Teo no existen en world.json y hay que definirlos con valores numéricos y un ⏳ → resuelto por [[Narrador]]: Resuelto en el documento 23, decisions.json y los documentos 08, 18 y story.json
- [[Analista de coherencia]] (analisis, resuelto): Hay que decidir de dónde sale el reproductor de cintas y qué NPC hace la revisión médica de Teo; ninguno está definido → resuelto por [[Narrador]]: Resuelto en el documento 23, decisions.json y los documentos 08, 18 y story.json
- [[Analista de coherencia]] (analisis, resuelto): El acreedor del Acto II es un sorteo y no una bifurcación, pero lo siguen llamando así los documentos 08 y 18 y el roadmap → resuelto por [[Narrador]]: Resuelto en el documento 23, decisions.json y los documentos 08, 18 y story.json
- [[Analista de coherencia]] (analisis, resuelto): La historia del mapa dice que encuentras las cintas en el Acto IV, y el reparto propuesto las recoge antes: hay que ajustar story.json → resuelto por [[Narrador]]: Resuelto en el documento 23, decisions.json y los documentos 08, 18 y story.json
- [[Analista de coherencia]] (analisis, resuelto): El trabajo de hub estimado sube de seis a ocho o nueve horas; el dibujo SVG del árbol conviene sacarlo a una tarea nueva → resuelto por [[Desarrollador de herramientas]]: Vista #/decisiones y filas del mapa con validación estricta, con el dibujo SVG fuera de esta tarea
- [[QA técnico]] (qa, resuelto):  → resuelto por [[Coordinador (Claude)]]: El autor confirmó la orden de Reme y los bandos de la huelga; se bajaron a 🟡 la biblia sobre Esteban y las pruebas del IV; se quitó el pendiente caduco del documento 23 y se renombró la función de chips de los filtros
- [[QA técnico]] (qa, resuelto):  → resuelto por [[Coordinador (Claude)]]: Se creó F0-75 para el dibujo SVG del árbol y se enlazó con un ⏳ en el documento 23

## Traspasos

- 2026-10-12 · [[Coordinador (Claude)]] → [[Ideador e investigador]] (entrega): Encargo: tres formas de estructurar el árbol de decisiones y consecuencias de los cuatro actos y de mostrarlo en el hub
- 2026-10-12 · [[Ideador e investigador]] → [[Analista de coherencia]] (entrega): Bosquejo del árbol con cupos, banderas y cuellos de botella por comprobar
- 2026-10-12 · [[Analista de coherencia]] → [[Coordinador (Claude)]] (entrega): Comprobación del bosquejo del árbol con cinco hallazgos y siete preguntas para el autor
- 2026-10-12 · [[Coordinador (Claude)]] → [[Narrador]] (entrega): Escribir el documento 23 con el árbol, los datos en decisions.json y resolver los ⏳ F0-45
- 2026-10-12 · [[Narrador]] → [[Coordinador (Claude)]] (entrega): Documento 23 y decisions.json escritos; ⏳ F0-45 resueltos
- 2026-10-12 · [[Coordinador (Claude)]] → [[Desarrollador de herramientas]] (entrega): Construir la vista #/decisiones, las filas del mapa, las validaciones de decisions.json y sus pruebas
- 2026-10-12 · [[Desarrollador de herramientas]] → [[Coordinador (Claude)]] (entrega): Vista #/decisiones, validaciones C12 a C15 y 20 pruebas nuevas
- 2026-10-12 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar el documento 23, decisions.json y la vista del hub antes de la revisión del autor
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): Entrega para tu revisión: documento 23 y la vista #/decisiones
- 2026-10-12 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobado: pasa al cierre

## Historial

- 2026-10-12 · backlog → doing · claude: Se empieza el árbol de decisiones y consecuencias con el flujo de especialistas. (rama studio/F0-45-arbol-de-decisiones)
- 2026-10-12 · doing → review · claude: Documento 23, decisions.json, vista #/decisiones y validaciones del hub; QA aprobado con correcciones, limpieza 66 % y coherencia 83 %. (rama studio/F0-45-arbol-de-decisiones)
- 2026-10-12 · review → done · claude: El autor aprobó el árbol de decisiones y la vista del hub desde el PR #36. (aprobación del autor en el PR #36)

## Relaciones

- **Hito:** [[F0.11 Biblia narrativa]]
- **Documentos:** [[18 Biblia narrativa]], [[23 Árbol de decisiones y consecuencias]]
- **Citada en:** [[18 §Estructura de esta biblia]], [[18 §Pendiente]], [[23 §1 Decisiones del autor]], [[23 §11 Criterios cumplidos]], [[23 §Pendiente]]

## Fuente

`studio/data/roadmap.json:497`
