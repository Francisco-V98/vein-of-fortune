---
id: "doc-02-minijuegos-de-extraccion"
tipo: "seccion"
title: "Minijuegos de extracción"
aliases: ["doc-02-minijuegos-de-extraccion"]
documento: "[[02 Extracción]]"
limpieza: 100
abiertos: 0
espera: 8
aplazado_a: ["[[F2-14 Picado (fuerza y precisión)]]", "[[F2-15 Perforación (velocidad y calor)]]", "[[F3-10 Peligros ambientales de la zona 1 y tareas de peligro]]", "[[F4-44 Cincelado - implementación y variante con mando]]", "[[F4-46 Cribado - implementación y variante con mando]]", "[[F4-48 Detonación - implementación y variante con mando]]", "[[F4-53 Tarea de peligro - reparar equipo (conectar cables)]]"]
estado: "con-aplazados"
anterior: "[[02 §Fallos y daño a la mena]]"
siguiente: "[[02 §Peligros y enemigos]]"
arriba: "[[02 Extracción]]"
fuente: "studio/docs/02-extraccion.md:106"
generado: true
---

# Minijuegos de extracción

> Varios tipos, simples, alineados con el juego. Inspiración: pesca de Stardew Valley (equilibrar dos parámetros hasta un punto óptimo, ej…

← [[02 §Fallos y daño a la mena]] · [[02 Extracción|↑ 02]] · [[02 §Peligros y enemigos]] →

✅ Varios tipos, simples, alineados con el juego. Inspiración: pesca de Stardew Valley (equilibrar **dos parámetros** hasta un punto óptimo, ej. fuerza vs. precisión) y minijuegos cortos tipo Among Us.

### Catálogo inicial ✅

**Estado:** los cinco minijuegos de extracción y su acto de entrada están confirmados en el registro del mundo (`world.json`), y que son de dos parámetros en tensión (con la excepción del Cincelado) lo está en [[09 Minijuegos|09]]. La mecánica fina de cada uno se fija al construirlo: ⏳ [[F2-14 Picado (fuerza y precisión)|F2-14]] y ⏳ [[F2-15 Perforación (velocidad y calor)|F2-15]] (Picado y Perforación), ⏳ [[F4-44 Cincelado - implementación y variante con mando|F4-44]] (Cincelado), ⏳ [[F4-46 Cribado - implementación y variante con mando|F4-46]] (Cribado) y ⏳ [[F4-48 Detonación - implementación y variante con mando|F4-48]] (Detonación).

| Minijuego | Mecánica | Parámetros |
|---|---|---|
| Picado | Timing de golpe | Fuerza ↔ precisión |
| Perforación | Mantener zona óptima | Velocidad ↔ calor (sobrecalentamiento) |
| Cincelado | Trazar líneas de corte | Precisión pura (gemas) ⏳ [[F4-44 Cincelado - implementación y variante con mando\|F4-44]] |
| Cribado / lavado | Mantener flujo | Inclinación ↔ caudal (como la pesca) |
| Detonación | Colocar carga | Potencia ↔ ubicación (riesgo de dañar la mena) |

Cada tipo de mineral/dureza se asocia a un minijuego. Detalle completo, automatización y MVP: ver [[09 Minijuegos|09-minijuegos.md]].

### Tareas de peligro (estilo Among Us) ✅

Para afrontar peligros ambientales: sellar una fuga de gas (secuencia), apuntalar un techo (patrón), reparar una herramienta (conectar piezas). Los nombres de las tres tareas están en el glosario ([[18 Biblia narrativa|18]]); su mecánica ⏳ [[F3-10 Peligros ambientales de la zona 1 y tareas de peligro|F3-10]] y ⏳ [[F4-53 Tarea de peligro - reparar equipo (conectar cables)|F4-53]] ([[09 Minijuegos|09]]).

## Fuente

`studio/docs/02-extraccion.md:106`
