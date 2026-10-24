---
id: "doc-10-exportacion-y-steam"
tipo: "seccion"
title: "Exportación y Steam 🟡"
aliases: ["doc-10-exportacion-y-steam"]
documento: "[[10 Técnico y herramientas]]"
limpieza: 50
abiertos: 1
espera: 0
estado: "con-abiertos"
anterior: "[[10 §Estructura del repositorio]]"
siguiente: "[[10 §Fase móvil (después de la 1.0)]]"
arriba: "[[10 Técnico y herramientas]]"
fuente: "studio/docs/10-tecnico-y-herramientas.md:133"
generado: true
---

# Exportación y Steam 🟡

> Falta una tarea del roadmap que integre Steamworks y fije la herramienta exacta (GodotSteam u otra); hay que crearla antes de la página de…

← [[10 §Estructura del repositorio]] · [[10 Técnico y herramientas|↑ 10]] · [[10 §Fase móvil (después de la 1.0)]] →

| Tema | Propuesta |
|---|---|
| Exportación | Plantillas de Godot para Windows y Linux, generadas por línea de comandos (sin abrir el editor), con build reproducible: misma fuente y misma versión de Godot, mismo resultado ([[F1-26 Exportación reproducible por línea de comandos para Windows\|F1-26]]) |
| Steamworks | **GodotSteam** detrás del puerto de plataforma/tienda ([[14 Arquitectura y modularidad\|14]]); sin Steam el juego debe arrancar igual (itch.io y pruebas) |
| Nube | Steam Auto-Cloud ✅ (ver «Seguridad y protección de datos») |
| Logros | Se conectan al módulo de logros por el puerto de tienda; el módulo no conoce a Steam |
| Subida de builds | Herramienta de línea de comandos de Steam (`steamcmd`) desde un equipo de publicación; las credenciales fuera del repositorio |

🟡 Falta una tarea del roadmap que integre Steamworks y fije la herramienta exacta (GodotSteam u otra); hay que crearla antes de la página de Steam (final de F4). Hasta que exista, esta propuesta sigue abierta y no se aplaza a ninguna tarea.

## Fuente

`studio/docs/10-tecnico-y-herramientas.md:133`
