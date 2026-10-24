---
id: "adr-0007-decision"
tipo: "seccion"
title: "Decisión"
aliases: ["adr-0007-decision"]
documento: "[[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[ADR-0007 §Contexto]]"
siguiente: "[[ADR-0007 §Alternativas consideradas]]"
arriba: "[[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro]]"
fuente: "studio/docs/adr/0007-telemetria-por-capas.md:9"
generado: true
---

# Decisión

> Capa A: telemetría local sin datos personales que el probador exporta. Capa B: Google Play Vitals al publicar. Capa C: envío opcional con…

← [[ADR-0007 §Contexto]] · [[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro|↑ ADR-0007]] · [[ADR-0007 §Alternativas consideradas]] →

Capa A: telemetría local sin datos personales que el probador exporta. Capa B: Google Play Vitals al publicar. Capa C: envío opcional con consentimiento, como idea futura.

> **Enmienda (2026-10-15):** al lanzar primero en PC ([[ADR-0009 PC primero (Steam) y móvil después|ADR-0009]]), la capa B ya no sería Google Play Vitals sino **lo que entregue Steam** (alcance por verificar en la fuente vigente en [[F5-40 Datos de rendimiento y errores en producción (telemetría|F5-40]]). Play Vitals queda para la fase móvil, después de la 1.0. Las capas A y C no cambian. El texto original se conserva como historial.

## Fuente

`studio/docs/adr/0007-telemetria-por-capas.md:9`
