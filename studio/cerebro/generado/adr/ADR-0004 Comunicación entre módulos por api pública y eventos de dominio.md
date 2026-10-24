---
id: "adr-0004"
tipo: "adr"
title: "ADR-0004 · Comunicación entre módulos por api pública y eventos de dominio"
aliases: ["adr-0004"]
estado: "Aceptada"
limpieza: 100
ok: 1
propuestas: 0
abiertos: 0
espera: 0
secciones: 4
fecha: "2026-10-11"
arriba: "[[MOC ADR]]"
fuente: "studio/docs/adr/0004-comunicacion-entre-modulos.md:1"
generado: true
---

# ADR-0004 · Comunicación entre módulos por api pública y eventos de dominio

> Limpieza 100 % · 0 abiertos · 4 secciones

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Secciones

1. [[ADR-0004 §Contexto]] — Los módulos deben colaborar sin conocerse por dentro ni crear ciclos.
2. [[ADR-0004 §Decisión]] — Dos canales: la api pública de cada módulo para preguntas síncronas, y eventos de dominio inmutables, definidos por quien los publica, para…
3. [[ADR-0004 §Alternativas consideradas]]
4. [[ADR-0004 §Consecuencias]] — Los módulos se prueban aislados y se reordenan sin romper a otros. Hay que cuidar que los eventos no se conviertan en un grafo oculto; el…

## Fuente

`studio/docs/adr/0004-comunicacion-entre-modulos.md:1`
