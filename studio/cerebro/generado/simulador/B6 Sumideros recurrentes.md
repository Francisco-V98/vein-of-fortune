---
id: "sim-B6"
tipo: "regla-sim"
title: "Sumideros recurrentes"
aliases: ["sim-B6"]
grupo: "B · Ritmo, progresión y estatus"
estado: "pasa"
origen: "doc"
valor: 3.0516
unidad: "%"
documentos: ["[[28 §2 Ritmo objetivo y patrimonio]]", "[[28 §5 Herramientas]]", "[[28 §6 Frenos de mercado]]", "[[28 §9 Información, viaje, pedidos y contratos]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:177"
generado: true
---

# Sumideros recurrentes

> B · Ritmo, progresión y estatus · pasa · prensa ≈ 1,5 % · licencias 1,5–3 % · viaje 3–5 % (II) y ≈ 1 % (IV) · reparación 7–9 % · re

**Grupo:** B · Ritmo, progresión y estatus · **Origen del umbral:** documento aprobado

## Qué mide

prensa, licencias, viaje, reparación y renta del almacén sobre el ingreso

## Umbral

prensa ≈ 1,5 % · licencias 1,5–3 % · viaje 3–5 % (II) y ≈ 1 % (IV) · reparación 7–9 % · renta ≤ 5 %

## Resultado

Estado: **pasa**. viaje sobre el valor bruto de las expediciones (Acto II): **3.0516 %** (IC95 [3.0301, 3.0731], n = 800).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 1.8315 | – | – |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| prensa sobre el ingreso mensual (Acto II) | 1.8315 % | [1.8216, 1.8414] | 1 a 2.2 | pasa |
| licencia del escalón del acto (comerciante) sobre el ingreso mensual (Acto II) | 1.9223 % | [1.9119, 1.9327] | 1.5 a 3 | pasa |
| licencia del escalón del acto (empresario) sobre el ingreso mensual (Acto III) | 2.3067 % | [2.2887, 2.3246] | 1.5 a 3 | pasa |
| licencia del escalón del acto (magnate) sobre el ingreso mensual (Acto IV) | 2.624 % | [2.6014, 2.6466] | 1.5 a 3 | pasa |
| viaje sobre el valor bruto de las expediciones (Acto II) | 3.0516 % | [3.0301, 3.0731] | 3 a 5 | pasa |
| viaje sobre el valor bruto de las expediciones (Acto IV) | 0.9005 % | [0.8941, 0.9068] | 0.5 a 1.5 | pasa |
| reparación sobre el valor bruto (Acto II) | 7.6101 % | [7.568, 7.6521] | 7 a 9 | pasa |
| reparación sobre el valor bruto (Acto III) | 7.6923 % | [7.6482, 7.7363] | 7 a 9 | pasa |
| reparación sobre el valor bruto (Acto IV) | 7.6533 % | [7.5874, 7.7191] | 7 a 9 | pasa |
| renta del almacén sobre el ingreso mensual (Acto III) | 0.2153 % | [0.2136, 0.217] | … a 5 | pasa |
| renta del almacén sobre el ingreso mensual (Acto IV) | 0.0648 % | [0.0643, 0.0654] | … a 5 | pasa |

## Criterio

- **prensa_min:** 1
- **prensa_max:** 2.2
- **lic_min:** 1.5
- **lic_max:** 3
- **viaje_II_min:** 3
- **viaje_II_max:** 5
- **viaje_IV_min:** 0.5
- **viaje_IV_max:** 1.5
- **rep_min:** 7
- **rep_max:** 9
- **renta_max:** 5

## Requisitos que protege

- Sumideros por acto y recurrentes (prensa, licencias, viaje, reparación, renta) ([[28 §2 Ritmo objetivo y patrimonio]])

## Mutaciones de prueba

- Prensa a un cuarto de precio
  - `economy.information.layers.1.papers.heraldo.subscription` = 60
  - `economy.information.layers.1.papers.voz.subscription` = 60
  - `economy.information.layers.1.papers.teletipo.subscription` = 100

## Relaciones

- **Documentos:** [[28 §2 Ritmo objetivo y patrimonio]], [[28 §5 Herramientas]], [[28 §6 Frenos de mercado]], [[28 §9 Información, viaje, pedidos y contratos]]
- **Bloques de economía:**
  - [[Ritmo objetivo]]
  - [[Guion económico del Acto I]]
  - [[Herramientas]]
  - [[Mercado]]
  - [[Deriva guionizada del Acto I]]
  - [[Información]]
  - [[Viaje]]
  - [[Pedidos]]
  - [[Reglas de los pedidos]]
- **Perfiles:** [[Perfil Medio]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:177`
