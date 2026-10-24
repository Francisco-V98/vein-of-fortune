---
id: "adr-0010-verificacion"
tipo: "seccion"
title: "Verificación"
aliases: ["adr-0010-verificacion"]
documento: "[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]"
abiertos: 0
espera: 1
aplazado_a: ["[[F0-89 Ajustes finos de consumo - agentes cortos, prefijo fijo y]]"]
estado: "con-aplazados"
anterior: "[[ADR-0010 §Consecuencias]]"
arriba: "[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]"
fuente: "studio/docs/adr/0010-politica-de-modelos-y-autorizacion-de-fable.md:42"
generado: true
---

# Verificación

← [[ADR-0010 §Consecuencias]] · [[ADR-0010 Política de modelos por rol y autorización de Fable 5.1|↑ ADR-0010]]

- `python3 studio/hub/build.py --strict` valida la tabla.
- `/consumo` muestra el gasto por modelo, ventana y día; la reducción de los cuatro datos del contexto se compara en ⏳ [[F0-89 Ajustes finos de consumo - agentes cortos, prefijo fijo y|F0-89]] con tareas comparables.

## Fuente

`studio/docs/adr/0010-politica-de-modelos-y-autorizacion-de-fable.md:42`
