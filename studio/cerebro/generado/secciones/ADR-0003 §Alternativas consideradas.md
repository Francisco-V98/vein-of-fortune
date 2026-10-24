---
id: "adr-0003-alternativas-consideradas"
tipo: "seccion"
title: "Alternativas consideradas"
aliases: ["adr-0003-alternativas-consideradas"]
documento: "[[ADR-0003 Arquitectura modular por cortes verticales y capas]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[ADR-0003 §Decisión]]"
siguiente: "[[ADR-0003 §Consecuencias]]"
arriba: "[[ADR-0003 Arquitectura modular por cortes verticales y capas]]"
fuente: "studio/docs/adr/0003-arquitectura-modular.md:13"
generado: true
---

# Alternativas consideradas

← [[ADR-0003 §Decisión]] · [[ADR-0003 Arquitectura modular por cortes verticales y capas|↑ ADR-0003]] · [[ADR-0003 §Consecuencias]] →

- **Estructura por tipo técnico** (todas las escenas juntas, todos los scripts juntos): simple al inicio, pero acopla todo y no escala.
- **ECS puro:** potente para simulaciones masivas, innecesario aquí y poco natural en Godot.
- **Nodos y señales sin capas:** rápido para empezar, pero mezcla reglas con interfaz y dificulta probar.

## Fuente

`studio/docs/adr/0003-arquitectura-modular.md:13`
