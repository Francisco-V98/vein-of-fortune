# ADR-0012 · Módulo `tutorial` para pasos guiados y compuertas; logros dentro de `progression`

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-24

## Contexto

El autor decidió el 2026-10-24 que todo proceso de primera vez y todo paso obligatorio lleva un **tutorial guiado** y una **compuerta**, sin saltos y sin softlock (inventario en [27](../27-guion-del-acto-i.md), sección 2.4). En el mapa de módulos de [14](../14-arquitectura-y-modularidad.md) ningún módulo alojaba esos pasos guiados. Además, el documento 14 decía a la vez que `progression` incluye los logros y que los logros «entrarán más adelante creando su propio módulo», mientras F4-235 los implementa dentro de F4. La revisión técnica de F0-57 detectó las dos cosas.

## Decisión ✅

Decisiones del autor (2026-10-24):

1. **Logros dentro de `progression`.** El módulo que mide el avance del jugador define el catálogo de logros y los emite como datos; solo el adaptador de tienda los envía a Steam (puerto de plataforma/tienda, [ADR-0009](0009-pc-primero-movil-despues.md)). Esto **reemplaza** la frase anterior del documento 14 que preveía un módulo propio de logros. El casino sigue previsto como módulo propio (V2.0, F6-01).
2. **Nuevo módulo `tutorial`**, que depende solo de `day` y de los eventos de `story`. Aloja los pasos guiados y las compuertas de la sección 2.4 del documento 27.

Diseño técnico que se deriva (arquitecto, misma fecha):

- **Qué guarda `tutorial`:** el catálogo de pasos guiados como datos (identificador estable, escena que lo abre, ancla de interfaz que se resalta, acción que lo completa, remedio si falla: reintento, recordatorio o práctica sin costo), el estado de cada paso (pendiente, activo, completado) y la regla «se completa una vez». Ofrece `snapshot()` y `restore()` para el guardado.
- **Qué publica en su `api`:** la consulta del paso activo y los eventos `PasoGuiadoIniciado`, `PasoGuiadoCompletado` y `RecordatorioPedido`.
- **Qué escucha:** `EscenaIniciada` de `story` (abre el paso ligado a esa escena) y el avance de bloque y día de `day` (recordatorios).
- **Cómo sabe que el jugador hizo la acción** sin depender de cada módulo que enseña: su capa `application` declara el puerto `AccionesDelJugador`, que recibe identificadores neutros de acción como datos (`accion.vender`, `accion.mejorar_herramienta`). Lo implementa un **puente de composición** en `app/puentes/`, que escucha los eventos de las `api` de `shop`, `extraction`, `crafting` y demás y los traduce a esos identificadores.
- **Cómo frena la compuerta:** la cola de escenas de `story` (⏳ F3-48) declara el puerto `CompuertasDeCola` («¿se cumplió la compuerta X?»), que implementa otro puente de `app/puentes/` leyendo la `api` de `tutorial`. Así `story` no depende de `tutorial` y el grafo sigue acíclico (A7): la escena siguiente espera y nunca se descarta.
- **Reglas de los puentes:** viven solo en `app/` (la raíz de composición, que ya puede conocerlo todo), usan solo las `api` de los módulos, solo traducen eventos o consultas (sin reglas del juego) y se listan en la tabla «Puentes de composición» del documento 14.
- **Presentación:** el marcador y el resaltado los dibuja `tutorial/presentation` con `ui_kit`; las escenas de los demás módulos exponen anclas con nombre estable (`ui.tienda.vender`), nunca rutas de nodos.

## Alternativas descartadas

| Alternativa | Por qué se descarta |
|---|---|
| **Tutorial dentro de `story`** | Mezcla el guion con la enseñanza de mecánicas y engorda el módulo con más reglas; los pasos de la mejora o del tablón no son escenas de historia |
| **`tutorial` depende de cada módulo que enseña** (`shop`, `extraction`, `crafting`...) | Cada tutorial nuevo añade una dependencia; el módulo acabaría conociendo casi todo el juego |
| **Que `story` consulte a `tutorial` directamente** | Crea un ciclo `story` ↔ `tutorial`, que el verificador rechaza (A7) |
| **Escuchar eventos por nombre en el bus, sin importar la `api`** | Es una referencia dinámica que el verificador no ve: un grafo oculto, lo que [ADR-0004](0004-comunicacion-entre-modulos.md) pide evitar |
| **Módulo propio de logros** (lo previsto antes) | Duplica la medición del avance que ya hace `progression` y obliga a escuchar los mismos eventos dos veces |

## Consecuencias

- `game/architecture.json` declara `tutorial` con `depends_on: ["day", "story"]`; `progression` no cambia de dependencias. Si un logro de F4-235 necesita eventos de otro módulo, esa tarea añade la dependencia en `architecture.json`, siempre que no forme ciclo.
- Aparece un patrón nuevo, el **puente de composición**, que amplía la raíz de composición de [ADR-0003](0003-arquitectura-modular.md): los puertos entre módulos se implementan en `app/` y no en la `infrastructure` del módulo.
- Riesgo: los puentes son un grafo que el verificador todavía no comprueba (hoy `app` puede usar cualquier carpeta). Se registra como deuda en el documento 14.
- Tutorial y onboarding: lo que se aprende, cómo se enseña, qué lo exige y qué pasa si falla salen del inventario del documento 27; este ADR solo fija dónde vive. El módulo lo crean el generador (F1-28) y la primera tarea que lo implementa (F3-16, F5-01).

## Verificación

- `python3 tools/arch/check_architecture.py game` sin errores (A7 y A8 con `tutorial`).
- Pruebas del dominio de `tutorial` (F1-33): todo paso tiene remedio, se completa una sola vez y ninguna compuerta queda sin forma de cumplirse (sin softlock).
- La cola de F3-48 prueba que la escena siguiente espera a la compuerta y nunca se descarta.
