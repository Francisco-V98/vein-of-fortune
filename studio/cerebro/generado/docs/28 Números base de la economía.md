---
id: "doc-28"
tipo: "documento"
title: "28 · Números base de la economía"
aliases: ["doc-28"]
estado: "con-abiertos"
limpieza: 91
ok: 43
propuestas: 4
abiertos: 4
espera: 13
secciones: 14
arriba: "[[MOC Documentos]]"
fuente: "studio/docs/28-numeros-base-de-la-economia.md:1"
generado: true
---

# 28 · Números base de la economía

> Limpieza 91 % · 4 abiertos · 14 secciones

Referencia única de las cifras de la economía de Veta de Fortuna: escalas, tiempo, ritmo, minerales, energía, herramientas, frenos de mercado, deuda, empleados, información, vigilancia, estilo de vida y reglas por dificultad. Nace de la tarea [[F0-52 Modelo económico - números base|F0-52]] y de las cinco rondas de decisión del autor (2026-10-15). Las reglas que producen estos números están en [[01 Core loop y ciclo del día|01]], [[02 Extracción|02]], [[03 Comercio y mercado|03]] y [[04 Progresión y meta|04]]; los mismos números viven en la sección `economy` y en los minerales y zonas de `studio/data/world.json`.

**Estado.** ✅ Las cifras de este documento son **decisión del autor** y las verificó el simulador de [[F0-53 Simulador de economía y progresión con reglas de equilibrio|F0-53]] (`tools/sim`, sección 13). El 2026-10-16 el autor aprobó los ajustes que propuso el simulador y están aplicados aquí y en `world.json`; Los cuatro puntos que dejó abiertos el Picado ampliado (ritmo del III, mejora del pico a nivel 2, piso de Comerciante y pares previstos de G1) también están aprobados y aplicados. Las decisiones del autor ya incorporadas: canal legal de la Aetherita en Puerto Meridiano, descartar menas, tienda y pedidos con mercancía propia, pedidos fuera del Acto I, empleados, Picado ampliado y aviso a los Mineros en el IV. Si una cifra cambia, se cambia aquí y en `world.json` a la vez y se vuelve a ejecutar el simulador (`python3 tools/sim/run.py --completo --escribir`). Moneda: **esquirlas** (singular «esquirla»; solo enteros, sin subunidad). ⏳ [[F2-20 Pantallas placeholder - día, mina, mercado y tienda en|F2-20]] El símbolo o la abreviatura de la moneda en pantalla no está decidido: hasta entonces se escribe «esquirlas» completo.

**Cómo está construido el modelo (en una frase).** El Acto I fija la escala (una expedición vale ≈ 250–350 esquirlas y la cuota del día 7, 960); cada acto multiplica el ritmo por ≈ 3–5 (por energía, por herramienta y por mineral de mayor tier); y lo que impide que una estrategia domine son seis frenos: spread con impuesto, profundidad del mercado, agotamiento de la zona, desgaste, vigilancia y topes diarios.

---

## Secciones

1. [[28 §1 Escalas]] — Regla de redacción para 03, 22, 23 y 27: el «%» y el «punto» de mercado coinciden por construcción (1 punto = 1 % del precio base), el…
2. [[28 §2 Ritmo objetivo y patrimonio]] — «Ingreso neto» = ventas − desgaste − impuestos − viajes. No incluye cuotas, salarios ni compras de mejoras. «Hora» es tiempo de día de…
3. [[28 §3 Los diez minerales]] — Rendimiento: unidades de mineral dominante por mena con resultado «bueno» y herramienta de nivel 1. Resultados (4): perfecto ×1,5 · bueno…
4. [[28 §4 Energía]] — Comprobación del arranque del guion: con 28 de energía, el carbón (8) da 3 menas y el hierro (10) da 2: «2 a 3 menas». Una expedición de…
5. [[28 §5 Herramientas]] — Cuatro tipos con 5 niveles (pico, taladro, cincel y criba) más el explosivo (consumible con 5 potencias): son los «5 tipos × 5 niveles». Un…
6. [[28 §6 Frenos de mercado]] — Licencias (renovación cada 28 días; F4-213 las construye): Minero con licencia 150 · Comerciante 900 · Empresario 4 500 · Magnate 17 000 (≈…
7. [[28 §7 Deuda del Acto I y sus nombres]] — «La deuda de Reme» eran varias deudas distintas. Cada una tiene ahora su nombre:
8. [[28 §8 Empleados]] — Un empleado tiene la misma energía y herramienta que tú, pero rinde una fracción de lo que tú sacarías (Eficiencia). Nivel = Eficiencia +…
9. [[28 §9 Información, viaje, pedidos y contratos]] — La prensa completa cuesta ≈ 890 por mes (≈ 1,5 % del ingreso mensual del Acto II).
10. [[28 §10 Vigilancia, multas, mercado negro y mora]] — Se multiplican por el factor f de dificultad (0,7 · 1 · 1,4 · 2).
11. [[28 §11 Estilo de vida V1]] — Orden de magnitud; el patrimonio no lo cuenta (sección 2).
12. [[28 §12 Reglas por dificultad]] — Solo la regla; los valores finos son de F3-22. Los números de este documento son los de Intermedio.
13. [[28 §13 Validación con el simulador (F0-53)]] — Estado. El simulador mide las cifras de este documento y el autor aprobó el 2026-10-16 todos los ajustes que propuso (ya aplicados en las…
14. [[28 §Documentos relacionados]] — 01 bucle de juego · 02 extracción · 03 comercio · 04 progresión · 05 minerales · 06 evolutivos · 09 minijuegos · 15 regla de lo diferido ·…

## Puntos abiertos

- [[28 §2 Ritmo objetivo y patrimonio]] (línea 58): «Ingreso neto» = ventas − desgaste − impuestos − viajes. No incluye cuotas, salarios ni compras de mejoras. «Hora» es tiempo de día de juego (13 min por día, sin escenas) y el objetivo de cada acto es
- [[28 §4 Energía]] (línea 219): Objetivo por acto (curva de F3-11) / I: 28–30 · II: 40 · III: 62 · IV: 80. 🟡 La curva sube linealmente desde el valor del acto anterior y llega al objetivo al 70 % del acto ()
- [[28 §9 Información, viaje, pedidos y contratos]] (línea 528): Frecuencia fuera del Acto I ✅ (decisión del autor, 2026-10-15). El Acto I está guionizado. Desde el II llega un pedido estándar cada 2 días (de 1 a 2 días de producción media, +12 %) y un urgente por 

## Relaciones

- **Aplazados a:**
  - [[F0-78 Diseñar el diario, la cola de historia y la misión de]]
  - [[F3-06 Bots agregados con 4 arquetipos]]
  - [[F3-07 Refinado y taller - lingotes y productos básicos]]
  - [[F3-11 Stats por uso e hitos (5 stats)]]
  - [[F3-22 Selector de dificultad con parámetros]]
  - [[F4-154 Viaje entre regiones - costo en dinero y zonas profundas]]
  - [[F4-31 Sectores de demanda - ferrocarril, energía, militar]]
  - [[F4-39 Ajuste de los 4 arquetipos de bots con los 10 minerales]]
  - [[F4-72 Mercado negro - operación nocturna con volumen limitado]]
- **Enlaza a:**
  - [[01 Core loop y ciclo del día]]
  - [[02 Extracción]]
  - [[03 Comercio y mercado]]
  - [[04 Progresión y meta]]
  - [[22 Acto II - las tres variantes de Reme]]
  - [[23 Árbol de decisiones y consecuencias]]
  - [[27 Guion del Acto I, día a día]]
  - [[17 Mapa de historia]]
  - [[25 Finales y epílogos]]
  - [[05 Mundo y minerales]]
  - [[06 Roadmap, ideas futuras y pendientes]]
  - [[24 Umbrales de acto]]
  - [[26 Zonas y edificios]]
  - [[09 Minijuegos]]
  - [[15 Flujo de trabajo y calidad]]
- **Citado por:**
  - [[01 Core loop y ciclo del día]]
  - [[02 Extracción]]
  - [[03 Comercio y mercado]]
  - [[04 Progresión y meta]]
  - [[05 Mundo y minerales]]
  - [[06 Roadmap, ideas futuras y pendientes]]
  - [[07 Sociedad, poder y eventos]]
  - [[08 Historia y personaje]]
  - [[09 Minijuegos]]
  - [[17 Mapa de historia]]
  - [[18 Biblia narrativa]]
  - [[19 Elenco a fondo]]
  - [[22 Acto II - las tres variantes de Reme]]
  - [[23 Árbol de decisiones y consecuencias]]
  - [[24 Umbrales de acto]]
  - [[25 Finales y epílogos]]
  - [[26 Zonas y edificios]]
  - [[27 Guion del Acto I, día a día]]

## Fuente

`studio/docs/28-numeros-base-de-la-economia.md:1`
