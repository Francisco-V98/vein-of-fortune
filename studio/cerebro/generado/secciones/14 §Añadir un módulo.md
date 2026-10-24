---
id: "doc-14-anadir-un-modulo"
tipo: "seccion"
title: "Añadir un módulo 🟡"
aliases: ["doc-14-anadir-un-modulo"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Verificación automática]]"
siguiente: "[[14 §Límites conocidos]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:189"
generado: true
---

# Añadir un módulo 🟡

> 1. Declararlo en game/architecture.json con sus dependson (y su ADR si introduce una decisión nueva).

← [[14 §Verificación automática]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Límites conocidos]] →

1. Declararlo en `game/architecture.json` con sus `depends_on` (y su ADR si introduce una decisión nueva).
2. Crear su estructura de carpetas con el generador (tarea [[F1-28 Generador de módulos|F1-28]]).
3. Escribir primero el dominio y sus pruebas; luego aplicación; después infraestructura y presentación.
4. Exponer solo lo necesario en `api/`.
5. Registrarlo en la raíz de composición.
6. Ejecutar el verificador de arquitectura y las pruebas.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:189`
