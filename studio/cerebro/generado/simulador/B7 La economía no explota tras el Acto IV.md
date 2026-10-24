---
id: "sim-B7"
tipo: "regla-sim"
title: "La economía no explota tras el Acto IV"
aliases: ["sim-B7"]
grupo: "B · Ritmo, progresión y estatus"
estado: "pasa"
origen: "prop."
valor: 60.5625
unidad: "%"
documentos: ["[[28 §2 Ritmo objetivo y patrimonio]]", "[[03 Comercio y mercado]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:199"
generado: true
---

# La economía no explota tras el Acto IV

> B · Ritmo, progresión y estatus · pasa · crecimiento ≤ 10 % · identidad exacta · ≤ techo × 1,05

**Grupo:** B · Ritmo, progresión y estatus · **Origen del umbral:** propuesta del simulador

## Qué mide

crecimiento del ingreso diario entre dos ventanas, identidad contable y techo físico

## Umbral

crecimiento ≤ 10 % · identidad exacta · ≤ techo × 1,05

## Resultado

Estado: **pasa**. ingreso semanal máximo frente al techo físico: **60.5625 %** (IC95 –, n = 4).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 1.3219 | [-0.8494, 3.4933] | 4 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| crecimiento del ingreso diario entre las dos ventanas | 1.3219 % | [-0.8494, 3.4933] | … a 10 | pasa |
| identidad contable (diferencia máxima en esquirlas) | 0 esq | [0, 0] | … a 0.5 | pasa |
| ingreso semanal máximo frente al techo físico | 60.5625 % | [60.5625, 60.5625] | … a 100 | pasa |

### Datos adicionales

- **dias:** 10000

## Criterio

- **ventana_a:** 25, 35
- **ventana_b:** 90, 100
- **crec_max:** 10
- **ident_max:** 0.5
- **techo_holgura:** 1.05

## Requisitos que protege

- La economía no explota después del Acto IV ([[28 §2 Ritmo objetivo y patrimonio]])

## Mutaciones de prueba

- El cliente medio de la tienda paga ×30: el ingreso supera el techo físico
  - `economy.market.store.avg_client_markup` = 30

## Relaciones

- **Documentos:** [[28 §2 Ritmo objetivo y patrimonio]], [[03 Comercio y mercado]]
- **Bloques de economía:** [[Ritmo objetivo]], [[Guion económico del Acto I]], [[Mercado]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:199`
