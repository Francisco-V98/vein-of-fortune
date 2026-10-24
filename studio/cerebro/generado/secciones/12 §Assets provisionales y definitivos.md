---
id: "doc-12-assets-provisionales-y-definitivos"
tipo: "seccion"
title: "Assets provisionales y definitivos ✅"
aliases: ["doc-12-assets-provisionales-y-definitivos"]
documento: "[[12 Dirección de arte]]"
limpieza: 89
abiertos: 4
espera: 1
aplazado_a: ["[[F4-233 Mapa de Valdoria definitivo en pixel art]]"]
estado: "con-abiertos"
anterior: "[[12 §Hojas de personajes y NPC]]"
siguiente: "[[12 §Decisiones técnicas de arte pendientes]]"
arriba: "[[12 Dirección de arte]]"
fuente: "studio/docs/12-direccion-de-arte.md:176"
generado: true
---

# Assets provisionales y definitivos ✅

> 1. No se invierte tiempo ni créditos en pulir lo provisional. Si no sirve para la prueba, se genera otro barato o se usa una forma simple…

← [[12 §Hojas de personajes y NPC]] · [[12 Dirección de arte|↑ 12]] · [[12 §Decisiones técnicas de arte pendientes]] →

### Política del autor ✅ (2026-10-13)

- ✅ Todo lo gráfico que existe hoy, **hasta el logo**, se rehará después: personajes, minerales, escenas, ambiente y animaciones.
- ✅ Todo el arte definitivo se hará en **pixel art con la herramienta PixelLab**.
- ✅ Lo que hay ahora sirve de **referencia o de uso interno**. Se reemplaza por cosas reales después de hacer pruebas y comprobar que todo funciona a la perfección.
- ✅ Habrá un momento en que se necesiten los assets reales (píxeles, imágenes, voces, etc.) para la **producción final**, no para pruebas y testeos. Antes de ese momento, el objetivo es **fallar barato y rápido**.
- ✅ Para el storyboard del Acto I ([[F0-24 Storyboard de las escenas clave del Acto I|F0-24]]): los personajes ya hechos y los minerales se reutilizan como referencia; los escenarios y los momentos se rehacen de forma barata.

### Qué es provisional y qué es definitivo ✅

| | Provisional | Definitivo |
|---|---|---|
| Para qué sirve | Referencia, pruebas, prototipo, vertical slice, storyboard y uso interno | Producción final del juego y de la tienda |
| Cómo se hace | Generado barato (calidad baja, pocas iteraciones), a partir de las referencias aprobadas | Pixel art con PixelLab; voces y audio finales |
| Acabado | Sin pulir; no se limpia ni se reconstruye | Revisado por el director de arte y aprobado por el autor |
| Cuánto se invierte | Lo mínimo: ni tiempo ni créditos de más | Presupuesto de producción propio, estimado tras la prueba de PixelLab |
| Cómo se marca | `estado: provisional` en `studio/data/assets.json` | `estado: definitivo` en `studio/data/assets.json` |
| Cuándo | Desde ya hasta la Puerta B | Solo después de que el vertical slice pase las pruebas y la Puerta B, y cuando el autor lo autorice |
| Llega a la tienda | ❌ Nunca | ✅ Sí |

### Qué es provisional hoy ✅

| Asset | Dónde está | Estado | En pruebas y storyboards |
|---|---|---|---|
| Hojas de personajes y NPC (modelo, expresiones y poses; protagonistas, elenco, 35 NPC y jefes) | `studio/assets-ref/personajes/`, `npc/` | Provisional ✅ | ✅ Se reutilizan como referencia |
| Minerales (`minerales-v2.png`) | `studio/assets-ref/prueba-de-estilo-2/` | Provisional ✅ | ✅ Se reutilizan como referencia |
| Retratos y sprites de la prueba de estilo | `prueba-de-estilo-2/` | Provisional ✅ | ✅ Referencia de diseño |
| Pruebas de estilo (rondas 1 y 2) y su paleta | `prueba-de-estilo/`, `prueba-de-estilo-2/` | Provisional ✅ | ✅ Referencia de dirección; la paleta de este documento sigue vigente |
| Escenarios (mina, zonas, edificios, tienda, interfaz de mercado y minijuegos) | `prueba-de-estilo-2/` | Provisional ✅ | ✅ Solo referencia de atmósfera; los del storyboard se generan nuevos y baratos |
| Momentos (escenas clave del Acto I) | No existen aún | — | ✅ Se generan nuevos y baratos para el storyboard |
| Mapa de Valdoria (`mapa-valdoria.png`) | `prueba-de-estilo-2/` | Provisional ✅ | Se regenera ahora, barato y con las zonas actuales (Altafría, Salinas Blancas y la capital) ✅ (decisión del autor, 2026-10-13); el definitivo se rehace en pixel art ⏳ [[F4-233 Mapa de Valdoria definitivo en pixel art\|F4-233]] |
| Logo y wordmark, íconos de app | `studio/assets-ref/marca/` | Provisional ✅ | ✅ Uso interno (hub, README y pruebas) |
| Íconos (minerales, herramientas, interfaz) | Recortes de las rondas de prueba | Provisional ✅ | ✅ Referencia de siluetas y colores |
| Ambiente y animaciones (ciclos de caminar de las hojas de poses) | Hojas de poses | Provisional ✅ | ✅ Referencia de movimiento |
| Audio y voces | Aún no hay | — | Todo lo que se haga de prueba es provisional |

### Reglas de uso 🟡

1. **No se invierte tiempo ni créditos en pulir lo provisional.** Si no sirve para la prueba, se genera otro barato o se usa una forma simple con los colores de la paleta ✅.
2. **Todo asset nuevo de prueba se marca provisional** en `studio/data/assets.json` con el campo `estado` (`provisional` o `definitivo`). Lo que no tenga el campo cuenta como provisional (`estado_por_defecto`).
3. **Nada provisional llega a la tienda**: ni capturas, ni ícono de la app, ni arte clave, ni kit de prensa ✅.
4. **La producción definitiva empieza cuando el autor la autoriza**, después de que el vertical slice pase las pruebas y la Puerta B ([[F3-23 Prueba de la tajada y decisión de seguir hacia la v1|F3-23]]). Antes no se produce arte final, voces ni audio final.
5. **Lo provisional también cumple las reglas de dirección de arte**: paleta, regla del éter, accesibilidad sin rojo y verde, y nada de texto dentro del arte, salvo el wordmark del logo. Así el reemplazo no cambia el diseño.
6. **Lo provisional se conserva como referencia** (rasgos, siluetas y colores) y no se edita a mano. Al reemplazarlo, el definitivo toma su lugar en el juego y el provisional queda en `studio/assets-ref/` como histórico.
7. **El registro de licencias incluye lo provisional**, porque sigue siendo contenido generado por IA ([[11 Legal y cumplimiento|11]]).

### De la prueba barata a lo definitivo 🟡

1. **Generar barato**: calidad baja, a partir de las referencias aprobadas.
2. **Marcar** `estado: provisional` en `assets.json`.
3. **Probar** en el prototipo, el vertical slice o el storyboard.
4. **Puerta B** ([[F3-23 Prueba de la tajada y decisión de seguir hacia la v1|F3-23]]): el vertical slice pasa las pruebas y el autor decide seguir.
5. **Autorización del autor** para empezar la producción definitiva.
6. **Prueba de PixelLab** con un personaje, un mineral y un fondo: flujo, estilo, paleta, tamaños y precio.
7. **Producción por lotes** en PixelLab, con lo provisional como referencia.
8. **Revisión** del director de arte contra este documento y aprobación del autor.
9. **Reemplazo**: se marca `estado: definitivo`, se registra la licencia y se sustituye lo provisional en el juego.

### PixelLab, herramienta del arte definitivo ✅

PixelLab es la herramienta del arte definitivo por decisión del autor. Su flujo de trabajo, estilo, paleta, tamaños y precio se prueban en la **primera tarea de producción definitiva** (paso 6 del flujo). 🟡 Hasta entonces no se contrata ni se gastan créditos en ella. Los tamaños de personajes, íconos y fondos quedan 🟡 hasta esa prueba; los valores actuales (unos 100 píxeles de alto por personaje, ver «Estética chibi de referencia») son los de las referencias, no los del arte definitivo.

## Fuente

`studio/docs/12-direccion-de-arte.md:176`
