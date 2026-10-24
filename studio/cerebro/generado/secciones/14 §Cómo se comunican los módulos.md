---
id: "doc-14-como-se-comunican-los-modulos"
tipo: "seccion"
title: "Cómo se comunican los módulos 🟡"
aliases: ["doc-14-como-se-comunican-los-modulos"]
documento: "[[14 Arquitectura y modularidad]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[14 §Módulos previstos]]"
siguiente: "[[14 §Presentación]]"
arriba: "[[14 Arquitectura y modularidad]]"
fuente: "studio/docs/14-arquitectura-y-modularidad.md:90"
generado: true
---

# Cómo se comunican los módulos 🟡

> Reglas de los eventos:

← [[14 §Módulos previstos]] · [[14 Arquitectura y modularidad|↑ 14]] · [[14 §Presentación]] →

| Mecanismo | Cuándo | Ejemplo |
|---|---|---|
| **API pública** (`api/`) | Pregunta síncrona: "dame un dato ahora" | `shop` pide a `market` el precio de venta actual |
| **Eventos de dominio** | Aviso: "pasó algo", sin saber quién escucha | `market` publica `PrecioCambiado`; `news` lo escucha |

Reglas de los eventos:

- Los define el módulo que los publica, dentro de su `api/`. Quien los escucha depende de esa `api`.
- Son **inmutables**, con nombre en pasado (`DiaAvanzado`, `HuelgaIniciada`) y llevan solo datos.
- Se entregan por un bus pequeño del `kernel`. No se usan para órdenes ("haz esto"): eso va por la API.
- Un evento nunca devuelve resultados a quien lo publica.

## Fuente

`studio/docs/14-arquitectura-y-modularidad.md:90`
