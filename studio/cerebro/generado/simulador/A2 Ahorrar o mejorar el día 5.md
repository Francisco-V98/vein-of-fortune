---
id: "sim-A2"
tipo: "regla-sim"
title: "Ahorrar o mejorar el día 5"
aliases: ["sim-A2"]
grupo: "A · Acto I y deuda"
estado: "pasa"
origen: "doc"
valor: 9.05
unidad: "pp"
documentos: ["[[28 §5 Herramientas]]", "[[28 §13 Validación con el simulador (F0-53)]]", "[[27 Guion del Acto I, día a día]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:21"
generado: true
---

# Ahorrar o mejorar el día 5

> A · Acto I y deuda · pasa · margen con mejora ≥ 10 % · diferencia 8–45 pp · pago con mejora ≥ 80 %

**Grupo:** A · Acto I y deuda · **Origen del umbral:** documento aprobado

## Qué mide

margen y pago del medio con la mejora del pico; diferencia con no mejorar

## Umbral

margen con mejora ≥ 10 % · diferencia 8–45 pp · pago con mejora ≥ 80 %

## Resultado

Estado: **pasa**. diferencia de pago sin y con mejora (pp): **9.05 pp** (IC95 [8.2941, 9.8059], n = 6000).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 90.5667 | – | 6000 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| margen con la mejora | 45.4284 % | [44.5934, 46.2633] | 10 a … | pasa |
| diferencia de pago sin y con mejora (pp) | 9.05 pp | [8.2941, 9.8059] | 8 a 45 | pasa |
| pago a tiempo con mejora | 90.5667 % | [89.8009, 91.2805] | 80 a … | pasa |

## Criterio

- **margen_con_min:** 10
- **dif_min:** 8
- **dif_max:** 45
- **pago_con_min:** 80

## Requisitos que protege

- La cuota del día 7 (960) se paga con 5 expediciones y el margen es real ([[28 §7 Deuda del Acto I y sus nombres]])

## Mutaciones de prueba

- Aguante 27 y mejora del día 5 a 300
  - `economy.energy.per_act.I` = 27, 30
  - `economy.tools.upgrade_cost.pico.2` = 300

## Relaciones

- **Documentos:** [[28 §5 Herramientas]], [[28 §13 Validación con el simulador (F0-53)]], [[27 Guion del Acto I, día a día]]
- **Bloques de economía:** [[Herramientas]], [[Energía]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:21`
