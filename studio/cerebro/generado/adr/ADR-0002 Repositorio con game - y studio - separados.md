---
id: "adr-0002"
tipo: "adr"
title: "ADR-0002 · Repositorio con game/ y studio/ separados"
aliases: ["adr-0002"]
estado: "Aceptada"
limpieza: 100
ok: 1
propuestas: 0
abiertos: 0
espera: 0
secciones: 4
fecha: "2026-10-11"
arriba: "[[MOC ADR]]"
fuente: "studio/docs/adr/0002-estructura-game-y-studio.md:1"
generado: true
---

# ADR-0002 · Repositorio con game/ y studio/ separados

> Limpieza 100 % · 0 abiertos · 4 secciones

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Secciones

1. [[ADR-0002 §Contexto]] — El juego y su gestión (documentos, roadmap, tareas, arte de referencia, hub) deben poder separarse, ignorarse o extraerse sin romper nada.
2. [[ADR-0002 §Decisión]] — Un solo repositorio con dos mundos independientes: game/ compila sin studio/ y studio/ no importa nada de game/. tools/ contiene…
3. [[ADR-0002 §Alternativas consideradas]]
4. [[ADR-0002 §Consecuencias]] — studio/ se puede ignorar (git sparse-checkout) o extraer con su historial (git subtree split); ambos probados en local.

## Fuente

`studio/docs/adr/0002-estructura-game-y-studio.md:1`
