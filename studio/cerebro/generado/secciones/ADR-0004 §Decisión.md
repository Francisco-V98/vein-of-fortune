---
id: "adr-0004-decision"
tipo: "seccion"
title: "Decisión"
aliases: ["adr-0004-decision"]
documento: "[[ADR-0004 Comunicación entre módulos por api pública y eventos de dominio]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[ADR-0004 §Contexto]]"
siguiente: "[[ADR-0004 §Alternativas consideradas]]"
arriba: "[[ADR-0004 Comunicación entre módulos por api pública y eventos de dominio]]"
fuente: "studio/docs/adr/0004-comunicacion-entre-modulos.md:9"
generado: true
---

# Decisión

> Dos canales: la api pública de cada módulo para preguntas síncronas, y eventos de dominio inmutables, definidos por quien los publica, para…

← [[ADR-0004 §Contexto]] · [[ADR-0004 Comunicación entre módulos por api pública y eventos de dominio|↑ ADR-0004]] · [[ADR-0004 §Alternativas consideradas]] →

Dos canales: la **api pública** de cada módulo para preguntas síncronas, y **eventos de dominio** inmutables, definidos por quien los publica, para avisos. Un bus pequeño en `kernel` los entrega. Los eventos no se usan para dar órdenes.

## Fuente

`studio/docs/adr/0004-comunicacion-entre-modulos.md:9`
