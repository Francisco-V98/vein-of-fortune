---
id: "doc-11-s07"
tipo: "seccion"
title: "7 · Propiedad intelectual y licencias"
aliases: ["doc-11-s07"]
documento: "[[11 Legal y cumplimiento]]"
limpieza: 0
abiertos: 3
espera: 6
aplazado_a: ["[[F1-45 GodotSteam - inicializar Steam y probar en la Steam Deck]]", "[[F4-227 Prueba de PixelLab - flujo, estilo, paleta, tamaños, precio]]", "[[F5-22 Cuenta de Steamworks y alta de la aplicación]]", "[[F5-26 Registro final de licencias de assets y audio]]", "[[F5-29 Búsqueda de marca formal del título]]"]
estado: "con-abiertos"
anterior: "[[11 §6 Documentos propios]]"
siguiente: "[[11 §8 Azar y casino (futuro)]]"
arriba: "[[11 Legal y cumplimiento]]"
fuente: "studio/docs/11-legal-y-cumplimiento.md:97"
generado: true
---

# 7 · Propiedad intelectual y licencias

← [[11 §6 Documentos propios]] · [[11 Legal y cumplimiento|↑ 11]] · [[11 §8 Azar y casino (futuro)]] →

| Tema | Acción |
|---|---|
| **Nombre del juego y marca** | Buscar conflictos de marca y de nombre en tiendas antes de fijar el título. "Valdoria" es el nombre del mundo; el título es **Veta de Fortuna / Vein of Fortune**, pendiente de búsqueda de marca formal ⏳ [[F5-29 Búsqueda de marca formal del título\|F5-29]]. Hay que hacerla **antes de abrir la página «Próximamente»**, porque la página publica el nombre 🟡 |
| **Referencias** | Fallout, Dave the Diver, Papers, Please, Balatro son **inspiración de estilo**, no se copian nombres, personajes, arte ni sonidos |
| **Registro de licencias** | Tabla con: asset, fuente, licencia, uso comercial permitido, enlace y captura de los términos al momento de la descarga (`studio/data/assets.json`). **Una fuente sin licencia comercial clara no entra** |
| **Contenido generado con IA** | Revisar los términos comerciales de **cada herramienta y plan**. El arte generado íntegramente por IA puede no tener protección de derecho de autor en algunas jurisdicciones; el arte propio retocado ayuda |
| **PixelLab (arte definitivo)** | 🟡 Términos leídos el 2026-10-15 en pixellab.ai/termsofservice (versión «Last Updated: 2025-11-23»): conservas la propiedad de lo que creas (cláusulas 1.3 y 3.3) y se permite el uso comercial; **no puedes usar las imágenes para entrenar tus propios modelos** (1.2); el uso programático solo por su API oficial (2.2); el **usuario responde** de que el resultado no infrinja derechos de terceros (3.3); el servicio se da «tal cual», sin garantía (5.1); las funciones y los precios pueden cambiar (2.1). El texto leído **no distingue entre plan gratuito y de pago**. No garantiza protección de derecho de autor sobre lo generado. **Formalización:** captura de los términos y del plan elegido al hacer la prueba ⏳ [[F4-227 Prueba de PixelLab - flujo, estilo, paleta, tamaños, precio\|F4-227]]; registro final ⏳ [[F5-26 Registro final de licencias de assets y audio\|F5-26]]. Hasta [[F4-227 Prueba de PixelLab - flujo, estilo, paleta, tamaños, precio\|F4-227]] no se contrata ni se gastan créditos ([[12 Dirección de arte\|12]]) |
| **Herramienta de las referencias provisionales** | ⏳ [[F5-26 Registro final de licencias de assets y audio\|F5-26]] Las imágenes provisionales se generaron con gpt_image_2_5 vía Higgsfield; sus términos comerciales **no se leyeron**. No importa para la tienda mientras nada provisional se publique (regla de [[12 Dirección de arte\|12]]); lo registra el **asesor legal** si algún provisional llegara a usarse en público (por ejemplo, el hub o el README públicos) |
| **Software de terceros** | Godot (licencia MIT): incluir su aviso en los créditos. 🟡 **GodotSteam**: verifica su licencia al integrarlo ⏳ [[F1-45 GodotSteam - inicializar Steam y probar en la Steam Deck\|F1-45]]. El **SDK de Steamworks** se rige por el acuerdo de distribución de Valve (⏳ [[F5-22 Cuenta de Steamworks y alta de la aplicación\|F5-22]] lo lee el autor al firmar el alta). Revisa cada plugin o librería |
| **Voces** | Si algún día se usan voces, contratos o licencias claras; no clonar voces de personas reales sin permiso |

## Fuente

`studio/docs/11-legal-y-cumplimiento.md:97`
