---
id: "sim-B5"
tipo: "regla-sim"
title: "El optimizador no se salta el techo de herramienta"
aliases: ["sim-B5"]
grupo: "B · Ritmo, progresión y estatus"
estado: "pasa"
origen: "prop."
valor: 100.0
unidad: "%"
documentos: ["[[28 §5 Herramientas]]", "[[28 §5 Herramientas]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:164"
generado: true
---

# El optimizador no se salta el techo de herramienta

> B · Ritmo, progresión y estatus · pasa · ≥ 90 % de las corridas con nivel ≤ guía del acto + 1

**Grupo:** B · Ritmo, progresión y estatus · **Origen del umbral:** propuesta del simulador

## Qué mide

corridas del optimizador con el nivel de pico dentro del techo del acto

## Umbral

≥ 90 % de las corridas con nivel ≤ guía del acto + 1

## Resultado

Estado: **pasa**. corridas con el nivel de pico ≤ 4 al cerrar el Acto II: **100 %** (IC95 [97.6553, 100], n = 160).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Optimizador\|optimizador]] | 100 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| corridas con el nivel de pico ≤ 4 al cerrar el Acto II | 100 % | [97.6553, 100] | 90 a … | pasa |
| corridas con el nivel de pico ≤ 5 al cerrar el Acto III | 100 % | [97.6553, 100] | 90 a … | pasa |

## Criterio

- **bajo_techo_min:** 90
- **margen_techo:** 1

## Requisitos que protege

- Niveles de herramienta por acto: guía, no tope ([[28 §5 Herramientas]])

## Mutaciones de prueba

- Mejoras de nivel 4 y 5 casi gratis: el optimizador llega al nivel 5 en el II
  - `economy.tools.upgrade_cost.pico.4` = 10
  - `economy.tools.upgrade_cost.pico.5` = 10
  - `economy.tools.upgrade_cost.criba.4` = 10
  - `economy.tools.upgrade_cost.criba.5` = 10
  - `economy.tools.upgrade_cost.taladro.4` = 10
  - `economy.tools.upgrade_cost.taladro.5` = 10
  - `economy.tools.upgrade_cost.cincel.4` = 10
  - `economy.tools.upgrade_cost.cincel.5` = 10

## Relaciones

- **Documentos:** [[28 §5 Herramientas]]
- **Bloques de economía:** [[Herramientas]]
- **Perfiles:** [[Perfil Optimizador]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:164`
