---
id: "F0-80"
tipo: "tarea"
title: "F0-80 Pasada de cierre: biblia, documentos de pasado, variantes, árbol, umbrales y finales, equipo y zonas (18, 20 a 26)"
aliases: ["F0-80"]
fase: "[[F0 Diseño]]"
hito: "[[F0.14 Mods y equipo de agentes]]"
prio: "P1"
est: 9.5
status: "done"
version: "MVP"
etapas: ["ideacion: omitida", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Narrador]]"
docs: ["[[18 Biblia narrativa]]", "[[20 Equipo y flujo de agentes]]", "[[21 Pasado de Valdoria y de la Aetherita]]", "[[22 Acto II - las tres variantes de Reme]]", "[[23 Árbol de decisiones y consecuencias]]", "[[24 Umbrales de acto]]", "[[25 Finales y epílogos]]", "[[26 Zonas y edificios]]", "[[15 Flujo de trabajo y calidad]]", "[[06 Roadmap, ideas futuras y pendientes]]", "[[27 Guion del Acto I, día a día]]"]
arriba: "[[F0.14 Mods y equipo de agentes]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:848"
generado: true
---

# F0-80 Pasada de cierre: biblia, documentos de pasado, variantes, árbol, umbrales y finales, equipo y zonas (18, 20 a 26)

> Repasar con el autor los documentos 18, 20, 21, 22, 23, 24, 25 y 26 hasta llevar cada uno a un 90 % o más de limpieza, confirmando lo que…

Repasar con el autor los documentos 18, 20, 21, 22, 23, 24, 25 y 26 hasta llevar cada uno a un 90 % o más de limpieza, confirmando lo que siga en propuesta y aplazando solo lo que cumpla la regla del documento 15. El guion del Acto I (27) lo cierra [[F0-86 Pasada de cierre - guion del Acto I (27)|F0-86]].

## Hecha cuando

Cada uno de los documentos 18, 20, 21, 22, 23, 24, 25 y 26 llega al 90 % de limpieza o tiene sus puntos abiertos aplazados con una tarea que no condiciona nada anterior.

## Flujo por etapas

Especialista de producción: [[Narrador]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | omitida |  |  | Es una pasada de cierre: los puntos abiertos se deciden con el autor |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-16 | Inventario de 271 propuestas en seis documentos, 14 hallazgos y 12 preguntas más el alcance; el autor decidió en cuatro rondas el 2026-10-16 |
| [[Etapa Producción\|produccion]] | hecha | [[Narrador]] | 2026-10-16 | Narrador (18, 21, 22, 23, 24, 25, 26 y datos de decisiones, hilos e historia) y diseñador (20, 28, 06 y 27) terminaron; la coordinación ajustó 7 tareas del roadmap y creó F0-86 |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-16 | QA devolvió 3 fallos de contenido y varios menores; se corrigieron (tarjetas de los finales a F4-212, tamaños de medidores confirmados por el autor, guion del Acto I, leyendas) y el build estricto y las 258 pruebas pasan |
| [[Etapa Revisión del autor\|autor]] | hecha |  | 2026-10-16 | El autor revisó y aprobó el entregable el 2026-10-16 |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha | [[Coordinador (Claude)]] | 2026-10-16 | Tarea cerrada y PR fusionado |

### Hallazgos

- [[QA técnico]] (qa, resuelto): Límites de tamaño y orden de las tarjetas del documento 25 marcados ✅ sin decisión del autor → resuelto por [[Narrador]]: Vuelven a ⏳ F4-212 y la tarea se amplía
- [[QA técnico]] (qa, resuelto): Tamaños de efecto de los medidores (24 §6) presentados como aceptados sin constancia → resuelto por [[Coordinador (Claude)]]: El autor los confirmó el 2026-10-16: 5, 10 y 20
- [[QA técnico]] (qa, resuelto): El documento 27 seguía diciendo «propuesta pendiente» de lo que F0-80 cerró → resuelto por [[Narrador]]: Líneas 114, 126, 361 y 376 pasan a confirmadas
- [[QA técnico]] (qa, resuelto): Leyendas y «Estado» de 23 y 24 con símbolos → resuelto por [[Narrador]]: Reescritas con palabras
- [[QA técnico]] (qa, resuelto): Patrimonio al entrar en el acta sin estado guardado → resuelto por [[Narrador]]: Nuevo e-patrimonio-acta en 25 §8, F2-01 y F4-109 lo recogen

## Traspasos

- 2026-10-16 · [[Coordinador (Claude)]] → [[Analista de coherencia]] (entrega): Encargo: inventario de puntos abiertos de los documentos 18 y 21 a 25
- 2026-10-16 · [[Analista de coherencia]] → [[Coordinador (Claude)]] (entrega): Entrega: informe de F0-80 con 271 propuestas clasificadas y 12 preguntas
- 2026-10-16 · [[Coordinador (Claude)]] → [[Narrador]] (entrega): Cerrar 18, 21, 26 y 22 a 25 con sus datos
- 2026-10-16 · [[Narrador]] → [[Coordinador (Claude)]] (entrega): Entrega: ocho documentos y los datos sincronizados
- 2026-10-16 · [[Coordinador (Claude)]] → [[Diseñador de sistemas]] (entrega): Documentos 20, 28, 06 y 27 (líneas de propuestas)
- 2026-10-16 · [[Diseñador de sistemas]] → [[Coordinador (Claude)]] (entrega): Entrega: documento 20 al 100 % y correcciones
- 2026-10-16 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Revisar F0-80
- 2026-10-16 · [[QA técnico]] → [[Coordinador (Claude)]] (devolucion): Devolución: 3 fallos de contenido y menores corregidos
- 2026-10-16 · [[Coordinador (Claude)]] → [[Fran (autor)]] (entrega): Revisión de F0-80: biblia y documentos 18 a 26 cerrados
- 2026-10-16 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobación de F0-80

## Historial

- 2026-10-16 · backlog → doing · claude: Se empieza la pasada de cierre de la biblia y los documentos 21 a 25 (rama studio/F0-80-cierre-biblia-y-documentos-narrativos)
- 2026-10-16 · doing → review · claude: Pasa a revisión del autor tras QA (PR de F0-80)
- 2026-10-16 · review → done · claude: El autor aprobó la tarea (PR #53)

## Relaciones

- **Hito:** [[F0.14 Mods y equipo de agentes]]
- **Documentos:**
  - [[18 Biblia narrativa]]
  - [[20 Equipo y flujo de agentes]]
  - [[21 Pasado de Valdoria y de la Aetherita]]
  - [[22 Acto II - las tres variantes de Reme]]
  - [[23 Árbol de decisiones y consecuencias]]
  - [[24 Umbrales de acto]]
  - [[25 Finales y epílogos]]
  - [[26 Zonas y edificios]]
  - [[15 Flujo de trabajo y calidad]]
  - [[06 Roadmap, ideas futuras y pendientes]]
  - [[27 Guion del Acto I, día a día]]
- **Citada en:**
  - [[06 §Registro de decisiones]]
  - [[18 §Estructura de esta biblia]]
  - [[18 §Pendiente]]
  - [[21 §1 Decisiones del autor]]
  - [[21 §Pendiente]]
  - [[22 §2 Las seis escenas ancla]]
  - [[22 §3 Las tres variantes, escena por escena]]
  - [[22 §5 La orden que duele igual]]
  - [[22 §6 El papel de cada personaje]]
  - [[22 §7 La primera huelga - depende de ti]]
  - [[22 §8 Capa de mercado - un precio y el mercado negro]]
  - [[22 §9 La alianza final y el costo para Reme]]
  - [[22 §10 El sorteo y las pistas del Acto I]]
  - [[22 §11 El cierre del acto]]
  - [[22 §Pendiente]]
  - [[22 Acto II - las tres variantes de Reme]]
  - [[23 §2 Reglas del árbol]]
  - [[23 §3 Acto I - tres consecuencias pequeñas]]
  - [[23 §4 Acto II - la política manda]]
  - [[23 §5 Acto III - el ascenso]]
  - [[23 §6 Acto IV - la cima]]
  - [[23 §7 Las ocho cintas]]
  - [[23 §8 Pruebas de Reme en el Acto IV]]
  - [[23 §9 Banderas - quién las fija y quién las lee]]
  - [[23 §Pendiente]]
  - [[23 Árbol de decisiones y consecuencias]]
  - [[24 §5 Los tramos de los medidores y lo que desbloquean]]
  - [[24 §6 Cómo alcanza cada medidor cada tramo]]
  - [[24 §8 Los disparadores de A1 a A6]]
  - [[24 §Pendiente]]
  - [[24 Umbrales de acto]]
  - [[25 §2 Reglas de las tarjetas]]
  - [[25 §4 La cabecera]]
  - [[25 §5 Las 54 piezas]]
  - [[25 §6 Cobertura de combinaciones]]
  - [[25 §8 Estado legible que se guarda]]
  - [[25 §Pendiente]]
  - [[25 Finales y epílogos]]
  - [[26 Zonas y edificios]]
  - [[27 §1 Decisiones del autor]]
  - [[27 §6 Día 3 - El hierro]]
  - [[27 §Puntos confirmados por el autor]]

## Fuente

`studio/data/roadmap.json:848`
