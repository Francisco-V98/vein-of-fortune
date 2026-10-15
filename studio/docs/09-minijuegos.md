# 09 · Minijuegos

## Reglas comunes ✅

**Estado:** confirmado que son simples, variados, de dos parámetros en tensión (con dos excepciones), con controles táctiles y de mando ([10](10-tecnico-y-herramientas.md)) y que la mejor herramienta los facilita; la duración ⏳ F0-52 y la zona óptima ⏳ F2-16.

- ✅ Minijuegos simples, variados (estilo Dave the Diver), alineados con el juego. Inspiración: pesca de Stardew Valley y minijuegos de Among Us.
- **Cortos:** 8–15 segundos (se cuadra con los minutos por día, ⏳ F0-52; [01](01-core-loop.md), [17](17-mapa-de-historia.md)). Con unas pocas menas por expedición (cuántas ⏳ F0-52), los minijuegos de un bloque suman unos minutos y respetan las sesiones de mobile.
- ✅ **Controles táctiles simples:** mantener pulsado, soltar, arrastrar, tocar en el momento justo; con mando hay una variante de cada uno (⏳ F1-07).
- ✅ **Dos parámetros en tensión** (fuerza ↔ precisión, etc.). Dos excepciones, porque no hay nada que equilibrar: el **Cincelado** es de precisión pura (si pasa a dos parámetros ⏳ F4-44) y **Tasar** es de observación: se juega con el Ojo, no con parámetros.
- ✅ Mejor herramienta → el minijuego es más fácil o la zona óptima más amplia.
- La zona óptima depende del nivel de la herramienta, la **Pericia** del jugador y la dureza del mineral. ⏳ F2-16 Cómo se calcula.

### Resultado ✅

Cada minijuego tiene **4 resultados posibles** (decisión del autor, 2026-10-15), los mismos de [02](02-extraccion.md):

| Resultado | Rendimiento (orientativo) | Daño a la mena | Desgaste de herramienta |
|---|---|---|---|
| Perfecto | Alto, con bonus | Ninguno | Mínimo |
| Bueno | Normal | Bajo | Normal |
| Regular | Reducido | Medio | Alto |
| Fallo | Muy bajo | La mena se daña o se pierde | Muy alto |

Los números son ilustrativos y se calibran en el prototipo ⏳ F2-13.

### Contra la repetición ✅

1. Cada mineral usa un minijuego distinto según su dureza y herramienta.
2. **Modificadores de mena** que cambian las reglas: *costra* (requiere un golpe previo), *inestable* (el marcador se mueve de forma errática), *veta rica* (zona extra de bonus). El diseño de cada uno ⏳ F4-57, ⏳ F4-58 y ⏳ F4-59.
3. Automatización cuando el jugador domina (ver abajo).
4. Los empleados hacen el trabajo repetitivo sin minijuego (ver [04](04-progresion-y-meta.md)).

## Automatización de minijuegos ✅ (a probar en prototipo)

- ✅ Solo en **etapas avanzadas**: con una herramienta de alto nivel y stats altos.
- ✅ Al automatizarse, el minijuego **dura solo los segundos de extracción**; no hay que jugarlo.
- ⏳ F4-173 Las condiciones exactas (propuesta: herramienta de nivel ≥ 4, Pericia por encima de cierto umbral y una cantidad de resultados perfectos en ese minijuego) y las reglas de dominio por tipo.
- ⏳ F4-173 El resultado automático (propuesta: «bueno» o una probabilidad calculada con los stats, nunca «perfecto» garantizado, para mantener un incentivo a jugarlo).
- ⏳ F4-173 Se calibra jugando: si automatizar rompe el ritmo o la economía, se ajusta o se quita.

## Minijuegos de extracción ✅

**Estado:** confirmados los nombres, la herramienta y el acto de entrada de cada minijuego (registro del mundo `world.json` y glosario, [18](18-biblia-narrativa.md), 6.10); la columna «Cómo se juega» se fija al construir cada uno (abajo).

| # | Minijuego | Herramienta | Parámetros | Cómo se juega |
|---|---|---|---|---|
| 1 | **Picado** | Pico | Fuerza ↔ Precisión | Mantienes pulsado para cargar fuerza mientras un marcador oscila sobre la mena. Sueltas cuando ambos están en zona. Las menas duras necesitan 2–3 golpes |
| 2 | **Perforación** | Taladro | Velocidad ↔ Calor | Mantener pulsado avanza más rápido pero sube el calor; soltar enfría. Llegar al fondo sin sobrecalentar |
| 3 | **Cincelado** | Cincel | Precisión pura | Trazar con el dedo una línea sobre la gema sin salirse del margen. Un error agrieta la pieza y pierdes fragmentos |
| 4 | **Cribado** | Criba | Inclinación ↔ Caudal | Dos deslizadores que mantienen un indicador de flotación en zona mientras la carga cambia |
| 5 | **Detonación** | Explosivo | Potencia ↔ Ubicación | Ubicar la carga en la fisura y elegir potencia. Mucho rompe la mena; poco la deja atascada. Alto rendimiento, alto riesgo (puede provocar derrumbes). El explosivo es consumible ([02](02-extraccion.md)) |

⏳ F2-14 y ⏳ F2-15 La implementación de Picado y Perforación; ⏳ F4-44 la del Cincelado, ⏳ F4-46 la del Cribado y ⏳ F4-48 la de la Detonación.

### Asignación a minerales ✅

Coincide con el registro del mundo y con los minijuegos de cada boca de mina ([26](26-zonas-y-edificios.md)). La **Detonación** también se juega en las **Galerías del Hollín** (decisión del autor, 2026-10-15), con el carbón.

| Mineral | Minijuego principal |
|---|---|
| Carbón | Picado / Detonación |
| Hierro | Picado / Perforación |
| Cobre | Perforación |
| Salitre | Cribado |
| Plata | Perforación / Cribado |
| Oro | Cribado (aluvial) / Perforación (veta) |
| Cuarzo | Cincelado |
| Esmeralda | Cincelado |
| Diamante | Cincelado de alto nivel |
| Aetherita | **Contención** (especial) |

### Contención (Aetherita) ✅

Minijuego propio para el final del juego: mantener una energía inestable entre **presión** y **resonancia**. Cada extracción acumula **exposición**, que enferma al jugador («mal del éter») y baja temporalmente sus stats. **El mal del éter no mata** ([04](04-progresion-y-meta.md)). Introduce el secreto de la Aetherita antes de revelarlo y es una decisión real: ¿vale la pena extraer más? (Ver [08](08-historia-y-personaje.md).)

## Escáner ✅

Para el MVP es **instantáneo**: tocar la mena y ver los rangos. El **Ojo** y la herramienta determinan qué tan estrechos son. El detector básico es una herencia de Anselmo desde el Acto I; el cuarzo lo mejora más adelante. Un minijuego de sintonización queda como posible mejora futura.

## Tareas de peligro (estilo Among Us) ✅

**Estado:** los nombres de las tareas están confirmados en el glosario; la mecánica de cada una ⏳ F3-10 y ⏳ F4-53.

Se activan cuando aparece un peligro ambiental. Muy cortas (5–8 s). El **Temple** da margen de tiempo y de error.

| Tarea | Peligro | Mecánica |
|---|---|---|
| **Sellar fuga** | Gas | Tocar válvulas en el orden que se mostró (memoria) |
| **Apuntalar** | Derrumbe | Arrastrar vigas a su sitio para formar un soporte |
| **Reparar** | Equipo roto | Conectar cables de colores |

Esta tarea **Reparar** es una emergencia en plena mina. No es lo mismo que **reparar el desgaste** de una herramienta, que se paga con dinero y materiales y no es un minijuego ([02](02-extraccion.md)).

## Encuentros ✅

- ✅ Los normales son por **eventos con decisión**, sin minijuego (ver [02](02-extraccion.md)).
- Los jefes de zona son **opcionales**, no una puerta ✅. Su duelo (propuesta: un **duelo de timing**, tocar en el momento justo para bloquear o contraatacar, en pocas rondas) ⏳ F4-54.

## Minijuegos de tienda ✅

**Estado:** confirmado que Regateo es del MVP, que Tasar detecta gemas falsas, que Reponer es parte de la tienda del puesto ([26](26-zonas-y-edificios.md)) y que el Refinado es de temperatura y tiempo (⏳ F4-56); la mecánica fina de cada uno ⏳ F2-19, ⏳ F4-55 y ⏳ F4-56.

| Minijuego | Parámetros | Mecánica |
|---|---|---|
| **Regateo** | Tu oferta ↔ Paciencia del cliente | No es de reflejos, es de leer. Subes o bajas el precio con un deslizador; el cliente reacciona con gestos pixel-art y tiene un precio máximo oculto. Cada contraoferta gasta paciencia. **Labia** da más pistas |
| **Refinado** | Temperatura ↔ Tiempo | Mantener el metal en la banda de temperatura (se ve por su color incandescente) el tiempo justo. Demasiado quema el lote. El taller abre en el Acto II |
| **Tasar** ✅ | Ojo (observación) | Detectar la gema falsa entre varias ⏳ F4-55 |
| **Reponer** | — | Arrastrar mercancía a los estantes y fijar precios; más gestión que minijuego |

Los empleados pueden automatizar estas tareas (ver [04](04-progresion-y-meta.md)). Los de la tienda se juegan en el modo tienda, que gasta un bloque y no se abre de noche ([01](01-core-loop.md)). Tasar también se juega en los Tasadores de las Cavernas ([26](26-zonas-y-edificios.md)).

## MVP de minijuegos ✅

Tres minijuegos para probar el loop completo:

1. **Picado**
2. **Perforación**
3. **Regateo**

Todo lo demás se agrega por fases.

## Pendiente

- ⏳ F2-14 · F2-15 · F2-16 Calibrar zonas óptimas, velocidades y bonus de cada resultado.
- ⏳ F4-173 Reglas exactas de dominio para la automatización.
- ⏳ F4-57 · F4-58 · F4-59 Diseño de cada modificador de mena.
- Feedback sensorial: vibración, sonido y efectos pixel-art por resultado (referencia sonora: Balatro). Los efectos pixel-art siguen la dirección de arte ([12](12-direccion-de-arte.md)); ⏳ F3-21 y ⏳ F4-184 los sonidos, ⏳ F5-20 el volumen y la vibración.
- Accesibilidad: no depender solo del color ✅ ([12](12-direccion-de-arte.md)). ⏳ F5-17 y ⏳ F5-52 No depender solo del tiempo y las opciones de dificultad por minijuego.
