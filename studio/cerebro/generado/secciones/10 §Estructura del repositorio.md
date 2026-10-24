---
id: "doc-10-estructura-del-repositorio"
tipo: "seccion"
title: "Estructura del repositorio ✅"
aliases: ["doc-10-estructura-del-repositorio"]
documento: "[[10 Técnico y herramientas]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[10 §Localización (español e inglés desde el inicio)]]"
siguiente: "[[10 §Exportación y Steam]]"
arriba: "[[10 Técnico y herramientas]]"
fuente: "studio/docs/10-tecnico-y-herramientas.md:118"
generado: true
---

# Estructura del repositorio ✅

> Un solo repositorio con dos mundos separados:

← [[10 §Localización (español e inglés desde el inicio)]] · [[10 Técnico y herramientas|↑ 10]] · [[10 §Exportación y Steam]] →

Un solo repositorio con dos mundos separados:

```
<nombre>/
├── game/       el juego (proyecto Godot)
├── studio/     documentos, roadmap, tareas, evidencias, hub y métricas
└── README.md
```

- `game/` **compila sin** `studio/`, y `studio/` **no importa** nada de `game/` (solo lee archivos de diagnóstico exportados).
- `studio/` se puede **ignorar** con una línea en `.gitignore` o **extraer con su historial** a otro repositorio con `git subtree split`.
- Repositorio **privado** en GitHub.

## Fuente

`studio/docs/10-tecnico-y-herramientas.md:118`
