---
id: "doc-01-ritmo-de-sesion-y-guardado"
tipo: "seccion"
title: "Ritmo de sesión y guardado ✅"
aliases: ["doc-01-ritmo-de-sesion-y-guardado"]
documento: "[[01 Core loop y ciclo del día]]"
limpieza: 86
abiertos: 1
espera: 3
aplazado_a: ["[[F2-01 Modelo de estado de partida y semilla]]", "[[F2-03 Guardado y carga versionado con escritura segura]]"]
estado: "con-abiertos"
anterior: "[[01 §Estructura del día]]"
siguiente: "[[01 §Ciclo macro]]"
arriba: "[[01 Core loop y ciclo del día]]"
fuente: "studio/docs/01-core-loop.md:56"
generado: true
---

# Ritmo de sesión y guardado ✅

> Estado: el punto de control, las 5 partidas guardables y el azar fijado en el punto de control están confirmados (decisión del autor…

← [[01 §Estructura del día]] · [[01 Core loop y ciclo del día|↑ 01]] · [[01 §Ciclo macro]] →

**Estado:** el punto de control, las 5 partidas guardables y el azar fijado en el punto de control están confirmados (decisión del autor, 2026-10-15).

🟡 En PC (y en la Steam Deck) las sesiones pueden ser más largas que las de un móvil, así que ya no se diseña para sesiones de 5–10 minutos. Meta de diseño propuesta: **un día completo se puede jugar de seguido** y el jugador decide cuántos días juega en cada sesión; la duración objetivo de una sesión sigue abierta hasta el prototipo.

- ✅ **Punto de control al iniciar cada acción.** El juego se puede cerrar en cualquier momento: al volver se retoma desde el inicio de la última acción, y lo que estaba en curso (un minijuego a medias, por ejemplo) se vuelve a empezar.
- ✅ **Hasta 5 partidas guardables**, y el jugador **elige cuál jugar** al abrir el juego. El estado de partida ⏳ [[F2-01 Modelo de estado de partida y semilla|F2-01]] y el guardado ⏳ [[F2-03 Guardado y carga versionado con escritura segura|F2-03]] lo construyen así ([[10 Técnico y herramientas|10]], [[14 Arquitectura y modularidad|14]]). En Steam se sincronizan con Auto-Cloud, y en Hardcore manda el guardado local.
- ✅ **El azar queda fijado al guardar el punto de control.** Cerrar y reabrir a mitad de una acción no repite la tirada, para que nadie esquive una derrota (sobre todo en Hardcore) recargando. El estado de partida lo guarda ⏳ [[F2-01 Modelo de estado de partida y semilla|F2-01]].
- ✅ Se puede cerrar o suspender en cualquier momento sin perder progreso (autoguardado instantáneo): la Steam Deck suspende y no se quiere perder avance (decisión del autor, 2026-10-15).
- ✅ **Tiempo de juego:** un día completo dura **12–15 minutos** (≈ 13 nominales) y cada bloque **≈ 4–5 minutos**. La semana son 7 días y el **mes y la estación duran 28 días** cada uno (4 estaciones por año); de ahí sale la duración de cada acto ([[17 Mapa de historia|17]], [[28 Números base de la economía|28]]).
- ✅ **Calendario de arranque:** el día 1 es el 22 de otoño, así que el invierno empieza el día 8, el primer día del Acto II ([[28 Números base de la economía|28]]).

## Fuente

`studio/docs/01-core-loop.md:56`
