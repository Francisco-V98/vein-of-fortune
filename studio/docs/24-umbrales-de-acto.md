# 24 · Umbrales de acto

> ⚠️ **Contiene spoilers de toda la historia** (el destino de Teo, las cintas, el Acto IV). Es material para quien escribe, programa o equilibra la progresión; no es para el jugador.

Qué hace falta para pasar de un acto al siguiente, y cómo se cumple de varias maneras sin obligarte a seguir la trama. Parte de [08](08-historia-y-personaje.md), [17](17-mapa-de-historia.md), [22](22-acto-ii-variantes.md) y [23](23-arbol-de-decisiones.md). Los tramos de los medidores también viven en `studio/data/decisions.json` (`meta.tramos`).

**Cómo leer las marcas.** La palomita verde es lo que decidió el autor (2026-10-12, F0-47, en dos rondas: el modelo y, después, los ajustes, las preguntas de la sección «Decisiones tomadas» y las secciones 5 y 6.4). El círculo amarillo es propuesta del narrador; si no la lleva una tarea, es menor y no condiciona finales ni guiones. El reloj de arena lleva el ID de la tarea existente de la que depende. Un título lleva la palomita solo si todo lo que tiene debajo está confirmado; si mezcla, lleva el círculo y una nota «Estado».

## Resumen en cinco líneas

1. Cada acto tiene **una puerta** con tres capas: un **hito de historia**, un **piso de estatus** (solo en A5 y en el círculo del III) y **vías «k de n»** (dos de tres entre deuda, logros y relación).
2. Los cuatro medidores (Unión, Esteban, Lucía y Teo) tienen **tres tramos**: bajo (menos de 35), medio (35 a 54) y alto (55 o más).
3. Las escenas ancla **se disparan por eventos tuyos**, no por calendario, y van encadenadas: cada una espera a la anterior.
4. Nada atasca la partida: el juego sigue como **sandbox**, la historia espera en una **cola**, un **diario** lista lo que falta y una **misión de rescate** llega tras mucho tiempo sin avanzar. **La deuda nunca bloquea.**
5. Para entrar al **IV** hacen falta el encuentro con Dueñas y las **cintas 1 a 5**.

---

## 1 · Decisiones del autor ✅

Decisiones del 2026-10-12 (F0-47), tomadas después de comparar tres modelos (puerta por acto con vías, puntuación acumulada y umbrales por escena).

| Tema | Decisión |
|---|---|
| Modelo | **Una puerta por acto** con vías «k de n» (dos de tres entre deuda, logros y relación). **Piso de estatus solo en dos puertas**: A5 del Acto II (Comerciante) y el círculo del Acto III (Empresario). Las anclas A1 a A6 van **encadenadas**: cada una se dispara con la anterior resuelta ✅ |
| Acto I | Se cierra al **reabrir el puesto, atender la primera cuota** (pagada o prorrogada) y tener el **primer contacto con los empleados**. «Minero con licencia» es el **premio** del cierre, no un requisito ✅ |
| Tramos | Para los cuatro medidores: **bajo menos de 35, medio 35 a 54, alto 55 o más**. Arrancan en 50; Esteban en 40 y Teo en 60 ✅ |
| Tramo medio | Teo **se queda** (si lo llevaste a revisión). Lucía **no publica**, así que lo publicas tú con costo alto y poco alcance. El **reproductor** lo entrega Lucía solo en tramo alto; con medio o bajo lo entrega Reme ✅ |
| Aval de Esteban | Basta su medidor en tramo alto. Si no lo tienes, el aval se muestra **bloqueado con el motivo**, y siempre quedan el sello de Dueñas y la presión de tu alianza ✅ |
| Vía de relación | Se cumple si **al menos uno de los cuatro medidores** está en tramo alto ✅ |
| Vía de deuda | Cuenta **solo lo que pagas tú** (% de capital pagado de tu bolsillo). Lo que asume el Consorcio no regala la vía ✅. La deuda de luz de los Faroleros no la rompe 🟡 |
| Cintas | Las cintas **1 a 5 son obligatorias** para entrar al IV, no caducan por tiempo ni por decisiones, y tienen una **misión persistente** si faltan ✅ |
| Red anti-atasco | El juego sigue como sandbox, **la historia espera en cola**, **el diario lista las vías que faltan** y **la misión de rescate** llega tras mucho tiempo sin avanzar. La deuda nunca bloquea. Las tres piezas se diseñan aparte ✅ ⏳ F0-78 |
| Teo | **Sin revisión muere**, también si le propones y aceptas su no: la opción respetuosa tiene costo ✅ |
| Magnate y cierre del IV | Magnate se concede al **cerrar el acta de calibración** y **no es puerta**. El IV cierra con el acta tras la decisión sobre la Aetherita; entonces empieza el sandbox ✅ |
| Disparadores | Van **por eventos del jugador y no por calendario**: A2 tras atender tu primera cuota después de A1; A3 tras tu primera venta o expedición en la zona; A4 tras el aviso de noticias y una acción tuya, sin plazo en días. Las opcionales O1 a O4 **no puntúan** para ninguna puerta ✅ |
| Círculo y entrada al IV | El círculo pide **Empresario + dos vías de tres + una puerta abierta** y cierra en el encuentro con Dueñas. El IV entra con ese encuentro resuelto y las cintas 1 a 5 recogidas. Dueñas **no tiene medidor**. Ninguna puerta lee `f-pago-reme` ni `f-orden-reme`, Reme nunca cierra puertas y ninguna facción es mejor por defecto ✅. `n-ii-alianza` lee `f-orden-reme` solo para mostrar el costo de Reme, sin usarlo para decidir 🟡 |

---

## 2 · Cómo funciona una puerta ✅

| Capa | Qué exige | Dónde se aplica |
|---|---|---|
| **Hito de historia** | La escena o el evento que cierra el acto. Siempre se exige ✅ | Las cuatro puertas ✅ |
| **Piso de estatus** | Un escalón mínimo de la escalera de [07](07-sociedad-y-eventos.md) ✅ | Solo A5 (Comerciante) y el círculo del III (Empresario) ✅ |
| **Vías «k de n»** | Cumplir **dos de tres**: deuda, logros o relación ✅ | A5 y el círculo del III. El Acto I y la entrada al IV no tienen vías ✅ |

- Ninguna vía es obligatoria por sí sola: basta cualquier par de las tres ✅.
- Las opcionales O1 a O4 pueden mover un medidor, pero **ninguna puerta las necesita** ✅ (se comprueba en la sección 6).
- Ninguna puerta lee `f-pago-reme` ni `f-orden-reme`: cómo trates a Reme no abre ni cierra nada ✅. El nodo `n-ii-alianza` lee `f-orden-reme` solo para mostrar el costo de Reme; ninguna puerta lo usa para decidir 🟡.
- Dueñas no tiene medidor; la Unión sí, y cuenta como cualquiera de los cuatro ✅.

---

## 3 · Las puertas, acto por acto ✅

| Puerta | Hito (siempre) | Piso de estatus | Vías | Qué bloquea | Qué no bloquea |
|---|---|---|---|---|---|
| **I → II** | Reabres el puesto, atiendes tu primera cuota (pagada o prorrogada) y tienes el primer contacto con los empleados ✅ | Ninguno. «Minero con licencia» es el premio ✅ | Ninguna ✅ | El paso al II y la escena A1 ✅ | La deuda total, los logros, las cintas y el estatus ✅ |
| **II → III** (A5) | A4 resuelta: viviste la huelga y el apagón ✅ | **Comerciante** ✅ | Dos de tres ✅ | La escena A5 y, con ella, el cierre del II ✅ | A1 a A4 (solo piden la anterior), Reme y las opcionales ✅ |
| **III · el círculo** | Una puerta abierta; el círculo cierra en el encuentro con Dueñas ✅ | **Empresario** ✅ | Dos de tres ✅ | El círculo y el encuentro con Dueñas ✅ | Un aval bloqueado: quedan el sello y la presión de tu alianza ✅ |
| **III → IV** (entrada) | Encuentro con Dueñas resuelto ✅ | Ninguno ✅ | Ninguna ✅ | La entrada al IV, hasta tener las cintas 1 a 5 ✅ | Cualquier medidor, la deuda y la alianza elegida ✅ |
| **IV → sandbox** | Cerrar el acta de calibración, tras la decisión sobre la Aetherita ✅ | Ninguno. Magnate es el premio, no una puerta ✅ | Ninguna ✅ | Nada: el sandbox empieza al cerrar el acta ✅ | — |

---

## 4 · Las tres vías 🟡

**Estado:** ✅ cómo se mide cada vía, qué no cuenta (incluidos los abonos anónimos) y que la relación nace cumplida; 🟡 las cifras de deuda (25 % y 50 %) y de logros (4 y 10), **aplazadas a propósito**: nada anterior depende de ellas, porque las puertas se leen en A5 y en el círculo, y las calibra la economía ⏳ F0-52 (deuda) y ⏳ F4-116 (logros). Si cambian, no hay que rehacer ninguna escena ni regla. ⏳ F4-127 el evaluador.

| Vía | Cómo se mide ✅ | Acto II (A5) | Acto III (círculo) | Qué no cuenta ✅ |
|---|---|---|---|---|
| **Deuda** | % del capital que pagaste **de tu bolsillo** ✅ | 25 % 🟡 ⏳ F0-52 | 50 % 🟡 ⏳ F0-52 | Lo que asume el Consorcio ✅; los abonos anónimos de Reme ✅; la deuda de luz de los Faroleros no la rompe 🟡 |
| **Logros** | Número de logros del sistema ✅ | 4 🟡 ⏳ F4-116 | 10 🟡 ⏳ F4-116 | Ninguno es obligatorio: sirve cualquiera 🟡 ⏳ F4-115 |
| **Relación** | Al menos un medidor en tramo alto ✅ | Igual ✅ | Igual ✅ | Reme y Dueñas no tienen medidor ✅ |

**Teo arranca en 60 (tramo alto) y la vía de relación nace cumplida** ✅. Es lo buscado: la relación es la vía más fácil, y la deuda y los logros son las que piden esfuerzo. Solo la pierdes si rompes la huelga de Teo y no cuidas a otro medidor.

- **El capital es el de la herencia.** 🟡 El porcentaje se mide sobre el capital original de la deuda de Reme ⏳ F0-52. La deuda de luz de los Faroleros es aparte: no entra en el numerador ni en el denominador 🟡.
- **Los abonos anónimos de Reme no cuentan como pagados por ti** ✅, para no regalar la vía. Su suma total debe dejar el umbral alcanzable ⏳ F0-52.
- **Los logros.** Cuántos hacen falta es la cifra de arriba; cuáles son lo decide el sistema ⏳ F4-115 y los primeros 30 ⏳ F4-116. 🟡 Restricción para esa tarea: los 30 primeros deben incluir al menos 4 que se puedan lograr antes de A5 sin tocar la historia ⏳ F4-116.
- **La deuda nunca bloquea** ✅. Ninguna puerta exige tenerla saldada y ninguna puerta depende solo de ella.
- **Siempre hay salida.** 🟡 Deuda y logros se logran jugando, sin importar tus decisiones. Por eso «dos de tres» es siempre alcanzable, aunque pierdas la relación. Lo comprueban ⏳ F0-52 y ⏳ F4-116 al fijar sus cifras.
- **Cuándo se evalúa.** Lo decide el evaluador ⏳ F4-127. Debe revisar las puertas al ocurrir un evento que mueve una vía (pagar una cuota, ganar un logro, mover un medidor, subir de estatus).

---

## 5 · Los tramos de los medidores y lo que desbloquean 🟡

**Estado:** ✅ los tramos, los arranques y lo que desbloquea cada tramo de Esteban (en `n-iv-esteban`), Lucía, Teo y la Unión (en `n-iv-duenas` y `n-iv-aetherita`); ✅ el castigo de que Dueñas solo pueda «borrarte» con la Unión alta; 🟡 tres reglas de lectura menores. Los movimientos de cada decisión ⏳ F4-61

| Tramo | Valor ✅ | Quién arranca aquí ✅ |
|---|---|---|
| **Bajo** | 0 a 34 | — |
| **Medio** | 35 a 54 | Unión (50), Lucía (50) y Esteban (40) |
| **Alto** | 55 a 100 | Teo (60) |

Los tramos están en `meta.tramos` de `decisions.json`. La pantalla muestra el tramo y su motivo, no la cifra 🟡 ⏳ F4-61.

| Medidor | Alto | Medio | Bajo |
|---|---|---|---|
| **Esteban** | Aval abierto ✅. En `n-iv-esteban` rompe con el Consorcio y te da el libro ✅ | Aval bloqueado, con el motivo ✅. En `n-iv-esteban` se aparta ✅ | Aval bloqueado ✅. En `n-iv-esteban` defiende al Consorcio ✅ |
| **Lucía** | Publica contigo ✅ y te da el reproductor ✅ | No publica, publicas tú con costo alto y poco alcance ✅. El reproductor lo entrega Reme ✅ | Publica en La Voz del Hollín sin ti ✅. El reproductor lo entrega Reme ✅ |
| **Teo** | Si hubo revisión, se queda ✅ | Si hubo revisión, se queda ✅ | Si hubo revisión, se va ✅ |
| **Unión** | Cuenta para la vía de relación ✅. En `n-iv-duenas`, Dueñas intenta borrarte ✅. En `n-iv-aetherita`, la Unión sale contigo si revelas ✅ | No cuenta para la vía de relación ✅. Sin efecto propio en el IV ✅ | En `n-iv-aetherita`, nadie te respalda en el Hollín si revelas ✅ |

- **Teo sin revisión muere, sea cual sea su tramo** ✅. Si el medidor y la revisión chocan, gana el no haberlo atendido ✅. Esto incluye la opción respetuosa «se lo propones y aceptas su no» ✅.
- **Esteban.** El aval se lee en el momento de elegir puerta ✅. 🟡 Como `n-iii-esteban-trato` ocurre antes, el medidor ya trae lo que hiciste en la bolsa. Después de la puerta, el medidor de Esteban no se mueve, así que el tramo del IV es el de la puerta ⏳ F4-61.
- **Lucía.** 🟡 Antes de decidir sobre la Aetherita se te muestra quién publicaría, para elegir con aviso ⏳ F4-142. `n-iv-lucia-publica` se activa si la verdad sale.
- **Unión.** En `n-iv-duenas`, «borrarte» pide Unión alta y al menos dos pruebas ✅. Como siempre conservas al menos tres ([23](23-arbol-de-decisiones.md), sección 8), en la práctica solo importa la Unión: es el castigo de quien tiene gente detrás ✅. Con Unión media o baja, Dueñas decide por la puerta que usaste, igual que hoy ✅.
- **Dueñas** no tiene tramos ✅.

---

## 6 · Cómo alcanza cada medidor cada tramo 🟡

**Estado:** ✅ los ajustes A a D y que romper la huelga baja mucho a Teo y a la Unión (sección 6.4, decisión del autor); 🟡 las tablas 6.1 a 6.3, que son cuentas del narrador con los tamaños de 23 (poco ≈ 5, normal ≈ 10, mucho ≈ 20). Las cifras finales ⏳ F4-61, que debe **conservar los caminos de esta sección**.

### 6.1 · Qué mueve a cada medidor 🟡

| Medidor | Arranque | Qué lo sube | Qué lo baja |
|---|---|---|---|
| **Esteban** | 40 | Aceptar su cita, solo con el Consorcio (+5). Apoyarlo en la compra grande (+20 con el ajuste A). Aceptar con un límite claro (+5) | Rechazar la cita, solo con el Consorcio (−5). Comprar antes que él (−10) |
| **Lucía** | 50 | Contarle el rumor entero (+10). Contarle lo del certificado (+10) | No contarle nada (−5). Decirle que no sabes nada del certificado (−20 con el ajuste B) |
| **Teo** | 60 | Apoyar la huelga (+10). Creerle sobre el abono (+10). Llevarlo a revisión (+5) | Romper la huelga (−20). Dudar de él (−20 con el ajuste C). No sacar el tema de la tos (−10) |
| **Unión** | 50 | Apoyar la huelga (+10). Plantarte en el primer conflicto (+5) | Romper la huelga (−20). Ceder en el conflicto (−5). Aliarte con el Consorcio o el Ministerio (−10). Entrar por la presión de ese aliado (−10, ajuste D) |

### 6.2 · Caminos mínimos, sin ninguna opcional 🟡

| Medidor | Alto (55 o más) | Medio (35 a 54) | Bajo (menos de 35) |
|---|---|---|---|
| **Esteban** | Apoyarlo en la compra grande: 1 decisión (60) | El arranque (40) | Comprar antes que él. Con el Consorcio y la cita aceptada da 35 (40 + 5 − 10), que es tramo medio; hay que rechazar o posponer la cita y comprar antes: 2 decisiones (25 o 30). Con el Ministerio o los Faroleros, 1 decisión (30) |
| **Lucía** | Contarle el rumor entero: 1 decisión (60), sin negarle después lo del certificado | El arranque (50) | Decirle que no sabes nada del certificado, sin haberle contado el rumor entero: 1 decisión (30) |
| **Teo** | El arranque (60). Apoyar la huelga lo sube a 70 | Romper la huelga o dudar de él, con revisión (45) | Romper la huelga y dudar de él, con revisión: 2 decisiones (25) |
| **Unión** | Con los Faroleros, apoyar la huelga: 1 decisión (60). Con el Consorcio o el Ministerio, apoyar y plantarte: 2 (55) | El arranque (50) | Romper la huelga: 1 decisión (30) |

### 6.3 · La prueba del aval, sin O2, en las tres variantes 🟡

O2 («Esteban gana un contrato») es opcional y no puede ser la llave del aval. Se parte de 40 y se cuenta solo lo que ocurre sin O2.

| Variante | Hoy: lo mejor sin O2 | Con el ajuste A: apoyarlo en la compra grande |
|---|---|---|
| Consorcio | 40 + 5 (cita) + 10 (apoyo normal) = 55. Alto, pero con dos decisiones exactas | 65 si aceptaste la cita, 60 si la pospusiste y 55 si la rechazaste. Alto con una decisión |
| Ministerio | 40 + 10 = 50. **Medio: no alcanza** | 60. Alto con una decisión |
| Faroleros | 40 + 10 = 50. **Medio: no alcanza** | 60. Alto con una decisión |

Sin ajuste, el aval solo se abre en la variante del Consorcio y con dos decisiones exactas. Con el ajuste A se abre en las tres.

### 6.4 · Ajustes de efectos ✅

Aceptados por el autor (2026-10-12). Son cambios pequeños, separados del resto. Ninguno toca un cupo.

| Ajuste | Nodo y opción | Antes | Queda | Por qué |
|---|---|---|---|---|
| **A** | `n-iii-esteban-trato` · «Lo apoyas en una compra grande» | Esteban «confía en ti» (≈ 10) | Esteban «confía mucho en ti» (≈ 20) ✅ | Abre el aval en las tres variantes con una decisión |
| **B** | `n-iii-lucia-letra` · «Dices que no sabes nada» | Lucía «confía menos» (≈ 10) | Lucía «no te cree» (≈ 20) ✅ | Sin O1, el tramo bajo de Lucía era inalcanzable (el mínimo era 35) |
| **C** | `n-iii-abono` · «Dudas de Teo» | Teo «le duele» (≈ 10) | Teo «le duele mucho» (≈ 20) ✅ | Sin esto, «se va» era inalcanzable con revisión (el mínimo era 35) |
| **D** | `n-iii-circulo` · «presión de tu alianza» | El texto dice que la Unión baja, pero la decisión no lo fija | `n-iii-circulo` fija `m-union` en esa opción ✅ | El efecto ya estaba escrito; ahora el dato lo registra |

Además, romper la huelga baja a Teo y a la Unión «mucho» (≈ 20) ✅. En 23 solo decía «se alejan». Es lo que permite que el tramo bajo exista en el II.

---

## 7 · Las tres alianzas y las vías 🟡

**Estado:** ✅ ninguna facción es mejor por defecto y lo que asume el Consorcio no cuenta como pagado por ti; 🟡 que la deuda de luz no rompa la vía y lo que hace cada alianza con cada vía. Los efectos de cada alianza ⏳ F4-133; el autor no revisó esta sección.

| Alianza | Deuda | Logros | Relación | Vías abiertas |
|---|---|---|---|---|
| **Consorcio Arvel** | Compra tu deuda y cambia el acreedor, no el capital 🟡. Si asumiera una parte, esa parte no cuenta ✅. Sigue abierta | Abierta 🟡 | La Unión baja ✅ (≈ 10 ⏳ F4-61). Quedan Lucía, Teo y Esteban | Las tres. Sin deuda, quedan logros + relación |
| **Ministerio** | Su oferta no toca tu deuda 🟡. Abierta | Abierta 🟡 | La Unión baja ✅ (≈ 10 ⏳ F4-61). Quedan Lucía, Teo y Esteban | Las tres |
| **Los Faroleros** | La deuda de luz se suma aparte y no rompe la vía 🟡. Abierta | Abierta 🟡 | La Unión se mantiene ✅ | Las tres |

- **Peor caso.** 🟡 ⏳ F4-133 Aunque el Consorcio dejara tu deuda cerrada para la vía, quedan logros y relación. La relación sigue abierta porque Lucía, Teo y Esteban no dependen de tu alianza (sección 6.2).
- Ninguna alianza cierra el círculo 🟡. Ninguna deja menos de dos vías alcanzables 🟡 ⏳ F4-133.

---

## 8 · Los disparadores de A1 a A6 🟡

**Estado:** ✅ el encadenado y los eventos de A2, A3 y A4; 🟡 el resto del detalle, que son ajustes menores que se cierran en el guion del Acto II ⏳ F4-128. Todo es **por eventos tuyos**, sin plazos en días. Si el evento no llega, la escena **espera en la cola** y el juego sigue ✅.

| Escena | Se dispara cuando… | Detalle |
|---|---|---|
| **A1** · La política manda | Cierras el Acto I ✅ | 🟡 El decreto de A1 es lo que abre las zonas del II; no es una condición previa ⏳ F4-128 |
| **A2** · La orden de Reme | A1 resuelta y atiendes tu primera cuota después de A1 ✅ | Pagada o prorrogada. Si ya saldaste la deuda, A2 llega en tu siguiente visita a Reme 🟡 ⏳ F0-52. El periodo de la cuota ⏳ F0-52 |
| **A3** · El primer conflicto | A2 resuelta y tu primera venta o expedición en la zona de tu variante ✅ | 🟡 Zona: Sierra Alta (Consorcio), Villa Brasa (Ministerio) y Salares (Faroleros), como en [22](22-acto-ii-variantes.md) ⏳ F4-128 |
| **A4** · La primera huelga | A3 resuelta, el aviso en las noticias y una acción tuya ✅, sin plazo en días ✅ | 🟡 «Acción tuya»: tu siguiente bloque de expedición, venta, taller o cierre del puesto. Cuántas acciones separan el aviso del cierre ⏳ F4-132 |
| **A5** · Las tres ofertas | A4 resuelta, estatus de Comerciante y dos vías de tres ✅ | Cierra el Acto II ✅. El estatus y sus cifras ⏳ F4-109 |
| **A6** · El cierre de Reme | A5 resuelta ✅ | Es la última pantalla del II, no una condición para el III ✅ |

- **Opcionales O1 a O4.** Se disparan también por evento (comprar tres rumores, perder un contrato, una visita nocturna, la primera visita a Quiroga) y **no puntúan** para ninguna puerta ✅.
- **Sin calendario.** 🟡 «Tardar» en un contrato (O2) se mide por el vencimiento del contrato, no por días de la historia ⏳ F4-128.

---

## 9 · Las cintas 1 a 5 y la entrada al IV 🟡

**Estado:** ✅ las cintas 1 a 5 son obligatorias, no caducan y tienen misión persistente; 🟡 el estado intermedio, el orden y La Fosa, que se cierran al escribir el IV ⏳ F4-142. El contenido de la misión ⏳ F4-150

| Cinta | Se recoge en el acto ✅ | Dónde ([23](23-arbol-de-decisiones.md), sección 7) |
|---|---|---|
| 1 | I | Puesto de Villa Brasa |
| 2 | II | Minas de Sierra Alta |
| 3 a 5 | III | Puerto Meridiano y Cavernas de Cristal |

- **Entrada al IV** ✅: encuentro con Dueñas resuelto y cintas 1 a 5 recogidas.
- **No caducan** ✅ por tiempo ni por decisiones. Ninguna decisión puede cerrar el camino a una cinta ✅.
- **Misión persistente** ✅: si falta una, queda en el diario con su lugar hasta que la recojas. No bloquea los actos anteriores.
- **Estado intermedio.** 🟡 El orden entre el encuentro con Dueñas y las cintas es libre. Si tienes el encuentro y faltan cintas, el III está cerrado y el IV espera en la cola, mientras sigues en sandbox.
- **Las cintas 6 a 8** esperan en La Fosa y se recogen dentro del IV ✅. 🟡 Dueñas no puede cerrarte La Fosa antes de que las recojas ⏳ F4-142.

---

## 10 · La red anti-atasco 🟡

**Estado:** ✅ qué piezas existen y qué hacen; ⏳ F0-78 su diseño. La deuda nunca bloquea ✅.

| Pieza | Qué hace ✅ | Diseño |
|---|---|---|
| **Sandbox** | Si no cumples una puerta, el juego sigue: minas, vendes, exploras y comercias | Ya existe como modo de juego |
| **Cola de historia** | La escena que no se puede disparar espera; no se pierde ni caduca | ⏳ F0-78 |
| **Diario** | Lista las vías que faltan para pasar de acto, con lo que ya cumples | ⏳ F0-78 |
| **Misión de rescate** | Llega tras mucho tiempo sin avanzar | ⏳ F0-78. Cuánto tiempo, en horas de juego ⏳ F0-53 |

- 🟡 **Restricciones para las tareas que lo diseñan.**
  - Misión de rescate (F0-78): señala qué falta y cómo; no concede estatus, logros ni medidores.
  - Estatus ⏳ F4-109: subir a Comerciante o a Empresario no puede exigir una escena de historia ni una puerta, para no crear un ciclo. Una vez cumplido el piso de una puerta, no se pierde por una pérdida de dinero.
  - Mora ⏳ F0-52: qué pasa si no pagas lo define la economía, y nunca puede cerrar una puerta.

---

## 11 · Casos «no cumples nada» 🟡

**Estado:** propuesta, con la salida ✅ en cada caso; los textos del diario se escriben en ⏳ F0-78. Todos terminan igual: el juego sigue y la historia espera.

| Te falta… | Qué pasa | Qué ves en el diario |
|---|---|---|
| Reabrir el puesto, atender la primera cuota o el contacto con los empleados | El Acto I no cierra; A1 espera ✅ | Las tres condiciones del I, con las que ya cumples. El contacto con los empleados está guionado ⏳ F0-23 |
| Atender una cuota (A2) | A2 espera en la cola ✅ | «Reme te espera para la cuota» ⏳ F0-78 |
| Tu primera venta o expedición en la zona de tu variante (A3) | A3 espera ✅ | La zona donde vender ⏳ F0-78 |
| Una acción tuya tras el aviso (A4) | La huelga espera ✅ | Nada que hacer: sigue tu juego ⏳ F0-78 |
| El estatus de Comerciante (A5) | A5 espera ✅ | El estatus que falta ⏳ F4-109 |
| Dos vías de tres (A5 o el círculo) | La escena espera ✅ | Las tres vías, con la que cumples y lo que falta ⏳ F0-78 |
| El aval de Esteban | El aval se ve bloqueado con el motivo; eliges sello o presión ✅ | El motivo: su tramo ⏳ F0-78 |
| Las cintas 1 a 5 | El IV espera ✅ | La misión de cada cinta que falta ✅ |
| **Nada de lo anterior** | Sigues en sandbox; nada se pierde ✅ | Todo lo que falta, y tras mucho tiempo llega la misión de rescate ✅ ⏳ F0-78 |

---

## 12 · Qué cambia en otros documentos

| Documento | Cambio | Marca |
|---|---|---|
| [22](22-acto-ii-variantes.md) | Los disparadores de A1 a A6 pasan a eventos; la regla de obligatoriedad queda cerrada; se resuelven los siete aplazamientos de esta tarea | ✅ |
| [23](23-arbol-de-decisiones.md) | Tramos, destino de Teo, quién publica y el aval; ajustes A a D | ✅ las decisiones del autor y los ajustes A a D |
| [17](17-mapa-de-historia.md) | Enlace a este documento y regla de la puerta del Acto I | ✅ |
| `decisions.json` | `meta.tramos`, textos de los nodos y de las banderas, y la bandera `m-union` en `n-iii-circulo` | ✅ tramos y la bandera `m-union` |

---

## Decisiones tomadas ✅

Respuestas del autor (2026-10-12, F0-47) a las preguntas que dejó el narrador.

| # | Pregunta | Respuesta del autor |
|---|---|---|
| 1 | ¿Aceptas los ajustes A a D de la sección 6.4? | Sí, los cuatro ✅. Además, romper la huelga baja a Teo y a la Unión «mucho» (≈ 20) ✅ |
| 2 | Teo arranca en 60 (tramo alto), así que la vía de relación nace cumplida | Aceptado ✅: la relación es la vía más fácil; la deuda y los logros piden esfuerzo |
| 3 | ¿Qué hace cada tramo de Esteban en `n-iv-esteban` y de la Unión en `n-iv-duenas` y `n-iv-aetherita`? | Lo que dice la sección 5 ✅ |
| 4 | Como siempre conservas tres pruebas, «borrarte» depende solo de la Unión alta | Confirmado ✅: es el castigo de quien tiene gente detrás |
| 5 | ¿Los abonos anónimos cuentan como pagados por ti? | No ✅, para no regalar la vía |

## Decisiones aplazadas 🟡

**Estado:** el autor aceptó dejar estas cifras como propuesta y calibrarlas con la economía. Se aplazan con una tarea porque nada que se escriba antes depende de ellas: ninguna escena, texto ni regla cambia si el 25 % pasa a 30 %.

| # | Qué falta | Propuesta del narrador | Tarea |
|---|---|---|---|
| 1 | Umbral de la vía de deuda en A5 y en el círculo | 25 % y 50 % | ⏳ F0-52 |
| 2 | Umbral de la vía de logros en A5 y en el círculo | 4 y 10 | ⏳ F4-116 |

---

## Pendiente

- ⏳ F0-78 Diseño del diario, la cola de historia y la misión de rescate.
- ⏳ F0-53 «Mucho tiempo sin avanzar», en horas de juego.
- ⏳ F4-109 Escalera de estatus: requisitos de Comerciante y de Empresario, y su patrimonio ⏳ F0-52
- ⏳ F0-52 Periodo de la cuota, mora, suma de los abonos anónimos y umbral de deuda (25 % y 50 % propuestos).
- ⏳ F4-132 Aviso previo de la huelga (cuántas acciones lo separan del cierre).
- ⏳ F4-61 Cifras de los medidores (deltas), conservando los caminos de la sección 6.
- ⏳ F4-115 Sistema de logros y ⏳ F4-116 los primeros 30 y el umbral de logros (4 y 10 propuestos).
- ⏳ F4-127 Evaluador de las puertas.
- ⏳ F4-150 Misión persistente de las cintas.
- ⏳ F0-23 Escena del primer contacto con los empleados, en el guion del Acto I.

---

## Criterios cumplidos

| Criterio de la tarea | Cumplido | Dónde |
|---|---|---|
| Umbrales definidos para los cuatro actos | Sí | Secciones 3 y 8 |
| Se pueden cumplir de varias maneras | Sí: dos de tres vías y una puerta siempre abierta | Secciones 2, 4 y 7 |
| No obligan a seguir la trama al pie de la letra | Sí: eventos tuyos, sandbox y cola | Secciones 8 a 10 |
| Medidores con tramos y lo que desbloquean | Sí | Secciones 5 y 6 |
| Acordados con el autor | Sí: todas las preguntas respondidas; solo quedan aplazadas las cifras de deuda y de logros | Sección 1 y «Decisiones tomadas» |
