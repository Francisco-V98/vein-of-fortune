---
id: "doc-14-principios"
tipo: "seccion"
title: "Principios ✅"
aliases: ["doc-14-principios"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Requisitos del autor]]"
siguiente: "[[14 §Estructura de `game - `]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:9"
generado: true
---

# Principios ✅

> 1. Regla de dependencia: las dependencias apuntan hacia el dominio. El dominio no conoce a nadie.

← [[14 §Requisitos del autor]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Estructura de `game - `]] →

1. **Regla de dependencia:** las dependencias apuntan hacia el dominio. El dominio no conoce a nadie.
2. **Alta cohesión, bajo acoplamiento:** cada módulo hace una cosa y se conecta con otros por contratos pequeños.
3. **Dependencias explícitas:** nada se busca en un global; todo se entrega desde fuera (inyección de dependencias).
4. **Datos antes que código:** el contenido (minerales, zonas, eventos, textos) vive en datos validados, no en el código.
5. **Determinismo:** la simulación usa una semilla y un reloj inyectados, para reproducir partidas y errores.
6. **Una razón para cambiar:** una clase, una responsabilidad; un módulo, un propósito.
7. **Composición sobre herencia:** se combinan piezas pequeñas.
8. **Verificación automática:** las reglas se comprueban en CI; lo que no se verifica se erosiona.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:9`
