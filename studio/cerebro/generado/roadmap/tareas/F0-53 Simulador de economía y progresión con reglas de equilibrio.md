---
id: "F0-53"
tipo: "tarea"
title: "F0-53 Simulador de economía y progresión con reglas de equilibrio"
aliases: ["F0-53"]
fase: "[[F0 Diseño]]"
hito: "[[F0.12 Limpieza y coherencia del diseño]]"
prio: "P1"
est: 16
status: "done"
version: "MVP"
etapas: ["ideacion: omitida", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Economista y balance]]"
docs: ["[[03 Comercio y mercado]]", "[[02 Extracción]]", "[[15 Flujo de trabajo y calidad]]", "[[23 Árbol de decisiones y consecuencias]]", "[[24 Umbrales de acto]]", "[[28 Números base de la economía]]"]
arriba: "[[F0.12 Limpieza y coherencia del diseño]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:575"
generado: true
---

# F0-53 Simulador de economía y progresión con reglas de equilibrio

> Simulación sin interfaz de miles de días. Comprueba que no hay bucles de ganancia infinita, que la deuda del Acto I se paga en su plazo sin…

Simulación sin interfaz de miles de días. Comprueba que no hay bucles de ganancia infinita, que la deuda del Acto I se paga en su plazo sin ser trivial, que mejorar una herramienta no se paga sola en una expedición, que los ingresos por hora crecen de forma razonable y que no hay una zona siempre óptima. Debe comprobar también que el impacto del jugador en el precio crece con su volumen y patrimonio sin crear bucles de ganancia (documento 03), y que contratar Mineros empleados no domina al jugador.

## Hecha cuando

Simulador en las pruebas automáticas con las reglas de equilibrio como casos y resultados visibles en el hub.

## Flujo por etapas

Especialista de producción: [[Economista y balance]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | omitida |  |  | El simulador y sus reglas ya están descritos en la tarea y en el documento 28 |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-15 | Reglas de equilibrio como 50 casos medibles, datos que lee el simulador, vista del hub y criterios de aceptación; el autor decidió 8 puntos el 2026-10-15 |
| [[Etapa Producción\|produccion]] | hecha |  |  | Simulador en tools/sim con 50 reglas (50 pasan), vista #/simulador, pruebas y CI; el autor aprobó los ajustes de cifras en 5 rondas |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-16 | QA devolvió un fallo grave en la vista del simulador y varias cifras viejas en documentos; se corrigieron y el build estricto y las 251 pruebas pasan |
| [[Etapa Revisión del autor\|autor]] | hecha |  | 2026-10-16 | El autor revisó y aprobó el entregable el 2026-10-16 |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-16 | Tarea cerrada y PR fusionado |

### Hallazgos

- [[QA técnico]] (qa, resuelto): La vista #/simulador se rompía con el resultados.json real (referencias como dict) → resuelto por [[Desarrollador de herramientas]]: app.js y build.py aceptan dict o lista, con 6 pruebas nuevas, entre ellas una con el resultado real
- [[QA técnico]] (qa, resuelto): El hub tenía los pisos de estatus viejos escritos a mano → resuelto por [[Desarrollador de herramientas]]: Se leen de los datos
- [[QA técnico]] (qa, resuelto): El modo rápido tardaba 80 s en la CLI → resuelto por [[Desarrollador de herramientas]]: --rapido no ejecuta las mutaciones por defecto: 33 s; la prueba cronometra lo mismo que la CLI
- [[QA técnico]] (qa, resuelto): Cifras viejas de sueldos, eficiencias, pisos y ritmos en los documentos 04, 23, 24, 25 y 28 → resuelto por [[Coordinador (Claude)]]: Se corrigieron y se alinearon con world.json
- [[QA técnico]] (qa, resuelto): Texto de la regla D2 (88 %) y de G1 (pares previstos) inconsistente → resuelto por [[Desarrollador de herramientas]]: Alineados en reglas.json y los documentos 04 y 28

## Traspasos

- 2026-10-15 · [[Coordinador (Claude)]] → [[Analista de coherencia]] (entrega): Encargo: reglas de equilibrio del simulador como casos medibles y criterios de aceptación
- 2026-10-15 · [[Analista de coherencia]] → [[Coordinador (Claude)]] (entrega): Entrega: informe con reglas A a I, límites del prototipo, vista #/simulador y criterios de aceptación
- 2026-10-15 · [[Coordinador (Claude)]] → [[Economista y balance]] (entrega): Simulador, reglas, datos y documentos
- 2026-10-16 · [[Economista y balance]] → [[Coordinador (Claude)]] (devolucion): Devolución parcial: 25 reglas fallaban con las cifras de F0-52; propuestas de ajuste
- 2026-10-15 · [[Coordinador (Claude)]] → [[Desarrollador de herramientas]] (entrega): Vista #/simulador, load_sim y paso de CI
- 2026-10-16 · [[Desarrollador de herramientas]] → [[Coordinador (Claude)]] (entrega): Entrega: vista, validación del esquema y 17 pruebas
- 2026-10-16 · [[Coordinador (Claude)]] → [[Diseñador de sistemas]] (entrega): Ajuste de los documentos 01, 04, 05 y 09
- 2026-10-16 · [[Diseñador de sistemas]] → [[Coordinador (Claude)]] (entrega): Entrega: documentos ajustados
- 2026-10-16 · [[Coordinador (Claude)]] → [[Narrador]] (entrega): Ajuste de los documentos 17, 19, 23, 25 y 26
- 2026-10-16 · [[Narrador]] → [[Coordinador (Claude)]] (entrega): Entrega: documentos ajustados y oficina de la Comisión
- 2026-10-16 · [[Economista y balance]] → [[Coordinador (Claude)]] (entrega): Entrega: 50 de 50 reglas pasan con los ajustes aprobados
- 2026-10-16 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar F0-53
- 2026-10-16 · [[QA técnico]] → [[Coordinador (Claude)]] (devolucion): Devolución: 1 fallo grave y 5 menores corregidos
- 2026-10-16 · [[Coordinador (Claude)]] → [[Fran (autor)]] (entrega): Revisión de F0-53: simulador, resultados y ajustes
- 2026-10-16 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobación de F0-53

## Historial

- 2026-10-15 · backlog → doing · claude: Se empieza el simulador de economía y progresión (rama studio/F0-53-simulador-de-economia)
- 2026-10-16 · doing → review · claude: Pasa a revisión del autor tras QA (PR de F0-53)
- 2026-10-16 · review → done · claude: El autor aprobó la tarea (PR #51)

## Relaciones

- **Hito:** [[F0.12 Limpieza y coherencia del diseño]]
- **Documentos:** [[03 Comercio y mercado]], [[02 Extracción]], [[15 Flujo de trabajo y calidad]], [[23 Árbol de decisiones y consecuencias]], [[24 Umbrales de acto]], [[28 Números base de la economía]]
- **Citada en:**
  - [[02 §Menas y detector de probabilidades]]
  - [[02 §Herramientas]]
  - [[03 §Oferta y demanda]]
  - [[15 §Limpieza del diseño]]
  - [[23 §2 Reglas del árbol]]
  - [[23 §Pendiente]]
  - [[24 §4 Las tres vías]]
  - [[24 §10 La red anti-atasco]]
  - [[24 §Pendiente]]
  - [[28 §5 Herramientas]]
  - [[28 §8 Empleados]]
  - [[28 §10 Vigilancia, multas, mercado negro y mora]]
  - [[28 Números base de la economía]]

## Fuente

`studio/data/roadmap.json:575`
