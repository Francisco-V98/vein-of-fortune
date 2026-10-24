---
id: "doc-15"
tipo: "documento"
title: "15 · Flujo de trabajo y calidad"
aliases: ["doc-15"]
estado: "con-abiertos"
limpieza: 48
ok: 16
propuestas: 14
abiertos: 17
espera: 0
secciones: 18
arriba: "[[MOC Documentos]]"
fuente: "studio/docs/15-flujo-de-trabajo-y-calidad.md:1"
generado: true
---

# 15 · Flujo de trabajo y calidad

> Limpieza 48 % · 17 abiertos · 18 secciones

## Secciones

1. [[15 §Requisito del autor]] — Trabajar por ramas, de forma muy organizada, cumpliendo la metodología de clean code. Este documento define cómo. El modelo concreto de…
2. [[15 §Modelo de ramas]] — GitHub Flow con ramas de versión. main siempre está sano; todo el trabajo entra por ramas cortas y pull requests.
3. [[15 §Commits]] — Convención Conventional Commits en español, con el ID de la tarea:
4. [[15 §Flujo de una tarea]] — 1. Elegir la tarea del Sprint y moverla a doing registrando la rama en el historial.
5. [[15 §Pull requests]]
6. [[15 §Integración continua]] — Se ejecuta en cada PR y en cada cambio de main (.github/workflows/ci.yml):
7. [[15 §Definición de listo y de terminado]] — Lista para empezar (Definition of Ready): tiene descripción y "listo cuando", prioridad, estimación de hasta 20 horas y no depende de algo…
8. [[15 §Limpieza del diseño]] — Requisito del autor: todo debe quedar acordado, sin ambigüedades, y todo debe conectar y funcionar bien. Solo puede quedar sin cerrar lo…
9. [[15 §Pruebas]]
10. [[15 §Versionado y publicación]]
11. [[15 §Decisiones de arquitectura (ADR)]] — Toda decisión que afecte la estructura, una dependencia o un proceso se registra en studio/docs/adr/NNNN-titulo.md con contexto, decisión…
12. [[15 §Deuda técnica]]
13. [[15 §Seguridad en el flujo]]
14. [[15 §Trabajo con IA]]
15. [[15 §Coste de la IA]] — Decisión del autor (2026-10-23, ADR-0010). Las reglas completas están en CLAUDE.md; este es el resumen:
16. [[15 §Ajustes de GitHub que hace el autor]] — En Settings → Branches → Branch protection rule para main:
17. [[15 §QA en el flujo]] — El QA es una etapa propia, entre la revisión y el cierre. Procedimiento completo, tipos de prueba, seguridad, errores y criterios de salida…
18. [[15 §Pendiente]]

## Puntos abiertos

- [[15 §Requisito del autor]] (línea 4): Trabajar por ramas, de forma muy organizada, cumpliendo la metodología de clean code. Este documento define cómo. El modelo concreto de ramas está marcado 🟡 hasta que lo confirmes ([ADR-0005](adr/0005
- [[15 §Pull requests]] (línea 86): ### Lista de revisión 🟡
- [[15 §Limpieza del diseño]] (línea 136): Limpieza de un documento / ✅ ÷ (✅ + 🟡 + ❓), en porcentaje. También se calcula para todo el diseño
- [[15 §Limpieza del diseño]] (línea 139): Meta / 🟡 Como mínimo 90 % por documento (umbral propuesto) y acercarse al 100 %
- [[15 §Limpieza del diseño]] (línea 160): 1. Un documento nuevo no se da por terminado mientras tenga puntos 🟡 o ❓ que se puedan decidir ya. Lo que no se puede decidir todavía se marca como diferido, con la tarea de la que depende.
- [[15 §Limpieza del diseño]] (línea 163): 4. 🟡 Más adelante la integración continua impedirá que la limpieza de un documento baje respecto de .

## Relaciones

- **Aplazados a:** [[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y]]
- **Enlaza a:** [[ADR-0005 GitHub Flow con ramas de versión y Conventional Commits]], [[16 Calidad y QA]], [[20 Equipo y flujo de agentes]], [[12 Dirección de arte]], [[10 Técnico y herramientas]], [[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]
- **Citado por:** [[10 Técnico y herramientas]], [[16 Calidad y QA]], [[20 Equipo y flujo de agentes]], [[28 Números base de la economía]], [[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]

## Fuente

`studio/docs/15-flujo-de-trabajo-y-calidad.md:1`
