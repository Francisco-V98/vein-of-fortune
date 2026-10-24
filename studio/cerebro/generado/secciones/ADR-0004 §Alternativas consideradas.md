---
id: "adr-0004-alternativas-consideradas"
tipo: "seccion"
title: "Alternativas consideradas"
aliases: ["adr-0004-alternativas-consideradas"]
documento: "[[ADR-0004 Comunicación entre módulos por api pública y eventos de dominio]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[ADR-0004 §Decisión]]"
siguiente: "[[ADR-0004 §Consecuencias]]"
arriba: "[[ADR-0004 Comunicación entre módulos por api pública y eventos de dominio]]"
fuente: "studio/docs/adr/0004-comunicacion-entre-modulos.md:13"
generado: true
---

# Alternativas consideradas

← [[ADR-0004 §Decisión]] · [[ADR-0004 Comunicación entre módulos por api pública y eventos de dominio|↑ ADR-0004]] · [[ADR-0004 §Consecuencias]] →

- **Señales de Godot entre nodos de módulos distintos:** acoplan la jerarquía de escenas.
- **Autoloads globales como servicios:** cómodos, pero crean dependencias ocultas y dificultan las pruebas.

## Fuente

`studio/docs/adr/0004-comunicacion-entre-modulos.md:13`
