# ADR-0001 · Godot 4.x con GDScript como motor

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Contexto

El juego es 2D en pixel art, con mucha interfaz y lógica de datos, para móvil primero. Se desarrolla con ayuda de IA y el autor tiene poca experiencia de programación.

## Decisión

Se usa **Godot 4.x** con **GDScript**.

> **Enmienda (2026-10-15):** la decisión del motor se mantiene, pero «para móvil primero» deja de ser cierto: el juego se lanza **primero en PC (Windows y Linux, con Steam como meta)** y el móvil llega después de la 1.0. Ver [ADR-0009](0009-pc-primero-movil-despues.md). El texto original se conserva como historial.

## Alternativas consideradas

- **Unity (C#):** más ecosistema y consolas directas, pero proyectos menos legibles para la IA, editor pesado y licencia con condiciones.
- **Otros motores 2D:** menos documentación y menos exportación móvil madura.

## Consecuencias

Proyectos en texto, fáciles de revisar y editar. Exportación a Android e iOS y a PC. La ruta a consolas es menos directa y se reevalúa si pasa a ser prioridad. GDScript no tiene interfaces, lo que condiciona cómo se implementan los puertos ([14](../14-arquitectura-y-modularidad.md)).
