# 26 · Zonas y edificios

Cómo está organizado el mapa vivo de Valdoria: qué zonas hay, qué edificaciones tiene cada una, qué se compra, vende, gana, gasta o juega en cada sitio, y en qué versión llega cada cosa. Nace de la tarea F0-82 y de las decisiones del autor del 2026-10-13. Las zonas de minado siguen en [02](02-extraccion.md), las regiones y los minerales en [05](05-mundo-y-minerales.md) y el estilo de vida en [04](04-progresion-y-meta.md).

**Cómo leer las marcas.** En las tablas del catálogo, la marca de la última columna habla de la **existencia y la versión** de la edificación: `✅` si el autor decidió las dos cosas y `🟡` si alguna sigue como propuesta. El autor confirmó el catálogo completo en lote (2026-10-13): cada edificación, su rol, lo que la hace propia de su zona y su versión. El detalle de la mercancía exacta de cada edificación se fija al hacerla, y va con el reloj de arena y su tarea. Lo que depende de una tarea del roadmap lleva el reloj de arena y su ID.

---

## 1 · Estructura: mapa, zona y edificación 🟡

**Estado:** ✅ la estructura de 1.1 y 1.2 (la región es la zona, con un asentamiento y la boca de mina como edificación), decisión del autor (2026-10-13), los nombres Altafría y Salinas Blancas en español y qué es cada uno; 🟡 los actos de apertura de cada asentamiento, el inglés de los dos nombres y las propuestas de 1.3.

### 1.1 Los tres niveles ✅

1. **Mapa de Valdoria.** Imagen ilustrada con las seis regiones tocables; las bloqueadas se ven apagadas ([12](12-direccion-de-arte.md), ⏳ F4-152 y ⏳ F4-153).
2. **Zona.** La región es la zona. Al hacer clic en ella (o elegirla con el mando) entras a la **vista de zona**: el asentamiento en isométrica, con sus edificaciones seleccionables ([12](12-direccion-de-arte.md), perspectiva).
3. **Edificación.** Eliges a cuál entrar y ves **esa edificación por separado**, en vista interior en corte transversal, como la tienda. La boca de mina es una edificación más: al entrar a ella pasas a la vista lateral de la mina.

La navegación entre los tres niveles es ⏳ F4-167.

### 1.2 Zona, asentamiento y zona de minado ✅

- **Zona** (del mapa) es la región con su asentamiento. **Zona de minado** son las seis de [02](02-extraccion.md); cada una se entra por su **boca de mina**, dentro de un asentamiento.
- Cada zona tiene **un asentamiento**. **Villa Brasa atiende las dos zonas de minado del Hollín** (Galerías del Hollín y Cañón Ferroso): desde su vista de zona eliges una de las dos bocas. **Puerto Meridiano** es la zona de la capital y no tiene boca de mina.
- El asentamiento es donde se comercia, se contrata y se vive; la boca de mina es donde se extrae. Moverte entre zonas no gasta bloques pero cuesta un poco de dinero (billete o combustible), y ver las zonas en el mapa es gratis ✅ ([01](01-core-loop.md); decisión del autor, 2026-10-15). El trayecto cuesta entre 30 y 150 esquirlas, 0 entre las dos bocas de Villa Brasa y nada en el Acto I, porque todo ocurre en Villa Brasa ✅ ([28](28-numeros-base-de-la-economia.md)). Las Cavernas y La Fosa son zonas profundas: 2 bloques, Tarde y Noche, y La Fosa solo abre 3 días por semana ✅: los días 2, 4 y 6 de cada semana, y el 7 queda libre para la cuota. Cómo se ve el viaje ⏳ F4-154.

| Zona (región) | Asentamiento | Bocas de mina | Se abre en el acto 🟡 |
|---|---|---|---|
| Cuenca del Hollín | **Villa Brasa** | Galerías del Hollín; Cañón Ferroso (desde el II) | I |
| Sierra Alta | **Altafría** | Minas de Sierra Alta | II |
| Salares del Litoral | **Salinas Blancas** | Salares del Litoral | II |
| Cavernas de Cristal | campamento (ver 1.3) | Cavernas de Cristal | III |
| La Fosa | campamento de la Comisión (ver 1.3) | La Fosa del Éter | IV |
| Puerto Meridiano | la propia ciudad | ninguna | III |

Los nombres **Altafría** y **Salinas Blancas**, en español, los decidió el autor ✅; Altafría es el pueblo de empresa del Consorcio en Sierra Alta y Salinas Blancas es el puerto de los Salares, de los Faroleros y del contrabando ✅. 🟡 En inglés, *Highchill* y *White Salt Flats* ([18](18-biblia-narrativa.md), 6.5), pendientes de confirmar en lote ⏳ F1-20. Los actos de la columna anterior son propuesta: los actos de las zonas de minado no cambian ([17](17-mapa-de-historia.md)), pero qué asentamiento abre en cada uno no lo ha revisado el autor.

### 1.3 Dos propuestas dentro de la estructura 🟡

- **Campamentos sin nombre propio.** Las Cavernas y la Fosa no tienen vivienda y su asentamiento es un campamento. Se usan nombres descriptivos («el campamento de las Cavernas», «el campamento de la Comisión») hasta que el autor elija nombres propios; cambiarlos solo toca textos y datos, no estructura.
- **Horarios por bloque.** Cada edificación declara en qué bloques del día abre (mañana, tarde, noche); el bar de Los Faroleros y el Salón del Farol, solo de noche, como el mercado negro ([03](03-comercio.md)). La tienda del jugador, en cambio, abre solo de mañana y de tarde: **nunca de noche** ✅ ([01](01-core-loop.md)).

---

## 2 · Catálogo de edificaciones por zona 🟡

**Estado:** ✅ el catálogo como base (decisión del autor, 2026-10-13): las edificaciones, sus roles, lo que hace propia a cada una de su zona y su versión (MVP, V1, V2.0, V2.1, V2.2 y evolutivo), incluidos los nombres del Salón del Farol, el chalet de Altafría, el caserón de Salinas Blancas y las tres mansiones; 🟡 el número exacto de edificaciones por zona (solo el total está confirmado) y la ubicación de la Lotería (la ventanilla de la sede del Ministerio). El detalle de la mercancía exacta de cada edificación se fija al hacerla: ⏳ F4-219 a F4-225 en V1 y ⏳ F6-47 a F6-58 en V2.

**Roles.** *Comprar* y *vender* (el jugador compra o vende), *ganar* (ingresos que no son una venta: contratos, sueldos, premios), *gastar* (cuotas, impuestos, mantenimiento, estilo de vida), *minijuego* (se juega uno de [09](09-minijuegos.md)) e *historia* (sitio de misión o de cinta, [23](23-arbol-de-decisiones.md), sección 7). **Versiones:** MVP, V1, V2.0, V2.1, V2.2 y evolutivo (sección 7). **ID:** `ed-<zona>-<nombre>`, con `vb` Villa Brasa, `af` Altafría, `sb` Salinas Blancas, `cv` Cavernas, `fo` Fosa y `pm` Puerto Meridiano.

Cada boca de mina lleva además el **mostrador de preparación** de su zona (loadout de [02](02-extraccion.md)): máscara y refuerzos en el Hollín, equipo para frío y altitud en Altafría, agua y protección en los Salares, y filtros en la Fosa. No cuenta como edificación aparte.

### 2.1 Cuenca del Hollín: Villa Brasa

Obrero y humo; manda la Unión. La herrería alimenta el Acero y la tienda atiende a clientes obreros.

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| `ed-vb-tienda` | Tienda (el puesto reabierto) | vender, comprar, minijuego (Regateo, Reponer) | Mercancía de carbón y hierro; clientes obreros; la cinta 1 está en el doble fondo de la caja | MVP | ✅ |
| `ed-vb-taller` | Taller | ganar (valor agregado), minijuego (Refinado) | Acero (hierro y carbón). Se construye en el MVP y **se abre en el Acto II**; el Acto I no lo usa ✅ | MVP | ✅ |
| `ed-vb-almacen` | Almacén | gastar (alquiler y costo de guardar) | Donde la especulación cuesta de verdad ([03](03-comercio.md)) | MVP | ✅ |
| `ed-vb-casa` | Casa obrera (casa base) | gastar | Chimeneas y humo en la vista; descanso y decoración (sección 4) | MVP; mejorable en V1 | ✅ |
| `ed-vb-reme` | Casa de Reme | gastar (cuotas de la deuda) | Reme, la prestamista; su facción cambia según la partida ([22](22-acto-ii-variantes.md)) | MVP | ✅ |
| `ed-vb-quiroga` | Oficina del Inspector | gastar (licencias, multas, «trámites») | Quiroga; baja o sube la vigilancia ([03](03-comercio.md)) | MVP | ✅ |
| `ed-vb-mina-galerias` | Boca de las Galerías del Hollín | minijuego (Picado y Perforación; la Detonación, con el explosivo, desde el Acto III y no en el MVP) | Carbón principal; Teo enseña el oficio. El Picado sirve para carbón, hierro, cobre, plata y oro ✅ ([09](09-minijuegos.md)); aquí se pica carbón y hierro | MVP | ✅ |
| `ed-vb-mina-canon` | Boca del Cañón Ferroso | minijuego (Picado, Perforación) | Hierro principal, con algo de cobre; bandas rivales. El Picado sirve para carbón, hierro, cobre, plata y oro ✅ ([09](09-minijuegos.md)), así que también pica el cobre | V1 | ✅ |
| `ed-vb-union` | Sede de la Unión | ganar (Bolsa de la Unión: contratar), gastar | Medidor de la Unión, huelgas, Delegado de la Unión | V1 | ✅ |
| `ed-vb-periodico` | Quiosco y redacción de La Voz del Hollín | comprar (prensa, anuncios), ganar (empleos) | Sesgo sindical; vende también el Heraldo y el Teletipo; Lucía y el voceador pasan por aquí | V1 | ✅ |
| `ed-vb-herreria` | Herrería-chatarrería | comprar, vender | Hierro, carbón y repuestos de herramientas; su hierro y su carbón alimentan el Acero del taller | V1 | ✅ |

### 2.2 Sierra Alta: Altafría

Frío y Consorcio. La plata que se afina aquí la compra después Casa Ormeño.

**Cumbre Clara no es un edificio ✅.** El Sanatorio de Cumbre Clara, donde murió Anselmo en público, es solo un nombre (decisión del autor, 2026-10-13): no es zona ni edificación de este catálogo y no se visita ([21](21-pasado-de-valdoria.md)).

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| `ed-af-mina` | Boca de las Minas de Sierra Alta | minijuego (Picado, Perforación, Cribado) | Cobre y plata principales (el Picado sirve para cobre, plata y oro ✅, [09](09-minijuegos.md)); frío y falta de aire; guardias de empresa | V1 | ✅ |
| `ed-af-consorcio` | Oficina del Consorcio Arvel | ganar (contratos del Consorcio) | Esteban Arvel; ejecutivos y capataces | V1 | ✅ |
| `ed-af-economato` | Economato del Consorcio | comprar | Abrigo y vales de empresa: se paga al precio del Consorcio | V1 | ✅ |
| `ed-af-plateria` | Fundición-platería | vender (plata), comprar (lingote de plata) | Afina la plata de la sierra; sus joyas de plata llegan con las gemas (sección 3) | V1 | ✅ |
| `ed-af-taller-ensayo` | Viejo taller de ensayo | historia | Casillero con la cinta 2 | V1 | ✅ |
| `ed-af-chalet` | Chalet de la cordillera | gastar (casa comprable) | Vista a la cordillera (sección 4) | V2.1 | ✅ |

### 2.3 Salares del Litoral: Salinas Blancas

Faroleros y contrabando. El salitre enlaza con la agricultura y la pólvora.

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| `ed-sb-mina` | Boca de los Salares del Litoral | minijuego (Cribado) | Salitre principal; sed y gases; contrabandistas e inspectores corruptos | V1 | ✅ |
| `ed-sb-lonja` | Lonja y almacén de salitre | vender, comprar | Salitre para agricultura y pólvora; más adelante, el pescado | V1 | ✅ |
| `ed-sb-bar` | Bar del Farol (Los Faroleros) | comprar y vender en el mercado negro, ganar | Casilda; abre de noche; contacto del mercado negro: en el III compras aquí la Aetherita y en el IV recibes sus encargos especiales, raros y con historia (la venta rutinaria va a la Comisión) (también hay una visita nocturna de Casilda a la tienda, que no es el modo tienda); joyas sin sello (sección 3) | V1 | ✅ |
| `ed-sb-caseron` | Caserón frente al mar | gastar (casa comprable) | Mar abierto (sección 4) | V2.1 | ✅ |
| `ed-sb-muelle` | Muelle de pesca | minijuego (pesca), vender | Pesca con el motor del Cribado | V2.2 | ✅ |
| `ed-sb-astillero` | Astillero | comprar (embarcaciones), gastar | Bote, pesquero y barcaza | V2.2 | ✅ |
| `ed-sb-aduana` | Aduana | gastar (impuestos de puerto) | Aduanero Mayor; de momento los impuestos van por pantalla | evolutivo | ✅ |

El bar está en Salinas Blancas porque los Faroleros nacieron como gremio de los faroles de los puertos ([21](21-pasado-de-valdoria.md)).

### 2.4 Cavernas de Cristal: campamento

Gemas en zona disputada; sin vivienda.

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| `ed-cv-mina` | Boca de las Cavernas de Cristal | minijuego (Picado, Cincelado, Perforación, Cribado) | Oro, cuarzo y esmeralda principales; cristales cortantes; cazarrecompensas; siempre abierta, expedición de 2 bloques (Tarde y Noche) ✅ | V1 | ✅ |
| `ed-cv-tasadores` | Tasadores | vender (gemas), minijuego (Tasar) | Tasan esmeralda, diamante y cuarzo; hay piezas falsas (⏳ F4-55) | V1 | ✅ |
| `ed-cv-campamento` | Campamento de ensayo | historia | Cinta 4, bajo el cuarzo | V1 | ✅ |
| `ed-cv-taller-talla` | Taller de talla | minijuego (Cincelado), vender | Joyas de gema tallada (sección 3) | V2.1 | ✅ |

### 2.5 La Fosa: campamento de la Comisión

Sin vivienda, lujo ni azar. Solo historia y la boca de mina.

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| `ed-fo-mina` | Boca de La Fosa del Éter | minijuego (Contención, Cincelado) | Aetherita y diamante principales; mostrador de filtros (los filtros de la Comisión que exige la Aetherita; cifras en [28](28-numeros-base-de-la-economia.md)); solo abre 3 días por semana, los de calibración de la Comisión ✅ (los días 2, 4 y 6 de cada semana) | V1 | ✅ |
| `ed-fo-campamento-viejo` | Campamento de la Primera Expedición | historia | Cinta 6, en la caja del equipo de ensayo | V1 | ✅ |
| `ed-fo-barracon` | Barracón de calibración | historia | Cintas 7 y 8 y el acta de calibración | V1 | ✅ |

### 2.6 Puerto Meridiano

Lujo, prensa y modas de la esmeralda. Llega en el Acto III.

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| `ed-pm-bolsa` | La Bolsa | comprar, vender (mercado spot) | Interfaz del mercado ([03](03-comercio.md), ⏳ F4-166); pestaña de inversiones en V2.2 | V1 | ✅ |
| `ed-pm-ministerio` | Sede del Ministerio de Recursos | gastar (licencias mayores, impuestos), ganar (contratos oficiales) | Montenegro; la ventanilla de la Lotería en V2.0 (ubicación 🟡, sección 5) | V1 | ✅ |
| `ed-pm-casa-ormeno` | Casa Ormeño (tienda insignia) | vender (plata, joyas), comprar (piezas de lujo) | Joyería de plata para la élite; sin dueño ni medidor | V1 | ✅ |
| `ed-pm-comision` | Oficina de la Comisión del Éter | vender (Aetherita) | Canal legal del Acto IV: la Comisión compra la Aetherita a valor justo, con tope diario; siempre abierta, pero hay que ir a la capital a vender ✅ ([28](28-numeros-base-de-la-economia.md)) | V1 | ✅ |
| `ed-pm-estacion` | Estación | historia | Consigna con la cinta 3 | V1 | ✅ |
| `ed-pm-pension` | Pensión | historia | Cinta 5, donde Anselmo se alojaba al entregar sus informes | V1 | ✅ |
| `ed-pm-salon` | Salón del Farol | ganar y gastar (azar), minijuego | Casino de noche de Los Faroleros (sección 5) | V2.0 | ✅ |
| `ed-pm-inmobiliaria` | Inmobiliaria | comprar (casas y mansiones) | Lista las propiedades de todas las zonas | V2.1 | ✅ |
| `ed-pm-mansion-paseo` | Mansión del Paseo Marítimo | gastar | Vista al mar | V2.1 | ✅ |
| `ed-pm-mansion-colina` | Mansión de la Colina de la Bolsa | gastar | Vista a la ciudad | V2.1 | ✅ |
| `ed-pm-mansion-barrio` | Mansión del Barrio Alto | gastar | Vista a un jardín | V2.1 | ✅ |
| `ed-pm-joyeria` | Joyería del dueño | comprar el negocio, ganar, minijuego | La joyería que compras y atiendes (sección 3.3) | V2.1 | ✅ |
| `ed-pm-concesionaria` | Concesionaria | comprar (vehículos) | Automóviles, camionetas y carretas | V2.1 | ✅ |
| `ed-pm-sastreria` | Sastrería | comprar (ropa) | Un traje por escalón de estatus y ropa cosmética | V2.1 | ✅ |
| `ed-pm-puerto-deportivo` | Puerto deportivo | comprar (yate), gastar | El yate, solo estatus | V2.2 | ✅ |

**Cuenta.** El catálogo tiene 46 filas: las **45 edificaciones** de MVP, V1 y V2 y, además, la aduana de Salinas Blancas, que es evolutivo y **no entra en las 45**. La oficina de la Comisión del Éter (`ed-pm-comision`, Puerto Meridiano) es la que se añadió el 2026-10-16 ✅.

**Edificaciones que se dejan fuera por ahora (evolutivo):** la aduana de Salinas Blancas (la única con fila, para reservar su ID), las redacciones del Heraldo y del Teletipo (hoy se compran en el quiosco), un tablón de cazarrecompensas en las Cavernas y una oficina del Consorcio en la capital. Ninguna es necesaria para la historia ni para el mercado.

---

## 3 · Joyerías y joyas por zona ✅

**Estado:** ✅ decisión del autor (2026-10-13): cada zona vende o compra joyas de sus minerales, Casa Ormeño es la tienda insignia de la capital y la joyería se compra a su dueño en Puerto Meridiano en V2.1. El dueño y el trabajo en el banco se detallan en ⏳ F6-54 y ⏳ F6-55.

### 3.1 Qué existe para hacer joyas

La única receta de joyería del registro del mundo es **Joyería = oro o plata + esmeralda o diamante** ([03](03-comercio.md), `world.json`). Las gemas aparecen en las Cavernas (Acto III), así que **ninguna joya existe antes del Acto III**: hasta entonces la platería de Altafría solo compra y vende plata y lingote de plata. No se inventan minerales ni recetas. Las cuatro combinaciones posibles (oro o plata, con esmeralda o diamante) son las «joyas específicas» de cada zona, según qué metal y qué gema abundan allí.

### 3.2 Por zona

| Zona | Joyería | Minerales de la zona | Joyas y estilo | Compra | Vende | Versión |
|---|---|---|---|---|---|---|
| Villa Brasa | ninguna | carbón, hierro | Sin joyería: es un pueblo obrero | — | — | — |
| Altafría | Platería (`ed-af-plateria`) | plata principal, oro secundario | Joyas de plata con esmeralda o diamante, sobrias y con sello del Consorcio | plata, joyas de plata | lingote de plata | V1 |
| Salinas Blancas | Mostrador sin sello del bar (`ed-sb-bar`) | plata secundaria | Joyas de plata sin sello: sin impuesto y con prima de mercado negro, a cambio de vigilancia ([03](03-comercio.md)) | joyas sin sello | — | V2.1 |
| Cavernas | Taller de talla (`ed-cv-taller-talla`) | oro, esmeralda y cuarzo principales, diamante secundario | Joyas de oro con esmeralda o diamante tallado: el corte fino se juega con Cincelado | gemas, joyas de gema | joyas de gema tallada | V2.1 |
| La Fosa | ninguna | diamante principal, oro y esmeralda secundarios | Sin lujo: su diamante se vende en las Cavernas o en la capital | — | — | — |
| Puerto Meridiano | Casa Ormeño (`ed-pm-casa-ormeno`) | plata que llega de Altafría | Joyas de plata con esmeralda: sigue las modas de la élite ([03](03-comercio.md)) | plata y joyas de plata, a prima si hay moda | piezas de lujo para la vitrina | V1 |
| Puerto Meridiano | Joyería comprable (`ed-pm-joyeria`) | las cuatro combinaciones | Todas, con el gusto del jugador | joyas | joyas | V2.1 |

### 3.3 La joyería que compras

El autor pidió que el jugador pueda **comprarle una joyería pequeña a su dueño y trabajar en ella** ✅, y confirmó que está en Puerto Meridiano y llega en V2.1 ✅. Está allí para competir de frente con Casa Ormeño. El dueño es un joyero mayor sin nombre de elenco, con su historia contada en un par de líneas y sin medidor (⏳ F6-54); «trabajar en ella» es atender a la clientela de la élite (Regateo) y labrar piezas en el banco (Cincelado), con empleados que pueden ayudar (⏳ F6-55). No añade minijuegos nuevos. Casa Ormeño sigue siendo una tienda insignia **sin dueño ni medidor** y no se compra ([21](21-pasado-de-valdoria.md)).

---

## 4 · Casas y mansiones 🟡

**Estado:** ✅ que hay casas y mansiones comprables en varias zonas, cada una con su vista, aspecto y nombre (el chalet de Altafría, el caserón de Salinas Blancas, las mansiones del Paseo Marítimo, la Colina de la Bolsa y el Barrio Alto) en V2.1, que la casa base es completa, que la de V1 nace con ranuras de decoración y que la decoración variada llega después; 🟡 las ranuras exactas, los objetos de decoración y los efectos de los bonos.

### 4.1 Dónde y con qué vista

| Casa | Zona | Vista y aspecto | Versión |
|---|---|---|---|
| Casa obrera (`ed-vb-casa`) | Villa Brasa | Chimeneas y humo; ladrillo y techo bajo. Es la **casa base**, desde el inicio | MVP |
| Chalet (`ed-af-chalet`) | Altafría | Cordillera nevada; madera y estufa | V2.1 |
| Caserón (`ed-sb-caseron`) | Salinas Blancas | Mar abierto y salinas; cal blanca y persianas | V2.1 |
| Mansión del Paseo Marítimo | Puerto Meridiano | Mar | V2.1 |
| Mansión de la Colina de la Bolsa | Puerto Meridiano | Ciudad y la Bolsa | V2.1 |
| Mansión del Barrio Alto | Puerto Meridiano | Jardín | V2.1 |

Que existan casas y mansiones con vistas distintas, sus nombres, su lugar y su versión V2.1 son ✅ (decisión del autor, 2026-10-13).

No hay casas en las Cavernas (campamento en zona disputada) ni en la Fosa (militarizada). Para V2.1, el orden de magnitud es de 150 000 a 250 000 esquirlas para el chalet y el caserón y de 600 000 a 2,5 millones para las mansiones ✅ ([28](28-numeros-base-de-la-economia.md)). El modelo del saqueo ⏳ F4-84.

### 4.2 La casa base completa

La casa **llega amueblada y completa** desde el MVP, sin habitaciones por desbloquear. En V1 se mejora (⏳ F4-110) y **nace con ranuras de decoración** ✅; las ranuras (⏳ F4-226) se hacen en el hito F4.7, antes de la casa mejorable. Las ranuras son cinco, fijas 🟡: **sala, despacho, dormitorio, vitrina y exterior**. Cada una acepta un objeto de una región (forja y lámparas del Hollín, pieles y mapas de la sierra, faroles y redes del litoral, geodas de las Cavernas, platería de la capital). En V1 cada ranura trae un objeto inicial; el catálogo variado llega en V2.1.

- **Bonos pequeños 🟡:** la casa mejor da un poco más de energía al empezar cada expedición: +2 por nivel, hasta +8 en el nivel 4 ✅ ([04](04-progresion-y-meta.md)); las ranuras no dan bonos de juego, son cosméticas.
- **Precios de la casa base en V1 ✅:** remozada, 4 000 esquirlas; de comerciante, 22 000; de empresario, 110 000; residencia, 450 000 ([28](28-numeros-base-de-la-economia.md)).
- **Costos:** impuesto predial (sumidero) de un 1 % del valor al mes y riesgo de saqueo, que se mitiga con guardias y protección ([07](07-sociedad-y-eventos.md)). Un seguro contra saqueo cuesta un 0,3 % del valor de la casa al mes; sin él, un saqueo cuesta cerca de un 3 % del efectivo ([28](28-numeros-base-de-la-economia.md)).
- **Varias casas:** puedes tener varias; duermes en la **casa base activa**, y las otras dan su vista y su decoración y cobran su impuesto.

### 4.3 Qué se deja para después

Decoración libre (colocar objetos donde quieras), subastas de propiedades, alquilar casas como ingreso y casas en otras ciudades: evolutivo, sin estimar.

---

## 5 · Salón del Farol y Lotería 🟡

**Estado:** ✅ que el casino llega en V2.0 con el nombre Salón del Farol, en Puerto Meridiano, y con sus condiciones legales (la sección 5.2); 🟡 la Lotería (su ubicación) y los premios.

### 5.1 Qué es

El **Salón del Farol** es el casino de Puerto Meridiano. Abre de noche y lo operan **Los Faroleros**, que no tienen medidor: se miden por la alianza ([07](07-sociedad-y-eventos.md)). Tiene tragamonedas, ruleta y blackjack ([06](06-roadmap-y-pendientes.md), ⏳ F6-01). Aparte, la **Lotería del Ministerio** hace un sorteo semanal que publica el Heraldo; los billetes se compran en la ventanilla de la sede del Ministerio 🟡. Cómo entra el Salón en la economía y la vigilancia ⏳ F6-11.

### 5.2 Condiciones legales ✅

- El juego **no se dirige a menores** ([11](11-legal-y-cumplimiento.md)).
- Solo **moneda del juego**, sin dinero real.
- **Probabilidades visibles** en cada juego.
- **Tope diario** de apuestas.
- Un **interruptor «ocultar azar»**. Las opciones de juego responsable ⏳ F6-14.

### 5.3 Reglas añadidas

- El interruptor «ocultar azar» oculta el Salón del Farol y la Lotería.
- Ningún premio es necesario para la historia, y **ninguno es Aetherita** ni joya de la historia.
- Los cuestionarios de edad pueden subir la clasificación al llegar el casino: verificar antes de publicarlo ⏳ F6-13. El lanzamiento (V1) no incluye azar, así que su cuestionario ⏳ F5-28 se contesta sin él.
- Como sumidero de dinero, su balance ⏳ F6-15.

---

## 6 · Vehículos, ropa, embarcaciones, pesca e inversiones 🟡

**Estado:** ✅ que existen, que la ropa solo cambia el sprite pequeño, que V1 trae ropa por estatus y un auto, y que la sastrería, la concesionaria, el astillero, el puerto deportivo y la pesca llegan en V2.1 y V2.2; 🟡 que el auto de V1 sea solo estatus y aspecto, qué vehículo va en qué zona y qué efecto tiene cada vehículo y embarcación.

| Cosa | Lugar temático | Qué hace | Por qué ahí | Versión |
|---|---|---|---|---|
| **Ropa**: un traje por escalón de estatus (Heredero a Magnate) | V1: pantalla de estilo de vida ⏳ F4-119; V2.1: sastrería de la capital | Solo cambia el sprite pequeño; las hojas de modelo y los retratos no se rehacen ✅. Un traje cuesta 300 esquirlas (Minero con licencia), 2 500 (Comerciante), 16 000 (Empresario) o 90 000 (Magnate) ✅ | La ropa dice a qué clase perteneces ([07](07-sociedad-y-eventos.md)); la sastrería es de la capital | V1 y V2.1 |
| **Auto**: uno en V1 (⏳ F4-112); en V2.1 tres 🟡 | V1: pantalla de estilo de vida; V2.1 🟡: carreta (herrería de Villa Brasa), camioneta (Altafría), automóvil (concesionaria) | El de V1 es solo estatus y aspecto, sin efecto en el viaje ✅, y cuesta 70 000 esquirlas, con un mantenimiento del 0,5 % al mes ✅; el viaje cuesta un poco de dinero y eso da sentido al auto ✅ ([01](01-core-loop.md)); el efecto funcional pequeño en tiempo de viaje y carga llega con la concesionaria de V2.1 ⏳ F6-57; ninguno es obligatorio | Cada vehículo es del lugar que lo usa: carreta en el Hollín obrero, camioneta en la sierra del Consorcio, automóvil en la capital | V1 y V2.1 |
| **Embarcaciones**: bote, pesquero y barcaza | Astillero de Salinas Blancas | El bote y el pesquero mejoran la pesca; la barcaza aligera el transporte de salitre por la costa (efecto ⏳ F6-63) | Solo hay puerto de pesca y carga en los Salares | V2.2 |
| **Yate** | Puerto deportivo de la capital | Solo estatus, de unos 3 millones de esquirlas ✅ | El lujo vive en Puerto Meridiano | V2.2 |
| **Pesca** | Muelle y lonja de Salinas Blancas | Se juega con el motor del Cribado ([09](09-minijuegos.md): inclinación y caudal, «como la pesca»); el pescado se vende en la lonja | El Cribado es del litoral y la lonja ya es el comercio del puerto | V2.2 |
| **Inversiones** | Pestaña de la Bolsa, no edificio | Sectores de [03](03-comercio.md): agricultura (la mueve el salitre), tecnología (la mueve el cuarzo) y pesca (la mueven las noticias del litoral; no mueve minerales); con spread y tope | La Bolsa es donde se especula; sin tope sería dinero gratis | V2.2 |

El pescado es una mercancía nueva y **no es un mineral**: no cambia la regla de 2 a 3 zonas por mineral. La «agricultura» puede nombrar Vega Mansa en las noticias sin visitarla ([18](18-biblia-narrativa.md)). El sector de pesca no está en la lista de sectores de demanda de [03](03-comercio.md) y se queda como sector de inversión; ⏳ F4-31 fija los de demanda.

---

## 7 · Versiones y horas 🟡

**Estado:** ✅ el reparto por versiones (decisión del autor, 2026-10-13): MVP con solo Villa Brasa y 6 edificaciones, V1 con unos 22, V2.0 con casino y lotería, V2.1 con casas y mansiones, decoración, joyería comprable, concesionaria y sastrería (unos 10), V2.2 con pesca, astillero, barcos e inversiones (unos 4) y los evolutivos, y el orden de V2 (casino, propiedad y mar); 🟡 todas las horas (±50 %, como el resto de F4 en adelante).

Las horas son del autor y se suman a las del roadmap ([06](06-roadmap-y-pendientes.md)). Supuesto 🟡: de 6 a 10 h por edificación nueva según plantilla (exterior, interior y datos); las 12 de F4-219 a F4-223 suman 78 h, unas 6,5 h cada una; la decoración y la ropa son el mayor gasto de arte. «V2» es el contenido de la fase F6; iOS, PC, voces e idiomas de F6 no se tocan.

| Versión | Fase del roadmap | Edificaciones | Contenido | Horas sobre el roadmap 🟡 |
|---|---|---|---|---|
| **MVP** | F2–F3 | 7: tienda, taller, almacén, casa, Reme, Quiroga y boca de las Galerías | Solo Villa Brasa, en lista con arte provisional (⏳ F3-18). Sin mapa. El taller se construye aquí pero se abre en el Acto II ✅ | 0 |
| **V1** | F4–F5 | +24: 19 edificios y 5 bocas de mina | Mapa y vista de zona de las seis zonas (⏳ F4-152, ⏳ F4-165); los 9 del roadmap (⏳ F4-155, ⏳ F4-156), la Bolsa, la oficina de la Comisión, 6 edificios de historia y 6 comercios; casa mejorable con ranuras, ropa por estatus y un auto | +110 a 150 |
| **V2.0** | F6, hito F6.1 | +1: Salón del Farol | Casino y Lotería | +12 (la Lotería; el casino son las ~100 h ya estimadas) |
| **V2.1** | F6, hito nuevo | +10 | Casas por zona y mansiones, catálogo de decoración, joyería comprable, joyas por zona, concesionaria y sastrería | 250 a 300 |
| **V2.2** | F6, hito nuevo | +3 y una pestaña | Pesca, astillero, embarcaciones, yate e inversiones en la Bolsa | 120 a 160 |
| **Evolutivos** | después de F6 | — | Decoración libre, subastas, alquiler de casas, aduana, redacciones, sucursales ([06](06-roadmap-y-pendientes.md), ⏳ F6-34) y más ciudades (⏳ F6-35) | sin estimar |

**Lo que suman.** Al final de V1 hay 31 edificaciones (25 edificios y 6 bocas); el autor decidió «unos 22 edificios», y salen de 9 del roadmap, la Bolsa, la oficina de la Comisión, 6 de historia y 6 comercios. Los otros 2 son la casa de Reme y la oficina de Quiroga, que ya existen en el MVP y reciben su exterior en V1. Con MVP, V1 y V2: 45 edificaciones (la aduana, evolutivo, es la fila 46 del catálogo y no cuenta). F6 pasa de 305–570 h a unas 690–1.040 h. El orden de V2 es casino, propiedad y mar ✅.

**Por qué los edificios de historia son seis y no cinco.** Las cintas 1 a 8 están en siete sitios ([23](23-arbol-de-decisiones.md), sección 7): el puesto (la tienda), el viejo taller de ensayo, la estación, el campamento de ensayo, la pensión, el campamento de la Primera Expedición y el barracón de calibración. Seis son edificaciones nuevas. Como las cintas 1 a 5 son obligatorias, no pueden ser opcionales.

### Lo que cada cosa necesita, y cuándo existe

| Cosa | Necesita | Existe desde |
|---|---|---|
| Joyas (todas las joyerías) | Oro o plata, y esmeralda o diamante | Acto III (las gemas) |
| Tasadores | Gemas y el minijuego Tasar | Acto III; el minijuego es ⏳ F4-55 |
| Casa Ormeño | Plata, que ya circula desde el II | Acto III (la capital) |
| Lonja y salitre | Salitre y Cribado | Acto II |
| Herrería | Hierro y carbón | Acto II |
| Pesca | Cribado | Acto II; sale a la venta en V2.2 |
| Inversión en tecnología | Cuarzo | Acto II |

---

## 8 · Por qué cada cosa está donde está 🟡

Las razones de cada colocación; nada se pone sin una razón de mundo. ✅ Las del catálogo, confirmadas por el autor; 🟡 la de los vehículos.

| Cosa | Dónde | Por qué ahí |
|---|---|---|
| Herrería y repuestos | Villa Brasa | El Hollín es hierro y carbón; la herrería convierte esos dos en Acero |
| Sede de la Unión y La Voz del Hollín | Villa Brasa | La Unión manda en el Hollín y su periódico es sindical |
| Economato y oficina del Consorcio | Altafría | Es un pueblo de empresa: el Consorcio es dueño del comercio y del contrato |
| Platería | Altafría | La plata principal está en la sierra |
| Casa Ormeño | Puerto Meridiano | Compra la plata de Sierra Alta y la vende a la élite ([21](21-pasado-de-valdoria.md)) |
| Lonja y salitre, pesca, astillero | Salinas Blancas | Salitre y Cribado son del litoral, y es el único puerto de carga |
| Bar del Farol y mercado negro | Salinas Blancas | Los Faroleros nacieron en los puertos |
| Salón del Farol | Puerto Meridiano | Los Faroleros llevan su farol a donde está el dinero; la capital es el lujo |
| Tasadores | Cavernas | Es donde nacen las gemas, y una gema falsa se nota con el Ojo |
| Sin casas en Cavernas y Fosa | — | Zona disputada y zona militarizada: nadie compra casa allí |
| Mansiones | Puerto Meridiano | El estatus alto vive en la capital |
| Joyería comprable | Puerto Meridiano | Compite con Casa Ormeño y vende a la misma élite |
| Carreta, camioneta, automóvil 🟡 | Hollín, Altafría y capital | Cada vehículo es del lugar que lo usa |
| Inversiones | Bolsa | La Bolsa es donde se especula |
| Historia (taller, estación, pensión, campamentos) | Donde Anselmo escondió las cintas | Son sitios de su vida ([23](23-arbol-de-decisiones.md)) |

---

## 9 · Riesgos y reglas de canon 🟡

**Estado:** ✅ solo Casa Ormeño; 🟡 las demás reglas y los riesgos, propuestos al autor.

**Reglas de canon** (se respetan en todo el catálogo):

- **Aetherita 🟡.** No va en joyas, casas, decoración ni premios. La celda de éter es otra receta. El éter no se muestra suelto ([18](18-biblia-narrativa.md), 5.2).
- **La Fosa 🟡.** No tiene vivienda, lujo ni azar.
- **Joyas y medidores 🟡.** Regalar o vender joyas no sube ningún medidor: los cuatro medidores se mueven por decisiones de la historia ([24](24-umbrales-de-acto.md)), y el estilo de vida no sube stats directamente ([04](04-progresion-y-meta.md)).
- **Casa Ormeño ✅.** Sin dueño, jefe, personaje ni medidor ([21](21-pasado-de-valdoria.md)).

**Riesgos:**

| Riesgo | Respuesta |
|---|---|
| Casas, casino e inversión son sumideros o atajos de dinero | Sus precios ya están en [28](28-numeros-base-de-la-economia.md) ✅ y se ajustan con ⏳ F5-06; la inversión usa los frenos de [03](03-comercio.md) (spread y tope) |
| Arte: la ropa multiplica piezas y la decoración es el mayor pozo | Ropa solo en el sprite pequeño; ranuras fijas; objetos como íconos, no sprites animados |
| Legal: azar y público | Sección 5 y [11](11-legal-y-cumplimiento.md); ⏳ F6-13 |
| Alcance: 45 edificaciones en total | Cada versión se corta sola; V2.1 y V2.2 son recortables sin tocar la historia |
| «Zona» es ambigua | Zona es la del mapa; las de [02](02-extraccion.md) son zonas de minado |

---

## 10 · Pendiente

- ✅ Precios de casas, vehículos, ropa y yate, impuesto predial y recargo por saqueo: fijados en [28](28-numeros-base-de-la-economia.md). Los de bote, pesquero y barcaza ⏳ F6-63.
- ⏳ F4-109 Qué escalón pide cada traje.
- ⏳ F4-110, ⏳ F4-111 y ⏳ F4-112 Casa, ropa y auto de V1; ⏳ F4-119 la pantalla donde se compran.
- ⏳ F4-154 Cómo se ve el viaje entre zonas (su costo en dinero ya está fijado ✅); ⏳ F6-57 efecto funcional de los vehículos de V2.1 y ⏳ F6-63 el de las embarcaciones.
- ⏳ F6-13 y ⏳ F6-14 Clasificación por edad y juego responsable del casino.
- ⏳ F1-20 Inglés de los términos nuevos del glosario ([18](18-biblia-narrativa.md)).
- Siguen 🟡 hasta que el autor las revise: las horas, el número exacto de edificaciones por zona, las ranuras exactas y los objetos de decoración, los vehículos por zona, los efectos de los bonos y la ubicación de la Lotería.

### Tareas creadas

Ya están en el roadmap, cada una de 20 h o menos. La columna ID dice cuál es; la última se partió en dos para no pasar de 20 h.

| ID | Nombre | Fase | Horas | Descripción |
|---|---|---|---|---|
| F0-83 | Registro de zonas y edificaciones en `world.json`, con su validación en el hub | F0, hito F0.12 | 6 | Seis asentamientos y las 45 edificaciones con ID, rol, versión y enlaces a minerales, recetas y facciones; el build comprueba que todo exista |
| F3-46 | Navegador zona a edificación y horarios por bloque | F3 | 6 | Lista de edificaciones de Villa Brasa en el MVP con apertura por bloque |
| F4-217 | Vista de zona: Villa Brasa, Altafría y Salinas Blancas | F4 | 12 | Los tres asentamientos isométricos con edificaciones tocables |
| F4-218 | Vista de zona: campamentos de las Cavernas y de la Fosa | F4 | 6 | Los dos campamentos |
| F4-219 | Herrería y economato | F4 | 16 | Exterior, interior y mercancía |
| F4-220 | Platería y lonja con almacén de salitre | F4 | 16 | Exterior, interior y mercancía |
| F4-221 | Tasadores y Casa Ormeño | F4 | 16 | Exterior, interior y mercancía |
| F4-222 | Edificios de historia: taller de ensayo, estación y pensión | F4 | 15 | Exterior, interior y el sitio de cada cinta |
| F4-223 | Edificios de historia: campamento de ensayo, campamento de la Primera Expedición y barracón | F4 | 15 | Exterior, interior y el sitio de cada cinta |
| F4-224 | Casa de Reme y oficina de Quiroga definitivas | F4 | 8 | Exterior e interior |
| F4-225 | Mostrador de preparación en las seis bocas de mina | F4 | 10 | Equipo propio de cada zona |
| F4-226 | Ranuras de decoración de la casa base | F4, hito F4.7 (antes de F4-110) | 8 | Cinco ranuras fijas con un objeto inicial |
| F6-46 | Lotería del Ministerio | F6, hito F6.1 | 12 | Sorteo semanal, ventanilla y publicación en el Heraldo |
| F6-47 | Inmobiliaria y compra de casas | F6, hito nuevo V2.1 | 14 | Comprar, vender y elegir la casa base |
| F6-48 | Chalet de Altafría y caserón de Salinas Blancas | F6, V2.1 | 18 | Exterior e interior de las dos casas |
| F6-49 | Mansiones del Paseo Marítimo y de la Colina de la Bolsa | F6, V2.1 | 20 | Dos mansiones con vista propia |
| F6-50 | Mansión del Barrio Alto | F6, V2.1 | 12 | La tercera, con vista al jardín |
| F6-51 | Decoración: objetos de Hollín, Altafría y Salinas Blancas | F6, V2.1 | 20 | Unos 15 objetos para las cinco ranuras |
| F6-52 | Decoración: objetos de Cavernas y Puerto Meridiano | F6, V2.1 | 20 | Unos 15 objetos más |
| F6-53 | Impuesto predial y saqueo de casas | F6, V2.1 | 14 | Sumidero, riesgo y balance |
| F6-54 | Joyería comprable: dueño, compra y precio | F6, V2.1 | 16 | El joyero, la compra del negocio y su historia breve |
| F6-55 | Joyería comprable: banco de trabajo y clientela | F6, V2.1 | 18 | Cincelado, Regateo y empleados |
| F6-56 | Joyas por zona: taller de talla y mostrador sin sello | F6, V2.1 | 20 | Las dos joyerías de zona |
| F6-57 | Concesionaria y vehículos | F6, V2.1 | 20 | Carreta, camioneta y automóvil |
| F6-58 | Sastrería y ropa cosmética | F6, V2.1 | 20 | Trajes y cosméticos del sprite pequeño |
| F6-59 | Textos ES/EN de V2.1 | F6, V2.1 | 14 | Todo lo anterior en los dos idiomas |
| F6-60 | Pruebas de V2.1 | F6, V2.1 | 12 | Casos y regresión |
| F6-61 | Reserva de V2.1 | F6, V2.1 | 12 | Correcciones |
| F6-62 | Pesca: muelle, peces y variante del Cribado | F6, hito nuevo V2.2 | 20 | Pesca con el motor del Cribado |
| F6-63 | Astillero y embarcaciones | F6, V2.2 | 20 | Bote, pesquero y barcaza |
| F6-64 | Puerto deportivo y yate | F6, V2.2 | 14 | Solo estatus |
| F6-65 | Inversiones en la Bolsa: sectores, spread y tope | F6, V2.2 | 20 | Agricultura, tecnología y pesca |
| F6-66 | Inversiones: noticias de sector y balance | F6, V2.2 | 14 | Con el simulador de mercado |
| F6-67 | Pesca: precios, lonja y balance | F6, V2.2 | 10 | Pescado como mercancía |
| F6-68 | Textos ES/EN de V2.2 | F6, V2.2 | 8 | Todo lo anterior en los dos idiomas |
| F6-69 y F6-70 | Pruebas y reserva de V2.2 | F6, V2.2 | 24 | Casos, regresión y correcciones |

Las tareas F4-217 a F4-226 suman **+122 h en F4**, dentro de las +110 a 150 h de V1; con F3-46 (6 h) son 128 h, también dentro. Las F6-47 a F6-61 suman 250 h (V2.1) y las F6-62 a F6-70, 130 h (V2.2).
