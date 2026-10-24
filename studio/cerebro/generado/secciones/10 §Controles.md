---
id: "doc-10-controles"
tipo: "seccion"
title: "Controles ✅"
aliases: ["doc-10-controles"]
documento: "[[10 Técnico y herramientas]]"
limpieza: 0
abiertos: 2
espera: 1
aplazado_a: ["[[F1-06 Resolución base, escalado entero y modos de pantalla]]"]
estado: "con-abiertos"
anterior: "[[10 §Arquitectura]]"
siguiente: "[[10 §Arte y sonido]]"
arriba: "[[10 Técnico y herramientas]]"
fuente: "studio/docs/10-tecnico-y-herramientas.md:56"
generado: true
---

# Controles ✅

> Decisión del autor (2026-10-15): ratón y teclado son los controles principales (hover, tooltips, atajos y ventanas de información densas) y…

← [[10 §Arquitectura]] · [[10 Técnico y herramientas|↑ 10]] · [[10 §Arte y sonido]] →

Decisión del autor (2026-10-15): **ratón y teclado son los controles principales** (hover, tooltips, atajos y ventanas de información densas) y el **mando está completo** (necesario para la Steam Deck *Verified*). La interfaz táctil queda como un **adaptador futuro** para el móvil; **no se construye HUD táctil ahora**.

| Aspecto | Regla |
|---|---|
| Capa de acciones | El juego se programa contra **acciones** (aceptar, cancelar, mover, usar, menú) y no contra botones concretos |
| Adaptadores | Ratón y teclado, y mando; el táctil se añadirá en la fase móvil sin tocar módulos ([[14 Arquitectura y modularidad\|14]]) |
| Detección | Detecta el último dispositivo usado (ratón y teclado, o mando) y cambia solo |
| Hover y tooltips | Información secundaria al pasar el cursor y atajos de teclado; **nada esencial depende solo del hover**, porque con mando no existe |
| Navegación | Todos los menús navegables por **foco** (teclado y mando) |
| Íconos | Los glifos de botones cambian según el dispositivo y el tipo de mando |
| Vibración | Vibración del mando cuando exista |
| Reasignación | Mapeo configurable (a futuro) |
| Resolución y ventana | Resolución base, escala entera con bandas, ventana y pantalla completa: ⏳ [[F1-06 Resolución base, escalado entero y modos de pantalla\|F1-06]] |

🟡 Minijuegos: Picado y Perforación se juegan con un botón (ratón, teclado o mando); Cincelado (trazar) y arrastrar mercancía usan el puntero con ratón y un cursor con el stick con mando. Hay que diseñarlos con ambas variantes desde el inicio. Las variantes táctiles (trazar con el dedo) pasan a la fase móvil.

🟡 Probar con un mando real en Windows y en la Steam Deck antes de dar por buenos los controles ([[F1-15 Probar un mando con la escena de prueba en PC y en la Steam|F1-15]]).

## Fuente

`studio/docs/10-tecnico-y-herramientas.md:56`
