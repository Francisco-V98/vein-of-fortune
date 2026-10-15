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

✅ Estas seis son **zonas de minado**: cada una se entra por la boca de mina de un asentamiento (Villa Brasa atiende las dos del Hollín). En el mapa, «zona» es la región completa con su asentamiento ([26](26-zonas-y-edificios.md)). Ir de una a otra no gasta bloque pero cuesta un poco de dinero (⏳ F0-52; [01](01-core-loop.md)). Las **Cavernas** y **La Fosa** son zonas profundas: una expedición cuesta 2 bloques y ocupa la Tarde y la Noche, y La Fosa solo abre 3 días por semana (días ⏳ F0-52; [01](01-core-loop.md)).

✅ Los «enemigos» de las primeras zonas son **personas** (capataces, bandas, inspectores que piden soborno), no monstruos, como muestra la tabla. Encaja con el tono y con los encuentros por decisión (pagar, negociar, pelear, huir). Las criaturas aparecen solo en La Fosa, por la Aetherita.

✅ **Los jefes de zona son opcionales, no una puerta:** ni el desbloqueo de zonas ni el cierre de un acto exigen vencerlos ([24](24-umbrales-de-acto.md)). El duelo de cada jefe ⏳ F4-54.

- ⏳ F2-10 Ficha completa de las Galerías del Hollín, la zona 1, con la plantilla de arriba.
- ⏳ F4-02 · F4-07 · F4-12 · F4-17 · F4-22 Fichas completas de las zonas 2 a 6, en ese orden.

## Menas y detector de probabilidades ✅

✅ Cada mena tiene una composición con probabilidades (ej. 30 % oro, 3 % diamante, 50 % carbón). Un **detector** muestra esas probabilidades y el jugador decide si le conviene extraerla o buscar otra, sabiendo que gasta energía y desgasta herramientas.

✅ El detector muestra **rangos** (ej. «oro: 20–40 %») y no valores exactos. El **Ojo** y la herramienta determinan qué tan estrechos son ([04](04-progresion-y-meta.md), [09](09-minijuegos.md)); la precisión mejora con mejores escáneres → la información es progresión.

✅ El protagonista empieza con un **detector básico heredado de Anselmo**. No depende del cuarzo: el cuarzo solo lo mejora más adelante.

✅ Las probabilidades de aparición y obtención se calibran para que no sea fácil ganar mucho dinero rápido ni terminar el juego pronto.

- ⏳ F0-52 Cuánta energía gasta cada mena y cuántas menas caben en una expedición.

## Herramientas ✅

✅ Estilo Minecraft:

- Las herramientas **se desgastan** con el uso.
- Cada herramienta sirve para ciertos materiales; los materiales de mayor nivel requieren herramientas mejores.
- Mejor herramienta → minijuego más fácil / zona óptima más amplia / más probabilidad de obtención.

✅ Categorías de mejoras que el jugador debe ir comprando: más resistencia, más almacenamiento (carga), mejor minado, mejor información (escáner).

### Modelo de herramientas ✅

Decisión del autor (2026-10-15):

| Pieza | Regla |
|---|---|
| Tipos | **5 tipos**: pico, taladro, cincel, criba y explosivo (los de [09](09-minijuegos.md)); cada uno cubre un tipo de minijuego ✅ |
| Niveles | **5 niveles por herramienta**, y los minerales de mayor nivel exigen herramientas de mayor nivel ✅ (a revisar si en el prototipo hace falta ampliar, ⏳ F4-60) |
| Explosivo | Es **consumible**: se gasta con cada uso en lugar de desgastarse ✅ |
| Reparar | Cuesta **dinero y materiales** ✅. Es otro sumidero de dinero. Los materiales concretos ⏳ F0-52 |
| Mejorar | Requiere **minerales específicos** (ej. hierro para el pico, diamante para el cincel, cuarzo para mejorar el detector). Así los minerales tienen utilidad real ✅ |
| Qué mineral | El mineral que sube una herramienta al nivel *k* se extrae con una herramienta de nivel *k*−1 ✅. Así nunca hace falta lo que aún no se puede sacar |
| Facciones | Mejorar es **neutral entre facciones** ✅ |
| Requisitos | Los niveles altos requieren **estatus, licencia o contacto** (influencia), no solo dinero ✅ (⏳ F4-114 proveedores por estatus, ⏳ F4-213 licencias) |

- ⏳ F0-52 Costos por nivel, de reparar (dinero y materiales) y de mejorar, y el costo del explosivo.

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
- ✅ En dificultades altas, la pérdida es mayor ([04](04-progresion-y-meta.md)). El porcentaje de carga que se pierde ⏳ F0-52, y los valores por dificultad ⏳ F3-22.
- ✅ En **Hardcore** solo mata un **encuentro de riesgo** o un **jefe** (ver [04](04-progresion-y-meta.md)). Quedarse sin energía no mata.
- ✅ **El mal del éter no mata.** Baja temporalmente las stats ([09](09-minijuegos.md)).

## Ideas para después ✅

- PvP: descartado para v1 (single-player). Si se retoma, sería asíncrono y es una decisión de arquitectura grande.
- Mineros empleados que hacen expediciones automáticas: ya no es «después», entran a mitad del juego (ver [04](04-progresion-y-meta.md)).
