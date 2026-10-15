# 17 · Mapa de historia

Qué pasa, qué se desbloquea y qué hace falta en cada acto. Se ve como cuadro en el hub (Panel → Mapa de historia); los datos viven en `studio/data/story.json`. La historia está en [08](08-historia-y-personaje.md); aquí se organiza por acto.

## Cómo leerlo ✅

- Cada acto es una **columna** y cada tema (narrativa, mecánicas, mercado, zonas, minerales, personajes, estatus, arte) es una **fila**.
- Los actos se activan por **umbrales** (estatus, logros, deuda pagada, relación con facciones) y no por fechas ([08](08-historia-y-personaje.md)). Las reglas de cada puerta (el paso de un acto al siguiente) están en [24](24-umbrales-de-acto.md).
- Después del Acto IV el juego sigue como **sandbox** con la capa de imperio ([04](04-progresion-y-meta.md)).
- Las pistas, promesas, secretos y conflictos de la historia (dónde se siembra cada uno, dónde se resuelve y qué cambia) están en `studio/data/hilos.json` y se ven en el hub (`#/hilos`).

## Cuadro resumido

| | **I · El recién llegado** | **II · Aprender las reglas** | **III · El ascenso** | **IV · La cima** |
|---|---|---|---|---|
| Lugar | Villa Brasa (Hollín) | Hollín, Sierra Alta, Salares | Puerto Meridiano, Cavernas | La Fosa |
| Se cierra cuando… | Reabres el puesto, atiendes tu primera cuota (vence el día 7; pagada o prorrogada) y tienes tu primer contacto con empleados | Eliges con qué facción te alías | Te aceptan en el círculo de poder | Decides qué hacer con la verdad y el poder, y cierras el acta de calibración |
| Zonas | Galerías del Hollín | Cañón Ferroso, Sierra Alta, Salares | Cavernas de Cristal | La Fosa del Éter |
| Minerales | Carbón, hierro | Cobre, salitre, plata, oro, cuarzo | Esmeralda, diamante. La Aetherita solo tiene precio visible y se compra en el mercado negro (Casilda) | Aetherita (la extracción empieza aquí) |
| Personajes | Reme, Teo, Quiroga, Lucía, Anselmo (como rastro: libreta, lámpara y firma) | Esteban Arvel, Casilda | Ministro Montenegro | — (Anselmo se revela solo al protagonista, al final: cintas completas y acta de calibración) |
| Estatus | Heredero → Minero con licencia | → Comerciante | → Empresario | → Magnate al cerrar el acta |
| Cintas | Cinta 1 | Cinta 2 | Cintas 3 a 5 | Cintas 6 a 8; todas se oyen aquí con el reproductor |
| Puerta | Hito del I, sin estatus ni vías | A5: Comerciante y dos vías de tres | Círculo: Empresario, dos vías de tres y una entrada (aval, sello o presión); luego, Montenegro y las cintas 1 a 5 | El acta de calibración; Magnate es el premio, no una puerta |

El detalle completo (mecánicas, mercado y eventos, arte) está en el cuadro del hub.

**Asentamientos por acto.** ✅ Cada región tiene un asentamiento y los actos de las zonas no cambian (decisión del autor, 2026-10-13). 🟡 Propuesta, sin revisar, de qué asentamiento abre en qué acto: Villa Brasa en el I; Altafría y Salinas Blancas en el II; Puerto Meridiano y el campamento de las Cavernas en el III; el campamento de la Comisión en la Fosa, en el IV. Catálogo de edificaciones en [26](26-zonas-y-edificios.md).

## Decisiones ✅

1. **Zonas:** se reparten como en el cuadro (1 en el Acto I, 3 en el II, 1 en el III y 1 en el IV).
2. **Empleados:** el Acto I **termina con el primer contacto** (el día 7, a primera hora; se habla de ellos, aparece un candidato en el periódico, pero todavía no se puede contratar). La contratación queda **implementada en el Acto II** como está en [04](04-progresion-y-meta.md): el botón «Contratar» se abre al cerrar el Acto I y también exige una mejora de la tienda, que se compra en la propia tienda desde el Acto II (en el Acto I está bloqueado por ese motivo). Se empieza con Minero y Dependiente, y el Analista llega en el Acto III (decisión del autor, 2026-10-15).
3. **Mercado negro:** entra en el **Acto II**, cuando conoces a los Faroleros, con el indicador de vigilancia ([03](03-comercio.md)). Se opera de noche, en el Bar del Farol de Salinas Blancas y con la visita nocturna de Casilda; la tienda no se abre de noche.
4. **Variantes del Acto II** (la facción de Reme): una columna común de seis escenas con escenas propias por variante, sorteo oculto al empezar y alianza final entre el Consorcio, el Ministerio y Los Faroleros. Escena por escena en [22](22-acto-ii-variantes.md).
5. **Árbol de decisiones:** las decisiones y consecuencias de los cuatro actos están en [23](23-arbol-de-decisiones.md) y sus datos en `studio/data/decisions.json`.
6. **Finales:** cada salida del IV cierra con una cabecera, tarjetas por piezas y el acta de calibración ([25](25-finales-y-epilogos.md)) ✅.
7. **Umbrales:** cada acto tiene una puerta con un hito de historia, un piso de estatus (solo en A5 y en el círculo del III) y vías «dos de tres» entre deuda, logros y relación. Las facciones no tienen medidor propio: la relación se mide con los cuatro medidores (Unión, Esteban, Lucía y Teo) y las facciones, por la alianza que elijas ([23](23-arbol-de-decisiones.md)). Todas las reglas, los tramos de los medidores y la red anti-atasco están en [24](24-umbrales-de-acto.md).
8. **Aetherita en el Acto III** ✅ (decisión del autor, 2026-10-12): el precio es visible y solo se compra en el mercado negro (Casilda), como mercancía escasa. La extracción no ocurre hasta el Acto IV.
9. **Escalera de estatus** ✅ (decisión del autor, 2026-10-12): Heredero, Minero con licencia, Comerciante, Empresario y Magnate. Los requisitos y las cifras ⏳ F4-109.

## La puerta del Acto I ✅

El Acto I se cierra cuando **reabres el puesto, atiendes tu primera cuota (pagada o prorrogada) y tienes el primer contacto con los empleados**. La primera cuota vence el día 7 y las siguientes, cada 7 días; si no puedes pagar, se prorroga una semana con un pequeño recargo (en Difícil y Hardcore, la cuota atrasada se suma a la del día 14 con un recargo mayor) ⏳ F0-52. No pide estatus, logros ni vías: «Minero con licencia» es el **premio** del cierre, no un requisito. Tampoco pide la cinta 1: si la dejas, queda como misión persistente hasta el IV. Detalle y las demás puertas en [24](24-umbrales-de-acto.md).

## Duración

Se mide en **tiempo real de juego**, no en días del calendario del juego ✅. La duración orientativa de cada acto es 🟡 (se calibra con el prototipo):

| Acto | Duración orientativa |
|---|---|
| I | 1,5–3 h |
| II | 4–10 h |
| III | 4–10 h |
| IV | 3–6 h |

Esas horas dependen de cuántos minutos dura un día de juego ([01](01-core-loop.md)): siete días en 1,5–3 h son 13–26 minutos por día, y la meta de sesiones cortas de 01 apunta a menos. Con esa misma cuenta, un contrato de empleado de 90 días ([04](04-progresion-y-meta.md)) serían entre 7 y 39 horas de juego, más que el Acto II entero. ⏳ F0-52 Los minutos por día y la duración en días de los contratos de 7, 30 y 90.

El modo historia **no obliga a seguir la trama con exactitud** ✅: el jugador puede hacer contratos, expediciones y otras acciones secundarias entre un hito y el siguiente. Por eso la duración depende de cómo lo aborde: quien va directo al siguiente hito termina antes, y quien se dedica al comercio y la exploración tarda más. Los umbrales que activan cada acto deben poder cumplirse de varias maneras.

## Pendiente de definir

- **Narrativa en detalle:** hoy están definidos el gancho, los cuatro actos, el elenco, la verdad de la Aetherita, las decisiones ([23](23-arbol-de-decisiones.md)), los umbrales ([24](24-umbrales-de-acto.md)) y el cierre ([25](25-finales-y-epilogos.md)). Falta bajar los actos II a IV a escenas y diálogos (guion). El guion del Acto I está en [27](27-guion-del-acto-i.md) y su storyboard ⏳ F0-24; los guiones de los actos II a IV ⏳ F4-128, ⏳ F4-135 y ⏳ F4-142, con la plantilla común ⏳ F4-216.
- ✅ **Cierre de la historia:** resuelto en [25](25-finales-y-epilogos.md). Cabecera, tarjetas por piezas (destino de cada personaje, facción, mundo y mercado) y el acta de calibración, con hilos abiertos para una segunda parte.
- ✅ Umbrales concretos que activan cada acto: resueltos en [24](24-umbrales-de-acto.md). Decididos por el autor (2026-10-12): el modelo de puertas, los tramos, los ajustes de efectos y que la relación nace cumplida. Las cifras de estatus ⏳ F4-109, deuda ⏳ F0-52, logros ⏳ F4-116 y el evaluador ⏳ F4-127 se calibran después.
- ✅ Cuántas bifurcaciones y consecuencias hay por acto: 3 grandes, 6 medianas y 18 pequeñas (3 en el I, 5 en el II, 5 en el III y 5 en el IV). Árbol en [23](23-arbol-de-decisiones.md).
