# 09 · Minijuegos

## Reglas comunes

- ✅ Minijuegos simples, variados (estilo Dave the Diver), alineados con el juego. Inspiración: pesca de Stardew Valley y minijuegos de Among Us.
- 🟡 **Cortos:** 8–15 segundos. Con 3 a 5 menas por expedición, los minijuegos de un día suman unos minutos y respetan las sesiones de mobile.
- 🟡 **Controles táctiles simples:** mantener pulsado, soltar, arrastrar, tocar en el momento justo.
- ✅ **Dos parámetros en tensión** (fuerza ↔ precisión, etc.).
- ✅ Mejor herramienta → el minijuego es más fácil o la zona óptima más amplia.
- 🟡 La zona óptima depende del nivel de la herramienta, la **Pericia** del jugador y la dureza del mineral.

### Resultado 🟡

| Resultado | Rendimiento (orientativo) | Daño a la mena | Desgaste de herramienta |
|---|---|---|---|
| Perfecto | Alto, con bonus | Ninguno | Mínimo |
| Bueno | Normal | Bajo | Normal |
| Regular | Reducido | Medio | Alto |
| Fallo | Muy bajo | La mena se daña o se pierde | Muy alto |

Los números son ilustrativos y se calibran en el prototipo.

### Contra la repetición 🟡

1. Cada mineral usa un minijuego distinto según su dureza y herramienta.
2. **Modificadores de mena** que cambian las reglas: *costra* (requiere un golpe previo), *inestable* (el marcador se mueve de forma errática), *veta rica* (zona extra de bonus).
3. Automatización cuando el jugador domina (ver abajo).
4. Los empleados hacen el trabajo repetitivo sin minijuego (ver [04](04-progresion-y-meta.md)).

## Automatización de minijuegos ✅ (a probar en prototipo)

- Solo en **etapas avanzadas**: con una herramienta de alto nivel y stats altos.
- Al automatizarse, el minijuego **dura solo los segundos de extracción**; no hay que jugarlo.
- 🟡 Propuesta de condiciones: herramienta de nivel ≥ 4, Pericia por encima de cierto umbral y una cantidad de resultados perfectos en ese minijuego (dominio por tipo).
- 🟡 El resultado automático sería "bueno" o una probabilidad calculada con los stats; nunca "perfecto" garantizado, para mantener un incentivo a jugarlo.
- ❓ Se calibra jugando: si automatizar rompe el ritmo o la economía, se ajusta o se quita.

## Minijuegos de extracción

| # | Minijuego | Herramienta | Parámetros | Cómo se juega |
|---|---|---|---|---|
| 1 | **Picado** | Pico | Fuerza ↔ Precisión | Mantienes pulsado para cargar fuerza mientras un marcador oscila sobre la mena. Sueltas cuando ambos están en zona. Las menas duras necesitan 2–3 golpes |
| 2 | **Perforación** | Taladro | Velocidad ↔ Calor | Mantener pulsado avanza más rápido pero sube el calor; soltar enfría. Llegar al fondo sin sobrecalentar |
| 3 | **Cincelado** | Cincel | Precisión pura | Trazar con el dedo una línea sobre la gema sin salirse del margen. Un error agrieta la pieza y pierdes fragmentos |
| 4 | **Cribado** | Criba | Inclinación ↔ Caudal | Dos deslizadores que mantienen un indicador de flotación en zona mientras la carga cambia |
| 5 | **Detonación** | Explosivo | Potencia ↔ Ubicación | Ubicar la carga en la fisura y elegir potencia. Mucho rompe la mena; poco la deja atascada. Alto rendimiento, alto riesgo (puede provocar derrumbes) |

### Asignación a minerales 🟡

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

Minijuego propio para el final del juego: mantener una energía inestable entre **presión** y **resonancia**. Cada extracción acumula **exposición**, que enferma al jugador ("mal del éter") y baja temporalmente sus stats. Introduce el secreto de la Aetherita antes de revelarlo y es una decisión real: ¿vale la pena extraer más? (Ver [08](08-historia-y-personaje.md).)

## Escáner ✅

Para el MVP es **instantáneo**: tocar la mena y ver los rangos. El **Ojo** y la herramienta determinan qué tan estrechos son. Un minijuego de sintonización queda como posible mejora futura.

## Tareas de peligro (estilo Among Us) 🟡

Se activan cuando aparece un peligro ambiental. Muy cortas (5–8 s). El **Temple** da margen de tiempo y de error.

| Tarea | Peligro | Mecánica |
|---|---|---|
| **Sellar fuga** | Gas | Tocar válvulas en el orden que se mostró (memoria) |
| **Apuntalar** | Derrumbe | Arrastrar vigas a su sitio para formar un soporte |
| **Reparar** | Equipo roto | Conectar cables de colores |

## Encuentros

- Los normales son por **eventos con decisión**, sin minijuego (ver [02](02-extraccion.md)).
- 🟡 Los jefes de zona usan un **duelo de timing**: tocar en el momento justo para bloquear o contraatacar, en pocas rondas.

## Minijuegos de tienda 🟡

| Minijuego | Parámetros | Mecánica |
|---|---|---|
| **Regateo** | Tu oferta ↔ Paciencia del cliente | No es de reflejos, es de leer. Subes o bajas el precio con un deslizador; el cliente reacciona con gestos pixel-art y tiene un precio máximo oculto. Cada contraoferta gasta paciencia. **Labia** da más pistas |
| **Refinado** | Temperatura ↔ Tiempo | Mantener el metal en la banda de temperatura (se ve por su color incandescente) el tiempo justo. Demasiado quema el lote |
| **Tasar** | Ojo | Detectar la pieza falsa o defectuosa entre varias |
| **Reponer** | — | Arrastrar mercancía a los estantes y fijar precios; más gestión que minijuego |

Los empleados pueden automatizar estas tareas (ver [04](04-progresion-y-meta.md)).

## MVP de minijuegos ✅

Tres minijuegos para probar el loop completo:

1. **Picado**
2. **Perforación**
3. **Regateo**

Todo lo demás se agrega por fases.

## Pendiente

- ❓ Calibrar zonas óptimas, velocidades y bonus de cada resultado.
- ❓ Reglas exactas de dominio para la automatización.
- ❓ Diseño de cada modificador de mena.
- ❓ Feedback sensorial: vibración, sonido y efectos pixel-art por resultado (referencia sonora: Balatro).
- ❓ Accesibilidad: no depender solo del color ni del tiempo; opciones de dificultad por minijuego.
