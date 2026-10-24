---
id: "sim-I3"
tipo: "regla-sim"
title: "Intervalos visibles y ninguna regla incierta"
aliases: ["sim-I3"]
grupo: "I · Meta-casos"
estado: "pasa"
origen: "prop."
valor: 0
unidad: "reglas"
documentos: ["[[15 Flujo de trabajo y calidad]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:709"
generado: true
---

# Intervalos visibles y ninguna regla incierta

> I · Meta-casos · pasa · 0

**Grupo:** I · Meta-casos · **Origen del umbral:** propuesta del simulador

## Qué mide

reglas en «incierto» y reglas medidas sin n ni intervalo

## Umbral

0

## Resultado

Estado: **pasa**. reglas en «incierto»: **0 reglas** (IC95 –, n = 49).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| reglas en «incierto» | 0 reglas | [0, 0] | … a 0 | pasa |
| reglas medidas sin n ni intervalo | 0 reglas | [0, 0] | … a 0 | pasa |

### Datos adicionales

- **inciertas:** 
- **sin_ic:** 

## Criterio

- **deterministas:** A6, A7, B8, C1, C4, E1, E2, E6, F4, G5, G6, H3, H4, H6, I1, I2, I3

## Requisitos que protege

- El simulador es reproducible y cada regla se puede voltear ([[15 Flujo de trabajo y calidad]])

## Relaciones

- **Documentos:** [[15 Flujo de trabajo y calidad]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:709`
