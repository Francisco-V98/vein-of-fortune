---
id: "F0-48"
tipo: "tarea"
title: "F0-48 Lectura final y coherencia de la biblia narrativa"
aliases: ["F0-48"]
fase: "[[F0 Diseño]]"
hito: "[[F0.11 Biblia narrativa]]"
prio: "P2"
est: 2
status: "done"
version: "MVP"
etapas: ["ideacion: omitida", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Narrador]]"
docs: ["[[18 Biblia narrativa]]", "[[21 Pasado de Valdoria y de la Aetherita]]", "[[22 Acto II - las tres variantes de Reme]]", "[[23 Árbol de decisiones y consecuencias]]", "[[24 Umbrales de acto]]", "[[25 Finales y epílogos]]"]
arriba: "[[F0.11 Biblia narrativa]]"
tags: ["estado/hecho", "prio/P2", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:524"
generado: true
---

# F0-48 Lectura final y coherencia de la biblia narrativa

> Revisión de que la biblia no se contradice con los documentos del juego, actualización del mapa de historia y de la presentación, y lista…

Revisión de que la biblia no se contradice con los documentos del juego, actualización del mapa de historia y de la presentación, y lista de lo que falta para empezar los guiones.

## Hecha cuando

Biblia revisada y sin contradicciones; mapa de historia actualizado.

## Flujo por etapas

Especialista de producción: [[Narrador]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | omitida |  |  | Es una auditoría: no hay opciones que explorar |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-12 | Las dos auditorías cruzaron la narrativa y el diseño del juego: el apellido nuevo está limpio y las fechas, edades, cupos y tramos coinciden; quedan decisiones que condicionan trabajo futuro y errores mecánicos |
| [[Etapa Producción\|produccion]] | hecha | [[Narrador]] | 2026-10-12 | Dos narradores trabajaron en paralelo, uno en el diseño y los datos y otro en la narrativa; limpieza 71 % y coherencia 86 % |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-13 | QA aprobó el build, los restos de nombres antiguos y los renombres; sus cinco arreglos y observaciones los aplicó el coordinador y comprobó con el build estricto y las pruebas (limpieza 71 %, coherencia 86 %) |
| [[Etapa Revisión del autor\|autor]] | hecha | [[Fran (autor)]] | 2026-10-13 | El autor revisó los cambios de la lectura final y aprobó el PR #42 |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-13 | Tarea cerrada y PR #42 fusionado |

### Hallazgos

- [[Analista de coherencia]] (analisis, resuelto): El diseño dice un medidor por facción y la narrativa fija cuatro medidores, y existen tres tareas F4 para los de las facciones → resuelto por [[Narrador]]: Aplicado en los documentos de diseño y de narrativa, en los datos y en el roadmap con las decisiones del autor
- [[Analista de coherencia]] (analisis, resuelto): El periodo de la cuota y el primer vencimiento del Acto I no están definidos aunque el texto del Acto I y el árbol los usan → resuelto por [[Narrador]]: Aplicado en los documentos de diseño y de narrativa, en los datos y en el roadmap con las decisiones del autor
- [[Analista de coherencia]] (analisis, resuelto): La Aetherita se negocia en el mercado negro del Acto III pero el mapa la sitúa en el IV, y el escáner del Acto I necesita cuarzo que aparece después → resuelto por [[Narrador]]: Aplicado en los documentos de diseño y de narrativa, en los datos y en el roadmap con las decisiones del autor
- [[Analista de coherencia]] (analisis, resuelto): La vigilancia se mide a la vez en puntos, en porcentaje y por lugares, y la escalera de estatus es tentativa en un documento y confirmada en otros → resuelto por [[Narrador]]: Aplicado en los documentos de diseño y de narrativa, en los datos y en el roadmap con las decisiones del autor
- [[Analista de coherencia]] (analisis, resuelto): El cian y el rojo del farol chocan con la regla de color de la Aetherita → resuelto por [[Narrador]]: Aplicado en los documentos de diseño y de narrativa, en los datos y en el roadmap con las decisiones del autor
- [[Analista de coherencia]] (analisis, resuelto): Hay ✅ y 🟡 mezclados, siete preguntas abiertas en el documento 25, tres usos de «puerta» y dos de «pieza», el glosario sin once términos y celdas del mapa y de la presentación desactualizadas → resuelto por [[Narrador]]: Aplicado en los documentos de diseño y de narrativa, en los datos y en el roadmap con las decisiones del autor
- [[QA técnico]] (qa, resuelto):  → resuelto por [[Coordinador (Claude)]]: Corregidos la palabra entrada en decisions.json y el roadmap, el cierre del Acto I en F3-17, las descripciones de F4-129 a F4-131 y F4-141, las líneas de ejemplo en 🟡 y el ejemplo del documento 15

## Traspasos

- 2026-10-12 · [[Coordinador (Claude)]] → [[Analista de coherencia]] (entrega): Encargo: leer la biblia narrativa y los documentos del juego buscando contradicciones, cifras que no coinciden y términos sin glosario
- 2026-10-12 · [[Analista de coherencia]] → [[Coordinador (Claude)]] (entrega): Dos auditorías con hallazgos mecánicos y decisiones que condicionan el futuro, y la lista de lo que falta para los guiones
- 2026-10-13 · [[Narrador]] → [[Coordinador (Claude)]] (entrega): Dos partes aplicadas y verificadas con el build estricto y las pruebas
- 2026-10-13 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar los cambios de la lectura final en los documentos, los datos y el roadmap
- 2026-10-13 · [[QA técnico]] → [[Fran (autor)]] (entrega): Entrega para tu revisión: lectura final de la biblia con tus decisiones aplicadas
- 2026-10-13 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobado: pasa al cierre

## Historial

- 2026-10-12 · backlog → doing · claude: Se empieza la lectura final y de coherencia de la biblia narrativa con el flujo de especialistas. (rama studio/F0-48-lectura-final-biblia)
- 2026-10-13 · doing → review · claude: Lectura final con once decisiones del autor y dieciocho correcciones aplicadas en 28 archivos; QA aprobado y limpieza 71 %. (rama studio/F0-48-lectura-final-biblia)
- 2026-10-13 · review → done · claude: El autor aprobó la lectura final de la biblia desde el PR #42. (aprobación del autor en el PR #42)

## Relaciones

- **Hito:** [[F0.11 Biblia narrativa]]
- **Documentos:** [[18 Biblia narrativa]], [[21 Pasado de Valdoria y de la Aetherita]], [[22 Acto II - las tres variantes de Reme]], [[23 Árbol de decisiones y consecuencias]], [[24 Umbrales de acto]], [[25 Finales y epílogos]]
- **Citada en:**
  - [[18 §Estructura de esta biblia]]
  - [[18 §6 Glosario ES - EN]]
  - [[18 §Pendiente]]
  - [[21 §Pendiente]]
  - [[22 §Pendiente]]
  - [[23 §Pendiente]]
  - [[24 §Pendiente]]
  - [[25 §Pendiente]]

## Fuente

`studio/data/roadmap.json:524`
