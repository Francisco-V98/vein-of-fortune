---
id: "eco-employees"
tipo: "economia"
title: "Empleados"
aliases: ["eco-employees", "economy.employees"]
bloque: "economy.employees"
seccion_doc28: "[[28 §8 Empleados]]"
arriba: "[[MOC Economía]]"
fuente: "studio/data/world.json:1866"
generado: true
---

# Empleados

> 5 niveles; sueldo diario de 70 a 720

- **levels:**
  - level: 1; efficiency_pct: 30; max_tier: 2; salary_per_day: 70
  - level: 2; efficiency_pct: 38; max_tier: 2; salary_per_day: 90
  - level: 3; efficiency_pct: 42; max_tier: 3; salary_per_day: 200
  - level: 4; efficiency_pct: 46; max_tier: 4; salary_per_day: 600
  - level: 5; efficiency_pct: 50; max_tier: 4; salary_per_day: 720
- **never_extract:** [[Aetherita]]
- **support_salary_per_day:**
  - **dependiente:**
    - **II:** 160
    - **III:** 620
    - **IV:** 2800
  - **refinador_equals:** dependiente
  - **guardia_pct_of_dependiente:** 60
  - **analista_pct_of_dependiente:** 140
  - **analista:**
    - **III:** 900
    - **IV:** 3900
- **contract_salary_mult:**
  - **7:** 1.3
  - **14:** 1.12
  - **30:** 1
- **dismissal_phi:**
  - **7:** 0.25
  - **14:** 0.4
  - **30:** 0.6
- **training:**
  - **salary_days_multiplier:** 8
  - **sick_days:** 3
  - **auto_level_every_days_worked:** 40
- **hire_channels:**
  - id: periodico; salary_days: 3; salary_mult: 1
  - id: anuncio; salary_days: 6; salary_mult: 1; candidates: 1, 3; days: 2, 4
  - id: bolsa-union; salary_days: 10; salary_mult: 1.15
- **max_staff_by_store_level:** 0, 2, 3, 5, 7
- **max_miners_by_store_level:** 0, 1, 2, 3, 4
- **zone_wear_per_expedition:**
  - **formula:** 6 x eficiencia
- **risk:**
  - **by_zone:**
    - **galerias-hollin:**
      - **injury_pct:** 1.5
      - **sick_days:** 3
      - **lose_load_pct:** 2.3
    - **canon-ferroso:**
      - **injury_pct:** 3
      - **sick_days:** 3
      - **lose_load_pct:** 4.5
    - **sierra-alta:**
      - **injury_pct:** 4
      - **sick_days:** 3
      - **lose_load_pct:** 6
    - **salares:**
      - **injury_pct:** 4
      - **sick_days:** 3
      - **lose_load_pct:** 6
    - **cavernas:**
      - **injury_pct:** 7
      - **sick_days:** 5
      - **lose_load_pct:** 10.5
    - **fosa:**
      - **injury_pct:** 12
      - **sick_days:** 8
      - **lose_load_pct:** 18
  - **care_reduction_max:** 2
  - **guard_halves:** sí
  - **loyalty_theft_pct_per_week:**
    - **baja:** 6
    - **media:** 1.5
    - **alta:** 0.3
  - **theft_pct_of_day_value:** 15
- **act_IV_role:** residual
- **miner_assignment:**
  - **expeditions_per_day:** 1
  - **zone:** asignada por el jugador
  - **salary_follows_level:** sí
  - **nota:** Decisión del autor (2026-10-15): un Minero hace una expedición al día en la zona que le asigna el jugador; al subir de nivel (entrenamiento o cada 40 días trabajados) el salario sigue al nivel (renegociación automática)
- **candidates:**
  - **loyalty_pct:**
    - **baja:** 25
    - **media:** 55
    - **alta:** 20
  - **level_pct_by_act:**
    - **II:**
      - **1:** 60
      - **2:** 40
    - **III:**
      - **2:** 20
      - **3:** 50
      - **4:** 30
    - **IV:**
      - **3:** 20
      - **4:** 50
      - **5:** 30
  - **nota:** Propuesta del simulador (F0-53): reparto de la Lealtad (oculta) y del nivel de los candidatos que llegan por el anuncio o la Bolsa de la Unión
- **support_roles:**
  - **dependiente_frees_shop_block:** sí
  - **refinador_added_value:** 0
  - **analista_only_cost:** sí
  - **nota:** El Dependiente libera el bloque de tienda; el Refinador no añade valor hasta que exista el refinado (F3-07); el Analista solo cuesta (aporta la capa 3 de información)
- **act_IV_warning:**
  - **warn_before_sending_to_depleted_zone:** sí
  - **shows_estimated_loss:** sí
  - **player_can_still_decide:** sí
  - **nota:** Decisión del autor (2026-10-16): en el Acto IV el juego avisa, con la pérdida estimada, antes de mandar a un Minero a una zona agotada, pero deja decidir al jugador. Sin el aviso, un Minero en La Fosa o las Cavernas resta ≈ 10 000 esquirlas al día (F0-53)

## Relaciones

- **Documento 28:** [[28 §8 Empleados]]
- **Reglas del simulador:** [[G1 El empleado no domina - salario frente a aporte]], [[G2 La plantilla máxima no domina]], [[G3 El jugador ausente rinde menos]], [[G4 El Dependiente aporta, pero poco]], [[G5 Entrenar y ascender no es un bucle]], [[G6 Riesgo de los empleados]]
- **Relacionado:** [[Sede de la Unión]]

## Fuente

`studio/data/world.json:1866`
