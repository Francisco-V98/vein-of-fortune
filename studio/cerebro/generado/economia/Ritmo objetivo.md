---
id: "eco-pace"
tipo: "economia"
title: "Ritmo objetivo"
aliases: ["eco-pace", "economy.pace"]
bloque: "economy.pace"
seccion_doc28: "[[28 §2 Ritmo objetivo y patrimonio]]"
arriba: "[[MOC Economía]]"
fuente: "studio/data/world.json:1198"
generado: true
---

# Ritmo objetivo

> Ingreso neto por hora, Acto I: 650 / 1 100 / 2 200 (lento, medio, rápido)

- **net_income_per_hour:**
  - **I:**
    - **slow:** 650
    - **medium:** 1100
    - **fast:** 2200
  - **II:**
    - **start:** 6300
    - **end:** 10800
    - **target:** 7500
  - **III:**
    - **attentive:** 38700
    - **target:** 33000
  - **IV:**
    - **attentive:** 181000
    - **target:** 110000
- **acts:**
  - **I:**
    - **hours:** 1.5, 3
    - **days:** 7, 7
    - **wealth_end:** 600, 1000
    - **wealth_end_fast:** 2300
  - **II:**
    - **hours:** 4, 10
    - **days:** 18, 46
    - **wealth_end:** 26000
  - **III:**
    - **hours:** 4, 10
    - **days:** 18, 46
    - **wealth_end:** 160000
  - **IV:**
    - **hours:** 3, 6
    - **days:** 14, 28
    - **wealth_end:** 280000
- **sinks_per_act:**
  - **II:** 20000
  - **III:** 100000
  - **IV:** 330000
- **wealth_definition:** efectivo + stock a valor justo; no resta la deuda; no cuentan herramientas, casa, ropa ni auto
- **status_floors:**
  - **comerciante:** 15000
  - **empresario:** 90000
  - **magnate:** 250000
- **status_floors_note:** orden de magnitud; F4-109 fija los finales
- **target_is_act_mean:** sí
- **hour_definition:** tiempo de día de juego (13 min por día, sin escenas ni diálogos)
- **act_ratio_note:** Decisión del autor (2026-10-15): el objetivo de cada acto es su media; el salto I→II puede llegar a ×7 (excepción); si el simulador muestra que las cifras no llegan, propone el ajuste

## Relaciones

- **Documento 28:** [[28 §2 Ritmo objetivo y patrimonio]]
- **Reglas del simulador:**
  - [[A5 Ingreso neto por hora del Acto I]]
  - [[B1 Ritmo por acto de la campaña completa]]
  - [[B2 Crecimiento razonable entre actos]]
  - [[B3 Patrimonio al cierre de cada acto]]
  - [[B4 Los estatus se alcanzan a tiempo]]
  - [[B6 Sumideros recurrentes]]
  - [[B7 La economía no explota tras el Acto IV]]
  - [[B8 El simulador reproduce el prototipo de F0-52]]

## Fuente

`studio/data/world.json:1198`
