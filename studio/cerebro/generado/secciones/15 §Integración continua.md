---
id: "doc-15-integracion-continua"
tipo: "seccion"
title: "Integración continua ✅"
aliases: ["doc-15-integracion-continua"]
documento: "[[15 Flujo de trabajo y calidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[15 §Pull requests]]"
siguiente: "[[15 §Definición de listo y de terminado]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:99"
generado: true
---

# Integración continua ✅

> Se ejecuta en cada PR y en cada cambio de main (.github/workflows/ci.yml):

← [[15 §Pull requests]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §Definición de listo y de terminado]] →

Se ejecuta en cada PR y en cada cambio de `main` (`.github/workflows/ci.yml`):

| Trabajo | Qué hace |
|---|---|
| `studio` | Valida roadmap, tareas, catálogo de QA y registro de errores (`build.py --strict`); el archivo generado `hub/data.js` no se versiona |
| `tools` | Pruebas de las herramientas de verificación |
| `commits` | Convención de mensajes de commit del PR |
| `architecture` | Verificador de arquitectura sobre `game/` |
| `game` | Formato, lint y pruebas de GDScript (se activa cuando exista `project.godot`) |

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:99`
