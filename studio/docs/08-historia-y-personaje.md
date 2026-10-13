# 08 · Historia y personaje

## Estructura narrativa

✅ El juego tiene **historia, actos y trama**, y luego queda como **sandbox**. No hay un final definitivo: la estructura social de Valdoria se mantiene. El protagonista logra escalar hasta lo más alto, pero el país sigue igual, porque él no gobierna.

**Tema:** *"No cambias el país, pero cambias tu lugar en él."*

## Gancho ✅

El protagonista **hereda la licencia, el puesto en el mercado y la deuda** de un tío que desapareció.

- La deuda da un objetivo claro desde el primer día y una razón mecánica para el tutorial.
- La desaparición del tío es el misterio de fondo, ligado a la Aetherita y La Fosa.

## Actos ✅

| Acto | Qué pasa | Se cierra cuando… |
|---|---|---|
| **I · El recién llegado** | Tutorial en la Cuenca del Hollín: aprende a minar y vender, conoce a los primeros personajes | Reabre el puesto, atiende la primera cuota de la deuda (pagada o prorrogada) y tiene el primer contacto con los empleados |
| **II · Aprender las reglas** | Descubre que la política manda: facciones, protección, primera huelga grande | Elige con quién se alía |
| **III · El ascenso** | Llega a la capital (Puerto Meridiano), entra a la bolsa, aparecen dilemas morales | Es aceptado en el círculo de poder |
| **IV · La cima** | Descubre qué le pasó a su tío y qué hay detrás de la Aetherita. Escala hasta lo más alto | Decide qué hacer con su poder y cierra el acta de calibración |

Después del Acto IV: **sandbox** con la capa de imperio (ver [04](04-progresion-y-meta.md)).

## Reglas de diseño narrativo 🟡

1. **Los actos se activan por umbrales** (estatus, logros, relación con facciones, deuda pagada), no por fechas. Así la historia convive con el mundo procedural y con el juego libre. Reglas concretas en [24](24-umbrales-de-acto.md).
2. **Los hitos son fijos; las circunstancias varían.** Cada partida cuenta la misma historia con otro mundo: otra facción hostil, otros eventos, otros precios.
3. **Permadeath y narrativa:** una partida es una historia completa. Si en hardcore mueres, la nueva partida arranca desde el Acto I. Se estudiará una forma de acelerar o resumir los actos ya vistos.
4. **MVP:** solo Cuenca del Hollín y Acto I, que ya prueba el loop completo y la voz del juego.

## Personaje jugable

✅ El jugador **personaliza** al protagonista:

| Elemento | Regla |
|---|---|
| Nombre del personaje | **Una sola palabra**; aparece en los diálogos |
| Nombre de la tienda | Permite **espacios** |
| Género | Hombre o mujer |
| Apariencia en v1 | **1 personaje hombre y 1 mujer** (sin editor de rostro) |

### Notas de producción 🟡

- Los diálogos usan una variable para el nombre (`{nombre}`). Hay que cuidar que no suene raro con nombres largos o con signos.
- El español tiene género gramatical. Para evitar duplicar todos los textos, conviene escribir diálogos **neutros** cuando se pueda y usar variantes solo donde sea necesario.
- Conviene validar el nombre (longitud, caracteres, filtro de palabras ofensivas) antes de aceptarlo, sobre todo si se piensa publicar en tiendas.
- El nombre de la tienda también aparece en periódicos, contratos y carteles, así que debe tener largo máximo.

## El tío y la deuda ✅

- **Tío: Anselmo Vidal.** Antes de desaparecer dejó una libreta y **cintas de grabación** (carretes). Se encuentran a lo largo del juego y revelan la verdad del Acto IV (equivalente a los holotapes de Fallout).
- **Acreedor: Doña Remedios "Reme" Salgado**, prestamista local amable. En el Acto I parece una vecina que da tiempo; en el Acto II se descubre que responde a una facción mayor.
- **La facción detrás de Reme cambia según la partida**: Consorcio Arvel, Los Faroleros o el Ministerio. Esto cumple "mismos hitos, otras circunstancias".
- ✅ El Acto II tiene 3 variantes: una columna común de seis escenas con piezas propias por variante, descritas en [22](22-acto-ii-variantes.md). No afecta al MVP (solo Acto I).
- ✅ **Anselmo está vivo, pero se cree que murió enfermo.** Es cómplice de la Comisión del Éter y el protagonista lo descubre al final del Acto IV, lo que deja abierta una continuación. Detalle y pistas en [19](19-elenco-a-fondo.md).
- ✅ **Reme traiciona en el Acto II por obligación, no por decisión propia**, y al final del Acto IV se une al protagonista para resolver el caso del tío.
- ✅ **El Ministro Montenegro es el enemigo claro**: duro e inflexible, convencido de que sostiene la nación, con una razón que no es tan razonable.

## Decisiones que cambian la historia ✅

La historia **cambia según las decisiones del jugador** (alianzas, qué hace con la verdad, etc.), aunque la estructura social de Valdoria se mantenga. ✅ Para controlar el alcance: **3 bifurcaciones grandes** (la alianza del Acto II, cómo entras al círculo en el III y el destino de la Aetherita en el IV), 6 medianas y 18 consecuencias pequeñas (diálogos, precios, relaciones). El acreedor del Acto II no es una bifurcación: la facción detrás de Reme **se sortea** al empezar la partida. El árbol completo está en [23](23-arbol-de-decisiones.md).

## Elenco ✅

| Personaje | Rol | Aporta |
|---|---|---|
| **Doña Reme Salgado** | Prestamista | Deuda; calidez con filo |
| **Teo Cárdenas, "el Viejo Teo"** | Minero veterano, amigo del tío | Mentor del tutorial de minería |
| **Inspector Quiroga** | Funcionario corrupto | Licencias y sobornos |
| **Lucía Montalvo** | Periodista del Teletipo Meridiano | Fuente de rumores; moralmente ambigua |
| **Esteban Arvel** | Heredero del Consorcio Arvel | Rival comerciante: tiene todo lo que el protagonista debe ganar |
| **Casilda Ibarra, "la Faro"** | Jefa de Los Faroleros | Extorsión y mercado negro |
| **Ministro Aurelio Montenegro** | Rostro del Estado | Antagonista principal |

**MVP:** Reme, Teo, Quiroga y Lucía. Los demás entran en actos posteriores.

## La verdad detrás de la Aetherita ✅

**La Aetherita enferma a quienes la extraen** ("el mal del éter"). La Comisión del Éter, dentro del Ministerio, lo oculta porque la economía y el ejército dependen de ella. Anselmo lo descubrió, y por eso desapareció. Lo que pasó antes del juego (hallazgo, Comisión, expedición y muerte pública de Anselmo) está en [21](21-pasado-de-valdoria.md).

En el Acto IV, ya en la cima, el jugador elige qué hacer con esa información:

| Opción | Consecuencia |
|---|---|
| **Revelarla** | La Aetherita cae en el mercado, rebota y queda algo por debajo del precio de antes; hay caos social ✅ |
| **Callarla** | Sigue ganando, con las consecuencias que eso implica |
| **Venderla** | La usa como moneda de poder con alguna facción |

Cualquier opción cambia la partida, pero **el sistema se reabsorbe y todo sigue igual**. El cierre de cada salida (cabecera, tarjetas y acta) está en [25](25-finales-y-epilogos.md) ✅; Anselmo sigue vivo y secreto en las tres. La caída y el rebote de la Aetherita son además una consecuencia de mercado: historia y economía se tocan.

## Lugares ✅

- Pueblo inicial (Cuenca del Hollín): **Villa Brasa**.
- Capital: **Puerto Meridiano**.

## Pendiente

- ❓ ¿Cuántas escenas/diálogos tiene el Acto I y con qué formato (viñetas, texto, retratos)?
- ❓ Idiomas: español primero; inglés después.
- ✅ Estructura de las variantes del Acto II decidida por el autor (sorteo oculto, alianza entre tres facciones, huelga que depende del jugador). El detalle escena por escena queda como propuesta en [22](22-acto-ii-variantes.md).
