---
id: "doc-14-clean-code-en-gdscript"
tipo: "seccion"
title: "Clean code en GDScript ✅"
aliases: ["doc-14-clean-code-en-gdscript"]
documento: "[[14 Arquitectura y modularidad]]"
limpieza: 0
abiertos: 1
espera: 0
estado: "con-abiertos"
anterior: "[[14 §Raíz de composición]]"
siguiente: "[[14 §Qué se prohíbe]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:143"
generado: true
---

# Clean code en GDScript ✅

> Requisito del autor; el detalle de umbrales es .

← [[14 §Raíz de composición]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Qué se prohíbe]] →

Requisito del autor; el detalle de umbrales es 🟡.

- **Tipado estático en todo:** variables, parámetros y retornos.
- **Nombres que explican:** funciones como verbos, booleanos como preguntas (`es_valido`), sin abreviaturas.
- **Funciones cortas** (guía: hasta ~20 líneas) y de **un solo nivel de abstracción**.
- **Un archivo, una clase.** Guía: hasta 400 líneas (el verificador avisa).
- **Sin números mágicos:** constantes con nombre o datos.
- **Retornos tempranos** en lugar de anidar condiciones.
- **Documentar el contrato** de lo público con comentarios `##`; el resto se explica con buenos nombres.
- **Sin código comentado** y **sin `TODO` sin tarea** (`TODO(F3-12): …`).
- **Errores explícitos:** el dominio devuelve un `Result`; las excepciones no se usan para el flujo normal.
- **Sin rutas de nodos escritas a mano**: referencias exportadas o nombres únicos.
- **Señales** con nombre en pasado y datos tipados.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:143`
