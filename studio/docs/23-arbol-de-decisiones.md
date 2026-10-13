# 23 · Árbol de decisiones y consecuencias

> ⚠️ **Contiene spoilers de toda la historia.** Es material para quien escribe y para quien programa la narrativa; no es para el jugador.

Todas las decisiones de los cuatro actos en un solo árbol: quién las dispara, qué opciones hay y qué cambian en el mundo, el mercado y los personajes. Los datos viven en `studio/data/decisions.json` (los valida el hub) y aquí se explican. Parte de [08](08-historia-y-personaje.md), [17](17-mapa-de-historia.md), [19](19-elenco-a-fondo.md), [21](21-pasado-de-valdoria.md), [22](22-acto-ii-variantes.md) y [03](03-comercio.md).

**Cómo leer las marcas.** La palomita verde es lo que decidió el autor. El círculo amarillo es propuesta del narrador. El reloj de arena lleva el ID de la tarea de la que depende. Un título lleva la palomita solo si todo lo que tiene debajo está confirmado; si mezcla, lleva el círculo y una nota «Estado». En las secciones de cada acto, un nodo con la palomita junto a su nombre es una decisión del autor; los demás son propuesta.

## Resumen en cinco líneas

1. El árbol tiene **27 decisiones**: 3 grandes, 6 medianas y 18 pequeñas.
2. Las grandes son la **alianza** (II), **cómo entras al círculo** (III) y el **destino de la Aetherita** (IV).
3. **14 banderas de elección y 4 medidores** (Unión, Esteban, Lucía y Teo) llevan el estado de una decisión a otra.
4. **Seis cuellos de botella** reúnen las ramas antes de cada gran escena, así que las historias se separan pero vuelven a juntarse.
5. Las **ocho cintas** se recogen antes (1 en el I, 2 en el II, 3 a 5 en el III y 6 a 8 en el IV) y solo se **oyen en el Acto IV**.

---

## 1 · Decisiones del autor ✅

Decisiones del 2026-10-12 (F0-45), más las que ya estaban en [22](22-acto-ii-variantes.md) y [19](19-elenco-a-fondo.md).

| Tema | Decisión |
|---|---|
| Cupos | **3 grandes, 6 medianas y 18 pequeñas** ✅ |
| Pequeñas por acto | **3 en el I, 5 en el II, 5 en el III y 5 en el IV** ✅ |
| Estado que se guarda | **Unas 14 banderas de elección y 4 medidores**: Unión, Esteban, Lucía y Teo ✅ |
| Las tres grandes | **Alianza** (II, escena A5), **cómo entras al círculo** (III) y **destino de la Aetherita** (IV: revelar, callar o vender) ✅ |
| Cómo entras al círculo | Tres puertas: el **aval de Esteban**, el **sello de Dueñas** (solo vale como firma, sin humanizarlo) o la **presión de tu alianza**. Todas llegan al **mismo encuentro con Dueñas** y la puerta fija **quién te debe un favor en el IV** ✅ |
| Destino de Teo | Se queda si su confianza es alta o media, se va si es baja y **muere si no hubo revisión en el III**, también si le propones y aceptas su no (la opción respetuosa tiene costo). Si chocan, gana el no haberlo atendido. La revisión solo puede decir «tos de mina» ✅ |
| Tramos de los medidores | **Bajo menos de 35, medio 35 a 54, alto 55 o más**, para Unión, Esteban, Lucía y Teo ✅ ([24](24-umbrales-de-acto.md)) |
| Lucía y el reproductor | Con tramo alto, Lucía publica contigo y entrega el reproductor. Con medio no publica (lo publicas tú, con costo alto y poco alcance) y con bajo publica en La Voz sin ti. Con medio o bajo, el reproductor lo entrega Reme ✅ |
| Aval de Esteban | Basta su medidor en tramo alto. Si no, se muestra bloqueado con el motivo y quedan el sello y la presión de tu alianza ✅ |
| Cintas | Se recogen antes (**1 en el I, 2 en el II, 3 a 5 en el III y 6 a 8 en el IV**) pero solo se oyen en el Acto IV, con un reproductor ✅ |
| Acreedor del Acto II | Es un **sorteo** al empezar la partida, **no una bifurcación jugable** ✅ |
| Acto II | La **huelga depende de ti** (apoyar, abstenerte o romper), la **orden de Reme** tiene tres salidas (aceptar, negociar o rechazar), la alianza es entre Consorcio, Ministerio y Faroleros, y **Dueñas no aparece** en el II ✅ |
| Reme | Siempre termina como **tu mayor aliada** ✅ |
| Canon que no se toca | Anselmo está vivo pero se cree muerto y enfermo, y es cómplice de la Comisión del Éter. Reme traiciona en el Acto II por obligación y al final es la mayor aliada. Dueñas es el enemigo claro, duro e inflexible ✅ |

---

## 2 · Reglas del árbol 🟡

**Estado:** ✅ los cupos, las banderas, los medidores y sus tramos de la sección 1; 🟡 las definiciones de nivel, los cuellos de botella y las reglas de seguridad, que propone el narrador. Todas las cifras de precios y de movimiento de los medidores son orientativas ⏳ F0-52 y ⏳ F4-61

### 2.1 Niveles

| Nivel | Qué cambia | Cupo | Reparto |
|---|---|---|---|
| **Grande** | Cambia el tramo de historia que sigue y lo recuerda el epílogo | 3 | 1 en el II, 1 en el III y 1 en el IV |
| **Mediana** | Cambia una escena entera o el destino de un personaje durante varios actos | 6 | 2 en el II, 2 en el III y 2 en el IV |
| **Pequeña** | Cambia un diálogo, un precio o un medidor | 18 | 3 en el I, 5 en el II, 5 en el III y 5 en el IV |

### 2.2 Banderas y medidores

- **Bandera de elección.** Guarda qué opción elegiste (dos o tres valores). Una decisión puede **fijar** una bandera y otra puede **leerla**. Una decisión solo lee banderas que se fijaron antes, en su acto o en uno anterior.
- **Medidor.** Número de 0 a 100. Arranca en 50, salvo Teo (60) y Esteban (40). Cada opción lo mueve poco (≈ 5), normal (≈ 10) o mucho (≈ 20) ⏳ F4-61. Los tramos son *bajo* (0 a 34), *medio* (35 a 54) y *alto* (55 o más) ✅, y qué desbloquea cada uno está en [24](24-umbrales-de-acto.md), sección 5. Los caminos a cada tramo que debe conservar F4-61 están en la sección 6 de ese documento
- **Los cuatro medidores.** **Unión** es el de la facción ([22](22-acto-ii-variantes.md), sección 9). **Esteban** es personal, no el del Consorcio ✅. **Lucía** y **Teo** miden cuánto confían en ti. **Dueñas no tiene medidor** ✅.
- **Desenlaces calculados.** Lo que hacen Esteban, Lucía y Dueñas en el IV no guarda una bandera nueva: se calcula leyendo medidores y banderas. El epílogo ⏳ F0-46 lee las mismas.
- **El sorteo no es una decisión.** La variante de Reme se fija antes de A1 y es oculta. Las decisiones del II la leen sin guardarla como bandera.

### 2.3 Cuellos de botella

Un cuello es un punto donde varias ramas se juntan. Así el árbol no se multiplica sin control: cada acto tiene al menos uno y todos reciben al menos dos ramas.

| Cuello | Acto | Qué reúne | Recibe |
|---|---|---|---|
| `c-i-cierre` | I | Las tres consecuencias del I se pierden en el mismo cierre: reabres el puesto, atiendes la primera cuota y tienes el primer contacto con los empleados. | `n-i-herencia`, `n-i-reme-plazo`, `n-i-lucia-rumor` |
| `c-ii-apagon` | II | El apagón del Hollín es común (22, sección 4): el conflicto, el contacto y la huelga cambian cómo lo vives, no si ocurre. | `n-ii-contacto`, `n-ii-conflicto`, `n-ii-huelga` |
| `c-ii-cierre` | II | A6: Reme calla el abono y paga o respira según su facción y tu alianza. Siempre termina como tu aliada. | `n-ii-orden`, `n-ii-huelga`, `n-ii-alianza` |
| `c-iii-encuentro` | III | Las tres puertas llegan al mismo encuentro con Dueñas. Cambian lo que te debe cada uno, no la escena. | `n-iii-circulo`, `n-iii-monopolio`, `n-iii-contrato-oficial`, `n-iii-esteban-trato` |
| `c-iv-pruebas` | IV | Todas las ramas llegan al enfrentamiento con al menos dos pruebas (sección 8). | `n-iv-reme-proteccion`, `n-iv-esteban`, `n-iv-quiroga-archivo` |
| `c-iv-acta` | IV | Revelar, callar o vender terminan en la misma última escena: el acta de calibración y la firma de Anselmo. | `n-iv-aetherita`, `n-iv-comprador`, `n-iv-lucia-publica`, `n-iv-teo` |

### 2.4 Reglas de seguridad

- **Ninguna puerta de acto lee `f-pago-reme` ni `f-orden-reme`** ✅ ([24](24-umbrales-de-acto.md)): Reme nunca cierra una puerta. `n-ii-alianza` lee `f-orden-reme` solo para mostrar el costo de Reme; no lo usa para decidir 🟡.
- **Ninguna rama cierra la ruta de Reme.** Rechazar su orden cambia el costo, no lo que puedes hacer después. Siempre termina como tu mayor aliada.
- **Cada ruta del IV conserva al menos dos pruebas** (sección 8). Nada de lo que hagas con el archivo de Quiroga destruye la copia del certificado ni la carta de la cinta 6.
- **Ningún personaje aparece antes de su acto:** Esteban y Casilda en el II, Dueñas en el III. En el II, Dueñas es solo decreto y firma.
- **Anselmo solo como sombra antes del IV**, con una sombra como máximo por escena. Las cintas se recogen en una misión, nunca dentro de una de las seis escenas ancla del II, y no se pueden oír hasta el IV.
- **Los avisos son justos.** Toda decisión con una consecuencia grave se anuncia antes: la tos de Teo se ve y los demás la comentan antes de la revisión.
- **El mercado se mide en puntos o en %.** El desplome de la Aetherita respeta el tope diario de variación de [03](03-comercio.md) ⏳ F0-52
- **El protagonista sigue siendo un optimista terco.** Ninguna opción lo hace cínico ni burlón con los trabajadores.

---

## 3 · Acto I: tres consecuencias pequeñas 🟡

**Estado:** ✅ el Acto I no tiene bifurcación grande y tiene 3 pequeñas; 🟡 cuáles son. Se activan en los días del tutorial ⏳ F0-23 y el guion ⏳ F3-16

**`n-i-herencia` · Cómo cuentas la herencia a tu familia** (pequeña)
- **Dispara:** Tu primera noche en Villa Brasa, cuando escribes a Vega Mansa ⏳ F0-23.
- **Les cuentas todo: el puesto, la deuda y la mina.** → *Mundo:* Tu padre contesta con una carta corta: sabe que rompiste su juramento. *Personajes:* Protagonista: duerme tranquilo. El padre: dolido, pero no te cierra la puerta.
- **Les cuentas que heredaste un puesto, sin decir mina.** → *Mundo:* En casa se alegran sin saber de la mina. *Personajes:* Protagonista: carga con un secreto pequeño.
- **No dices nada hasta tener algo que mostrar.** → *Mundo:* Pasan semanas sin carta de casa. *Personajes:* Protagonista: el orgullo le pesa más que la culpa.
- **Fija:** `f-familia`. **Lee:** —.

**`n-i-reme-plazo` · Pagar a Reme antes o después del plazo** (pequeña)
- **Dispara:** Llega el día de la primera cuota de la deuda.
- **Pagas antes del plazo.** → *Mundo:* Reme te invita al café y anota que eres de fiar. *Mercado:* Interés de la deuda: -1 punto ⏳ F0-52. *Personajes:* Reme: cálida, con una pizca de culpa.
- **Pagas justo en el plazo.** → *Mundo:* Todo sigue su curso. *Personajes:* Reme: «Con calma, criatura».
- **Pides una semana más.** → *Mundo:* Reme te da el tiempo, pero la cuota sube. *Mercado:* Interés de la deuda: +1 punto ⏳ F0-52. *Personajes:* Reme: te da el plazo con un consejo que suena a aviso.
- **Fija:** `f-pago-reme`. **Lee:** —.

**`n-i-lucia-rumor` · Confiar en Lucía con un rumor** (pequeña)
- **Dispara:** Lucía te ofrece un rumor a cambio de otro.
- **Le cuentas el rumor entero.** → *Mundo:* El Teletipo lo publica con su SIN CONFIRMAR. *Mercado:* El mineral del rumor se mueve 2 a 3 puntos ese día. *Personajes:* Lucía: confía más en ti.
- **Le cuentas la mitad.** → *Mundo:* Sale una nota vaga. *Mercado:* El mineral del rumor se mueve 1 punto. *Personajes:* Lucía: sospecha, pero te debe una.
- **No le cuentas nada.** → *Mundo:* No sale nada. *Personajes:* Lucía: toma nota y confía un poco menos.
- **Fija:** `m-lucia`. **Lee:** —.

**Cuello:** `c-i-cierre`. Las tres terminan en el mismo cierre del acto.

---

## 4 · Acto II: la política manda 🟡

**Estado:** ✅ la alianza (grande), la orden de Reme y la huelga (medianas) y sus opciones; 🟡 las cinco pequeñas, todos los efectos y las cifras. El orden de la lista es el de juego. Los efectos propios de cada variante están en [22](22-acto-ii-variantes.md), secciones 7 a 9. La escena O3 (Casilda te cita de noche) es un camino extra y no ramifica 🟡

**`n-ii-contacto` · Responder al primer contacto de la política** (pequeña)
- **Dispara:** Acto I cerrado (escena A1 de 22). El decreto de A1 es lo que abre las zonas del II; no es una condición previa 🟡 ⏳ F4-128.
- **Aceptas la cita.** → *Mundo:* Queda en cola la orden de Reme para tu próxima cuota. *Personajes:* Esteban, Quiroga o un cobrador farolero (según tu variante) te trata como cliente. Solo con el Consorcio sube el medidor de Esteban.
- **Rechazas la cita.** → *Mundo:* La facción lo toma como un desaire; la orden de Reme llega igual. *Personajes:* El contacto de tu variante te recuerda. Solo con el Consorcio baja el medidor de Esteban.
- **La pospones.** → *Mundo:* El contacto vuelve a aparecer en la siguiente zona. *Personajes:* Sin cambios.
- **Fija:** `m-esteban`. **Lee:** —.

**`n-ii-orden` · La orden de Reme** (mediana) ✅
- **Dispara:** Escena A2 de 22: llega tu próxima cuota a Reme y ella revela la facción que la manda (sorteada al empezar).
- **Aceptas lo que pide tu facción.** → *Mundo:* Cumples la petición de tu variante: vender solo al Consorcio, entregar tus cuentas o pagar la deuda de luz. *Mercado:* Consorcio: prima de contrato +3 a +5 puntos, pero un solo comprador. Ministerio: el Ministerio ve tus cuentas. Faroleros: cuota extra de luz ⏳ F0-52. *Personajes:* Reme: alivio y vergüenza. «Perdóname, criatura. Esto no lo elegí yo».
- **Negocias con Labia una versión más corta.** → *Mundo:* Si la prueba sale bien, cumples solo la mitad de la petición. *Mercado:* La mitad del efecto de aceptar. *Personajes:* Reme: orgullosa de ti, sin decirlo.
- **Rechazas la orden.** → *Mundo:* La cuota de la deuda se adelanta. La ruta sigue abierta. *Mercado:* Adelanto de la cuota ⏳ F0-52; menor si pagaste a tiempo en el Acto I. *Personajes:* Reme: calla un segundo. Su facción le cobra un costo.
- **Fija:** `f-orden-reme`. **Lee:** `f-pago-reme`.

**`n-ii-conflicto` · Resolver el primer conflicto con tu facción** (pequeña)
- **Dispara:** Escena A3 de 22: primera expedición o venta en la zona de tu variante (contratos, licencias o cobros de luz).
- **Pagas el costo y sigues.** → *Mundo:* El conflicto se cierra sin ruido. *Mercado:* Pierdes 3 a 5 % del valor de tus ventas de esa semana en la zona. *Personajes:* La facción te respeta.
- **Cedes lo que piden.** → *Mundo:* Pierdes un contrato, pasas una revisión de licencia o dejas una noche de luz a la facción. *Personajes:* La Unión lo nota: baja un poco.
- **Te plantas.** → *Mundo:* El conflicto escala y la facción fija su postura ante la huelga. *Mercado:* Sin prima de la zona esa semana. *Personajes:* La Unión lo nota: sube un poco.
- **Fija:** `m-union`. **Lee:** `f-orden-reme`.

**`n-ii-huelga` · La primera huelga** (mediana) ✅
- **Dispara:** Escena A4 de 22: el aviso sale en las noticias y la huelga cierra Cañón Ferroso. Ocurre en las tres variantes.
- **Apoyas la huelga.** → *Mundo:* Cierras el puesto un día y entregas mineral a la caja de huelga. Luego llega el apagón, común a todos. *Mercado:* Hierro +8 a +12 % mientras dura el cierre, dentro del tope diario; el segundo mineral de tu variante, +3 a +5 puntos. *Personajes:* Teo y la Unión se acercan. Tu variante añade una consecuencia pequeña (22, sección 7).
- **Te abstienes.** → *Mundo:* Sigues con tu negocio. Llega el mismo apagón. *Mercado:* Mismo movimiento de precios para todos. *Personajes:* Teo y la Unión no cambian. No se activa ninguna consecuencia de variante.
- **Rompes la huelga.** → *Mundo:* Vendes el mineral que pide quien quiere la huelga rota. Luego llega el mismo apagón. *Mercado:* Mismo movimiento de precios; la prima de contrato de tu variante sube 3 a 5 puntos. *Personajes:* Teo y la Unión se alejan mucho. Tu variante añade una consecuencia pequeña (22, sección 7).
- **Fija:** `f-huelga`, `m-teo`, `m-union`. **Lee:** —.

**`n-ii-lucia` · Lo que vende Lucía** (pequeña)
- **Dispara:** Comprar tres rumores (escena opcional O1 de 22).
- **La confrontas.** → *Mundo:* Lucía deja de venderte rumores flojos. *Personajes:* Lucía: admite a medias y confía más.
- **Usas su doble juego.** → *Mundo:* Le das un dato para que llegue a la otra parte (Esteban, Quiroga o los informantes de Casilda). *Mercado:* Un rumor mueve un mineral 2 a 3 puntos. *Personajes:* Lucía: si lo descubre, confía menos.
- **Te lo guardas.** → *Mundo:* Sigues leyendo sus rumores con cuidado. *Personajes:* Lucía: no se entera.
- **Fija:** `m-lucia`. **Lee:** `m-lucia`.

**`n-ii-esteban-contrato` · Esteban se queda un contrato** (pequeña)
- **Dispara:** Rechazas o tardas en un contrato de hierro o cobre (escena opcional O2 de 22).
- **Compites por el siguiente contrato.** → *Mundo:* Recuperas el contrato siguiente. *Mercado:* Pierdes 3 a 5 puntos de margen en ese contrato. *Personajes:* Esteban: te respeta, aunque diga «amigo» más seco.
- **Se lo dejas.** → *Mundo:* Esteban se lleva este contrato y el siguiente. *Mercado:* Esteban compra y empuja el precio un 2 a 4 %. *Personajes:* Esteban: más seguro y con menos respeto por ti.
- **Le avisas a Quiroga de su papeleo.** → *Mundo:* Quiroga revisa los papeles de Esteban y se los devuelve con un retraso. *Mercado:* El contrato se retrasa una semana. *Personajes:* Esteban: «No es personal… es completamente personal». Baja mucho.
- **Fija:** `m-esteban`. **Lee:** `m-esteban`.

**`n-ii-certificado` · El certificado a solas** (pequeña)
- **Dispara:** Primera visita a Quiroga después de la orden (escena opcional O4 de 22). Si no ocurre, A5 siembra la pista.
- **Le pides una copia.** → *Mundo:* Quiroga la da con una «gestión» y se pone nervioso. *Mercado:* Una gestión pequeña ⏳ F0-52. *Personajes:* Quiroga: anota que lo sabes.
- **Miras el sello y no dices nada.** → *Mundo:* Te quedas con la sombra: sello irregular y sin registro de cremación. *Personajes:* Quiroga: respira aliviado.
- **Le dices que sabes lo del sello.** → *Mundo:* Quiroga se vuelve dependiente de ti. *Mercado:* Vigilancia -10 en Villa Brasa. *Personajes:* Quiroga: te teme y te necesita.
- **Fija:** `f-certificado`. **Lee:** —.

**`n-ii-alianza` · La alianza** (grande) ✅
- **Dispara:** Escena A5 de 22: tras la huelga y con estatus de Comerciante, llegan las tres ofertas. Cierra el Acto II.
- **Te alías con el Consorcio Arvel.** → *Mundo:* Contratos grandes y tu deuda pasa a la casa. *Mercado:* Los modificadores de tu variante se sustituyen por los de la alianza ⏳ F4-133. *Personajes:* Esteban: socio incómodo. La Unión baja. Reme paga o respira según su facción (22, sección 9).
- **Te alías con el Ministerio.** → *Mundo:* Licencia ampliada y trámite preferente. *Mercado:* Los modificadores de tu variante se sustituyen por los de la alianza ⏳ F4-133. *Personajes:* Quiroga: tu enlace. La Unión baja. Reme paga o respira según su facción.
- **Te alías con Los Faroleros.** → *Mundo:* Protección y luz; tu deuda de luz se suma a tu deuda. *Mercado:* Los modificadores de tu variante se sustituyen por los de la alianza ⏳ F4-133. *Personajes:* Casilda: aliada interesada. La Unión se mantiene. Reme paga o respira según su facción.
- **Fija:** `f-alianza`, `m-union`. **Lee:** `f-orden-reme`, `f-huelga`.
- **Nota sobre la lectura.** 🟡 El nodo lee `f-orden-reme` solo para mostrar el costo de Reme (que paga o respira). Ninguna puerta lo lee ni lo usa para decidir.

**Cuellos:** `c-ii-apagon` (el apagón común) y `c-ii-cierre` (la escena A6 de Reme). La alianza cierra el acto.

---

## 5 · Acto III: el ascenso 🟡

**Estado:** ✅ la grande «cómo entras al círculo» y sus tres puertas, y los ajustes A a D de [24](24-umbrales-de-acto.md) sobre las opciones de Esteban, Lucía, Teo y el círculo (decisión del autor, 2026-10-12); 🟡 las dos medianas, las cinco pequeñas y los demás efectos. Las tres pequeñas de Quiroga, Lucía y el contrato oficial son los tres dilemas morales ⏳ F4-137, ⏳ F4-138 y ⏳ F4-139. El médico de la revisión de Teo es un figurante nuevo, el «médico del dispensario», que no está en el registro del mundo ⏳ F4-135

La puerta que elijas decide quién te debe un favor en el IV:

| Puerta | Quién te debe el favor | Dónde lo cobras |
|---|---|---|
| Aval de Esteban | Esteban | `n-iv-esteban` |
| Sello de Dueñas | Quiroga (tramitó el sello); Dueñas no te debe nada | `n-iv-quiroga-archivo` |
| Presión de tu alianza | La facción aliada | `n-iv-comprador` |

**`n-iii-quiroga-salida` · Quiroga pide una salida** (pequeña)
- **Dispara:** Llegas a Puerto Meridiano y Quiroga se ofrece a ayudarte en la capital a cambio de una salida. Dilema de favores ⏳ F4-137.
- **Le consigues el retiro que busca.** → *Mundo:* Quiroga te abre puertas en las oficinas. *Mercado:* Vigilancia -10 en Puerto Meridiano. *Personajes:* Quiroga: leal a su manera; guarda su archivo como seguro.
- **Le prometes ayuda para más adelante.** → *Mundo:* Quiroga espera. *Mercado:* Vigilancia -5 en Puerto Meridiano. *Personajes:* Quiroga: nervioso; su archivo es su seguro.
- **Lo dejas solo.** → *Mundo:* Quiroga sigue cobrando por su cuenta. *Personajes:* Quiroga: guarda el archivo por si acaso.
- **Fija:** `f-quiroga-salida`. **Lee:** `f-certificado`.

**`n-iii-lucia-letra` · La letra de un muerto** (pequeña)
- **Dispara:** Lucía oyó que alguien de la Comisión recibe cartas con la letra de un muerto. Dilema de información ⏳ F4-139.
- **Le cuentas lo del certificado.** → *Mundo:* Lucía junta dos cabos y no publica todavía. *Personajes:* Lucía: confía más y sabe más de lo que dice.
- **Le pides que espere.** → *Mundo:* Lucía espera, con prisa. *Personajes:* Lucía: sin cambio.
- **Dices que no sabes nada.** → *Mundo:* Lucía sigue por su cuenta. *Personajes:* Lucía: no te cree y confía mucho menos.
- **Fija:** `m-lucia`. **Lee:** `f-certificado`.

**`n-iii-abono` · El abono que sigue llegando** (pequeña)
- **Dispara:** El abono anónimo llega otra vez y Teo jura que no es él.
- **Le preguntas a Reme.** → *Mundo:* Reme cambia de tema: sigue distante pero atenta. *Personajes:* Reme: calla. Teo: sin cambio.
- **Le crees a Teo.** → *Mundo:* Teo respira. *Personajes:* Teo: alivio.
- **Dudas de Teo.** → *Mundo:* Teo se encierra en su silencio. *Personajes:* Teo: le duele mucho.
- **Fija:** `m-teo`. **Lee:** —.

**`n-iii-revision-teo` · Llevar a Teo a revisión** (mediana)
- **Dispara:** La tos de Teo se nota en escena y Reme y Lucía lo comentan. La revisión solo puede decir «tos de mina».
- **Lo llevas al médico del dispensario, aunque proteste.** → *Mundo:* El médico dice «tos de mina»: reposo y aire. *Personajes:* Teo: gruñe y lo agradece.
- **Se lo propones y aceptas su no.** → *Mundo:* No hay revisión y no habrá otra ocasión: en el IV Teo muere. La opción te lo avisa antes de elegir. *Personajes:* Teo: sin cambio.
- **No sacas el tema.** → *Mundo:* No hay revisión y la tos empeora. *Personajes:* Teo: confía menos.
- **Fija:** `f-teo-revision` (sí o no), `m-teo`. **Lee:** `m-teo`.

**`n-iii-esteban-trato` · Esteban te pide algo en la bolsa** (pequeña)
- **Dispara:** Esteban, guardián del círculo de la capital, te encuentra en la bolsa, antes de que elijas puerta.
- **Lo apoyas en una compra grande.** → *Mundo:* Esteban te presenta a gente del círculo. *Mercado:* El mineral que compra sube un 2 a 4 %. *Personajes:* Esteban: confía mucho en ti ✅ (ajuste A de [24](24-umbrales-de-acto.md)).
- **Aceptas con un límite claro.** → *Mundo:* Trato justo y sin deudas. *Mercado:* El mineral se mueve un 1 a 2 %. *Personajes:* Esteban: te respeta un poco más.
- **Compras antes que él.** → *Mundo:* Le ganas la compra. *Mercado:* El mineral baja un 2 a 3 % por la competencia. *Personajes:* Esteban: herido, y todo es personal.
- **Fija:** `m-esteban`. **Lee:** `f-alianza`.

**`n-iii-contrato-oficial` · Contrato oficial con cuota** (pequeña)
- **Dispara:** Primer contrato oficial del Ministerio, con cuota. Dilema de sobornos ⏳ F4-138.
- **Cumples la cuota.** → *Mundo:* Dueñas lo anota: eres un proveedor fiable. *Mercado:* Cuota de un 10 % del volumen del contrato ⏳ F0-52. *Personajes:* Quiroga: nada que cobrar.
- **Pagas una «gestión» para bajarla.** → *Mundo:* La cuota baja, pero queda registro. *Mercado:* Cuota -30 % y vigilancia +10. *Personajes:* Quiroga o su oficial cobra la gestión.
- **Rechazas el contrato.** → *Mundo:* El contrato pasa a otro proveedor. *Mercado:* Pierdes la prima del contrato; vigilancia +10. *Personajes:* El Ministerio te mira más.
- **Fija:** —. **Lee:** `f-alianza`.

**`n-iii-monopolio` · El monopolio de la Aetherita negra** (mediana)
- **Dispara:** Casilda negocia el monopolio del mercado negro de Aetherita en la capital.
- **Dejas que Casilda lo controle.** → *Mundo:* Casilda manda en la venta clandestina de Aetherita. *Mercado:* Prima negra de Aetherita +10 puntos; vigilancia -20 %. *Personajes:* Casilda: socia interesada.
- **Pides tu parte.** → *Mundo:* Tú y Casilda os repartís el negocio. *Mercado:* Prima +5 puntos; vigilancia sin cambio. *Personajes:* Casilda: respeto seco.
- **No entras.** → *Mundo:* El Consorcio o el Ministerio ocupan el hueco. *Mercado:* Prima +0 puntos; vigilancia +10 %. *Personajes:* Casilda: cobra la luz de lo que toque.
- **Fija:** `f-monopolio`. **Lee:** `f-alianza`.

**`n-iii-circulo` · Cómo entras al círculo** (grande) ✅
- **Dispara:** Con el estatus de Empresario, dos vías de tres y una puerta abierta ([24](24-umbrales-de-acto.md)). Tres puertas, un solo encuentro con Dueñas, que cierra el acto.
- **Esteban te avala.** → *Mundo:* Entras por la puerta del Consorcio. *Mercado:* Compras de hierro y cobre al Consorcio 2 a 3 % más baratas. *Personajes:* Esteban te debe un favor en el IV. Requiere su medidor en tramo alto ✅; si no lo tienes, el aval se muestra bloqueado con el motivo y quedan las otras dos puertas ✅.
- **Entras con el sello de Dueñas.** → *Mundo:* Es una firma y nada más: no te protege ni te ata. Dueñas no te debe nada. *Mercado:* Licencia ampliada; vigilancia +10. *Personajes:* Quiroga te debe un favor en el IV, porque tramitó el sello.
- **Entras con la presión de tu alianza.** → *Mundo:* Tu alianza empuja y el círculo cede. *Mercado:* Prima de contratos de tu alianza +3 a +5 puntos. *Personajes:* La facción aliada te debe un favor en el IV. Con el Consorcio o el Ministerio, la Unión baja ✅ (ajuste D de [24](24-umbrales-de-acto.md)).
- **Fija:** `f-puerta`, y `m-union` si entras por la presión de tu alianza. **Lee:** `f-alianza`, `m-esteban`, `m-union`.

**Cuello:** `c-iii-encuentro`. Dueñas te evalúa y te deja subir porque le sirves. No se le humaniza.

---

## 6 · Acto IV: la cima 🟡

**Estado:** ✅ la grande (revelar, callar o vender), el destino de Teo, que el comprador se elige entre Casilda, el Consorcio y el Ministerio, que Lucía publica contigo en tramo alto, no publica en medio (lo publicas tú) y publica en La Voz del Hollín en bajo, y que el reproductor lo entrega Lucía en tramo alto y si no Reme (decisiones del autor, 2026-10-12); ✅ también qué hace cada tramo de Esteban en `n-iv-esteban` y de la Unión en `n-iv-duenas` y `n-iv-aetherita`, y que «borrarte» solo ocurre con la Unión alta; 🟡 los demás efectos de las dos medianas y de las otras pequeñas. Orden de juego: las cintas y el reproductor, Reme, Esteban, el archivo de Quiroga, Dueñas, la Aetherita, el comprador, Lucía, Teo y el acta. Vender al Ministerio no es callar: el Ministerio se queda con la prueba y contigo ✅. El reproductor lo entrega Lucía si su medidor está en tramo alto; con medio o bajo, Reme ✅; el objeto ⏳ F4-150. Si Lucía está en tramo bajo, publica en La Voz del Hollín, a donde iba la cinta 6 ✅. Los tramos y lo que desbloquean: [24](24-umbrales-de-acto.md), sección 5.

**`n-iv-reme-proteccion` · Proteger a Reme** (pequeña)
- **Dispara:** Reme se une a ti y te entrega los comprobantes del abono. Ahora tienes estatus para protegerla.
- **Usas tu influencia para ponerla a salvo.** → *Mundo:* Reme sale de la cadena de su facción. *Personajes:* Reme: aliada, con lágrimas contenidas. Su facción se enemista contigo.
- **Pagas el capital que su facción le prestó.** → *Mundo:* La deuda de Reme queda en cero. *Mercado:* Gasto grande ⏳ F0-52. *Personajes:* Reme: «criatura», sin ironía.
- **Dejas que decida ella.** → *Mundo:* Reme conserva su casa de préstamos y te ayuda por su cuenta. *Personajes:* Reme: aliada igual.
- **Fija:** `f-reme-proteccion`. **Lee:** `f-alianza`.

**`n-iv-esteban` · Esteban descubre el fondo reservado** (mediana)
- **Dispara:** El libro del fondo reservado sale a la luz y Esteban debe elegir. Lo resuelve su medidor: alto se une, medio se aparta y bajo defiende al Consorcio ✅. La puerta del aval ya garantiza el tramo alto.
- **Esteban rompe con el Consorcio y te da el libro.** → *Mundo:* Las cuentas del Consorcio con la Comisión entran a tus pruebas. *Personajes:* Esteban: cambia su apellido por una verdad. Con su medidor en tramo alto; si entraste por el aval, es el favor que te debe.
- **Esteban defiende al Consorcio.** → *Mundo:* El Consorcio te cierra puertas. *Mercado:* El hierro y el cobre suben 3 a 5 puntos como revancha. *Personajes:* Esteban: enemigo. Con su medidor en tramo bajo.
- **Esteban se aparta.** → *Mundo:* No ayuda ni estorba. *Personajes:* Esteban: sin camino claro; queda para el epílogo. Con su medidor en tramo medio.
- **Fija:** —. **Lee:** `m-esteban`, `f-puerta`.

**`n-iv-quiroga-archivo` · El archivo de Quiroga** (pequeña)
- **Dispara:** Quiroga te ofrece su archivo de sobornos. Si entraste con el sello, te lo debe como favor y no cobra. No se puede destruir la copia del certificado ni la carta de la cinta 6.
- **Lo proteges, con Quiroga incluido.** → *Mundo:* Quiroga se retira con su archivo a salvo. *Personajes:* Quiroga: se va a Puerto Meridiano con lo ahorrado.
- **Lo usas contra el Ministerio.** → *Mundo:* Los sobornos salen a la luz. *Mercado:* Los contratos oficiales se congelan una semana. *Personajes:* Quiroga: cae con su archivo, salvo que le cumpliste la salida.
- **Lo vendes a quien lo pague.** → *Mundo:* El archivo cambia de manos. *Mercado:* Ingreso grande ⏳ F0-52. *Personajes:* Quiroga: queda a merced del comprador.
- **Fija:** `f-archivo`. **Lee:** `f-quiroga-salida`, `f-certificado`, `f-puerta`.

**`n-iv-duenas` · Dueñas se mueve contra ti** (mediana)
- **Dispara:** Enfrentamiento en La Fosa. Dueñas elige cómo según la puerta que usaste, tu gente y tu fuerza. Nunca se humaniza.
- **Dueñas intenta comprarte.** → *Mundo:* Te ofrece una concesión de Aetherita a cambio de callar. Se activa si entraste con su sello. *Personajes:* Dueñas: seco, sin disculpas ni ruego.
- **Dueñas te amenaza.** → *Mundo:* Nombra a Teo, a Reme y a tu familia. Se activa si entraste por el aval o por tu alianza. Pierde fuerza si protegiste a Reme. *Personajes:* Dueñas: no alza la voz.
- **Dueñas intenta borrarte.** → *Mundo:* Suspende tus licencias y manda cerrar tus zonas. Se activa si la Unión está en tramo alto y llevas al menos dos pruebas. *Mercado:* Tus ventas caen a la mitad durante tres días y la vigilancia pasa a Bajo investigación. *Personajes:* Dueñas: «No le pregunto qué opina»
- **Fija:** —. **Lee:** `f-puerta`, `f-familia`, `f-reme-proteccion`, `m-union`.

**`n-iv-aetherita` · El destino de la Aetherita** (grande) ✅
- **Dispara:** Con la verdad en la mano y las ocho cintas oídas. Antes de elegir se te muestra quién publicaría (el tramo de Lucía) y cómo está la Unión 🟡 ⏳ F4-142.
- **La revelas.** → *Mundo:* La verdad sale: caos social, el Ministerio contraataca. Con la Unión en tramo alto, sale contigo y el caos se contiene; con la Unión en tramo bajo, nadie te respalda en el Hollín ✅. *Mercado:* La Aetherita cae un 40 a 60 % en 5 a 8 días, en tramos del tope diario ⏳ F4-147. *Personajes:* Te separas de Anselmo.
- **La callas.** → *Mundo:* Sigues ganando; el mal del éter sigue y nadie tiene la prueba. *Mercado:* La Aetherita sube un 5 a 10 % en el mes. *Personajes:* Te pareces a Anselmo.
- **La vendes.** → *Mundo:* La verdad es moneda de poder: eliges comprador. *Mercado:* Depende del comprador. *Personajes:* Quien compra gana poder sobre ti.
- **Fija:** `f-destino`. **Lee:** `f-archivo`, `m-union`, `m-lucia`.

**`n-iv-comprador` · A quién vendes la verdad** (pequeña)
- **Dispara:** Elegiste vender. Vender al Ministerio no es callar: el Ministerio se queda con la prueba y contigo. Si entraste por la presión de tu alianza, la facción aliada te paga mejor.
- **A Casilda.** → *Mundo:* Casilda controla la verdad y su mercado negro. *Mercado:* Prima negra de Aetherita +10 a +15 puntos. *Personajes:* Casilda: aliada interesada.
- **Al Consorcio.** → *Mundo:* El Consorcio financia el silencio ahora a tu nombre. *Mercado:* La Aetherita sube un 8 a 12 %. *Personajes:* Esteban: atrapado en su apellido.
- **Al Ministerio.** → *Mundo:* Dueñas te deja subir y se queda con tu archivo. *Mercado:* La Aetherita se mantiene (0 a +3 %) por la cuota. *Personajes:* Dueñas gana; tú te vuelves una pieza de la Comisión.
- **Fija:** `f-comprador`. **Lee:** `f-destino`, `f-monopolio`, `f-puerta`.

**`n-iv-lucia-publica` · Quién publica** (pequeña)
- **Dispara:** La verdad sale a la luz o se filtra. Depende del tramo de Lucía: alto, publica contigo; medio, no publica y lo publicas tú; bajo, publica sin ti.
- **Lucía publica contigo.** → *Mundo:* Una sola versión, con las cintas completas. *Mercado:* La caída se da en tramos del tope diario, sin pánico extra. *Personajes:* Lucía: una sola lealtad.
- **Lucía publica en La Voz del Hollín sin ti.** → *Mundo:* Sale antes y a medias; la Unión se agita. *Mercado:* Cae al tope el primer día y rebota 5 a 10 puntos si el Heraldo desmiente. *Personajes:* Lucía: te traiciona por la historia.
- **Nadie publica.** → *Mundo:* Lucía guarda la historia y lo publicas tú. *Mercado:* Publicar te cuesta caro ⏳ F0-52 y llega a poca gente: la caída es más lenta. *Personajes:* Lucía: se queda con las ganas.
- **Fija:** —. **Lee:** `m-lucia`, `f-destino`, `f-comprador`.

**`n-iv-teo` · El destino de Teo** (pequeña) ✅
- **Dispara:** Teo confiesa lo que firmó. Se queda si hubo revisión y su confianza es media o alta, se va si hubo revisión y es baja, y muere si no hubo revisión, también si le propusiste y aceptaste su no. Si chocan, gana el no haberlo atendido.
- **Teo se queda.** → *Mundo:* Confiesa lo que firmó y sigue contigo en el Hollín. *Personajes:* Teo: reconciliado.
- **Teo se va.** → *Mundo:* Confiesa a medias y se va. *Personajes:* Teo: se despide sin rencor.
- **Teo muere.** → *Mundo:* Muere de «tos de mina». *Personajes:* Teo: la Unión lo recuerda.
- **Fija:** —. **Lee:** `f-teo-revision`, `m-teo`.

**Cuellos:** `c-iv-pruebas` y `c-iv-acta`. Las tres salidas terminan en la misma escena: la firma de Anselmo en el acta de calibración, sin discurso. Epílogos ⏳ F0-46

---

## 7 · Las ocho cintas 🟡

**Estado:** ✅ el acto en que se recoge cada una, que todas se oyen en el IV y quién entrega el reproductor (Lucía en tramo alto, si no Reme); 🟡 el lugar donde las dejó Anselmo. Títulos y fechas en [21](21-pasado-de-valdoria.md), sección 7.

| # | Título | Se recoge en el acto ✅ | Dónde la dejó Anselmo 🟡 |
|---|---|---|---|
| 1 | La lámpara y el sobrino | I | Puesto de Villa Brasa: doble fondo del cajón de la caja, junto a la libreta. |
| 2 | La Escuela y Dueñas | II | Minas de Sierra Alta: casillero del viejo taller de ensayo. |
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

## 8 · Pruebas de Reme en el Acto IV 🟡

**Estado:** ✅ Reme entrega los comprobantes del abono ([21](21-pasado-de-valdoria.md), sección 6); 🟡 la prueba extra de cada variante y el resto del reparto, de [22](22-acto-ii-variantes.md), sección 11.

| Variante de Reme | Prueba extra de Reme |
|---|---|
| Consorcio Arvel | El libro del fondo reservado: Reme vio los giros del Consorcio al pedir su préstamo. |
| Ministerio | La orden de la cadena: Reme la recibió por escrito, con sello. |
| Los Faroleros | El registro de informantes: Casilda le dejó copia al cobrarle la deuda de luz. |

| Prueba | De quién | Se puede perder |
|---|---|---|
| Comprobantes del abono | Reme (común) | No |
| Prueba extra de su variante | Reme | No |
| Las ocho cintas | Anselmo | No |
| Copia del certificado y carta de la cinta 6 | Archivo de Quiroga | No: no se puede destruir |
| Cuentas del Consorcio con la Comisión | Esteban, si se une a ti | Sí |

Aunque vendas el archivo de Quiroga y Esteban se quede con el Consorcio, conservas los comprobantes, la prueba de Reme y las cintas: **al menos tres**.

---

## 9 · Banderas: quién las fija y quién las lee 🟡

**Estado:** ✅ el número de banderas y de medidores; 🟡 los valores y a quién lee cada decisión.

| Bandera | Tipo | Valores | La fija | La leen |
|---|---|---|---|---|
| `f-familia` | elección | todo / a medias / nada | `n-i-herencia` | `n-iv-duenas` |
| `f-pago-reme` | elección | antes / a tiempo / tarde | `n-i-reme-plazo` | `n-ii-orden` |
| `f-orden-reme` | elección | aceptar / negociar / rechazar | `n-ii-orden` | `n-ii-conflicto`, `n-ii-alianza` |
| `f-huelga` | elección | apoyar / abstenerte / romper | `n-ii-huelga` | `n-ii-alianza` |
| `f-alianza` | elección | Consorcio / Ministerio / Faroleros | `n-ii-alianza` | `n-iii-esteban-trato`, `n-iii-contrato-oficial`, `n-iii-monopolio`, `n-iii-circulo`, `n-iv-reme-proteccion` |
| `f-certificado` | elección | copia / callar / presionar | `n-ii-certificado` | `n-iii-quiroga-salida`, `n-iii-lucia-letra`, `n-iv-quiroga-archivo` |
| `f-puerta` | elección | aval / sello / presión | `n-iii-circulo` | `n-iv-esteban`, `n-iv-quiroga-archivo`, `n-iv-duenas`, `n-iv-comprador` |
| `f-monopolio` | elección | aceptar / compartir / rechazar | `n-iii-monopolio` | `n-iv-comprador` |
| `f-teo-revision` | elección | sí / no | `n-iii-revision-teo` | `n-iv-teo` |
| `f-quiroga-salida` | elección | ayudar / prometer / rechazar | `n-iii-quiroga-salida` | `n-iv-quiroga-archivo` |
| `f-reme-proteccion` | elección | proteger / saldar / dejar | `n-iv-reme-proteccion` | `n-iv-duenas` |
| `f-archivo` | elección | proteger / usar / vender | `n-iv-quiroga-archivo` | `n-iv-aetherita` |
| `f-destino` | elección | revelar / callar / vender | `n-iv-aetherita` | `n-iv-comprador`, `n-iv-lucia-publica` |
| `f-comprador` | elección | Casilda / Consorcio / Ministerio | `n-iv-comprador` | `n-iv-lucia-publica` |
| `m-union` | medidor | 0 a 100 | `n-ii-conflicto`, `n-ii-huelga`, `n-ii-alianza`, `n-iii-circulo` | `n-iii-circulo`, `n-iv-duenas`, `n-iv-aetherita` |
| `m-esteban` | medidor | 0 a 100 | `n-ii-contacto`, `n-ii-esteban-contrato`, `n-iii-esteban-trato` | `n-ii-esteban-contrato`, `n-iii-circulo`, `n-iv-esteban` |
| `m-lucia` | medidor | 0 a 100 | `n-i-lucia-rumor`, `n-ii-lucia`, `n-iii-lucia-letra` | `n-ii-lucia`, `n-iv-aetherita`, `n-iv-lucia-publica` |
| `m-teo` | medidor | 0 a 100 | `n-ii-huelga`, `n-iii-abono`, `n-iii-revision-teo` | `n-iii-revision-teo`, `n-iv-teo` |

---

## 10 · Riesgos de combinatoria 🟡

**Estado:** estimaciones del narrador.

| Riesgo | Por qué importa | Cómo se contiene |
|---|---|---|
| Demasiados caminos | 13 banderas de tres valores y una de dos son unos 3 millones de combinaciones nominales | Se prueban por **cuello de botella**, no por camino. Los recorridos principales son 81: 3 variantes por 3 alianzas por 3 puertas por 3 destinos |
| Variantes de Reme por alianza | El costo de Reme cambia con su facción y con tu alianza: 9 casos, y se muestra antes de elegir ([22](22-acto-ii-variantes.md), sección 9) | Una sola escena A6 con tres capas |
| Medidores sin tramo | Sin umbrales, `n-iv-esteban`, `n-iv-lucia-publica` y `n-iv-teo` no se pueden probar | Tres tramos por medidor (bajo, medio, alto) ✅ y caminos a cada uno en [24](24-umbrales-de-acto.md), sección 6 |
| Textos que se multiplican | Cada pequeña añade un diálogo por opción | Las pequeñas cambian una frase o un medidor, no una escena |
| Muertes que parecen injustas | Teo muere si no hubo revisión, también si aceptas su no | Avisos antes, incluido en la opción respetuosa (sección 2.4), y una sola regla que lo decide |
| Epílogos por camino | Un epílogo por cada combinación no se puede escribir | Epílogos **por piezas** que leen las banderas ⏳ F0-46 |
| Ramas que se contradicen | Una decisión del I cambia algo en el IV | Cada decisión solo lee lo fijado antes; el hub comprueba que toda bandera se fija y se lee |

---

## 11 · Criterios cumplidos

| Criterio | Cumplido | Dónde |
|---|---|---|
| Cupos exactos: 3 grandes, 6 medianas y 18 pequeñas (3/5/5/5) | Sí | `decisions.json` y sección 2.1 |
| Cada decisión dice quién la dispara, sus opciones y qué cambia en mundo, mercado y personajes | Sí | Secciones 3 a 6 |
| Cada bandera se fija y se lee al menos una vez | Sí | Sección 9 |
| Cada cuello recibe al menos dos ramas y ninguna decisión apunta a un acto anterior | Sí | Sección 2.3 |
| Acreedor del Acto II como sorteo, no bifurcación | Sí | Sección 1; corregido en 08 y 18 |
| Reparto de las cintas y dónde las dejó Anselmo | Sí, con el lugar 🟡 | Sección 7 |
| Pruebas de Reme por variante y mínimo de dos pruebas por ruta | Sí | Sección 8 |
| Cobertura de lo que el bosquejo no tocaba: monopolio de Casilda, Dueñas, Esteban en el IV y pequeñas del I | Sí | Secciones 3, 5 y 6 |
| Los 14 pendientes de F0-45 y las dos preguntas abiertas, resueltos | Sí | 08, 17, 18, 19, 21 y 22 |
| Fila de narrativa del IV: «Oyes las cintas» | Sí | `story.json` |

---

## Pendiente

- ⏳ F0-46 Epílogos por piezas: leen `f-destino`, `f-comprador`, `f-alianza`, `f-reme-proteccion`, `f-archivo` y los medidores.
- ✅ Umbrales de los medidores y de cada acto: resueltos en [24](24-umbrales-de-acto.md). El evaluador ⏳ F4-127
- ⏳ F4-61 Cifras y efectos de los medidores por facción.
- ⏳ F4-150 El reproductor y el sistema de cintas.
- ⏳ F4-147 La curva del desplome de la Aetherita dentro del tope diario.
- ⏳ F0-52 Cifras de precios, cuotas, gastos y vigilancia.
- ⏳ F4-135 Guion del Acto III, con el médico del dispensario.
- ⏳ F0-75 Dibujo del árbol con conexiones (SVG) en el hub; la vista actual usa columnas, tarjetas y flechas de texto.
