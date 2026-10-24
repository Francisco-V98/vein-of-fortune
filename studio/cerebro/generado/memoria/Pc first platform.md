---
id: "mem-pc-first-platform"
tipo: "memoria"
title: "Pc first platform"
aliases: ["mem-pc-first-platform"]
nombre: "pc-first-platform"
memoria_tipo: "project"
arriba: "[[MOC Memoria]]"
generado: true
---

# Pc first platform

> Platform decision (2026-10-15): launch on PC first (Windows+Linux, Steam), mobile only after a stable 1.0 on Steam

The game launches first on PC (Windows and Linux) via Steam (+ itch.io for tests); target Steam Deck Verified; mouse+keyboard primary, full gamepad; Steam Auto-Cloud with 5 saves, local-only in Hardcore; «Próximamente» page at the END of F4. Mobile (iOS/Android) is phase F6.2, only after the 1.0 is published and stable. The author works on Mac, so a real Windows PC is required for testing ([[F1-39 Plan de pruebas y matriz de PC con un PC Windows real|F1-39]]). See ADR-0009 and doc 11.

**Why:** the author wants to finish and validate the full game on PC, and only port to mobile if they like the result.

**How to apply:** never design or schedule anything as «Android first» or touch-first; any mobile work goes to F6.2 tasks. Steam prerequisites for the store page live in F4.19.

## Relaciones

- **Documentos:** [[11 Legal y cumplimiento]], [[ADR-0009 PC primero (Steam) y móvil después]]
- **Tareas:** [[F1-39 Plan de pruebas y matriz de PC con un PC Windows real]]
