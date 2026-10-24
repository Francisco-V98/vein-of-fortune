# 23 · Árbol de decisiones y consecuencias

> ⚠️ **Contiene spoilers de toda la historia.** Es material para quien escribe y para quien programa la narrativa; no es para el jugador.

Todas las decisiones de los cuatro actos en un solo árbol: quién las dispara, qué opciones hay y qué cambian en el mundo, el mercado y los personajes. Los datos viven en `studio/data/decisions.json` (los valida el hub) y aquí se explican. Parte de [08](08-historia-y-personaje.md), [17](17-mapa-de-historia.md), [19](19-elenco-a-fondo.md), [21](21-pasado-de-valdoria.md), [22](22-acto-ii-variantes.md) y [03](03-comercio.md).

**Cómo leer las marcas.** La palomita verde es lo que decidió el autor. Todo el árbol quedó confirmado por el autor en la pasada de cierre F0-80 (2026-10-16): las 27 decisiones llevan la palomita junto a su nombre y no queda ninguna propuesta ni pregunta abierta. El reloj de arena lleva el ID de la tarea existente de la que depende un detalle que nada anterior necesita (cifras, sistemas y guiones).

## Resumen en cinco líneas

1. El árbol tiene **27 decisiones**: 3 grandes, 6 medianas y 18 pequeñas.
2. Las grandes son la **alianza** (II), **cómo entras al círculo** (III) y el **destino de la Aetherita** (IV).
3. **14 banderas de elección y 4 medidores** (Unión, Esteban, Lucía y Teo) llevan el estado de una decisión a otra. Las facciones se miden por la alianza elegida, no por un medidor propio.
4. **Seis cuellos de botella** reúnen las ramas antes de cada gran escena, así que las historias se separan pero vuelven a juntarse.
5. Las **ocho cintas** se recogen antes (1 en el I, 2 en el II, 3 a 5 en el III y 6 a 8 en el IV) y solo se **oyen en el Acto IV**.

---

## 1 · Decisiones del autor ✅

Decisiones del 2026-10-12 (F0-45), más las que ya estaban en [22](22-acto-ii-variantes.md) y [19](19-elenco-a-fondo.md).

| Tema | Decisión |
|---|---|
| Cupos | **3 grandes, 6 medianas y 18 pequeñas** ✅ |
| Pequeñas por acto | **3 en el I, 5 en el II, 5 en el III y 5 en el IV** ✅ |
| Estado que se guarda | **Unas 14 banderas de elección y 4 medidores**: Unión, Esteban, Lucía y Teo ✅. El Consorcio, el Ministerio y Los Faroleros **no tienen medidor propio**: se miden por la alianza que elijas ✅ |
| Deuda del Acto I | La cuota vence **cada 7 días y la primera, el día 7**. Si no puedes pagar, se **prorroga una semana con un recargo del 6 % de la cuota atrasada** en Intermedio (4 % en Novato; en Difícil y Hardcore, la cuota atrasada se suma a la del día 14 con un recargo del 12 % y el 18 %). La cuota del día 7 es de **960 esquirlas** y su recargo en Intermedio, de 58 ✅ ([28](28-numeros-base-de-la-economia.md)) |
| Aetherita en el III y el IV | En el III el precio es visible y **solo se compra en el mercado negro (Casilda)**, como mercancía escasa; la extracción no ocurre hasta el IV ✅. En el IV se vende por un **canal legal con tope**: la oficina de la Comisión del Éter en Puerto Meridiano, siempre abierta y a valor justo ([26](26-zonas-y-edificios.md)) y el mercado negro solo recibe **encargos especiales** raros, con su historia, nunca como venta rutinaria ✅ ([28](28-numeros-base-de-la-economia.md)) |
| Vigilancia | Un **indicador global de 0 a 100** que sube con las operaciones negras. Sus cambios se escriben «vigilancia +N» o «vigilancia −N», sin la palabra «puntos»; el «%» solo describe el ritmo de subida, y nunca se nombra un lugar. «Bajo investigación» es la redada ([03](03-comercio.md)) ✅ |
| Las tres grandes | **Alianza** (II, escena A5), **cómo entras al círculo** (III) y **destino de la Aetherita** (IV: revelar, callar o vender) ✅ |
| Cómo entras al círculo | Tres entradas: el **aval de Esteban**, el **sello de Montenegro** (solo vale como firma, sin humanizarlo) o la **presión de tu alianza**. Todas llegan al **mismo encuentro con Montenegro** y la entrada fija **quién te debe un favor en el IV** ✅. «Puerta» queda para el paso entre actos ([24](24-umbrales-de-acto.md)) ✅ |
| Destino de Teo | Se queda si su confianza es alta o media, se va si es baja y **muere si no hubo revisión en el III**, también si le propones y aceptas su no (la opción respetuosa tiene costo). Si chocan, gana el no haberlo atendido. La revisión solo puede decir «tos de mina» ✅ |
| Tramos de los medidores | **Bajo menos de 35, medio 35 a 54, alto 55 o más**, para Unión, Esteban, Lucía y Teo ✅ ([24](24-umbrales-de-acto.md)) |
| Lucía y el reproductor | Con tramo alto, Lucía publica contigo y entrega el reproductor. Con medio no publica (lo publicas tú, con costo alto y poco alcance) y con bajo publica en La Voz sin ti. Con medio o bajo, el reproductor lo entrega Reme ✅ |
| Aval de Esteban | Basta su medidor en tramo alto. Si no, se muestra bloqueado con el motivo y quedan el sello y la presión de tu alianza ✅ |
| Cintas | Se recogen antes (**1 en el I, 2 en el II, 3 a 5 en el III y 6 a 8 en el IV**) pero solo se oyen en el Acto IV, con un reproductor ✅ |
| Facción de Reme | Es un **sorteo** al empezar la partida, **no una bifurcación jugable** ✅. Se guarda en el estado de la partida ⏳ F2-01 |
| Acto II | La **huelga depende de ti** (apoyar, abstenerte o romper), la **orden de Reme** tiene tres salidas (aceptar, negociar o rechazar), la alianza es entre Consorcio, Ministerio y Faroleros, y **Montenegro no aparece** en el II ✅ |
| Reme | Siempre termina como **tu mayor aliada** ✅ |
| Canon que no se toca | Anselmo está vivo pero se cree muerto y enfermo, y es cómplice de la Comisión del Éter. Reme traiciona en el Acto II por obligación y al final es la mayor aliada. Montenegro es el enemigo claro, duro e inflexible ✅ |

---

## 2 · Reglas del árbol ✅

**Estado:** los cupos, las banderas, los medidores y sus tramos son de la sección 1. Las definiciones de nivel, los cuellos de botella y las reglas de seguridad los confirmó el autor el 2026-10-16 (F0-80); no cambian los cupos 3/6/18, las 14 banderas ni los 4 medidores. Las cifras de precios, cuotas y gastos son las de [28](28-numeros-base-de-la-economia.md), ya decididas (base que verificó F0-53 con el simulador: con los ajustes que aprobó el autor pasan las 50 reglas de equilibrio, ver [28](28-numeros-base-de-la-economia.md), sección 13); el movimiento de los medidores usa los tamaños 5, 10 y 20 que decidió el autor el 2026-10-16, y su ajuste fino ⏳ F4-61

### 2.1 Niveles

| Nivel | Qué cambia | Cupo | Reparto |
|---|---|---|---|
| **Grande** | Cambia el tramo de historia que sigue y lo recuerda el epílogo | 3 | 1 en el II, 1 en el III y 1 en el IV |
| **Mediana** | Cambia una escena entera o el destino de un personaje durante varios actos | 6 | 2 en el II, 2 en el III y 2 en el IV |
| **Pequeña** | Cambia un diálogo, un precio o un medidor | 18 | 3 en el I, 5 en el II, 5 en el III y 5 en el IV |

### 2.2 Banderas y medidores

- **Bandera de elección.** Guarda qué opción elegiste (dos o tres valores). Una decisión puede **fijar** una bandera y otra puede **leerla**. Una decisión solo lee banderas que se fijaron antes, en su acto o en uno anterior.
- **Medidor.** Número de 0 a 100. Arranca en 50, salvo Teo (60) y Esteban (40). Cada opción lo mueve poco (≈ 5), normal (≈ 10) o mucho (≈ 20) ✅ (decisión del autor, 2026-10-16); F4-61 los implementa y solo afina el ajuste fino, sin cambiar los caminos mínimos ⏳ F4-61. Los tramos son *bajo* (0 a 34), *medio* (35 a 54) y *alto* (55 o más) ✅, y qué desbloquea cada uno está en [24](24-umbrales-de-acto.md), sección 5. Los caminos a cada tramo que debe conservar F4-61 están en la sección 6 de ese documento
- **Los cuatro medidores.** **Unión** es el de su sindicato ([22](22-acto-ii-variantes.md), sección 9). **Esteban** es personal, no el del Consorcio ✅. Las facciones aliables (Consorcio, Ministerio y Los Faroleros) **no tienen medidor propio** ✅: se miden por la alianza que elegiste. **Lucía** y **Teo** miden cuánto confían en ti. **Montenegro no tiene medidor** ✅.
- **Desenlaces calculados.** Lo que hacen Esteban, Lucía, Montenegro y Teo en el IV no guarda una bandera nueva: se calcula leyendo medidores y banderas. El epílogo ([25](25-finales-y-epilogos.md)) lee las mismas y guarda los resultados como estado legible con nombres estables ✅ (sección 8 de ese documento, ⏳ F2-01); no son banderas del árbol, así que no cambian los cupos.
- **El sorteo no es una decisión.** La variante de Reme se fija antes de A1, se guarda en el estado ⏳ F2-01 y es oculta. Las decisiones del II la leen sin guardarla como bandera.

### 2.3 Cuellos de botella

Un cuello es un punto donde varias ramas se juntan. Así el árbol no se multiplica sin control: cada acto tiene al menos uno y todos reciben al menos dos ramas.

| Cuello | Acto | Qué reúne | Recibe |
|---|---|---|---|
| `c-i-cierre` | I | Las tres consecuencias del I se pierden en el mismo cierre: reabres el puesto, atiendes la primera cuota y tienes el primer contacto con los empleados. | `n-i-herencia`, `n-i-reme-plazo`, `n-i-lucia-rumor` |
| `c-ii-apagon` | II | El apagón del Hollín es común (22, sección 4): el conflicto, el contacto y la huelga cambian cómo lo vives, no si ocurre. | `n-ii-contacto`, `n-ii-conflicto`, `n-ii-huelga` |
| `c-ii-cierre` | II | A6: Reme calla el abono y paga o respira según su facción y tu alianza. Siempre termina como tu aliada. | `n-ii-orden`, `n-ii-huelga`, `n-ii-alianza` |
| `c-iii-encuentro` | III | Las tres entradas llegan al mismo encuentro con Montenegro. Cambian lo que te debe cada uno, no la escena. | `n-iii-circulo`, `n-iii-monopolio`, `n-iii-contrato-oficial`, `n-iii-esteban-trato` |
| `c-iv-pruebas` | IV | Todas las ramas llegan al enfrentamiento con al menos tres pruebas que no se pierden (sección 8). | `n-iv-reme-proteccion`, `n-iv-esteban`, `n-iv-quiroga-archivo` |
| `c-iv-acta` | IV | Revelar, callar o vender terminan en la misma última escena: el acta de calibración y la firma de Anselmo. | `n-iv-aetherita`, `n-iv-comprador`, `n-iv-lucia-publica`, `n-iv-teo` |

### 2.4 Reglas de seguridad

- **Ninguna puerta de acto lee `f-pago-reme` ni `f-orden-reme`** ✅ ([24](24-umbrales-de-acto.md)): Reme nunca cierra una puerta. `n-ii-alianza` lee `f-orden-reme` solo para mostrar el costo de Reme; no lo usa para decidir ✅ (decisión del autor, 2026-10-16).
- **Ninguna rama cierra la ruta de Reme.** Rechazar su orden cambia el costo, no lo que puedes hacer después. Siempre termina como tu mayor aliada.
- **Cada ruta del IV conserva al menos tres pruebas** (sección 8); la regla de Montenegro pide dos para intentar borrarte. Nada de lo que hagas con el archivo de Quiroga destruye la copia del certificado ni la carta de la cinta 6.
- **Ningún personaje aparece antes de su acto:** Esteban y Casilda en el II, Montenegro en el III. En el II, Montenegro es solo decreto y firma.
- **Anselmo solo como sombra antes del IV**, con una sombra como máximo por escena. Las cintas se recogen en una misión, nunca dentro de una de las seis escenas ancla del II, y no se pueden oír hasta el IV.
- **Los avisos son justos.** Toda decisión con una consecuencia grave se anuncia antes: la tos de Teo se ve y los demás la comentan antes de la revisión.
- **Cada magnitud tiene su palabra** ✅: el mercado se mide en **puntos** (un punto es el 1 % del precio base del mineral), el interés de la deuda en **pp** (punto porcentual de la tasa mensual) y la vigilancia como «vigilancia +N»; el «%» solo describe el ritmo de subida o una proporción. La caída y el rebote de la Aetherita respetan su tope diario de variación, del 15 % ([03](03-comercio.md), [28](28-numeros-base-de-la-economia.md))
- **El protagonista sigue siendo un optimista terco.** Ninguna opción lo hace cínico ni burlón con los trabajadores.

---

## 3 · Acto I: tres consecuencias pequeñas ✅

**Estado:** el Acto I no tiene bifurcación grande y tiene 3 pequeñas, y el autor confirmó cuáles son el 2026-10-16 (F0-80). Se activan en los días del tutorial ([27](27-guion-del-acto-i.md), sección 12) y sus textos ⏳ F3-47

**`n-i-herencia` · Cómo cuentas la herencia a tu familia** (pequeña) ✅
- **Dispara:** Tu primera noche en Villa Brasa (día 1, bloque de noche), cuando escribes a Vega Mansa.
- **Les cuentas todo: el puesto, la deuda y la mina.** → *Mundo:* Tu padre contesta con una carta corta: sabe que rompiste su juramento. *Personajes:* Protagonista: duerme en paz. El padre: dolido, pero no te da la espalda.
- **Les cuentas que heredaste un puesto, sin decir mina.** → *Mundo:* En casa se alegran sin saber de la mina. *Personajes:* Protagonista: carga con un secreto pequeño.
- **No dices nada hasta tener algo que mostrar.** → *Mundo:* Pasan semanas sin carta de casa. *Personajes:* Protagonista: el orgullo le pesa más que la culpa.
- **Fija:** `f-familia`. **Lee:** —.

**`n-i-reme-plazo` · Pagar a Reme antes o después del plazo** (pequeña) ✅
- **Dispara:** Vence la primera cuota de la deuda: el día 7 y, después, cada 7 días ✅. Puedes pagar antes desde el día 4.
- **Pagas antes del plazo.** → *Mundo:* Reme te invita al café y anota que eres de fiar. *Mercado:* Interés de la deuda de la herencia: −1 pp (del 4 % al 3 % mensual), permanente; puedes pagar antes desde el día 4. *Personajes:* Reme: cálida, con una pizca de culpa.
- **Pagas justo en el plazo.** → *Mundo:* Todo sigue su curso. *Personajes:* Reme: «Con calma, criatura».
- **Pides una prórroga de una semana.** → *Mundo:* En Novato e Intermedio toda la serie se desplaza una semana, con un recargo por cada semana de atraso (6 % de la cuota en Intermedio, 4 % en Novato), y no pagar equivale a pedirla; en Difícil y Hardcore la cuota atrasada se suma a la del día 14 con un recargo mayor que en los otros dos ✅ ([27](27-guion-del-acto-i.md), sección 11). *Mercado:* Recargo de la prórroga: {recargo}, que en Intermedio es el 6 % de la cuota atrasada (58 esquirlas sobre la cuota del día 7). Con 4 semanas de atraso acumuladas sube la tasa +1 pp hasta que pagues una cuota completa; nunca cierra una puerta. *Personajes:* Reme: te da el plazo con un consejo que suena a aviso.
- **Fija:** `f-pago-reme`. **Lee:** —.

**`n-i-lucia-rumor` · Confiar en Lucía con un rumor** (pequeña) ✅
- **Dispara:** Lucía te ofrece un rumor a cambio de otro (día 5, bloque de mañana, en tu puesto).
- **Le cuentas el rumor entero.** → *Mundo:* El Teletipo lo publica con su SIN CONFIRMAR. *Mercado:* El mineral del rumor se mueve 2 a 3 puntos ese día. *Personajes:* Lucía: confía más en ti.
- **Le cuentas la mitad.** → *Mundo:* Sale una nota vaga. *Mercado:* El mineral del rumor se mueve 1 punto. *Personajes:* Lucía: sospecha, pero te debe una.
- **No le cuentas nada.** → *Mundo:* No sale nada. *Personajes:* Lucía: toma nota y confía un poco menos.
- **Fija:** `m-lucia`. **Lee:** —.

**Cuello:** `c-i-cierre`. Las tres terminan en el mismo cierre del acto.

---

## 4 · Acto II: la política manda ✅

**Estado:** la alianza (grande), la orden de Reme y la huelga (medianas) y sus opciones son decisión del autor (2026-10-12); las cinco pequeñas y los efectos los confirmó el 2026-10-16 (F0-80). Los tamaños de efecto en los medidores (≈ 5, ≈ 10 y ≈ 20) los decidió el autor el 2026-10-16; su ajuste fino ⏳ F4-61. El orden de la lista es el de juego. Los efectos propios de cada variante están en [22](22-acto-ii-variantes.md), secciones 7 a 9. La escena O3 (Casilda te cita de noche) es un camino extra y no ramifica, y eso está decidido

**`n-ii-contacto` · Responder al primer contacto de la política** (pequeña) ✅
- **Dispara:** Acto I cerrado (escena A1 de 22). El decreto de A1 es lo que abre las zonas del II; no es una condición previa ✅ (su guion ⏳ F4-128).
- **Aceptas la cita.** → *Mundo:* Queda en cola la orden de Reme para tu próxima cuota. *Personajes:* Esteban, Quiroga o un cobrador farolero (según tu variante) te trata como cliente. Solo con el Consorcio sube el medidor de Esteban.
- **Rechazas la cita.** → *Mundo:* La facción lo toma como un desaire; la orden de Reme llega igual. *Personajes:* El contacto de tu variante te recuerda. Solo con el Consorcio baja el medidor de Esteban.
- **La pospones.** → *Mundo:* El contacto vuelve a aparecer en la siguiente zona. *Personajes:* Sin cambios.
- **Fija:** `m-esteban`. **Lee:** —.

**`n-ii-orden` · La orden de Reme** (mediana) ✅
- **Dispara:** Escena A2 de 22: llega tu próxima cuota a Reme y ella revela la facción que la manda (sorteada al empezar).
- **Aceptas lo que pide tu facción.** → *Mundo:* Cumples la petición de tu variante: vender solo al Consorcio, entregar tus cuentas o pagar la cuota extra de luz. *Mercado:* Consorcio: prima de contrato +3 a +5 puntos, pero un solo comprador (exclusividad de venta ⏳ F4-215). Ministerio: el Ministerio ve tus cuentas (entrega de cuentas ⏳ F4-215). Faroleros: cuota extra de luz de 960 esquirlas, una vez. *Personajes:* Reme: alivio y vergüenza. «Perdóname, criatura. Esto no lo elegí yo».
- **Negocias con Labia una versión más corta.** → *Mundo:* Si la prueba sale bien, cumples solo la mitad de la petición. *Mercado:* La mitad del efecto de aceptar. *Personajes:* Reme: orgullosa de ti, sin decirlo.
- **Rechazas la orden.** → *Mundo:* La cuota de la deuda se adelanta. La ruta sigue abierta. *Mercado:* Adelanto de la cuota: se cobra por adelantado la mitad de la siguiente cuota si pagaste a tiempo en el Acto I y la cuota entera si prorrogaste. Se acredita a las siguientes cuotas, sin costo extra, y cuenta para la vía de deuda. *Personajes:* Reme: calla un segundo. Su facción le cobra un costo.
- **Fija:** `f-orden-reme`. **Lee:** `f-pago-reme`.

**`n-ii-conflicto` · Resolver el primer conflicto con tu facción** (pequeña) ✅
- **Dispara:** Escena A3 de 22: primera expedición o venta en la zona de tu variante (contratos, licencias o cobros de luz).
- **Pagas el costo y sigues.** → *Mundo:* El conflicto se cierra sin ruido. *Mercado:* Pierdes 3 a 5 % del valor de tus ventas de esa semana en la zona. *Personajes:* La facción te respeta.
- **Cedes lo que piden.** → *Mundo:* Pierdes un contrato, pasas una revisión de licencia o dejas una noche de luz a la facción. *Personajes:* La Unión lo nota: baja un poco.
- **Te plantas.** → *Mundo:* El conflicto escala y la facción fija su postura ante la huelga. *Mercado:* Sin prima de la zona esa semana. *Personajes:* La Unión lo nota: sube un poco.
- **Fija:** `m-union`. **Lee:** `f-orden-reme`.

**`n-ii-huelga` · La primera huelga** (mediana) ✅
- **Dispara:** Escena A4 de 22: el aviso sale en las noticias y la huelga cierra Cañón Ferroso por completo (excepción de guion de cierre total, [07](07-sociedad-y-eventos.md)). Ocurre en las tres variantes.
- **Apoyas la huelga.** → *Mundo:* Cierras el puesto un día y entregas mineral a la caja de huelga. Luego llega el apagón, común a todos. *Mercado:* Hierro +8 a +12 % mientras dura el cierre, dentro del tope diario; el segundo mineral de tu variante, +3 a +5 puntos. *Personajes:* Teo y la Unión se acercan. Tu variante añade una consecuencia pequeña (22, sección 7).
- **Te abstienes.** → *Mundo:* Sigues con tu negocio. Llega el mismo apagón. *Mercado:* Mismo movimiento de precios para todos. *Personajes:* Teo y la Unión no cambian. No se activa ninguna consecuencia de variante.
- **Rompes la huelga.** → *Mundo:* Vendes el mineral que pide quien quiere la huelga rota. Luego llega el mismo apagón. *Mercado:* Mismo movimiento de precios; la prima de contrato de tu variante sube 3 a 5 puntos. *Personajes:* Teo y la Unión se alejan mucho. Tu variante añade una consecuencia pequeña (22, sección 7).
- **Fija:** `f-huelga`, `m-teo`, `m-union`. **Lee:** —.

**`n-ii-lucia` · Lo que vende Lucía** (pequeña) ✅
- **Dispara:** Comprar tres rumores (escena opcional O1 de 22; los rumores ⏳ F4-214).
- **La confrontas.** → *Mundo:* Lucía deja de venderte rumores flojos. *Personajes:* Lucía: admite a medias y confía más.
- **Usas su doble juego.** → *Mundo:* Le das un dato para que llegue a la otra parte (Esteban, Quiroga o los informantes de Casilda). *Mercado:* Un rumor mueve un mineral 2 a 3 puntos. *Personajes:* Lucía: si lo descubre, confía menos.
- **Te lo guardas.** → *Mundo:* Sigues leyendo sus rumores con cuidado. *Personajes:* Lucía: no se entera.
- **Fija:** `m-lucia`. **Lee:** `m-lucia`.

**`n-ii-esteban-contrato` · Esteban se queda un contrato** (pequeña) ✅
- **Dispara:** Rechazas o tardas en un contrato de hierro o cobre (escena opcional O2 de 22).
- **Compites por el siguiente contrato.** → *Mundo:* Recuperas el contrato siguiente. *Mercado:* Pierdes 3 a 5 puntos de margen en ese contrato. *Personajes:* Esteban: te respeta, aunque diga «amigo» más seco.
- **Se lo dejas.** → *Mundo:* Esteban se lleva este contrato y el siguiente. *Mercado:* Esteban compra y empuja el precio un 2 a 4 %. *Personajes:* Esteban: más seguro y con menos respeto por ti.
- **Le avisas a Quiroga de su papeleo.** → *Mundo:* Quiroga revisa los papeles de Esteban y se los devuelve con un retraso. *Mercado:* El contrato se retrasa una semana. *Personajes:* Esteban: «No es personal… es completamente personal». Baja mucho.
- **Fija:** `m-esteban`. **Lee:** `m-esteban`.

**`n-ii-certificado` · El certificado a solas** (pequeña) ✅
- **Dispara:** Primera visita a Quiroga después de la orden (escena opcional O4 de 22). Si no ocurre, A5 siembra la pista.
- **Le pides una copia.** → *Mundo:* Quiroga la da con una «gestión» y se pone nervioso. *Mercado:* Una gestión pequeña: 400 esquirlas. *Personajes:* Quiroga: anota que lo sabes.
- **Miras el sello y no dices nada.** → *Mundo:* Te quedas con la sombra: sello irregular y sin registro de cremación. *Personajes:* Quiroga: respira aliviado.
- **Le dices que sabes lo del sello.** → *Mundo:* Quiroga se vuelve dependiente de ti. *Mercado:* Vigilancia −10. *Personajes:* Quiroga: te teme y te necesita.
- **Fija:** `f-certificado`. **Lee:** —.

**`n-ii-alianza` · La alianza** (grande) ✅
- **Dispara:** Escena A5 de 22: tras la huelga y con estatus de Comerciante, llegan las tres ofertas. Cierra el Acto II.
- **Te alías con el Consorcio Arvel.** → *Mundo:* Contratos grandes y tu deuda pasa a la casa. *Mercado:* Los modificadores de tu variante se sustituyen por los de la alianza ⏳ F4-133. *Personajes:* Esteban: socio incómodo. La Unión baja. Reme paga o respira según su facción (22, sección 9).
- **Te alías con el Ministerio.** → *Mundo:* Licencia ampliada y trámite preferente. *Mercado:* Los modificadores de tu variante se sustituyen por los de la alianza ⏳ F4-133. *Personajes:* Quiroga: tu enlace. La Unión baja. Reme paga o respira según su facción.
- **Te alías con Los Faroleros.** → *Mundo:* Protección y luz; tu deuda de luz (3 600 esquirlas, sin interés, que crece un 2 % al mes si no la tocas) se suma aparte de la deuda de la herencia y no entra en la vía de deuda. *Mercado:* Los modificadores de tu variante se sustituyen por los de la alianza ⏳ F4-133. *Personajes:* Casilda: aliada interesada. La Unión se mantiene. Reme paga o respira según su facción.
- **Fija:** `f-alianza`, `m-union`. **Lee:** `f-orden-reme`, `f-huelga`.
- **Nota sobre la lectura.** ✅ El nodo lee `f-orden-reme` solo para mostrar el costo de Reme (que paga o respira). Ninguna puerta lo lee ni lo usa para decidir.

**Cuellos:** `c-ii-apagon` (el apagón común) y `c-ii-cierre` (la escena A6 de Reme). La alianza cierra el acto.

---

## 5 · Acto III: el ascenso ✅

**Estado:** la grande «cómo entras al círculo» y sus tres entradas, y los ajustes A a D de [24](24-umbrales-de-acto.md) sobre las opciones de Esteban, Lucía, Teo y el círculo son decisión del autor (2026-10-12); las dos medianas, las cinco pequeñas y los demás efectos los confirmó el 2026-10-16 (F0-80). Las tres pequeñas de Quiroga, Lucía y el contrato oficial son los tres dilemas morales ⏳ F4-137, ⏳ F4-138 y ⏳ F4-139. El médico de la revisión de Teo es un figurante nuevo, el «médico del dispensario», que no está en el registro del mundo ⏳ F4-135. En el III la Aetherita solo se compra en el mercado negro y no se extrae hasta el IV, y eso es decisión del autor (2026-10-12)

La entrada que elijas decide quién te debe un favor en el IV:

| Entrada | Quién te debe el favor | Dónde lo cobras |
|---|---|---|
| Aval de Esteban | Esteban | `n-iv-esteban` |
| Sello de Montenegro | Quiroga (tramitó el sello); Montenegro no te debe nada | `n-iv-quiroga-archivo` |
| Presión de tu alianza | La facción aliada | `n-iv-comprador` |

**`n-iii-quiroga-salida` · Quiroga pide una salida** (pequeña) ✅
- **Dispara:** Llegas a Puerto Meridiano y Quiroga se ofrece a ayudarte en la capital a cambio de una salida. Dilema de favores ⏳ F4-137.
- **Le consigues el retiro que busca.** → *Mundo:* Quiroga te facilita los trámites en las oficinas. *Mercado:* Vigilancia −10. *Personajes:* Quiroga: leal a su manera; guarda su archivo como seguro.
- **Le prometes ayuda para más adelante.** → *Mundo:* Quiroga espera. *Mercado:* Vigilancia −5. *Personajes:* Quiroga: nervioso; su archivo es su seguro.
- **Lo dejas solo.** → *Mundo:* Quiroga sigue cobrando por su cuenta. *Personajes:* Quiroga: guarda el archivo por si acaso.
- **Fija:** `f-quiroga-salida`. **Lee:** `f-certificado`.

**`n-iii-lucia-letra` · La letra de un muerto** (pequeña) ✅
- **Dispara:** Lucía oyó que alguien de la Comisión recibe cartas con la letra de un muerto, y reconoce esa letra: es la firma de Anselmo ✅ (decisión del autor, 2026-10-12). No sabe que vive. Dilema de información ⏳ F4-139.
- **Le cuentas lo del certificado.** → *Mundo:* Lucía junta dos cabos y no publica todavía. *Personajes:* Lucía: confía más y sabe más de lo que dice.
- **Le pides que espere.** → *Mundo:* Lucía espera, con prisa. *Personajes:* Lucía: sin cambio.
- **Dices que no sabes nada.** → *Mundo:* Lucía sigue por su cuenta. *Personajes:* Lucía: no te cree y confía mucho menos.
- **Fija:** `m-lucia`. **Lee:** `f-certificado`.

**`n-iii-abono` · El abono que sigue llegando** (pequeña) ✅
- **Dispara:** El abono anónimo llega otra vez y Teo jura que no es él.
- **Le preguntas a Reme.** → *Mundo:* Reme cambia de tema: sigue distante pero atenta. *Personajes:* Reme: calla. Teo: sin cambio.
- **Le crees a Teo.** → *Mundo:* Teo respira. *Personajes:* Teo: alivio.
- **Dudas de Teo.** → *Mundo:* Teo se encierra en su silencio. *Personajes:* Teo: le duele mucho.
- **Fija:** `m-teo`. **Lee:** —.

**`n-iii-revision-teo` · Llevar a Teo a revisión** (mediana) ✅
- **Dispara:** La tos de Teo se nota en escena y Reme y Lucía lo comentan. La revisión solo puede decir «tos de mina».
- **Lo llevas al médico del dispensario, aunque proteste.** → *Mundo:* El médico dice «tos de mina»: reposo y aire. *Personajes:* Teo: gruñe y lo agradece.
- **Se lo propones y aceptas su no.** → *Mundo:* No hay revisión y no habrá otra ocasión: en el IV Teo muere. La opción te lo avisa antes de elegir. *Personajes:* Teo: sin cambio.
- **No sacas el tema.** → *Mundo:* No hay revisión y la tos empeora. *Personajes:* Teo: confía menos.
- **Fija:** `f-teo-revision` (sí o no), `m-teo`. **Lee:** `m-teo`.

**`n-iii-esteban-trato` · Esteban te pide algo en la bolsa** (pequeña) ✅
- **Dispara:** Esteban, guardián del círculo de la capital, te encuentra en la bolsa, antes de que elijas entrada.
- **Lo apoyas en una compra grande.** → *Mundo:* Esteban te presenta a gente del círculo. *Mercado:* El mineral que compra sube un 2 a 4 %. *Personajes:* Esteban: confía mucho en ti ✅ (ajuste A de [24](24-umbrales-de-acto.md)).
- **Aceptas con un límite claro.** → *Mundo:* Trato justo y sin deudas. *Mercado:* El mineral se mueve un 1 a 2 %. *Personajes:* Esteban: te respeta un poco más.
- **Compras antes que él.** → *Mundo:* Le ganas la compra. *Mercado:* El mineral baja un 2 a 3 % por la competencia. *Personajes:* Esteban: herido, y todo es personal.
- **Fija:** `m-esteban`. **Lee:** `f-alianza`.

**`n-iii-contrato-oficial` · Contrato oficial con cuota de entrega** (pequeña) ✅
- **Dispara:** Primer contrato oficial del Ministerio, con cuota de entrega obligatoria (su definición ⏳ F4-74). Dilema de sobornos ⏳ F4-138.
- **Cumples la cuota de entrega.** → *Mundo:* Montenegro lo anota: eres un proveedor fiable. *Mercado:* La cuota de entrega es el 10 % del volumen del contrato (no es la cuota de la deuda). *Personajes:* Quiroga: nada que cobrar.
- **Pagas una «gestión» para bajarla.** → *Mundo:* La cuota baja, pero queda registro. *Mercado:* Cuota de entrega −30 % a cambio del 5 % del valor del contrato, y vigilancia +10. *Personajes:* Quiroga o su oficial cobra la gestión.
- **Rechazas el contrato.** → *Mundo:* El contrato pasa a otro proveedor. *Mercado:* Pierdes la prima del contrato; vigilancia +10. *Personajes:* El Ministerio te mira más.
- **Fija:** —. **Lee:** `f-alianza`.

**`n-iii-monopolio` · El monopolio de la Aetherita negra** (mediana) ✅
- **Dispara:** Casilda negocia el monopolio de la Aetherita en el mercado negro (el Bar del Farol de Salinas Blancas y su visita nocturna a la tienda). En el III la Aetherita solo se compra ahí, como mercancía escasa; no se extrae hasta el IV ✅. En el IV la venta rutinaria va por el canal legal (la oficina de la Comisión en Puerto Meridiano): lo que Casilda controla son los **encargos especiales** del negro, raros y con historia ✅.
- **Dejas que Casilda lo controle.** → *Mundo:* Casilda manda en los encargos especiales de Aetherita del mercado negro, no en la venta rutinaria. *Mercado:* Prima negra de Aetherita +10 puntos, que se cobra en esos encargos ([28](28-numeros-base-de-la-economia.md), sección 3.6); la vigilancia sube un 20 % más despacio. *Personajes:* Casilda: socia interesada.
- **Pides tu parte.** → *Mundo:* Tú y Casilda os repartís el negocio. *Mercado:* Prima +5 puntos; vigilancia sin cambio. *Personajes:* Casilda: respeto seco.
- **No entras.** → *Mundo:* El Consorcio o el Ministerio ocupan el hueco. *Mercado:* Prima +0 puntos; la vigilancia sube un 10 % más rápido. *Personajes:* Casilda: cobra la luz de lo que toque.
- **Fija:** `f-monopolio`. **Lee:** `f-alianza`.

**`n-iii-circulo` · Cómo entras al círculo** (grande) ✅
- **Dispara:** Con el estatus de Empresario, dos vías de tres y una entrada abierta ([24](24-umbrales-de-acto.md)). Tres entradas, un solo encuentro con Montenegro, que cierra el acto.
- **Esteban te avala.** → *Mundo:* Entras al círculo con el aval del Consorcio. *Mercado:* Compras de hierro y cobre al Consorcio 2 a 3 % más baratas. *Personajes:* Esteban te debe un favor en el IV. Requiere su medidor en tramo alto ✅; si no lo tienes, el aval se muestra bloqueado con el motivo y quedan las otras dos entradas ✅.
- **Entras con el sello de Montenegro.** → *Mundo:* Es una firma y nada más: no te protege ni te ata. Montenegro no te debe nada. *Mercado:* Licencia ampliada; vigilancia +10. *Personajes:* Quiroga te debe un favor en el IV, porque tramitó el sello.
- **Entras con la presión de tu alianza.** → *Mundo:* Tu alianza empuja y el círculo cede. *Mercado:* Prima de contratos de tu alianza +3 a +5 puntos. *Personajes:* La facción aliada te debe un favor en el IV. Con el Consorcio o el Ministerio, la Unión baja ✅ (ajuste D de [24](24-umbrales-de-acto.md)).
- **Fija:** `f-entrada`, y `m-union` si entras por la presión de tu alianza. **Lee:** `f-alianza`, `m-esteban`, `m-union`.

**Cuello:** `c-iii-encuentro`. Montenegro te evalúa y te deja subir porque le sirves. No se le humaniza.

---

## 6 · Acto IV: la cima ✅

**Estado:** la grande (revelar, callar o vender), el destino de Teo, que el comprador se elige entre Casilda, el Consorcio y el Ministerio, que Lucía publica contigo en tramo alto, no publica en medio (lo publicas tú) y publica en La Voz del Hollín en bajo, y que el reproductor lo entrega Lucía en tramo alto y si no Reme (decisiones del autor, 2026-10-12); también qué hace cada tramo de Esteban en `n-iv-esteban` y de la Unión en `n-iv-montenegro` y `n-iv-aetherita`, y que «borrarte» solo ocurre con la Unión alta. Los demás efectos de las dos medianas y de las otras pequeñas, y el orden de juego (las cintas y el reproductor, Reme, Esteban, el archivo de Quiroga, el enfrentamiento con Montenegro, la Aetherita, el comprador, el desenlace de Montenegro, Lucía, Teo y el acta), los confirmó el autor el 2026-10-16 (F0-80); que el desenlace de Montenegro se decide al cerrar el acto, con el comprador ya fijado, también lo decidió el autor. Montenegro actúa con una regla única de prioridad y Lucía tiene pieza también al callar o vender; Anselmo sigue vivo y secreto en las tres salidas, y el abono se corta solo si revelas ([25](25-finales-y-epilogos.md)). Vender al Ministerio no es callar: el Ministerio se queda con tu prueba (los comprobantes y las cintas que usas) y contigo, no con el archivo de Quiroga, y eso está decidido. Al revelar, la Aetherita cae, rebota y queda algo por debajo del precio de antes, y eso está decidido. El reproductor lo entrega Lucía si su medidor está en tramo alto; con medio o bajo, Reme, y eso está decidido; el objeto ⏳ F4-150. Si Lucía está en tramo bajo, publica en La Voz del Hollín, a donde iba la cinta 6, y eso está decidido. Los tramos y lo que desbloquean: [24](24-umbrales-de-acto.md), sección 5.

**`n-iv-reme-proteccion` · Proteger a Reme** (pequeña) ✅
- **Dispara:** Reme se une a ti y te entrega los comprobantes del abono. Ahora tienes estatus para protegerla.
- **Usas tu influencia para ponerla a salvo.** → *Mundo:* Reme sale de la cadena de su facción. *Personajes:* Reme: aliada, con lágrimas contenidas. Su facción se enemista contigo.
- **Pagas el capital que su facción le prestó.** → *Mundo:* El préstamo de su facción queda saldado y Reme sale de la cadena. *Mercado:* Gasto grande: 150 000 esquirlas, el capital que su facción le prestó hace 25 años (no es la deuda de la herencia). *Personajes:* Reme: «criatura», sin ironía.
- **Dejas que decida ella.** → *Mundo:* Reme conserva su casa de préstamos y te ayuda por su cuenta. *Personajes:* Reme: aliada igual.
- **Fija:** `f-reme-proteccion`. **Lee:** `f-alianza`.

**`n-iv-esteban` · Esteban descubre el fondo reservado** (mediana) ✅
- **Dispara:** El libro del fondo reservado sale a la luz y Esteban debe elegir. Lo resuelve su medidor: alto se une, medio se aparta y bajo defiende al Consorcio ✅. El aval ya garantiza el tramo alto.
- **Esteban rompe con el Consorcio y te da el libro.** → *Mundo:* Las cuentas del Consorcio con la Comisión entran a tus pruebas. *Personajes:* Esteban: cambia su apellido por una verdad. Con su medidor en tramo alto; si entraste por el aval, es el favor que te debe.
- **Esteban defiende al Consorcio.** → *Mundo:* El Consorcio te cierra el acceso a sus contratos. *Mercado:* El hierro y el cobre suben 3 a 5 puntos como revancha. *Personajes:* Esteban: enemigo. Con su medidor en tramo bajo.
- **Esteban se aparta.** → *Mundo:* No ayuda ni estorba. *Personajes:* Esteban: sin camino claro; queda para el epílogo. Con su medidor en tramo medio.
- **Fija:** —. **Lee:** `m-esteban`, `f-entrada`.

**`n-iv-quiroga-archivo` · El archivo de Quiroga** (pequeña) ✅
- **Dispara:** Quiroga te ofrece su archivo de sobornos. Si entraste con el sello, te lo debe como favor y no cobra. No se puede destruir la copia del certificado ni la carta de la cinta 6.
- **Lo proteges, con Quiroga incluido.** → *Mundo:* Quiroga se retira con su archivo a salvo. *Personajes:* Quiroga: se va a Puerto Meridiano con lo ahorrado.
- **Lo usas contra el Ministerio.** → *Mundo:* Los sobornos salen a la luz. *Mercado:* Los contratos oficiales se congelan una semana. *Personajes:* Quiroga: cae con su archivo, salvo que le cumpliste la salida.
- **Lo vendes a quien lo pague.** → *Mundo:* El archivo cambia de manos. *Mercado:* Ingreso grande: 200 000 esquirlas. *Personajes:* Quiroga: queda a merced del comprador.
- **Fija:** `f-archivo`. **Lee:** `f-quiroga-salida`, `f-certificado`, `f-entrada`.

**`n-iv-montenegro` · Montenegro se mueve contra ti** (mediana) ✅
- **Dispara:** Enfrentamiento en La Fosa. Montenegro actúa con una **regla única de prioridad** ✅ (decisión del autor, 2026-10-12): si vendes al Ministerio, te compra con el sello; si no, y la Unión está en tramo alto y llevas al menos dos pruebas, intenta borrarte y falla; en el resto, te amenaza. Nunca cae, no se arrepiente ni nombra sucesor, y nunca se humaniza. Su desenlace se calcula al cerrar el acto, con el comprador ya fijado ✅ (decisión del autor, 2026-10-12), sin bandera nueva.
- **Montenegro intenta comprarte.** → *Mundo:* Te ofrece una concesión de Aetherita a cambio de callar y, si vendes al Ministerio, te compra con el sello ✅. *Personajes:* Montenegro: seco, sin disculpas ni ruego.
- **Montenegro te amenaza.** → *Mundo:* Nombra a Teo, a Reme y a tu familia. Se activa en el resto de los casos ✅. Pierde fuerza si protegiste a Reme. *Personajes:* Montenegro: no alza la voz.
- **Montenegro intenta borrarte.** → *Mundo:* Suspende tus licencias y manda cerrar tus zonas, pero **falla** ✅. Se activa si la Unión está en tramo alto y llevas al menos dos pruebas y no vendes al Ministerio. *Mercado:* Tus ventas caen a la mitad durante tres días y la vigilancia sube a Bajo investigación (una redada). *Personajes:* Montenegro: «No le pregunto qué opina»
- **Si revelas:** Montenegro queda bajo investigación, con resultado abierto, y el Ministerio emite un comunicado de una línea ✅.
- **Fija:** —. **Lee:** `f-entrada`, `f-familia`, `f-reme-proteccion`, `m-union`, `f-comprador`.

**`n-iv-aetherita` · El destino de la Aetherita** (grande) ✅
- **Dispara:** Con la verdad en la mano y las ocho cintas oídas. Antes de elegir se te muestra quién publicaría (el tramo de Lucía) y cómo está la Unión ✅ (su implementación ⏳ F4-142).
- **La revelas.** → *Mundo:* La verdad sale: caos social, el Ministerio contraataca. Con la Unión en tramo alto, sale contigo y el caos se contiene; con la Unión en tramo bajo, nadie te respalda en el Hollín ✅. *Mercado:* La Aetherita cae un 40 a 60 % en 5 a 8 días, en tramos del tope diario; después rebota y sube, porque su extracción es difícil y el mineral es limitado, y queda algo por debajo del precio de antes ✅. No deja de valer ni se acaba el mercado ✅. El tope diario es del 15 % ✅ y la caída escrita cabe en él; la curva y el nivel exacto ⏳ F4-147. *Personajes:* Te separas de Anselmo. La Comisión corta el abono mensual de Reme ✅ (hilo abierto para una segunda parte).
- **La callas.** → *Mundo:* Sigues ganando; el mal del éter sigue y nadie tiene la prueba. *Mercado:* La Aetherita sube un 5 a 10 % en el mes. *Personajes:* Te pareces a Anselmo. El abono sigue llegando ✅.
- **La vendes.** → *Mundo:* La verdad es moneda de poder: eliges comprador. *Mercado:* Depende del comprador. *Personajes:* Quien compra gana poder sobre ti.
- **Fija:** `f-destino`. **Lee:** `f-archivo`, `m-union`, `m-lucia`.

**`n-iv-comprador` · A quién vendes la verdad** (pequeña) ✅
- **Dispara:** Elegiste vender. Vender al Ministerio no es callar: el Ministerio se queda con tu prueba (los comprobantes y las cintas que usas) y contigo ✅. No se queda con el archivo de Quiroga ✅. Si entraste por la presión de tu alianza, la facción aliada te paga mejor.
- **A Casilda.** → *Mundo:* Casilda controla la verdad y su mercado negro. *Mercado:* Prima negra de Aetherita +10 a +15 puntos, que se cobra solo en los encargos especiales del negro. Con Casilda de compradora esos encargos llegan más a menudo (cada ~14 días en vez de ~21) y con más historia ✅; la Aetherita rutinaria sigue yendo a la Comisión. *Personajes:* Casilda: aliada interesada.
- **Al Consorcio.** → *Mundo:* El Consorcio financia el silencio ahora a tu nombre. *Mercado:* La Aetherita sube un 8 a 12 %. *Personajes:* Esteban: atrapado en su apellido.
- **Al Ministerio.** → *Mundo:* Montenegro te deja subir y se queda con tu prueba (los comprobantes y las cintas que usas), no con el archivo de Quiroga ✅ (si lo protegiste, sigue a salvo). *Mercado:* La Aetherita se mantiene (0 a +3 %) por la cuota. *Personajes:* Montenegro gana; tú te vuelves una pieza de la Comisión.
- **Fija:** `f-comprador`. **Lee:** `f-destino`, `f-monopolio`, `f-entrada`.

**`n-iv-lucia-publica` · Quién publica** (pequeña) ✅
- **Dispara:** La verdad sale a la luz o se filtra. Si revelas, depende del tramo de Lucía: alto, publica contigo; medio, no publica y lo publicas tú; bajo, publica sin ti ✅. Si callas o vendes: con su tramo bajo filtra una versión a medias, sin pruebas ni cintas; en medio o alto, calla ✅. Lucía nunca publica el acta ✅.
- **Lucía publica contigo.** → *Mundo:* Una sola versión, con las cintas completas. *Mercado:* La caída se da en tramos del tope diario, sin pánico extra. *Personajes:* Lucía: una sola lealtad.
- **Lucía publica en La Voz del Hollín sin ti.** → *Mundo:* Sale antes y a medias; la Unión se agita. *Mercado:* Cae al tope el primer día y rebota 5 a 10 puntos si el Heraldo desmiente. *Personajes:* Lucía: te traiciona por la historia.
- **Nadie publica.** → *Mundo:* Lucía guarda la historia y lo publicas tú. *Mercado:* Publicar te cuesta 60 000 esquirlas y llega a poca gente: la caída es más lenta. *Personajes:* Lucía: se queda con las ganas.
- **Fija:** —. **Lee:** `m-lucia`, `f-destino`, `f-comprador`.

**`n-iv-teo` · El destino de Teo** (pequeña) ✅
- **Dispara:** Teo confiesa lo que firmó. Se queda si hubo revisión y su confianza es media o alta, se va si hubo revisión y es baja, y muere si no hubo revisión, también si le propusiste y aceptaste su no. Si chocan, gana el no haberlo atendido.
- **Teo se queda.** → *Mundo:* Confiesa lo que firmó y sigue contigo en el Hollín. *Personajes:* Teo: reconciliado.
- **Teo se va.** → *Mundo:* Confiesa a medias y se va. *Personajes:* Teo: se despide sin rencor.
- **Teo muere.** → *Mundo:* Muere de «tos de mina». *Personajes:* Teo: la Unión lo recuerda.
- **Fija:** —. **Lee:** `f-teo-revision`, `m-teo`.

**Cuellos:** `c-iv-pruebas` y `c-iv-acta`. Las tres salidas terminan en la misma escena: la firma de Anselmo en el acta de calibración, sin discurso y con una línea breve del protagonista ✅. Cabecera, tarjetas y acta: [25](25-finales-y-epilogos.md).

---

## 7 · Las ocho cintas ✅

**Estado:** el acto en que se recoge cada una, que todas se oyen en el IV y quién entrega el reproductor (Lucía en tramo alto, si no Reme) son decisión del autor (2026-10-12); los ocho lugares donde las dejó Anselmo y el humor casi apagado de las cintas 7 y 8 los confirmó el 2026-10-16 (F0-80). Títulos y fechas en [21](21-pasado-de-valdoria.md), sección 7.

| # | Título | Se recoge en el acto ✅ | Dónde la dejó Anselmo ✅ |
|---|---|---|---|
| 1 | La lámpara y el sobrino | I | Puesto de Villa Brasa: doble fondo del cajón de la caja, junto a la libreta. |
| 2 | La Escuela y Montenegro | II | Minas de Sierra Alta: casillero del viejo taller de ensayo. |
| 3 | El hallazgo y la expedición | III | Puerto Meridiano: consigna de la estación, con una etiqueta de Anselmo. |
| 4 | Los primeros enfermos y Teo | III | Cavernas de Cristal: campamento de ensayo bajo el cuarzo. |
| 5 | Lo que midió | III | Puerto Meridiano: pensión donde Anselmo se alojaba al entregar sus informes. |
| 6 | La denuncia que preparó | IV | La Fosa: caja del equipo de ensayo que quedó en el campamento de la Primera Expedición. |
| 7 | La detención | IV | La Fosa: bajo la litera del barracón de calibración. |
| 8 | Cortada | IV | La Fosa: junto al registrador, el carrete cortado y sin etiqueta. |

- Anselmo las escondió él mismo en sitios de su vida, en los meses anteriores a la detención. Cada carrete lleva solo un número en la etiqueta: sin nombres ni fechas, para no romper la regla de una sombra por escena.
- Las cinco primeras se recogen en una misión de su acto, de modo que llegan siempre; las tres últimas esperan en La Fosa. Las cintas 1 a 5 son obligatorias para entrar al IV, no caducan y tienen misión persistente si faltan ✅ ([24](24-umbrales-de-acto.md), sección 9).
- Lucía oye hablar de las cintas en el III ([19](19-elenco-a-fondo.md)). El objeto y el sistema ⏳ F4-150 y su texto y sonido ⏳ F4-151
- El humor de Anselmo se apaga de la primera a la octava; quién cortó la octava queda abierto ✅ ([21](21-pasado-de-valdoria.md)).

---

## 8 · Pruebas de Reme en el Acto IV ✅

**Estado:** Reme entrega los comprobantes del abono, que son los sobres sin remitente del Acto II y el mismo hilo que la carta sin firma y el giro mensual ([21](21-pasado-de-valdoria.md), sección 6; decisión del autor, 2026-10-13). La prueba extra de cada variante y el resto del reparto, de [22](22-acto-ii-variantes.md), sección 11, los confirmó el autor el 2026-10-16 (F0-80).

| Variante de Reme | Prueba extra de Reme |
|---|---|
| Consorcio Arvel | El libro del fondo reservado: Reme vio los giros del Consorcio al pedir su préstamo. |
| Ministerio | La orden de la cadena: Reme la recibió por escrito, con sello. |
| Los Faroleros | El registro de informantes: Casilda le dejó copia al cobrarle la deuda de luz. |

| Prueba | De quién | Se puede perder |
|---|---|---|
| Comprobantes del abono (los sobres de cada mes) | Reme (común) | No |
| Prueba extra de su variante | Reme | No |
| Las ocho cintas | Anselmo | No |
| Copia del certificado y carta de la cinta 6 | Archivo de Quiroga | No: no se puede destruir |
| Cuentas del Consorcio con la Comisión | Esteban, si se une a ti | Sí |

Aunque vendas el archivo de Quiroga y Esteban se quede con el Consorcio, conservas los comprobantes, la prueba de Reme y las cintas: **al menos tres**. Si vendes al Ministerio, él se queda con esas pruebas al cerrar la venta ✅; para entonces la regla de Montenegro ya mandó con el sello, así que el conteo no importa ✅. El archivo de Quiroga no entra en esa venta ✅.

---

## 9 · Banderas: quién las fija y quién las lee ✅

**Estado:** el número de banderas y de medidores es decisión del autor (2026-10-12); los valores y a quién lee cada decisión los confirmó el 2026-10-16 (F0-80).

| Bandera | Tipo | Valores | La fija | La leen |
|---|---|---|---|---|
| `f-familia` | elección | todo / a medias / nada | `n-i-herencia` | `n-iv-montenegro` |
| `f-pago-reme` | elección | antes / a tiempo / tarde | `n-i-reme-plazo` | `n-ii-orden` |
| `f-orden-reme` | elección | aceptar / negociar / rechazar | `n-ii-orden` | `n-ii-conflicto`, `n-ii-alianza` |
| `f-huelga` | elección | apoyar / abstenerte / romper | `n-ii-huelga` | `n-ii-alianza` |
| `f-alianza` | elección | Consorcio / Ministerio / Faroleros | `n-ii-alianza` | `n-iii-esteban-trato`, `n-iii-contrato-oficial`, `n-iii-monopolio`, `n-iii-circulo`, `n-iv-reme-proteccion` |
| `f-certificado` | elección | copia / callar / presionar | `n-ii-certificado` | `n-iii-quiroga-salida`, `n-iii-lucia-letra`, `n-iv-quiroga-archivo` |
| `f-entrada` | elección | aval / sello / presión | `n-iii-circulo` | `n-iv-esteban`, `n-iv-quiroga-archivo`, `n-iv-montenegro`, `n-iv-comprador` |
| `f-monopolio` | elección | aceptar / compartir / rechazar | `n-iii-monopolio` | `n-iv-comprador` |
| `f-teo-revision` | elección | sí / no | `n-iii-revision-teo` | `n-iv-teo` |
| `f-quiroga-salida` | elección | ayudar / prometer / rechazar | `n-iii-quiroga-salida` | `n-iv-quiroga-archivo` |
| `f-reme-proteccion` | elección | proteger / saldar / dejar | `n-iv-reme-proteccion` | `n-iv-montenegro` |
| `f-archivo` | elección | proteger / usar / vender | `n-iv-quiroga-archivo` | `n-iv-aetherita` |
| `f-destino` | elección | revelar / callar / vender | `n-iv-aetherita` | `n-iv-comprador`, `n-iv-lucia-publica` |
| `f-comprador` | elección | Casilda / Consorcio / Ministerio | `n-iv-comprador` | `n-iv-lucia-publica` |
| `m-union` | medidor | 0 a 100 | `n-ii-conflicto`, `n-ii-huelga`, `n-ii-alianza`, `n-iii-circulo` | `n-iii-circulo`, `n-iv-montenegro`, `n-iv-aetherita` |
| `m-esteban` | medidor | 0 a 100 | `n-ii-contacto`, `n-ii-esteban-contrato`, `n-iii-esteban-trato` | `n-ii-esteban-contrato`, `n-iii-circulo`, `n-iv-esteban` |
| `m-lucia` | medidor | 0 a 100 | `n-i-lucia-rumor`, `n-ii-lucia`, `n-iii-lucia-letra` | `n-ii-lucia`, `n-iv-aetherita`, `n-iv-lucia-publica` |
| `m-teo` | medidor | 0 a 100 | `n-ii-huelga`, `n-iii-abono`, `n-iii-revision-teo` | `n-iii-revision-teo`, `n-iv-teo` |

---

## 10 · Riesgos de combinatoria

**Estado:** estimaciones del narrador. Los recorridos y las combinaciones se comprueban con la consola ⏳ F1-23 y el motor de epílogos ⏳ F4-210.

| Riesgo | Por qué importa | Cómo se contiene |
|---|---|---|
| Demasiados caminos | 13 banderas de tres valores y una de dos son unos 3 millones de combinaciones nominales | Se prueban por **cuello de botella**, no por camino. Los recorridos principales son 81: 3 variantes por 3 alianzas por 3 entradas por 3 destinos |
| Variantes de Reme por alianza | El costo de Reme cambia con su facción y con tu alianza: 9 casos, y se muestra antes de elegir ([22](22-acto-ii-variantes.md), sección 9) | Una sola escena A6 con tres capas |
| Medidores sin tramo | Sin umbrales, `n-iv-esteban`, `n-iv-lucia-publica` y `n-iv-teo` no se pueden probar | Tres tramos por medidor (bajo, medio, alto) ✅ y caminos a cada uno en [24](24-umbrales-de-acto.md), sección 6 |
| Textos que se multiplican | Cada pequeña añade un diálogo por opción | Las pequeñas cambian una frase o un medidor, no una escena |
| Opciones largas | Unas 30 de las 81 opciones de `decisions.json` pasan de 28 caracteres | Son descripciones para el equipo, no el texto del botón; el botón final se escribe al guionizar y respeta el límite de [18](18-biblia-narrativa.md), 1.9 ⏳ F4-128, ⏳ F4-135 y ⏳ F4-142 |
| Muertes que parecen injustas | Teo muere si no hubo revisión, también si aceptas su no | Avisos antes, incluido en la opción respetuosa (sección 2.4), y una sola regla que lo decide |
| Epílogos por camino | Un epílogo por cada combinación no se puede escribir | Epílogos **por piezas** que leen las banderas ✅ ([25](25-finales-y-epilogos.md): 54 piezas, unas 17 por partida) |
| Ramas que se contradicen | Una decisión del I cambia algo en el IV | Cada decisión solo lee lo fijado antes; el hub comprueba que toda bandera se fija y se lee |

---

## 11 · Criterios cumplidos

| Criterio | Cumplido | Dónde |
|---|---|---|
| Cupos exactos: 3 grandes, 6 medianas y 18 pequeñas (3/5/5/5) | Sí | `decisions.json` y sección 2.1 |
| Cada decisión dice quién la dispara, sus opciones y qué cambia en mundo, mercado y personajes | Sí | Secciones 3 a 6 |
| Cada bandera se fija y se lee al menos una vez | Sí | Sección 9 |
| Cada cuello recibe al menos dos ramas y ninguna decisión apunta a un acto anterior | Sí | Sección 2.3 |
| Facción de Reme como sorteo, no bifurcación | Sí | Sección 1; corregido en 08 y 18 |
| Reparto de las cintas y dónde las dejó Anselmo | Sí | Sección 7 |
| Pruebas de Reme por variante y mínimo de tres pruebas por ruta | Sí | Sección 8 |
| Cobertura de lo que el bosquejo no tocaba: monopolio de Casilda, Montenegro, Esteban en el IV y pequeñas del I | Sí | Secciones 3, 5 y 6 |
| Los 14 pendientes de F0-45 y las dos preguntas abiertas, resueltos | Sí | 08, 17, 18, 19, 21 y 22 |
| Fila de narrativa del IV: «Oyes las cintas» | Sí | `story.json` |

---

## Pendiente

- ✅ Epílogos por piezas: resueltos en [25](25-finales-y-epilogos.md). El motor ⏳ F4-210
- ✅ Umbrales de los medidores y de cada acto: resueltos en [24](24-umbrales-de-acto.md). El evaluador ⏳ F4-127
- ⏳ F4-61 Cifras y efectos de los medidores por facción.
- ⏳ F4-150 El reproductor y el sistema de cintas.
- ⏳ F4-147 La curva de la caída y el rebote de la Aetherita dentro del tope diario, y el nivel en que queda (algo por debajo del de antes ✅).
- ✅ Cifras de precios, cuotas, gastos y vigilancia: resueltas en [28](28-numeros-base-de-la-economia.md); su verificación con el simulador ✅ (F0-53, [28](28-numeros-base-de-la-economia.md) sección 13): la cuota del día 7 y los recargos se sostienen con el Aguante 28, la vía de deuda es alcanzable y la mora no cierra puertas; los ajustes de patrimonio, estatus y empleados los aprobó el autor.
- ⏳ F4-135 Guion del Acto III, con el médico del dispensario.
- ⏳ F0-75 Dibujo del árbol con conexiones (SVG) en el hub; la vista actual usa columnas, tarjetas y flechas de texto.
- ⏳ F4-213 Licencias (sello, revisión, ampliación y suspensión), ⏳ F4-214 rumores comprados y contados a Lucía y ⏳ F4-215 exclusividad de venta y entrega de cuentas: los sistemas que usan las decisiones del II y del III. La plantilla de guion con identificadores y condiciones ⏳ F4-216.
- ⏳ F4-62, ⏳ F4-63 y ⏳ F4-65 Las alianzas con el Ministerio, el Consorcio y Los Faroleros: sus efectos se definen por la alianza elegida, sin un medidor propio por facción.
- ✅ F0-45 está hecha y la lectura final F0-48 de este documento se cierra con esta revisión: términos (entrada, facción de Reme), vigilancia como «vigilancia +N», prórroga de la cuota y pruebas.
- ✅ F0-80 cerró este documento con el autor (2026-10-16): no queda ningún punto abierto; lo que depende de otras tareas lleva la tarea que lo resuelve.
