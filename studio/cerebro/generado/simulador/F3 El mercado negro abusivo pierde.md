---
id: "sim-F3"
tipo: "regla-sim"
title: "El mercado negro abusivo pierde"
aliases: ["sim-F3"]
grupo: "F · Mercado negro y vigilancia"
estado: "pasa"
origen: "doc"
valor: 13.1474
unidad: "días"
documentos: ["[[03 Comercio y mercado]]", "[[28 §10 Vigilancia, multas, mercado negro y mora]]", "[[28 §10 Vigilancia, multas, mercado negro y mora]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:458"
generado: true
---

# El mercado negro abusivo pierde

> F · Mercado negro y vigilancia · pasa · < 0 % · una redada cada 11 ± 3 días

**Grupo:** F · Mercado negro y vigilancia · **Origen del umbral:** documento aprobado

## Qué mide

ganancia y días entre redadas del jugador que no se detiene

## Umbral

< 0 % · una redada cada 11 ± 3 días

## Resultado

Estado: **pasa**. días entre redadas del jugador abusivo (Acto IV): **13.1474 días** (IC95 –, n = 502).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | -15.1837 | [-17.1309, -13.2365] | 30 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| ganancia del jugador abusivo (peor acto: IV) | -15.1837 % | [-17.1309, -13.2365] | … a 0 | pasa |
| días entre redadas del jugador abusivo (Acto II) | 10.9453 días | [10.9453, 10.9453] | 8 a 14 | pasa |
| días entre redadas del jugador abusivo (Acto III) | 10.9453 días | [10.9453, 10.9453] | 8 a 14 | pasa |
| días entre redadas del jugador abusivo (Acto IV) | 13.1474 días | [13.1474, 13.1474] | 8 a 14 | pasa |

## Criterio

- **politica:** umbral: 100
- **max:** 0
- **intervalo_min:** 8
- **intervalo_max:** 14

## Requisitos que protege

- El mercado negro es un complemento moderado, no una estrategia dominante ([[03 Comercio y mercado]])

## Mutaciones de prueba

- Sin multas, sin redadas y vigilancia que baja 50 al día
  - `economy.surveillance.raid.fine_pct_wealth` = 0
  - `economy.surveillance.raid.fine_min` = 0
  - `economy.surveillance.fines.vigilado.fine_pct_wealth` = 0
  - `economy.surveillance.fines.vigilado.fine_min` = 0
  - `economy.surveillance.fines.observado.fine_pct_wealth` = 0
  - `economy.surveillance.fines.observado.fine_min` = 0
  - `economy.surveillance.raid.at` = 300
  - `economy.surveillance.natural_decay_per_day` = 50

## Relaciones

- **Documentos:** [[03 Comercio y mercado]], [[28 §10 Vigilancia, multas, mercado negro y mora]]
- **Bloques de economía:** [[Vigilancia]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:458`
