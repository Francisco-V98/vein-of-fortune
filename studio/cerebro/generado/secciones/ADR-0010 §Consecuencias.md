---
id: "adr-0010-consecuencias"
tipo: "seccion"
title: "Consecuencias"
aliases: ["adr-0010-consecuencias"]
documento: "[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]"
abiertos: 0
espera: 2
aplazado_a: ["[[F0-88 Consulta del estudio sin leer documentos enteros]]", "[[F0-89 Ajustes finos de consumo - agentes cortos, prefijo fijo y]]"]
estado: "con-aplazados"
anterior: "[[ADR-0010 §Alternativas descartadas]]"
siguiente: "[[ADR-0010 §Verificación]]"
arriba: "[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]"
fuente: "studio/docs/adr/0010-politica-de-modelos-y-autorizacion-de-fable.md:35"
generado: true
---

# Consecuencias

← [[ADR-0010 §Alternativas descartadas]] · [[ADR-0010 Política de modelos por rol y autorización de Fable 5.1|↑ ADR-0010]] · [[ADR-0010 §Verificación]] →

- El coordinador debe fijar `model` y `effort` en cada llamada a `Agent`; el hook de `vf-equipo` sobre `Agent` reescribe la llamada con los valores del rol y pide la autorización de Fable, sin modificar archivos.
- Se añade el campo `politica_modelos` y los campos `modelo` y `esfuerzo` en `equipo.json`; el hub los valida.
- Las tareas de seguimiento son ⏳ [[F0-88 Consulta del estudio sin leer documentos enteros|F0-88]] (consulta del estudio sin leer documentos enteros) y ⏳ [[F0-89 Ajustes finos de consumo - agentes cortos, prefijo fijo y|F0-89]] (ajustes finos y `/consumo` por rol, con la medición antes y después).
- Riesgo: un modelo más barato puede dar peor calidad en un rol concreto; se corrige subiéndolo en la tabla o en la tarea.

## Fuente

`studio/docs/adr/0010-politica-de-modelos-y-autorizacion-de-fable.md:35`
