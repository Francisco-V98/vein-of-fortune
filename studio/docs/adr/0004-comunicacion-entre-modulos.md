# ADR-0004 · Comunicación entre módulos por api pública y eventos de dominio

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Contexto

Los módulos deben colaborar sin conocerse por dentro ni crear ciclos.

## Decisión

Dos canales: la **api pública** de cada módulo para preguntas síncronas, y **eventos de dominio** inmutables, definidos por quien los publica, para avisos. Un bus pequeño en `kernel` los entrega. Los eventos no se usan para dar órdenes.

## Alternativas consideradas

- **Señales de Godot entre nodos de módulos distintos:** acoplan la jerarquía de escenas.
- **Autoloads globales como servicios:** cómodos, pero crean dependencias ocultas y dificultan las pruebas.

## Consecuencias

Los módulos se prueban aislados y se reordenan sin romper a otros. Hay que cuidar que los eventos no se conviertan en un grafo oculto; el verificador exige declarar las dependencias.

## Enmienda (2026-10-24, F0-57)

Para que dos módulos colaboren sin crear un ciclo, un módulo puede declarar un puerto que implementa un puente de `app/` sobre la `api` del otro ([ADR-0012](0012-modulo-tutorial-y-logros-en-progression.md)). Los puentes se listan en el documento [14](../14-arquitectura-y-modularidad.md) para que no se conviertan en el grafo oculto que este ADR quiere evitar.
