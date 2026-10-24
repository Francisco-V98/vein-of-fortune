---
id: "doc-14"
tipo: "documento"
title: "14 · Arquitectura y modularidad"
aliases: ["doc-14"]
estado: "con-abiertos"
limpieza: 22
ok: 4
propuestas: 13
abiertos: 14
espera: 1
secciones: 15
arriba: "[[MOC Documentos]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:1"
generado: true
---

# 14 · Arquitectura y modularidad

> Limpieza 22 % · 14 abiertos · 15 secciones

## Secciones

1. [[14 §Requisitos del autor]] — El proyecto debe ser muy modular, sin dependencias directas entre partes, escalable, con una buena estructura de scaffolding, independencia…
2. [[14 §Principios]] — 1. Regla de dependencia: las dependencias apuntan hacia el dominio. El dominio no conoce a nadie.
3. [[14 §Estructura de `game - `]]
4. [[14 §Capas dentro de un módulo]]
5. [[14 §Módulos previstos]] — Cada módulo corresponde a un tema de diseño ya documentado. depende de son las únicas apis de otros módulos que puede usar; todo debe…
6. [[14 §Cómo se comunican los módulos]] — Reglas de los eventos:
7. [[14 §Presentación]]
8. [[14 §Datos y persistencia]]
9. [[14 §Plataforma]] — El juego se lanza primero en PC (Windows y Linux, con Steam) y el móvil llega después de la 1.0 (ADR-0009). La arquitectura ya lo prevé: la…
10. [[14 §Raíz de composición]] — app/ es el único lugar que conoce las implementaciones concretas: crea los módulos, conecta puertos con adaptadores y arranca el juego. Los…
11. [[14 §Clean code en GDScript]] — Requisito del autor; el detalle de umbrales es .
12. [[14 §Qué se prohíbe]]
13. [[14 §Verificación automática]] — El verificador de arquitectura ya tiene 22 pruebas automáticas sobre estructuras de ejemplo. Falta ejecutarlo contra código real de…
14. [[14 §Añadir un módulo]] — 1. Declararlo en game/architecture.json con sus dependson (y su ADR si introduce una decisión nueva).
15. [[14 §Límites conocidos]]

## Puntos abiertos

- [[14 §Requisitos del autor]] (línea 6): Todo lo que sigue es la forma de cumplirlo. Los principios son requisitos; el diseño concreto está marcado 🟡 y se confirma con los ADR (ver [ADR-0003](adr/0003-arquitectura-modular.md)).
- [[14 §Plataforma]] (línea 125): Plataforma / tienda / Logros, nube y actualizaciones / Steam (🟡 GodotSteam, [10](10-tecnico-y-herramientas.md)); un adaptador nulo para itch.io y pruebas, de modo que el juego corra sin Steam
- [[14 §Clean code en GDScript]] (línea 144): Requisito del autor; el detalle de umbrales es 🟡.

## Relaciones

- **Aplazados a:** [[F1-06 Resolución base, escalado entero y modos de pantalla]]
- **Enlaza a:**
  - [[ADR-0003 Arquitectura modular por cortes verticales y capas]]
  - [[01 Core loop y ciclo del día]]
  - [[03 Comercio y mercado]]
  - [[02 Extracción]]
  - [[09 Minijuegos]]
  - [[04 Progresión y meta]]
  - [[07 Sociedad, poder y eventos]]
  - [[08 Historia y personaje]]
  - [[10 Técnico y herramientas]]
  - [[12 Dirección de arte]]
  - [[ADR-0009 PC primero (Steam) y móvil después]]
- **Citado por:** [[01 Core loop y ciclo del día]], [[03 Comercio y mercado]], [[10 Técnico y herramientas]], [[16 Calidad y QA]], [[ADR-0001 Godot 4.x con GDScript como motor]], [[ADR-0009 PC primero (Steam) y móvil después]]

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:1`
