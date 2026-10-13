# 17 · Mapa de historia

Qué pasa, qué se desbloquea y qué hace falta en cada acto. Se ve como cuadro en el hub (Panel → Mapa de historia); los datos viven en `studio/data/story.json`. La historia está en [08](08-historia-y-personaje.md); aquí se organiza por acto.

## Cómo leerlo ✅

- Cada acto es una **columna** y cada tema (narrativa, mecánicas, mercado, zonas, minerales, personajes, estatus, arte) es una **fila**.
- Los actos se activan por **umbrales** (estatus, logros, deuda pagada, relación con facciones) y no por fechas ([08](08-historia-y-personaje.md)). Las reglas de cada puerta están en [24](24-umbrales-de-acto.md).
- Después del Acto IV el juego sigue como **sandbox** con la capa de imperio ([04](04-progresion-y-meta.md)).

## Cuadro resumido

| | **I · El recién llegado** | **II · Aprender las reglas** | **III · El ascenso** | **IV · La cima** |
|---|---|---|---|---|
| Lugar | Villa Brasa (Hollín) | Hollín, Sierra Alta, Salares | Puerto Meridiano, Cavernas | La Fosa |
| Se cierra cuando… | Reabres el puesto, atiendes tu primera cuota (pagada o prorrogada) y tienes tu primer contacto con empleados | Eliges con qué facción te alías | Te aceptan en el círculo de poder | Decides qué hacer con la verdad y el poder, y cierras el acta de calibración |
| Zonas | Galerías del Hollín | Cañón Ferroso, Sierra Alta, Salares | Cavernas de Cristal | La Fosa del Éter |
| Minerales | Carbón, hierro | Cobre, salitre, plata | Oro, cuarzo, esmeralda | Diamante, Aetherita |
| Personajes | Reme, Teo, Quiroga, Lucía, Anselmo (como rastro: libreta, lámpara y firma) | Esteban Arvel, Casilda | Ministro Montenegro | — (Anselmo se revela solo al protagonista, al final: cintas completas y acta de calibración) |
| Estatus | Buscador → Minero con licencia | → Comerciante | → Empresario | → Magnate |

El detalle completo (mecánicas, mercado y eventos, arte) está en el cuadro del hub.

## Decisiones ✅

1. **Zonas:** se reparten como en el cuadro (1 en el Acto I, 3 en el II, 1 en el III y 1 en el IV).
2. **Empleados:** el Acto I **termina con el primer contacto** (se habla de ellos, aparece un candidato en el periódico, pero todavía no se puede contratar). La contratación queda **implementada en el Acto II** como está en [04](04-progresion-y-meta.md).
3. **Mercado negro:** entra en el **Acto II**, cuando conoces a los Faroleros, con el indicador de vigilancia ([03](03-comercio.md)).
4. **Variantes del Acto II** (quién está detrás de Reme): una columna común de seis escenas con piezas propias por variante, sorteo oculto al empezar y alianza final entre el Consorcio, el Ministerio y Los Faroleros. Escena por escena en [22](22-acto-ii-variantes.md).
5. **Árbol de decisiones:** las decisiones y consecuencias de los cuatro actos están en [23](23-arbol-de-decisiones.md) y sus datos en `studio/data/decisions.json`.
6. **Finales:** cada salida del IV cierra con una cabecera, tarjetas por piezas y el acta de calibración ([25](25-finales-y-epilogos.md)) ✅.
7. **Umbrales:** cada acto tiene una puerta con un hito de historia, un piso de estatus (solo en A5 y en el círculo del III) y vías «dos de tres» entre deuda, logros y relación. Todas las reglas, los tramos de los medidores y la red anti-atasco están en [24](24-umbrales-de-acto.md).

## La puerta del Acto I ✅

El Acto I se cierra cuando **reabres el puesto, atiendes tu primera cuota (pagada o prorrogada) y tienes el primer contacto con los empleados**. No pide estatus, logros ni vías: «Minero con licencia» es el **premio** del cierre, no un requisito. Tampoco pide la cinta 1: si la dejas, queda como misión persistente hasta el IV. Detalle y las demás puertas en [24](24-umbrales-de-acto.md).

## Duración ✅

Se mide en **tiempo real de juego**, no en días del calendario del juego. Orientativo y 🟡 (se calibra con el prototipo):

| Acto | Duración orientativa |
|---|---|
| I | 1,5–3 h |
| II | 4–10 h |
| III | 4–10 h |
| IV | 3–6 h |

El modo historia **no obliga a seguir la trama con exactitud**: el jugador puede hacer contratos, expediciones y otras acciones secundarias entre un hito y el siguiente. Por eso la duración depende de cómo lo aborde: quien va directo al siguiente hito termina antes, y quien se dedica al comercio y la exploración tarda más. Los umbrales que activan cada acto deben poder cumplirse de varias maneras.

## Pendiente de definir

- ❓ **Narrativa en detalle:** hoy están definidos el gancho, los cuatro actos, el elenco y la verdad de la Aetherita. Falta bajar cada acto a escenas, diálogos, decisiones y consecuencias (guion). El roadmap ya tiene el guion día a día y el storyboard del Acto I (F0-23, F0-24) y los guiones de los actos II–IV (F4-128, F4-135, F4-142), pero con poco tiempo asignado para el nivel de detalle que se busca.
- ✅ **Cierre de la historia:** resuelto en [25](25-finales-y-epilogos.md). Cabecera, tarjetas por piezas (destino de cada personaje, facción, mundo y mercado) y el acta de calibración, con hilos abiertos para una segunda parte.
- ✅ Umbrales concretos que activan cada acto: resueltos en [24](24-umbrales-de-acto.md). Decididos por el autor (2026-10-12): el modelo de puertas, los tramos, los ajustes de efectos y que la relación nace cumplida. Las cifras de estatus ⏳ F4-109, deuda ⏳ F0-52, logros ⏳ F4-116 y el evaluador ⏳ F4-127 se calibran después.
- ✅ Cuántas bifurcaciones y consecuencias hay por acto: 3 grandes, 6 medianas y 18 pequeñas (3 en el I, 5 en el II, 5 en el III y 5 en el IV). Árbol en [23](23-arbol-de-decisiones.md).
