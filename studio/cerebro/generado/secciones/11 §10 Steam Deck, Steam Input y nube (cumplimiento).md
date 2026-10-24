---
id: "doc-11-s10"
tipo: "seccion"
title: "10 · Steam Deck, Steam Input y nube (cumplimiento)"
aliases: ["doc-11-s10"]
documento: "[[11 Legal y cumplimiento]]"
abiertos: 0
espera: 3
aplazado_a: ["[[F4-236 Steam Input y glifos del mando]]", "[[F4-239 Lista de verificación de Steam Deck Verified y prueba en la]]"]
estado: "con-aplazados"
anterior: "[[11 §9 Protección de datos]]"
siguiente: "[[11 §11 Fiscalidad y estructura]]"
arriba: "[[11 Legal y cumplimiento]]"
fuente: "studio/docs/11-legal-y-cumplimiento.md:138"
generado: true
---

# 10 · Steam Deck, Steam Input y nube (cumplimiento)

> Verificado el 2026-10-15 en partner.steamgames.com/doc/steamdeck/compat. Esto es un resumen; el detalle técnico vive en 10.

← [[11 §9 Protección de datos]] · [[11 Legal y cumplimiento|↑ 11]] · [[11 §11 Fiscalidad y estructura]] →

Verificado el 2026-10-15 en partner.steamgames.com/doc/steamdeck/compat. Esto es un **resumen**; el detalle técnico vive en [[10 Técnico y herramientas|10]].

- **Entrada:** la configuración de mando por defecto debe dar acceso a **todo el contenido** sin tocar ajustes. Los glifos deben coincidir con el dispositivo activo (la fuente recomienda la API de Steam Input). El texto escrito necesita el teclado en pantalla de Steam o una entrada propia con mando ⏳ [[F4-236 Steam Input y glifos del mando|F4-236]].
- **Pantalla:** resolución de **1280×800** (preferida) o 1280×720. Texto legible a unos 30 cm: altura mínima de **9 px** a 1280×800, **12 px** recomendado, y conviene un tamaño de texto ajustable ⏳ [[F4-239 Lista de verificación de Steam Deck Verified y prueba en la|F4-239]].
- **Fluidez:** sin avisos de que SteamOS o la GPU no son compatibles; si hay lanzador, debe navegarse con mando (se recomienda no tener lanzador). Rendimiento: **30 fps a 800p** por defecto.
- **Linux y Proton:** si hay build nativo de Linux, Valve lo prueba primero; si falla, prueba el de Windows con Proton y publica el mejor resultado. Los problemas bloqueantes dan el distintivo *No compatible*.
- **Revisión:** primero hay que pasar la revisión normal del build; se pide con «Steam Hardware Compatibility Review» (acceso limitado); resultados en ~1 semana.
- **Steam Input ⏳ [[F4-239 Lista de verificación de Steam Deck Verified y prueba en la|F4-239]]:** la fuente dice que se recomienda; no se confirmó si es obligatorio para *Verified*. Lo confirma el **autor** en [[F4-239 Lista de verificación de Steam Deck Verified y prueba en la|F4-239]] con la lista oficial.

## Fuente

`studio/docs/11-legal-y-cumplimiento.md:138`
