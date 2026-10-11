# ADR-0008 · El QA es una etapa propia del flujo de trabajo

**Estado:** 🟡 Propuesta · **Fecha:** 2026-10-11

## Contexto

El autor exige que el QA (revisiones, pruebas funcionales, seguridad y más) sea un proceso dentro del flujo, no una fase final.

## Decisión

El flujo pasa a `backlog → sprint → doing → review → qa → done`. `review` verifica código y arquitectura; `qa` verifica comportamiento con casos de prueba, regresión, seguridad y rendimiento. Los casos viven en un catálogo con resultados, los errores se registran con severidad y cada versión tiene criterios de salida e informe.

## Alternativas consideradas

- **QA solo antes del lanzamiento:** los errores llegan tarde y cuestan más.
- **QA dentro de `review`:** mezcla dos verificaciones distintas y oculta si una tarea ya fue probada.

## Consecuencias

Cada tarea con comportamiento queda probada antes de cerrarse y deja evidencia. Añade tiempo por tarea; las estimaciones del roadmap incluyen las pruebas y se reservan horas de QA por fase.
