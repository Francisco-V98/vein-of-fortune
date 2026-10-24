---
id: "doc-10-telemetria-por-capas"
tipo: "seccion"
title: "Telemetría por capas ✅"
aliases: ["doc-10-telemetria-por-capas"]
documento: "[[10 Técnico y herramientas]]"
limpieza: 0
abiertos: 1
espera: 0
estado: "con-abiertos"
anterior: "[[10 §Fase móvil (después de la 1.0)]]"
siguiente: "[[10 §Seguridad y protección de datos]]"
arriba: "[[10 Técnico y herramientas]]"
fuente: "studio/docs/10-tecnico-y-herramientas.md:163"
generado: true
---

# Telemetría por capas ✅

> Se puede medir un juego sin conexión. Tres capas, en este orden:

← [[10 §Fase móvil (después de la 1.0)]] · [[10 Técnico y herramientas|↑ 10]] · [[10 §Seguridad y protección de datos]] →

Se puede medir un juego sin conexión. Tres capas, en este orden:

| Capa | Cómo | Cuándo |
|---|---|---|
| **A · Local y exportable** | El juego guarda rendimiento, errores y eventos en un archivo local sin datos personales; el probador lo exporta y se carga en el panel de `studio/` | Desde la Fase 2 |
| **B · Steam** 🟡 | Lo que entregue Steam sobre cierres y rendimiento, sin SDK propio en el juego; el alcance real se verifica en la fuente vigente en [[F5-40 Datos de rendimiento y errores en producción (telemetría\|F5-40]]. *Antes era Google Play Vitals, que pasa a la fase móvil* ([[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro\|ADR-0007]]) | Al publicar o en pruebas |
| **C · Envío opcional** | Con consentimiento explícito y datos anónimos, a un servidor propio | Idea futura; cambia la política de privacidad y los formularios |

Reglas de la capa A:

- ID anónimo y reiniciable; **sin** nombre del jugador ni de la tienda.
- Nada se envía automáticamente.
- Detalle ampliado solo en versiones de pruebas.
- Un cierre nativo no puede registrarse a sí mismo: se detecta con una **marca de cierre no limpio** al siguiente arranque.

Qué muestra el panel: rendimiento por equipo, errores, estabilidad, economía (curva de dinero, abandono por día, éxito en minijuegos, muertes en hardcore) e informes del simulador de mercado.

## Fuente

`studio/docs/10-tecnico-y-herramientas.md:163`
