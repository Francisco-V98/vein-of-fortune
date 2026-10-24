---
id: "adr-0008-decision"
tipo: "seccion"
title: "Decisión"
aliases: ["adr-0008-decision"]
documento: "[[ADR-0008 El QA es una etapa propia del flujo de trabajo]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[ADR-0008 §Contexto]]"
siguiente: "[[ADR-0008 §Alternativas consideradas]]"
arriba: "[[ADR-0008 El QA es una etapa propia del flujo de trabajo]]"
fuente: "studio/docs/adr/0008-qa-como-etapa-del-flujo.md:9"
generado: true
---

# Decisión

> El flujo pasa a backlog → sprint → doing → review → qa → done. review verifica código y arquitectura; qa verifica comportamiento con casos…

← [[ADR-0008 §Contexto]] · [[ADR-0008 El QA es una etapa propia del flujo de trabajo|↑ ADR-0008]] · [[ADR-0008 §Alternativas consideradas]] →

El flujo pasa a `backlog → sprint → doing → review → qa → done`. `review` verifica código y arquitectura; `qa` verifica comportamiento con casos de prueba, regresión, seguridad y rendimiento. Los casos viven en un catálogo con resultados, los errores se registran con severidad y cada versión tiene criterios de salida e informe.

## Fuente

`studio/docs/adr/0008-qa-como-etapa-del-flujo.md:9`
