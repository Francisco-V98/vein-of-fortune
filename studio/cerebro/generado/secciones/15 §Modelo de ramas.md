---
id: "doc-15-modelo-de-ramas"
tipo: "seccion"
title: "Modelo de ramas 🟡"
aliases: ["doc-15-modelo-de-ramas"]
documento: "[[15 Flujo de trabajo y calidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[15 §Requisito del autor]]"
siguiente: "[[15 §Commits]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:7"
generado: true
---

# Modelo de ramas 🟡

> GitHub Flow con ramas de versión. main siempre está sano; todo el trabajo entra por ramas cortas y pull requests.

← [[15 §Requisito del autor]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §Commits]] →

**GitHub Flow con ramas de versión.** `main` siempre está sano; todo el trabajo entra por ramas cortas y *pull requests*.

| Rama | Para qué | Vida | Sale de | Entra en |
|---|---|---|---|---|
| `main` | Estado estable y publicable | permanente | — | — |
| `feat/ID-slug` | Funcionalidad nueva | corta | `main` | `main` |
| `fix/ID-slug` | Corrección de un error | corta | `main` | `main` |
| `refactor/ID-slug` | Reorganizar sin cambiar comportamiento | corta | `main` | `main` |
| `test/ID-slug` | Pruebas | corta | `main` | `main` |
| `docs/ID-slug` | Documentación | corta | `main` | `main` |
| `studio/ID-slug` | Roadmap, tareas, hub y arte de referencia | corta | `main` | `main` |
| `chore/ID-slug` | Herramientas, CI y mantenimiento | corta | `main` | `main` |
| `release/X.Y` | Estabilizar una versión antes de publicarla (solo correcciones) | semanas | `main` | `main` + etiqueta |
| `hotfix/X.Y.Z` | Corrección urgente de una versión publicada | horas | etiqueta | `main` + etiqueta |

- **Nombre:** `tipo/ID-descripcion-corta` en minúsculas con guiones, por ejemplo `feat/F2-04-modelo-de-precio`.
- **Una rama, una tarea** (o varias muy pequeñas del mismo hito). Si la rama crece, se divide.
- **Vida corta:** idealmente una sesión de trabajo; se actualiza con `main` antes de abrir el PR.
- **`main` está protegida:** nadie sube directamente; todo entra por PR con la integración continua en verde.
- **Por qué no Git Flow completo:** una rama `develop` añade fusiones y no aporta nada a un proyecto de una persona con integración continua. Si prefieres Git Flow, se cambia con un ADR.

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:7`
