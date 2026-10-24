---
id: "doc-10-arquitectura"
tipo: "seccion"
title: "Arquitectura 🟡"
aliases: ["doc-10-arquitectura"]
documento: "[[10 Técnico y herramientas]]"
limpieza: 100
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[10 §Motor (confirmado el 2026-10-11)]]"
siguiente: "[[10 §Controles]]"
arriba: "[[10 Técnico y herramientas]]"
fuente: "studio/docs/10-tecnico-y-herramientas.md:37"
generado: true
---

# Arquitectura 🟡

> Separar en capas, con el contenido en datos:

← [[10 §Motor (confirmado el 2026-10-11)]] · [[10 Técnico y herramientas|↑ 10]] · [[10 §Controles]] →

Separar en capas, con el contenido en datos:

| Capa | Contenido | Nota |
|---|---|---|
| **Núcleo (simulación)** | Mercado, día/bloques, economía, eventos, contratos, vigilancia, empleados | Código sin interfaz, **simulable offline** durante miles de días |
| **Datos** | Minerales, zonas, herramientas, noticias, facciones, textos | Archivos de datos (JSON/recursos); cambiar un precio no toca el código |
| **Interfaz** | Pantallas, minijuegos, HUD | Consume el núcleo, no contiene reglas |
| **Entrada** | Ratón y teclado, y mando; el táctil queda como adaptador futuro | Capa de acciones (ver abajo) |
| **Guardado** | Persistencia | Versionado, con migraciones. Punto de control al iniciar cada acción y hasta 5 partidas guardables a elegir ✅ ([[01 Core loop y ciclo del día\|01]]) |
| **Plataforma** | Windows y Linux (Steam); móvil más adelante | Tienda (logros, nube, actualizaciones), pantalla (resolución, ventana), ciclo de vida |

Principios:

- **Semilla (seed)** para todo lo procedural, para reproducir partidas y bugs.
- **Pruebas automáticas** del núcleo y **simulador de mercado** que se ejecuta sin abrir el juego, para calibrar precios, volatilidad, multas y sumideros.
- Todo el contenido (minerales, zonas, eventos) en datos desde el inicio.

## Fuente

`studio/docs/10-tecnico-y-herramientas.md:37`
