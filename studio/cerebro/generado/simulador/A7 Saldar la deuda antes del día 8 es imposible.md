---
id: "sim-A7"
tipo: "regla-sim"
title: "Saldar la deuda antes del día 8 es imposible"
aliases: ["sim-A7"]
grupo: "A · Acto I y deuda"
estado: "pasa"
origen: "doc"
valor: 19.3714
unidad: "%"
documentos: ["[[28 §7 Deuda del Acto I y sus nombres]]", "[[24 Umbrales de acto]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:92"
generado: true
---

# Saldar la deuda antes del día 8 es imposible

> A · Acto I y deuda · pasa · < 100 % de K

**Grupo:** A · Acto I y deuda · **Origen del umbral:** documento aprobado

## Qué mide

caja máxima del Acto I frente al capital de la deuda

## Umbral

< 100 % de K

## Resultado

Estado: **pasa**. caja máxima del Acto I frente al capital: **19.3714 %** (IC95 –, n = 6000).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Rápido\|rapido]] | 19.3714 | – | 6000 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| caja máxima del Acto I frente al capital | 19.3714 % | [19.3714, 19.3714] | … a 99.9 | pasa |

## Criterio

- **tope_pct:** 99.9

## Requisitos que protege

- Saldar la deuda antes de A2 es imposible ([[24 Umbrales de acto]])

## Mutaciones de prueba

- Capital de 1 500: el rápido podría saldarlo
  - `economy.debt.principal` = 1500

## Relaciones

- **Documentos:** [[28 §7 Deuda del Acto I y sus nombres]], [[24 Umbrales de acto]]
- **Bloques de economía:** [[Deuda del Acto I]]
- **Perfiles:** [[Perfil Rápido]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:92`
