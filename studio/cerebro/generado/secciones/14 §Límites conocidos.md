---
id: "doc-14-limites-conocidos"
tipo: "seccion"
title: "Límites conocidos ❓"
aliases: ["doc-14-limites-conocidos"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Añadir un módulo]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:198"
generado: true
---

# Límites conocidos ❓

← [[14 §Añadir un módulo]] · [[14 Arquitectura y modularidad|↑ 14]]

- **GDScript no tiene interfaces.** Los puertos se implementan como clases base abstractas con `assert`/`push_error` y se prueban con dobles. Hay que validar el patrón en Godot real.
- El verificador es **estático y aproximado**: detecta rutas `res://` y nombres de clase; no ve referencias dinámicas (`load(variable)`). Por eso se prohíben las rutas construidas en tiempo de ejecución dentro de `src/`.
- Todo esto se valida con código real a partir de la Fase 1.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:198`
