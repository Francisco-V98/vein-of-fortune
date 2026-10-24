---
id: "doc-11-s12"
tipo: "seccion"
title: "12 · Fase móvil (después de la 1.0)"
aliases: ["doc-11-s12"]
documento: "[[11 Legal y cumplimiento]]"
abiertos: 0
espera: 9
aplazado_a: ["[[F6-18 Cuenta de Apple Developer]]", "[[F6-19 Exportación y firma para iOS]]", "[[F6-22 Ficha de App Store en español e inglés]]", "[[F6-23 Revisión de Apple y correcciones]]", "[[F6-71 Exportación y firma para Android]]", "[[F6-75 Ficha de Google Play y formularios de seguridad de datos]]", "[[F6-76 Prueba cerrada y revisión de Google Play]]"]
estado: "con-aplazados"
anterior: "[[11 §11 Fiscalidad y estructura]]"
siguiente: "[[11 §13 Calendario legal sugerido]]"
arriba: "[[11 Legal y cumplimiento]]"
fuente: "studio/docs/11-legal-y-cumplimiento.md:157"
generado: true
---

# 12 · Fase móvil (después de la 1.0)

> Se activa solo cuando la 1.0 esté publicada y estable en Steam (ADR-0009). Lo siguiente se conserva de la versión anterior de este…

← [[11 §11 Fiscalidad y estructura]] · [[11 Legal y cumplimiento|↑ 11]] · [[11 §13 Calendario legal sugerido]] →

Se activa solo cuando la 1.0 esté publicada y estable en Steam ([[ADR-0009 PC primero (Steam) y móvil después|ADR-0009]]). Lo siguiente se conserva de la versión anterior de este documento y **debe volver a verificarse** en la fuente vigente cuando llegue el momento. Tareas: [[F6-18 Cuenta de Apple Developer|F6-18]] a [[F6-23 Revisión de Apple y correcciones|F6-23]] (iOS) y [[F6-71 Exportación y firma para Android|F6-71]] a [[F6-76 Prueba cerrada y revisión de Google Play|F6-76]] (Android).

### Cuentas de desarrollador

| Tienda | Qué hace falta | Nota |
|---|---|---|
| Google Play | Cuenta de desarrollador (pago único, ≈25 USD) y verificación de identidad ⏳ [[F6-75 Ficha de Google Play y formularios de seguridad de datos\|F6-75]] | Las cuentas personales nuevas suelen requerir una **prueba cerrada con un mínimo de testers durante un tiempo** antes de producción. Verificar el requisito vigente ⏳ [[F6-76 Prueba cerrada y revisión de Google Play\|F6-76]] |
| Apple | Apple Developer Program (≈99 USD/año) ⏳ [[F6-18 Cuenta de Apple Developer\|F6-18]] | Solo si se sale en iOS |

### Formularios de las tiendas móviles

- **Google Play:** declaración de seguridad de datos (*Data safety*), cuestionario de **clasificación de contenido** (IARC), público objetivo, declaraciones sobre anuncios y otros ⏳ [[F6-75 Ficha de Google Play y formularios de seguridad de datos|F6-75]].
- **Apple:** etiquetas de privacidad (*App Privacy*), clasificación por edad, declaración de cifrado ⏳ [[F6-22 Ficha de App Store en español e inglés|F6-22]].
- **Telemetría de tienda móvil:** **Google Play Vitals** recopila datos de fallos por su cuenta; revisar cómo debe reflejarse en los formularios.
- **Claves y firma:** keystore de Android y su respaldo seguro ⏳ [[F6-71 Exportación y firma para Android|F6-71]]; firma de iOS ⏳ [[F6-19 Exportación y firma para iOS|F6-19]].
- **Prueba cerrada y revisión** de Google Play ⏳ [[F6-76 Prueba cerrada y revisión de Google Play|F6-76]]; revisión de Apple ⏳ [[F6-23 Revisión de Apple y correcciones|F6-23]].
- **Casino en móvil:** las tiendas móviles tienen políticas propias sobre azar simulado; se revisan aparte si el casino llega a móvil.
- Coherencia: lo que se declare debe coincidir con lo que el juego realmente hace (**sin cuentas, sin anuncios, sin analíticas** en la v1).

## Fuente

`studio/docs/11-legal-y-cumplimiento.md:157`
