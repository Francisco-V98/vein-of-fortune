---
id: "adr-0009-decision"
tipo: "seccion"
title: "Decisión ✅"
aliases: ["adr-0009-decision"]
documento: "[[ADR-0009 PC primero (Steam) y móvil después]]"
limpieza: 0
abiertos: 4
espera: 5
aplazado_a: ["[[F1-06 Resolución base, escalado entero y modos de pantalla]]", "[[F3-23 Prueba de la tajada y decisión de seguir hacia la v1]]", "[[F4-227 Prueba de PixelLab - flujo, estilo, paleta, tamaños, precio]]", "[[F5-33 Ficha de tienda en español]]"]
estado: "con-abiertos"
anterior: "[[ADR-0009 §Contexto]]"
siguiente: "[[ADR-0009 §Alternativas descartadas]]"
arriba: "[[ADR-0009 PC primero (Steam) y móvil después]]"
fuente: "studio/docs/adr/0009-pc-primero-movil-despues.md:9"
generado: true
---

# Decisión ✅

> Decisiones del autor (2026-10-15):

← [[ADR-0009 §Contexto]] · [[ADR-0009 PC primero (Steam) y móvil después|↑ ADR-0009]] · [[ADR-0009 §Alternativas descartadas]] →

Decisiones del autor (2026-10-15):

1. **El juego se lanza primero en PC**, compatible y preparado para Steam. El móvil (Android e iOS) llega **después de que el juego esté completo en PC**: la 1.0 publicada y estable en Steam.
2. **Plataformas de la 1.0:** Windows y Linux. macOS queda para después de la 1.0. El motor sigue siendo Godot 4.x.
3. **Steam Deck:** se apunta a la categoría *Verified*: mando completo, sin HUD táctil y texto legible en 1280×800.
4. **Tiendas:** Steam como meta; itch.io para builds de prueba. GOG y Epic quedan fuera de la 1.0.
5. **Controles:** ratón y teclado principales (hover, tooltips, atajos y ventanas de información densas), con **mando completo**. La interfaz táctil queda como un **adaptador futuro** para el móvil; no se construye HUD táctil ahora.
6. **Nube y partidas:** Steam Auto-Cloud con una carpeta de guardados pequeños y hasta **5 partidas**. En Hardcore manda el guardado **local**: no se puede restaurar desde la nube tras morir.
7. **Página de Steam («Próximamente»):** se abre al final de F4, con el juego casi completo. Se mantiene la regla de arte «nada provisional llega a la tienda»: la página usa arte definitivo.
8. **Pruebas:** en un **PC Windows real** (el autor lo tiene o lo consigue) y en la Steam Deck si la hay. Es un requisito de F1. El autor trabaja en Mac, así que ese PC es indispensable.
9. **Sin cambio:** pago único, sin anuncios ni compras dentro del juego; autoguardado instantáneo (la Steam Deck suspende el juego en cualquier momento).

Propuestas 🟡 que acompañan la decisión:

- 🟡 Integrar Steamworks con **GodotSteam**, siempre detrás del puerto de plataforma/tienda ([[14 Arquitectura y modularidad|14]]), de modo que el juego también corra sin Steam (itch.io y pruebas).
- 🟡 Integración continua con exportación a **Windows y Linux** y build reproducible por línea de comandos.
- 🟡 La capa B de telemetría ([[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro|ADR-0007]]) pasa a ser lo que entregue Steam; su alcance real se verifica en la fuente vigente al llegar a [[F5-40 Datos de rendimiento y errores en producción (telemetría|F5-40]].

Aplazado con su tarea (⏳): resolución base y modo ventana ⏳ [[F1-06 Resolución base, escalado entero y modos de pantalla|F1-06]]; precio y DLC ⏳ [[F5-33 Ficha de tienda en español|F5-33]], [[F6-01 Diseño del casino - integración suave en la economía y la|F6-01]] y [[F6-61 Reserva de V2.1|F6-61]]; demo con el Acto I ⏳ [[F3-23 Prueba de la tajada y decisión de seguir hacia la v1|F3-23]]; declaración de IA de Steam y términos de PixelLab ⏳ [[F4-227 Prueba de PixelLab - flujo, estilo, paleta, tamaños, precio|F4-227]].

## Fuente

`studio/docs/adr/0009-pc-primero-movil-despues.md:9`
