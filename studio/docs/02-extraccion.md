# 02 · Extracción

## Zonas ✅

✅ Cada zona tiene características propias: qué minerales aparecen y con qué probabilidad, qué peligros tiene y su nivel de dificultad. El jugador debe decidir a cuál ir y ser consciente de los riesgos.

✅ Los minerales son más probables en unas zonas que en otras.

✅ Desbloqueo **por etapas**; cuando el jugador las tiene todas, puede moverse con libertad según su necesidad.

✅ Recursos **limitados** por zona, con **reactivaciones/regeneración** cada cierto tiempo.

✅ La versión 1 trae **6 zonas** (la tabla de abajo). Cada mineral aparece en **más de una zona** (en 2 o 3, como muestra [05](05-mundo-y-minerales.md)) y con probabilidades distintas, de modo que no exista una «zona óptima» fija.

✅ **Excepciones a esa regla (decisión del autor, 2026-10-15):** el **salitre** y la **Aetherita** aparecen en una sola zona porque están ligados a la historia. El salitre es de los Salares del Litoral, y la Aetherita solo sale de La Fosa del Éter, por canon.

### Ficha de zona (plantilla) ✅

```
Nombre:
Nivel de peligro (visible):
Minerales y probabilidades base:
Peligros ambientales:
Enemigos / criaturas:
Requisito de desbloqueo:
Ciclo de regeneración:
Lore:
```

### Zonas de la versión completa ✅ (6, desbloqueo en este orden)

| # | Zona | Región | Peligros | Quién molesta | Jefe de zona ✅ |
|---|---|---|---|---|---|
| 1 | Galerías del Hollín | Cuenca del Hollín | Gas, polvo, derrumbes | Capataces, saqueadores | Capataz Mayor |
| 2 | Cañón Ferroso | Cuenca del Hollín | Calor, desprendimientos | Rivales, bandas | Cabecilla de la banda rival |
| 3 | Minas de Sierra Alta | Sierra Alta | Frío, altitud, falta de aire | Guardias de empresa | Jefe de seguridad del Consorcio |
| 4 | Salares del Litoral | Salares del Litoral | Sed, calor, gases | Contrabandistas, inspectores corruptos | Aduanero Mayor |
| 5 | Cavernas de Cristal | Cavernas de Cristal | Cristales cortantes, desorientación | Cazarrecompensas | Cazarrecompensas Mayor |
| 6 | La Fosa del Éter | La Fosa | Radiación de éter, inestabilidad | Militares, criaturas mutadas | Coronel de la Comisión |

✅ Las zonas están ambientadas en Valdoria (ver [05](05-mundo-y-minerales.md) para regiones y distribución de minerales).

✅ Estas seis son **zonas de minado**: cada una se entra por la boca de mina de un asentamiento (Villa Brasa atiende las dos del Hollín). En el mapa, «zona» es la región completa con su asentamiento ([26](26-zonas-y-edificios.md)). Ir de una a otra se hace en **tren**: no gasta bloque y el billete es el costo del viaje (de 42 a 210 esquirlas por trayecto ✅; [01](01-core-loop.md), [28](28-numeros-base-de-la-economia.md)). Las **Cavernas** y **La Fosa** son zonas profundas: una expedición cuesta 2 bloques y ocupa la Tarde y la Noche, y La Fosa solo abre 3 días por semana, los días 2, 4 y 6 ✅ ([01](01-core-loop.md)).

✅ Los «enemigos» de las primeras zonas son **personas** (capataces, bandas, inspectores que piden soborno), no monstruos, como muestra la tabla. Encaja con el tono y con los encuentros por decisión (pagar, negociar, pelear, huir). Las criaturas aparecen solo en La Fosa, por la Aetherita.

✅ **Los jefes de zona son opcionales, no una puerta:** ni el desbloqueo de zonas ni el cierre de un acto exigen vencerlos ([24](24-umbrales-de-acto.md)). El duelo de cada jefe ⏳ F4-54.

- ⏳ F2-10 Ficha completa de las Galerías del Hollín, la zona 1, con la plantilla de arriba.
- ⏳ F4-02 · F4-07 · F4-12 · F4-17 · F4-22 Fichas completas de las zonas 2 a 6, en ese orden.

## Menas y detector de probabilidades ✅

✅ Cada mena tiene una composición con probabilidades (ej. 30 % oro, 3 % diamante, 50 % carbón). Cambio de diseño del autor (2026-10-24, F0-91): el **detector** ya no es un escáner instantáneo del mapa, sino una herramienta que se usa **dentro de la mina**, con **batería** (ver «La mina por dentro»): un clic en una mena gasta 1 carga y muestra los rangos de composición con su promedio y los de cantidad, y el jugador decide si le conviene picarla o buscar otra.

✅ El detector muestra **rangos** (ej. «oro: 20–40 %») y no valores exactos; el rango va desplazado respecto al valor real para que el promedio no delate la verdad. El **Ojo** y el nivel del detector determinan qué tan estrechos son ([04](04-progresion-y-meta.md), [09](09-minijuegos.md)); la precisión mejora con mejores detectores → la información es progresión.

✅ El protagonista empieza con un **detector básico heredado de Anselmo**. No depende del cuarzo: el cuarzo solo lo mejora más adelante.

✅ Las probabilidades de aparición y obtención se calibran para que no sea fácil ganar mucho dinero rápido ni terminar el juego pronto.

- ✅ **Energía:** el **Aguante base es de 28** (decisión del autor, 2026-10-16: sube de 25 porque con 25 el jugador medio no pagaba la primera cuota con margen) y es la energía máxima de **cada expedición**: se rellena entera al empezar, y una casa mejor sube un poco la energía inicial (+2 por nivel de casa). Cada mena gasta energía según su mineral: carbón 8 · hierro 10 · cobre 12 · salitre 12 · plata 14 · cuarzo 16 · oro 18 · esmeralda 22 · diamante 26 · Aetherita 34 (cada nivel de herramienta la baja un 10 % del valor base, hasta ×0,6 en el nivel 5).
- ✅ **No hay descarte con costo de energía** (decisión del autor, 2026-10-24; sustituye la del 2026-10-15, que cobraba el 25 % de la energía de la mena): lo que cuesta mirar una mena es la **carga de la batería** del detector. Caminar por la mina no gasta Aguante ni bloque. El Aguante 28 se mantiene y deja de repartirse entre extraer y descartar; la regla C5b del simulador mide la carga del detector (F0-92 ✅; C5 sigue midiendo el modelo sin entradas; [28](28-numeros-base-de-la-economia.md), sección 4).
- ✅ **Menas por expedición:** variable según tus skills, herramientas y mejoras. Al principio caben **2 a 3** (con 28 de energía, 3 de carbón o 2 de hierro) y el número crece con la recolección: unas 4 en el Acto II, 7 en el III y hasta 10 por bloque en el IV. Los empleados rinden mucho menos que tú, pero escalan igual con sus skills ([04](04-progresion-y-meta.md)).
- ✅ **Expedición profunda:** gasta **×1,8 de energía** y permite **×1,5 de carga**.
- ✅ **Consumibles de recarga de energía** y similares: versiones futuras, mucho después de la V1 ([06](06-roadmap-y-pendientes.md)).
- ✅ **Minas que se agotan:** cada visita baja la riqueza de la mina 6 puntos, cada día sube 3 y nunca baja del 40 %, así que rotar de mina rinde más que repetir una. La riqueza es **de la mina, no de la entrada** y multiplica las unidades; el cambio de entrada no cuenta como otra visita ([28](28-numeros-base-de-la-economia.md)).

## La mina por dentro ✅

Cambio de diseño del autor (2026-10-24, F0-91, modelo «Galería del día»). Las cifras las calibró F0-92 con el simulador y el autor las aprobó el 2026-10-24 ✅ ([28](28-numeros-base-de-la-economia.md), «Entradas, batería y cierres»).

### Recinto de 5 entradas ✅

- La **boca de mina** es una edificación del asentamiento. Al entrar hay un **recinto con cinco entradas**: **2 de recursos escasos, 2 medios y 1 abundante**. El reparto (cuál es cuál) se sortea **cada día y a ciegas**: no se ve antes de entrar. Semilla determinista `hash(partida, día, mina, entrada)`.
- Cada entrada es una **galería caminable de 2 a 3 pantallas** en **vista aérea cenital** (tipo Stardew; la vista lateral plana queda solo para los interiores de edificios). El jugador camina hasta las menas y no gasta Aguante ni bloque por caminar.
- **Calidad de la entrada: solo cantidades** (unidades por mena): escasa ×0,78, media ×1,0, abundante ×1,44 ✅ (antes ×0,7 · ×1,0 · ×1,6). En el Acto I el abanico es estrecho (0,85 · 1,0 · 1,3) para no romper la cuota. **No cambia la mezcla de minerales** de la zona. Los rendimientos base bajan un 15 % en todos los actos (`base_yield_mult` 0,85 ✅), porque quien escanea y cambia de entrada gana ≈ +8 % por la entrada y ≈ +13 % por elegir las menas de más cantidad.
- **Cambio de entrada: una sola vez por mina y por día**, dentro del mismo bloque y con el mismo Aguante; no cuenta como otra visita para el agotamiento. Si no te gusta la primera, entras en otra (con suerte distinta), pero ya habrás gastado detector y batería en la primera. Las demás visitas del día vuelven a «tu entrada del día».
- Se ven **el doble de menas de las que puedes picar**: Acto I 5–6, II 8, III 14, IV 18 menas visibles.

### Detector con batería ✅

- Un clic en una mena gasta **1 carga** y muestra el rango de composición con marca de promedio, el rango de cantidad y un **color**: gris (tu herramienta no puede picarla), ámbar o verde.
- **Batería de 12 · 17 · 25 · 32 cargas ✅ (calibrado en F0-92)** según el nivel del detector (1 a 4). Con 0 carga picas **a ciegas**: la roca solo insinúa el tier.
- **Sonar (detector de nivel 2):** colorea cada cámara de la galería en frío, tibio o caliente según lo que hay en ella.
- **Recarga:** entera y gratis cada noche, al pasar el día; no se liga a la casa (la casa ya da +2 de Aguante). **Pilas de repuesto** opcionales desde el Acto II, máximo 1 al día, como sumidero de dinero.
- **Herramienta en consonancia:** el desgaste actual se mantiene; por debajo del 20 % de integridad la herramienta queda **mellada** (margen del minijuego −30 %). Son tres límites a la vez (Aguante, batería, desgaste): al principio es complicado y con mejoras se vuelve más fácil; el simulador vigila que no frustre (✅ J3: la batería se queda corta ≈ 45 % de los días normales y ≈ 56 % de los de nieve).

### Cierres de entradas ✅

- Los problemas sociales o políticos que afectan a un mineral cierran entradas **de esa mina** ([07](07-sociedad-y-eventos.md), «Severidad y cierres»): suave = 1 entrada cerrada, complicado = 2, situación complicada en Valdoria = 3. **Siempre quedan al menos 2 abiertas.**
- **Orden de cierre:** primero la abundante, luego una media y de tercero una escasa (con 3 cierres quedan 1 media y 1 escasa).
- **Alcance:** un evento puede afectar a una o varias minas de distintos minerales: gravedad entera donde el mineral es el principal de la mina, un nivel menos donde es secundario (≥ 25 % de la mezcla), nada si es menor. Con dos eventos en la misma mina, el mayor +1, tope 3.
- **Presión** (más mineros en menos galerías): unidades de las entradas abiertas ×0,95 con 1 cierre, ×0,88 con 2 y ×0,75 con 3, para que más cierres rindan siempre menos.
- **Cuándo rigen:** al empezar el día, con aviso previo, nunca con el jugador dentro; un evento de guion a mitad de día rige desde el bloque siguiente. Si cierra tu entrada del día, se te reasigna gratis sin gastar el cambio. Se ve el cierre (piquete, precinto o soldados) con una frase del diario.
- **Reapertura:** al terminar el evento reabre una entrada por día, en orden inverso (escasa → media → abundante). **Sin cierres en el Acto I.**
- **Empleados:** sufren lo mismo; entran por una entrada abierta al azar, sin detector, y rinden la media de las abiertas.
- **Cierre total:** solo como **excepción de guion** cuando la historia lo amerite (la huelga del Acto II que cierra el Cañón Ferroso, [22](22-acto-ii-variantes.md)); no es un cierre por gravedad.
- **Guardado:** solo en puntos seguros (calle, casa, andén); no dentro de una mina.

## Herramientas ✅

✅ Estilo Minecraft:

- Las herramientas **se desgastan** con el uso.
- Cada herramienta sirve para ciertos materiales; los materiales de mayor nivel requieren herramientas mejores.
- Mejor herramienta → minijuego más fácil / zona óptima más amplia / más probabilidad de obtención.

✅ **Los niveles de herramienta por acto son una guía, no un tope** (decisión del autor, 2026-10-15): Acto I 1–2 · II 2–3 · III 3–4 · IV 4–5 indican el nivel con el que se espera llegar a cada acto; si un jugador compra antes un nivel que se lo puede permitir, puede. Si el simulador (F0-53) ve que el optimizador llega demasiado pronto a un nivel, propone subir el costo de ese nivel y el autor decide.

✅ Lo que mejora el jugador al ir comprando: más resistencia, más almacenamiento (carga), mejor minado, mejor información (detector). Son los cuatro componentes de **cada nivel**: un nivel de herramienta es un paquete que mejora las cuatro cosas a la vez, no cuatro escaleras separadas ✅.

### Modelo de herramientas ✅

Decisión del autor (2026-10-15):

| Pieza | Regla |
|---|---|
| Tipos | **5 tipos**: pico, taladro, cincel, criba y explosivo (los de [09](09-minijuegos.md)); cada uno cubre un tipo de minijuego ✅ |
| Niveles | **5 niveles por herramienta**, y los minerales de mayor nivel exigen herramientas de mayor nivel ✅ (a revisar si en el prototipo hace falta ampliar, ⏳ F4-60) |
| Explosivo | Es **consumible**: se gasta con cada uso en lugar de desgastarse ✅ |
| Reparar | Cuesta **dinero y materiales** ✅. Es otro sumidero de dinero. Los materiales son **1 repuesto por cada 20 puntos de desgaste**: de hierro en los niveles 1–2, de cobre en el 3, de plata en el 4 y de oro en el 5 ✅ |
| Mejorar | Requiere **minerales específicos** (ej. hierro para el pico, diamante para el cincel, cuarzo para mejorar el detector). Así los minerales tienen utilidad real ✅ |
| Qué mineral | El mineral que sube una herramienta al nivel *k* se extrae con una herramienta de nivel *k*−1 ✅. Así nunca hace falta lo que aún no se puede sacar |
| Facciones | Mejorar es **neutral entre facciones** ✅ |
| Requisitos | Los niveles altos requieren **estatus, licencia o contacto** (influencia), no solo dinero ✅ (⏳ F4-114 proveedores por estatus, ⏳ F4-213 licencias) |

- ✅ **Costo de mejorar** (un costo en dinero y un mineral por nivel; las cifras del pico, y los otros tipos cuestan ×1,1 la criba, ×1,25 el taladro y ×1,5 el cincel): subir al nivel 2 cuesta **480 esquirlas**, al 3 **1 100**, al 4 **13 000** y al 5 **40 000**, más el mineral de cada subida (3 hierro para el nivel 2, cobre para el 3, plata para el 4 y esmeralda para el 5 en el pico). La mejor mejora de cada nivel se paga en pocas expediciones: 1,0 en el nivel 2 (el pico a 480 se paga en 1,04), 3,4 en el 3, 7,1 en el 4 y 3,2 en el 5 ([28](28-numeros-base-de-la-economia.md) §5.2). El detalle por tipo y mineral está en [28](28-numeros-base-de-la-economia.md).
- ✅ **Costo de reparar:** dinero por punto de desgaste según el nivel (3 · 5 · 20 · 85 · 240 esquirlas, por el factor del tipo) más los repuestos de arriba; en total, **7–9 % del valor bruto de una expedición** en todos los actos.
- ✅ **Explosivo:** consumible con **5 potencias** (cada una sirve para los minerales de un nivel) que cuestan **15 · 50 · 130 · 330 · 900 esquirlas**; entra en el Acto III. El **detector** se mejora aparte con cuarzo ([28](28-numeros-base-de-la-economia.md)).

## Fallos y daño a la mena ✅

✅ Si el jugador falla el minijuego, puede **fallar** la extracción y también **dañar la mena** (menor rendimiento o pérdida).

✅ Cada minijuego tiene **4 resultados posibles**: perfecto, bueno, regular y fallo. El resultado modifica el rendimiento, el daño y el desgaste (tabla en [09](09-minijuegos.md)). Las cifras se calibran en el prototipo ⏳ F2-13.

## Minijuegos de extracción

✅ Varios tipos, simples, alineados con el juego. Inspiración: pesca de Stardew Valley (equilibrar **dos parámetros** hasta un punto óptimo, ej. fuerza vs. precisión) y minijuegos cortos tipo Among Us.

### Catálogo inicial ✅

**Estado:** los cinco minijuegos de extracción y su acto de entrada están confirmados en el registro del mundo (`world.json`), y que son de dos parámetros en tensión (con la excepción del Cincelado) lo está en [09](09-minijuegos.md). La mecánica fina de cada uno se fija al construirlo: ⏳ F2-14 y ⏳ F2-15 (Picado y Perforación), ⏳ F4-44 (Cincelado), ⏳ F4-46 (Cribado) y ⏳ F4-48 (Detonación).

| Minijuego | Mecánica | Parámetros |
|---|---|---|
| Picado | Timing de golpe | Fuerza ↔ precisión |
| Perforación | Mantener zona óptima | Velocidad ↔ calor (sobrecalentamiento) |
| Cincelado | Trazar líneas de corte | Precisión pura (gemas) ⏳ F4-44 |
| Cribado / lavado | Mantener flujo | Inclinación ↔ caudal (como la pesca) |
| Detonación | Colocar carga | Potencia ↔ ubicación (riesgo de dañar la mena) |

Cada tipo de mineral/dureza se asocia a un minijuego. Detalle completo, automatización y MVP: ver [09-minijuegos.md](09-minijuegos.md).

### Tareas de peligro (estilo Among Us) ✅

Para afrontar peligros ambientales: sellar una fuga de gas (secuencia), apuntalar un techo (patrón), reparar una herramienta (conectar piezas). Los nombres de las tres tareas están en el glosario ([18](18-biblia-narrativa.md)); su mecánica ⏳ F3-10 y ⏳ F4-53 ([09](09-minijuegos.md)).

## Peligros y enemigos ✅

**Estado:** los peligros por zona, que el jugador decide cómo afrontarlos y que los encuentros normales son eventos con decisión y sin minijuego están confirmados ([09](09-minijuegos.md), «Encuentros»; ⏳ F3-09). Los eventos concretos de cada zona ⏳ F3-09, ⏳ F4-05, ⏳ F4-10, ⏳ F4-15, ⏳ F4-20 y ⏳ F4-25.

✅ **Peligros ambientales** por zona. Algunos enemigos o criaturas. El jugador decide: **retirarse, pelear o armar una estrategia** según la situación.

### Encuentros por eventos ✅

- Aparece una ilustración + texto con la situación.
- Opciones: pelear, huir, sobornar/negociar, soltar parte de la carga, usar un objeto ✅ (las cuatro primeras son las de F3-09; los objetos para asegurar la carga o escapar están en «Pérdida», más abajo).
- Las estadísticas y el equipo determinan las probabilidades (**Temple** para la defensa y **Labia** para negociar y sobornar, [04](04-progresion-y-meta.md)); el jugador las ve antes de decidir ✅ (criterio de cierre de F3-09).
- Los jefes son opcionales (arriba) y su encuentro es un minijuego corto de timing ⏳ F4-54.
- Cada zona tiene un **nivel de peligro visible** antes de entrar.

### Preparación (loadout) ✅

Antes de salir, el jugador elige equipo según los peligros de la zona (máscara para gas, refuerzos, armas, objetos de escape). Se hace en el **mostrador de preparación** de cada boca de mina ✅ ([26](26-zonas-y-edificios.md)).

## Pérdida ✅

Decisión del autor (2026-10-15):

- ✅ **Energía en 0 durante una expedición:** vuelves con **carga parcial**. Solo se pierde la carga de **esa** expedición, nunca lo que ya está en el almacén.
- ✅ La pérdida es **parcial**, no total, con objetos para asegurar la carga o escapar ⏳ F3-09. Perderlo todo por un solo error de preparación frustraría demasiado; el castigo duro queda para las dificultades altas y el hardcore.
- ✅ **El día 3 del Acto I todavía no hay pérdida grave**, en ninguna dificultad ([27](27-guion-del-acto-i.md)).
- ✅ En dificultades altas, la pérdida es mayor ([04](04-progresion-y-meta.md)). Se pierde el **35 %** de las unidades de esa expedición en Intermedio y la regla escala con la dificultad (Novato 25 %, Difícil 49 %, Hardcore 70 %; [28](28-numeros-base-de-la-economia.md)) ✅; el ajuste fino por dificultad ⏳ F3-22.
- ✅ En **Hardcore** solo mata un **encuentro de riesgo** o un **jefe** (ver [04](04-progresion-y-meta.md)). Quedarse sin energía no mata.
- ✅ **El mal del éter no mata.** Baja temporalmente las stats ([09](09-minijuegos.md)).

## Ideas para después ✅

- PvP: descartado para v1 (single-player). Si se retoma, sería asíncrono y es una decisión de arquitectura grande.
- Mineros empleados que hacen expediciones automáticas: ya no es «después», entran a mitad del juego (ver [04](04-progresion-y-meta.md)).
