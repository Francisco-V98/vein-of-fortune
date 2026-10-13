# 02 · Extracción

## Zonas

✅ Cada zona tiene características propias: qué minerales aparecen y con qué probabilidad, qué peligros tiene y su nivel de dificultad. El jugador debe decidir a cuál ir y ser consciente de los riesgos.

✅ Los minerales son más probables en unas zonas que en otras.

✅ Desbloqueo **por etapas**; cuando el jugador las tiene todas, puede moverse con libertad según su necesidad.

✅ Recursos **limitados** por zona, con **reactivaciones/regeneración** cada cierto tiempo.

🟡 Para la versión 1: 5–6 zonas. Cada mineral aparece en 2–3 zonas con probabilidades distintas, de modo que no exista una "zona óptima" fija.

### Ficha de zona (plantilla)

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

✅ Estas seis son **zonas de minado**: cada una se entra por la boca de mina de un asentamiento (Villa Brasa atiende las dos del Hollín). En el mapa, «zona» es la región completa con su asentamiento ([26](26-zonas-y-edificios.md)).

🟡 Los "enemigos" de las primeras zonas son **personas** (capataces, bandas, inspectores que piden soborno), no monstruos. Encaja con el tono y con los encuentros por decisión (pagar, negociar, pelear, huir). Las criaturas aparecen solo en La Fosa, por la Aetherita.

❓ Fichas completas por zona (usar la plantilla anterior).

## Menas y detector de probabilidades

✅ Cada mena tiene una composición con probabilidades (ej. 30 % oro, 3 % diamante, 50 % carbón). Un **detector** muestra esas probabilidades y el jugador decide si le conviene extraerla o buscar otra, sabiendo que gasta energía y desgasta herramientas.

🟡 El detector muestra **rangos** (ej. "oro: 20–40 %") y no valores exactos. La precisión mejora con mejores escáneres → la información es progresión.

✅ El protagonista empieza con un **detector básico heredado de Anselmo**. No depende del cuarzo: el cuarzo solo lo mejora más adelante.

✅ Las probabilidades de aparición y obtención se calibran para que no sea fácil ganar mucho dinero rápido ni terminar el juego pronto.

## Herramientas

✅ Estilo Minecraft:

- Las herramientas **se desgastan** con el uso.
- Cada herramienta sirve para ciertos materiales; los materiales de mayor nivel requieren herramientas mejores.
- Mejor herramienta → minijuego más fácil / zona óptima más amplia / más probabilidad de obtención.

✅ Categorías de mejoras que el jugador debe ir comprando: más resistencia, más almacenamiento (carga), mejor minado, mejor información (escáner).

🟡 Mantenimiento: reparar herramientas cuesta dinero y/o tiempo (otro sumidero de dinero).

✅ **5 niveles por herramienta** (a revisar si en el prototipo hace falta ampliar). Los minerales de mayor nivel exigen herramientas de mayor nivel.

🟡 Tipos: pico, taladro, cincel, criba y explosivo (los de [09](09-minijuegos.md)); cada uno cubre un tipo de minijuego.

🟡 Mejorar una herramienta requiere **minerales específicos** (ej. hierro para el pico, diamante para el cincel, cuarzo para mejorar el detector). Así los minerales tienen utilidad real.

🟡 Los niveles altos de equipo requieren licencias o contactos (influencia), no solo dinero.

## Fallos y daño a la mena

✅ Si el jugador falla el minijuego, puede **fallar** la extracción y también **dañar la mena** (menor rendimiento o pérdida).

🟡 El resultado del minijuego (perfecto / bueno / malo) modifica el rendimiento y el daño.

## Minijuegos de extracción

✅ Varios tipos, simples, alineados con el juego. Inspiración: pesca de Stardew Valley (equilibrar **dos parámetros** hasta un punto óptimo, ej. fuerza vs. precisión) y minijuegos cortos tipo Among Us.

### Catálogo inicial 🟡

| Minijuego | Mecánica | Parámetros |
|---|---|---|
| Picado | Timing de golpe | Fuerza ↔ precisión |
| Perforación | Mantener zona óptima | Velocidad ↔ calor (sobrecalentamiento) |
| Cincelado | Trazar líneas de corte | Precisión pura (gemas) |
| Cribado / lavado | Mantener flujo | Inclinación ↔ caudal (como la pesca) |
| Detonación | Colocar carga | Potencia ↔ ubicación (riesgo de dañar la mena) |

Cada tipo de mineral/dureza se asocia a un minijuego. Detalle completo, automatización y MVP: ver [09-minijuegos.md](09-minijuegos.md).

### Tareas de peligro (estilo Among Us) 🟡

Para afrontar peligros ambientales: sellar una fuga de gas (secuencia), apuntalar un techo (patrón), reparar una herramienta (conectar piezas).

## Peligros y enemigos

✅ **Peligros ambientales** por zona. Algunos enemigos o criaturas. El jugador decide: **retirarse, pelear o armar una estrategia** según la situación.

### Encuentros por eventos 🟡

- Aparece una ilustración + texto con la situación.
- Opciones: pelear, huir, sobornar/negociar, soltar parte de la carga, usar un objeto.
- Las estadísticas y el equipo determinan las probabilidades; el jugador las ve antes de decidir.
- Jefes ocasionales: encuentro con un minijuego corto de timing.
- Cada zona tiene un **nivel de peligro visible** antes de entrar.

### Preparación (loadout) 🟡

Antes de salir, el jugador elige equipo según los peligros de la zona (máscara para gas, refuerzos, armas, objetos de escape).

## Pérdida

✅ Existe la posibilidad de perder materiales en una expedición si el jugador no está preparado.

🟡 La pérdida es **parcial**, no total, con objetos para asegurar o escapar. En mobile, perderlo todo frustra demasiado.

🟡 En dificultades altas, la pérdida es mayor. En **hardcore**, la derrota termina la partida (ver [04](04-progresion-y-meta.md)).

## Ideas para después

- PvP: descartado para v1 (single-player). Si se retoma, sería asíncrono y es una decisión de arquitectura grande.
- Mineros empleados que hacen expediciones automáticas: ya no es "después", entran a mitad del juego (ver [04](04-progresion-y-meta.md)).
