---
id: "eco-market"
tipo: "economia"
title: "Mercado"
aliases: ["eco-market", "economy.market"]
bloque: "economy.market"
seccion_doc28: "[[28 §6 Frenos de mercado]]"
arriba: "[[MOC Economía]]"
fuente: "studio/data/world.json:1634"
generado: true
---

# Mercado

> Impuesto de venta 3 %; eventos de 2 a 12 puntos

- **event_base_points:**
  - **menor:** 2
  - **medio:** 5
  - **mayor:** 8
  - **extremo:** 12
- **event_categories:** produccion, politica, laboral, tecnologico, clima, guerra, moda_lujo, descubrimiento
- **sectors:** ferrocarril, energia, militar, agricultura, lujo, tecnologia
- **noise_persistence_per_block:** 0.7
- **event_decay_per_day:** 0.15
- **sale_tax_pct:** 3
- **black_market_tax_pct:** 0
- **bolsa:**
  - **act:** III
  - **spread_mult:** 0.5
  - **sale_tax_pct:** 0
  - **place:** Puerto Meridiano
- **slippage:**
  - **formula:** caida_pct = w*q/(L*D) por tanda
  - **depth_by_act:**
    - **I:** 1
    - **II:** 1.5
    - **III:** 2.5
    - **IV:** 4
  - **buyers_npc_by_act:**
    - **I:** 2
    - **II:** 3
    - **III:** 5
    - **IV:** 8
- **player_impact:**
  - **w_min:** 0.5
  - **w_span:** 3.5
  - **w_half_wealth:** 400000
  - **w_max:** 4
  - **by_act:**
    - **I:** 0.5
    - **II:** 0.6
    - **III:** 1
    - **IV:** 1.6
  - **recovery_per_block:** 0.25
- **marketplace_markup:** 1.18
- **store:**
  - **list_markup:** 1.2
  - **avg_client_markup:** 1.15
  - **slippage:** no
  - **units_per_block:** 16, 40, 60, 80, 100
  - **own_goods_only:** sí
  - **client_markup_by_skill:**
    - **lento:** 1.08
    - **medio:** 1.15
    - **rapido:** 1.2
  - **own_goods_note:** Decisión del autor (2026-10-15): la tienda y los pedidos solo aceptan mercancía propia (extraída o refinada); no se compra al mercado para revender en la tienda o en un pedido
- **licenses:**
  - **renewal_days:** 28
  - **minero:** 150
  - **comerciante:** 900
  - **empresario:** 4500
  - **magnate:** 17000
- **storage_min_fee_per_lot_day:** 1
- **warehouse:**
  - level: 0; name: Trastienda; capacity: 40; rent_per_day: 0; cost: 0
  - level: 1; capacity: 120; rent_per_day: 15; cost: 1500
  - level: 2; capacity: 300; rent_per_day: 50; cost: 7000
  - level: 3; capacity: 700; rent_per_day: 150; cost: 35000
  - level: 4; capacity: 1600; rent_per_day: 450; cost: 160000
  - level: 5; capacity: 3500; rent_per_day: 1200; cost: 600000
- **loose_events:**
  - **prob_pct_per_mineral_day:** 8
  - **magnitude_weights:**
    - **menor:** 40
    - **medio:** 30
    - **mayor:** 20
    - **extremo:** 10
  - **nota:** Eventos sueltos de un solo mineral (sin sector): probabilidad por mineral y día, magnitud entre event_base_points; signo al azar. Fijado desde el prototipo de F0-52
- **buyer_cap_excess_slippage_mult:** 3

## Relaciones

- **Documento 28:** [[28 §6 Frenos de mercado]]
- **Reglas del simulador:** [[B6 Sumideros recurrentes]], [[E1 Sin ganancia segura entre canales]], [[E2 Impacto del jugador en el precio]], [[E3 Sin bucle de impacto]], [[E6 Tope por comprador y capacidad del almacén]]

## Fuente

`studio/data/world.json:1634`
