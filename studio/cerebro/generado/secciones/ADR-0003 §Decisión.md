---
id: "adr-0003-decision"
tipo: "seccion"
title: "Decisión"
aliases: ["adr-0003-decision"]
documento: "[[ADR-0003 Arquitectura modular por cortes verticales y capas]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[ADR-0003 §Contexto]]"
siguiente: "[[ADR-0003 §Alternativas consideradas]]"
arriba: "[[ADR-0003 Arquitectura modular por cortes verticales y capas]]"
fuente: "studio/docs/adr/0003-arquitectura-modular.md:9"
generado: true
---

# Decisión

> Cada funcionalidad es un módulo con capas domain, application, infrastructure, presentation y api. Las dependencias apuntan hacia el…

← [[ADR-0003 §Contexto]] · [[ADR-0003 Arquitectura modular por cortes verticales y capas|↑ ADR-0003]] · [[ADR-0003 §Alternativas consideradas]] →

Cada funcionalidad es un **módulo** con capas `domain`, `application`, `infrastructure`, `presentation` y `api`. Las dependencias apuntan hacia el dominio. Un módulo solo usa la `api` de otro y debe declararlo en `architecture.json`. Entrada, almacenamiento, audio, idioma y reloj son **puertos** con adaptadores. Una **raíz de composición** (`app`) conecta todo. El cumplimiento se verifica automáticamente.

## Fuente

`studio/docs/adr/0003-arquitectura-modular.md:9`
