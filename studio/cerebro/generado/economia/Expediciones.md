---
id: "eco-expedition"
tipo: "economia"
title: "Expediciones"
aliases: ["eco-expedition", "economy.expedition"]
bloque: "economy.expedition"
seccion_doc28: "[[28 §1 Escalas]]"
arriba: "[[MOC Economía]]"
fuente: "studio/data/world.json:1099"
generado: true
---

# Expediciones

> 1 bloque normal y 2 profunda; hasta 3 normales al día

- **normal_blocks:** 1
- **deep_blocks:** 2
- **max_normal_per_day:** 3
- **fixed_seconds:** 100
- **seconds_per_ore:** 20
- **minigame_seconds:** 8, 15
- **ores_per_expedition:**
  - **I:** 2, 3
  - **II:** 4, 4
  - **III_normal:** 7
  - **III_deep:** 8, 9
  - **IV_deep:** 8, 9
  - **soft_cap_per_block:** 10
- **act1_expeditions_in_script:** 5
- **result_multipliers:**
  - **perfecto:** 1.5
  - **bueno:** 1
  - **regular:** 0.5
  - **fallo:** 0
- **result_probs:**
  - **lento:** 5, 40, 35, 20
  - **medio:** 15, 50, 25, 10
  - **rapido:** 30, 50, 15, 5
- **deep_energy_mult:** 1.8
- **deep_load_mult:** 1.5
- **zone_wealth:**
  - **min:** 40
  - **max:** 100
  - **per_expedition:** -6
  - **per_day:** 3
  - **full_regen_days:** 20
  - **avg_at_exit_pct:**
    - **II:** 59
    - **III:** 65
    - **IV:** 94
- **aetherita:**
  - **minigame:** [[Contención]]
  - **tool_min_level:** 5
  - **tool_types:** taladro, cincel
  - **filter_cost_per_expedition:** 400
  - **employees_can_extract:** no
  - **legal_channel:**
    - **buyer:** [[Comisión del Éter]]
    - **from_act:** IV
    - **max_vials_per_day:** 5
    - **price_mult_of_fair:** 1
    - **sale_tax_applies:** sí
    - **slippage:** no
    - **vigilance:** 0
    - **nota:** Decisión del autor (2026-10-15 y 2026-10-16): en el Acto IV la Comisión del Éter compra Aetherita por el canal legal, con un tope diario de viales, en una oficina de Puerto Meridiano siempre abierta. El precio (valor justo, sin prima) y el impuesto son la propuesta del simulador (F0-53), aprobada
    - **location:** [[Puerto Meridiano]]
    - **always_open:** sí
    - **description:** Oficina de la Comisión del Éter en Puerto Meridiano, siempre abierta; compra hasta 5 viales al día a valor justo, sin prima
- **ore_discard:**
  - **energy_pct_of_ore:** 25
  - **nota:** Decisión del autor (2026-10-15): descartar una mena escaneada (la que no quieres o la que tu herramienta no puede extraer) cuesta el 25 % de la energía que habría costado extraerla

## Relaciones

- **Documento 28:** [[28 §1 Escalas]]
- **Reglas del simulador:** [[D3 La Fosa y la Aetherita no mandan]]
- **Relacionado:** [[Contención]], [[Comisión del Éter]]

## Fuente

`studio/data/world.json:1099`
