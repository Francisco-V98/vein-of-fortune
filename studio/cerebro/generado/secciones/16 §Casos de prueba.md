---
id: "doc-16-casos-de-prueba"
tipo: "seccion"
title: "Casos de prueba ✅"
aliases: ["doc-16-casos-de-prueba"]
documento: "[[16 Calidad y QA]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[16 §Seguridad en QA]]"
siguiente: "[[16 §Errores]]"
arriba: "[[16 Calidad y QA]]"
fuente: "studio/docs/16-calidad-y-qa.md:77"
generado: true
---

# Casos de prueba ✅

← [[16 §Seguridad en QA]] · [[16 Calidad y QA|↑ 16]] · [[16 §Errores]] →

- Viven en `studio/data/qa/cases.json` y se ven en el hub (sección **QA**).
- Cada caso tiene: identificador, área, tipo, nivel (unitaria, integración o manual), si es automático, prioridad, pasos, resultado esperado, tareas relacionadas y último resultado.
- **Resultados:** `not-run`, `pass`, `fail`, `blocked`, `skipped`; cada resultado lleva fecha, versión probada y quién lo ejecutó.
- El catálogo inicial tenía **49 casos** derivados de lo diseñado; con el cambio a PC primero ([[ADR-0009 PC primero (Steam) y móvil después|ADR-0009]]) suma **55**: accesibilidad por teclado (TC-050), Steam Auto-Cloud (TC-051), pantallas de PC (TC-052) y tres casos con la etiqueta **[Fase móvil]** (TC-053 a TC-055, prioridad P3) que conservan lo táctil y lo de Android. Se amplía cada vez que una tarea introduce comportamiento.
- Los casos automáticos se convierten en pruebas del repositorio; los manuales se ejecutan en el PC de pruebas.

## Fuente

`studio/docs/16-calidad-y-qa.md:77`
