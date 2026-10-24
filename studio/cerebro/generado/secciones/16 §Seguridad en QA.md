---
id: "doc-16-seguridad-en-qa"
tipo: "seccion"
title: "Seguridad en QA ✅"
aliases: ["doc-16-seguridad-en-qa"]
documento: "[[16 Calidad y QA]]"
limpieza: 0
abiertos: 1
espera: 0
estado: "con-abiertos"
anterior: "[[16 §Tipos de verificación]]"
siguiente: "[[16 §Casos de prueba]]"
arriba: "[[16 Calidad y QA]]"
fuente: "studio/docs/16-calidad-y-qa.md:59"
generado: true
---

# Seguridad en QA ✅

> Lista de verificación adaptada de OWASP MASVS (estándar de seguridad para aplicaciones móviles, que sigue siendo una buena guía) a un juego…

← [[16 §Tipos de verificación]] · [[16 Calidad y QA|↑ 16]] · [[16 §Casos de prueba]] →

Lista de verificación **adaptada de OWASP MASVS** (estándar de seguridad para aplicaciones móviles, que sigue siendo una buena guía) a un juego de PC **sin conexión ni cuentas propias** 🟡:

| Área | Verificación |
|---|---|
| Secretos | Sin claves, tokens ni contraseñas en el repositorio ni en las builds de Windows y Linux (escaneo automático) |
| Almacenamiento | Los guardados no incluyen datos personales; el archivo de diagnóstico tampoco |
| Integridad de datos | Un guardado corrupto o manipulado se detecta y no rompe el juego ni ejecuta contenido |
| Entradas | El nombre del personaje y de la tienda tienen límites y caracteres permitidos, y no inyectan formato (por ejemplo etiquetas de texto enriquecido) ni rompen la interfaz |
| Plataforma | El juego solo escribe en su carpeta de guardados y diagnóstico; sin ejecutables ni librerías sin explicar en la build |
| Compilación | Versión de lanzamiento sin depuración activada y con las credenciales de Steam fuera del repositorio |
| Dependencias | Pocas, con versión fija y licencia revisada; sin avisos de vulnerabilidades conocidas |
| Privacidad | Nada se envía sin una acción del usuario; el ID anónimo se puede reiniciar |
| Resistencia | Se asume que un jugador puede manipular su guardado: no es crítico en un juego de un jugador, pero no debe provocar fallos |

Cada punto tiene un caso de prueba en el catálogo (área **Seguridad** y **Privacidad**). Las comprobaciones de APK, manifiesto y firma de Google Play pasan a la fase móvil (ver más abajo).

## Fuente

`studio/docs/16-calidad-y-qa.md:59`
