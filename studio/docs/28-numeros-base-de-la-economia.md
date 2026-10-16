# 28 · Números base de la economía

Referencia única de las cifras de la economía de Veta de Fortuna: escalas, tiempo, ritmo, minerales, energía, herramientas, frenos de mercado, deuda, empleados, información, vigilancia, estilo de vida y reglas por dificultad. Nace de la tarea F0-52 y de las cinco rondas de decisión del autor (2026-10-15). Las reglas que producen estos números están en [01](01-core-loop.md), [02](02-extraccion.md), [03](03-comercio.md) y [04](04-progresion-y-meta.md); los mismos números viven en la sección `economy` y en los minerales y zonas de `studio/data/world.json`.

**Estado.** ✅ Las cifras de este documento son **decisión del autor** y las verificó el simulador de F0-53 (`tools/sim`, sección 13). El 2026-10-16 el autor aprobó los ajustes que propuso el simulador y están aplicados aquí y en `world.json`; Los cuatro puntos que dejó abiertos el Picado ampliado (ritmo del III, mejora del pico a nivel 2, piso de Comerciante y pares previstos de G1) también están aprobados y aplicados. Las decisiones del autor ya incorporadas: canal legal de la Aetherita en Puerto Meridiano, descartar menas, tienda y pedidos con mercancía propia, pedidos fuera del Acto I, empleados, Picado ampliado y aviso a los Mineros en el IV. Si una cifra cambia, se cambia aquí y en `world.json` a la vez y se vuelve a ejecutar el simulador (`python3 tools/sim/run.py --completo --escribir`). Moneda: **esquirlas** (singular «esquirla»; solo enteros, sin subunidad). ⏳ F2-20 El símbolo o la abreviatura de la moneda en pantalla no está decidido: hasta entonces se escribe «esquirlas» completo.

**Cómo está construido el modelo (en una frase).** El Acto I fija la escala (una expedición vale ≈ 250–350 esquirlas y la cuota del día 7, 960); cada acto multiplica el ritmo por ≈ 3–5 (por energía, por herramienta y por mineral de mayor tier); y lo que impide que una estrategia domine son seis frenos: spread con impuesto, profundidad del mercado, agotamiento de la zona, desgaste, vigilancia y topes diarios.

---

## 1 · Escalas ✅

### 1.1 Palabras: qué significa «punto» ✅

| Término | Definición única | Ejemplo |
|---|---|---|
| **punto** (a secas, en mercado) | **1 % del precio base del mineral** (no del precio del momento, para que los puntos se sumen) | «Carbón +3 puntos» = +3 % de 50 = +1,5 esquirlas |
| **pp** (punto porcentual de interés) | Un punto de la tasa de interés mensual de la deuda | «Interés −1 pp» = del 4 % al 3 % mensual |
| **vigilancia +N** | Unidad del indicador 0–100; se escribe «vigilancia +10», nunca «+10 puntos» a secas | «Vigilancia −15» |
| **%** | Solo para ritmos y proporciones («sube un 20 % más despacio») | |

Regla de redacción para [03](03-comercio.md), [22](22-acto-ii-variantes.md), [23](23-arbol-de-decisiones.md) y [27](27-guion-del-acto-i.md): el «%» y el «punto» de mercado coinciden por construcción (1 punto = 1 % del precio base), el interés se escribe en «pp» y la vigilancia no lleva la palabra «puntos» sola.

Precios: **por unidad y enteros** al mostrarse; el **total de cada operación se redondea una sola vez**. Por eso el mineral más barato (carbón) cuesta 50 esquirlas: 1 punto son 0,5 esquirlas y el error de redondeo no pasa del 1 %.

### 1.2 Tiempo y calendario ✅

| Magnitud | Valor | Cuenta |
|---|---|---|
| Día de juego | **13 min nominales** (rango 12–15) | |
| Bloque | **≈ 4,3 min** (rango 4–5) | 3 bloques por día |
| Semana | **7 días** (la cuota llega cada 7 días) | 91 min de juego |
| Mes y estación | **28 días** cada uno (coinciden: 4 semanas) | 6,1 h de juego |
| Año | 112 días (4 estaciones) | ≈ 24 h de juego |
| Contratos de empleado | **7, 14 y 30 días** | 1,5 h · 3,0 h · 6,5 h de juego |
| Duración del juego (orientativa) | ≈ 90 días de calendario (7 + 32 + 32 + 20) | ≈ 20 h |

- **Calendario de arranque ✅.** Estaciones en orden: primavera, verano, otoño, invierno. El **día 1 es el 22 de otoño**, así que el **invierno empieza el día 8** (primer día del Acto II). Encaja con la noticia del día 2 («el frío llegará antes») y con el apagón y la huelga del Acto II: el carbón sube justo cuando empiezas a dominar el mercado.
- **La Fosa abre los días 2, 4 y 6 de cada semana ✅** (la semana empieza el día 1; el día 7 queda libre para la cuota). Una expedición profunda a La Fosa son 2 bloques, así que caben como máximo 3 por semana.
- **Minutos y actos.** Siete días de 13 min son 91 min, el suelo del Acto I (1,5–3 h con texto y escenas). El Acto II (4–10 h) equivale a 18–46 días, el III igual y el IV (3–6 h) a 14–28 días. El contrato más largo, de 30 días, son 6,5 h de juego, menos que un acto.

### 1.3 Expediciones por día ✅

| Concepto | Valor |
|---|---|
| Expedición normal | **1 bloque** (≈ 4,3 min) |
| Expedición profunda (Cavernas, La Fosa) | **2 bloques** (Tarde y Noche, ≈ 8,6 min) |
| Máximo al día | **3 normales** (sin abrir tienda), o 1 profunda + 1 normal por la mañana, o 1 profunda + tienda por la mañana |
| Tiempo dentro de una expedición | ≈ 100 s fijos (equipo, viaje, evento, volver) + ≈ 20 s por mena (8–15 s de minijuego + escanear y elegir) |
| Menas por expedición | Variable según skills, herramientas y mejoras. Acto I: **2–3** (carbón 3, hierro 2). II: 4. III: 7 (normal) · 8–9 (profunda). IV: 8–9 (profunda) · tope blando **10** por bloque. Los empleados escalan igual, pero rinden mucho menos que tú |
| Expediciones en el guion del Acto I | **5 posibles** (días 1, 3, 4, 5 y 6; la 5.ª y la 6.ª son de respiro) |

Un jugador medio hace en el Acto II ≈ 2,5 bloques de expedición y 0,5 de tienda por día.

---

## 2 · Ritmo objetivo y patrimonio ✅

«Ingreso neto» = ventas − desgaste − impuestos − viajes. No incluye cuotas, salarios ni compras de mejoras. «Hora» es tiempo de día de juego (13 min por día, sin escenas) y el objetivo de cada acto es **su media** (decisión del autor, 2026-10-15). 🟡 Los valores del modelo «atento» son los del prototipo de F0-52 con las cifras de esta versión; el del IV ya incluye el canal legal de la Aetherita en vez del mercado negro.

| Acto | Duración ([17](17-mapa-de-historia.md)) | Días | Ingreso neto por hora · modelo «atento» | Ingreso neto por hora · **objetivo, jugador medio** (≈ 75 %) | Patrimonio al cierre (medio) |
|---|---|---|---|---|---|
| **I** | 1,5–3 h | 7 | 650 lento · **1 100 medio** · 2 200 rápido | **≈ 1 100** | **≈ 600–1 000** (rápido ≈ 2 300) |
| **II** | 4–10 h | 18–46 | 6 300 (inicio) → 10 800 (final) | **≈ 7 500** | **≈ 26 000** |
| **III** | 4–10 h | 18–46 | 38 700 | **≈ 33 000** | **≈ 160 000** |
| **IV** | 3–6 h | 14–28 | 181 000 | **≈ 110 000** | **≈ 280 000** |

**Patrimonio ✅** = efectivo + stock a valor justo, **sin restar la deuda**. No cuentan herramientas, casa, ropa ni auto (son consumo). Así el estilo de vida sigue siendo un sumidero real y la deuda no baja el estatus.

**Pisos de estatus ✅** (orden de magnitud; F4-109 fija los finales):

- **Comerciante ≈ 15 000.** Se alcanza hacia el 75 % del Acto II para un jugador medio y a las ≈ 3,5 h para uno rápido.
- **Empresario ≈ 90 000.** Hacia el 65 % del Acto III; un jugador rápido, a las 3,3 h.
- **Magnate ≈ 250 000.** Es premio al cerrar el acta, no puerta; el jugador medio llega a ≈ 280 000.

**Sumideros típicos por acto ✅** (para que el patrimonio no sea la suma de ingresos): II ≈ 20 000 (herramientas nivel 3, mejora de tienda, detector, prensa, licencias, casa y ropa, cuotas y abonos extra); III ≈ 100 000; IV ≈ 330 000 (las mejoras de nivel 4 y 5, la tienda de nivel 3, el detector, la información y el estilo de vida suman más de lo que se pensó).

---

## 3 · Los diez minerales ✅

### 3.1 Ficha base

Rendimiento: unidades de **mineral dominante** por mena con resultado «bueno» y herramienta de nivel 1. Resultados (4): perfecto ×1,5 · bueno ×1 · regular ×0,5 · fallo ×0, con redondeo aleatorio para las unidades enteras. Probabilidad de cada resultado (perfecto/bueno/regular/fallo): jugador lento 5/40/35/20 %, medio 15/50/25/10 %, rápido 30/50/15/5 %.

| Mineral | Tier (nivel de herramienta que exige) | Unidad | Energía por mena | Rend. por mena | Precio base (esquirlas por unidad) | Valor por mena (nivel 1) | Valor por energía |
|---|---|---|---|---|---|---|---|
| Carbón | 1 | saco | 8 | 2 | **50** | 100 | 12,5 |
| Hierro | 1 | saco | 10 | 2 | **90** | 180 | 18,0 |
| Cobre | 2 | saco | 12 | 2 | **170** | 340 | 28,3 |
| Salitre | 2 | saco | 12 | 2 | **150** | 300 | 25,0 |
| Plata | 2 | bolsa | 14 | 2 | **200** | 400 | 28,6 |
| Cuarzo | 2 | bolsa | 16 | 2 | **300** | 600 | 37,5 |
| Oro | 3 | bolsa | 18 | 2 | **420** | 840 | 46,7 |
| Esmeralda | 4 | pieza | 22 | 2 | **800** | 1 600 | 72,7 |
| Diamante | 4 | pieza | 26 | 1 | **1 800** | 1 800 | 69,2 |
| Aetherita | 5 | vial | 34 | 1 | **6 000** | 6 000 | 176 |

- El **tier** reparte los minerales por acto: tier 1 en el I (carbón, hierro); tier 2 y 3 en el II (cobre, salitre, plata, cuarzo, oro); tier 4 en el III (esmeralda, diamante); tier 5 en el IV (Aetherita). Un mineral de tier *t* exige una herramienta de nivel ≥ *t* del tipo de su minijuego.
- El «valor por energía» sube con el tier (12 → 176): el mejor mineral rinde más por energía, pero exige herramienta mejor, zona más lejana y un mercado más fino.
- **Aetherita ✅:** la extrae el minijuego **Contención** con una herramienta de nivel 5 (taladro o cincel) y un **filtro de la Comisión** (consumible del mostrador de filtros de La Fosa, ≈ 400 esquirlas por expedición). Los empleados **nunca** la extraen. **Dónde se vende ✅ (decisión del autor, 2026-10-15 y 2026-10-16):** en el Acto IV la **Comisión del Éter** la compra por un **canal legal con tope**, en una **oficina de Puerto Meridiano siempre abierta**: **5 viales al día**, a valor justo sin prima y con el impuesto general de 3 %. En el mercado negro solo entra como **encargo especial**: raro, de pocos viales y con su historia, nunca un canal rutinario (un encargo cada ≈ 21 días como mucho, 1 o 2 viales, prima de 30 % y vigilancia +8). Si **Casilda** es la compradora elegida en el final, los encargos llegan cada ≈ 14 días, con más historia, y la prima sigue en +10 a +15 puntos.

### 3.2 Volatilidad, liquidez y costos ✅

La volatilidad se da con **cuatro números** que usa F2-04: σ del ruido por bloque (en puntos), tope diario (en %), persistencia φ = 0,7 por bloque (el ruido decae 30 % por bloque) y vida de los eventos (decaen 15 % por día).

| Mineral | Etiqueta | σ por bloque (puntos) | **Tope diario (%)** | Desv. diaria simulada (%) | Liquidez L (u. por −1 %) | Tope por comprador (u./día) | Costo de guardar (% del precio base por unidad y día) | Spread de ida y vuelta (%) | Fricción total ida y vuelta (spread + 3 % de impuesto) |
|---|---|---|---|---|---|---|---|---|---|
| Carbón | baja–media | 1,2 | **6** | 2,5 | 10 | 30 | 0,15 | 2 | 5 |
| Hierro | baja | 0,8 | **5** | 1,8 | 8 | 24 | 0,15 | 2 | 5 |
| Cobre | media | 1,5 | **8** | 2,9 | 6 | 18 | 0,12 | 2 | 5 |
| Salitre | media–alta | 2,0 | **10** | 3,8 | 6 | 18 | 0,12 | 3 | 6 |
| Plata | media | 1,6 | **8** | 3,0 | 4 | 12 | 0,08 | 3 | 6 |
| Cuarzo | media | 1,6 | **8** | 3,0 | 4 | 12 | 0,08 | 3 | 6 |
| Oro | baja–media | 1,1 | **6** | 2,3 | 3 | 9 | 0,05 | 2 | 5 |
| Esmeralda | alta | 2,4 | **12** | 4,3 | 2 | 6 | 0,04 | 5 | 8 |
| Diamante | alta | 2,5 | **12** | 4,3 | 1,2 | 4 | 0,03 | 5 | 8 |
| Aetherita | muy alta | 3,3 | **15** (el más amplio) | 5,7 | 0,8 | 2 | 0,03 | 8 | 11 |

- **Etiquetas respetadas:** el orden de la desviación simulada es hierro < carbón ≈ oro < cobre ≈ plata ≈ cuarzo < salitre < esmeralda ≈ diamante < Aetherita.
- **Magnitudes ya escritas, comprobadas:** hierro +8 a +12 % durante el cierre por huelga ([23](23-arbol-de-decisiones.md)): con tope del 5 % al día se alcanza en 2–3 días. Aetherita «cae al tope el primer día» y baja 40–60 % en 5–8 días: al tope del 15 % harían falta 3,2 y 5,5 días, así que la curva escrita (8–11 % medio) cabe dentro del tope ([25](25-finales-y-epilogos.md)). Rebote de 5–10 puntos.
- El tope diario se alcanza el 1–5 % de los días (con eventos); no es la norma.
- **Costo de guardar:** mínimo 1 esquirla por lote y día. En el Acto I, 9 sacos de hierro guardados un día cuestan 1 esquirla (la decisión del día 3 es pequeña de verdad). La **renta del almacén** (sección 6.1) es el sumidero relevante.
- La mercancía **no se deteriora** al guardarla.

### 3.3 Estacionalidad ✅

Puntos de mercado a mitad de estación; la curva se interpola entre estaciones.

| Mineral | Primavera | Verano | Otoño | **Invierno** |
|---|---|---|---|---|
| Carbón | −4 | −8 | +4 | **+12** |
| Salitre | +8 | +2 | +3 | −5 |
| Cobre | 0 | −2 | 0 | +4 |
| Oro | 0 | 0 | 0 | +2 |
| Esmeralda | +2 | −3 | 0 | +6 |
| Diamante | 0 | 0 | 0 | +4 |
| Hierro, plata, cuarzo, Aetherita | 0 | 0 | 0 | 0 |

Carbón: de pleno verano (−8) a pleno invierno (+12) hay 20 puntos; con costo de guardar de 0,15 % al día, comprar en verano y vender en invierno (56 días) deja ≈ +21 − 5 − 8 = **+8 %**. Especular con la estación rinde poco y tarda 12 h de juego: es una opción, no una máquina.

### 3.4 Sensibilidad a eventos ✅

Evento base (antes del factor): **menor 2 puntos · medio 5 · mayor 8 · extremo 12**. Cada mineral lo multiplica por un factor según la categoría ([03](03-comercio.md): producción, política, laboral, tecnológico, clima, guerra o exterior, moda de lujo, descubrimiento). Fuera de la tabla el factor es 1,0.

| Mineral | Factores > 1 | Factores < 1 |
|---|---|---|
| Carbón | laboral ×1,5 · clima ×1,4 | moda de lujo ×0,3 |
| Hierro | guerra ×1,5 · producción (ferrocarril) ×1,3 | clima ×0,7 |
| Cobre | tecnológico ×1,3 · laboral ×1,3 (apagones) · clima ×1,2 | moda de lujo ×0,3 |
| Salitre | clima ×1,5 (cosechas) · política ×1,3 (puertos) · guerra ×1,2 | tecnológico ×0,5 |
| Plata | tecnológico ×1,2 · moda de lujo ×1,2 | guerra ×0,7 |
| Oro | política ×1,5 · guerra ×1,3 | clima ×0,5 |
| Cuarzo | tecnológico ×1,6 · descubrimiento ×1,2 | moda de lujo ×0,5 |
| Esmeralda | moda de lujo ×2,0 · política ×1,2 | laboral ×0,5 |
| Diamante | moda de lujo ×1,6 · tecnológico ×1,3 (corte) | laboral ×0,5 |
| Aetherita | descubrimiento ×2,5 · política ×2,0 · guerra ×1,5 | laboral ×0,5 |

Los eventos **sectoriales** mueven al mineral según su peso: Δ mineral = peso del sector (%) × Δ sector. Ejemplo: sector militar +10 puntos → hierro +3,5 y salitre +3,5.

### 3.5 Sectores de demanda ✅

Cada mineral pertenece a **2 o más** de los 6 sectores; los pesos suman 100. Cierra en lo numérico el reparto de [05](05-mundo-y-minerales.md); la lista de sectores de la economía los pesos quedan como están; F4-31 construye el modelo y los eventos sin cambiar el modelo.

| Mineral | Ferrocarril | Energía | Militar | Agricultura | Lujo | Tecnología |
|---|---|---|---|---|---|---|
| Carbón | 30 | **55** | 15 | | | |
| Hierro | **45** | 10 | 35 | | | 10 |
| Cobre | 10 | **50** | 10 | | | 30 |
| Salitre | 10 | | 35 | **55** | | |
| Plata | | 25 | | | 40 | 35 |
| Oro | | | 15 | | **65** | 20 |
| Cuarzo | | | 15 | | 15 | **70** |
| Esmeralda | | | | | **90** | 10 |
| Diamante | 15 | | | | 55 | 30 |
| Aetherita | | 40 | 40 | | | 20 |

Cumple lo escrito: hierro = ferrocarril + guerra; cobre = electrificación; salitre = agricultura + pólvora; cuarzo = tecnología; esmeralda = élite.

### 3.6 Prima del mercado negro ✅

Sobre el valor justo, sin impuesto y sin licencia:

| Mineral | Prima |
|---|---|
| Carbón · hierro | 20 % |
| Cobre | 22 % |
| Plata · cuarzo | 25 % |
| Oro · Aetherita | 30 % |
| Esmeralda | 32 % |
| Salitre (restringido, se paga más) · diamante | 35 % |

Dentro del rango orientativo +20–40 % de [03](03-comercio.md), variable por mineral. Con el trato de Casilda ([23](23-arbol-de-decisiones.md)) la Aetherita sube a 40–45 %. La prima de la Aetherita solo se cobra en sus encargos especiales (sección 3.1): el resto de la Aetherita se vende en el canal legal de la Comisión. Como el mercado negro tampoco paga el 3 % de impuesto, la ganancia real frente al mercado normal es la prima más ≈ 4 %.

### 3.7 Mezcla de menas por zona y agotamiento ✅

Probabilidad (%) de que una mena sea de cada mineral. Con herramienta insuficiente escaneas y saltas esa mena (no se extrae; descartarla cuesta el 25 % de su energía). Respeta el mineral principal y secundario de cada zona en [02](02-extraccion.md).

| Zona | Mezcla |
|---|---|
| 1 · Galerías del Hollín | carbón 70 · hierro 30 |
| 2 · Cañón Ferroso | hierro 55 · carbón 20 · cobre 25 |
| 3 · Minas de Sierra Alta | cobre 40 · plata 35 · hierro 15 · oro 10 |
| 4 · Salares del Litoral | salitre 55 · cuarzo 25 · plata 20 |
| 5 · Cavernas de Cristal (profunda) | cuarzo 30 · oro 25 · esmeralda 25 · diamante 10 · plata 10 |
| 6 · La Fosa del Éter (profunda, 3 días por semana) | Aetherita 40 · diamante 35 · esmeralda 15 · oro 10 |

**Descartar una mena ✅ (decisión del autor, 2026-10-15).** Escaneada una mena, puedes extraerla o descartarla. **Descartar cuesta el 25 % de la energía que habría costado extraerla** (también si tu herramienta no puede con ella). Con el descarte gratis, el jugador solo minaba lo de mayor valor por energía; con este costo el simulador mide una pérdida de ingreso de ≈ 23 % frente a descartar gratis y de ≈ 3 % adicional si el costo se duplicara (sección 13, C5).

**Agotamiento de zona ✅** (regla de [01](01-core-loop.md) y [02](02-extraccion.md): las menas se agotan y regeneran). Cada zona tiene una **riqueza** de 40 a 100 % que multiplica el rendimiento y que empieza en 100 %. Cada expedición la baja **6 puntos**, cada día sube **3**, con suelo del 40 %. Una zona sostiene **0,5 expediciones al día** sin empobrecerse; un jugador medio hace 2,5 al día repartidas en 4–5 zonas, así que en régimen la riqueza media al salir es **≈ 59 % (II) · 65 % (III) · 94 % (IV)**, ya incluida en los ingresos de la sección 2. Quien repite una sola zona cae al suelo (40 %) y rinde entre un 5 % (II) y un 27 % (IV) menos que quien rota. Ciclo de regeneración completo (de 40 a 100): 20 días.

---

## 4 · Energía ✅

| Concepto | Valor |
|---|---|
| **Aguante base** (energía máxima por expedición; se rellena entera al empezar) | **28** (decisión del autor, 2026-10-16) |
| Objetivo por acto (curva de F3-11) | I: 28–30 · II: 40 · III: 62 · IV: 80. 🟡 La curva sube linealmente desde el valor del acto anterior y llega al objetivo al **70 % del acto** (`ramp_fraction_of_act`) |
| Casa mejor (sube un poco la energía inicial) | **+2 por nivel de casa** (casas 1 a 4: +2, +4, +6, +8) |
| Menas por expedición | `floor(Aguante / (energía de la mena × multiplicador de herramienta))` |
| Multiplicador de energía por nivel de herramienta | 1,00 · 0,90 · 0,80 · 0,70 · 0,60 |
| Expedición profunda | **energía ×1,8 y carga ×1,5** (cuesta 2 bloques; rinde ≈ 0,9 de un bloque normal por bloque, compensado por la mena más valiosa) |
| Energía en 0 | vuelves con **carga parcial**; nunca se toca el almacén |
| **Carga que se pierde** (Intermedio) | **35 %** de las unidades de esa expedición (al azar entre las que llevas) |
| Regla por dificultad | `pérdida = min(75 %, 35 % × f)` con f = 0,7 · 1 · 1,4 · 2 → **Novato 25 % · Intermedio 35 % · Difícil 49 % · Hardcore 70 %** |
| Objeto de seguro (F3-09) | reduce la pérdida a la mitad; precio ≈ 6 % del valor medio de una expedición de su acto |

Comprobación del arranque del guion: con 28 de energía, el carbón (8) da 3 menas y el hierro (10) da 2: «2 a 3 menas». Una expedición de carbón del Acto I vale ≈ 255 esquirlas y una de hierro ≈ 305, con resultados medios.

**Consumibles de recarga de energía y otros ✅:** son una versión futura, mucho después de la V1, sin cifra; viven en la tabla de evolutivos de [06](06-roadmap-y-pendientes.md).

---

## 5 · Herramientas ✅

### 5.1 Modelo y niveles

Cuatro tipos con 5 niveles (pico, taladro, cincel y criba) más el **explosivo** (consumible con 5 potencias): son los «5 tipos × 5 niveles». **Un nivel es un paquete:** cada nivel mejora a la vez rendimiento (minado), energía por mena, resistencia, carga y escáner; las cuatro categorías de [02](02-extraccion.md) son los componentes de cada paquete, no escaleras separadas. Cada tipo corresponde a un minijuego: pico (Picado), criba (Cribado), taladro (Perforación) y cincel (Cincelado).

| Nivel | Rendimiento | Energía por mena | Resistencia (puntos de desgaste hasta romper) | Carga (unidades) | Ancho del rango del escáner |
|---|---|---|---|---|---|
| 1 | ×1,00 | ×1,00 | 30 | 12 | ×1,00 |
| 2 | ×1,25 | ×0,90 | 45 | 18 | ×0,92 |
| 3 | ×1,50 | ×0,80 | 65 | 26 | ×0,84 |
| 4 | ×1,80 | ×0,70 | 90 | 36 | ×0,76 |
| 5 | ×2,00 | ×0,60 | 120 | 50 | ×0,68 |

Niveles por acto: **Acto I: 1–2 · II: 2–3 · III: 3–4 · IV: 4–5**, como **guía, no como tope** (decisión del autor, 2026-10-15): si el optimizador del simulador llega antes a un nivel, el simulador propone subir su costo y el autor decide.

**Picado ampliado ✅ (decisión del autor, 2026-10-16):** el pico (minijuego Picado) extrae carbón y hierro y, desde ahora, también **cobre, plata y oro**; antes sus niveles 4 y 5 no se pagaban nunca porque solo servían para tier 1. Las demás herramientas no cambian: criba (salitre, plata, oro), taladro (hierro, cobre, plata, oro), cincel (cuarzo, esmeralda, diamante); la Aetherita sigue con taladro o cincel de nivel 5 y Contención.

### 5.2 Costo de mejorar

Un costo en dinero y un mineral por nivel. Regla: el mineral que sube la herramienta al nivel *k* se extrae con una herramienta de nivel *k*−1 (su tier es ≤ *k*−1); se cumple en las 16 mejoras. Dinero para **subir al nivel k**; los otros tipos multiplican el del pico: **criba ×1,1 · taladro ×1,25 · cincel ×1,5**.

| Subir a | Pico | Criba | Taladro | Cincel |
|---|---|---|---|---|
| 2 | 480 | 528 | 600 | 720 |
| 3 | 1 100 | 1 210 | 1 380 | 1 650 |
| 4 | 13 000 | 14 300 | 16 250 | 19 500 |
| 5 | 40 000 | 44 000 | 50 000 | 60 000 |

Primer nivel (comprar nuevo): pico 90 (Teo presta el suyo) · criba 130 · taladro 150 · cincel 200.

Mineral que consume cada subida:

| Subir a | Pico | Taladro | Criba | Cincel |
|---|---|---|---|---|
| 2 | hierro ×3 | hierro ×3 | carbón ×8 | hierro ×3 |
| 3 | cobre ×6 | cobre ×6 | salitre ×6 | salitre ×6 |
| 4 | plata ×8 | oro ×5 | cuarzo ×6 | cuarzo ×6 |
| 5 | esmeralda ×6 | diamante ×5 | esmeralda ×6 | diamante ×5 |

Comprar el mineral que falta en el marketplace cuesta +18 % (valor justo × 1,18): el costo total del pico a nivel 2 sube de 750 a 799.

**Mejorar no se paga solo en una expedición.** Medido con el simulador (F0-53, regla C1; cada mejora sube un solo tipo de herramienta y rinde solo en los minerales que ese tipo extrae), la **mejor mejora de cada nivel** se paga en **1,0 · 3,4 · 7,1 · 3,2 expediciones** (niveles 2 a 5; el costo total es dinero más mineral a precio base). Las otras de cada nivel son opcionales y más lentas (el pico a nivel 4 y 5 tarda 17 y 70 expediciones; criba nivel 4, 31). En el Acto I, mejorar el día 5 deja al jugador medio un margen del 39 % de la cuota (sección 7): «ahorrar o mejorar» es una decisión real.

### 5.3 Reparar y desgaste

- Desgaste por mena = resultado (perfecto 0,5 · bueno 1 · regular 1,5 · fallo 3) × dureza (1 + 0,2 × (tier − 1)).
- **Reparar cuesta dinero y materiales:** por punto de desgaste, dinero `[0,9, 1,5, 6, 25, 72]` según el nivel (× el factor del tipo) y **1 repuesto cada 20 puntos**, hecho de hierro (niveles 1–2), cobre (3), plata (4) u oro (5). Los repuestos se compran en Teo o en la herrería (Acto II) o se sacan de la mina.
- Reparar cuesta **7–9 % del valor bruto de la expedición** en todos los actos (8,7 · 7,0 · 7,5 · 7,0 %). Reparar del todo un pico nivel 1 son ≈ 162 esquirlas (27 de dinero + 1,5 de hierro).
- Las herramientas **no se reemplazan, se reparan**: una herramienta rota es inservible hasta repararla.
- Difícil: desgaste ×1,4; Hardcore ×2; Novato ×0,7 (regla f de la sección 12).

### 5.4 Explosivo (consumible, sin desgaste)

Existe desde el Acto III (`world.json`: Detonación); no forma parte del MVP.

| Potencia | Costo | Mineral para el que sirve | Resultado de la detonación (rendimiento) |
|---|---|---|---|
| 1 | 20 | tier 1 | perfecto +80 % · bueno +40 % · regular −20 % · fallo: se pierde la mena y con potencia ≥ 3 puede haber derrumbe (−35 % de la carga) |
| 2 | 55 | tier 2 | ídem |
| 3 | 130 | tier 3 | ídem |
| 4 | 330 | tier 4 | ídem |
| 5 | 900 | tier 5 | ídem |

El costo es ≈ 15 % del valor de la mena para la que sirve. Con la distribución «medio» (15/50/25/10) el explosivo rinde ≈ +17 % de la mena (neto ≈ +2 %: apenas compensa); con «rápido» (30/50/15/5), ≈ +36 % (neto ≈ +21 %). Es la herramienta de quien domina el minijuego: alto rendimiento, alto riesgo.

### 5.5 Detector

El detector básico heredado es el nivel 1. Se mejora **aparte con cuarzo** (tier 2, que se obtiene con un cincel nivel 2):

| Nivel | Costo | Ancho del rango (± puntos de probabilidad, antes del Ojo y del paquete de herramienta) |
|---|---|---|
| 1 (heredado) | — | ±20 |
| 2 | 400 esquirlas + 3 cuarzo | ±14 |
| 3 | 2 500 + 5 cuarzo | ±9 |
| 4 | 14 000 + 8 cuarzo | ±5 |

Nivel por acto: 2 en el II, 3 en el III, 4 en el IV. Ancho final = ancho del detector × multiplicador del escáner de la herramienta × (1 − efecto del Ojo, F3-11).

---

## 6 · Frenos de mercado ✅

| Freno | Cifra |
|---|---|
| **Spread** | tabla 3.2 (2–8 % de ida y vuelta): compras a valor justo × (1 + s/2) y vendes a × (1 − s/2) |
| **Impuesto de ventas** | **3 %** en el mercado normal, la tienda y los pedidos y contratos; **0 %** en el mercado negro. **Bolsa de Puerto Meridiano (Acto III):** la mitad de spread y ningún impuesto de venta (sin esto, especular no rinde) |
| **Profundidad del mercado (slippage)** | caída del precio = `w × q / (L × D)` por tanda, con q = unidades vendidas, L = tabla 3.2 y **D = 1,0 · 1,5 · 2,5 · 4,0** por acto (2, 3, 5 y 8 compradores NPC) |
| **Impacto del jugador** (crece con volumen y patrimonio) | `w(P) = 0,5 + 3,5 × P / (P + 400 000)`, con P = patrimonio: w = 0,5 (Acto I) · 0,6 (II) · 1,0 (III) · 1,6 (IV) · máximo 4 |
| Recuperación del impacto | se disipa **25 % por bloque** (≈ 58 % al día) |
| **Tope diario por comprador** | tabla 3.2 (≈ 3 × L unidades por día y comprador) |
| **Tope de variación diaria** | tabla 3.2 (5–15 %; Aetherita 15 %) |
| **Costo de guardar** | tabla 3.2 |
| **Renta y capacidad del almacén** | sección 6.1 |
| **Marketplace** (comprar lo que falta) | valor justo × **1,18** |
| **Carga por expedición** | 12 · 18 · 26 · 36 · 50 unidades según el nivel de herramienta (profunda ×1,5) |
| **Tienda** (venta a clientes) | precio de lista = valor justo × 1,20; el cliente medio paga **×1,15** (regateo medio; ×1,08 el jugador lento y ×1,20 el rápido); sin slippage; unidades por bloque de tienda `[16, 40, 60, 80, 100]` según el nivel de la tienda (sección 8.5). **Solo mercancía propia ✅** (extraída o refinada): la tienda y los pedidos no aceptan lo que compraste en el mercado, así que no hay bucle de compra y reventa (decisión del autor, 2026-10-15) |

**Licencias** (renovación cada 28 días; F4-213 las construye): Minero con licencia **150** · Comerciante **900** · Empresario **4 500** · Magnate **17 000** (≈ 2–3 % del ingreso mensual de cada acto).

### 6.1 Almacén ✅

| Nivel | Capacidad (unidades) | Renta (esquirlas por día) | Costo de comprar la mejora |
|---|---|---|---|
| Trastienda (incluida) | 40 | 0 (solo costo de guardar) | — |
| 1 | 120 | 15 | 1 500 |
| 2 | 300 | 50 | 7 000 |
| 3 | 700 | 150 | 35 000 |
| 4 | 1 600 | 450 | 160 000 |
| 5 | 3 500 | 1 200 | 600 000 |

---

## 7 · Deuda del Acto I y sus nombres ✅

### 7.1 Las deudas, con nombre único

«La deuda de Reme» eran varias deudas distintas. Cada una tiene ahora su nombre:

| Nombre | Qué es | Cifra |
|---|---|---|
| **Deuda de la herencia** (también «libro de deuda», «la deuda del protagonista») | La de Anselmo con Reme que heredas. **Es la que cuenta para la vía de deuda** | Capital **K = 24 000** |
| **Abono anónimo** (el giro mensual) | Pago mensual de Anselmo (vía la Comisión); no es deuda | **400 al mes**; solo paga intereses y nunca toca el capital |
| **Fiado de la gestión** | Lo que Reme adelanta a Quiroga si no alcanza el efectivo | **240**, sin interés, se paga junto con la siguiente cuota; **no** se suma a K (línea aparte; se conserva la salvaguarda de [24](24-umbrales-de-acto.md)) |
| **Recargo por atraso** | Cargo por cada semana de atraso; no es interés ni multa | tabla 7.3 |
| **Cuota extra de luz** (A2, variante Faroleros) | Pago único que pide Reme en nombre de Casilda | **960** (una cuota) |
| **Deuda de luz** (alianza con Los Faroleros) | Se suma aparte; no entra en la vía | **3 600**, sin interés, **crece 2 % al mes** si no la tocas |
| **Préstamo de Reme a su facción** | El capital que su facción le prestó hace 25 años («gasto grande» de [23](23-arbol-de-decisiones.md)) | **150 000** |
| **Deuda del banco agrario** (familia) | Solo narrativa, sin cifras ([25](25-finales-y-epilogos.md)) | — |
| **Deuda comprada** (alianza Consorcio) | Cambia el acreedor, no el capital | el mismo K |

Otras cifras de [23](23-arbol-de-decisiones.md): *gestión pequeña* de Quiroga (copia del certificado) **400**; *cuota de entrega* del contrato oficial **10 % del volumen** (se llama «cuota de entrega» para no confundirla con la cuota de la deuda); *pagar una gestión para bajar la cuota oficial*: −30 % de cuota a cambio de **5 % del valor del contrato** y vigilancia +10; *ingreso grande* (vender el archivo de Quiroga) **200 000**; *publicar tú mismo* la verdad (Lucía en tramo medio) **60 000**.

### 7.2 La cuota

- **Interés:** **4 % al mes** (28 días) sobre el saldo, devengado **1 % por semana**.
- **Cuota semanal** = amortización fija **720** (3 % de K) + interés de la semana − crédito del abono.
- **Cuota del día 7 = 960** (720 + 240). Siguientes: 953 (día 14), luego ≈ 846, 838, 831, 824, 817… (el crédito del abono baja la cuota ≈ 100 por semana desde el día 21).
- **Abono anónimo:** llega **el día 14 y cada 28 días** (14, 42, 70, 98…). Acredita 100 por semana durante las 4 semanas siguientes (nunca más que el interés devengado) y **nunca amortiza capital**. Si lo cortan (Acto IV, revelas), el interés completo vuelve y la deuda «se dispara» (+≈ 100 por semana).
- **Pagar antes** (desde el día 4): interés **−1 pp** (de 4 % a 3 % mensual; −25 %), permanente. Con −1 pp la cuota inicial baja de 960 a 900.
- **Gestión de Quiroga:** **240**; se cobra con la primera venta (día 2) o la fía Reme.
- **Efectivo inicial:** **120 esquirlas**, más el detector heredado y el pico de Teo.

### 7.3 Recargos, prórroga, tope y mora

| | Novato | Intermedio | Difícil | Hardcore |
|---|---|---|---|---|
| Recargo por semana de atraso (% de la cuota atrasada) | 4 % | **6 %** | 12 % | 18 % |
| En esquirlas sobre la cuota del día 7 (960) | 38 | **58** | 115 | 173 |
| Qué pasa con la cuota atrasada | desplaza la serie 1 semana | ídem | se suma a la del día 14 | ídem |
| Cuota total el día 14 si no pagaste el 7 | 960 + 58 (serie desplazada) | ídem | 960 + 960 + 115 = **2 035** | 960 + 960 + 173 = **2 093** |

- **Tope:** el recargo de una misma cuota **deja de crecer a las 3 semanas** (máximo 12 / 18 / 36 / 54 % de la cuota).
- **Mora** (nunca cierra una puerta): con **4 semanas de atraso acumuladas** la tasa sube **+1 pp** hasta que pagues una cuota completa; además Reme deja de fiar la gestión. No hay otra consecuencia.
- **Adelanto de la cuota** (rechazar la orden de Los Faroleros en A2): Reme cobra por adelantado la cuota de la semana siguiente, **media cuota** si pagaste a tiempo en el Acto I o **cuota completa** si prorrogaste. Es un **adelanto, no un costo extra**: se acredita a las siguientes cuotas, cuenta para la vía de deuda y solo aprieta la caja.
- **Cuota extra de luz** (aceptar la orden de Los Faroleros): **960** una vez.
- **Saldar la deuda antes de A2** ([24](24-umbrales-de-acto.md)): imposible con estas cifras (K = 24 000 son ≈ 3,8 h al ritmo del inicio del Acto II, unos 6 300 por hora); el caso de «si ya saldaste la deuda» queda como salvaguarda.

### 7.4 Vía de deuda ([24](24-umbrales-de-acto.md))

Se mide como **capital amortizado de tu bolsillo / K**. No cuentan intereses, recargos, abonos anónimos de Reme ni lo que asuma el Consorcio.

| Umbral | Capital pagado de tu bolsillo |
|---|---|
| **A5 (Acto II): 25 %** | **6 000** |
| **Círculo (Acto III): 50 %** | **12 000** |

| Ritmo | Cuotas hasta A5 | Capital por cuotas | Falta para el 25 % | Equivale a… |
|---|---|---|---|---|
| Rápido (Acto II = 4 h) | 3 (día 25) | 2 160 (9 %) | 3 840 | 23 min al ritmo del final del Acto II (≈ 10 800 por hora) |
| Medio (7 h) | 5 (día 39) | 3 600 (15 %) | 2 400 | 14 min |
| Lento (10 h) | 7 (día 53) | 5 040 (21 %) | 960 | 6 min |

Para el círculo (50 %) faltan 7 680 (rápido), 4 800 (medio) y 1 920 (lento) tras las cuotas, es decir 13, 8 y 3 minutos al ritmo del Acto III. Conclusiones:

- La vía es **alcanzable con un esfuerzo moderado** y nunca imposible. Combinar Comerciante (15 000) con el 25 % de K exige ≈ 6 h de juego en el Acto II: la ruta «deuda + estatus» es para quien no tiene prisa; el jugador rápido usa logros y relación.
- Los **abonos anónimos no la hacen inalcanzable**: suman 800–1 600 hasta el círculo (3–7 % de K), se aplican solo a intereses y el interés mensual los supera hasta el 50 % pagado (960 al inicio, 480 con el 50 % pagado; por debajo, el abono se recorta al interés).
- **Tope a lo que asume el Consorcio:** no pasa del **30 % de K (7 200)**, para que el 50 % siga siendo alcanzable (debe quedar al menos el 50 % de K pendiente).

---

## 8 · Empleados ✅

### 8.1 Rendimiento y niveles

Un empleado tiene la **misma energía y herramienta** que tú, pero **rinde una fracción** de lo que tú sacarías (Eficiencia). Nivel = Eficiencia + qué tier puede extraer:

| Nivel | Eficiencia (parte de lo que sacaría el jugador) | Tier máximo |
|---|---|---|
| N1 | 30 % | 2 |
| N2 | 38 % | 2 |
| N3 | 42 % | 3 |
| N4 | 46 % | 4 |
| N5 | 50 % | 4 |

La Aetherita, nunca. «Nivel alto» ([04](04-progresion-y-meta.md)) = **N4 y N5** (tier 4: gemas). Un empleado también agota la zona, en proporción a su Eficiencia (6 × Eficiencia puntos por expedición). En el Acto IV su papel es residual: no se toca la economía del IV.

### 8.2 Salarios y contrato

Salario por día con contrato de 30 días:

| Rol | Salario por día | Cuándo |
|---|---|---|
| **Minero N1 · N2 · N3 · N4 · N5** | **70 · 90 · 200 · 600 · 720** | N1–N2 en el II; N3–N5 en el III |
| **Dependiente** | 160 (II) · 620 (III) · 2 800 (IV) | libera el bloque de tienda |
| Refinador | igual que el Dependiente | desde el Acto II (taller) |
| Guardia | 60 % del Dependiente | |
| Analista (llega en el III) | 140 % del Dependiente (900 en el III · 3 900 en el IV) | aporta la capa 3 de información |

El salario de los roles de apoyo sube con tu estatus porque lo que hacen vale lo mismo que tu ritmo.

- **Modificador por duración del contrato:** **7 días ×1,30 · 14 días ×1,12 · 30 días ×1,00.**
- **Indemnización por despido anticipado:** `salario × días que faltan × φ`, con φ = **0,25** (7 d) · **0,40** (14 d) · **0,60** (30 d). Despedir el primer día de un contrato de 30 días cuesta ≈ 17 días de salario.
- **Asignación ✅ (decisión del autor, 2026-10-15):** un Minero hace **una expedición al día** en la zona que le asigna el jugador; cuando sube de nivel (entrenamiento o cada 40 días trabajados) su **salario sigue al nivel** (se renegocia solo), así que subir de nivel sin pagar más no es un bucle.
- **Entrenamiento** (sube un nivel): **8 × el salario diario del nivel siguiente**, 3 días de baja. Sube además 1 nivel por cada **40 días trabajados** sin entrenar.
- **Contratar** (tarifa de canal): sección de empleos del periódico → 3 días de salario; anuncio propio → 6 días de salario (llegan 1–3 candidatos en 2–4 días); Bolsa de la Unión → 10 días de salario y +15 % de salario (candidatos más fiables).

### 8.3 Lo que aporta frente a lo que cuesta

Aporte bruto de **un** Minero (esquirlas por día) medido con el simulador (F0-53, regla G1; incluye su huella sobre la riqueza de la zona y el mercado, el desgaste que paga el jugador y el jugador presente; sin heridas ni robo, que van aparte en 8.4):

| | N1 | N2 | N4 | N5 |
|---|---|---|---|---|
| Acto II | 119 | 179 | — | — |
| Acto III | — | 397 | 1 385 | 1 559 |

- **Salario ≈ 43–50 % de lo que aporta** en los pares previstos (N2 50 % en el II; N4 43 % y N5 46 % en el III); el N1 del II (59 %) no es un par previsto: solo debe quedar por debajo del 100 %; con contrato de 7 días (×1,30) sube a ≈ 76 %, siempre por debajo del 100 %. El N3 (tier 3) no tiene hueco propio en la economía medida: aporta poco en el III, por eso no es un par previsto de G1.
- **Plantilla máxima** por nivel de tienda: 0 · 2 · 3 · 5 · 7, y **Mineros ≤ 0 · 1 · 2 · 3 · 4**. La plantilla máxima del Acto III (2 Mineros N4 y un Dependiente, simulado) aporta el **68 % del jugador solo en bruto y el 42 % neto**; sin el jugador presente rinde el 63 %, y jugador + plantilla ganan un 11 % más que el jugador solo en el II. El Dependiente aporta ≈ 72 esquirlas netas al día en el II y ≈ 227 en el III (el 4 % y el 3 % del ingreso del jugador).
- En el Acto IV un Minero **no compensa** en las zonas compartidas: el mercado de gemas es fino y La Fosa y las Cavernas ya están agotadas por el jugador; cada Minero resta ≈ 9 000–10 000 esquirlas al día. Por eso su papel allí es residual. **El juego avisa ✅ (decisión del autor, 2026-10-16):** antes de enviar a un Minero a una zona agotada, muestra la pérdida estimada, pero deja decidir al jugador (`employees.act_IV_warning` en `world.json`).

### 8.4 Riesgo

| Zona | Herida por expedición | Baja | Perder la carga |
|---|---|---|---|
| Galerías | 1,5 % | 3 días | 2,3 % |
| Cañón Ferroso | 3 % | 3 días | 4,5 % |
| Sierra Alta · Salares | 4 % | 3 días | 6 % |
| Cavernas | 7 % | 5 días | 10,5 % |
| La Fosa | 12 % | 8 días | 18 % |

Cuidado alto resta hasta 2 puntos; un Guardia asignado resta la mitad. Lealtad (oculta): probabilidad de robar por semana **6 %** (baja) · **1,5 %** (media) · **0,3 %** (alta); lo robado es el 15 % del valor del día.

### 8.5 Mejora de la tienda (la que habilita «Contratar») ✅

| Nivel | Nombre | Costo | Plantilla (Mineros) | Unidades por bloque de tienda |
|---|---|---|---|---|
| 0 | Puesto (Acto I) | — | 0 | 16 |
| **1** | **Puesto ampliado (desbloquea «Contratar»)** | **3 500** | 2 (1) | 40 |
| 2 | Tienda | 18 000 | 3 (2) | 60 |
| 3 | Casa comercial | 90 000 | 5 (3) | 80 |
| 4 | Emporio | 450 000 | 7 (4) | 100 |

El nivel 1 vale por sí solo (capacidad de tienda ×2,5) y se compra en la propia tienda desde el Acto II; 3 500 son ≈ 33 min al ritmo del inicio del Acto II (unos 6 300 por hora).

---

## 9 · Información, viaje, pedidos y contratos ✅

### 9.1 Información por capas

| Capa | Costo |
|---|---|
| 1 · Básica | gratis |
| 2 · Prensa (Acto I gratis) | desde el II, suscripción de 28 días: **Heraldo 120 · La Voz 120 · Teletipo 250**; ejemplar suelto 10 · 10 · 20; un rumor comprado 40 |
| 3 · Análisis (7 y 30 días, oferta y demanda) | **3 000** una vez (o el salario del Analista) |
| 4 · Tabulador (valor justo con margen) | **18 000** una vez; margen de error ±12 puntos, baja con el Ojo hasta ±4 |

La prensa completa cuesta ≈ 890 por mes (≈ 1,5 % del ingreso mensual del Acto II).

### 9.2 Viaje

Viajar no gasta bloque pero cuesta un poco de dinero; ver las zonas en el mapa es gratis ([01](01-core-loop.md)). Costo por trayecto, ida o vuelta:

| Origen | Destino | Costo |
|---|---|---|
| Villa Brasa | Altafría · Salinas Blancas · Puerto Meridiano · Cavernas · La Fosa | 42 · 56 · 98 · 126 · 196 |
| Altafría | Salinas Blancas · Puerto Meridiano · Cavernas · La Fosa | 63 · 84 · 140 · 210 |
| Salinas Blancas | Puerto Meridiano · Cavernas · La Fosa | 49 · 119 · 182 |
| Puerto Meridiano | Cavernas · La Fosa | 70 · 154 |
| Cavernas | La Fosa | 98 |

Galerías del Hollín y Cañón Ferroso comparten la boca de Villa Brasa: **0**. En el **Acto I todo ocurre en Villa Brasa: no hay costo de viaje**. El viaje es 3–5 % de una expedición del Acto II y ≈ 1 % en el IV (sumidero pequeño). ⏳ F4-154 fija solo cómo se ve y cuánto dura el viaje en pantalla.

### 9.3 Pedidos y contratos

| Tipo | Entra | Cantidad | Prima sobre valor justo | Plazo | Penalización |
|---|---|---|---|---|---|
| **Estándar** | I | Acto I: 8 sacos de carbón; luego 1–2 días de producción media | **+12 %** | 3–7 días | Acto I: **ninguna** (se pierde sin castigo); II+: 15 % del valor |
| **Urgente** | I | Acto I: 6 de hierro | **+35 %** | 1–3 días | Acto I: ≤ 5 % del valor (nunca bloquea); II+: 30 % |
| **Negro** | II | 1 noche del tope nocturno | prima de su mineral (20–35 %), sin impuesto | 2–4 días | 25 % del valor + vigilancia +8 |
| **A largo plazo** | III | entregas semanales | precio fijo al valor justo del día de firma (puede acabar ±15–20 %) | 14–28 días | 40 % |
| **Oficial del Ministerio** | III | cuota de entrega obligatoria | +8 % | 7–14 días | 50 % + vigilancia +10 |

**Frecuencia fuera del Acto I ✅ (decisión del autor, 2026-10-15).** El Acto I está guionizado. Desde el II llega **un pedido estándar cada 2 días** (de 1 a 2 días de producción media, +12 %) y **un urgente por semana** (+35 %; 🟡 de medio día a un día de producción); entre todos aportan como máximo el **15 % del ingreso**. Los contratos a largo plazo y los oficiales llegan según su acto (🟡 uno cada 14 días). Los pedidos, como la tienda, se cumplen **solo con mercancía propia**.

Ejemplos del Acto I: el pedido estándar del día 4 (8 de carbón × 50 × 1,12) vale 448 menos el 3 % de impuesto; el urgente del día 6 (6 de hierro × 90 × 1,35) vale 729.

---

## 10 · Vigilancia, multas, mercado negro y mora ✅

### 10.1 Indicador (0–100)

| Concepto | Valor |
|---|---|
| Niveles | Tranquilo 0–29 · Observado 30–59 · Vigilado 60–84 · Bajo investigación 85–100 |
| **Subida por operación negra** | `4 + 8 × (valor de la operación / tope nocturno)` → de **vigilancia +4 a +12** |
| **Bajada natural** | **−2 al día** (también los días con operación) |
| Alianza con Los Faroleros | la vigilancia sube un **20 % más despacio** (×0,8) |
| Volumen máximo por noche (valor) | **3 300 (II) · 12 000 (III) · 55 000 (IV)**. La Aetherita ya no entra en las noches negras de rutina: en el IV se vende por el canal legal de la Comisión (sección 3.1) y solo aparece en el mercado negro como **encargo especial** (uno cada ≈ 21 días como mucho —14 con Casilda—, 1 o 2 viales, vigilancia +8) |
| Soborno a Quiroga (costo creciente) | `(500 + 0,8 % del patrimonio) × 1,35^(n−1)`; baja la vigilancia **−15**. n = sobornos hechos, y **baja 1 cada 56 días** |
| Otras bajadas ([23](23-arbol-de-decisiones.md)) | favor del retiro −10 · promesa −5 · «sabes lo del sello» −10 |
| Guardia contratado | −0,25 al día extra por guardia (máx. 3) |

### 10.2 Multas

Se multiplican por el factor f de dificultad (0,7 · 1 · 1,4 · 2).

| Nivel | Qué ocurre en cada operación negra | Multa |
|---|---|---|
| Tranquilo | nada | — |
| Observado | 20 % de inspección | **leve: 1 % del patrimonio** (mín. 60) |
| Vigilado | 50 % de inspección; **contratos oficiales bloqueados** | **fuerte: 3 % del patrimonio** (mín. 300) + decomiso del 25 % del lote |
| Bajo investigación | **redada** | ver 10.3 |

### 10.3 Redada

Al llegar a 85: confiscación del lote de esa noche y del stock negro, **multa de 6 % del patrimonio** (mín. 600), **tienda cerrada 2 días**, **mercado negro cerrado 7 días**, y la vigilancia **baja a 60**. Tras la redada sigues en Vigilado hasta que baja a 58 (al día siguiente); con el mercado negro cerrado 7 días llegas a 46 (Observado) antes de reabrir. Posible arresto (F4-69): 1 día perdido con 25 % de probabilidad en Difícil y Hardcore.

### 10.4 ¿Compensa el mercado negro?

Ganancia neta semanal respecto del ingreso honesto (simulador de F0-53, 250 días por corrida): usarlo con prudencia (parar al llegar a 30) deja **+6,6 a +7,1 %** del ingreso semanal en los actos II–IV; el mejor de 60 políticas (umbrales, sobornos, guardias, Faroleros y comprar para llenar el lote) deja +9,0 %; abusar (no parar nunca) da **−15 %** por las redadas (una cada ≈ 11–13 días). Es un complemento moderado, no una estrategia dominante.

---

## 11 · Estilo de vida V1 ✅

Orden de magnitud; el patrimonio no lo cuenta (sección 2).

| Cosa | Precio | Bonos y costos |
|---|---|---|
| **Casa 1 «remozada»** | 4 000 | +2 energía inicial; impuesto predial 1 % del valor al mes |
| Casa 2 «de comerciante» | 22 000 | +4 energía |
| Casa 3 «de empresario» | 110 000 | +6 energía |
| Casa 4 «residencia» | 450 000 | +8 energía |
| **Ropa** (un traje por escalón) | Minero con licencia 300 · Comerciante 2 500 · Empresario 16 000 · Magnate 90 000 | solo aspecto |
| **Auto** (uno en V1, solo estatus) | 70 000 | sin efecto en el viaje; mantenimiento 0,5 % al mes |
| Seguro contra saqueo | 0,3 % del valor de la casa al mes | sin seguro, un saqueo (F4-84) cuesta ≈ 3 % del efectivo |

Orden de magnitud para V2.1 y V2.2 ([06](06-roadmap-y-pendientes.md), [26](26-zonas-y-edificios.md)): chalet o caserón 150 000–250 000 · mansiones 600 000–2,5 M · yate ≈ 3 M. Encajan con el ingreso del Acto IV (110 000 por hora): son la meta aspiracional tras el cierre.

---

## 12 · Reglas por dificultad ✅

Solo la regla; los valores finos son de F3-22. Los números de este documento son los de **Intermedio**.

| | Novato | Intermedio | Difícil | Hardcore |
|---|---|---|---|---|
| **Factor de castigo f** | 0,7 | 1,0 | 1,4 | 2,0 |
| **Factor de ayuda g** | 1,15 | 1,0 | 0,9 | 0,8 |
| Ruido de los precios (σ ×) | 0,8 | 1 | 1,25 | 1,5 |
| Ancho del rango del detector y margen de error de los minijuegos (×) | 0,8 | 1 | 1,25 | 1,5 |

- Se multiplica por f: desgaste, multas de vigilancia, pérdida de carga (con tope del 75 %), costo de contratar, ruido de los precios y probabilidad de herida de los empleados.
- g multiplica la probabilidad de aparición de minerales raros.
- **No cambian entre dificultades** ([27](27-guion-del-acto-i.md)): efectivo inicial, cuota, capital, interés y precios base. Solo cambian el **recargo** (tabla 7.3) y la mora.

---

## 13 · Validación con el simulador (F0-53) ✅

**Estado.** ✅ El simulador mide las cifras de este documento y el autor aprobó el 2026-10-16 todos los ajustes que propuso (ya aplicados en las secciones 1 a 12 y en `world.json`). Con ellas, de las 50 reglas de equilibrio 50 pasan, 0 fallan y 0 son inciertas. El Picado ampliado obligó a cuatro ajustes más (13.4), que el autor también aprobó y están aplicados.

### 13.1 Qué es y cómo se ejecuta

- **Código** en `tools/sim/` (solo biblioteca estándar de Python): `mundo.py` lee **todas** las cifras de `world.json` y calcula la **huella** de las claves que usa; `mercado.py` es el mercado de referencia, con una interfaz que F2-04 y F2-08 pueden sustituir por el real; `jugador.py`, `campana.py`, `reglas.py` e `informe.py` hacen el resto. No hay cifras del juego en el código (una prueba lo comprueba).
- **Datos** en `studio/data/sim/`: `supuestos.json` (perfiles, semillas, tamaños de corrida, mutaciones y supuestos de modelado), `reglas.json` (las 50 reglas con su umbral, su origen —`doc` si sale de un documento aprobado, `prop.` si lo propuso el simulador y el autor lo aceptó— y la trazabilidad requisito → regla) y `resultados.json` (lo que mide el simulador; lo muestra el hub en `#/simulador`).
- **Cómo se ejecuta:** `python3 tools/sim/run.py --rapido` (≈ 33 s medidos en esta máquina, el que corre en CI; no incluye la regla I2 de mutaciones, que añade ≈ 45 s con `--mutaciones` y siempre corre en el modo completo; la prueba de I2 está en `tools/ci`) y `python3 tools/sim/run.py --completo --escribir` (60 semillas, 6 000 corridas del Acto I, 800 corridas para el ritmo del medio, 10 000 días tras el IV; ≈ 16 minutos; reescribe `resultados.json`). Si cambia una cifra que el simulador lee, la huella cambia, los resultados caducan y `build.py --strict` falla hasta que se reejecuta.
- **Perfiles:** lento (probabilidades 5/40/35/20 y 4 expediciones en el Acto I), medio (15/50/25/10 y 5), rápido (30/50/15/5 y 9) y **optimizador** (el «modelo atento»: compra cada mejora en cuanto se paga y busca bucles). La duración de cada acto sale de la tabla de la sección 2: lento = máximo de horas, medio = media, rápido = mínimo. «Hora» es tiempo de día de juego (13 min por día, sin escenas) ✅.
- **Qué modela:** menas enteras con descarte y resultado de cada una, zonas que se agotan, tienda (solo mercancía propia), pedidos, mercado spot y Bolsa con spread, impuesto, slippage y tope por comprador, mercado negro con vigilancia, multas, redadas, sobornos, guardias y Faroleros, Aetherita por el canal legal y por encargos especiales (también la variante de Casilda), empleados (Mineros y Dependiente), mejoras de herramientas elegidas por su recuperación, deuda con abono anónimo, recargos y mora, y estilo de vida. Reproduce el prototipo de F0-52 dentro del 5 % (B8).

### 13.2 Resultado

Modo completo, 2026-10-16 (60 semillas y 800 corridas del medio para el ritmo; intervalos de confianza del 95 % en `resultados.json`). El origen de cada umbral (`doc` o `prop.`) está por regla en `reglas.json`.

| Regla | Qué se comprueba | Umbral | Resultado (la condición que decide) | Estado |
|---|---|---|---|---|
| A1 | Cuota del día 7 sin mejora | pago 95–99,9 % · margen 30–75 % de la cuota | Pago a tiempo: 99,6 % | pasa |
| A2 | Ahorrar o mejorar el día 5 | margen con mejora ≥ 10 % · diferencia 8–45 pp · pago con mejora ≥ 80 % | Diferencia de pago sin y con mejora (pp): 9,1 pp | pasa |
| A3 | El lento no es imposible ni trivial | 4 exp.: 10–60 % · 5 exp.: ≥ 60 % · cierra el acto · día 14 ≥ 90 % | El acto cierra aunque no pague (la mora no cierra puertas): 100 % | pasa |
| A4 | El rápido paga con holgura | pago ≥ 99,9 % · margen 100–300 % | Pago a tiempo: 100 % | pasa |
| A5 | Ingreso neto por hora del Acto I | ≤ 20 % | Desviación del ingreso/h (lento): 13,7 % | pasa |
| A6 | Cuota del día 14 y recargos en las cuatro dificultades | Novato e Intermedio ≤ 30 % · Difícil ≤ 55 % · Hardcore ≤ 60 % | Recargo de Intermedio menos 6 % de la cuota (esquirlas): 0,4 esq | pasa |
| A7 | Saldar la deuda antes del día 8 es imposible | < 100 % de K | Caja máxima del Acto I frente al capital: 19,4 % | pasa |
| B1 | Ritmo por acto de la campaña completa | ±20 % del objetivo · medio = 60–80 % del optimizador · lento < medio < rápido · rápido/lento ≤ 4 | Orden lento < medio < rápido en II, III y IV (1 = sí): 1 | pasa |
| B2 | Crecimiento razonable entre actos | I < II < III < IV · razones 3–5 (I→II hasta 7) · rampa ≤ ×3,5 | Crece I < II < III < IV (1 = sí): 1 | pasa |
| B3 | Patrimonio al cierre de cada acto | Acto I dentro de 600–1 000 (rápido ±25 % de 2 300) · II, III, IV ±25 % · sumideros ±40 % · lento ≥ 50 % del medio | Patrimonio al cierre del Acto I (medio), en esquirlas: 693,5 esq | pasa |
| B4 | Los estatus se alcanzan a tiempo | ≥ 95 % de las corridas · entre el 60 y el 90 % del acto · Magnate antes del cierre | Comerciante alcanzado dentro del acto: 100 % | pasa |
| B5 | El optimizador no se salta el techo de herramienta | ≥ 90 % de las corridas con nivel ≤ guía del acto + 1 | Corridas con el nivel de pico ≤ 4 al cerrar el Acto II: 100 % | pasa |
| B6 | Sumideros recurrentes | prensa ≈ 1,5 % · licencias 1,5–3 % · viaje 3–5 % (II) y ≈ 1 % (IV) · reparación 7–9 % · renta ≤ 5 % | Viaje sobre el valor bruto de las expediciones (Acto II): 3,1 % | pasa |
| B7 | La economía no explota tras el Acto IV | crecimiento ≤ 10 % · identidad exacta · ≤ techo × 1,05 | Ingreso semanal máximo frente al techo físico: 60,6 % | pasa |
| B8 | El simulador reproduce el prototipo de F0-52 | ≤ 5 % | Prototipo IIe frente a 6300 esq/h: 0,9 % | pasa |
| C1 | Cada mejora se paga en pocas expediciones | la mejor mejora de cada nivel se paga en 1–8 expediciones | Expediciones para pagar la mejora más rápida: 1,0 exp | pasa |
| C2 | Cadencia de mejoras | 0,3–3 h | Horas de ingreso para pagar la mejora más cara (cincel a nivel 4): 2,6 h | pasa |
| C3 | Reparar cuesta 7–9 % del valor bruto | 6–10 % | Reparación sobre el valor bruto de la expedición (Acto II): 7,5 % | pasa |
| C4 | El explosivo apenas compensa | medio ≤ +5 % · rápido ≤ +25 % | Rendimiento neto del explosivo, perfil rapido (peor: potencia 2): 22,6 % | pasa |
| C5 | Descartar una mena tiene un costo real | pérdida 3–35 % · al doblar el costo pierde ≥ 1 % más · ≤ 60 % de las menas descartadas | Pérdida de ingreso de descartar a coste normal frente a descartar gratis: 22,1 % | pasa |
| D1 | Ninguna zona es siempre la óptima | mejor zona ≤ 65 % · mejor fija ≤ 100 % de la adaptativa · ≥ 3 zonas con ≥ 15 % de uso | Zonas con uso ≥ 15 % (mínimo de los actos): 3 zonas | pasa |
| D2 | Agotamiento de las zonas | 59 · 65 · 94 % ±5 pp · repetir pierde ≥ 5 % | Pérdida de quien repite una sola zona (acto con menor pérdida): 7,6 % | pasa |
| D3 | La Fosa y la Aetherita no mandan | ≤ 3 por semana · Aetherita ≤ 60 % de las ventas | Expediciones a La Fosa en una semana (máximo): 3 exp | pasa |
| E1 | Sin ganancia segura entre canales | ninguna ganancia fuera del negro · negro ≤ 15 % del ingreso diario | Mayor ganancia diaria sostenible de comprar para vender en negro (% del ingreso diario): 10,2 % del día | pasa |
| E2 | Impacto del jugador en el precio | w crece de 0,5 a 4 · slippage creciente (o estable, ≥ 0,9×) y ≤ 12 % en el IV · w por acto ±15 % | W(P) estrictamente creciente (1 = sí): 1 | pasa |
| E3 | Sin bucle de impacto | < 0 en todo el rango | Mayor ganancia media de un bucle de impacto (acto III, espera 0 bloques): -5,8 % | pasa |
| E4 | La especulación no domina | spot ≤ +2,5 % · Bolsa ≤ +7 % · estación ≤ +12 % · trader ≤ 25 % del ingreso minero | Mejor rendimiento neto de especular con aviso perfecto (bolsa; evento ≥ 12, espera 1): 6,9 % | pasa |
| E5 | Volatilidad y topes diarios | ±10 % · orden respetado · ≤ 6 % de los días en el tope | Orden de volatilidad entre minerales respetado (1 = sí): 1 | pasa |
| E6 | Tope por comprador y capacidad del almacén | ±10 % del ritmo | El excedente sobre el tope se vende más barato (1 = sí): 1 | pasa |
| E7 | Los pedidos son un complemento | > 0 y ≤ 15 % del ingreso | Ganancia extra de los pedidos sobre el ingreso (Acto IV): 1,0 % | pasa |
| F1 | Mercado negro prudente | +3 a +12 % | Ganancia semanal del mercado negro prudente sobre el ingreso honesto (Acto III): 6,6 % | pasa |
| F2 | Barrido de políticas del mercado negro | ≤ +12 % | Mayor ganancia semanal entre 60 políticas (acto II, umbral 45): 9,0 % | pasa |
| F3 | El mercado negro abusivo pierde | < 0 % · una redada cada 11 ± 3 días | Días entre redadas del jugador abusivo (Acto IV): 13,1 días | pasa |
| F4 | Aetherita en el Acto IV: canal legal con tope | legal ≥ 90 % de las ventas · encargo cada ≥ 14 días y ≤ 2 viales · vigilancia ≤ 25 % de la bajada natural | Encargos especiales: viales por encargo (máximo): 2 viales | pasa |
| F5 | Cuánto cuesta una noche negra en bloques | informativa (> 0) | Bloques que puede costar una noche negra sin perder (Acto II): 1,0 bloques | pasa |
| G1 | El empleado no domina: salario frente a aporte | pares previstos 40–60 % (N2 del II; N4 y N5 del III) · todos ≤ 100 % (también N1) · 7 días ≤ 85 % · aporte neto en el IV ≤ 0 | Salario ÷ aporte, par previsto más bajo (III N4): 43,3 % | pasa |
| G2 | La plantilla máxima no domina | bruto ≤ 70 % · neto ≤ 45 % del jugador solo | Aporte bruto de la plantilla máxima sobre el jugador solo (peor: Acto III): 67,9 % | pasa |
| G3 | El jugador ausente rinde menos | plantilla sola ≤ 65 % · jugador + plantilla ≥ solo + 5 % | Ingreso de la plantilla sola frente al jugador solo (peor: Acto III): 63,5 % | pasa |
| G4 | El Dependiente aporta, pero poco | > 0 y ≤ 35 % (II y III) | Aporte neto del Dependiente sobre el ingreso del jugador (Acto II): 4,1 % | pasa |
| G5 | Entrenar y ascender no es un bucle | retorno ≥ 5 días, sin máximo | El salario sigue al nivel (1 = sí): 1 | pasa |
| G6 | Riesgo de los empleados | informativa (≤ 100 % del aporte) | Pérdida esperada de un Minero por riesgo (peor zona: fosa), en % del aporte: 98,2 % | pasa |
| H1 | Vía de deuda del 25 % en el Acto II | falta ≤ 0,5 h · alcanzable · Comerciante + 25 % ≤ 6,5 h | Horas del Acto II para ser Comerciante y llevar el 25 % pagado: 6,1 h | pasa |
| H2 | Vía de deuda del 50 % en el círculo | falta ≤ 0,3 h | Horas de ingreso del Acto III que faltan para el 50 % sin pagos extra (rapido): 0,2 h | pasa |
| H3 | Abonos anónimos y Consorcio | mismo capital · abono < interés · Consorcio ≤ 30 % de K y queda ≥ 50 % | Capital máximo que asume el Consorcio frente a K: 30 % | pasa |
| H4 | La mora no cierra puertas | ≤ 2 · 3 · 4 semanas · Hardcore día 14 ≤ 40 % del ingreso del lento | Algún estado de la mora cierra una puerta (0 = no): 0 | pasa |
| H5 | Variantes de A2 con el lento | caja < 0 a lo sumo una semana · vía alcanzable | La deuda de luz crece más despacio que la deuda principal (1 = sí): 1 | pasa |
| H6 | Misión de rescate: horas de juego | entrega de la cifra (informativa) | Horas de la misión de rescate para la puerta A5 (1,25 × p95 del lento, a 0,5 h): 13,5 h | pasa |
| I1 | Determinismo | idéntico | Misma semilla, mismo resultado (1 = sí): 1 | pasa |
| I2 | Mutaciones | 100 % de las reglas | Reglas cuya mutación cambia el estado de alguna condición: 100 % | pasa |
| I3 | Intervalos visibles y ninguna regla incierta | 0 | Reglas en «incierto»: 0 reglas | pasa |

### 13.3 Qué dicen los resultados

- **Acto I.** Con el Aguante inicial de 28, la mejora del día 5 a 480 y el descarte al 25 %, el jugador medio paga la cuota del día 7 el 99,6 % de las veces con un margen del 72 % (con 25 de Aguante pagaba el 86,8 % con un margen del 26 %: Galerías 70/30 y las menas enteras costaban demasiado). Mejorar el día 5 baja el pago al 90,6 % (9 pp) y deja un margen del 45 %: «ahorrar o mejorar» es una decisión real. El lento paga el 57 % con 4 expediciones y el 86 % con 5.
- **Ritmo por acto.** El jugador medio rinde ≈ 1 170 · 7 840 · 31 900 · 108 100 esquirlas por hora (objetivos: 1 100 · 7 500 · 33 000 · 110 000; el del III subió de 27 000 a 33 000 con el Picado ampliado). El patrimonio al cerrar es ≈ 30 600 · 157 000 · 245 000 (objetivos: 26 000 · 160 000 · 280 000).
- **Estatus.** Comerciante se alcanza al ≈ 66 % del Acto II, Empresario al 70 % del III y Magnate antes del cierre del IV en casi todas las corridas.
- **Reparar** cuesta el 7,5–7,8 % del valor bruto de la expedición con los nuevos precios por punto.
- **Mejoras.** La mejor mejora de cada nivel se paga en 1,0 (nivel 2), 3,4 (3), 7,1 (4) y 3,2 (5) expediciones. La mejora del pico a nivel 2 (480) se paga en 1,04 expediciones.
- **Empleados.** Salario ÷ aporte: 59 % (N1) y 50 % (N2) en el II; 43 % (N4) y 46 % (N5) en el III. La plantilla máxima del III aporta el 68 % del jugador solo en bruto y el 42 % neto. En el IV cada Minero resta ≈ 9 000–10 000 al día (el juego avisa antes de mandarlo, 8.3).
- **Aetherita.** Por el canal legal de 5 viales al día es el 56 % de las ventas del IV; los encargos especiales del negro suponen el 16 % de la bajada natural de vigilancia (22 % con la variante de Casilda, cada 14 días).
- **Mercado.** Ninguna combinación de comprar y vender deja ganancia segura: la ida y vuelta pierde un 5,9 % y la mejor compra para vender en negro rinde, con la vigilancia como freno, el 11,7 % del ingreso diario. Especular con aviso perfecto de un evento extremo rinde +2,1 % (spot) y +6,9 % (Bolsa) por operación; con la estación, +6,5 % (carbón). La profundidad del mercado casi no se nota (0,5 % del bruto en el IV vendiendo todo al spot) porque la tienda, a ×1,15 y sin slippage, absorbe lo que cabe en ella. Los pedidos aportan el 1,5–3,5 % del ingreso.
- **Mercado negro.** Prudente (parar en vigilancia 30): +6,9 % (II), +6,6 % (III) y +7,1 % (IV) del ingreso honesto; la mejor de 60 políticas, +9,0 %; abusivo: −15 % con una redada cada 11–13 días. Una noche negra puede costar hasta 0,97 · 0,95 · 0,85 bloques antes de dejar de compensar (insumo para ⏳ F4-72).
- **Deuda.** La vía del 25 % falta 0,3 h de ingreso del Acto II sin pagos extra y la del 50 % 0,14 h del III; se alcanzan en el 100 % de las corridas. Comerciante + 25 % tarda 6,1 h del Acto II (límite 6,5 h). La mora nunca cierra una puerta; ponerse al corriente tras 12 semanas de atraso cuesta 2–3 semanas.
- **Misión de rescate (⏳ F0-78).** Horas de juego acumuladas tras las que debería llegar: **13,5 h** para la puerta A5 y **26,5 h** para el círculo (1,25 × el percentil 95 del jugador lento, a 0,5 h; `economy.rescue_mission`).

### 13.4 Ajustes que trajo el Picado ampliado

Ampliar el Picado a cobre, plata y oro aceleró el Acto III y abarató el pico; el simulador propuso cuatro ajustes y el autor los aprobó el 2026-10-16:

| Regla | Medido antes del ajuste | Ajuste aplicado |
|---|---|---|
| B1 · ritmo del medio en el III | 32 000 por hora, un 21 % sobre 27 000 | Objetivo del III de 27 000 a **33 000** |
| C1 · la mejora más rápida se paga en ≥ 1 expedición | 0,93 (pico a nivel 2) | Mejoras de nivel 2: pico **480**, criba 528, taladro 600, cincel 720 |
| B4 · Comerciante entre el 60 y el 90 % del Acto II | 60,5 %, incierta | Piso de Comerciante de 14 000 a **15 000** |
| G1 · salario ÷ aporte del N1 en el II | 58,6 %, incierta (aporta poco y con ruido) | El N1 sale de los pares previstos; sigue en «todos ≤ 100 %» |

### 13.5 Lo que el simulador no modela

El refinado y las recetas (valor agregado 0 hasta ⏳ F3-07), los bots y el mercado interno (⏳ F3-06 y ⏳ F4-39), el modelo real de sectores y eventos (⏳ F4-31: los eventos del simulador son sueltos, de un solo mineral), el coste en bloques de una noche negra (⏳ F4-72: F5 da el máximo que compensa), la curva real del Aguante (⏳ F3-11), los valores de dificultad (⏳ F3-22), los minijuegos más allá de sus cuatro probabilidades, la prensa más allá de su precio, los encuentros, las relaciones y los logros. Cuando F2-04 y F2-08 construyan el mercado real, se reejecutan las reglas E.

---

## Documentos relacionados

[01](01-core-loop.md) bucle de juego · [02](02-extraccion.md) extracción · [03](03-comercio.md) comercio · [04](04-progresion-y-meta.md) progresión · [05](05-mundo-y-minerales.md) minerales · [06](06-roadmap-y-pendientes.md) evolutivos · [09](09-minijuegos.md) minijuegos · [15](15-flujo-de-trabajo-y-calidad.md) regla de lo diferido · [17](17-mapa-de-historia.md) actos · [22](22-acto-ii-variantes.md) · [23](23-arbol-de-decisiones.md) · [24](24-umbrales-de-acto.md) vía de deuda · [25](25-finales-y-epilogos.md) · [26](26-zonas-y-edificios.md) zonas · [27](27-guion-del-acto-i.md) guion del Acto I.
