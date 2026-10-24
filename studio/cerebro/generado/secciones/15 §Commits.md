---
id: "doc-15-commits"
tipo: "seccion"
title: "Commits ✅ / 🟡"
aliases: ["doc-15-commits"]
documento: "[[15 Flujo de trabajo y calidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[15 §Modelo de ramas]]"
siguiente: "[[15 §Flujo de una tarea]]"
arriba: "[[15 Flujo de trabajo y calidad]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:30"
generado: true
---

# Commits ✅ / 🟡

> Convención Conventional Commits en español, con el ID de la tarea:

← [[15 §Modelo de ramas]] · [[15 Flujo de trabajo y calidad|↑ 15]] · [[15 §Flujo de una tarea]] →

Convención **Conventional Commits** en español, con el ID de la tarea:

```
tipo(ámbito): ID descripción breve en imperativo

Cuerpo opcional: qué y por qué (no cómo).

Co-Authored-By: …
```

| Tipo | Uso |
|---|---|
| `feat` | Funcionalidad nueva |
| `fix` | Corrección de un error |
| `refactor` | Cambio interno sin cambiar el comportamiento |
| `perf` | Mejora de rendimiento |
| `test` | Pruebas |
| `docs` | Documentación |
| `studio` | Roadmap, tareas, hub y arte de referencia |
| `chore`, `ci`, `build`, `style`, `revert` | Mantenimiento, integración continua, empaquetado, formato, reversión |

- **Ámbito:** el módulo (`market`, `shop`…) o el área (`ci`, `roadmap`, `hub`).
- Asunto de **hasta 100 caracteres**, sin punto final. Un commit = un cambio con sentido, que compila y pasa las pruebas.
- Se verifica con `tools/ci/check_commits.py`. Un commit sin ID de tarea da aviso.

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:30`
