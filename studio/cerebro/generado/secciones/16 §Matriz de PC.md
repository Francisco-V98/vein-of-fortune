---
id: "doc-16-matriz-de-pc"
tipo: "seccion"
title: "Matriz de PC 🟡"
aliases: ["doc-16-matriz-de-pc"]
documento: "[[16 Calidad y QA]]"
limpieza: 0
abiertos: 1
espera: 1
aplazado_a: ["[[F1-06 Resolución base, escalado entero y modos de pantalla]]"]
estado: "con-abiertos"
anterior: "[[16 §Plan de QA por fase]]"
siguiente: "[[16 §Presupuestos de rendimiento (a medir en PC F1-44)]]"
arriba: "[[16 Calidad y QA]]"
fuente: "studio/docs/16-calidad-y-qa.md:121"
generado: true
---

# Matriz de PC 🟡

> Decisión del autor (2026-10-15): se prueba en un PC Windows real y en la Steam Deck si la hay (ADR-0009). Es un requisito de F1.

← [[16 §Plan de QA por fase]] · [[16 Calidad y QA|↑ 16]] · [[16 §Presupuestos de rendimiento (a medir en PC F1-44)]] →

Decisión del autor (2026-10-15): se prueba en un **PC Windows real** y en la Steam Deck si la hay ([[ADR-0009 PC primero (Steam) y móvil después|ADR-0009]]). Es un requisito de F1.

| Dimensión | Cobertura mínima |
|---|---|
| Gama del equipo | Gama baja y **GPU integrada**; un equipo medio o alto como referencia |
| Sistema operativo | **Windows** y **Linux** |
| Steam Deck | 1280×800 con mando, sin HUD táctil y texto legible (objetivo *Verified*) |
| Resolución | 1080p, 1440p y 4K |
| Proporción de pantalla | 16:9 y **ultrapanorámico**; cómo se escala lo decide ⏳ [[F1-06 Resolución base, escalado entero y modos de pantalla\|F1-06]] |
| Entrada | Ratón y teclado, y mando (incluido el de la Deck) |
| Equipo real | Un **PC Windows real** de pruebas |
| macOS | Después de la 1.0 |

❓ Falta definir los equipos reales: el autor trabaja en Mac, así que el PC Windows (que tiene o consigue) y la Steam Deck, si la hay, son la base; el resto de la matriz se completa con máquinas virtuales (Linux) y equipos prestados si hace falta.

## Fuente

`studio/docs/16-calidad-y-qa.md:121`
