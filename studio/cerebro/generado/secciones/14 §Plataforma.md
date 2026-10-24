---
id: "doc-14-plataforma"
tipo: "seccion"
title: "Plataforma 🟡"
aliases: ["doc-14-plataforma"]
documento: "[[14 Arquitectura y modularidad]]"
limpieza: 0
abiertos: 1
espera: 1
aplazado_a: ["[[F1-06 Resolución base, escalado entero y modos de pantalla]]"]
estado: "con-abiertos"
anterior: "[[14 §Datos y persistencia]]"
siguiente: "[[14 §Raíz de composición]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:118"
generado: true
---

# Plataforma 🟡

> El juego se lanza primero en PC (Windows y Linux, con Steam) y el móvil llega después de la 1.0 (ADR-0009). La arquitectura ya lo prevé: la…

← [[14 §Datos y persistencia]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Raíz de composición]] →

El juego se lanza **primero en PC (Windows y Linux, con Steam)** y el móvil llega después de la 1.0 ([[ADR-0009 PC primero (Steam) y móvil después|ADR-0009]]). La arquitectura ya lo prevé: la plataforma son **puertos** con adaptadores intercambiables, así que llevar el juego a otro lugar es añadir adaptadores, no modificar módulos.

| Puerto | Qué cubre | Adaptadores |
|---|---|---|
| Entrada | Acciones (aceptar, cancelar, mover, usar, menú) y detección del último dispositivo | **Ratón y teclado** y **mando** (Steam Deck incluida); **táctil**: adaptador futuro, fase móvil |
| Almacenamiento | Guardados, carpeta de guardados y diagnóstico local | Archivos locales; Steam Auto-Cloud sincroniza esa carpeta (hasta 5 partidas; en Hardcore manda el guardado local) |
| **Plataforma / tienda** | Logros, nube y actualizaciones | Steam (🟡 GodotSteam, [[10 Técnico y herramientas\|10]]); un adaptador **nulo** para itch.io y pruebas, de modo que el juego corra sin Steam |
| **Pantalla** | Resolución, modo ventana y pantalla completa, escala | Adaptador de PC; el detalle (resolución base, escala entera con bandas) ⏳ [[F1-06 Resolución base, escalado entero y modos de pantalla\|F1-06]] |
| Audio, idioma, reloj | Reproducción, idioma activo, tiempo inyectado | Adaptadores de PC y dobles de pruebas |
| Háptica | Vibración | Vibración del mando; en la fase móvil, la del teléfono |

Reglas:

- Los módulos solo hablan con los **puertos**; el dominio no usa `Input`, `OS` ni `DisplayServer` (símbolos prohibidos que ya vigila el verificador, regla A4).
- Los logros los define el módulo que los otorga y los emite como datos; solo el adaptador de tienda los envía a Steam.
- Nada del dominio sabe que existe Steam. Si Steam no está, el adaptador nulo responde sin hacer nada.
- Los controles (ratón y teclado, mando) viven detrás del puerto de entrada ([[10 Técnico y herramientas|10]]).
- El **camino al móvil** consiste en escribir el adaptador táctil, la háptica del teléfono y los de almacenamiento y ciclo de vida de Android e iOS. Para no cerrarlo, ninguna interfaz nueva depende solo del hover.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:118`
