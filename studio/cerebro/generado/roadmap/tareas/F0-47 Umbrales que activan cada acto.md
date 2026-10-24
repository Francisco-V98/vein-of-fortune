---
id: "F0-47"
tipo: "tarea"
title: "F0-47 Umbrales que activan cada acto"
aliases: ["F0-47"]
fase: "[[F0 Diseño]]"
hito: "[[F0.11 Biblia narrativa]]"
prio: "P1"
est: 3
status: "done"
version: "MVP"
etapas: ["ideacion: hecha", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Narrador]]"
docs: ["[[18 Biblia narrativa]]", "[[24 Umbrales de acto]]"]
arriba: "[[F0.11 Biblia narrativa]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:515"
generado: true
---

# F0-47 Umbrales que activan cada acto

> Reglas concretas para pasar de un acto al siguiente (estatus, deuda, logros, relación con facciones) de modo que se puedan cumplir de…

Reglas concretas para pasar de un acto al siguiente (estatus, deuda, logros, relación con facciones) de modo que se puedan cumplir de varias maneras y no obliguen a seguir la trama al pie de la letra.

## Hecha cuando

Umbrales definidos para los 4 actos y acordados con el autor.

## Flujo por etapas

Especialista de producción: [[Narrador]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | hecha | [[Ideador e investigador]] | 2026-10-12 | Tres modelos: A puerta por acto con vías k de n, B puntuación acumulada, C umbrales por escena; recomienda A con un piso de estatus |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-12 | El modelo A es viable con cinco correcciones; el análisis clasificó cada punto abierto entre decidir ahora y aplazar con su tarea |
| [[Etapa Producción\|produccion]] | hecha | [[Narrador]] | 2026-10-12 | Correcciones de QA aplicadas por el narrador; limpieza 69 % |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-12 | QA aprobó el build, las pruebas y la aritmética de los tramos; las cinco correcciones las comprobó el coordinador con el build estricto y las pruebas (limpieza 69 %, coherencia 83 %) |
| [[Etapa Revisión del autor\|autor]] | hecha | [[Fran (autor)]] | 2026-10-12 | El autor revisó el documento 24 y aprobó los umbrales desde /equipo |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-12 | Tarea cerrada y PR #39 fusionado |

### Hallazgos

- [[Analista de coherencia]] (analisis, resuelto): El Acto I no puede exigir Minero con licencia ni el logro del tutorial: el estatus y los logros llegan en la fase 4, después del Acto I → resuelto por [[Narrador]]: Resuelto en el documento 24 y en los documentos 17, 22 y 23, con la tarea nueva F0-78 para el diario, la cola y la misión de rescate
- [[Analista de coherencia]] (analisis, resuelto): No hay medidor de relación para las tres facciones aliables; solo existen los de la Unión, Esteban, Lucía y Teo → resuelto por [[Narrador]]: Resuelto en el documento 24 y en los documentos 17, 22 y 23, con la tarea nueva F0-78 para el diario, la cola y la misión de rescate
- [[Analista de coherencia]] (analisis, resuelto): La deuda puede regalar o romper la vía: el Consorcio pasa tu deuda a la casa y la deuda de luz de los Faroleros se suma a la tuya → resuelto por [[Narrador]]: Resuelto en el documento 24 y en los documentos 17, 22 y 23, con la tarea nueva F0-78 para el diario, la cola y la misión de rescate
- [[Analista de coherencia]] (analisis, resuelto): El bosquejo omite el primer contacto con empleados, que cierra el Acto I, y dos tramos de medidor coinciden con sus valores de arranque → resuelto por [[Narrador]]: Resuelto en el documento 24 y en los documentos 17, 22 y 23, con la tarea nueva F0-78 para el diario, la cola y la misión de rescate
- [[Analista de coherencia]] (analisis, resuelto): Diario, cola de historia y misión de rescate no existen en ningún documento ni tarea del roadmap → resuelto por [[Narrador]]: Resuelto en el documento 24 y en los documentos 17, 22 y 23, con la tarea nueva F0-78 para el diario, la cola y la misión de rescate
- [[QA técnico]] (qa, resuelto): El disparador de A1 está desactualizado en el documento 23 y en decisions.json: el decreto de A1 abre las zonas y no es una condición previa → resuelto por [[Narrador]]: Corregido en los documentos 23 y 24 y en decisions.json
- [[QA técnico]] (qa, resuelto):  → resuelto por [[Coordinador (Claude)]]: Las restricciones de los documentos 24 se copiaron a la descripción y al criterio de cierre de F4-61, F4-109, F4-116 y F4-133 en el roadmap
- [[QA técnico]] (qa, resuelto): La sección 7 del documento 24 lleva ✅ que el autor no vio, y dos líneas extienden el ✅ a que la deuda de luz no rompe la vía → resuelto por [[Narrador]]: Corregido en los documentos 23 y 24 y en decisions.json
- [[QA técnico]] (qa, resuelto): El camino de Esteban a tramo bajo cuenta una decisión pero hacen falta dos; sigue siendo menos de tres → resuelto por [[Narrador]]: Corregido en los documentos 23 y 24 y en decisions.json
- [[QA técnico]] (qa, resuelto): El nodo de la alianza lee f-orden-reme solo para mostrar el costo de Reme: hay que aclararlo para que no parezca una puerta que lo lee → resuelto por [[Narrador]]: Corregido en los documentos 23 y 24 y en decisions.json

## Traspasos

- 2026-10-12 · [[Coordinador (Claude)]] → [[Ideador e investigador]] (entrega): Encargo: tres modelos de umbral para activar cada acto y sus escenas
- 2026-10-12 · [[Ideador e investigador]] → [[Analista de coherencia]] (entrega): Modelo A de puertas por acto con piso de estatus por comprobar
- 2026-10-12 · [[Analista de coherencia]] → [[Coordinador (Claude)]] (entrega): Comprobación del modelo A con cinco hallazgos, la clasificación de puntos abiertos y nueve preguntas para el autor
- 2026-10-12 · [[Coordinador (Claude)]] → [[Narrador]] (entrega): Escribir el documento 24 con los umbrales de los cuatro actos y cerrar los ⏳ F0-47
- 2026-10-12 · [[Narrador]] → [[Coordinador (Claude)]] (entrega): Documento 24 escrito y confirmaciones del autor aplicadas
- 2026-10-12 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar el documento 24 y los cambios en 08, 17, 18, 22, 23, decisions.json y story.json
- 2026-10-12 · [[QA técnico]] → [[Narrador]] (devolucion): Devolución: corregir el disparador de A1, los ✅ de la sección 7, la cuenta de Esteban y la aclaración de f-orden-reme
- 2026-10-12 · [[Narrador]] → [[Coordinador (Claude)]] (entrega): Correcciones de la devolución de QA aplicadas
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): Entrega para tu revisión: documento 24 con los umbrales de los cuatro actos
- 2026-10-12 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobado: pasa al cierre

## Historial

- 2026-10-12 · backlog → doing · claude: Se empiezan los umbrales de acto con el flujo de especialistas. (rama studio/F0-47-umbrales-de-acto)
- 2026-10-12 · doing → review · claude: Documento 24 con los umbrales de los cuatro actos, ⏳ F0-47 resueltos; QA aprobado tras dos pasadas y limpieza 69 %. (rama studio/F0-47-umbrales-de-acto)
- 2026-10-12 · review → done · claude: El autor aprobó los umbrales de acto desde la bandeja de /equipo. (aprobación del autor con el botón «Terminé mi parte»)

## Relaciones

- **Hito:** [[F0.11 Biblia narrativa]]
- **Documentos:** [[18 Biblia narrativa]], [[24 Umbrales de acto]]
- **Citada en:** [[18 §Estructura de esta biblia]], [[18 §Pendiente]], [[24 §1 Decisiones del autor]], [[24 §Decisiones tomadas]], [[24 §Pendiente]], [[24 Umbrales de acto]]

## Fuente

`studio/data/roadmap.json:515`
