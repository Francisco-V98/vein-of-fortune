---
id: "sim-E4"
tipo: "regla-sim"
title: "La especulación no domina"
aliases: ["sim-E4"]
grupo: "E · Mercado y bucles"
estado: "pasa"
origen: "doc"
valor: 6.8769
unidad: "%"
documentos: ["[[03 Comercio y mercado]]", "[[28 §3 Los diez minerales]]", "[[28 §3 Los diez minerales]]", "[[28 §13 Validación con el simulador (F0-53)]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:373"
generado: true
---

# La especulación no domina

> E · Mercado y bucles · pasa · spot ≤ +2,5 % · Bolsa ≤ +7 % · estación ≤ +12 % · trader ≤ 25 % del ingreso minero

**Grupo:** E · Mercado y bucles · **Origen del umbral:** documento aprobado

## Qué mide

rendimiento neto de especular con aviso perfecto, con la estación y de un trader puro

## Umbral

spot ≤ +2,5 % · Bolsa ≤ +7 % · estación ≤ +12 % · trader ≤ 25 % del ingreso minero

## Resultado

Estado: **pasa**. mejor rendimiento neto de especular con aviso perfecto (bolsa; evento ≥ 12, espera 1): **6.8769 %** (IC95 [6.7756, 6.9783], n = 5313).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| mejor rendimiento neto de especular con aviso perfecto (spot; evento ≥ 12, espera 1) | 2.119 % | [2.0195, 2.2185] | … a 2.5 | pasa |
| mejor rendimiento neto de especular con aviso perfecto (bolsa; evento ≥ 12, espera 1) | 6.8769 % | [6.7756, 6.9783] | … a 7 | pasa |
| mejor rendimiento neto de especular con la estación (carbon, espera 56 días) | 6.4783 % | [6.4783, 6.4783] | … a 12 | pasa |
| ingreso de un trader puro frente al ingreso minero (peor acto) | 0 % | [0, 0] | … a 25 | pasa |

## Criterio

- **umbrales:** 5, 8, 12
- **esperas:** 1, 3
- **spot_max:** 2.5
- **bolsa_max:** 7
- **estacion_max:** 12
- **esperas_estacion:** 28, 56
- **trader_max:** 25

## Requisitos que protege

- No existe ganancia segura entre canales (tienda y pedidos solo con mercancía propia) ([[03 Comercio y mercado]])

## Mutaciones de prueba

- Bolsa con el spread completo y sin impuesto
  - `economy.market.bolsa.spread_mult` = 1
  - `economy.market.sale_tax_pct` = 0

## Relaciones

- **Documentos:** [[03 Comercio y mercado]], [[28 §3 Los diez minerales]], [[28 §13 Validación con el simulador (F0-53)]]
- **Bloques de economía:** [[Mercado]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:373`
