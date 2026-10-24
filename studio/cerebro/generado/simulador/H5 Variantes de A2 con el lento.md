---
id: "sim-H5"
tipo: "regla-sim"
title: "Variantes de A2 con el lento"
aliases: ["sim-H5"]
grupo: "H · Deuda, mora y rescate"
estado: "pasa"
origen: "prop."
valor: 1.0
unidad: ""
documentos: ["[[28 §7 Deuda del Acto I y sus nombres]]", "[[28 §7 Deuda del Acto I y sus nombres]]", "[[23 Árbol de decisiones y consecuencias]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:652"
generado: true
---

# Variantes de A2 con el lento

> H · Deuda, mora y rescate · pasa · caja < 0 a lo sumo una semana · vía alcanzable

**Grupo:** H · Deuda, mora y rescate · **Origen del umbral:** propuesta del simulador

## Qué mide

caja negativa del lento y vía alcanzable con la cuota extra de luz y con el adelanto de cuota

## Umbral

caja < 0 a lo sumo una semana · vía alcanzable

## Resultado

Estado: **pasa**. la deuda de luz crece más despacio que la deuda principal (1 = sí): **1 ** (IC95 –, n = –).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Lento\|lento]] | 100 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| corridas del lento con caja negativa a lo sumo una semana (cuota_extra) | 100 % | [97.6553, 100] | 90 a … | pasa |
| corridas del lento que alcanzan el 25 % al cerrar el Acto II (cuota_extra) | 100 % | [97.6553, 100] | 90 a … | pasa |
| corridas del lento con caja negativa a lo sumo una semana (adelanto) | 100 % | [97.6553, 100] | 90 a … | pasa |
| corridas del lento que alcanzan el 25 % al cerrar el Acto II (adelanto) | 100 % | [97.6553, 100] | 90 a … | pasa |
| la deuda de luz crece más despacio que la deuda principal (1 = sí) | 1  | [1, 1] | 1 a 1 | pasa |

## Criterio

- **caja_min:** 90
- **via_min:** 90

## Requisitos que protege

- Variantes de A2 (cuota extra de luz, deuda de luz, adelanto de cuota) ([[23 Árbol de decisiones y consecuencias]])

## Mutaciones de prueba

- Cuota extra de luz de 30 000
  - `economy.debt.extra_light_fee` = 30000

## Relaciones

- **Documentos:** [[28 §7 Deuda del Acto I y sus nombres]], [[23 Árbol de decisiones y consecuencias]]
- **Bloques de economía:** [[Deuda del Acto I]]
- **Perfiles:** [[Perfil Lento]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:652`
