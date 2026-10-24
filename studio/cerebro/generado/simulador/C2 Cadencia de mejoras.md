---
id: "sim-C2"
tipo: "regla-sim"
title: "Cadencia de mejoras"
aliases: ["sim-C2"]
grupo: "C · Herramientas"
estado: "pasa"
origen: "prop."
valor: 2.6124
unidad: "h"
documentos: ["[[28 §5 Herramientas]]", "[[28 §5 Herramientas]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:241"
generado: true
---

# Cadencia de mejoras

> C · Herramientas · pasa · 0,3–3 h

**Grupo:** C · Herramientas · **Origen del umbral:** propuesta del simulador

## Qué mide

horas de juego entre un nivel de herramienta y el siguiente

## Umbral

0,3–3 h

## Resultado

Estado: **pasa**. horas de ingreso para pagar la mejora más cara (cincel a nivel 4): **2.6124 h** (IC95 –, n = 16).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 2.6124 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| horas de ingreso para pagar la mejora más barata (criba a nivel 3) | 0.4687 h | [0.4687, 0.4687] | 0.3 a … | pasa |
| horas de ingreso para pagar la mejora más cara (cincel a nivel 4) | 2.6124 h | [2.6124, 2.6124] | … a 3 | pasa |

## Criterio

- **horas_min:** 0.3
- **horas_max:** 3

## Requisitos que protege

- Niveles de herramienta por acto: guía, no tope ([[28 §5 Herramientas]])
- Mejorar no se paga en una sola expedición ([[28 §5 Herramientas]])

## Mutaciones de prueba

- Cincel a nivel 4 por 500 000
  - `economy.tools.upgrade_cost.cincel.4` = 500000

## Relaciones

- **Documentos:** [[28 §5 Herramientas]]
- **Bloques de economía:** [[Herramientas]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:241`
