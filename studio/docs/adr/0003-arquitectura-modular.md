# ADR-0003 · Arquitectura modular por cortes verticales y capas

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Contexto

El autor exige un proyecto muy modular, sin dependencias directas, escalable, con independencia entre partes y buenas prácticas de diseño y desarrollo.

## Decisión

Cada funcionalidad es un **módulo** con capas `domain`, `application`, `infrastructure`, `presentation` y `api`. Las dependencias apuntan hacia el dominio. Un módulo solo usa la `api` de otro y debe declararlo en `architecture.json`. Entrada, almacenamiento, audio, idioma y reloj son **puertos** con adaptadores. Una **raíz de composición** (`app`) conecta todo. El cumplimiento se verifica automáticamente.

## Alternativas consideradas

- **Estructura por tipo técnico** (todas las escenas juntas, todos los scripts juntos): simple al inicio, pero acopla todo y no escala.
- **ECS puro:** potente para simulaciones masivas, innecesario aquí y poco natural en Godot.
- **Nodos y señales sin capas:** rápido para empezar, pero mezcla reglas con interfaz y dificulta probar.

## Consecuencias

Más disciplina y carpetas al inicio a cambio de poder cambiar un módulo sin romper otros, probar el dominio sin Godot y sumar plataformas o funciones sin tocar lo existente. Hay que validar el patrón con código real en la Fase 1.

## Enmienda (2026-10-24, F0-57)

La raíz de composición también aloja los **puentes de composición** (`app/puentes/`): implementan puertos que un módulo declara para recibir datos de otros sin depender de ellos, usando solo sus `api` y sin reglas del juego. Lo introduce [ADR-0012](0012-modulo-tutorial-y-logros-en-progression.md) para el módulo `tutorial` y la cola de `story`. La validación con código real sigue en la Fase 1 (F1-28, F1-30, F1-33).
