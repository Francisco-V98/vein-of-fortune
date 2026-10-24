---
id: "sim-A3"
tipo: "regla-sim"
title: "El lento no es imposible ni trivial"
aliases: ["sim-A3"]
grupo: "A · Acto I y deuda"
estado: "pasa"
origen: "prop."
valor: 100.0
unidad: "%"
documentos: ["[[28 §7 Deuda del Acto I y sus nombres]]", "[[28 §13 Validación con el simulador (F0-53)]]", "[[24 Umbrales de acto]]", "[[27 Guion del Acto I, día a día]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:36"
generado: true
---

# El lento no es imposible ni trivial

> A · Acto I y deuda · pasa · 4 exp.: 10–60 % · 5 exp.: ≥ 60 % · cierra el acto · día 14 ≥ 90 %

**Grupo:** A · Acto I y deuda · **Origen del umbral:** propuesta del simulador

## Qué mide

pago del lento con 4 y 5 expediciones; cierre del acto; pago del día 14 tras prorrogar

## Umbral

4 exp.: 10–60 % · 5 exp.: ≥ 60 % · cierra el acto · día 14 ≥ 90 %

## Resultado

Estado: **pasa**. el acto cierra aunque no pague (la mora no cierra puertas): **100 %** (IC95 –, n = –).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Lento\|lento]] | 56.8333 | [55.5761, 58.0819] | 6000 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| pago del lento con 4 expediciones | 56.8333 % | [55.5761, 58.0819] | 10 a 60 | pasa |
| pago del lento con 5 expediciones | 85.85 % | [84.9451, 86.709] | 60 a … | pasa |
| el acto cierra aunque no pague (la mora no cierra puertas) | 100 % | [100, 100] | 100 a 100 | pasa |
| paga el día 14 tras prorrogar | 98.6301 % | [92.6401, 99.7578] | 90 a … | pasa |

## Criterio

- **exp_lento:** 4
- **pago4_min:** 10
- **pago4_max:** 60
- **pago5_min:** 60
- **pago14_min:** 90

## Requisitos que protege

- El lento no es imposible ni trivial; la prórroga no cierra puertas ([[28 §7 Deuda del Acto I y sus nombres]])

## Mutaciones de prueba

- Aguante 27: el lento paga más
  - `economy.energy.per_act.I` = 27, 30

## Relaciones

- **Documentos:** [[28 §7 Deuda del Acto I y sus nombres]], [[28 §13 Validación con el simulador (F0-53)]], [[24 Umbrales de acto]], [[27 Guion del Acto I, día a día]]
- **Bloques de economía:** [[Deuda del Acto I]], [[Energía]]
- **Perfiles:** [[Perfil Lento]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:36`
