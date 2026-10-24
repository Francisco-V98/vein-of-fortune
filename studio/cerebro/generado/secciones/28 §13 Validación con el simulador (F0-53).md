---
id: "doc-28-s13"
tipo: "seccion"
title: "13 · Validación con el simulador (F0-53) ✅"
aliases: ["doc-28-s13"]
documento: "[[28 Números base de la economía]]"
limpieza: 100
abiertos: 0
espera: 9
aplazado_a: ["[[F0-78 Diseñar el diario, la cola de historia y la misión de]]", "[[F3-06 Bots agregados con 4 arquetipos]]", "[[F3-07 Refinado y taller - lingotes y productos básicos]]", "[[F3-11 Stats por uso e hitos (5 stats)]]", "[[F3-22 Selector de dificultad con parámetros]]", "[[F4-31 Sectores de demanda - ferrocarril, energía, militar]]", "[[F4-39 Ajuste de los 4 arquetipos de bots con los 10 minerales]]", "[[F4-72 Mercado negro - operación nocturna con volumen limitado]]"]
estado: "con-aplazados"
anterior: "[[28 §12 Reglas por dificultad]]"
siguiente: "[[28 §Documentos relacionados]]"
arriba: "[[28 Números base de la economía]]"
fuente: "studio/docs/28-numeros-base-de-la-economia.md:606"
generado: true
---

# 13 · Validación con el simulador (F0-53) ✅

> Estado. El simulador mide las cifras de este documento y el autor aprobó el 2026-10-16 todos los ajustes que propuso (ya aplicados en las…

← [[28 §12 Reglas por dificultad]] · [[28 Números base de la economía|↑ 28]] · [[28 §Documentos relacionados]] →

**Estado.** ✅ El simulador mide las cifras de este documento y el autor aprobó el 2026-10-16 todos los ajustes que propuso (ya aplicados en las secciones 1 a 12 y en `world.json`). Con ellas, de las 50 reglas de equilibrio 50 pasan, 0 fallan y 0 son inciertas. El Picado ampliado obligó a cuatro ajustes más (13.4), que el autor también aprobó y están aplicados.

### 13.1 Qué es y cómo se ejecuta

- **Código** en `tools/sim/` (solo biblioteca estándar de Python): `mundo.py` lee **todas** las cifras de `world.json` y calcula la **huella** de las claves que usa; `mercado.py` es el mercado de referencia, con una interfaz que [[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y|F2-04]] y [[F2-08 Simulador por consola de miles de días|F2-08]] pueden sustituir por el real; `jugador.py`, `campana.py`, `reglas.py` e `informe.py` hacen el resto. No hay cifras del juego en el código (una prueba lo comprueba).
- **Datos** en `studio/data/sim/`: `supuestos.json` (perfiles, semillas, tamaños de corrida, mutaciones y supuestos de modelado), `reglas.json` (las 50 reglas con su umbral, su origen —`doc` si sale de un documento aprobado, `prop.` si lo propuso el simulador y el autor lo aceptó— y la trazabilidad requisito → regla) y `resultados.json` (lo que mide el simulador; lo muestra el hub en `#/simulador`).
- **Cómo se ejecuta:** `python3 tools/sim/run.py --rapido` (≈ 33 s medidos en esta máquina, el que corre en CI; no incluye la regla I2 de mutaciones, que añade ≈ 45 s con `--mutaciones` y siempre corre en el modo completo; la prueba de I2 está en `tools/ci`) y `python3 tools/sim/run.py --completo --escribir` (60 semillas, 6 000 corridas del Acto I, 800 corridas para el ritmo del medio, 10 000 días tras el IV; ≈ 16 minutos; reescribe `resultados.json`). Si cambia una cifra que el simulador lee, la huella cambia, los resultados caducan y `build.py --strict` falla hasta que se reejecuta.
- **Perfiles:** lento (probabilidades 5/40/35/20 y 4 expediciones en el Acto I), medio (15/50/25/10 y 5), rápido (30/50/15/5 y 9) y **optimizador** (el «modelo atento»: compra cada mejora en cuanto se paga y busca bucles). La duración de cada acto sale de la tabla de la sección 2: lento = máximo de horas, medio = media, rápido = mínimo. «Hora» es tiempo de día de juego (13 min por día, sin escenas) ✅.
- **Qué modela:** menas enteras con descarte y resultado de cada una, zonas que se agotan, tienda (solo mercancía propia), pedidos, mercado spot y Bolsa con spread, impuesto, slippage y tope por comprador, mercado negro con vigilancia, multas, redadas, sobornos, guardias y Faroleros, Aetherita por el canal legal y por encargos especiales (también la variante de Casilda), empleados (Mineros y Dependiente), mejoras de herramientas elegidas por su recuperación, deuda con abono anónimo, recargos y mora, y estilo de vida. Reproduce el prototipo de [[F0-52 Modelo económico - números base|F0-52]] dentro del 5 % (B8).

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
| B8 | El simulador reproduce el prototipo de [[F0-52 Modelo económico - números base\|F0-52]] | ≤ 5 % | Prototipo IIe frente a 6300 esq/h: 0,9 % | pasa |
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
- **Mercado negro.** Prudente (parar en vigilancia 30): +6,9 % (II), +6,6 % (III) y +7,1 % (IV) del ingreso honesto; la mejor de 60 políticas, +9,0 %; abusivo: −15 % con una redada cada 11–13 días. Una noche negra puede costar hasta 0,97 · 0,95 · 0,85 bloques antes de dejar de compensar (insumo para ⏳ [[F4-72 Mercado negro - operación nocturna con volumen limitado|F4-72]]).
- **Deuda.** La vía del 25 % falta 0,3 h de ingreso del Acto II sin pagos extra y la del 50 % 0,14 h del III; se alcanzan en el 100 % de las corridas. Comerciante + 25 % tarda 6,1 h del Acto II (límite 6,5 h). La mora nunca cierra una puerta; ponerse al corriente tras 12 semanas de atraso cuesta 2–3 semanas.
- **Misión de rescate (⏳ [[F0-78 Diseñar el diario, la cola de historia y la misión de|F0-78]]).** Horas de juego acumuladas tras las que debería llegar: **13,5 h** para la puerta A5 y **26,5 h** para el círculo (1,25 × el percentil 95 del jugador lento, a 0,5 h; [[Misión de rescate|economy.rescue_mission]]).

### 13.4 Ajustes que trajo el Picado ampliado

Ampliar el Picado a cobre, plata y oro aceleró el Acto III y abarató el pico; el simulador propuso cuatro ajustes y el autor los aprobó el 2026-10-16:

| Regla | Medido antes del ajuste | Ajuste aplicado |
|---|---|---|
| B1 · ritmo del medio en el III | 32 000 por hora, un 21 % sobre 27 000 | Objetivo del III de 27 000 a **33 000** |
| C1 · la mejora más rápida se paga en ≥ 1 expedición | 0,93 (pico a nivel 2) | Mejoras de nivel 2: pico **480**, criba 528, taladro 600, cincel 720 |
| B4 · Comerciante entre el 60 y el 90 % del Acto II | 60,5 %, incierta | Piso de Comerciante de 14 000 a **15 000** |
| G1 · salario ÷ aporte del N1 en el II | 58,6 %, incierta (aporta poco y con ruido) | El N1 sale de los pares previstos; sigue en «todos ≤ 100 %» |

### 13.5 Lo que el simulador no modela

El refinado y las recetas (valor agregado 0 hasta ⏳ [[F3-07 Refinado y taller - lingotes y productos básicos|F3-07]]), los bots y el mercado interno (⏳ [[F3-06 Bots agregados con 4 arquetipos|F3-06]] y ⏳ [[F4-39 Ajuste de los 4 arquetipos de bots con los 10 minerales|F4-39]]), el modelo real de sectores y eventos (⏳ [[F4-31 Sectores de demanda - ferrocarril, energía, militar|F4-31]]: los eventos del simulador son sueltos, de un solo mineral), el coste en bloques de una noche negra (⏳ [[F4-72 Mercado negro - operación nocturna con volumen limitado|F4-72]]: F5 da el máximo que compensa), la curva real del Aguante (⏳ [[F3-11 Stats por uso e hitos (5 stats)|F3-11]]), los valores de dificultad (⏳ [[F3-22 Selector de dificultad con parámetros|F3-22]]), los minijuegos más allá de sus cuatro probabilidades, la prensa más allá de su precio, los encuentros, las relaciones y los logros. Cuando [[F2-04 Modelo de precio - valor justo, oferta y demanda, ruido y|F2-04]] y [[F2-08 Simulador por consola de miles de días|F2-08]] construyan el mercado real, se reejecutan las reglas E.

---

## Fuente

`studio/docs/28-numeros-base-de-la-economia.md:606`
