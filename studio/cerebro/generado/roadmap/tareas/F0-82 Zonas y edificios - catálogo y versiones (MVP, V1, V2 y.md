---
id: "F0-82"
tipo: "tarea"
title: "F0-82 Zonas y edificios: catálogo y versiones (MVP, V1, V2 y evolutivos)"
aliases: ["F0-82"]
fase: "[[F0 Diseño]]"
hito: "[[F0.14 Mods y equipo de agentes]]"
prio: "P1"
est: 8
status: "done"
version: "MVP"
etapas: ["ideacion: hecha", "analisis: omitida", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Diseñador de contenido]]"
docs: ["[[18 Biblia narrativa]]", "[[26 Zonas y edificios]]"]
arriba: "[[F0.14 Mods y equipo de agentes]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:857"
generado: true
---

# F0-82 Zonas y edificios: catálogo y versiones (MVP, V1, V2 y evolutivos)

> Estructura de mapa, zonas y edificaciones donde entras a cada edificio por separado. Qué edificios lleva cada zona según su temática…

Estructura de mapa, zonas y edificaciones donde entras a cada edificio por separado. Qué edificios lleva cada zona según su temática (tiendas específicas, joyerías con joyas de la zona, casas y mansiones con distintas vistas, pesca en el puerto, casino, vehículos, embarcaciones, inversiones) y en qué versión entra cada uno, sin que nada se vea puesto sin razón.

## Hecha cuando

Catálogo de edificios por zona acordado con el autor, con la estructura mapa-zona-edificio y la división en MVP, V1, V2 y evolutivos, y sin contradicciones con el mundo y la economía.

## Flujo por etapas

Especialista de producción: [[Diseñador de contenido]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | hecha | [[Ideador e investigador]] | 2026-10-13 | Recomienda que la zona sea la región, con un asentamiento y la boca de mina como una edificación más; catálogo de seis regiones y Puerto Meridiano repartido en MVP, V1 y V2 |
| [[Etapa Análisis\|analisis]] | omitida |  |  | El autor revisó el catálogo del ideador en el chat y decidió estructura, alcance de V1, casas, casino y nombres; el contraste con los documentos lo hace QA |
| [[Etapa Producción\|produccion]] | hecha | [[Diseñador de contenido]] | 2026-10-13 | Correcciones de QA aplicadas y confirmaciones del autor en lote; limpieza 71 % |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-13 | QA aprobó el build, las tareas, las sumas de horas y el canon; sus correcciones las comprobó el coordinador con el build estricto y las pruebas (limpieza 71 %, coherencia 86 %) |
| [[Etapa Revisión del autor\|autor]] | hecha | [[Fran (autor)]] | 2026-10-13 | El autor revisó el documento 26 y las tareas nuevas y aprobó desde /equipo |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-13 | Tarea cerrada y PR #44 fusionado |

### Hallazgos

- [[QA técnico]] (qa, resuelto): Hay ✅ sin respaldo del autor en el reparto por versiones, los nombres de las casas, la concesionaria y la sastrería, el Salón del Farol y los actos por asentamiento → resuelto por [[Diseñador de contenido]]: Marcas corregidas con las confirmaciones del autor, cuenta de 44 edificaciones más la aduana evolutiva y horas por edificación de 6 a 10
- [[QA técnico]] (qa, resuelto):  → resuelto por [[Coordinador (Claude)]]: El auto de V1 pasa a ser solo estatus y aspecto, el efecto funcional llega con la concesionaria de V2.1 y las ranuras de la casa pasan a F4.7 antes de la casa mejorable
- [[QA técnico]] (qa, resuelto): El catálogo tiene 45 filas porque incluye la aduana como evolutivo, pero el total y F0-83 dicen 44; las horas por edificación de las tareas F4 no cuadran con el supuesto de 8 a 10 horas → resuelto por [[Diseñador de contenido]]: Marcas corregidas con las confirmaciones del autor, cuenta de 44 edificaciones más la aduana evolutiva y horas por edificación de 6 a 10

## Traspasos

- 2026-10-13 · [[Coordinador (Claude)]] → [[Ideador e investigador]] (entrega): Encargo: catálogo de edificios por zona y su reparto en MVP, V1, V2 y evolutivos
- 2026-10-13 · [[Ideador e investigador]] → [[Coordinador (Claude)]] (entrega): Catálogo de edificios por zona y reparto en versiones, con once preguntas para el autor
- 2026-10-13 · [[Coordinador (Claude)]] → [[Diseñador de contenido]] (entrega): Escribir el documento 26 con el catálogo de zonas y edificios y las versiones
- 2026-10-13 · [[Diseñador de contenido]] → [[Coordinador (Claude)]] (entrega): Documento 26 entregado con la lista de tareas por crear
- 2026-10-13 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar el documento 26, los cambios en 02, 04, 05, 06, 07, 11, 17, 18 y 21 y las tareas nuevas del roadmap
- 2026-10-13 · [[QA técnico]] → [[Diseñador de contenido]] (devolucion): Devolución: bajar a 🟡 los ✅ sin respaldo, decidir si la aduana cuenta y alinear las horas por edificación
- 2026-10-13 · [[Diseñador de contenido]] → [[Coordinador (Claude)]] (entrega): Correcciones de la devolución de QA y confirmaciones aplicadas
- 2026-10-13 · [[QA técnico]] → [[Fran (autor)]] (entrega): Entrega para tu revisión: documento 26 con las zonas, los edificios y las versiones
- 2026-10-13 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobado: pasa al cierre

## Historial

- 2026-10-13 · backlog → doing · claude: El autor pidió una visión de zonas y edificios para el mapa vivo, dividida en versiones. (rama studio/F0-82-zonas-y-edificios)
- 2026-10-13 · doing → review · claude: Documento 26 con el catálogo de zonas y edificios por versiones y 37 tareas nuevas en el roadmap; QA aprobado y limpieza 71 %. (rama studio/F0-82-zonas-y-edificios)
- 2026-10-13 · review → done · claude: El autor aprobó el catálogo de zonas y edificios desde la bandeja de /equipo. (aprobación del autor con el botón «Terminé mi parte»)

## Relaciones

- **Hito:** [[F0.14 Mods y equipo de agentes]]
- **Documentos:** [[18 Biblia narrativa]], [[26 Zonas y edificios]]
- **Citada en:** [[18 §6 Glosario ES - EN]], [[18 §Pendiente]], [[26 Zonas y edificios]]

## Fuente

`studio/data/roadmap.json:857`
