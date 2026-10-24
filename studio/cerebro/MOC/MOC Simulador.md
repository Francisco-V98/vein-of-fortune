---
id: "moc-simulador"
tipo: "moc"
title: "Simulador"
aliases: ["moc-simulador"]
arriba: "[[00 Inicio]]"
generado: true
---

# Simulador

> Las reglas de equilibrio de la economía y su resultado en el simulador.

50 reglas de equilibrio medidas con el simulador (`tools/sim`, tarea [[F0-53 Simulador de economía y progresión con reglas de equilibrio]]): 50 pasa.

Resumen: [[Resultados del simulador]] · supuestos: [[Supuestos del simulador]].

## A · Acto I y deuda

| Regla | Estado | Umbral |
|---|---|---|
| [[A1 Cuota del día 7 sin mejora]] | pasa | pago 95–99,9 % · margen 30–75 % de la cuota |
| [[A2 Ahorrar o mejorar el día 5]] | pasa | margen con mejora ≥ 10 % · diferencia 8–45 pp · pago con mejora ≥ 80 % |
| [[A3 El lento no es imposible ni trivial]] | pasa | 4 exp.: 10–60 % · 5 exp.: ≥ 60 % · cierra el acto · día 14 ≥ 90 % |
| [[A4 El rápido paga con holgura]] | pasa | pago ≥ 99,9 % · margen 100–300 % |
| [[A5 Ingreso neto por hora del Acto I]] | pasa | ≤ 20 % |
| [[A6 Cuota del día 14 y recargos en las cuatro dificultades]] | pasa | Novato e Intermedio ≤ 30 % · Difícil ≤ 55 % · Hardcore ≤ 60 % |
| [[A7 Saldar la deuda antes del día 8 es imposible]] | pasa | < 100 % de K |

## B · Ritmo, progresión y estatus

| Regla | Estado | Umbral |
|---|---|---|
| [[B1 Ritmo por acto de la campaña completa]] | pasa | ±20 % del objetivo · medio = 60–80 % del optimizador · lento < medio < rápido · rápido/lento ≤ 4 |
| [[B2 Crecimiento razonable entre actos]] | pasa | I < II < III < IV · razones 3–5 (I→II hasta 7) · rampa ≤ ×3,5 |
| [[B3 Patrimonio al cierre de cada acto]] | pasa | Acto I dentro de 600–1 000 (rápido ±25 % de 2 300) · II, III, IV ±25 % · sumideros ±40 % · lento ≥ 50 % del medio |
| [[B4 Los estatus se alcanzan a tiempo]] | pasa | ≥ 95 % de las corridas · entre el 60 y el 90 % del acto · Magnate antes del cierre |
| [[B5 El optimizador no se salta el techo de herramienta]] | pasa | ≥ 90 % de las corridas con nivel ≤ guía del acto + 1 |
| [[B6 Sumideros recurrentes]] | pasa | prensa ≈ 1,5 % · licencias 1,5–3 % · viaje 3–5 % (II) y ≈ 1 % (IV) · reparación 7–9 % · renta ≤ 5 % |
| [[B7 La economía no explota tras el Acto IV]] | pasa | crecimiento ≤ 10 % · identidad exacta · ≤ techo × 1,05 |
| [[B8 El simulador reproduce el prototipo de F0-52]] | pasa | ≤ 5 % |

## C · Herramientas

| Regla | Estado | Umbral |
|---|---|---|
| [[C1 Cada mejora se paga en pocas expediciones]] | pasa | la mejor mejora de cada nivel se paga en 1–8 expediciones |
| [[C2 Cadencia de mejoras]] | pasa | 0,3–3 h |
| [[C3 Reparar cuesta 7–9 % del valor bruto]] | pasa | 6–10 % |
| [[C4 El explosivo apenas compensa]] | pasa | medio ≤ +5 % · rápido ≤ +25 % |
| [[C5 Descartar una mena tiene un costo real]] | pasa | pérdida 3–35 % · al doblar el costo pierde ≥ 1 % más · ≤ 60 % de las menas descartadas |

## D · Zonas

| Regla | Estado | Umbral |
|---|---|---|
| [[D1 Ninguna zona es siempre la óptima]] | pasa | mejor zona ≤ 65 % · mejor fija ≤ 100 % de la adaptativa · ≥ 3 zonas con ≥ 15 % de uso |
| [[D2 Agotamiento de las zonas]] | pasa | 59 · 65 · 94 % ±5 pp · repetir pierde ≥ 5 % |
| [[D3 La Fosa y la Aetherita no mandan]] | pasa | ≤ 3 por semana · Aetherita ≤ 60 % de las ventas |

## E · Mercado y bucles

| Regla | Estado | Umbral |
|---|---|---|
| [[E1 Sin ganancia segura entre canales]] | pasa | ninguna ganancia fuera del negro · negro ≤ 15 % del ingreso diario |
| [[E2 Impacto del jugador en el precio]] | pasa | w crece de 0,5 a 4 · slippage creciente (o estable, ≥ 0,9×) y ≤ 12 % en el IV · w por acto ±15 % |
| [[E3 Sin bucle de impacto]] | pasa | < 0 en todo el rango |
| [[E4 La especulación no domina]] | pasa | spot ≤ +2,5 % · Bolsa ≤ +7 % · estación ≤ +12 % · trader ≤ 25 % del ingreso minero |
| [[E5 Volatilidad y topes diarios]] | pasa | ±10 % · orden respetado · ≤ 6 % de los días en el tope |
| [[E6 Tope por comprador y capacidad del almacén]] | pasa | ±10 % del ritmo |
| [[E7 Los pedidos son un complemento]] | pasa | > 0 y ≤ 15 % del ingreso |

## F · Mercado negro y vigilancia

| Regla | Estado | Umbral |
|---|---|---|
| [[F1 Mercado negro prudente]] | pasa | +3 a +12 % |
| [[F2 Barrido de políticas del mercado negro]] | pasa | ≤ +12 % |
| [[F3 El mercado negro abusivo pierde]] | pasa | < 0 % · una redada cada 11 ± 3 días |
| [[F4 Aetherita en el Acto IV - canal legal con tope\|F4 Aetherita en el Acto IV: canal legal con tope]] | pasa | legal ≥ 90 % de las ventas · encargo cada ≥ 14 días y ≤ 2 viales · vigilancia ≤ 25 % de la bajada natural |
| [[F5 Cuánto cuesta una noche negra en bloques]] | pasa | informativa (> 0) |

## G · Empleados

| Regla | Estado | Umbral |
|---|---|---|
| [[G1 El empleado no domina - salario frente a aporte\|G1 El empleado no domina: salario frente a aporte]] | pasa | pares previstos 40–60 % (N2 del II; N4 y N5 del III) · todos ≤ 100 % (también N1) · 7 días ≤ 85 % · aporte neto en el IV ≤ 0 |
| [[G2 La plantilla máxima no domina]] | pasa | bruto ≤ 70 % · neto ≤ 45 % del jugador solo |
| [[G3 El jugador ausente rinde menos]] | pasa | plantilla sola ≤ 65 % · jugador + plantilla ≥ solo + 5 % |
| [[G4 El Dependiente aporta, pero poco]] | pasa | > 0 y ≤ 35 % (II y III) |
| [[G5 Entrenar y ascender no es un bucle]] | pasa | retorno ≥ 5 días, sin máximo |
| [[G6 Riesgo de los empleados]] | pasa | informativa (≤ 100 % del aporte) |

## H · Deuda, mora y rescate

| Regla | Estado | Umbral |
|---|---|---|
| [[H1 Vía de deuda del 25 % en el Acto II]] | pasa | falta ≤ 0,5 h · alcanzable · Comerciante + 25 % ≤ 6,5 h |
| [[H2 Vía de deuda del 50 % en el círculo]] | pasa | falta ≤ 0,3 h |
| [[H3 Abonos anónimos y Consorcio]] | pasa | mismo capital · abono < interés · Consorcio ≤ 30 % de K y queda ≥ 50 % |
| [[H4 La mora no cierra puertas]] | pasa | ≤ 2 · 3 · 4 semanas · Hardcore día 14 ≤ 40 % del ingreso del lento |
| [[H5 Variantes de A2 con el lento]] | pasa | caja < 0 a lo sumo una semana · vía alcanzable |
| [[H6 Misión de rescate - horas de juego\|H6 Misión de rescate: horas de juego]] | pasa | entrega de la cifra (informativa) |

## I · Meta-casos

| Regla | Estado | Umbral |
|---|---|---|
| [[I1 Determinismo]] | pasa | idéntico |
| [[I2 Mutaciones]] | pasa | 100 % de las reglas |
| [[I3 Intervalos visibles y ninguna regla incierta]] | pasa | 0 |

## Relaciones

- **Perfiles:** [[Perfil Lento]], [[Perfil Medio]], [[Perfil Rápido]], [[Perfil Optimizador]]
- **Documento:** [[28 §13 Validación con el simulador (F0-53)]]
