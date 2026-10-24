---
id: "adr-0003"
tipo: "adr"
title: "ADR-0003 · Arquitectura modular por cortes verticales y capas"
aliases: ["adr-0003"]
estado: "Aceptada"
limpieza: 100
ok: 1
propuestas: 0
abiertos: 0
espera: 0
secciones: 4
fecha: "2026-10-11"
arriba: "[[MOC ADR]]"
fuente: "studio/docs/adr/0003-arquitectura-modular.md:1"
generado: true
---

# ADR-0003 · Arquitectura modular por cortes verticales y capas

> Limpieza 100 % · 0 abiertos · 4 secciones

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-11

## Secciones

1. [[ADR-0003 §Contexto]] — El autor exige un proyecto muy modular, sin dependencias directas, escalable, con independencia entre partes y buenas prácticas de diseño y…
2. [[ADR-0003 §Decisión]] — Cada funcionalidad es un módulo con capas domain, application, infrastructure, presentation y api. Las dependencias apuntan hacia el…
3. [[ADR-0003 §Alternativas consideradas]]
4. [[ADR-0003 §Consecuencias]] — Más disciplina y carpetas al inicio a cambio de poder cambiar un módulo sin romper otros, probar el dominio sin Godot y sumar plataformas o…

## Relaciones

- **Citado por:** [[14 Arquitectura y modularidad]], [[ADR-0009 PC primero (Steam) y móvil después]]

## Fuente

`studio/docs/adr/0003-arquitectura-modular.md:1`
