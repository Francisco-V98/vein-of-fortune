---
id: "eco-tools"
tipo: "economia"
title: "Herramientas"
aliases: ["eco-tools", "economy.tools"]
bloque: "economy.tools"
seccion_doc28: "[[28 §5 Herramientas]]"
arriba: "[[MOC Economía]]"
fuente: "studio/data/world.json:1329"
generado: true
---

# Herramientas

> 4 tipos, 5 niveles; primer costo del pico 90

- **types:**
  - id: pico; minigame: [[Picado]]; cost_mult: 1; first_cost: 90
  - id: criba; minigame: [[Cribado]]; cost_mult: 1.1; first_cost: 130
  - id: taladro; minigame: [[Perforación]]; cost_mult: 1.25; first_cost: 150
  - id: cincel; minigame: [[Cincelado]]; cost_mult: 1.5; first_cost: 200
- **consumable_types:** explosivo
- **levels:**
  - level: 1; yield_mult: 1; energy_mult: 1; durability: 30; load: 12; scan_width_mult: 1
  - level: 2; yield_mult: 1.25; energy_mult: 0.9; durability: 45; load: 18; scan_width_mult: 0.92
  - level: 3; yield_mult: 1.5; energy_mult: 0.8; durability: 65; load: 26; scan_width_mult: 0.84
  - level: 4; yield_mult: 1.8; energy_mult: 0.7; durability: 90; load: 36; scan_width_mult: 0.76
  - level: 5; yield_mult: 2; energy_mult: 0.6; durability: 120; load: 50; scan_width_mult: 0.68
- **act_levels:**
  - **I:** 1, 2
  - **II:** 2, 3
  - **III:** 3, 4
  - **IV:** 4, 5
- **upgrade_cost_base:**
  - **2:** 480
  - **3:** 1100
  - **4:** 13000
  - **5:** 40000
- **upgrade_cost:**
  - **pico:**
    - **2:** 480
    - **3:** 1100
    - **4:** 13000
    - **5:** 40000
  - **criba:**
    - **2:** 528
    - **3:** 1210
    - **4:** 14300
    - **5:** 44000
  - **taladro:**
    - **2:** 600
    - **3:** 1380
    - **4:** 16250
    - **5:** 50000
  - **cincel:**
    - **2:** 720
    - **3:** 1650
    - **4:** 19500
    - **5:** 60000
- **upgrade_minerals:**
  - **pico:**
    - **2:**
      - **mineral:** [[Hierro]]
      - **qty:** 3
    - **3:**
      - **mineral:** [[Cobre]]
      - **qty:** 6
    - **4:**
      - **mineral:** [[Plata]]
      - **qty:** 8
    - **5:**
      - **mineral:** [[Esmeralda]]
      - **qty:** 6
  - **taladro:**
    - **2:**
      - **mineral:** [[Hierro]]
      - **qty:** 3
    - **3:**
      - **mineral:** [[Cobre]]
      - **qty:** 6
    - **4:**
      - **mineral:** [[Oro]]
      - **qty:** 5
    - **5:**
      - **mineral:** [[Diamante]]
      - **qty:** 5
  - **criba:**
    - **2:**
      - **mineral:** [[Carbón]]
      - **qty:** 8
    - **3:**
      - **mineral:** [[Salitre]]
      - **qty:** 6
    - **4:**
      - **mineral:** [[Cuarzo]]
      - **qty:** 6
    - **5:**
      - **mineral:** [[Esmeralda]]
      - **qty:** 6
  - **cincel:**
    - **2:**
      - **mineral:** [[Hierro]]
      - **qty:** 3
    - **3:**
      - **mineral:** [[Salitre]]
      - **qty:** 6
    - **4:**
      - **mineral:** [[Cuarzo]]
      - **qty:** 6
    - **5:**
      - **mineral:** [[Diamante]]
      - **qty:** 5
- **upgrade_mineral_rule:** el mineral que sube al nivel k tiene tier <= k-1 (se extrae con herramienta de nivel k-1)
- **marketplace_markup:** 1.18
- **repair:**
  - **money_per_point:** 0.9, 1.5, 6, 25, 72
  - **type_mult_as_upgrade:** sí
  - **points_per_part:** 20
  - **part_mineral:** [[Hierro]], [[Hierro]], [[Cobre]], [[Plata]], [[Oro]]
  - **wear_per_ore:**
    - **perfecto:** 0.5
    - **bueno:** 1
    - **regular:** 1.5
    - **fallo:** 3
  - **hardness_per_tier:** 0.2
  - **repair_pct_of_gross:** 7, 9
  - **tools_are_repaired_not_replaced:** sí
  - **broken_is_unusable:** sí
- **explosive:**
  - **wear:** no
  - **from_act:** III
  - **powers:**
    - power: 1; cost: 20; for_tier: 1
    - power: 2; cost: 55; for_tier: 2
    - power: 3; cost: 130; for_tier: 3
    - power: 4; cost: 330; for_tier: 4
    - power: 5; cost: 900; for_tier: 5
  - **result_yield_bonus_pct:**
    - **perfecto:** 80
    - **bueno:** 40
    - **regular:** -20
    - **fallo:** –
  - **fail_loses_ore:** sí
  - **collapse_min_power:** 3
  - **collapse_load_loss_pct:** 35
- **detector:**
  - **base_level:** 1
  - **upgrade_mineral:** [[Cuarzo]]
  - **levels:**
    - level: 1; cost: 0; minerals: 0; width: 20
    - level: 2; cost: 400; minerals: 3; width: 14
    - level: 3; cost: 2500; minerals: 5; width: 9
    - level: 4; cost: 14000; minerals: 8; width: 5
  - **act_level:**
    - **II:** 2
    - **III:** 3
    - **IV:** 4

## Relaciones

- **Documento 28:** [[28 §5 Herramientas]]
- **Reglas del simulador:**
  - [[A2 Ahorrar o mejorar el día 5]]
  - [[B5 El optimizador no se salta el techo de herramienta]]
  - [[B6 Sumideros recurrentes]]
  - [[C1 Cada mejora se paga en pocas expediciones]]
  - [[C2 Cadencia de mejoras]]
  - [[C3 Reparar cuesta 7–9 % del valor bruto]]
  - [[C4 El explosivo apenas compensa]]
- **Relacionado:** [[Picado]], [[Perforación]], [[Cribado]], [[Cincelado]]

## Fuente

`studio/data/world.json:1329`
