---
id: "sim-I1"
tipo: "regla-sim"
title: "Determinismo"
aliases: ["sim-I1"]
grupo: "I · Meta-casos"
estado: "pasa"
origen: "prop."
valor: 1.0
unidad: ""
documentos: ["[[15 Flujo de trabajo y calidad]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:681"
generado: true
---

# Determinismo

> I · Meta-casos · pasa · idéntico

**Grupo:** I · Meta-casos · **Origen del umbral:** propuesta del simulador

## Qué mide

misma semilla, mismo resultado tras redondear

## Umbral

idéntico

## Resultado

Estado: **pasa**. misma semilla, mismo resultado (1 = sí): **1 ** (IC95 –, n = –).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| misma semilla, mismo resultado (1 = sí) | 1  | [1, 1] | 1 a 1 | pasa |

## Criterio

- **acto1:** 150
- **semillas:** 1
- **dias:** 60
- **pasos:** 40

## Requisitos que protege

- El simulador es reproducible y cada regla se puede voltear ([[15 Flujo de trabajo y calidad]])

## Relaciones

- **Documentos:** [[15 Flujo de trabajo y calidad]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:681`
