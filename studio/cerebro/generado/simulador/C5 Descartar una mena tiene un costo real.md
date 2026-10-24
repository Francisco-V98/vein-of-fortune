---
id: "sim-C5"
tipo: "regla-sim"
title: "Descartar una mena tiene un costo real"
aliases: ["sim-C5"]
grupo: "C · Herramientas"
estado: "pasa"
origen: "prop."
valor: 22.0671
unidad: "%"
documentos: ["[[02 Extracción]]", "[[28 §4 Energía]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:280"
generado: true
---

# Descartar una mena tiene un costo real

> C · Herramientas · pasa · pérdida 3–35 % · al doblar el costo pierde ≥ 1 % más · ≤ 60 % de las menas descartadas

**Grupo:** C · Herramientas · **Origen del umbral:** propuesta del simulador

## Qué mide

pérdida de ingreso por descartar al 25 % de la energía frente a descartar gratis; sensibilidad al 0, 25 y 50 %

## Umbral

pérdida 3–35 % · al doblar el costo pierde ≥ 1 % más · ≤ 60 % de las menas descartadas

## Resultado

Estado: **pasa**. pérdida de ingreso de descartar a coste normal frente a descartar gratis: **22.0671 %** (IC95 [21.5603, 22.5738], n = 16).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Optimizador\|optimizador]] | 22.0671 | [21.5603, 22.5738] | 16 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| pérdida de ingreso de descartar a coste normal frente a descartar gratis | 22.0671 % | [21.5603, 22.5738] | 3 a 35 | pasa |
| pérdida adicional al doblar el costo de descartar | 5.4856 % | [5.0283, 5.943] | 1 a … | pasa |
| mena descartada sobre las escaneadas (coste normal) | 27.1899 % | [26.8704, 27.5094] | … a 60 | pasa |

### Datos adicionales

- **ingreso_h:**
  - **0:** 51980.9582
  - **25:** 40505.5837
  - **50:** 38281.4098

## Criterio

- **perdida_min:** 3
- **perdida_max:** 35
- **doble_min:** 1
- **descartes_max:** 60

## Requisitos que protege

- Descartar una mena cuesta el 25 % de su energía ([[02 Extracción]])

## Mutaciones de prueba

- Descartar una mena sin costo
  - `economy.expedition.ore_discard.energy_pct_of_ore` = 0

## Relaciones

- **Documentos:** [[02 Extracción]], [[28 §4 Energía]]
- **Bloques de economía:** [[Energía]], [[Expediciones]]
- **Perfiles:** [[Perfil Optimizador]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:280`
