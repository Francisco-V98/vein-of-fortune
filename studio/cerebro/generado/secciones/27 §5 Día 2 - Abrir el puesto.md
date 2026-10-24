---
id: "doc-27-s05"
tipo: "seccion"
title: "5 · Día 2 · Abrir el puesto ✅"
aliases: ["doc-27-s05"]
documento: "[[27 Guion del Acto I, día a día]]"
limpieza: 100
abiertos: 0
espera: 2
aplazado_a: ["[[F3-14 Personalización del protagonista]]", "[[F3-31 Diez noticias iniciales y seis eventos del Acto I]]"]
estado: "con-aplazados"
anterior: "[[27 §4 Día 1 - La llave]]"
siguiente: "[[27 §6 Día 3 - El hierro]]"
arriba: "[[27 Guion del Acto I, día a día]]"
fuente: "studio/docs/27-guion-del-acto-i.md:182"
generado: true
---

# 5 · Día 2 · Abrir el puesto ✅

> Reabrir el puesto es el trámite de Quiroga más la primera venta, el jugador pone nombre a la tienda al colgar el cartel y la cinta 1 está…

← [[27 §4 Día 1 - La llave]] · [[27 Guion del Acto I, día a día|↑ 27]] · [[27 §6 Día 3 - El hierro]] →

**Estado:** cerrada. Reabrir el puesto es el trámite de Quiroga más la primera venta, el jugador pone nombre a la tienda al colgar el cartel y la cinta 1 está en el doble fondo del cajón de la caja. El margen, el orden de los bloques y la primera noticia los confirmó el autor el 2026-10-16 ([[F0-86 Pasada de cierre - guion del Acto I (27)|F0-86]]).

| Campo | Contenido |
|---|---|
| Se aprende | La tienda: surtir los estantes y fijar los precios |
| Decisión | Principal: el **margen**, que por defecto es del 20 %: precio de lista = valor justo × 1,20, y el cliente medio paga × 1,15 ✅ ([[28 Números base de la economía\|28]], `world.json`). Menor: el **nombre de la tienda**, al colgar el cartel (la pantalla, ⏳ [[F3-14 Personalización del protagonista\|F3-14]]) |
| Lo cierra | La primera venta y el cierre de caja; el puesto queda reabierto |
| Si no haces lo esperado | Sin ir a Quiroga, el puesto sigue cerrado y la escena espera. Mientras tanto vendes al contado en el mercado, con peor precio |
| Sin dinero | Quiroga cobra su gestión (240 esquirlas) con la primera venta; si no alcanza, Reme la fía como «fiado de la gestión», sin interés y fuera de la deuda de la herencia (se paga junto con la siguiente cuota) ✅ |

**Líneas de ejemplo**

| Escena | Bloque | Qué pasa | Quién habla |
|---|---|---|---|
| [[d2.1 El trámite\|d2.1]] El trámite | Mañana | Quiroga pone el puesto a tu nombre. Lo llama «gestión» y la cobra con la primera venta | **Quiroga:** «Es un simple trámite, estimado (estimada). Tan simple que me da pena cobrarlo.» |
| [[d2.2 Surtir los estantes\|d2.2]] Surtir los estantes | Tarde | Es la mecánica **Reponer**: arrastras la mercancía a los estantes (con mando, eliges estante y mercancía) y fijas el precio ✅ ([[03 Comercio y mercado\|03]], [[09 Minijuegos\|09]]). Colocas el carbón de ayer (o el saco que dejó Anselmo en la trastienda) | **Narrador:** «Queda un saco de carbón en la trastienda. Dos años de polvo y sigue negro.» |
| [[d2.3 La primera venta\|d2.3]] La primera venta | Tarde | Llega un cliente obrero. Vendes, eliges el margen y cuelgas el cartel con el nombre. El puesto queda **reabierto** | **Cliente:** «¿Es verdad que reabren el puesto? Aquí compraba mi padre.» |
| [[d2.4 Cierre de caja\|d2.4]] Cierre de caja | Noche | El puesto ya cerró y no se vende: solo cuadras la caja. El cajón de la caja se atasca; debajo del doble fondo hay un carrete con el número 1 y aparece el aviso «Encontraste una cinta» | **Narrador:** «El cajón suena hueco. Debajo hay un carrete con un número: 1.» |

- **Noticia guionizada (la primera, de ⏳ [[F3-31 Diez noticias iniciales y seis eventos del Acto I|F3-31]]):** el Heraldo dice que el abasto de carbón está garantizado, pero que el frío llega antes (el día 1 es el 22 de otoño y el invierno empieza el día 8 ✅). El Teletipo trae el primer **rumor** y el carbón sube un poco en los dos bloques siguientes, así que el rumor era cierto. Los dos pasan por el mostrador, repartidos por el voceador. Es la noticia y el rumor del día, dentro del tope ✅.
  - **Heraldo:** «El Ministerio informa de que el frío llegará antes, pero el carbón está garantizado este invierno.»
  - **Teletipo:** «FRÍO ADELANTADO EN EL HOLLÍN. CARBÓN SUBIRÍA. SIN CONFIRMAR»
- **Hilos que se siembran:** [[La lámpara que Anselmo prestó al sobrino y la cinta 1|h-lampara-y-cinta-1]] ([[d2.4 Cierre de caja|d2.4]]) ✅ ([[23 Árbol de decisiones y consecuencias|23]], sección 7; `hilos.json`). Las demás escenas no siembran nada nuevo.
- **Sombras:** la cinta 1 ([[d2.4 Cierre de caja|d2.4]]). El saco de Anselmo ([[d2.2 Surtir los estantes|d2.2]]) no cuenta como sombra ✅.

---

## Fuente

`studio/docs/27-guion-del-acto-i.md:182`
