---
id: "doc-14-raiz-de-composicion"
tipo: "seccion"
title: "Raíz de composición 🟡"
aliases: ["doc-14-raiz-de-composicion"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Plataforma]]"
siguiente: "[[14 §Clean code en GDScript]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:139"
generado: true
---

# Raíz de composición 🟡

> app/ es el único lugar que conoce las implementaciones concretas: crea los módulos, conecta puertos con adaptadores y arranca el juego. Los…

← [[14 §Plataforma]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Clean code en GDScript]] →

`app/` es el único lugar que conoce las implementaciones concretas: crea los módulos, conecta puertos con adaptadores y arranca el juego. Los autoloads se limitan a uno (`App`); el resto se entrega por parámetro.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:139`
