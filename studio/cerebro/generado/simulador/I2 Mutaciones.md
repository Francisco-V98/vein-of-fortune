---
id: "sim-I2"
tipo: "regla-sim"
title: "Mutaciones"
aliases: ["sim-I2"]
grupo: "I · Meta-casos"
estado: "pasa"
origen: "prop."
valor: 100.0
unidad: "%"
documentos: ["[[15 Flujo de trabajo y calidad]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:696"
generado: true
---

# Mutaciones

> I · Meta-casos · pasa · 100 % de las reglas

**Grupo:** I · Meta-casos · **Origen del umbral:** propuesta del simulador

## Qué mide

cambiar una cifra de world.json en memoria cambia el estado de su regla

## Umbral

100 % de las reglas

## Resultado

Estado: **pasa**. reglas cuya mutación cambia el estado de alguna condición: **100 %** (IC95 –, n = 47).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| reglas cuya mutación cambia el estado de alguna condición | 100 % | [100, 100] | 100 a … | pasa |

### Datos adicionales

- **sin_volteo:** 

## Criterio

- **min:** 100
- **modo:** mini

## Requisitos que protege

- El simulador es reproducible y cada regla se puede voltear ([[15 Flujo de trabajo y calidad]])

## Relaciones

- **Documentos:** [[15 Flujo de trabajo y calidad]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:696`
