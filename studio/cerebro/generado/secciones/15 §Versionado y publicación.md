---
id: "doc-15-versionado-y-publicacion"
tipo: "seccion"
title: "Versionado y publicación 🟡"
aliases: ["doc-15-versionado-y-publicacion"]
documento: "[[15 Flujo de trabajo y calidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[15 §Pruebas]]"
siguiente: "[[15 §Decisiones de arquitectura (ADR)]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:191"
generado: true
---

# Versionado y publicación 🟡

← [[15 §Pruebas]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §Decisiones de arquitectura (ADR)]] →

- **SemVer** `MAJOR.MINOR.PATCH` para el juego, con etiquetas `vX.Y.Z` en `main`.
- **`CHANGELOG.md`** en formato *Keep a Changelog*, derivado de los commits.
- Steam: la versión del juego (`vX.Y.Z`) se registra en cada build subida. Fase móvil (después de la 1.0): en Android, `versionCode` que solo crece y `versionName` igual a la versión del juego ([[10 Técnico y herramientas|10]]).
- Se corta `release/X.Y` cuando una versión está completa; allí solo entran correcciones.

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:191`
