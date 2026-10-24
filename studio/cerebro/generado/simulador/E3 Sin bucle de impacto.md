---
id: "sim-E3"
tipo: "regla-sim"
title: "Sin bucle de impacto"
aliases: ["sim-E3"]
grupo: "E · Mercado y bucles"
estado: "pasa"
origen: "doc"
valor: -5.8488
unidad: "%"
documentos: ["[[03 Comercio y mercado]]", "[[28 §6 Frenos de mercado]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:363"
generado: true
---

# Sin bucle de impacto

> E · Mercado y bucles · pasa · < 0 en todo el rango

**Grupo:** E · Mercado y bucles · **Origen del umbral:** documento aprobado

## Qué mide

ganancia de vender y recomprar, o de comprar, esperar hasta 8 bloques y vender

## Umbral

< 0 en todo el rango

## Resultado

Estado: **pasa**. mayor ganancia media de un bucle de impacto (acto III, espera 0 bloques): **-5.8488 %** (IC95 [-5.8788, -5.8187], n = 5004).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| mayor ganancia media de un bucle de impacto (acto III, espera 0 bloques) | -5.8488 % | [-5.8788, -5.8187] | … a 0 | pasa |

## Requisitos que protege

- No existe ganancia segura entre canales (tienda y pedidos solo con mercancía propia) ([[03 Comercio y mercado]])
- El impacto del jugador no crea bucles de ganancia ([[03 Comercio y mercado]])

## Mutaciones de prueba

- Sin impuesto ni spread: la ida y vuelta no pierde
  - `economy.market.sale_tax_pct` = 0
  - `minerals.carbon.spread` = 0
  - `minerals.hierro.spread` = 0
  - `minerals.cobre.spread` = 0
  - `minerals.salitre.spread` = 0
  - `minerals.plata.spread` = 0
  - `minerals.cuarzo.spread` = 0
  - `minerals.oro.spread` = 0
  - `minerals.esmeralda.spread` = 0
  - `minerals.diamante.spread` = 0

## Relaciones

- **Documentos:** [[03 Comercio y mercado]], [[28 §6 Frenos de mercado]]
- **Bloques de economía:** [[Mercado]], [[Deriva guionizada del Acto I]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:363`
