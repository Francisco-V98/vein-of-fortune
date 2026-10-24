---
id: "eco-debt"
tipo: "economia"
title: "Deuda del Acto I"
aliases: ["eco-debt", "economy.debt"]
bloque: "economy.debt"
seccion_doc28: "[[28 §7 Deuda del Acto I y sus nombres]]"
arriba: "[[MOC Economía]]"
fuente: "studio/data/world.json:1776"
generado: true
---

# Deuda del Acto I

> Principal 24 000, interés 4 % al mes, primer pago 960 el día 7

- **principal:** 24000
- **start_cash:** 120
- **interest_monthly_pct:** 4
- **interest_weekly_pct:** 1
- **amortization_weekly:** 720
- **first_due_day:** 7
- **first_payment:** 960
- **payment_day_14:** 953
- **anonymous_payment:**
  - **amount_per_month:** 400
  - **first_day:** 14
  - **period_days:** 28
  - **interest_only:** sí
  - **credit_per_week:** 100
  - **weeks:** 4
  - **amortizes_capital:** no
- **early_payment:**
  - **from_day:** 4
  - **interest_pp:** -1
- **quiroga_management:**
  - **fee:** 240
  - **financed_by_reme:** sí
  - **interest_pct:** 0
  - **counts_in_principal:** no
  - **paid_with_next_installment:** sí
- **surcharge_pct_per_week:**
  - **novato:** 4
  - **intermedio:** 6
  - **dificil:** 12
  - **hardcore:** 18
- **surcharge_cap_weeks:** 3
- **late_installment:**
  - **novato:** desplaza la serie 1 semana
  - **intermedio:** desplaza la serie 1 semana
  - **dificil:** se suma a la del dia 14
  - **hardcore:** se suma a la del dia 14
- **mora:**
  - **weeks_late:** 4
  - **interest_pp:** 1
  - **reme_stops_financing:** sí
  - **closes_doors:** no
- **advance_installment:**
  - **on_time_fraction:** 0.5
  - **after_extension_fraction:** 1
  - **credited:** sí
  - **counts_for_route:** sí
  - **extra_cost:** 0
- **extra_light_fee:** 960
- **light_debt:**
  - **amount:** 3600
  - **interest_pct:** 0
  - **growth_monthly_pct:** 2
  - **counts_for_route:** no
- **reme_faction_loan:** 150000
- **bought_debt_same_principal:** sí
- **other_amounts:**
  - **small_management:** 400
  - **delivery_fee_pct_of_volume:** 10
  - **pay_management_discount_pct:** 30
  - **pay_management_cost_pct_of_contract:** 5
  - **pay_management_vigilance:** 10
  - **big_income:** 200000
  - **publish_truth:** 60000
- **route:**
  - **base:** principal
  - **counts:** capital amortizado de tu bolsillo
  - **excludes:** intereses, recargos, abonos anonimos, lo que asuma el Consorcio
  - **A5_pct:** 25
  - **A5_amount:** 6000
  - **circle_pct:** 50
  - **circle_amount:** 12000
  - **consortium_cap_pct:** 30
  - **consortium_cap_amount:** 7200

## Relaciones

- **Documento 28:** [[28 §7 Deuda del Acto I y sus nombres]]
- **Reglas del simulador:**
  - [[A1 Cuota del día 7 sin mejora]]
  - [[A3 El lento no es imposible ni trivial]]
  - [[A6 Cuota del día 14 y recargos en las cuatro dificultades]]
  - [[A7 Saldar la deuda antes del día 8 es imposible]]
  - [[H1 Vía de deuda del 25 % en el Acto II]]
  - [[H2 Vía de deuda del 50 % en el círculo]]
  - [[H3 Abonos anónimos y Consorcio]]
  - [[H4 La mora no cierra puertas]]
  - [[H5 Variantes de A2 con el lento]]
- **Relacionado:** [[Reme]], [[Casa de Reme]]

## Fuente

`studio/data/world.json:1776`
