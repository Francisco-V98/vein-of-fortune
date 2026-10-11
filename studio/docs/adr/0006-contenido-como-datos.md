# ADR-0006 · El contenido del juego vive en datos validados

**Estado:** 🟡 Propuesta · **Fecha:** 2026-10-11

## Contexto

Minerales, zonas, eventos, noticias y textos son cientos de elementos que cambiarán durante el balance.

## Decisión

El contenido se define en archivos de datos con esquema, identificadores estables y validación al arrancar. El código no contiene números ni textos del juego.

## Alternativas consideradas

- **Constantes en el código:** rápido, pero cada ajuste exige tocar código y se mezcla con la lógica.

## Consecuencias

Se puede equilibrar el juego sin tocar código y la IA puede editar contenido con seguridad. Hay que mantener los esquemas y los validadores.
