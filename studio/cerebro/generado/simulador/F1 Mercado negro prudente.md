---
id: "sim-F1"
tipo: "regla-sim"
title: "Mercado negro prudente"
aliases: ["sim-F1"]
grupo: "F · Mercado negro y vigilancia"
estado: "pasa"
origen: "doc"
valor: 6.5903
unidad: "%"
documentos: ["[[03 Comercio y mercado]]", "[[28 §10 Vigilancia, multas, mercado negro y mora]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:430"
generado: true
---

# Mercado negro prudente

> F · Mercado negro y vigilancia · pasa · +3 a +12 %

**Grupo:** F · Mercado negro y vigilancia · **Origen del umbral:** documento aprobado

## Qué mide

ganancia semanal del jugador que se detiene en vigilancia 30 sobre su ingreso honesto

## Umbral

+3 a +12 %

## Resultado

Estado: **pasa**. ganancia semanal del mercado negro prudente sobre el ingreso honesto (Acto III): **6.5903 %** (IC95 [5.7187, 7.4619], n = 30).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 7.0969 | [5.7209, 8.4729] | 30 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| ganancia semanal del mercado negro prudente sobre el ingreso honesto (Acto II) | 6.9211 % | [5.8722, 7.97] | 3 a 12 | pasa |
| ganancia semanal del mercado negro prudente sobre el ingreso honesto (Acto III) | 6.5903 % | [5.7187, 7.4619] | 3 a 12 | pasa |
| ganancia semanal del mercado negro prudente sobre el ingreso honesto (Acto IV) | 7.0969 % | [5.7209, 8.4729] | 3 a 12 | pasa |

## Criterio

- **politica:** umbral: 30
- **min:** 3
- **max:** 12

## Requisitos que protege

- El mercado negro es un complemento moderado, no una estrategia dominante ([[03 Comercio y mercado]])

## Mutaciones de prueba

- Prima negra de 90 %
  - `minerals.carbon.black_premium` = 90
  - `minerals.hierro.black_premium` = 90
  - `minerals.cobre.black_premium` = 90
  - `minerals.salitre.black_premium` = 90
  - `minerals.plata.black_premium` = 90
  - `minerals.cuarzo.black_premium` = 90
  - `minerals.oro.black_premium` = 90
  - `minerals.esmeralda.black_premium` = 90
  - `minerals.diamante.black_premium` = 90

## Relaciones

- **Documentos:** [[03 Comercio y mercado]], [[28 §10 Vigilancia, multas, mercado negro y mora]]
- **Bloques de economía:** [[Vigilancia]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:430`
