---
id: "sim-B1"
tipo: "regla-sim"
title: "Ritmo por acto de la campaña completa"
aliases: ["sim-B1"]
grupo: "B · Ritmo, progresión y estatus"
estado: "pasa"
origen: "doc"
valor: 1.0
unidad: ""
documentos: ["[[28 §2 Ritmo objetivo y patrimonio]]", "[[04 Progresión y meta]]", "[[17 Mapa de historia]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:104"
generado: true
---

# Ritmo por acto de la campaña completa

> B · Ritmo, progresión y estatus · pasa · ±20 % del objetivo · medio = 60–80 % del optimizador · lento < medio < rápido · rápido/len

**Grupo:** B · Ritmo, progresión y estatus · **Origen del umbral:** documento aprobado

## Qué mide

ingreso neto por hora de cada acto frente al objetivo (la media del acto); medio frente al optimizador; orden de perfiles

## Umbral

±20 % del objetivo · medio = 60–80 % del optimizador · lento < medio < rápido · rápido/lento ≤ 4

## Resultado

Estado: **pasa**. orden lento < medio < rápido en II, III y IV (1 = sí): **1 ** (IC95 –, n = –).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Lento\|lento]] | 36.7323 | – | – |
| [[Perfil Rápido\|rapido]] | 43.8836 | – | – |
| [[Perfil Optimizador\|optimizador]] | 75.3903 | – | – |
| [[Perfil Medio\|medio]] | 4.5638 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| desviación del ritmo del Acto I (medio) | 6.0819 % | [5.6855, 6.4783] | … a 20 | pasa |
| desviación del ritmo del Acto II (medio) | 3.5101 % | [2.9633, 4.0569] | … a 20 | pasa |
| desviación del ritmo del Acto III (medio) | 1.3464 % | [0.5954, 2.0974] | … a 20 | pasa |
| desviación del ritmo del Acto IV (medio) | 1.5453 % | [0.7677, 2.323] | … a 20 | pasa |
| ritmo del medio frente al optimizador | 67.4406 % | [66.2696, 68.6117] | 60 a 80 | pasa |
| orden lento < medio < rápido en II, III y IV (1 = sí) | 1  | [1, 1] | 1 a 1 | pasa |
| razón máxima rápido / lento | 2.1596 x | [2.1596, 2.1596] | … a 4 | pasa |

### Datos adicionales

- **objetivo:**
  - **I:** 1100
  - **II:** 7500
  - **III:** 33000
  - **IV:** 110000

## Criterio

- **desv_max:** 20
- **opt_min:** 60
- **opt_max:** 80
- **rapido_lento_max:** 4

## Requisitos que protege

- Ingreso neto por hora del Acto I (650 · 1 100 · 2 200) ([[28 §2 Ritmo objetivo y patrimonio]])
- Ritmo por acto 1 100 · 7 500 · 27 000 · 125 000 (la media del acto) ([[28 §2 Ritmo objetivo y patrimonio]])

## Mutaciones de prueba

- Objetivos del medio rebajados al ritmo medido
  - `economy.pace.net_income_per_hour.IV.target` = 75000
  - `economy.pace.net_income_per_hour.III.target` = 24000

## Relaciones

- **Documentos:** [[28 §2 Ritmo objetivo y patrimonio]], [[04 Progresión y meta]], [[17 Mapa de historia]]
- **Bloques de economía:** [[Ritmo objetivo]], [[Guion económico del Acto I]]
- **Perfiles:** [[Perfil Lento]], [[Perfil Rápido]], [[Perfil Optimizador]], [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:104`
