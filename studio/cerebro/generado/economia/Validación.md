---
id: "eco-validation"
tipo: "economia"
title: "Validación"
aliases: ["eco-validation", "economy.validation"]
bloque: "economy.validation"
seccion_doc28: "[[28 §13 Validación con el simulador (F0-53)]]"
arriba: "[[MOC Economía]]"
fuente: "studio/data/world.json:2542"
generado: true
---

# Validación

> Verificado en F0-53; última simulación: tools/sim/run.py --completo (2026-10-16; resultados en studio/data/sim/resultados.json)

- **last_simulated:** tools/sim/run.py --completo (2026-10-16; resultados en studio/data/sim/resultados.json)
- **verified_in:** F0-53
- **results_file:** studio/data/sim/resultados.json
- **rules_file:** studio/data/sim/reglas.json
- **assumptions_file:** studio/data/sim/supuestos.json
- **checks:** cuota del dia 7, ritmo por acto, ninguna zona siempre optima, mejorar no se paga en una expedicion, via de deuda alcanzable, empleado no domina, sin ganancia segura, topes de volatilidad, mercado negro, reparar, descartar menas, Aetherita con canal legal, tienda y pedidos con mercancia propia, mision de rescate
- **summary:** 50 de 50 reglas de equilibrio pasan con las cifras aprobadas el 2026-10-16 (resultados en studio/data/sim/resultados.json)

## Relaciones

- **Documento 28:** [[28 §13 Validación con el simulador (F0-53)]]
- **Reglas del simulador:**
  - [[A1 Cuota del día 7 sin mejora]]
  - [[A2 Ahorrar o mejorar el día 5]]
  - [[A3 El lento no es imposible ni trivial]]
  - [[A4 El rápido paga con holgura]]
  - [[B2 Crecimiento razonable entre actos]]
  - [[B8 El simulador reproduce el prototipo de F0-52]]
  - [[D1 Ninguna zona es siempre la óptima]]
  - [[E4 La especulación no domina]]
- **Relacionado:** [[MOC Simulador]]

## Fuente

`studio/data/world.json:2542`
