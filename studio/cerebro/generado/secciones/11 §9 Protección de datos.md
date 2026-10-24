---
id: "doc-11-s09"
tipo: "seccion"
title: "9 · Protección de datos"
aliases: ["doc-11-s09"]
documento: "[[11 Legal y cumplimiento]]"
limpieza: 33
abiertos: 2
espera: 3
aplazado_a: ["[[F4-234 Steam Auto-Cloud y las 5 partidas guardables (local en]]", "[[F5-40 Datos de rendimiento y errores en producción (telemetría]]", "[[F5-41 Actualizar política y formularios con la telemetría real]]"]
estado: "con-abiertos"
anterior: "[[11 §8 Azar y casino (futuro)]]"
siguiente: "[[11 §10 Steam Deck, Steam Input y nube (cumplimiento)]]"
arriba: "[[11 Legal y cumplimiento]]"
fuente: "studio/docs/11-legal-y-cumplimiento.md:123"
generado: true
---

# 9 · Protección de datos

← [[11 §8 Azar y casino (futuro)]] · [[11 Legal y cumplimiento|↑ 11]] · [[11 §10 Steam Deck, Steam Input y nube (cumplimiento)]] →

- Con un juego **sin cuentas propias, sin anuncios y sin analíticas** en la v1, la carga es mínima: se declara que el juego no recopila datos.
- El juego usa servicios de Steam (nube, logros): esos datos los trata Steam bajo su política de privacidad. Aun así, la política propia debe decir qué guarda el juego (partidas locales y en la nube de Steam) y que no envía datos a terceros. 🟡
- **Nube y Hardcore ✅:** Auto-Cloud con una carpeta de guardados pequeños y hasta 5 partidas; en Hardcore manda el guardado **local**. La fuente confirma que el patrón de archivos de Auto-Cloud lo eliges tú: excluye la partida Hardcore. La fuente no da cuotas por defecto; las fijas en el panel de Steamworks ⏳ [[F4-234 Steam Auto-Cloud y las 5 partidas guardables (local en|F4-234]].
- Cualquier SDK o servicio que se agregue (analíticas, anuncios, reporte de fallos) **cambia la declaración** y puede activar leyes de protección de datos (por ejemplo, GDPR, LGPD, CCPA, según el público).
- Mantener un inventario de **qué datos entran y salen del equipo**, aunque sea "ninguno".

### Telemetría y privacidad 🟡

- La **telemetría local** (capa A, ver [[10 Técnico y herramientas|10]]) no envía datos: el probador decide si comparte el archivo. No incluye nombre de jugador ni de tienda.
- La **capa B** (datos de tienda) pasa de Play Vitals a lo que Steam entregue. ⏳ [[F5-40 Datos de rendimiento y errores en producción (telemetría|F5-40]] No se verificó qué informes de fallos ofrece Steamworks: lo comprueba el **autor** con el panel de Steamworks.
- Si algún día se activa el **envío opcional** (capa C): consentimiento explícito, datos anónimos, actualización de la política de privacidad y del cuestionario ⏳ [[F5-41 Actualizar política y formularios con la telemetría real|F5-41]].
- Fichas de tienda y política de privacidad en **español e inglés**.

## Fuente

`studio/docs/11-legal-y-cumplimiento.md:123`
