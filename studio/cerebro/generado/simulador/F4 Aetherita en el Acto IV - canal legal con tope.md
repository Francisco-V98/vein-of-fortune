---
id: "sim-F4"
tipo: "regla-sim"
title: "Aetherita en el Acto IV: canal legal con tope"
aliases: ["sim-F4"]
grupo: "F · Mercado negro y vigilancia"
estado: "pasa"
origen: "prop."
valor: 2
unidad: "viales"
documentos: ["[[03 Comercio y mercado]]", "[[28 §3 Los diez minerales]]", "[[28 §10 Vigilancia, multas, mercado negro y mora]]", "[[25 Finales y epílogos]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:475"
generado: true
---

# Aetherita en el Acto IV: canal legal con tope

> F · Mercado negro y vigilancia · pasa · legal ≥ 90 % de las ventas · encargo cada ≥ 14 días y ≤ 2 viales · vigilancia ≤ 25 % de la

**Grupo:** F · Mercado negro y vigilancia · **Origen del umbral:** propuesta del simulador

## Qué mide

canal legal con tope; negro solo en encargos especiales raros; la vigilancia no depende de ella

## Umbral

legal ≥ 90 % de las ventas · encargo cada ≥ 14 días y ≤ 2 viales · vigilancia ≤ 25 % de la bajada natural

## Resultado

Estado: **pasa**. encargos especiales: viales por encargo (máximo): **2 viales** (IC95 –, n = –).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 97.7093 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| canal legal de la Aetherita: viales por día (1 = existe y tiene tope) | 5 viales | [5, 5] | 1 a 6 | pasa |
| parte de la Aetherita que se vende por el canal legal | 97.7093 % | [97.7093, 97.7093] | 90 a … | pasa |
| encargos especiales: días entre uno y otro | 21 días | [21, 21] | 14 a … | pasa |
| encargos especiales: viales por encargo (máximo) | 2 viales | [2, 2] | … a 2 | pasa |
| encargos especiales: es un canal rutinario (0 = no) | 0  | [0, 0] | … a 0 | pasa |
| vigilancia diaria que añade la Aetherita frente a la bajada natural | 15.6757 % | [15.6757, 15.6757] | … a 25 | pasa |
| variante Casilda: encargos especiales: días entre uno y otro | 14 días | [14, 14] | 14 a … | pasa |
| variante Casilda: parte de la Aetherita que se vende por el canal legal | 96.3369 % | [96.3369, 96.3369] | 90 a … | pasa |
| variante Casilda: vigilancia diaria que añade la Aetherita frente a la bajada natural | 22.2297 % | [22.2297, 22.2297] | … a 25 | pasa |

## Criterio

- **umbral_politica:** 30
- **tope_max:** 6
- **legal_min:** 90
- **cada_min:** 14
- **viales_max:** 2
- **vig_max:** 25

## Requisitos que protege

- La Fosa abre tres días por semana; la Aetherita no domina ([[28 §1 Escalas]])
- Aetherita del Acto IV: canal legal con tope; negro solo en encargos especiales ([[03 Comercio y mercado]])

## Mutaciones de prueba

- Canal legal de 50 viales al día
  - `economy.expedition.aetherita.legal_channel.max_vials_per_day` = 50

## Relaciones

- **Documentos:** [[03 Comercio y mercado]], [[28 §3 Los diez minerales]], [[28 §10 Vigilancia, multas, mercado negro y mora]], [[25 Finales y epílogos]]
- **Bloques de economía:** [[Vigilancia]], [[Expediciones]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:475`
