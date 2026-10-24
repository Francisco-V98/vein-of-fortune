# 29 · Calendario y temporadas

Cómo se ve y se juega el paso del año en Veta de Fortuna: estaciones y clima del día, la ficha única del calendario, los festivos y las mini-historias de temporada. Nace de la tarea F0-94 y de las decisiones del autor del 2026-10-24. El calendario base (año de 112 días, cuatro estaciones de 28) está en [28](28-numeros-base-de-la-economia.md) §1.2; la historia principal **no** depende de este documento ([24](24-umbrales-de-acto.md), [27](27-guion-del-acto-i.md)).

**Estado.** ✅ El alcance, la ficha, las reglas y el molde de las mini-historias son decisión del autor. ✅ Los 8 festivos y el catálogo de 12 mini-historias (títulos, ganchos, misiones y variantes) los aprobó el autor el 2026-10-24. ⏳ F0-92 y ⏳ F0-93: las cifras de efecto de la sección 2 viven en claves nuevas de `world.json` que el simulador **todavía no lee**; la huella del simulador no cambia con este documento.

---

## 1 · Calendario de partida ✅

El año tiene 112 días: primavera, verano, otoño e invierno, 28 días cada una (4 semanas). El día 1 de la partida es el **22 de otoño**, así que el invierno empieza el día 8 (primer día del Acto II). Fechas de ejemplo: día 14 = 7 de invierno; día 36 = 1 de primavera; día 113 = 22 de otoño del segundo año.

| Estación | Días de partida (año 1) | Idea |
|---|---|---|
| Otoño | 92–112 (y 1–7 del arranque) | Ahorro y aviso del frío |
| Invierno | 8–35 | Cuesta más moverse |
| Primavera | 36–63 | Las minas se recuperan |
| Verano | 64–91 | Se gastan las herramientas |

## 2 · Estación y clima: visual y jugable ligero ✅

**Alcance.** Cambia la paleta y el aspecto del mapa, los asentamientos y las minas (nieve, lluvia, niebla), con efectos suaves. Es un tinte u overlay de paleta, no hojas de arte nuevas (⏳ F4-217, ⏳ F4-165). Un sistema completo de clima queda para V2 o un DLC (sección 7).

### 2.1 Efecto de la estación ✅ (cifras de partida, ⏳ F0-92 y ⏳ F0-93)

| Estación | Efecto | Nota |
|---|---|---|
| Invierno | Aguante −2 (de 28 a 26) | Cuidado con contar dos veces el frío y el carbón +12 de la tabla de estacionalidad: se anota en [28](28-numeros-base-de-la-economia.md) |
| Primavera | Riqueza de mina +4 al día en vez de +3 | |
| Verano | Desgaste de herramienta +10 % | |
| Otoño | −1 mena visible | |

### 2.2 Clima del día por zona ✅ (cifras de partida, ⏳ F0-92 y ⏳ F0-93)

| Clima | Efecto |
|---|---|
| Despejado | Ninguno |
| Lluvia | Si es fuerte, cierra **1 entrada** de mina por un día; se avisa la víspera; máximo 2 por estación y zona; severidad suave; reutiliza ⏳ F4-250 |
| Nieve | −1 carga de detector (la nieve choca con la regla J3; la mide ⏳ F0-92) |
| Niebla | −1 mena visible |

Reglas ✅: **nunca hay clima con efecto en el Acto I** (días 1–7). Un cierre por lluvia pausa el plazo de cualquier mini-historia en curso. El clima solo sale en el calendario como ficha de tipo «clima» cuando es un cierre anunciado.

## 3 · Pantalla y ficha única ✅

### 3.1 Dónde se ve

- **Barra superior**, siempre visible: «Día 14 · 7 de invierno · nieve». Un punto junto a la fecha avisa si hay una ficha hoy; el clic abre el calendario.
- **Calendario**: pestaña del diario (⏳ F3-48), en forma de **lista, mes a mes**. Solo muestra fichas con efecto o que puedas elegir; incluye las que **podrían ocurrir**. Al pulsar una se abre su detalle.
- **Tablón del pueblo**: en cada asentamiento, es el calendario filtrado por zona. El «tablón de pedidos» del puesto ([27](27-guion-del-acto-i.md)) se unifica con él: un pedido es un tipo de ficha.
- Una mini-historia aceptada pasa al diario, apartado «En curso».

### 3.2 La ficha (8 campos, igual para todos los tipos) ✅

| Campo | Valores |
|---|---|
| Tipo | festivo · mercado · social · político · clima · propuesta · pedido |
| Fecha o ventana | «7 de invierno» o «del 3 al 17 de primavera» |
| Zona | Villa Brasa, Altafría, Salinas Blancas, Puerto Meridiano… o «Todo el mapa» |
| Efecto | Lo que cambia mientras dura (mercado, entrada, Aguante…) |
| Recompensa | Lo que ganas |
| Riesgo | Lo que puedes perder, dicho claro |
| Estado | posible → anunciado → en curso → cerrado |
| Certeza | rumor · probable · confirmado |

Los campos vacíos se escriben «—». Ejemplo de ficha:

> **Feria del Primer Hollín** · festivo · 9 de otoño · Villa Brasa · Hierro +2 puntos en el mercado · Recompensa: —  · Riesgo: — · Estado: anunciado · Certeza: confirmado.

## 4 · Festivos y fechas fijas ✅

Entre 1 y 2 por estación (8 al año en este catálogo). Efecto pequeño: **mercado ±2 puntos como tope** (igual que un evento menor del documento 28), más una escena breve o una decoración. Se repiten todos los años en la misma fecha. Nunca bloquean nada ni se pierden por no ir.

| Estación | Festivo ✅ | Fecha | Zona | Efecto de mercado | Escena o decoración |
|---|---|---|---|---|---|
| Otoño | Feria del Primer Hollín | 9 de otoño | Villa Brasa | Hierro +2 | Puestos con faroles en la plaza |
| Otoño | Noche de las Calderas | 18 de otoño | Villa Brasa | Carbón +1 | Calderas encendidas en la calle; escena breve con la Unión |
| Invierno | Día del Brasero | 6 de invierno | Altafría | Carbón +2 | Braseros en la plaza y chocolate caliente |
| Invierno | Vigilia del Muelle | 21 de invierno | Salinas Blancas | Salitre −1 | Barcas con luces en el muelle |
| Primavera | Suelta de las Palomas | 10 de primavera | Puerto Meridiano | — | Palomas sobre La Bolsa; escena breve |
| Primavera | Feria del Deshielo | 24 de primavera | Altafría | Cobre +2 | Banderines en las bocas de mina |
| Verano | Fiesta de la Sal | 8 de verano | Salinas Blancas | Salitre +2 | Montículos de sal pintados |
| Verano | Noche de los Faroleros | 22 de verano | Puerto Meridiano | Plata +1 | Fila de faroles en el Paseo Marítimo; la presencia de Los Faroleros |

Cada festivo tiene su ficha de tipo «festivo». ⏳ F4-32 construye el calendario y ⏳ F0-92 mide el efecto antes de fijar las cifras.

## 5 · Reglas de las mini-historias ✅

**Qué son.** Historias de 2 o 3 misiones lineales y enlazadas. **Tres por estación, 12 en el catálogo**, genéricas, repetibles cada año y sin molestar. La historia principal no depende de ellas ni de la fecha; son aleatorias y opcionales, y no mueven la línea temporal. Nada ocurre siempre.

| Regla | Valor |
|---|---|
| Elección | Se ofrecen las 3 de la estación y el jugador **elige 1** cuando quiere; las otras quedan para otro año |
| Activas | Máximo **1** a la vez |
| Coste de cada misión | Máximo **1 bloque** |
| Ventana | **14–28 días**. El día de cuota (día 7 de cada semana según [28](28-numeros-base-de-la-economia.md)) no vence ningún plazo |
| Cierres | Un cierre de entrada **pausa** el plazo |
| Aguante | No piden Aguante extra |
| Puertas y escenas | No puntúan para las puertas de acto ni bloquean escenas ancla |
| La Fosa | Solo se usa en los días 2, 4 y 6; este catálogo no la usa |
| Recompensa | **0,5–1 día de ingreso medio del acto** más una pila u objeto de decoración |
| Rotación | La historia hecha descansa un año o vuelve con otra variante |
| Acto | Se ofrecen **desde el Acto II**. Las de otoño no salen en la campaña (el otoño es el Acto I): se ven en el sandbox (⏳ F4-149) y en el segundo año |
| Mecánicas | Solo acciones que ya existen (hablar, extraer, comprar, vender, entregar); ninguna mecánica nueva |

### 5.1 Molde B1 ✅

Cada historia sigue: **gancho → obstáculo → entrega**, con huecos que se rellenan al empezar (zona, mineral, cliente sin nombre, facción). Hay **2 variantes de obstáculo** y se sortea una con `hash(partida, año, historia)`, así dos partidas distintas ven historias distintas y la misma partida es reproducible.

Obstáculos genéricos que se pueden usar:

| Obstáculo | Qué pasa |
|---|---|
| Plazo | La entrega vence en N días; el día de cuota no cuenta |
| Cierre | Una entrada de mina que necesitas está cerrada 1 o 2 días; el plazo se pausa |
| Vigilancia +N con atajo | Un camino corto sube la vigilancia en N; el largo cuesta 1 bloque más y no la sube |
| Comprador rival sin nombre | Otro comprador quiere lo mismo; llegas antes o aceptas menos |

Tono ✅: español neutro con tuteo, frases cortas, humor seco, nunca burla de los trabajadores. Los clientes no tienen nombre; las facciones son las que ya existen (Unión, Consorcio Arvel, Los Faroleros, Teletipo Meridiano).

## 6 · Catálogo de 12 mini-historias ✅

Cada una: **zona**, **misiones** (2 o 3), **obstáculo A / B** (se sortea uno) y **recompensa** (0,5–1 día de ingreso medio + pila u objeto). Cada misión cuesta, como máximo, 1 bloque. Las cifras de vigilancia (N) se fijan al medirlas ⏳ F0-92.

### 6.1 Primavera ✅

**P1 · «Hierro para las vigas» ✅** (Sierra Alta · Consorcio Arvel).
Gancho: el deshielo ha tirado una viga del economato y el capataz necesita hierro antes de que vuelva la nieve.
1. Hablas con el capataz en Altafría y aceptas el encargo.
2. Extraes el hierro en Sierra Alta.
3. Lo entregas en el economato.
- A · Plazo: vence en 14 días. B · Comprador rival sin nombre: otro contratista quiere el mismo hierro.
- Recompensa: 1 día de ingreso medio y una viga de madera para tu casa (decoración).

**P2 · «Salitre para los huertos» ✅** (Salares · Unión de Mineros del Hollín).
Gancho: la Unión quiere cultivar un huerto en el patio de la sede, y la tierra del Hollín no da nada sola.
1. Hablas con la Unión en Villa Brasa.
2. Consigues salitre (extraído o comprado).
3. Lo entregas en la sede.
- A · Cierre: la entrada que usas está cerrada un día. B · Vigilancia +N con atajo: el camino corto pasa junto a una inspección.
- Recompensa: 0,5 días de ingreso medio y una maceta para la casa.

**P3 · «Faroles nuevos» ✅** (Salinas Blancas · Los Faroleros).
Gancho: el invierno se llevó la mitad de los faroles del muelle y Los Faroleros buscan cobre para repararlos.
1. Recibes el encargo en el Bar del Farol.
2. Extraes el cobre.
3. Lo entregas en el muelle.
- A · Plazo: 21 días. B · Comprador rival sin nombre: alguien compra todo el cobre del mercado.
- Recompensa: 0,75 días de ingreso medio y un farol de bronce (decoración).

### 6.2 Verano ✅

**V1 · «Sal para el camino» ✅** (Salares · Puerto Meridiano).
Gancho: un cliente sin nombre del Puerto necesita sal para conservar una carga de pescado antes de que se eche a perder con el calor.
1. Aceptas el pedido en Puerto Meridiano.
2. Extraes salitre en Salares.
3. Lo entregas en el Puerto.
- A · Plazo: 14 días. B · Vigilancia +N con atajo: el atajo por la aduana la sube.
- Recompensa: 1 día de ingreso medio y una pila.

**V2 · «La pala que se rinde» ✅** (Cañón Ferroso · Unión).
Gancho: el calor ha estropeado los picos de la Unión y piden hierro para la herrería.
1. Hablas con la Unión.
2. Extraes hierro en el Cañón.
3. Lo entregas en la herrería-chatarrería.
- A · Cierre: una entrada del Cañón cerrada un día por un problema social (suave). B · Comprador rival sin nombre: otro herrero lo quiere.
- Recompensa: 0,75 días de ingreso medio y un martillo de adorno (decoración).

**V3 · «Fiesta sin plata» ✅** (Altafría · Consorcio Arvel).
Gancho: el Consorcio prepara una cena en el chalet y le falta plata para los cubiertos.
1. Recibes el encargo en la oficina del Consorcio.
2. Entregas la plata.
- A · Plazo: 14 días. B · Vigilancia +N con atajo: el camino corto pasa por una oficina que fiscaliza.
- Recompensa: 1 día de ingreso medio y un juego de cubiertos (decoración).

### 6.3 Otoño ✅ (solo sandbox y segundo año)

**O1 · «La última carga antes del frío» ✅** (Cuenca del Hollín · Unión).
Gancho: la Unión quiere llenar los almacenes de carbón antes del invierno y paga por adelantado.
1. Hablas con la Unión.
2. Extraes carbón.
3. Lo entregas en el almacén.
- A · Plazo: 14 días. B · Comprador rival sin nombre: otro vendedor ofrece carbón más barato.
- Recompensa: 0,75 días de ingreso medio y una pila.

**O2 · «Cosecha de sal» ✅** (Salares · Teletipo Meridiano).
Gancho: el Teletipo necesita salitre para un reportaje sobre la cosecha de sal del Litoral.
1. Aceptas el pedido.
2. Extraes salitre.
3. Lo entregas en la lonja.
- A · Cierre: una entrada cerrada por un problema social (suave). B · Vigilancia +N con atajo: pasas por la aduana.
- Recompensa: 0,5 días de ingreso medio y un ejemplar enmarcado del Teletipo (decoración).

**O3 · «El mercadillo de Altafría» ✅** (Altafría · Consorcio Arvel).
Gancho: un cliente sin nombre pide cobre para llenar un puesto en el mercadillo.
1. Recibes el encargo.
2. Extraes cobre.
3. Lo entregas en el puesto.
- A · Plazo: 21 días. B · Comprador rival sin nombre: otro puesto compra antes.
- Recompensa: 0,75 días de ingreso medio y una pila.

### 6.4 Invierno ✅

**I1 · «Carbón para la plaza» ✅** (Villa Brasa · Unión).
Gancho: la Unión quiere brasas en la plaza para las noches más frías y pide carbón.
1. Hablas con la Unión.
2. Extraes carbón.
3. Lo entregas en la plaza.
- A · Cierre: una entrada cerrada un día por un problema social (suave). B · Plazo: 14 días.
- Recompensa: 0,75 días de ingreso medio y un brasero (decoración).

**I2 · «El pedido del Puerto» ✅** (Puerto Meridiano · cliente sin nombre).
Gancho: un cliente sin nombre del Puerto pide plata a buen precio y necesita que no se sepa.
1. Aceptas el pedido.
2. Entregas la plata.
- A · Vigilancia +N con atajo: el camino corto pasa por la aduana. B · Comprador rival sin nombre: otro cliente se adelanta.
- Recompensa: 1 día de ingreso medio y una pila.

**I3 · «Un abrigo para la guardia» ✅** (Salinas Blancas · Los Faroleros).
Gancho: Los Faroleros hacen guardia en el muelle y no tienen con qué calentarse; piden carbón.
1. Recibes el encargo.
2. Extraes carbón.
3. Lo entregas en el muelle.
- A · Plazo: 14 días. B · Cierre: una entrada de los Salares cerrada un día por un problema social (suave).
- Recompensa: 0,5 días de ingreso medio y un abrigo colgado en tu casa (decoración).

## 7 · Futuro: sistema completo de clima ⏳ F6-77 y F6-78

Pronóstico, salud, ruta del tren y producción afectados por el clima quedan para V2+ o DLC (~40 h), como **«Sistema de clima completo»** (F6-77 y F6-78, registradas en el roadmap). F6-37, F6-38 y F6-39 quedan como están.

## 8 · Tareas que dependen de este documento

| Tarea | Qué toma |
|---|---|
| ⏳ F3-48 | Pestaña «Calendario» y apartado «En curso» del diario |
| ⏳ F4-32 | Calendario estacional, festivos y ciclos |
| ⏳ F4-33 | Noticias de clima |
| ⏳ F4-89 · ⏳ F4-171 | Fichas posibles y variación por semilla |
| ⏳ F4-250 | Cierres por lluvia |
| ⏳ F4-217 · ⏳ F4-165 | Tinte de paleta en los asentamientos |
| ⏳ F4-149 | Mini-historias de otoño en el sandbox |
| ⏳ F0-92 · ⏳ F0-93 | Cifras de efecto en el simulador |

## 9 · Decisiones del autor ✅

1. Los 8 festivos (nombres, fechas, zonas y efectos de mercado) quedan aprobados el 2026-10-24.
2. Los 12 títulos y ganchos del catálogo quedan aprobados el 2026-10-24; los de otoño no se ven en la campaña hasta el segundo año.
3. Doble cuenta del invierno ✅: el Aguante −2 y el carbón +12 son una compensación deliberada. ⏳ F0-93 añade la regla J6 (el ingreso por hora de cada estación queda dentro de ±20 % de la media); si el invierno se sale, se ajusta el −2 y no el carbón. La nieve ocurre como máximo 6 días por invierno y zona, y ⏳ F0-92 mide J3 por separado en días normales y en días de nieve.
4. Las cifras de vigilancia (N) y de plazo de cada variante se fijan al medirlas con el simulador (⏳ F0-92).
