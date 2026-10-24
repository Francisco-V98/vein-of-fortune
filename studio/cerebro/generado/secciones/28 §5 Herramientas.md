---
id: "doc-28-s05"
tipo: "seccion"
title: "5 · Herramientas ✅"
aliases: ["doc-28-s05"]
documento: "[[28 Números base de la economía]]"
limpieza: 100
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[28 §4 Energía]]"
siguiente: "[[28 §6 Frenos de mercado]]"
arriba: "[[28 Números base de la economía]]"
fuente: "studio/docs/28-numeros-base-de-la-economia.md:236"
generado: true
---

# 5 · Herramientas ✅

> Cuatro tipos con 5 niveles (pico, taladro, cincel y criba) más el explosivo (consumible con 5 potencias): son los «5 tipos × 5 niveles». Un…

← [[28 §4 Energía]] · [[28 Números base de la economía|↑ 28]] · [[28 §6 Frenos de mercado]] →

### 5.1 Modelo y niveles

Cuatro tipos con 5 niveles (pico, taladro, cincel y criba) más el **explosivo** (consumible con 5 potencias): son los «5 tipos × 5 niveles». **Un nivel es un paquete:** cada nivel mejora a la vez rendimiento (minado), energía por mena, resistencia, carga y escáner; las cuatro categorías de [[02 Extracción|02]] son los componentes de cada paquete, no escaleras separadas. Cada tipo corresponde a un minijuego: pico (Picado), criba (Cribado), taladro (Perforación) y cincel (Cincelado).

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

**Mejorar no se paga solo en una expedición.** Medido con el simulador ([[F0-53 Simulador de economía y progresión con reglas de equilibrio|F0-53]], regla C1; cada mejora sube un solo tipo de herramienta y rinde solo en los minerales que ese tipo extrae), la **mejor mejora de cada nivel** se paga en **1,0 · 3,4 · 7,1 · 3,2 expediciones** (niveles 2 a 5; el costo total es dinero más mineral a precio base). Las otras de cada nivel son opcionales y más lentas (el pico a nivel 4 y 5 tarda 17 y 70 expediciones; criba nivel 4, 31). En el Acto I, mejorar el día 5 deja al jugador medio un margen del 45 % de la cuota (sección 7): «ahorrar o mejorar» es una decisión real.

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

Nivel por acto: 2 en el II, 3 en el III, 4 en el IV. Ancho final = ancho del detector × multiplicador del escáner de la herramienta × (1 − efecto del Ojo, [[F3-11 Stats por uso e hitos (5 stats)|F3-11]]).

---

## Fuente

`studio/docs/28-numeros-base-de-la-economia.md:236`
