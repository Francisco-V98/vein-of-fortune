---
id: "n-i-reme-plazo.tarde"
tipo: "opcion"
title: "Pides una prórroga de una semana."
aliases: ["n-i-reme-plazo.tarde", "n-i-reme-plazo.b3"]
decision: "[[Pagar a Reme antes o después del plazo]]"
opcion: "tarde"
fija: ["[[Bandera pago reme]]"]
boton: "Pedir una semana más"
arriba: "[[Pagar a Reme antes o después del plazo]]"
tags: ["acto/I"]
fuente: "studio/data/decisions.json:99"
generado: true
---

# Pides una prórroga de una semana.

> Pides una prórroga de una semana.

## Efectos

- **Mundo:** En Novato e Intermedio toda la serie se desplaza una semana, con un recargo por cada semana de atraso (6 % de la cuota en Intermedio, 4 % en Novato), y no pagar equivale a pedirla. En Difícil y Hardcore la cuota atrasada se suma a la del día 14, con un recargo mayor (12 % y 18 %).
- **Mercado:** Recargo por cada semana de atraso ({recargo}): el 6 % de la cuota atrasada en Intermedio (58 esquirlas sobre la cuota del día 7, de 960); 12 % en Difícil y 18 % en Hardcore. Con 4 semanas de atraso acumuladas sube la tasa +1 pp hasta que pagues una cuota completa; nunca cierra una puerta.
- **Personajes:** Reme: te da el plazo con un consejo que suena a aviso.

**Botón:** «Pedir una semana más»

## Relaciones

- **Decisión:** [[Pagar a Reme antes o después del plazo]]
- **Fija o mueve:** [[Bandera pago reme]]

## Fuente

`studio/data/decisions.json:99`
