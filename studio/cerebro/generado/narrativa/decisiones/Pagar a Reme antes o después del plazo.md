---
id: "n-i-reme-plazo"
tipo: "nodo"
title: "Pagar a Reme antes o después del plazo"
aliases: ["n-i-reme-plazo"]
acto: "I"
nivel: "pequeña"
estado: "ok"
opciones: 3
fija: ["[[Bandera pago reme]]"]
lee: []
arriba: "[[MOC Decisiones]]"
tags: ["acto/I"]
fuente: "studio/data/decisions.json:72"
generado: true
---

# Pagar a Reme antes o después del plazo

> Acto I · decisión pequeña · 3 opciones

**Se dispara:** Vence la primera cuota de la deuda (el día 7; cada cuota vence cada 7 días). Puedes pagar antes desde el día 4.

## Opciones

| Opción | Qué haces | Fija |
|---|---|---|
| [[Pagar a Reme antes o después del plazo - antes]] | Pagas antes del plazo. | [[Bandera pago reme]] |
| [[Pagar a Reme antes o después del plazo - plazo]] | Pagas justo en el plazo. | [[Bandera pago reme]] |
| [[Pagar a Reme antes o después del plazo - tarde]] | Pides una prórroga de una semana. | [[Bandera pago reme]] |

## Relaciones

- **Opciones:** [[Pagar a Reme antes o después del plazo - antes]], [[Pagar a Reme antes o después del plazo - plazo]], [[Pagar a Reme antes o después del plazo - tarde]]
- **Fija o mueve:** [[Bandera pago reme]]
- **Cuello de botella:** [[Se cierra el Acto I]]
- **Acto:** [[Acto I - El recién llegado]]
- **Hilos que lo citan:** [[La deuda heredada y las cuotas cada 7 días]]
- **Escenas:** [[d7.2 La cuota]]

## Fuente

`studio/data/decisions.json:72`
