---
id: "sim-E1"
tipo: "regla-sim"
title: "Sin ganancia segura entre canales"
aliases: ["sim-E1"]
grupo: "E · Mercado y bucles"
estado: "pasa"
origen: "doc"
valor: 10.1979
unidad: "% del día"
documentos: ["[[03 Comercio y mercado]]", "[[28 §6 Frenos de mercado]]", "[[28 §3 Los diez minerales]]"]
arriba: "[[MOC Simulador]]"
tags: ["sim/pasa"]
fuente: "studio/data/sim/reglas.json:336"
generado: true
---

# Sin ganancia segura entre canales

> E · Mercado y bucles · pasa · ninguna ganancia fuera del negro · negro ≤ 15 % del ingreso diario

**Grupo:** E · Mercado y bucles · **Origen del umbral:** documento aprobado

## Qué mide

mayor ganancia de comprar (spot, marketplace o bolsa) y revender (spot, bolsa; tienda si no fuera solo mercancía propia); y ganancia diaria sostenible de llenar el lote del mercado negro, limitada por la vigilancia

## Umbral

ninguna ganancia fuera del negro · negro ≤ 15 % del ingreso diario

## Resultado

Estado: **pasa**. mayor ganancia diaria sostenible de comprar para vender en negro (% del ingreso diario): **10.1979 % del día** (IC95 –, n = –).

### Condiciones

| Condición | Valor | IC95 | Límites | Estado |
|---|---|---|---|---|
| mayor ganancia de comprar y revender sin pasar por el mercado negro (% de un bloque) | -0.0584 % bloque | [-0.0584, -0.0584] | … a 0 | pasa |
| mayor ganancia diaria sostenible de comprar para vender en negro (% del ingreso diario) | 10.1979 % del día | [10.1979, 10.1979] | … a 15 | pasa |

### Datos adicionales

- **seguro:** IV, carbon, bolsa, bolsa
- **negro:** II, salitre, spot, 1
- **noche_negra_en_bloques:** 1.8356
- **tienda_y_pedidos_solo_propia:** sí

## Criterio

- **negro_max:** 15

## Requisitos que protege

- No existe ganancia segura entre canales (tienda y pedidos solo con mercancía propia) ([[03 Comercio y mercado]])

## Mutaciones de prueba

- La tienda y los pedidos aceptan mercancía comprada, con regateo ×1,4
  - `economy.market.store.own_goods_only` = no
  - `economy.orders_rules.own_goods_only` = no
  - `economy.market.store.avg_client_markup` = 1.4

## Relaciones

- **Documentos:** [[03 Comercio y mercado]], [[28 §6 Frenos de mercado]], [[28 §3 Los diez minerales]]
- **Bloques de economía:** [[Mercado]], [[Deriva guionizada del Acto I]], [[Reglas de los pedidos]]
- **Tarea:** [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]
- **Resumen de resultados:** [[Resultados del simulador]]

## Fuente

`studio/data/sim/reglas.json:336`
