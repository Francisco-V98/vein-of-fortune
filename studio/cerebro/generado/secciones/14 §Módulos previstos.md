---
id: "doc-14-modulos-previstos"
tipo: "seccion"
title: "Módulos previstos 🟡"
aliases: ["doc-14-modulos-previstos"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Capas dentro de un módulo]]"
siguiente: "[[14 §Cómo se comunican los módulos]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:64"
generado: true
---

# Módulos previstos 🟡

> Cada módulo corresponde a un tema de diseño ya documentado. depende de son las únicas apis de otros módulos que puede usar; todo debe…

← [[14 §Capas dentro de un módulo]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Cómo se comunican los módulos]] →

Cada módulo corresponde a un tema de diseño ya documentado. `depende de` son las únicas *apis* de otros módulos que puede usar; todo debe quedar declarado en `architecture.json`.

| Módulo | Responsabilidad | Depende de | Documento |
|---|---|---|---|
| `day` | Días, bloques de tiempo y calendario | — | [[01 Core loop y ciclo del día\|01]] |
| `inventory` | Ítems, almacén, capacidad y costos | — | [[03 Comercio y mercado\|03]] |
| `market` | Precios, oferta y demanda, bots, spread | day | [[03 Comercio y mercado\|03]] |
| `extraction` | Zonas, menas, escáner, minijuegos y peligros | day, inventory | [[02 Extracción\|02]], [[09 Minijuegos\|09]] |
| `shop` | Tienda, ventas, contratos y regateo | market, inventory, day | [[03 Comercio y mercado\|03]] |
| `crafting` | Refinado y productos | inventory, market | [[03 Comercio y mercado\|03]] |
| `staff` | Empleados, contratos de trabajo y lealtad | day, extraction, shop | [[04 Progresión y meta\|04]] |
| `factions` | Alianza, los cuatro medidores de relación y vigilancia | day | [[07 Sociedad, poder y eventos\|07]] |
| `world_events` | Apagones, huelgas, saqueos y otros eventos | day, factions | [[07 Sociedad, poder y eventos\|07]] |
| `news` | Prensa: noticias, rumores y sesgos | world_events, market | [[03 Comercio y mercado\|03]] |
| `story` | Actos, diálogos, cintas y decisiones | day, factions, world_events | [[08 Historia y personaje\|08]] |
| `progression` | Stats por uso, estatus y logros | extraction, shop | [[04 Progresión y meta\|04]] |
| `lifestyle` | Casa, ropa, auto y cosméticos | progression, inventory | [[04 Progresión y meta\|04]] |
| `save` | Guardado versionado, con punto de control por acción y hasta 5 partidas guardables | — | [[01 Core loop y ciclo del día\|01]], [[10 Técnico y herramientas\|10]] |
| `telemetry` | Diagnóstico local exportable | — | [[10 Técnico y herramientas\|10]] |

El casino y los logros entrarán más adelante creando su propio módulo, sin tocar los demás. Los logros llegan a Steam a través del puerto de tienda.

El grafo es **acíclico**: ningún módulo puede depender, directa o indirectamente, de sí mismo (regla A7).

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:64`
