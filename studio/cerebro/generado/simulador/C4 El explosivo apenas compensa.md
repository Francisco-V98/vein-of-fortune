---
id: "sim-C4"
tipo: "regla-sim"
title: "El explosivo apenas compensa"
aliases: ["sim-C4"]
grupo: "C · Herramientas"
estado: "pasa"
origen: "doc"
valor: 22.5854
unidad: "%"
documentos: ["[[28 §5 Herramientas]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:267"
generado: true
---

# El explosivo apenas compensa

> C · Herramientas · pasa · medio ≤ +5 % · rápido ≤ +25 %

**Grupo:** C · Herramientas · **Origen del umbral:** documento aprobado

## Qué mide

rendimiento neto del explosivo para el medio y para el rápido

## Umbral

medio ≤ +5 % · rápido ≤ +25 %

## Resultado

Estado: **pasa**. rendimiento neto del explosivo, perfil rapido (peor: potencia 2): **22.5854 %** (IC95 –, n = –).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Lento\|lento]] | -7 | – | – |
| [[Perfil Medio\|medio]] | 17 | – | – |
| [[Perfil Rápido\|rapido]] | 36 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| rendimiento neto del explosivo, perfil medio (peor: potencia 2) | 3.5854 % | [3.5854, 3.5854] | … a 5 | pasa |
| rendimiento neto del explosivo, perfil rapido (peor: potencia 2) | 22.5854 % | [22.5854, 22.5854] | … a 25 | pasa |

## Criterio

- **medio_max:** 5
- **rapido_max:** 25

## Requisitos que protege

- El explosivo apenas compensa ([[28 §5 Herramientas]])

## Mutaciones de prueba

- Explosivo de potencia 1 a 1 esquirla
  - `economy.tools.explosive.powers.0.cost` = 1

## Relaciones

- **Documentos:** [[28 §5 Herramientas]]
- **Bloques de economía:** [[Herramientas]]
- **Perfiles:** [[Perfil Lento]], [[Perfil Medio]], [[Perfil Rápido]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:267`
