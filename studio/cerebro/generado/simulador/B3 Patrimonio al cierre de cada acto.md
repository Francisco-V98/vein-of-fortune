---
id: "sim-B3"
tipo: "regla-sim"
title: "Patrimonio al cierre de cada acto"
aliases: ["sim-B3"]
grupo: "B · Ritmo, progresión y estatus"
estado: "pasa"
origen: "doc"
valor: 693.4794
unidad: "esq"
documentos: ["[[28 §2 Ritmo objetivo y patrimonio]]", "[[04 Progresión y meta]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:135"
generado: true
---

# Patrimonio al cierre de cada acto

> B · Ritmo, progresión y estatus · pasa · Acto I dentro de 600–1 000 (rápido ±25 % de 2 300) · II, III, IV ±25 % · sumideros ±40 % ·

**Grupo:** B · Ritmo, progresión y estatus · **Origen del umbral:** documento aprobado

## Qué mide

patrimonio (efectivo + stock) al cerrar cada acto frente al objetivo; sumideros por acto

## Umbral

Acto I dentro de 600–1 000 (rápido ±25 % de 2 300) · II, III, IV ±25 % · sumideros ±40 % · lento ≥ 50 % del medio

## Resultado

Estado: **pasa**. patrimonio al cierre del Acto I (medio), en esquirlas: **693.4794 esq** (IC95 [686.9664, 699.9924], n = 6000).

| Perfil | Valor | IC95 | n |
|---|---|---|---|
| [[Perfil Medio\|medio]] | 244974.9668 | – | – |
| [[Perfil Lento\|lento]] | 80.1305 | [77.0792, 83.1819] | 60 |

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| patrimonio al cierre del Acto I (medio), en esquirlas | 693.4794 esq | [686.9664, 699.9924] | 600 a 1000 | pasa |
| patrimonio al cierre del Acto I (rápido), desviación | 1.5136 % | [1.1522, 1.875] | … a 25 | pasa |
| patrimonio al cierre del Acto II (medio), desviación | 17.5294 % | [13.5043, 21.5544] | … a 25 | pasa |
| patrimonio al cierre del Acto III (medio), desviación | 1.8441 % | [0, 6.1085] | … a 25 | pasa |
| patrimonio al cierre del Acto IV (medio), desviación | 12.5089 % | [9.5196, 15.4983] | … a 25 | pasa |
| sumideros del Acto II frente al objetivo, desviación | 35.1955 % | [34.1351, 36.256] | … a 40 | pasa |
| sumideros del Acto III frente al objetivo, desviación | 6.1211 % | [5.6997, 6.5424] | … a 40 | pasa |
| sumideros del Acto IV frente al objetivo, desviación | 23.9285 % | [18.3601, 29.4968] | … a 40 | pasa |
| patrimonio del lento frente al medio (peor acto) | 80.1305 % | [77.0792, 83.1819] | 50 a … | pasa |

## Criterio

- **desv_max:** 25
- **lento_min:** 50
- **sumideros_max:** 40

## Requisitos que protege

- Patrimonio al cierre de cada acto ([[28 §2 Ritmo objetivo y patrimonio]])

## Mutaciones de prueba

- Patrimonio objetivo del IV de 50 000
  - `economy.pace.acts.IV.wealth_end` = 50000

## Relaciones

- **Documentos:** [[28 §2 Ritmo objetivo y patrimonio]], [[04 Progresión y meta]]
- **Bloques de economía:** [[Ritmo objetivo]], [[Guion económico del Acto I]]
- **Perfiles:** [[Perfil Medio]], [[Perfil Lento]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:135`
