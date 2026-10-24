---
id: "F0-52"
tipo: "tarea"
title: "F0-52 Modelo económico: números base"
aliases: ["F0-52"]
fase: "[[F0 Diseño]]"
hito: "[[F0.12 Limpieza y coherencia del diseño]]"
prio: "P1"
est: 10
status: "done"
version: "MVP"
etapas: ["ideacion: omitida", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Economista y balance]]"
docs: ["[[06 Roadmap, ideas futuras y pendientes]]", "[[28 Números base de la economía]]"]
arriba: "[[F0.12 Limpieza y coherencia del diseño]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:566"
generado: true
---

# F0-52 Modelo económico: números base

> Decidir con el autor los números base: precio y volatilidad de cada mineral, sectores de demanda, spreads, costos de herramientas…

Decidir con el autor los números base: precio y volatilidad de cada mineral, sectores de demanda, spreads, costos de herramientas, salarios, deuda y duración del día. Se cargan en el registro del mundo. Incluye también impuestos, multas, vigilancia, precios de información, renta, mora, mejora de tienda para contratar, materiales de reparar, energía por mena, pérdida y minutos por día frente a contratos de 7, 14 y 30 días. Incluye los salarios y el entrenamiento de empleados, el impacto del jugador en el precio y el costo del viaje y de la mejora de tienda.

## Hecha cuando

Todos los minerales con precio base, volatilidad y demanda; costos y salarios acordados.

## Flujo por etapas

Especialista de producción: [[Economista y balance]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | omitida |  |  | Las propuestas de números las hace el economista en producción |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-15 | Inventario: ~15 familias de números, 19 decisiones, 14 contradicciones y criterios de aceptación; se decide en 4 o 5 rondas con el autor |
| [[Etapa Producción\|produccion]] | hecha | [[Economista y balance]] | 2026-10-15 | Documento 28 nuevo, cifras cargadas en 20 documentos, world.json y roadmap; sin ⏳ F0-52 |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-15 | QA devolvió 10 puntos menores (un «90 días» en F0-52, ritmo del Acto II mal rotulado, símbolo de moneda sin tarea, F4-31 contradictoria, deuda de luz en 🟡); se corrigieron y el build estricto y las 108 pruebas pasan |
| [[Etapa Revisión del autor\|autor]] | hecha |  | 2026-10-15 | El autor revisó y aprobó el entregable el 2026-10-15 |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-15 | Tarea cerrada y PR fusionado |

### Hallazgos

- [[QA técnico]] (qa, resuelto): La descripción de F0-52 seguía diciendo contratos de 7, 30 y 90 días → resuelto por [[Coordinador (Claude)]]: Se corrigió a 7, 14 y 30 días
- [[QA técnico]] (qa, resuelto): El documento 28 citaba en negativo la «meta de sesiones cortas» y los contratos de 90 días → resuelto por [[Coordinador (Claude)]]: Se reescribió sin esas menciones
- [[QA técnico]] (qa, resuelto): Los minutos de ritmo del Acto II usaban el ritmo del final del acto y decían «inicio» → resuelto por [[Coordinador (Claude)]]: Se corrigieron las cifras (3,8 h y 33 min al inicio) y se rotuló el final del acto
- [[QA técnico]] (qa, resuelto): F2-20 no recogía la decisión del símbolo de la moneda → resuelto por [[Coordinador (Claude)]]: Se añadió a su descripción
- [[QA técnico]] (qa, resuelto): Los documentos 03 y 28 decían que F4-31 puede reasignar pesos, contra su descripción → resuelto por [[Coordinador (Claude)]]: Se unificó: F4-31 construye el modelo y los eventos con los pesos de F0-52
- [[QA técnico]] (qa, resuelto): La deuda de luz seguía en 🟡 en el doc 24 y se llamaba igual que la cuota extra en el doc 22 → resuelto por [[Coordinador (Claude)]]: Pasa a ✅ y la orden de A2 se llama «cuota extra de luz»

## Traspasos

- 2026-10-15 · [[Coordinador (Claude)]] → [[Analista de coherencia]] (entrega): Encargo: inventario de todo lo que F0-52 debe fijar, con las restricciones ya decididas
- 2026-10-15 · [[Analista de coherencia]] → [[Coordinador (Claude)]] (entrega): Entrega: inventario de F0-52 con 19 decisiones por orden, 14 contradicciones y criterios de aceptación
- 2026-10-15 · [[Coordinador (Claude)]] → [[Economista y balance]] (entrega): Propuesta numérica completa con simulaciones del Acto I
- 2026-10-15 · [[Economista y balance]] → [[Coordinador (Claude)]] (entrega): Entrega: propuesta con 16 secciones, 10 decisiones y 14 contradicciones
- 2026-10-15 · [[Economista y balance]] → [[Coordinador (Claude)]] (entrega): Entrega: documento 28 y world.json con las cifras
- 2026-10-15 · [[Coordinador (Claude)]] → [[Diseñador de sistemas]] (entrega): Cifras en los documentos 01 a 09 y 15
- 2026-10-15 · [[Diseñador de sistemas]] → [[Coordinador (Claude)]] (entrega): Entrega: 43 ⏳ F0-52 resueltos
- 2026-10-15 · [[Coordinador (Claude)]] → [[Narrador]] (entrega): Cifras en los documentos de historia y datos de decisiones e hilos
- 2026-10-15 · [[Narrador]] → [[Coordinador (Claude)]] (entrega): Entrega: 71 ⏳ F0-52 resueltos
- 2026-10-15 · [[Coordinador (Claude)]] → [[Desarrollador de herramientas]] (entrega): Comprobaciones C20 a C32 de los datos económicos y pruebas
- 2026-10-15 · [[Desarrollador de herramientas]] → [[Coordinador (Claude)]] (entrega): Entrega: 13 comprobaciones nuevas y 108 pruebas
- 2026-10-15 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar F0-52
- 2026-10-15 · [[QA técnico]] → [[Coordinador (Claude)]] (devolucion): Devolución: 6 puntos corregidos por la coordinación
- 2026-10-15 · [[Coordinador (Claude)]] → [[Fran (autor)]] (entrega): Revisión de F0-52: documento 28 y cifras base
- 2026-10-15 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobación de F0-52

## Historial

- 2026-10-15 · backlog → doing · claude: Se empieza el modelo económico: números base (rama studio/F0-52-numeros-base-de-la-economia)
- 2026-10-15 · doing → review · claude: Pasa a revisión del autor tras QA (PR de F0-52)
- 2026-10-15 · review → done · claude: El autor aprobó la tarea (PR #50)

## Relaciones

- **Hito:** [[F0.12 Limpieza y coherencia del diseño]]
- **Documentos:** [[06 Roadmap, ideas futuras y pendientes]], [[28 Números base de la economía]]
- **Citada en:** [[06 §Registro de decisiones]], [[28 §2 Ritmo objetivo y patrimonio]], [[28 §13 Validación con el simulador (F0-53)]], [[28 Números base de la economía]]

## Fuente

`studio/data/roadmap.json:566`
