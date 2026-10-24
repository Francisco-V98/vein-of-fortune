---
id: "sim-B2"
tipo: "regla-sim"
title: "Crecimiento razonable entre actos"
aliases: ["sim-B2"]
grupo: "B · Ritmo, progresión y estatus"
estado: "pasa"
origen: "doc"
valor: 1.0
unidad: ""
documentos: ["[[28 §2 Ritmo objetivo y patrimonio]]", "[[28 §13 Validación con el simulador (F0-53)]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:119"
generado: true
---

# Crecimiento razonable entre actos

> B · Ritmo, progresión y estatus · pasa · I < II < III < IV · razones 3–5 (I→II hasta 7) · rampa ≤ ×3,5

**Grupo:** B · Ritmo, progresión y estatus · **Origen del umbral:** documento aprobado

## Qué mide

razones de ritmo entre actos y rampa dentro de cada acto

## Umbral

I < II < III < IV · razones 3–5 (I→II hasta 7) · rampa ≤ ×3,5

## Resultado

Estado: **pasa**. crece I < II < III < IV (1 = sí): **1 ** (IC95 –, n = –).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 6.7206 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| crece I < II < III < IV (1 = sí) | 1  | [1, 1] | 1 a 1 | pasa |
| razón I→II | 6.7206 x | [6.7206, 6.7206] | 3 a 7 | pasa |
| razón II→III | 4.0694 x | [3.9708, 4.168] | 3 a 5 | pasa |
| razón III→IV | 3.4403 x | [3.2849, 3.5957] | 3 a 5 | pasa |
| rampa fin/inicio dentro de un acto (peor: II) | 2.538 x | [2.3129, 2.7631] | … a 3.5 | pasa |

## Criterio

- **razon_min:** 3
- **razon_max:** 5
- **razon_12_max:** 7
- **rampa_max:** 3.5
- **tramo_div:** 4

## Requisitos que protege

- Ritmo por acto 1 100 · 7 500 · 27 000 · 125 000 (la media del acto) ([[28 §2 Ritmo objetivo y patrimonio]])

## Mutaciones de prueba

- Aguante del Acto III de 20: el III deja de crecer
  - `economy.energy.per_act.III` = 20

## Relaciones

- **Documentos:** [[28 §2 Ritmo objetivo y patrimonio]], [[28 §13 Validación con el simulador (F0-53)]]
- **Bloques de economía:** [[Ritmo objetivo]], [[Guion económico del Acto I]], [[Energía]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:119`
