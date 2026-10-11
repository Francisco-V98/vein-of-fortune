# ADR-0002 · Repositorio con game/ y studio/ separados

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Contexto

El juego y su gestión (documentos, roadmap, tareas, arte de referencia, hub) deben poder separarse, ignorarse o extraerse sin romper nada.

## Decisión

Un solo repositorio con dos mundos independientes: `game/` compila sin `studio/` y `studio/` no importa nada de `game/`. `tools/` contiene herramientas neutrales para ambos.

## Alternativas consideradas

- **Dos repositorios desde el inicio:** más aislamiento, pero más fricción para un proyecto de una persona.
- **Todo mezclado:** más simple, pero imposible de separar después.

## Consecuencias

`studio/` se puede ignorar (`git sparse-checkout`) o extraer con su historial (`git subtree split`); ambos probados en local.
