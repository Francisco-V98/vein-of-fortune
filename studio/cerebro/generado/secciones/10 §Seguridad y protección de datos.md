---
id: "doc-10-seguridad-y-proteccion-de-datos"
tipo: "seccion"
title: "Seguridad y protección de datos ✅"
aliases: ["doc-10-seguridad-y-proteccion-de-datos"]
documento: "[[10 Técnico y herramientas]]"
limpieza: 50
abiertos: 2
espera: 0
estado: "con-abiertos"
anterior: "[[10 §Telemetría por capas]]"
siguiente: "[[10 §Calidad y pruebas]]"
arriba: "[[10 Técnico y herramientas]]"
fuente: "studio/docs/10-tecnico-y-herramientas.md:182"
generado: true
---

# Seguridad y protección de datos ✅

> Principio: reducir la superficie de ataque y los datos que se manejan.

← [[10 §Telemetría por capas]] · [[10 Técnico y herramientas|↑ 10]] · [[10 §Calidad y pruebas]] →

Principio: **reducir la superficie de ataque y los datos que se manejan**.

### Decisiones para la v1 🟡

| Tema | Decisión |
|---|---|
| Cuentas y autenticación | **Sin cuentas en la v1**: juego offline, sin servidores propios. Nada que autenticar |
| Datos personales | Casi ninguno: el nombre del personaje y de la tienda son locales y no salen del equipo (Steam Auto-Cloud sincroniza los guardados con la cuenta de Steam, no con servidores propios) |
| Anuncios y analíticas de terceros | **Ninguno en la v1** (pago único); cada SDK trae recolección de datos y obligaciones |
| Guardado | Formato versionado, escritura segura (archivo temporal y reemplazo), copia de respaldo y verificación de integridad para detectar corrupción. **Autoguardado instantáneo**: la Steam Deck suspende el juego en cualquier momento. Cada una de las hasta 5 partidas guardables tiene su propio archivo y su punto de control ✅ ([[01 Core loop y ciclo del día\|01]]) |
| Nube y partidas ✅ | **Steam Auto-Cloud** con una carpeta de guardados pequeños y hasta **5 partidas**. En **Hardcore manda el guardado local**: no se puede restaurar desde la nube tras morir |
| Trampas | En un juego de un jugador no es prioridad. Una verificación ligera solo evita corrupción accidental |
| Validación de entradas | Nombre y tienda con límite de longitud, caracteres permitidos y filtro de palabras ofensivas |
| Permisos y acceso a archivos | El juego solo escribe en su carpeta de guardados y de diagnóstico |
| Dependencias | Pocas, con versión fijada, de fuentes confiables; revisar licencias |
| Secretos | **Nunca en el repositorio** (claves, tokens, contraseñas) |
| Claves de Steam | Las claves de Steamworks y cualquier credencial de publicación **no entran en el repositorio** |
| Compra del juego | Gestionada por Steam (pago único); no se implementa validación propia |
| Repositorio | Privado, con copias de respaldo |

### Si en el futuro hay nube o cuentas 🟡

- Usar el inicio de sesión de la plataforma (Steam; en el móvil, Google Play Games o Sign in with Apple); **no guardar contraseñas propias**.
- Cifrado en tránsito, mínimo de datos, política de privacidad actualizada.
- Ampliar la revisión legal ([[11 Legal y cumplimiento|11]]).

## Fuente

`studio/docs/10-tecnico-y-herramientas.md:182`
