---
id: "doc-10"
tipo: "documento"
title: "10 · Técnico y herramientas"
aliases: ["doc-10"]
estado: "con-abiertos"
limpieza: 52
ok: 21
propuestas: 15
abiertos: 19
espera: 4
secciones: 16
arriba: "[[MOC Documentos]]"
fuente: "studio/docs/10-tecnico-y-herramientas.md:1"
generado: true
---

# 10 · Técnico y herramientas

> Limpieza 52 % · 19 abiertos · 16 secciones

## Secciones

1. [[10 §Enfoque]]
2. [[10 §Plataformas]] — Decisión del autor (2026-10-15), con su ADR en ADR-0009:
3. [[10 §Motor (confirmado el 2026-10-11)]] — Godot 4.x con GDScript.
4. [[10 §Arquitectura]] — Separar en capas, con el contenido en datos:
5. [[10 §Controles]] — Decisión del autor (2026-10-15): ratón y teclado son los controles principales (hover, tooltips, atajos y ventanas de información densas) y…
6. [[10 §Arte y sonido]] — 1. Prototipo y vertical slice: formas simples, referencias y sonidos genéricos, todo provisional (política del autor, 2026-10-13)…
7. [[10 §Localización (español e inglés desde el inicio)]] — El juego se hace en español e inglés desde el principio, con un marco que permita sumar más idiomas sin tocar el código.
8. [[10 §Estructura del repositorio]] — Un solo repositorio con dos mundos separados:
9. [[10 §Exportación y Steam]] — Falta una tarea del roadmap que integre Steamworks y fije la herramienta exacta (GodotSteam u otra); hay que crearla antes de la página de…
10. [[10 §Fase móvil (después de la 1.0)]] — Empieza cuando la 1.0 esté publicada y estable en Steam (ADR-0009). Todo lo que sigue se conserva del plan anterior de «Android primero» y…
11. [[10 §Telemetría por capas]] — Se puede medir un juego sin conexión. Tres capas, en este orden:
12. [[10 §Seguridad y protección de datos]] — Principio: reducir la superficie de ataque y los datos que se manejan.
13. [[10 §Calidad y pruebas]]
14. [[10 §Trabajar con IA]]
15. [[10 §Cerebro del proyecto en Obsidian]]
16. [[10 §Pendiente]]

## Puntos abiertos

- [[10 §Controles]] (línea 71): 🟡 Minijuegos: Picado y Perforación se juegan con un botón (ratón, teclado o mando); Cincelado (trazar) y arrastrar mercancía usan el puntero con ratón y un cursor con el stick con mando. Hay que diseñ
- [[10 §Controles]] (línea 73): 🟡 Probar con un mando real en Windows y en la Steam Deck antes de dar por buenos los controles (F1-15).
- [[10 §Arte y sonido]] (línea 77): ### Pipeline 🟡
- [[10 §Arte y sonido]] (línea 90): ### Audio 🟡
- [[10 §Localización (español e inglés desde el inicio)]] (línea 103): Formato de traducciones 🟡 / Archivos (gettext) que Godot soporta de forma nativa, con contexto y plurales
- [[10 §Localización (español e inglés desde el inicio)]] (línea 109): Flujo 🟡 / Extraer cadenas, traducir con asistencia de IA, revisar con un glosario ES/EN y compilar
- [[10 §Localización (español e inglés desde el inicio)]] (línea 110): Herramientas 🟡 / Edición de con un editor como Poedit; una plataforma de traducción (por ejemplo Weblate o Crowdin) solo si más adelante hay colaboradores
- [[10 §Exportación y Steam]] (línea 142): 🟡 Falta una tarea del roadmap que integre Steamworks y fije la herramienta exacta (GodotSteam u otra); hay que crearla antes de la página de Steam (final de F4). Hasta que exista, esta propuesta sigue
- [[10 §Telemetría por capas]] (línea 169): B · Steam 🟡 / Lo que entregue Steam sobre cierres y rendimiento, sin SDK propio en el juego; el alcance real se verifica en la fuente vigente en F5-40. Antes era Google Play Vitals, que pasa a la fase
- [[10 §Seguridad y protección de datos]] (línea 185): ### Decisiones para la v1 🟡
- [[10 §Seguridad y protección de datos]] (línea 203): ### Si en el futuro hay nube o cuentas 🟡
- [[10 §Calidad y pruebas]] (línea 213): Integración continua: exportación a Windows y Linux 🟡 y build reproducible por línea de comandos (F1-26); el detalle está en [15](15-flujo-de-trabajo-y-calidad.md).
- [[10 §Pendiente]] (línea 232): ❓ Estructura de carpetas del proyecto del juego.
- [[10 §Pendiente]] (línea 234): ❓ Herramientas concretas de audio.
- [[10 §Pendiente]] (línea 235): ❓ Un PC Windows real para pruebas (requisito de F1): el autor lo tiene o lo consigue.
- [[10 §Pendiente]] (línea 237): ❓ Hub de documentación y tablero de tareas (ver [06](06-roadmap-y-pendientes.md)).

## Relaciones

- **Aplazados a:** [[F0-88 Consulta del estudio sin leer documentos enteros]], [[F1-06 Resolución base, escalado entero y modos de pantalla]]
- **Enlaza a:**
  - [[ADR-0009 PC primero (Steam) y móvil después]]
  - [[01 Core loop y ciclo del día]]
  - [[14 Arquitectura y modularidad]]
  - [[11 Legal y cumplimiento]]
  - [[12 Dirección de arte]]
  - [[15 Flujo de trabajo y calidad]]
  - [[16 Calidad y QA]]
  - [[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro]]
  - [[06 Roadmap, ideas futuras y pendientes]]
- **Citado por:**
  - [[00 Visión]]
  - [[01 Core loop y ciclo del día]]
  - [[03 Comercio y mercado]]
  - [[08 Historia y personaje]]
  - [[09 Minijuegos]]
  - [[11 Legal y cumplimiento]]
  - [[14 Arquitectura y modularidad]]
  - [[15 Flujo de trabajo y calidad]]
  - [[16 Calidad y QA]]
  - [[ADR-0009 PC primero (Steam) y móvil después]]

## Fuente

`studio/docs/10-tecnico-y-herramientas.md:1`
