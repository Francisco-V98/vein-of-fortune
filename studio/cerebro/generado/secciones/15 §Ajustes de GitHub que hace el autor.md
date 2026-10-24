---
id: "doc-15-ajustes-de-github-que-hace-el-autor"
tipo: "seccion"
title: "Ajustes de GitHub que hace el autor 🟡"
aliases: ["doc-15-ajustes-de-github-que-hace-el-autor"]
documento: "[[15 Flujo de trabajo y calidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[15 §Coste de la IA]]"
siguiente: "[[15 §QA en el flujo]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:230"
generado: true
---

# Ajustes de GitHub que hace el autor 🟡

> En Settings → Branches → Branch protection rule para main:

← [[15 §Coste de la IA]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §QA en el flujo]] →

En *Settings → Branches → Branch protection rule* para `main`:

- Requerir *pull request* antes de fusionar.
- Requerir que pasen las comprobaciones de la integración continua.
- Requerir historial lineal (squash).
- No permitir subidas forzadas ni borrar la rama.
- En *General*: borrar ramas automáticamente al fusionar.

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:230`
