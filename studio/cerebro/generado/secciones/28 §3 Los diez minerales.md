---
id: "doc-28-s03"
tipo: "seccion"
title: "3 · Los diez minerales ✅"
aliases: ["doc-28-s03"]
documento: "[[28 Números base de la economía]]"
limpieza: 100
abiertos: 0
espera: 2
aplazado_a: ["[[F3-07 Refinado y taller - lingotes y productos básicos]]"]
estado: "con-aplazados"
anterior: "[[28 §2 Ritmo objetivo y patrimonio]]"
siguiente: "[[28 §4 Energía]]"
arriba: "[[28 Números base de la economía]]"
fuente: "studio/docs/28-numeros-base-de-la-economia.md:80"
generado: true
---

# 3 · Los diez minerales ✅

> Rendimiento: unidades de mineral dominante por mena con resultado «bueno» y herramienta de nivel 1. Resultados (4): perfecto ×1,5 · bueno…

← [[28 §2 Ritmo objetivo y patrimonio]] · [[28 Números base de la economía|↑ 28]] · [[28 §4 Energía]] →

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
- **Celda de éter ✅ (decisión del autor, 2026-10-16):** la receta de Aetherita + cuarzo ([[03 Comercio y mercado|03]]) se abre en el Acto IV y **gasta viales del mismo tope diario** de 5 al día de la oficina de Puerto Meridiano; solo la compran la **Comisión del Éter** o el **Consorcio**, nunca la tienda ni los pedidos de cliente (que aceptan solo mercancía propia extraída o refinada). El simulador no modela recetas (valor agregado 0 hasta ⏳ [[F3-07 Refinado y taller - lingotes y productos básicos|F3-07]], sección 13.5), así que esto **no cambia ninguna cifra ni caduca los resultados**: el tope de 5 viales al día y su impuesto siguen igual, y lo que cuesten el cuarzo y el lote lo fija ⏳ [[F3-07 Refinado y taller - lingotes y productos básicos|F3-07]].

### 3.2 Volatilidad, liquidez y costos ✅

La volatilidad se da con **cuatro números** que usa [[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y|F2-04]]: σ del ruido por bloque (en puntos), tope diario (en %), persistencia φ = 0,7 por bloque (el ruido decae 30 % por bloque) y vida de los eventos (decaen 15 % por día).

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
- **Magnitudes ya escritas, comprobadas:** hierro +8 a +12 % durante el cierre por huelga ([[23 Árbol de decisiones y consecuencias|23]]): con tope del 5 % al día se alcanza en 2–3 días. Aetherita «cae al tope el primer día» y baja 40–60 % en 5–8 días: al tope del 15 % harían falta 3,2 y 5,5 días, así que la curva escrita (8–11 % medio) cabe dentro del tope ([[25 Finales y epílogos|25]]). Rebote de 5–10 puntos.
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

Evento base (antes del factor): **menor 2 puntos · medio 5 · mayor 8 · extremo 12**. Cada mineral lo multiplica por un factor según la categoría ([[03 Comercio y mercado|03]]: producción, política, laboral, tecnológico, clima, guerra o exterior, moda de lujo, descubrimiento). Fuera de la tabla el factor es 1,0.

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

Cada mineral pertenece a **2 o más** de los 6 sectores; los pesos suman 100. Cierra en lo numérico el reparto de [[05 Mundo y minerales|05]]; la lista de sectores de la economía los pesos quedan como están; [[F4-31 Sectores de demanda - ferrocarril, energía, militar|F4-31]] construye el modelo y los eventos sin cambiar el modelo.

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

Dentro del rango orientativo +20–40 % de [[03 Comercio y mercado|03]], variable por mineral. Con el trato de Casilda ([[23 Árbol de decisiones y consecuencias|23]]) la Aetherita sube a 40–45 %. La prima de la Aetherita solo se cobra en sus encargos especiales (sección 3.1): el resto de la Aetherita se vende en el canal legal de la Comisión. Como el mercado negro tampoco paga el 3 % de impuesto, la ganancia real frente al mercado normal es la prima más ≈ 4 %.

### 3.7 Mezcla de menas por zona y agotamiento ✅

Probabilidad (%) de que una mena sea de cada mineral. Con herramienta insuficiente escaneas y saltas esa mena (no se extrae; descartarla cuesta el 25 % de su energía). Respeta el mineral principal y secundario de cada zona en [[02 Extracción|02]].

| Zona | Mezcla |
|---|---|
| 1 · Galerías del Hollín | carbón 70 · hierro 30 |
| 2 · Cañón Ferroso | hierro 55 · carbón 20 · cobre 25 |
| 3 · Minas de Sierra Alta | cobre 40 · plata 35 · hierro 15 · oro 10 |
| 4 · Salares del Litoral | salitre 55 · cuarzo 25 · plata 20 |
| 5 · Cavernas de Cristal (profunda) | cuarzo 30 · oro 25 · esmeralda 25 · diamante 10 · plata 10 |
| 6 · La Fosa del Éter (profunda, 3 días por semana) | Aetherita 40 · diamante 35 · esmeralda 15 · oro 10 |

**Descartar una mena ✅ (decisión del autor, 2026-10-15).** Escaneada una mena, puedes extraerla o descartarla. **Descartar cuesta el 25 % de la energía que habría costado extraerla** (también si tu herramienta no puede con ella). Con el descarte gratis, el jugador solo minaba lo de mayor valor por energía; con este costo el simulador mide una pérdida de ingreso de ≈ 23 % frente a descartar gratis y de ≈ 3 % adicional si el costo se duplicara (sección 13, C5).

**Agotamiento de zona ✅** (regla de [[01 Core loop y ciclo del día|01]] y [[02 Extracción|02]]: las menas se agotan y regeneran). Cada zona tiene una **riqueza** de 40 a 100 % que multiplica el rendimiento y que empieza en 100 %. Cada expedición la baja **6 puntos**, cada día sube **3**, con suelo del 40 %. Una zona sostiene **0,5 expediciones al día** sin empobrecerse; un jugador medio hace 2,5 al día repartidas en 4–5 zonas, así que en régimen la riqueza media al salir es **≈ 59 % (II) · 65 % (III) · 94 % (IV)**, ya incluida en los ingresos de la sección 2. Quien repite una sola zona cae al suelo (40 %) y rinde entre un 5 % (II) y un 27 % (IV) menos que quien rota. Ciclo de regeneración completo (de 40 a 100): 20 días.

---

## Fuente

`studio/docs/28-numeros-base-de-la-economia.md:80`
