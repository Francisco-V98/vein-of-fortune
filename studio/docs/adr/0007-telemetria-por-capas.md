# ADR-0007 · Telemetría local exportable, Play Vitals y envío opcional futuro

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Contexto

Se quiere medir rendimiento, fallos y economía del juego sin conexión y sin romper la privacidad.

## Decisión

Capa A: telemetría local sin datos personales que el probador exporta. Capa B: Google Play Vitals al publicar. Capa C: envío opcional con consentimiento, como idea futura.

## Alternativas consideradas

- **SDK de analíticas de terceros desde el inicio:** más datos, pero recolección y obligaciones legales que no se necesitan.

## Consecuencias

Privacidad por defecto y declaraciones de tienda simples. La telemetría de cierres nativos se detecta con una marca al siguiente arranque.
