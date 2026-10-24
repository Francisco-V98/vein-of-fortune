---
id: "F0-41"
tipo: "tarea"
title: "F0-41 Biblia narrativa: estructura, voz y glosario"
aliases: ["F0-41"]
fase: "[[F0 Diseño]]"
hito: "[[F0.11 Biblia narrativa]]"
prio: "P1"
est: 3
status: "done"
version: "MVP"
etapas: ["ideacion: hecha", "analisis: hecha", "produccion: hecha", "qa: hecha", "autor: hecha", "playtest: omitida", "cierre: hecha"]
especialista: "[[Narrador]]"
docs: ["[[18 Biblia narrativa]]"]
arriba: "[[F0.11 Biblia narrativa]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:461"
generado: true
---

# F0-41 Biblia narrativa: estructura, voz y glosario

> Documento 18 con la estructura de la biblia narrativa, las reglas de escritura (tono, voz por personaje, cómo se nombra a las facciones y a…

Documento 18 con la estructura de la biblia narrativa, las reglas de escritura (tono, voz por personaje, cómo se nombra a las facciones y a la Aetherita) y un glosario de términos de Valdoria en español e inglés.

## Hecha cuando

Estructura y reglas de escritura acordadas con el autor.

## Flujo por etapas

Especialista de producción: [[Narrador]].

| Etapa | Estado | Por | Fecha | Nota |
|---|---|---|---|---|
| [[Etapa Ideación\|ideacion]] | hecha | [[Ideador e investigador]] | 2026-10-12 | Tres estructuras: por actos (A), por entidades (B) y por escenas y decisiones (C); recomienda B con un anexo de cronología y bifurcaciones |
| [[Etapa Análisis\|analisis]] | hecha | [[Analista de coherencia]] | 2026-10-12 | Se verificaron las cinco comprobaciones del ideador contra los documentos |
| [[Etapa Producción\|produccion]] | hecha | [[Narrador]] | 2026-10-12 | Documento 18 corregido con las decisiones del autor y los fallos de QA; celda de Anselmo corregida en story.json y doc 17 |
| [[Etapa QA\|qa]] | hecha | [[QA técnico]] | 2026-10-12 | Segunda pasada: de 7 fallos quedó 1 (celda de Anselmo en C11), corregido; build estricto, pruebas, enlaces y ⏳ en verde |
| [[Etapa Revisión del autor\|autor]] | hecha |  | 2026-10-12 | Aprobado por el autor con «Todo bien» y «Terminé mi parte» |
| [[Etapa Prueba del autor\|playtest]] | omitida |  |  |  |
| [[Etapa Cierre\|cierre]] | hecha |  | 2026-10-12 | Tarea cerrada y PR #33 fusionado |

### Hallazgos

- [[Analista de coherencia]] (analisis, abierto): 
- [[Analista de coherencia]] (analisis, abierto): 
- [[Analista de coherencia]] (analisis, abierto): 
- [[Analista de coherencia]] (analisis, abierto): 
- [[Narrador]] (produccion, resuelto):  → resuelto por [[Localizador ES - EN]]: La línea del doc 12 pasó a «fragmento de Aetherita»
- [[Narrador]] (produccion, resuelto):  → resuelto por [[Narrador]]: La celda del Acto IV de story.json y del doc 17 dice ahora que aparece desde el Acto I y se revela en el IV
- [[Localizador ES - EN]] (produccion, resuelto):  → resuelto por [[Fran (autor)]]: El autor decidió las 13 dudas: the Pit, the Beacon, ether sickness, Ether Commission y confirmó el resto
- [[QA técnico]] (qa, resuelto):  → resuelto por [[Narrador]]: Limpieza 65 %, fuentes de los ✅ aclaradas, marcas unificadas y un solo ⏳ por cada asunto de las cintas
- [[QA técnico]] (qa, resuelto):  → resuelto por [[Narrador]]: Limpieza 65 %, fuentes de los ✅ aclaradas, marcas unificadas y un solo ⏳ por cada asunto de las cintas
- [[QA técnico]] (qa, resuelto):  → resuelto por [[Narrador]]: Limpieza 65 %, fuentes de los ✅ aclaradas, marcas unificadas y un solo ⏳ por cada asunto de las cintas
- [[QA técnico]] (qa, resuelto):  → resuelto por [[Coordinador (Claude)]]: Anselmo Vidal pasa a la celda de personajes del Acto I y la del Acto IV queda sin nuevos; coherencia 68 % → 70 %

## Traspasos

- 2026-10-12 · [[Coordinador (Claude)]] → [[Ideador e investigador]] (entrega): Encargo: tres opciones para la estructura de la biblia, la voz de cada personaje y el glosario ES/EN
- 2026-10-12 · [[Ideador e investigador]] → [[Analista de coherencia]] (entrega): Tres opciones de estructura y una lista de términos e incoherencias por comprobar
- 2026-10-12 · [[Analista de coherencia]] → [[Coordinador (Claude)]] (entrega): Informe: cuatro hallazgos y seis preguntas que decide el autor antes de producir
- 2026-10-12 · [[Coordinador (Claude)]] → [[Narrador]] (entrega): Decisiones del autor: estructura por entidades con el 19 como fuente, Aetherita mineral y éter fenómeno, usted solo para Quiroga y Montenegro, se traduce casi todo al inglés
- 2026-10-12 · [[Narrador]] → [[Localizador ES - EN]] (entrega): Documento 18 con el capítulo 6 (glosario) vacío para que el localizador lo complete en ES/EN
- 2026-10-12 · [[Localizador ES - EN]] → [[QA técnico]] (entrega): Documento 18 con el glosario ES/EN completo y el doc 12 corregido
- 2026-10-12 · [[QA técnico]] → [[Narrador]] (devolucion): QA con fallos: limpieza 44 %, ✅ sin respaldo, marcas incoherentes y un ⏳ distinto para las cintas
- 2026-10-12 · [[Coordinador (Claude)]] → [[Narrador]] (entrega): Decisiones del autor sobre las 13 dudas de traducción y las 5 preguntas pendientes, y la corrección de la celda de Anselmo
- 2026-10-12 · [[Narrador]] → [[QA técnico]] (entrega): Documento 18 corregido: limpieza 65 %, coherencia 68 %, sin ❓
- 2026-10-12 · [[QA técnico]] → [[Coordinador (Claude)]] (devolucion): QA con un fallo: la celda de Anselmo seguía sin cuadrar con el registro (C11)
- 2026-10-12 · [[Coordinador (Claude)]] → [[QA técnico]] (entrega): Celda de Anselmo en el Acto I; coherencia 70 %
- 2026-10-12 · [[QA técnico]] → [[Fran (autor)]] (entrega): QA aprobado: limpieza 65 %, coherencia 70 %, sin ❓ en el documento 18
- 2026-10-12 · [[Fran (autor)]] → [[Coordinador (Claude)]] (entrega): Aprobado: «Terminé mi parte» sin ajustes

## Historial

- 2026-10-12 · backlog → doing · claude: Se empieza la biblia narrativa con el flujo de especialistas: primero la ideación de la estructura. (rama studio/F0-41-biblia-narrativa-estructura)
- 2026-10-12 · doing → review · claude: Documento 18 completo con reglas, nueve fichas de voz, glosario ES/EN y anexo; QA aprobado tras dos pasadas. (rama studio/F0-41-biblia-narrativa-estructura)
- 2026-10-12 · review → done · claude: El autor aprobó la biblia narrativa desde la bandeja de /equipo. (aprobación del autor con el botón «Terminé mi parte»)

## Comentarios

- 2026-10-12 · claude: Se ejecutaron las dos primeras etapas con subagentes reales: el ideador propuso tres estructuras y el analista verificó contra los documentos. Ambos informes están en esta conversación; las decisiones que quedan son del autor antes de que el narrador y el localizador escriban el documento 18.
- 2026-10-12 · autor: Decisiones: estructura por entidades con el documento 19 como fuente; Aetherita es el mineral y éter el fenómeno; Quiroga y Montenegro de usted y el resto de tú; se traduce casi todo al inglés.
- 2026-10-12 · autor: Decisiones del glosario: La Fosa es the Pit; la Faro es the Beacon; mal del éter es ether sickness y Comisión del Éter es Ether Commission; confirmo todas las demás traducciones propuestas. El personal figurante del Ministerio y la Comisión habla de usted; el protagonista tutea a doña Reme y al resto de los que tutean; hay variantes de género en los apelativos; la gente de la calle puede decir «el éter» por el mineral (nunca la interfaz, el narrador ni los titulares); y se corrige la celda de Anselmo del Acto IV.
- 2026-10-12 · claude: F0-41 recorrió el flujo con subagentes reales: el ideador propuso tres estructuras, el analista verificó cinco comprobaciones y fijó ocho criterios, el narrador escribió el documento 18, el localizador completó el glosario, y QA lo devolvió una vez (limpieza 44 %, ✅ sin respaldo, marcas incoherentes) y lo aprobó en la segunda pasada. Tus decisiones están aplicadas y la celda de Anselmo corregida: limpieza 49 % → 65 % y coherencia 68 % → 70 %.
- 2026-10-12 · autor: Terminé mi parte: revisé el entregable y está aprobado. Pásala a la siguiente etapa del flujo.

## Relaciones

- **Hito:** [[F0.11 Biblia narrativa]]
- **Documentos:** [[18 Biblia narrativa]]
- **Citada en:** [[18 §Estructura de esta biblia]], [[18 §1 Reglas globales]], [[18 §5 Objetos y minerales clave]], [[18 §6 Glosario ES - EN]], [[18 §Anexo Cronología y bifurcaciones]], [[18 §Pendiente]]

## Fuente

`studio/data/roadmap.json:461`
