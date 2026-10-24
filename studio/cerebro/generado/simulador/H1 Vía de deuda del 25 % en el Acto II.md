---
id: "sim-H1"
tipo: "regla-sim"
title: "Vía de deuda del 25 % en el Acto II"
aliases: ["sim-H1"]
grupo: "H · Deuda, mora y rescate"
estado: "pasa"
origen: "doc"
valor: 6.0748
unidad: "h"
documentos: ["[[28 §7 Deuda del Acto I y sus nombres]]", "[[24 Umbrales de acto]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:593"
generado: true
---

# Vía de deuda del 25 % en el Acto II

> H · Deuda, mora y rescate · pasa · falta ≤ 0,5 h · alcanzable · Comerciante + 25 % ≤ 6,5 h

**Grupo:** H · Deuda, mora y rescate · **Origen del umbral:** documento aprobado

## Qué mide

horas de ingreso que faltan para el 25 % sin pagos extra; corridas que lo alcanzan con la política «paga cuota y extra»; combinación con Comerciante

## Umbral

falta ≤ 0,5 h · alcanzable · Comerciante + 25 % ≤ 6,5 h

## Resultado

Estado: **pasa**. horas del Acto II para ser Comerciante y llevar el 25 % pagado: **6.0748 h** (IC95 [6.0636, 6.086], n = 160).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Lento\|lento]] | 0.2539 | [0.2335, 0.2743] | 60 |
| [[Perfil Medio\|medio]] | 0.3059 | [0.2997, 0.3121] | 60 |
| [[Perfil Rápido\|rapido]] | 0.3568 | [0.3489, 0.3647] | 60 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| horas de ingreso del Acto II que faltan para el 25 % sin pagos extra (lento) | 0.2539 h | [0.2335, 0.2743] | … a 0.5 | pasa |
| horas de ingreso del Acto II que faltan para el 25 % sin pagos extra (medio) | 0.3059 h | [0.2997, 0.3121] | … a 0.5 | pasa |
| horas de ingreso del Acto II que faltan para el 25 % sin pagos extra (rapido) | 0.3568 h | [0.3489, 0.3647] | … a 0.5 | pasa |
| corridas del medio que alcanzan el 25 % al cerrar el Acto II | 100 % | [97.6553, 100] | 90 a … | pasa |
| horas del Acto II para ser Comerciante y llevar el 25 % pagado | 6.0748 h | [6.0636, 6.086] | … a 6.5 | pasa |

## Criterio

- **horas_max:** 0.5
- **alcanza_min:** 90
- **combinado_max:** 6.5

## Requisitos que protege

- Pisos de estatus (Comerciante, Empresario, Magnate) ([[28 §2 Ritmo objetivo y patrimonio]])
- Vía de deuda: 25 % en el Acto II y 50 % en el círculo ([[24 Umbrales de acto]])

## Mutaciones de prueba

- Umbral del 25 % en 30 000
  - `economy.debt.route.A5_amount` = 30000

## Relaciones

- **Documentos:** [[28 §7 Deuda del Acto I y sus nombres]], [[24 Umbrales de acto]]
- **Bloques de economía:** [[Deuda del Acto I]]
- **Perfiles:** [[Perfil Lento]], [[Perfil Medio]], [[Perfil Rápido]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:593`
