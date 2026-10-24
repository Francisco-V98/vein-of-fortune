---
id: "adr-0009"
tipo: "adr"
title: "ADR-0009 · PC primero (Steam) y móvil después"
aliases: ["adr-0009"]
estado: "Aceptada"
limpieza: 29
ok: 2
propuestas: 5
abiertos: 5
espera: 6
secciones: 4
fecha: "2026-10-15"
arriba: "[[MOC ADR]]"
fuente: "studio/docs/adr/0009-pc-primero-movil-despues.md:1"
generado: true
---

# ADR-0009 · PC primero (Steam) y móvil después

> Limpieza 29 % · 5 abiertos · 4 secciones

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-15

## Secciones

1. [[ADR-0009 §Contexto]] — Hasta ahora el plan era Android primero: el juego se diseñaba para pantalla táctil, con resolución y zona segura pensadas para teléfonos…
2. [[ADR-0009 §Decisión]] — Decisiones del autor (2026-10-15):
3. [[ADR-0009 §Alternativas descartadas]]
4. [[ADR-0009 §Consecuencias]]

## Puntos abiertos

- [[ADR-0009 §Decisión]] (línea 22): Propuestas 🟡 que acompañan la decisión:
- [[ADR-0009 §Decisión]] (línea 24): 🟡 Integrar Steamworks con GodotSteam, siempre detrás del puerto de plataforma/tienda ([14](../14-arquitectura-y-modularidad.md)), de modo que el juego también corra sin Steam (itch.io y pruebas).
- [[ADR-0009 §Decisión]] (línea 25): 🟡 Integración continua con exportación a Windows y Linux y build reproducible por línea de comandos.
- [[ADR-0009 §Decisión]] (línea 26): 🟡 La capa B de telemetría ([ADR-0007](0007-telemetria-por-capas.md)) pasa a ser lo que entregue Steam; su alcance real se verifica en la fuente vigente al llegar a F5-40.
- [[ADR-0009 §Alternativas descartadas]] (línea 36): Con macOS en la 1.0 / Aplazada por el autor hasta después de la 1.0; 🟡 además implicaría firma y notarización de Apple, por verificar entonces

## Relaciones

- **Aplazados a:** [[F1-06 Resolución base, escalado entero y modos de pantalla]], [[F1-44 Presupuestos de rendimiento medidos en PC]], [[F3-23 Prueba de la tajada y decisión de seguir hacia la v1]], [[F4-227 Prueba de PixelLab - flujo, estilo, paleta, tamaños, precio]], [[F5-33 Ficha de tienda en español]]
- **Enlaza a:**
  - [[ADR-0001 Godot 4.x con GDScript como motor]]
  - [[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro]]
  - [[14 Arquitectura y modularidad]]
  - [[ADR-0003 Arquitectura modular por cortes verticales y capas]]
  - [[10 Técnico y herramientas]]
  - [[16 Calidad y QA]]
  - [[11 Legal y cumplimiento]]
- **Citado por:**
  - [[10 Técnico y herramientas]]
  - [[11 Legal y cumplimiento]]
  - [[12 Dirección de arte]]
  - [[14 Arquitectura y modularidad]]
  - [[16 Calidad y QA]]
  - [[18 Biblia narrativa]]
  - [[ADR-0001 Godot 4.x con GDScript como motor]]
  - [[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro]]

## Fuente

`studio/docs/adr/0009-pc-primero-movil-despues.md:1`
