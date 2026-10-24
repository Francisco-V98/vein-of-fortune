---
id: "sim-H4"
tipo: "regla-sim"
title: "La mora no cierra puertas"
aliases: ["sim-H4"]
grupo: "H · Deuda, mora y rescate"
estado: "pasa"
origen: "prop."
valor: 0.0
unidad: ""
documentos: ["[[28 §7 Deuda del Acto I y sus nombres]]", "[[24 Umbrales de acto]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:633"
generado: true
---

# La mora no cierra puertas

> H · Deuda, mora y rescate · pasa · ≤ 2 · 3 · 4 semanas · Hardcore día 14 ≤ 40 % del ingreso del lento

**Grupo:** H · Deuda, mora y rescate · **Origen del umbral:** propuesta del simulador

## Qué mide

semanas para ponerse al corriente tras 4, 8 y 12 semanas de atraso, en las cuatro dificultades, con el ritmo del lento

## Umbral

≤ 2 · 3 · 4 semanas · Hardcore día 14 ≤ 40 % del ingreso del lento

## Resultado

Estado: **pasa**. algún estado de la mora cierra una puerta (0 = no): **0 ** (IC95 –, n = –).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Lento\|lento]] | 7635.9048 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| semanas para ponerse al corriente tras 4 de atraso (novato) | 1 semanas | [1, 1] | … a 2 | pasa |
| semanas para ponerse al corriente tras 8 de atraso (novato) | 2 semanas | [2, 2] | … a 3 | pasa |
| semanas para ponerse al corriente tras 12 de atraso (novato) | 2 semanas | [2, 2] | … a 4 | pasa |
| semanas para ponerse al corriente tras 4 de atraso (intermedio) | 1 semanas | [1, 1] | … a 2 | pasa |
| semanas para ponerse al corriente tras 8 de atraso (intermedio) | 2 semanas | [2, 2] | … a 3 | pasa |
| semanas para ponerse al corriente tras 12 de atraso (intermedio) | 3 semanas | [3, 3] | … a 4 | pasa |
| semanas para ponerse al corriente tras 4 de atraso (dificil) | 1 semanas | [1, 1] | … a 3 | pasa |
| semanas para ponerse al corriente tras 8 de atraso (dificil) | 2 semanas | [2, 2] | … a 4 | pasa |
| semanas para ponerse al corriente tras 12 de atraso (dificil) | 3 semanas | [3, 3] | … a 5 | pasa |
| semanas para ponerse al corriente tras 4 de atraso (hardcore) | 1 semanas | [1, 1] | … a 3 | pasa |
| semanas para ponerse al corriente tras 8 de atraso (hardcore) | 2 semanas | [2, 2] | … a 4 | pasa |
| semanas para ponerse al corriente tras 12 de atraso (hardcore) | 3 semanas | [3, 3] | … a 5 | pasa |
| cuota del día 14 de Hardcore frente al ingreso semanal del lento | 27.4074 % | [27.4074, 27.4074] | … a 40 | pasa |
| algún estado de la mora cierra una puerta (0 = no) | 0  | [0, 0] | … a 0 | pasa |

### Datos adicionales

- **ingreso_semana_lento:** 7635.9048

## Criterio

- **atrasos:** 4, 8, 12
- **semanas:** 4: 2; 8: 3; 12: 4
- **extra_dificiles:** 1
- **hardcore_max:** 40

## Requisitos que protege

- El lento no es imposible ni trivial; la prórroga no cierra puertas ([[28 §7 Deuda del Acto I y sus nombres]])
- Cuota del día 14 y recargos en las cuatro dificultades ([[28 §7 Deuda del Acto I y sus nombres]])

## Mutaciones de prueba

- La mora cierra puertas
  - `economy.debt.mora.closes_doors` = sí

## Relaciones

- **Documentos:** [[28 §7 Deuda del Acto I y sus nombres]], [[24 Umbrales de acto]]
- **Bloques de economía:** [[Deuda del Acto I]]
- **Perfiles:** [[Perfil Lento]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:633`
