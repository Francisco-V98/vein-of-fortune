---
id: "doc-16-el-qa-en-el-flujo"
tipo: "seccion"
title: "El QA en el flujo ✅"
aliases: ["doc-16-el-qa-en-el-flujo"]
documento: "[[16 Calidad y QA]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[16 §Principios]]"
siguiente: "[[16 §Tipos de verificación]]"
arriba: "[[16 Calidad y QA]]"
fuente: "studio/docs/16-calidad-y-qa.md:18"
generado: true
---

# El QA en el flujo ✅

← [[16 §Principios]] · [[16 Calidad y QA|↑ 16]] · [[16 §Tipos de verificación]] →

```
backlog → sprint → doing → review → qa → done
                              │      │
                              │      └─ falla: vuelve a doing (con el error anotado)
                              └─ cambios pedidos: vuelve a doing
```

| Estado | Qué se verifica | Quién | Entrada | Salida |
|---|---|---|---|---|
| `review` | **Código y arquitectura:** claridad, capas y módulos, pruebas escritas, seguridad, lista de revisión de [[15 Flujo de trabajo y calidad\|15]] | Claude (auto-revisión) y autor (PR) | PR abierto y CI en verde | Revisión aprobada |
| `qa` | **Comportamiento:** casos de prueba de la tarea, regresión, pruebas en el PC de pruebas, seguridad y rendimiento que apliquen | Claude (automáticas) y autor (aceptación) | Revisión aprobada | Casos aprobados y sin errores S1 o S2 abiertos |
| `done` | Fusionada en `main` con evidencia | Autor | QA aprobado | — |

- Una tarea **no pasa a `done` sin QA**, salvo las que no producen comportamiento (documentos, decisiones, estudio), que pasan de `review` a `done` y lo dicen en su nota.
- Si QA falla, la tarea vuelve a `doing` y el error se registra con su severidad.
- El resultado de QA queda en el historial de la tarea y en el catálogo de casos.

## Fuente

`studio/docs/16-calidad-y-qa.md:18`
