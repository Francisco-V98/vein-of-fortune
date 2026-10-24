---
id: "eco-orders"
tipo: "economia"
title: "Pedidos"
aliases: ["eco-orders", "economy.orders"]
bloque: "economy.orders"
seccion_doc28: "[[28 §9 Información, viaje, pedidos y contratos]]"
arriba: "[[MOC Economía]]"
fuente: "studio/data/world.json:2234"
generado: true
---

# Pedidos

> Pedidos: estandar +12 %, urgente +35 %, negro +prima del mineral (20-35) %, largo-plazo +0 %, oficial +8 %

- **niveles:**
  - id: estandar; from_act: I; premium_pct: 12; deadline_days: 3, 7; penalty_pct: I: 0; II: 15; first_qty: 8 sacos de carbon; cadence_days: 2; qty_days_of_production: 1, 2; first_units: 8; first_mineral: [[Carbón]]
  - id: urgente; from_act: I; premium_pct: 35; deadline_days: 1, 3; penalty_pct: I: 5; II: 30; first_qty: 6 de hierro; cadence_days: 7; qty_days_of_production: 0.5, 1; first_units: 6; first_mineral: [[Hierro]]
  - id: negro; from_act: II; premium_pct: prima del mineral (20-35); tax_pct: 0; deadline_days: 2, 4; penalty_pct: 25; vigilance: 8
  - id: largo-plazo; from_act: III; premium_pct: 0; price_fixed_at_signing: sí; deadline_days: 14, 28; penalty_pct: 40; price_drift_pct: 15, 20; cadence_days: 14; qty_days_of_production: 3, 5
  - id: oficial; from_act: III; premium_pct: 8; deadline_days: 7, 14; penalty_pct: 50; vigilance: 10; cadence_days: 14; qty_days_of_production: 1, 2

## Relaciones

- **Documento 28:** [[28 §9 Información, viaje, pedidos y contratos]]
- **Reglas del simulador:** [[B6 Sumideros recurrentes]], [[E7 Los pedidos son un complemento]]
- **Relacionado:** [[Tienda de Villa Brasa]]

## Fuente

`studio/data/world.json:2234`
