---
id: "doc-24-s10"
tipo: "seccion"
title: "10 · La red anti-atasco ✅"
aliases: ["doc-24-s10"]
documento: "[[24 Umbrales de acto]]"
limpieza: 100
abiertos: 0
espera: 7
aplazado_a: ["[[F0-78 Diseñar el diario, la cola de historia y la misión de]]", "[[F4-109 Escalera de estatus y condiciones de ascenso]]"]
estado: "con-aplazados"
anterior: "[[24 §9 Las cintas 1 a 5 y la puerta al IV]]"
siguiente: "[[24 §11 Casos «no cumples nada»]]"
arriba: "[[24 Umbrales de acto]]"
fuente: "studio/docs/24-umbrales-de-acto.md:216"
generado: true
---

# 10 · La red anti-atasco ✅

> Estado: qué piezas existen y qué hacen está decidido; su diseño F0-78. La deuda nunca bloquea, y eso está decidido.

← [[24 §9 Las cintas 1 a 5 y la puerta al IV]] · [[24 Umbrales de acto|↑ 24]] · [[24 §11 Casos «no cumples nada»]] →

**Estado:** qué piezas existen y qué hacen está decidido; su diseño ⏳ [[F0-78 Diseñar el diario, la cola de historia y la misión de|F0-78]]. La deuda nunca bloquea, y eso está decidido.

| Pieza | Qué hace ✅ | Diseño |
|---|---|---|
| **Sandbox** | Si no cumples una puerta, el juego sigue: minas, vendes, exploras y comercias | Ya existe como modo de juego |
| **Cola de historia** | La escena que no se puede disparar espera; no se pierde ni caduca | ⏳ [[F0-78 Diseñar el diario, la cola de historia y la misión de\|F0-78]] |
| **Diario** | Lista las vías que faltan para pasar de acto, con lo que ya cumples | ⏳ [[F0-78 Diseñar el diario, la cola de historia y la misión de\|F0-78]] |
| **Misión de rescate** | Llega tras mucho tiempo sin avanzar | ⏳ [[F0-78 Diseñar el diario, la cola de historia y la misión de\|F0-78]]. Cuánto tiempo, en horas de juego ✅ ([[F0-53 Simulador de economía y progresión con reglas de equilibrio\|F0-53]], con las cifras aprobadas el 2026-10-16): **13,5 h** acumuladas para la puerta A5 y **26,5 h** para el círculo (1,25 × el percentil 95 del jugador lento, redondeado a 0,5 h; [[28 Números base de la economía\|28]] sección 13; viven en `world.json`, [[Misión de rescate\|economy.rescue_mission]]) |

- **Restricciones para las tareas que lo diseñan** (⏳ [[F0-78 Diseñar el diario, la cola de historia y la misión de|F0-78]] y ⏳ [[F4-109 Escalera de estatus y condiciones de ascenso|F4-109]]).
  - Misión de rescate ([[F0-78 Diseñar el diario, la cola de historia y la misión de|F0-78]]): señala qué falta y cómo; no concede estatus, logros ni medidores.
  - Estatus ⏳ [[F4-109 Escalera de estatus y condiciones de ascenso|F4-109]]: subir a Comerciante o a Empresario no puede exigir una escena de historia ni una puerta, para no crear un ciclo. Una vez cumplido el piso de una puerta, no se pierde por una pérdida de dinero ni por suspender la licencia ✅ (decisión del autor, 2026-10-15).
  - Mora ✅: con 4 semanas de atraso acumuladas la tasa sube +1 pp hasta que pagues una cuota completa y Reme deja de fiar la gestión. Nunca cierra una puerta ([[28 Números base de la economía|28]]).

---

## Fuente

`studio/docs/24-umbrales-de-acto.md:216`
