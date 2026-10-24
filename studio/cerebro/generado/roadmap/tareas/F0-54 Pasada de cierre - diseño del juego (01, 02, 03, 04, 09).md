---
id: "F0-54"
tipo: "tarea"
title: "F0-54 Pasada de cierre: diseño del juego (01, 02, 03, 04, 09)"
aliases: ["F0-54"]
fase: "[[F0 Diseño]]"
hito: "[[F0.12 Limpieza y coherencia del diseño]]"
prio: "P1"
est: 10
status: "done"
version: "MVP"
etapas: ["ideacion: omitida", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Diseñador de sistemas]]"
docs: ["[[27 Guion del Acto I, día a día]]"]
arriba: "[[F0.12 Limpieza y coherencia del diseño]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:584"
generado: true
---

# F0-54 Pasada de cierre: diseño del juego (01, 02, 03, 04, 09)

> Presentar al autor los puntos y de los documentos de núcleo, extracción, comercio, progresión y minijuegos, decidirlos y dejarlos o con su…

Presentar al autor los puntos 🟡 y ❓ de los documentos de núcleo, extracción, comercio, progresión y minijuegos, decidirlos y dejarlos ✅ o ⏳ con su tarea.

## Hecha cuando

Cada documento por encima de la meta de limpieza.

## Flujo por etapas

Especialista de producción: [[Diseñador de sistemas]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | omitida |  |  | Es una pasada de cierre: no hay opciones que explorar |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-15 | El analista dejó 14 preguntas en siete rondas, un lote de confirmaciones menores, las contradicciones con los documentos de historia y la lista de números para F0-52 |
| [[Etapa Producción\|produccion]] | hecha | [[Diseñador de sistemas]] | 2026-10-15 | El diseñador de sistemas aplicó las decisiones de cuatro rondas y una final del autor; el coordinador ajustó el roadmap, la presentación y la comprobación C2; limpieza 78 %, coherencia 94 % |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-15 | QA aprobó el build, las 103 referencias a tareas, las sumas de horas y la coherencia con la historia; sus seis fallos del roadmap, la presentación y los documentos 09, 17 y 26 se corrigieron y el coordinador comprobó el build y las pruebas |
| [[Etapa Revisión del autor\|autor]] | hecha | [[Fran (autor)]] | 2026-10-15 | El autor revisó y aprobó el entregable el 2026-10-15 |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-15 | Tarea cerrada y PR fusionado |

### Hallazgos

- [[Analista de coherencia]] (analisis, resuelto): Catorce puntos del núcleo condicionan la economía, los guiones o los documentos de historia y deben decidirse con el autor antes de cerrar la pasada → resuelto por [[Diseñador de sistemas]]: Decidido con el autor en cinco rondas y aplicado en los documentos 01, 02, 03, 04 y 09 y en los de historia; roadmap ajustado
- [[Analista de coherencia]] (analisis, resuelto): Hay contradicciones entre los documentos 01 a 09 y los de historia sobre la Unión y los empleados, el taller, las ayudas del legado y los resultados de los minijuegos → resuelto por [[Diseñador de sistemas]]: Decidido con el autor en cinco rondas y aplicado en los documentos 01, 02, 03, 04 y 09 y en los de historia; roadmap ajustado
- [[Analista de coherencia]] (analisis, resuelto): La descripción de F0-52 omite impuestos, multas, vigilancia, información y renta, que sí necesitan números → resuelto por [[Diseñador de sistemas]]: Decidido con el autor en cinco rondas y aplicado en los documentos 01, 02, 03, 04 y 09 y en los de historia; roadmap ajustado
- [[QA técnico]] (qa, resuelto):  → resuelto por [[Coordinador (Claude)]]: Se completaron F4-154 y F2-02 con el costo en dinero y las zonas profundas, se creó F4-245 para la mejora de tienda, se movió la Detonación a F4-48 y se corrigieron textos viejos en los documentos 17 y 26 y en la presentación

## Traspasos

- 2026-10-15 · [[Coordinador (Claude)]] → [[Analista de coherencia]] (entrega): Encargo: extraer y clasificar los puntos abiertos de los documentos 01, 02, 03, 04 y 09 para llevarlos al autor por rondas
- 2026-10-15 · [[Analista de coherencia]] → [[Coordinador (Claude)]] (entrega): Catorce preguntas en siete rondas y un lote de confirmaciones para el autor
- 2026-10-15 · [[Coordinador (Claude)]] → [[Diseñador de sistemas]] (entrega): Aplicar las decisiones del autor y el lote en los documentos 01, 02, 03, 04 y 09 y corregir las contradicciones
- 2026-10-15 · [[Diseñador de sistemas]] → [[Coordinador (Claude)]] (entrega): Documentos del núcleo cerrados y lista de tareas del roadmap por ajustar
- 2026-10-15 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar los documentos 01 a 04 y 09, los cambios en 05, 06, 10, 14, 17, 18, 22, 24, 26 y 27, world.json, presentation.json, coherence.py y el roadmap
- 2026-10-15 · [[QA técnico]] → [[Fran (autor)]] (entrega): Entrega para tu revisión: documentos 01, 02, 03, 04 y 09 cerrados
- 2026-10-15 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobación de F0-54

## Historial

- 2026-10-15 · backlog → doing · claude: Se empieza la pasada de cierre del diseño del juego (documentos 01, 02, 03, 04 y 09). (rama studio/F0-54-cierre-diseno-del-juego)
- 2026-10-15 · doing → review · claude: Pasa a revisión del autor tras QA (PR #48)
- 2026-10-15 · review → done · claude: El autor aprobó la tarea (PR #48)

## Relaciones

- **Hito:** [[F0.12 Limpieza y coherencia del diseño]]
- **Documentos:** [[27 Guion del Acto I, día a día]]
- **Citada en:** [[27 §1 Decisiones del autor]]

## Fuente

`studio/data/roadmap.json:584`
