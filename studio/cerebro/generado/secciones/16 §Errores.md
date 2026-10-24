---
id: "doc-16-errores"
tipo: "seccion"
title: "Errores ✅"
aliases: ["doc-16-errores"]
documento: "[[16 Calidad y QA]]"
limpieza: 0
abiertos: 1
espera: 0
estado: "con-abiertos"
anterior: "[[16 §Casos de prueba]]"
siguiente: "[[16 §Criterios de salida de una versión]]"
arriba: "[[16 Calidad y QA]]"
fuente: "studio/docs/16-calidad-y-qa.md:85"
generado: true
---

# Errores ✅

> Cada error es un archivo en studio/data/qa/bugs/BUG-NNNN.json con título, severidad, estado, versión donde apareció, pasos para…

← [[16 §Casos de prueba]] · [[16 Calidad y QA|↑ 16]] · [[16 §Criterios de salida de una versión]] →

Cada error es un archivo en `studio/data/qa/bugs/BUG-NNNN.json` con título, severidad, estado, versión donde apareció, pasos para reproducirlo, resultado esperado y real, y evidencias.

### Severidad 🟡

| Nivel | Significado | Ejemplo | Regla |
|---|---|---|---|
| **S1 · Crítico** | Pérdida de datos, cierre del juego, bloqueo total | Se pierde la partida al guardar | Detiene todo; se corrige primero |
| **S2 · Grave** | Función principal rota sin atajo | No se puede vender | Se corrige antes de la siguiente versión |
| **S3 · Moderado** | Falla con alternativa o efecto limitado | Un texto se corta | Se planifica |
| **S4 · Menor** | Cosmético o muy poco probable | Un píxel desalineado | Cuando haya tiempo |

### Ciclo de vida

`abierto → triaje → en corrección → corregido → verificado → cerrado`, o `no se corrige` con su motivo. Todo error corregido incorpora una **prueba de regresión**.

## Fuente

`studio/docs/16-calidad-y-qa.md:85`
