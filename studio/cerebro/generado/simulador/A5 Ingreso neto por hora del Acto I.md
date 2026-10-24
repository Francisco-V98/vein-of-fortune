---
id: "sim-A5"
tipo: "regla-sim"
title: "Ingreso neto por hora del Acto I"
aliases: ["sim-A5"]
grupo: "A · Acto I y deuda"
estado: "pasa"
origen: "doc"
valor: 13.6851
unidad: "%"
documentos: ["[[28 §2 Ritmo objetivo y patrimonio]]", "[[17 Mapa de historia]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:66"
generado: true
---

# Ingreso neto por hora del Acto I

> A · Acto I y deuda · pasa · ≤ 20 %

**Grupo:** A · Acto I y deuda · **Origen del umbral:** documento aprobado

## Qué mide

desviación del ingreso por hora de cada perfil frente a 650 · 1 100 · 2 200

## Umbral

≤ 20 %

## Resultado

Estado: **pasa**. desviación del ingreso/h (lento): **13.6851 %** (IC95 [13.1463, 14.2239], n = 6000).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Lento\|lento]] | 738.9533 | [735.4512, 742.4555] | 6000 |
| [[Perfil Medio\|medio]] | 1166.9007 | [1162.5401, 1171.2613] | 6000 |
| [[Perfil Rápido\|rapido]] | 2205.6183 | [2200.1381, 2211.0984] | 6000 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| desviación del ingreso/h (lento) | 13.6851 % | [13.1463, 14.2239] | … a 20 | pasa |
| desviación del ingreso/h (medio) | 6.0819 % | [5.6855, 6.4783] | … a 20 | pasa |
| desviación del ingreso/h (rapido) | 0.2554 % | [0.0063, 0.5045] | … a 20 | pasa |

## Criterio

- **desv_max:** 20

## Requisitos que protege

- Ingreso neto por hora del Acto I (650 · 1 100 · 2 200) ([[28 §2 Ritmo objetivo y patrimonio]])

## Mutaciones de prueba

- Aguante del Acto I de 20: el ritmo del Acto I se hunde
  - `economy.energy.per_act.I` = 20, 30

## Relaciones

- **Documentos:** [[28 §2 Ritmo objetivo y patrimonio]], [[17 Mapa de historia]]
- **Bloques de economía:** [[Ritmo objetivo]], [[Guion económico del Acto I]], [[Energía]]
- **Perfiles:** [[Perfil Lento]], [[Perfil Medio]], [[Perfil Rápido]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:66`
