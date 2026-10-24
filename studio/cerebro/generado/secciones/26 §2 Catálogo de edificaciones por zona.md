---
id: "doc-26-s02"
tipo: "seccion"
title: "2 · Catálogo de edificaciones por zona ✅"
aliases: ["doc-26-s02"]
documento: "[[26 Zonas y edificios]]"
limpieza: 100
abiertos: 0
espera: 5
aplazado_a: ["[[F4-166 Bolsa - interfaz]]", "[[F4-219 Herrería y economato]]", "[[F4-55 Tasar piezas - detectar falsas]]", "[[F6-46 Lotería del Ministerio]]", "[[F6-47 Inmobiliaria y compra de casas]]"]
estado: "con-aplazados"
anterior: "[[26 §1 Estructura - mapa, zona y edificación]]"
siguiente: "[[26 §3 Joyerías y joyas por zona]]"
arriba: "[[26 Zonas y edificios]]"
fuente: "studio/docs/26-zonas-y-edificios.md:43"
generado: true
---

# 2 · Catálogo de edificaciones por zona ✅

> El detalle de la mercancía exacta de cada edificación se fija al hacerla: F4-219 a F4-225 en V1 y F6-47 a F6-58 en V2.

← [[26 §1 Estructura - mapa, zona y edificación]] · [[26 Zonas y edificios|↑ 26]] · [[26 §3 Joyerías y joyas por zona]] →

El detalle de la mercancía exacta de cada edificación se fija al hacerla: ⏳ [[F4-219 Herrería y economato|F4-219]] a [[F4-225 Mostrador de preparación en las seis bocas de mina|F4-225]] en V1 y ⏳ [[F6-47 Inmobiliaria y compra de casas|F6-47]] a [[F6-58 Sastrería y ropa cosmética|F6-58]] en V2.

**Roles.** *Comprar* y *vender* (el jugador compra o vende), *ganar* (ingresos que no son una venta: contratos, sueldos, premios), *gastar* (cuotas, impuestos, mantenimiento, estilo de vida), *minijuego* (se juega uno de [[09 Minijuegos|09]]) e *historia* (sitio de misión o de cinta, [[23 Árbol de decisiones y consecuencias|23]], sección 7). **Versiones:** MVP, V1, V2.0, V2.1, V2.2 y evolutivo (sección 7). **ID:** `ed-<zona>-<nombre>`, con `vb` Villa Brasa, `af` Altafría, `sb` Salinas Blancas, `cv` Cavernas, `fo` Fosa y `pm` Puerto Meridiano.

Cada boca de mina lleva además el **mostrador de preparación** de su zona (loadout de [[02 Extracción|02]]): máscara y refuerzos en el Hollín, equipo para frío y altitud en Altafría, agua y protección en los Salares, y filtros en la Fosa. No cuenta como edificación aparte.

### 2.1 Cuenca del Hollín: Villa Brasa

Obrero y humo; manda la Unión. La herrería alimenta el Acero y la tienda atiende a clientes obreros.

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| [[Tienda de Villa Brasa\|ed-vb-tienda]] | Tienda (el puesto reabierto) | vender, comprar, minijuego (Regateo, Reponer) | Mercancía de carbón y hierro; clientes obreros; la cinta 1 está en el doble fondo de la caja | MVP | ✅ |
| [[Taller de Villa Brasa\|ed-vb-taller]] | Taller | ganar (valor agregado), minijuego (Refinado) | Acero (hierro y carbón). Se construye en el MVP y **se abre en el Acto II**; el Acto I no lo usa ✅ | MVP | ✅ |
| [[Almacén de Villa Brasa\|ed-vb-almacen]] | Almacén | gastar (alquiler y costo de guardar) | Donde la especulación cuesta de verdad ([[03 Comercio y mercado\|03]]) | MVP | ✅ |
| [[Casa obrera\|ed-vb-casa]] | Casa obrera (casa base) | gastar | Chimeneas y humo en la vista; descanso y decoración (sección 4) | MVP; mejorable en V1 | ✅ |
| [[Casa de Reme\|ed-vb-reme]] | Casa de Reme | gastar (cuotas de la deuda) | Reme, la prestamista; su facción cambia según la partida ([[22 Acto II - las tres variantes de Reme\|22]]) | MVP | ✅ |
| [[Oficina del Inspector\|ed-vb-quiroga]] | Oficina del Inspector | gastar (licencias, multas, «trámites») | Quiroga; baja o sube la vigilancia ([[03 Comercio y mercado\|03]]) | MVP | ✅ |
| [[Boca de las Galerías del Hollín\|ed-vb-mina-galerias]] | Boca de las Galerías del Hollín | minijuego (Picado y Perforación; la Detonación, con el explosivo, desde el Acto III y no en el MVP) | Carbón principal; Teo enseña el oficio. El Picado sirve para carbón, hierro, cobre, plata y oro ✅ ([[09 Minijuegos\|09]]); aquí se pica carbón y hierro. En la boca está la placa de Pozo Negro, prop fijo del Acto I ([[27 Guion del Acto I, día a día\|27]], [[d3.2 La placa\|d3.2]]; [[21 Pasado de Valdoria y de la Aetherita\|21]]) | MVP | ✅ |
| [[Boca del Cañón Ferroso\|ed-vb-mina-canon]] | Boca del Cañón Ferroso | minijuego (Picado, Perforación) | Hierro principal, con algo de cobre; bandas rivales. El Picado sirve para carbón, hierro, cobre, plata y oro ✅ ([[09 Minijuegos\|09]]), así que también pica el cobre | V1 | ✅ |
| [[Sede de la Unión\|ed-vb-union]] | Sede de la Unión | ganar (Bolsa de la Unión: contratar), gastar | Medidor de la Unión, huelgas, Delegado de la Unión | V1 | ✅ |
| [[Quiosco y redacción de La Voz del Hollín\|ed-vb-periodico]] | Quiosco y redacción de La Voz del Hollín | comprar (prensa, anuncios), ganar (empleos) | Sesgo sindical; vende también el Heraldo y el Teletipo; Lucía y el voceador pasan por aquí | V1 | ✅ |
| [[Herrería-chatarrería\|ed-vb-herreria]] | Herrería-chatarrería | comprar, vender | Hierro, carbón y repuestos de herramientas; su hierro y su carbón alimentan el Acero del taller | V1 | ✅ |

### 2.2 Sierra Alta: Altafría

Frío y Consorcio. La plata que se afina aquí la compra después Casa Ormeño.

**Cumbre Clara no es un edificio ✅.** El Sanatorio de Cumbre Clara, donde murió Anselmo en público, es solo un nombre (decisión del autor, 2026-10-13): no es zona ni edificación de este catálogo y no se visita ([[21 Pasado de Valdoria y de la Aetherita|21]]).

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| [[Boca de las Minas de Sierra Alta\|ed-af-mina]] | Boca de las Minas de Sierra Alta | minijuego (Picado, Perforación, Cribado) | Cobre y plata principales (el Picado sirve para cobre, plata y oro ✅, [[09 Minijuegos\|09]]); frío y falta de aire; guardias de empresa | V1 | ✅ |
| [[Oficina del Consorcio Arvel\|ed-af-consorcio]] | Oficina del Consorcio Arvel | ganar (contratos del Consorcio) | Esteban Arvel; ejecutivos y capataces | V1 | ✅ |
| [[Economato del Consorcio\|ed-af-economato]] | Economato del Consorcio | comprar | Abrigo y vales de empresa: se paga al precio del Consorcio | V1 | ✅ |
| [[Fundición-platería\|ed-af-plateria]] | Fundición-platería | vender (plata), comprar (lingote de plata) | Afina la plata de la sierra; sus joyas de plata llegan con las gemas (sección 3) | V1 | ✅ |
| [[Viejo taller de ensayo\|ed-af-taller-ensayo]] | Viejo taller de ensayo | historia | Casillero con la cinta 2 | V1 | ✅ |
| [[Chalet de la cordillera\|ed-af-chalet]] | Chalet de la cordillera | gastar (casa comprable) | Vista a la cordillera (sección 4) | V2.1 | ✅ |

### 2.3 Salares del Litoral: Salinas Blancas

Faroleros y contrabando. El salitre enlaza con la agricultura y la pólvora.

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| [[Boca de los Salares del Litoral\|ed-sb-mina]] | Boca de los Salares del Litoral | minijuego (Cribado) | Salitre principal; sed y gases; contrabandistas e inspectores corruptos | V1 | ✅ |
| [[Lonja y almacén de salitre\|ed-sb-lonja]] | Lonja y almacén de salitre | vender, comprar | Salitre para agricultura y pólvora; más adelante, el pescado | V1 | ✅ |
| [[Bar del Farol\|ed-sb-bar]] | Bar del Farol (Los Faroleros) | comprar y vender en el mercado negro, ganar | Casilda; abre de noche; contacto del mercado negro: en el III compras aquí la Aetherita y en el IV recibes sus encargos especiales, raros y con historia (la venta rutinaria va a la Comisión) (también hay una visita nocturna de Casilda a la tienda, que no es el modo tienda); joyas sin sello (sección 3) | V1 | ✅ |
| [[Caserón frente al mar\|ed-sb-caseron]] | Caserón frente al mar | gastar (casa comprable) | Mar abierto (sección 4) | V2.1 | ✅ |
| [[Muelle de pesca\|ed-sb-muelle]] | Muelle de pesca | minijuego (pesca), vender | Pesca con el motor del Cribado | V2.2 | ✅ |
| [[Astillero\|ed-sb-astillero]] | Astillero | comprar (embarcaciones), gastar | Bote, pesquero y barcaza | V2.2 | ✅ |
| [[Aduana\|ed-sb-aduana]] | Aduana | gastar (impuestos de puerto) | Aduanero Mayor; de momento los impuestos van por pantalla | evolutivo | ✅ |

El bar está en Salinas Blancas porque los Faroleros nacieron como gremio de los faroles de los puertos ([[21 Pasado de Valdoria y de la Aetherita|21]]).

### 2.4 Cavernas de Cristal: campamento

Gemas en zona disputada; sin vivienda.

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| [[Boca de las Cavernas de Cristal\|ed-cv-mina]] | Boca de las Cavernas de Cristal | minijuego (Picado, Cincelado, Perforación, Cribado) | Oro, cuarzo y esmeralda principales; cristales cortantes; cazarrecompensas; siempre abierta, expedición de 2 bloques (Tarde y Noche) ✅ | V1 | ✅ |
| [[Tasadores\|ed-cv-tasadores]] | Tasadores | vender (gemas), minijuego (Tasar) | Tasan esmeralda, diamante y cuarzo; hay piezas falsas (⏳ [[F4-55 Tasar piezas - detectar falsas\|F4-55]]) | V1 | ✅ |
| [[Campamento de ensayo\|ed-cv-campamento]] | Campamento de ensayo | historia | Cinta 4, bajo el cuarzo | V1 | ✅ |
| [[Taller de talla\|ed-cv-taller-talla]] | Taller de talla | minijuego (Cincelado), vender | Joyas de gema tallada (sección 3) | V2.1 | ✅ |

### 2.5 La Fosa: campamento de la Comisión

Sin vivienda, lujo ni azar. Solo historia y la boca de mina.

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| [[Boca de La Fosa del Éter\|ed-fo-mina]] | Boca de La Fosa del Éter | minijuego (Contención, Cincelado) | Aetherita y diamante principales; mostrador de filtros (los filtros de la Comisión que exige la Aetherita; cifras en [[28 Números base de la economía\|28]]); solo abre 3 días por semana, los de calibración de la Comisión ✅ (los días 2, 4 y 6 de cada semana) | V1 | ✅ |
| [[Campamento de la Primera Expedición\|ed-fo-campamento-viejo]] | Campamento de la Primera Expedición | historia | Cinta 6, en la caja del equipo de ensayo | V1 | ✅ |
| [[Barracón de calibración\|ed-fo-barracon]] | Barracón de calibración | historia | Cintas 7 y 8 y el acta de calibración | V1 | ✅ |

### 2.6 Puerto Meridiano

Lujo, prensa y modas de la esmeralda. Llega en el Acto III.

| ID | Edificación | Rol | Qué la hace de su zona | Versión | Marca |
|---|---|---|---|---|---|
| [[La Bolsa\|ed-pm-bolsa]] | La Bolsa | comprar, vender (mercado spot) | Interfaz del mercado ([[03 Comercio y mercado\|03]], ⏳ [[F4-166 Bolsa - interfaz\|F4-166]]); pestaña de inversiones en V2.2 | V1 | ✅ |
| [[Sede del Ministerio de Recursos\|ed-pm-ministerio]] | Sede del Ministerio de Recursos | gastar (licencias mayores, impuestos), ganar (contratos oficiales) | Montenegro; la ventanilla de la Lotería en V2.0 (ubicación ⏳ [[F6-46 Lotería del Ministerio\|F6-46]], sección 5) | V1 | ✅ |
| [[Casa Ormeño\|ed-pm-casa-ormeno]] | Casa Ormeño (tienda insignia) | vender (plata, joyas), comprar (piezas de lujo) | Joyería de plata para la élite; sin dueño ni medidor | V1 | ✅ |
| [[Oficina de la Comisión del Éter\|ed-pm-comision]] | Oficina de la Comisión del Éter | vender (Aetherita) | Canal legal del Acto IV: la Comisión compra la Aetherita a valor justo, con tope diario; siempre abierta, pero hay que ir a la capital a vender ✅ ([[28 Números base de la economía\|28]]) | V1 | ✅ |
| [[Estación\|ed-pm-estacion]] | Estación | historia | Consigna con la cinta 3 | V1 | ✅ |
| [[Pensión\|ed-pm-pension]] | Pensión | historia | Cinta 5, donde Anselmo se alojaba al entregar sus informes | V1 | ✅ |
| [[Salón del Farol\|ed-pm-salon]] | Salón del Farol | ganar y gastar (azar), minijuego | Casino de noche de Los Faroleros (sección 5) | V2.0 | ✅ |
| [[Inmobiliaria\|ed-pm-inmobiliaria]] | Inmobiliaria | comprar (casas y mansiones) | Lista las propiedades de todas las zonas | V2.1 | ✅ |
| [[Mansión del Paseo Marítimo\|ed-pm-mansion-paseo]] | Mansión del Paseo Marítimo | gastar | Vista al mar | V2.1 | ✅ |
| [[Mansión de la Colina de la Bolsa\|ed-pm-mansion-colina]] | Mansión de la Colina de la Bolsa | gastar | Vista a la ciudad | V2.1 | ✅ |
| [[Mansión del Barrio Alto\|ed-pm-mansion-barrio]] | Mansión del Barrio Alto | gastar | Vista a un jardín | V2.1 | ✅ |
| [[Joyería del dueño\|ed-pm-joyeria]] | Joyería del dueño | comprar el negocio, ganar, minijuego | La joyería que compras y atiendes (sección 3.3) | V2.1 | ✅ |
| [[Concesionaria\|ed-pm-concesionaria]] | Concesionaria | comprar (vehículos) | Automóviles, camionetas y carretas | V2.1 | ✅ |
| [[Sastrería\|ed-pm-sastreria]] | Sastrería | comprar (ropa) | Un traje por escalón de estatus y ropa cosmética | V2.1 | ✅ |
| [[Puerto deportivo\|ed-pm-puerto-deportivo]] | Puerto deportivo | comprar (yate), gastar | El yate, solo estatus | V2.2 | ✅ |

**Cuenta.** El catálogo tiene 46 filas: las **45 edificaciones** de MVP, V1 y V2 y, además, la aduana de Salinas Blancas, que es evolutivo y **no entra en las 45**. La oficina de la Comisión del Éter ([[Oficina de la Comisión del Éter|ed-pm-comision]], Puerto Meridiano) es la que se añadió el 2026-10-16 ✅.

**Edificaciones que se dejan fuera por ahora (evolutivo):** la aduana de Salinas Blancas (la única con fila, para reservar su ID), las redacciones del Heraldo y del Teletipo (hoy se compran en el quiosco), un tablón de cazarrecompensas en las Cavernas y una oficina del Consorcio en la capital. Ninguna es necesaria para la historia ni para el mercado.

---

## Fuente

`studio/docs/26-zonas-y-edificios.md:43`
