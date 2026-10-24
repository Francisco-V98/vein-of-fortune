---
id: "sim-E2"
tipo: "regla-sim"
title: "Impacto del jugador en el precio"
aliases: ["sim-E2"]
grupo: "E · Mercado y bucles"
estado: "pasa"
origen: "doc"
valor: 1.0
unidad: ""
documentos: ["[[03 Comercio y mercado]]", "[[28 §6 Frenos de mercado]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:348"
generado: true
---

# Impacto del jugador en el precio

> E · Mercado y bucles · pasa · w crece de 0,5 a 4 · slippage creciente (o estable, ≥ 0,9×) y ≤ 12 % en el IV · w por acto

**Grupo:** E · Mercado y bucles · **Origen del umbral:** documento aprobado

## Qué mide

w(P) monótona y coste del slippage sobre el ingreso bruto; w por acto frente al w del patrimonio medio

## Umbral

w crece de 0,5 a 4 · slippage creciente (o estable, ≥ 0,9×) y ≤ 12 % en el IV · w por acto ±15 %

## Resultado

Estado: **pasa**. w(P) estrictamente creciente (1 = sí): **1 ** (IC95 –, n = –).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 0.5241 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| w(P) estrictamente creciente (1 = sí) | 1  | [1, 1] | 1 a 1 | pasa |
| w en patrimonio 0 menos w mínimo | 0  | [0, 0] | … a 0 | pasa |
| w máximo alcanzable frente al tope | 99.6514 % | [99.6514, 99.6514] | … a 100 | pasa |
| razón mínima del coste de slippage entre actos consecutivos (crece o se mantiene) | 1.0729 x | [1.0729, 1.0729] | 0.9 a … | pasa |
| coste de slippage sobre el ingreso bruto vendiendo todo al spot (Acto IV) | 0.5241 % | [0.4852, 0.563] | … a 12 | pasa |
| w del acto frente al w del patrimonio medio (Acto II) | 1.3967 % | [1.3967, 1.3967] | … a 15 | pasa |
| w del acto frente al w del patrimonio medio (Acto III) | 1.8234 % | [1.8234, 1.8234] | … a 15 | pasa |
| w del acto frente al w del patrimonio medio (Acto IV) | 0.4783 % | [0.4783, 1.7224] | … a 15 | pasa |

## Criterio

- **slip_IV_max:** 12
- **w_acto_max:** 15
- **grilla_patrimonio:** 0, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000
- **razon_min:** 0.9

## Requisitos que protege

- El impacto del jugador no crea bucles de ganancia ([[03 Comercio y mercado]])

## Mutaciones de prueba

- w del Acto IV de 8
  - `economy.market.player_impact.by_act.IV` = 8

## Relaciones

- **Documentos:** [[03 Comercio y mercado]], [[28 §6 Frenos de mercado]]
- **Bloques de economía:** [[Mercado]], [[Deriva guionizada del Acto I]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:348`
