---
id: "sim-C1"
tipo: "regla-sim"
title: "Cada mejora se paga en pocas expediciones"
aliases: ["sim-C1"]
grupo: "C · Herramientas"
estado: "pasa"
origen: "doc"
valor: 1.037
unidad: "exp"
documentos: ["[[28 §5 Herramientas]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:227"
generado: true
---

# Cada mejora se paga en pocas expediciones

> C · Herramientas · pasa · la mejor mejora de cada nivel se paga en 1–8 expediciones

**Grupo:** C · Herramientas · **Origen del umbral:** documento aprobado

## Qué mide

expediciones para pagar cada una de las 16 mejoras (mineral propio o comprado a ×1,18)

## Umbral

la mejor mejora de cada nivel se paga en 1–8 expediciones

## Resultado

Estado: **pasa**. expediciones para pagar la mejora más rápida: **1.037 exp** (IC95 –, n = 4).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| expediciones para pagar la mejora más rápida | 1.037 exp | [1.037, 1.037] | 1 a … | pasa |
| expediciones para pagar la mejora más lenta (mineral propio) | 7.0806 exp | [7.0806, 7.0806] | … a 8 | pasa |
| expediciones para pagar la mejora más lenta (mineral comprado) | 7.1883 exp | [7.1883, 7.1883] | … a 8 | pasa |

### Datos adicionales

- **propios:** 1.04, 3.44, 7.08, 3.22

## Criterio

- **exp_min:** 1
- **exp_max:** 8
- **modo:** mejor_por_nivel

## Requisitos que protege

- Mejorar no se paga en una sola expedición ([[28 §5 Herramientas]])

## Mutaciones de prueba

- Mejoras de nivel 2 a 10 esquirlas: la más rápida se paga en menos de una expedición
  - `economy.tools.upgrade_cost.pico.2` = 10
  - `economy.tools.upgrade_cost.criba.2` = 10
  - `economy.tools.upgrade_cost.taladro.2` = 10
  - `economy.tools.upgrade_cost.cincel.2` = 10

## Relaciones

- **Documentos:** [[28 §5 Herramientas]]
- **Bloques de economía:** [[Herramientas]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:227`
