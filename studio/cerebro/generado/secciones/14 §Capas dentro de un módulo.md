---
id: "doc-14-capas-dentro-de-un-modulo"
tipo: "seccion"
title: "Capas dentro de un módulo 🟡"
aliases: ["doc-14-capas-dentro-de-un-modulo"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Estructura de `game - `]]"
siguiente: "[[14 §Módulos previstos]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:47"
generado: true
---

# Capas dentro de un módulo 🟡

← [[14 §Estructura de `game - `]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Módulos previstos]] →

```
presentation ─┐
              ├─► application ─► domain
infrastructure┘                  ▲
   (implementa los puertos que declara application)
```

| Capa | Puede usar | No puede usar |
|---|---|---|
| `domain` | solo `kernel` y su propio dominio | nodos, UI, archivos, entrada, otros módulos, plataforma |
| `application` | `domain`, `kernel`, puertos de `platform`, `data` | `presentation`, `infrastructure` |
| `infrastructure` | `application`, `domain`, `kernel`, puertos, `data` | `presentation` |
| `presentation` | `application`, `domain`, `kernel`, `ui_kit`, puertos | `infrastructure` |
| `api` | `application`, `domain` | `presentation`, `infrastructure` |

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:47`
