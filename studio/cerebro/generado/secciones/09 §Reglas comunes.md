---
id: "doc-09-reglas-comunes"
tipo: "seccion"
title: "Reglas comunes ✅"
aliases: ["doc-09-reglas-comunes"]
documento: "[[09 Minijuegos]]"
limpieza: 75
abiertos: 2
espera: 8
aplazado_a: ["[[F1-07 Capa de entrada por acciones - ratón, teclado y mando]]", "[[F2-13 Resultado de extracción - rendimiento, daño y pérdida]]", "[[F2-16 Zona óptima según herramienta y Pericia]]", "[[F4-44 Cincelado - implementación y variante con mando]]", "[[F4-57 Modificador de mena - costra]]", "[[F4-58 Modificador de mena - inestable]]", "[[F4-59 Modificador de mena - veta rica]]"]
estado: "con-abiertos"
siguiente: "[[09 §Automatización de minijuegos (a probar en prototipo)]]"
arriba: "[[09 Minijuegos]]"
fuente: "studio/docs/09-minijuegos.md:3"
generado: true
---

# Reglas comunes ✅

> Estado: confirmado que son simples, variados, de dos parámetros en tensión (con dos excepciones), con controles táctiles y de mando (10) y…

[[09 Minijuegos|↑ 09]] · [[09 §Automatización de minijuegos (a probar en prototipo)]] →

**Estado:** confirmado que son simples, variados, de dos parámetros en tensión (con dos excepciones), con controles táctiles y de mando ([[10 Técnico y herramientas|10]]) y que la mejor herramienta los facilita; la duración ✅ (8–15 segundos) y la zona óptima ⏳ [[F2-16 Zona óptima según herramienta y Pericia|F2-16]].

- ✅ Minijuegos simples, variados (estilo Dave the Diver), alineados con el juego. Inspiración: pesca de Stardew Valley y minijuegos de Among Us.
- ✅ **Cortos:** 8–15 segundos (se cuadra con el día de 12–15 minutos y el bloque de ≈ 4–5; [[01 Core loop y ciclo del día|01]], [[17 Mapa de historia|17]], [[28 Números base de la economía|28]]). Con unas pocas menas por expedición (2 a 3 al principio, hasta 10 por bloque en el Acto IV; [[02 Extracción|02]]), los minijuegos de un bloque suman unos minutos y caben en cualquier sesión de PC o de Steam Deck.
- 🟡 **Controles simples en ratón, teclado y mando:** mantener pulsado (clic izquierdo, una tecla o un botón del mando), soltar, arrastrar con el cursor y pulsar en el momento justo; con mando hay una variante de cada uno (⏳ [[F1-07 Capa de entrada por acciones - ratón, teclado y mando|F1-07]]). El táctil (mantener pulsado, arrastrar con el dedo y tocar) es una variante de la fase móvil, después de la 1.0 (decisión del autor, 2026-10-15).
- 🟡 **Dos parámetros en tensión** (fuerza ↔ precisión, etc.). Dos excepciones, porque no hay nada que equilibrar: el **Cincelado** es de precisión pura (si pasa a dos parámetros ⏳ [[F4-44 Cincelado - implementación y variante con mando|F4-44]]) y **Tasar** es de observación: se juega con el Ojo, no con parámetros.
- ✅ Mejor herramienta → el minijuego es más fácil o la zona óptima más amplia.
- La zona óptima depende del nivel de la herramienta, la **Pericia** del jugador y la dureza del mineral. ⏳ [[F2-16 Zona óptima según herramienta y Pericia|F2-16]] Cómo se calcula.

### Resultado ✅

Cada minijuego tiene **4 resultados posibles** (decisión del autor, 2026-10-15), los mismos de [[02 Extracción|02]]:

| Resultado | Rendimiento (orientativo) | Daño a la mena | Desgaste de herramienta |
|---|---|---|---|
| Perfecto | Alto, con bonus | Ninguno | Mínimo |
| Bueno | Normal | Bajo | Normal |
| Regular | Reducido | Medio | Alto |
| Fallo | Muy bajo | La mena se daña o se pierde | Muy alto |

Los números son ilustrativos y se calibran en el prototipo ⏳ [[F2-13 Resultado de extracción - rendimiento, daño y pérdida|F2-13]].

### Contra la repetición ✅

1. Cada mineral usa un minijuego distinto según su dureza y herramienta.
2. **Modificadores de mena** que cambian las reglas: *costra* (requiere un golpe previo), *inestable* (el marcador se mueve de forma errática), *veta rica* (zona extra de bonus). El diseño de cada uno ⏳ [[F4-57 Modificador de mena - costra|F4-57]], ⏳ [[F4-58 Modificador de mena - inestable|F4-58]] y ⏳ [[F4-59 Modificador de mena - veta rica|F4-59]].
3. Automatización cuando el jugador domina (ver abajo).
4. Los empleados hacen el trabajo repetitivo sin minijuego (ver [[04 Progresión y meta|04]]).

## Fuente

`studio/docs/09-minijuegos.md:3`
