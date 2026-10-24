---
id: "doc-14-datos-y-persistencia"
tipo: "seccion"
title: "Datos y persistencia 🟡"
aliases: ["doc-14-datos-y-persistencia"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Presentación]]"
siguiente: "[[14 §Plataforma]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:112"
generado: true
---

# Datos y persistencia 🟡

← [[14 §Presentación]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Plataforma]] →

- El contenido se define en archivos de datos con **esquema y validación**; cargar un dato inválido falla de forma clara al arrancar.
- Los identificadores de contenido son **cadenas estables** (`mineral.hierro`), nunca posiciones.
- El guardado usa **DTO versionados** con migraciones, un **punto de control al iniciar cada acción** y hasta **5 partidas guardables** que el jugador elige ([[01 Core loop y ciclo del día|01]]). Cada módulo ofrece `snapshot()` y `restore()`; el módulo `save` los reúne a través de la raíz de composición, sin conocerlos.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:112`
