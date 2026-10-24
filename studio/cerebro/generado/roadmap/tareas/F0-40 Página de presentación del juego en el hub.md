---
id: "F0-40"
tipo: "tarea"
title: "F0-40 Página de presentación del juego en el hub"
aliases: ["F0-40"]
fase: "[[F0 Diseño]]"
hito: "[[F0.10 Presentación del juego]]"
prio: "P1"
est: 6
status: "done"
version: "MVP"
docs: []
arriba: "[[F0.10 Presentación del juego]]"
tags: ["estado/hecho", "prio/P1", "fase/F0", "version/MVP"]
fuente: "studio/data/roadmap.json:446"
generado: true
---

# F0-40 Página de presentación del juego en el hub

> Página «El juego» con 28 láminas que resumen la idea, la jugabilidad, el mundo, la historia, el arte, cómo se construye y el plan, para…

Página «El juego» con 28 láminas que resumen la idea, la jugabilidad, el mundo, la historia, el arte, cómo se construye y el plan, para tener todo en un solo lugar. Cada lámina enlaza a su documento fuente.

## Hecha cuando

La página se abre desde el hub, se navega con teclado, funciona en móvil, se puede imprimir y todas las fuentes e imágenes existen.

## Historial

- 2026-10-11 · backlog → doing · claude: El autor pide una página con todo el contexto, la historia y el juego, como una presentación, para tenerlo todo en un lugar. (rama studio/F0-40-pagina-de-presentacion)
- 2026-10-11 · doing → review · claude: 28 láminas basadas en los documentos, con navegación por teclado, pantalla completa, impresión y cálculo en vivo de fases y estado. (rama studio/F0-40-pagina-de-presentacion)
- 2026-10-11 · review → doing · claude: El autor pide estructurarlo mejor porque quedó muy texto plano. Se rediseña con 40 láminas, 6 secciones y 26 formatos visuales. (rama studio/F0-40-pagina-de-presentacion)
- 2026-10-11 · doing → review · claude: Rediseño listo: agenda por secciones, tarjetas con iconos, cifras grandes, gráfico de mercado, mapa con marcadores, recortes de zonas, minerales y personajes, plan y estado calculados en vivo. (rama studio/F0-40-pagina-de-presentacion)
- 2026-10-11 · review → done · claude: El autor revisó y aprobó el PR y se fusionó en main. (PR #5)

## Comentarios

- 2026-10-11 · autor: ¿Puedes agregar una página con todo el contexto, historia y todo sobre el juego, como una presentación, para tenerlo todo en un lugar?
- 2026-10-11 · claude: Es un resumen curado: si un documento cambia, hay que revisar la lámina que lo cita (cada una enlaza a su fuente). Las láminas de plan y estado se calculan en vivo del roadmap. El modo de pantalla completa no pude probarlo en el panel de vista previa.
- 2026-10-11 · autor: Estructúralo un poco mejor porque quedó muy texto plano, quiero mejorarlo mucho más.
- 2026-10-11 · claude: Rehecho: ahora son 40 láminas con 6 secciones (barra de secciones arriba), menos de 45 palabras por lámina de media y un formato visual por tema. Los recortes de zonas, minerales y personajes salen de las imágenes de referencia, así que su encuadre es aproximado. Pantalla completa y PDF siguen sin probarse en el panel de vista previa.

## Evidencias

- image: Portada
- image: Lámina de minijuegos
- image: Lámina del plan (calculada en vivo)
- image: Mosaico de dirección de arte
- image: Mapa de Valdoria con marcadores
- image: Lámina de minerales (recortes de la hoja de sprites)
- file: Contenido de las láminas
- note: Verificación

## Relaciones

- **Hito:** [[F0.10 Presentación del juego]]

## Fuente

`studio/data/roadmap.json:446`
