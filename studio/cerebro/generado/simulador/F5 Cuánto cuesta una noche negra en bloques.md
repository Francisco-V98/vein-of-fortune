---
id: "sim-F5"
tipo: "regla-sim"
title: "Cuánto cuesta una noche negra en bloques"
aliases: ["sim-F5"]
grupo: "F · Mercado negro y vigilancia"
estado: "pasa"
origen: "prop."
valor: 0.9683
unidad: "bloques"
documentos: ["[[03 Comercio y mercado]]", "[[28 §10 Vigilancia, multas, mercado negro y mora]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:492"
generado: true
---

# Cuánto cuesta una noche negra en bloques

> F · Mercado negro y vigilancia · pasa · informativa (> 0)

**Grupo:** F · Mercado negro y vigilancia · **Origen del umbral:** propuesta del simulador

## Qué mide

bloques de expedición que puede costar una noche negra antes de que deje de compensar (insumo para F4-72)

## Umbral

informativa (> 0)

## Resultado

Estado: **pasa**. bloques que puede costar una noche negra sin perder (Acto II): **0.9683 bloques** (IC95 –, n = 1403).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 0.8535 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| bloques que puede costar una noche negra sin perder (Acto II) | 0.9683 bloques | [0.9683, 0.9683] | 0 a … | pasa |
| bloques que puede costar una noche negra sin perder (Acto III) | 0.9495 bloques | [0.9495, 0.9495] | 0 a … | pasa |
| bloques que puede costar una noche negra sin perder (Acto IV) | 0.8535 bloques | [0.8535, 0.8535] | 0 a … | pasa |

### Datos adicionales

- **por_acto:**
  - **II:**
    - **valor:** 0.9683
    - **n:** 1403
  - **III:**
    - **valor:** 0.9495
    - **n:** 1372
  - **IV:**
    - **valor:** 0.8535
    - **n:** 1628

## Criterio

- **politica:** umbral: 30
- **min:** 0
- **informativa:** sí

## Requisitos que protege

- El mercado negro es un complemento moderado, no una estrategia dominante ([[03 Comercio y mercado]])

## Mutaciones de prueba

- Sin prima negra: una noche negra no compensa nada
  - `minerals.carbon.black_premium` = 0
  - `minerals.hierro.black_premium` = 0
  - `minerals.cobre.black_premium` = 0
  - `minerals.salitre.black_premium` = 0
  - `minerals.plata.black_premium` = 0
  - `minerals.cuarzo.black_premium` = 0
  - `minerals.oro.black_premium` = 0
  - `minerals.esmeralda.black_premium` = 0
  - `minerals.diamante.black_premium` = 0

## Relaciones

- **Documentos:** [[03 Comercio y mercado]], [[28 §10 Vigilancia, multas, mercado negro y mora]]
- **Bloques de economía:** [[Vigilancia]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:492`
