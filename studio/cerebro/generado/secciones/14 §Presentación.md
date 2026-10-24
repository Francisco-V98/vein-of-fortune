---
id: "doc-14-presentacion"
tipo: "seccion"
title: "Presentación 🟡"
aliases: ["doc-14-presentacion"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Cómo se comunican los módulos]]"
siguiente: "[[14 §Datos y persistencia]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:104"
generado: true
---

# Presentación 🟡

← [[14 §Cómo se comunican los módulos]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Datos y persistencia]] →

- Las escenas son **tontas**: muestran datos y emiten señales; no tienen reglas del juego.
- Cada pantalla tiene un **presentador** que traduce entre el caso de uso y la vista.
- "Las señales suben, las llamadas bajan": un nodo hijo emite señales; el padre le llama.
- Los textos siempre pasan por el sistema de traducción (ver [[10 Técnico y herramientas|10]]).
- La apariencia sale del **tema** de `ui_kit` y de los tokens de diseño derivados de la paleta ([[12 Dirección de arte|12]]), no de valores sueltos en cada escena.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:104`
