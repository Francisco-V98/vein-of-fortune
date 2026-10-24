---
id: "adr-0009-contexto"
tipo: "seccion"
title: "Contexto"
aliases: ["adr-0009-contexto"]
documento: "[[ADR-0009 PC primero (Steam) y móvil después]]"
abiertos: 0
espera: 0
estado: "limpia"
siguiente: "[[ADR-0009 §Decisión]]"
arriba: "[[ADR-0009 PC primero (Steam) y móvil después]]"
fuente: "studio/docs/adr/0009-pc-primero-movil-despues.md:5"
generado: true
---

# Contexto

> Hasta ahora el plan era Android primero: el juego se diseñaba para pantalla táctil, con resolución y zona segura pensadas para teléfonos…

[[ADR-0009 PC primero (Steam) y móvil después|↑ ADR-0009]] · [[ADR-0009 §Decisión]] →

Hasta ahora el plan era **Android primero**: el juego se diseñaba para pantalla táctil, con resolución y zona segura pensadas para teléfonos, pruebas en el Android del autor y Play Vitals como telemetría de tienda ([[ADR-0001 Godot 4.x con GDScript como motor|ADR-0001]], [[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro|ADR-0007]]). El autor cambió la prioridad el 2026-10-15: el juego se lanza primero en PC y Steam es la tienda objetivo. Observación del análisis: el juego maneja mucha información a la vez (mercado, noticias, contratos, ventanas densas) y eso se aprovecha mejor con hover, tooltips y atajos.

## Fuente

`studio/docs/adr/0009-pc-primero-movil-despues.md:5`
