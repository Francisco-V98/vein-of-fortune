# ADR-0007 · Telemetría local exportable, Play Vitals y envío opcional futuro

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Contexto

Se quiere medir rendimiento, fallos y economía del juego sin conexión y sin romper la privacidad.

## Decisión

Capa A: telemetría local sin datos personales que el probador exporta. Capa B: Google Play Vitals al publicar. Capa C: envío opcional con consentimiento, como idea futura.

> **Enmienda (2026-10-15):** al lanzar primero en PC ([ADR-0009](0009-pc-primero-movil-despues.md)), la capa B ya no sería Google Play Vitals sino **lo que entregue Steam** (alcance por verificar en la fuente vigente en F5-40). Play Vitals queda para la fase móvil, después de la 1.0. Las capas A y C no cambian. El texto original se conserva como historial.

## Alternativas consideradas

- **SDK de analíticas de terceros desde el inicio:** más datos, pero recolección y obligaciones legales que no se necesitan.

## Consecuencias

Privacidad por defecto y declaraciones de tienda simples. La telemetría de cierres nativos se detecta con una marca al siguiente arranque.
