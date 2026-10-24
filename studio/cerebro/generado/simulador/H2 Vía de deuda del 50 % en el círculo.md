---
id: "sim-H2"
tipo: "regla-sim"
title: "Vía de deuda del 50 % en el círculo"
aliases: ["sim-H2"]
grupo: "H · Deuda, mora y rescate"
estado: "pasa"
origen: "doc"
valor: 0.1785
unidad: "h"
documentos: ["[[28 §7 Deuda del Acto I y sus nombres]]", "[[24 Umbrales de acto]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:607"
generado: true
---

# Vía de deuda del 50 % en el círculo

> H · Deuda, mora y rescate · pasa · falta ≤ 0,3 h

**Grupo:** H · Deuda, mora y rescate · **Origen del umbral:** documento aprobado

## Qué mide

horas de ingreso del Acto III que faltan para el 50 % sin pagos extra

## Umbral

falta ≤ 0,3 h

## Resultado

Estado: **pasa**. horas de ingreso del Acto III que faltan para el 50 % sin pagos extra (rapido): **0.1785 h** (IC95 [0.1719, 0.1852], n = 60).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Lento\|lento]] | 0.1055 | [0.0999, 0.1112] | 60 |
| [[Perfil Medio\|medio]] | 0.1423 | [0.1384, 0.1462] | 60 |
| [[Perfil Rápido\|rapido]] | 0.1785 | [0.1719, 0.1852] | 60 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| horas de ingreso del Acto III que faltan para el 50 % sin pagos extra (lento) | 0.1055 h | [0.0999, 0.1112] | … a 0.3 | pasa |
| horas de ingreso del Acto III que faltan para el 50 % sin pagos extra (medio) | 0.1423 h | [0.1384, 0.1462] | … a 0.3 | pasa |
| horas de ingreso del Acto III que faltan para el 50 % sin pagos extra (rapido) | 0.1785 h | [0.1719, 0.1852] | … a 0.3 | pasa |

## Criterio

- **horas_max:** 0.3

## Requisitos que protege

- Vía de deuda: 25 % en el Acto II y 50 % en el círculo ([[24 Umbrales de acto]])

## Mutaciones de prueba

- Amortización semanal de 100
  - `economy.debt.amortization_weekly` = 100

## Relaciones

- **Documentos:** [[28 §7 Deuda del Acto I y sus nombres]], [[24 Umbrales de acto]]
- **Bloques de economía:** [[Deuda del Acto I]]
- **Perfiles:** [[Perfil Lento]], [[Perfil Medio]], [[Perfil Rápido]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:607`
