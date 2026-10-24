---
id: "moc-economia"
tipo: "moc"
title: "Economía"
aliases: ["moc-economia"]
arriba: "[[00 Inicio]]"
generado: true
---

# Economía

> Los números base de la economía: un bloque de world.json por nota, enlazado al documento 28.

Números base de la economía (docs/28-numeros-base-de-la-economia.md). Decididos por el autor como base a verificar en F0-53; se recalibran con el simulador completo. Moneda: Esquirlas (solo enteros). Precios por unidad; el total de cada operación se redondea una sola vez.

Fuente de verdad: `studio/data/world.json` (bloque `economy`); explicación en [[28 Números base de la economía]].

## Bloques

| Bloque | Cifras clave | Sección del 28 |
|---|---|---|
| [[Moneda]] | Esquirlas, solo enteros | [[28 §1 Escalas]] |
| [[Punto de mercado]] | 1 punto de mercado = 1 % del precio base | [[28 §1 Escalas]] |
| [[Tiempo]] | Día de 13 min, 3 bloques, mes de 28 días, año de 112 | [[28 §1 Escalas]] |
| [[Calendario]] | Empieza el día 1 en otono; la Fosa abre los días 2, 4, 6 | [[28 §1 Escalas]] |
| [[Expediciones]] | 1 bloque normal y 2 profunda; hasta 3 normales al día | [[28 §1 Escalas]] |
| [[Ritmo objetivo]] | Ingreso neto por hora, Acto I: 650 / 1 100 / 2 200 (lento, medio, rápido) | [[28 §2 Ritmo objetivo y patrimonio]] |
| [[Energía]] | Aguante base 28; por acto: I 28–30, II 40, III 62, IV 80 | [[28 §4 Energía]] |
| [[Herramientas]] | 4 tipos, 5 niveles; primer costo del pico 90 | [[28 §5 Herramientas]] |
| [[Mercado]] | Impuesto de venta 3 %; eventos de 2 a 12 puntos | [[28 §6 Frenos de mercado]] |
| [[Deuda del Acto I]] | Principal 24 000, interés 4 % al mes, primer pago 960 el día 7 | [[28 §7 Deuda del Acto I y sus nombres]] |
| [[Empleados]] | 5 niveles; sueldo diario de 70 a 720 | [[28 §8 Empleados]] |
| [[Mejoras de la tienda]] | 5 niveles: Puesto (0) → Puesto ampliado (3 500) → Tienda (18 000) → Casa comercial (90 000) → Emporio (450 000) | [[28 §8 Empleados]] |
| [[Información]] | 4 capas de información: Basica, Prensa, Analisis, Tabulador | [[28 §9 Información, viaje, pedidos y contratos]] |
| [[Viaje]] | 15 trayectos de 42 a 210 esquirlas | [[28 §9 Información, viaje, pedidos y contratos]] |
| [[Pedidos]] | Pedidos: estandar +12 %, urgente +35 %, negro +prima del mineral (20-35) %, largo-plazo +0 %, oficial +8 % | [[28 §9 Información, viaje, pedidos y contratos]] |
| [[Reglas de los pedidos]] | Solo bienes propios; como máximo el 15 % del ingreso | [[28 §9 Información, viaje, pedidos y contratos]] |
| [[Vigilancia]] | Niveles: tranquilo, observado, vigilado, bajo-investigacion | [[28 §10 Vigilancia, multas, mercado negro y mora]] |
| [[Estilo de vida]] | 4 casas de 4 000 a 450 000 esquirlas | [[28 §11 Estilo de vida V1]] |
| [[Dificultad]] | Dificultades: novato, intermedio, dificil, hardcore | [[28 §12 Reglas por dificultad]] |
| [[Validación]] | Verificado en F0-53; última simulación: tools/sim/run.py --completo (2026-10-16; resultados en studio/data/sim/resultados.json) | [[28 §13 Validación con el simulador (F0-53)]] |
| [[Deriva guionizada del Acto I]] | 2 derivas guionizadas: carbon, hierro | [[28 §6 Frenos de mercado]] |
| [[Guion económico del Acto I]] | Expediciones los días 1, 3, 4, 5, 6; mejora el día 5 | [[28 §2 Ritmo objetivo y patrimonio]] |
| [[Misión de rescate]] | Llega tras 13.5 h (puerta A5) y 26.5 h (círculo) | [[28 §13 Validación con el simulador (F0-53)]] |

## Relaciones

- **Documento:** [[28 Números base de la economía]]
