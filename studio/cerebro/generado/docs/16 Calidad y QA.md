---
id: "doc-16"
tipo: "documento"
title: "16 · Calidad y QA"
aliases: ["doc-16"]
estado: "con-abiertos"
limpieza: 37
ok: 7
propuestas: 10
abiertos: 12
espera: 7
secciones: 15
arriba: "[[MOC Documentos]]"
fuente: "studio/docs/16-calidad-y-qa.md:1"
generado: true
---

# 16 · Calidad y QA

> Limpieza 37 % · 12 abiertos · 15 secciones

## Secciones

1. [[16 §Requisito del autor]] — El QA es un proceso dentro del flujo de trabajo: revisiones, pruebas funcionales, pruebas en general, seguridad y lo que haga falta. No es…
2. [[16 §Principios]] — 1. Calidad desde el principio: se previene antes de detectar. La arquitectura modular y las pruebas del dominio son la primera defensa (14).
3. [[16 §El QA en el flujo]]
4. [[16 §Tipos de verificación]]
5. [[16 §Seguridad en QA]] — Lista de verificación adaptada de OWASP MASVS (estándar de seguridad para aplicaciones móviles, que sigue siendo una buena guía) a un juego…
6. [[16 §Casos de prueba]]
7. [[16 §Errores]] — Cada error es un archivo en studio/data/qa/bugs/BUG-NNNN.json con título, severidad, estado, versión donde apareció, pasos para…
8. [[16 §Criterios de salida de una versión]]
9. [[16 §Plan de QA por fase]]
10. [[16 §Matriz de PC]] — Decisión del autor (2026-10-15): se prueba en un PC Windows real y en la Steam Deck si la hay (ADR-0009). Es un requisito de F1.
11. [[16 §Presupuestos de rendimiento (a medir en PC F1-44)]] — No hay cifras definitivas: se miden en la matriz de PC con la tarea F1-44 y recién entonces se fijan los límites.
12. [[16 §Fase móvil (después de la 1.0)]] — Se conserva lo previsto para Android y se retoma cuando empiece el móvil (10, «Fase móvil»).
13. [[16 §Métricas de calidad]] — Aprobación de casos, errores por severidad, errores que llegaron a una versión, cobertura del dominio, sesiones sin cierres y tiempo de…
14. [[16 §Responsabilidades]] — Límite honesto: Claude no puede jugar en el PC de pruebas ni sentir si algo es divertido o fluido. Esa parte de QA es del autor.
15. [[16 §Pendiente]]

## Puntos abiertos

- [[16 §Requisito del autor]] (línea 6): Los principios son requisitos; los umbrales y los detalles están marcados 🟡 y se afinan con el prototipo ([ADR-0008](adr/0008-qa-como-etapa-del-flujo.md)).
- [[16 §Seguridad en QA]] (línea 60): Lista de verificación adaptada de OWASP MASVS (estándar de seguridad para aplicaciones móviles, que sigue siendo una buena guía) a un juego de PC sin conexión ni cuentas propias 🟡:
- [[16 §Errores]] (línea 88): ### Severidad 🟡
- [[16 §Matriz de PC]] (línea 135): ❓ Falta definir los equipos reales: el autor trabaja en Mac, así que el PC Windows (que tiene o consigue) y la Steam Deck, si la hay, son la base; el resto de la matriz se completa con máquinas virtua
- [[16 §Fase móvil (después de la 1.0)]] (línea 158): Rendimiento / Arranque en frío ≤ 5 s en gama media; 60 cuadros por segundo en interfaz y mínimo 30 en minijuegos; descarga ≤ 150 MB; batería y calor a medir (los números del plan anterior son 🟡 y se r

## Relaciones

- **Aplazados a:** [[F1-06 Resolución base, escalado entero y modos de pantalla]], [[F1-44 Presupuestos de rendimiento medidos en PC]]
- **Enlaza a:** [[ADR-0008 El QA es una etapa propia del flujo de trabajo]], [[14 Arquitectura y modularidad]], [[15 Flujo de trabajo y calidad]], [[ADR-0009 PC primero (Steam) y móvil después]], [[10 Técnico y herramientas]], [[ADR-0007 Telemetría local exportable, Play Vitals y envío opcional futuro]]
- **Citado por:** [[10 Técnico y herramientas]], [[15 Flujo de trabajo y calidad]], [[ADR-0009 PC primero (Steam) y móvil después]]

## Fuente

`studio/docs/16-calidad-y-qa.md:1`
