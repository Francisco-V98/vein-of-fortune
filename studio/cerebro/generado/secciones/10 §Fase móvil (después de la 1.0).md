---
id: "doc-10-fase-movil-despues-de-la-1-0"
tipo: "seccion"
title: "Fase móvil (después de la 1.0)"
aliases: ["doc-10-fase-movil-despues-de-la-1-0"]
documento: "[[10 Técnico y herramientas]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[10 §Exportación y Steam]]"
siguiente: "[[10 §Telemetría por capas]]"
arriba: "[[10 Técnico y herramientas]]"
fuente: "studio/docs/10-tecnico-y-herramientas.md:145"
generado: true
---

# Fase móvil (después de la 1.0)

> Empieza cuando la 1.0 esté publicada y estable en Steam (ADR-0009). Todo lo que sigue se conserva del plan anterior de «Android primero» y…

← [[10 §Exportación y Steam]] · [[10 Técnico y herramientas|↑ 10]] · [[10 §Telemetría por capas]] →

Empieza cuando la 1.0 esté publicada y estable en Steam ([[ADR-0009 PC primero (Steam) y móvil después|ADR-0009]]). Todo lo que sigue se conserva del plan anterior de «Android primero» y se retoma entonces.

| Tema | Contenido |
|---|---|
| Exportación a Android | Instalar **JDK** y **Android SDK**, crear una **keystore** de debug y configurar la exportación; generar el **APK** (y el paquete de tienda) por línea de comandos |
| Versionado | `versionCode` que solo crece y `versionName` igual a la versión del juego ([[15 Flujo de trabajo y calidad\|15]]) |
| Pantalla | Orientación horizontal, interfaz con los pulgares en los bordes y **zona segura** (muescas, bordes redondeados, proporciones como 20:9) |
| Entrada | Adaptador **táctil** con HUD táctil que se oculta al usar mando; minijuegos con el dedo (trazar, arrastrar) y háptica |
| Permisos | Los mínimos posibles (idealmente solo vibración) |
| Copias de seguridad | Decidir de forma consciente si los guardados entran en el backup de Android |
| Firma | La clave de firma se respalda **fuera del repo**; perderla puede impedir actualizaciones. Usar la firma gestionada por Google Play |
| Telemetría | **Google Play Vitals** como capa B del móvil (cierres, arranque, batería, renderizado lento) |
| iOS | Solo si todo va bien. Se puede probar en el simulador de Xcode en Mac, pero no reemplaza a un dispositivo real, y publicar requiere cuenta de pago |
| Idioma | Idioma inicial según el del dispositivo |
| Pruebas | Dispositivo Android propio, tres gamas y mandos Bluetooth ([[16 Calidad y QA\|16]], «Fase móvil») |

## Fuente

`studio/docs/10-tecnico-y-herramientas.md:145`
