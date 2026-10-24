---
id: "doc-14-verificacion-automatica"
tipo: "seccion"
title: "Verificación automática ✅"
aliases: ["doc-14-verificacion-automatica"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Qué se prohíbe]]"
siguiente: "[[14 §Añadir un módulo]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:169"
generado: true
---

# Verificación automática ✅

> El verificador de arquitectura ya tiene 22 pruebas automáticas sobre estructuras de ejemplo. Falta ejecutarlo contra código real de…

← [[14 §Qué se prohíbe]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Añadir un módulo]] →

| Regla | Qué comprueba | Herramienta |
|---|---|---|
| A1 | Capas dentro de un módulo | `tools/arch/check_architecture.py` |
| A2 | Un módulo solo usa la `api` de otro y si lo declara | ídem |
| A3 | El dominio no depende de otros módulos ni de la plataforma | ídem |
| A4 | El dominio no usa clases del motor, entrada ni archivos | ídem |
| A5 | `kernel` no depende de nada fuera de `kernel` | ídem |
| A6 | Solo `app` conoce `platform/adapters` | ídem |
| A7 | El grafo de módulos no tiene ciclos | ídem |
| A8 | Los módulos del código y los declarados coinciden | ídem |
| A9 | Solo los autoloads permitidos | ídem |
| Estilo | Formato y lint de GDScript | `gdformat` y `gdlint` (se instalan en [[F1-32 gdlint y gdformat configurados y en integración continua\|F1-32]]) |
| Pruebas | Dominio y aplicación, sin interfaz | GUT con Godot sin interfaz ([[F1-33 Pruebas del dominio con Godot sin interfaz en integración\|F1-33]]) |
| Convención | Mensajes de commit | `tools/ci/check_commits.py` |
| Datos | Estado de tareas coherente con su historial | `studio/hub/build.py --strict` |

El verificador de arquitectura ya tiene **22 pruebas automáticas** sobre estructuras de ejemplo. Falta ejecutarlo contra código real de GDScript, que empieza en F1.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:169`
