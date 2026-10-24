---
id: "doc-28-s08"
tipo: "seccion"
title: "8 · Empleados ✅"
aliases: ["doc-28-s08"]
documento: "[[28 Números base de la economía]]"
limpieza: 100
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[28 §7 Deuda del Acto I y sus nombres]]"
siguiente: "[[28 §9 Información, viaje, pedidos y contratos]]"
arriba: "[[28 Números base de la economía]]"
fuente: "studio/docs/28-numeros-base-de-la-economia.md:417"
generado: true
---

# 8 · Empleados ✅

> Un empleado tiene la misma energía y herramienta que tú, pero rinde una fracción de lo que tú sacarías (Eficiencia). Nivel = Eficiencia +…

← [[28 §7 Deuda del Acto I y sus nombres]] · [[28 Números base de la economía|↑ 28]] · [[28 §9 Información, viaje, pedidos y contratos]] →

### 8.1 Rendimiento y niveles

Un empleado tiene la **misma energía y herramienta** que tú, pero **rinde una fracción** de lo que tú sacarías (Eficiencia). Nivel = Eficiencia + qué tier puede extraer:

| Nivel | Eficiencia (parte de lo que sacaría el jugador) | Tier máximo |
|---|---|---|
| N1 | 30 % | 2 |
| N2 | 38 % | 2 |
| N3 | 42 % | 3 |
| N4 | 46 % | 4 |
| N5 | 50 % | 4 |

La Aetherita, nunca. «Nivel alto» ([[04 Progresión y meta|04]]) = **N4 y N5** (tier 4: gemas). Un empleado también agota la zona, en proporción a su Eficiencia (6 × Eficiencia puntos por expedición). En el Acto IV su papel es residual: no se toca la economía del IV.

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

Aporte bruto de **un** Minero (esquirlas por día) medido con el simulador ([[F0-53 Simulador de economía y progresión con reglas de equilibrio|F0-53]], regla G1; incluye su huella sobre la riqueza de la zona y el mercado, el desgaste que paga el jugador y el jugador presente; sin heridas ni robo, que van aparte en 8.4):

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

## Fuente

`studio/docs/28-numeros-base-de-la-economia.md:417`
