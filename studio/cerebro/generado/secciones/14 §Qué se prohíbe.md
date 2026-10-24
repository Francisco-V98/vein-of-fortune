---
id: "doc-14-que-se-prohibe"
tipo: "seccion"
title: "Qué se prohíbe 🟡"
aliases: ["doc-14-que-se-prohibe"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Clean code en GDScript]]"
siguiente: "[[14 §Verificación automática]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:159"
generado: true
---

# Qué se prohíbe 🟡

← [[14 §Clean code en GDScript]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Verificación automática]] →

- Singletons y estado global (salvo `App`).
- Que un módulo use las carpetas internas de otro.
- Lógica de juego en las escenas.
- Que el dominio use `Node`, `Input`, archivos o el árbol de escenas.
- Números y textos del juego escritos dentro del código.
- Clases "dios" y utilidades genéricas sin dueño.
- Dependencias circulares.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:159`
