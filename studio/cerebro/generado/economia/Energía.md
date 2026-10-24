---
id: "eco-energy"
tipo: "economia"
title: "Energía"
aliases: ["eco-energy", "economy.energy"]
bloque: "economy.energy"
seccion_doc28: "[[28 §4 Energía]]"
arriba: "[[MOC Economía]]"
fuente: "studio/data/world.json:1285"
generado: true
---

# Energía

> Aguante base 28; por acto: I 28–30, II 40, III 62, IV 80

- **base:** 28
- **per_act:**
  - **I:** 28, 30
  - **II:** 40
  - **III:** 62
  - **IV:** 80
- **house_bonus_per_level:** 2
- **house_bonus:** 2, 4, 6, 8
- **tool_energy_mult:** 1, 0.9, 0.8, 0.7, 0.6
- **refill_on_start:** sí
- **zero_energy_returns_partial_load:** sí
- **storage_untouched_on_zero:** sí
- **load_loss_pct:** 35
- **load_loss_cap_pct:** 75
- **load_loss_by_difficulty:**
  - **novato:** 25
  - **intermedio:** 35
  - **dificil:** 49
  - **hardcore:** 70
- **insurance:**
  - **reduces_loss_by:** 0.5
  - **price_pct_of_avg_expedition:** 6
- **consumables_note:** Consumibles de recarga de energía y similares: versiones futuras, sin cifra
- **ramp_fraction_of_act:** 0.7
- **ramp_note:** Fracción del acto en la que el Aguante sube linealmente desde el valor del acto anterior hasta el objetivo del acto (1 = lo alcanza al terminar el acto; 0,5 = a mitad del acto). Supuesto del simulador (F0-53) hasta que F3-11 fije la curva de Aguante

## Relaciones

- **Documento 28:** [[28 §4 Energía]]
- **Reglas del simulador:** [[C5 Descartar una mena tiene un costo real]]

## Fuente

`studio/data/world.json:1285`
