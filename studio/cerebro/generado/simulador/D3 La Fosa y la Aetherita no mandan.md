---
id: "sim-D3"
tipo: "regla-sim"
title: "La Fosa y la Aetherita no mandan"
aliases: ["sim-D3"]
grupo: "D · Zonas"
estado: "pasa"
origen: "prop."
valor: 3
unidad: "exp"
documentos: ["[[28 §1 Escalas]]", "[[28 §3 Los diez minerales]]", "[[26 Zonas y edificios]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:323"
generado: true
---

# La Fosa y la Aetherita no mandan

> D · Zonas · pasa · ≤ 3 por semana · Aetherita ≤ 60 % de las ventas

**Grupo:** D · Zonas · **Origen del umbral:** propuesta del simulador

## Qué mide

expediciones a La Fosa por semana y parte de la Aetherita en las ventas del Acto IV

## Umbral

≤ 3 por semana · Aetherita ≤ 60 % de las ventas

## Resultado

Estado: **pasa**. expediciones a La Fosa en una semana (máximo): **3 exp** (IC95 –, n = 16).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 55.705 | [54.9564, 56.4536] | 16 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| expediciones a La Fosa en una semana (máximo) | 3 exp | [3, 3] | … a 3 | pasa |
| parte de la Aetherita en las ventas del Acto IV | 55.705 % | [54.9564, 56.4536] | … a 60 | pasa |

## Criterio

- **fosa_semana_max:** 3
- **aeth_max:** 60

## Requisitos que protege

- La Fosa abre tres días por semana; la Aetherita no domina ([[28 §1 Escalas]])
- Aetherita del Acto IV: canal legal con tope; negro solo en encargos especiales ([[03 Comercio y mercado]])

## Mutaciones de prueba

- Aetherita a 60 000 esquirlas: domina las ventas del IV
  - `minerals.aetherita.base_price` = 60000

## Relaciones

- **Documentos:** [[28 §1 Escalas]], [[28 §3 Los diez minerales]], [[26 Zonas y edificios]]
- **Bloques de economía:** [[Moneda]], [[Punto de mercado]], [[Tiempo]], [[Calendario]], [[Expediciones]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:323`
