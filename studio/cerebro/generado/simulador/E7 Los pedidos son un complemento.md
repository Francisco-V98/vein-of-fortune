---
id: "sim-E7"
tipo: "regla-sim"
title: "Los pedidos son un complemento"
aliases: ["sim-E7"]
grupo: "E · Mercado y bucles"
estado: "pasa"
origen: "doc"
valor: 1.0052
unidad: "%"
documentos: ["[[28 §9 Información, viaje, pedidos y contratos]]", "[[03 Comercio y mercado]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:417"
generado: true
---

# Los pedidos son un complemento

> E · Mercado y bucles · pasa · > 0 y ≤ 15 % del ingreso

**Grupo:** E · Mercado y bucles · **Origen del umbral:** documento aprobado

## Qué mide

ganancia extra de los pedidos sobre el ingreso de cada acto

## Umbral

> 0 y ≤ 15 % del ingreso

## Resultado

Estado: **pasa**. ganancia extra de los pedidos sobre el ingreso (Acto IV): **1.0052 %** (IC95 [0.9386, 1.0718], n = 60).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 1.0052 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| ganancia extra de los pedidos sobre el ingreso (Acto II) | 2.1865 % | [2.1055, 2.2676] | 0.5 a 15 | pasa |
| ganancia extra de los pedidos sobre el ingreso (Acto III) | 2.9734 % | [2.8197, 3.127] | 0.5 a 15 | pasa |
| ganancia extra de los pedidos sobre el ingreso (Acto IV) | 1.0052 % | [0.9386, 1.0718] | 0.5 a 15 | pasa |

## Criterio

- **extra_min:** 0.5
- **extra_max:** 15

## Requisitos que protege

- Pedidos fuera del Acto I: un estándar cada 2 días y un urgente por semana, ≤ 15 % del ingreso ([[28 §9 Información, viaje, pedidos y contratos]])

## Mutaciones de prueba

- Pedido estándar con prima de 400 %
  - `economy.orders.0.premium_pct` = 400

## Relaciones

- **Documentos:** [[28 §9 Información, viaje, pedidos y contratos]], [[03 Comercio y mercado]]
- **Bloques de economía:** [[Información]], [[Viaje]], [[Pedidos]], [[Reglas de los pedidos]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:417`
