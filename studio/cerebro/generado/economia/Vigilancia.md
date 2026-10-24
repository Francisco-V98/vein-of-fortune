---
id: "eco-surveillance"
tipo: "economia"
title: "Vigilancia"
aliases: ["eco-surveillance", "economy.surveillance"]
bloque: "economy.surveillance"
seccion_doc28: "[[28 §10 Vigilancia, multas, mercado negro y mora]]"
arriba: "[[MOC Economía]]"
fuente: "studio/data/world.json:2326"
generado: true
---

# Vigilancia

> Niveles: tranquilo, observado, vigilado, bajo-investigacion

- **levels:**
  - id: tranquilo; min: 0; max: 29
  - id: observado; min: 30; max: 59
  - id: vigilado; min: 60; max: 84
  - id: bajo-investigacion; min: 85; max: 100
- **per_operation:**
  - **base:** 4
  - **span:** 8
  - **formula:** 4 + 8 * (valor de la operacion / tope nocturno)
  - **min:** 4
  - **max:** 12
- **natural_decay_per_day:** 2
- **faroleros_rate_mult:** 0.8
- **night_volume_cap:**
  - **II:** 3300
  - **III:** 12000
  - **IV:** 55000
- **bribe_quiroga:**
  - **base:** 500
  - **pct_of_wealth:** 0.8
  - **growth:** 1.35
  - **vigilance:** -15
  - **counter_drops_every_days:** 56
  - **counter_drop:** 1
- **other_reductions:**
  - **favor_retiro:** -10
  - **promesa:** -5
  - **sello:** -10
- **guard_extra_decay_per_day:** 0.25
- **guard_max:** 3
- **fines:**
  - **observado:**
    - **inspection_pct:** 20
    - **fine_pct_wealth:** 1
    - **fine_min:** 60
  - **vigilado:**
    - **inspection_pct:** 50
    - **fine_pct_wealth:** 3
    - **fine_min:** 300
    - **seizure_pct:** 25
    - **official_contracts_blocked:** sí
- **raid:**
  - **at:** 85
  - **fine_pct_wealth:** 6
  - **fine_min:** 600
  - **store_closed_days:** 2
  - **black_market_closed_days:** 7
  - **vigilance_after:** 60
  - **seizes_night_lot_and_black_stock:** sí
  - **arrest:**
    - **lost_days:** 1
    - **probability_pct:** 25
    - **difficulties:** dificil, hardcore
- **black_market_net_weekly_pct:**
  - **prudent:** 7, 8
  - **reckless:** -12, -8
- **aetherita_special_orders:**
  - **from_act:** IV
  - **every_days:** 21
  - **vials:** 1, 2
  - **premium_pct:** 30
  - **vigilance:** 8
  - **routine:** no
  - **nota:** Decisión del autor (2026-10-15): la Aetherita solo entra en el mercado negro como encargo especial (con trasfondo e historia), raro, de poco volumen y a veces una compra sin mucho detalle; nunca un canal rutinario ni de grandes cantidades. Frecuencia, viales y vigilancia son la propuesta del simulador (F0-53)
  - **casilda_variant:**
    - **every_days:** 14
    - **premium_bonus_points:** 10, 15
    - **nota:** Decisión del autor (2026-10-16): si Casilda es la compradora elegida en el final, los encargos especiales de Aetherita del negro llegan cada ≈ 14 días en vez de ≈ 21 (con más historia); la prima sigue en +10 a +15 puntos sobre la base

## Relaciones

- **Documento 28:** [[28 §10 Vigilancia, multas, mercado negro y mora]]
- **Reglas del simulador:** [[F1 Mercado negro prudente]], [[F2 Barrido de políticas del mercado negro]], [[F3 El mercado negro abusivo pierde]], [[F4 Aetherita en el Acto IV - canal legal con tope]], [[F5 Cuánto cuesta una noche negra en bloques]]
- **Relacionado:** [[Inspector Quiroga]], [[Oficina del Inspector]], [[Los Faroleros]]

## Fuente

`studio/data/world.json:2326`
