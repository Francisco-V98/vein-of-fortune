---
id: "adr-0010-contexto"
tipo: "seccion"
title: "Contexto"
aliases: ["adr-0010-contexto"]
documento: "[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]"
abiertos: 0
espera: 0
estado: "limpia"
siguiente: "[[ADR-0010 §Decisión]]"
arriba: "[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1]]"
fuente: "studio/docs/adr/0010-politica-de-modelos-y-autorizacion-de-fable.md:5"
generado: true
---

# Contexto

> El consumo de tokens del estudio crecía más rápido que el trabajo hecho. Los datos medidos con el mod vf-consumo:

[[ADR-0010 Política de modelos por rol y autorización de Fable 5.1|↑ ADR-0010]] · [[ADR-0010 §Decisión]] →

El consumo de tokens del estudio crecía más rápido que el trabajo hecho. Los datos medidos con el mod `vf-consumo`:

- El **contexto mediano** de una sesión era de **436 k tokens**, y se relee completo en cada turno.
- El **56 %** de los tokens frescos se gastaba en **subagentes**.
- Los informes de los agentes llegaban a **43 k caracteres**, que luego se pagaban en cada turno del coordinador.
- Hubo **335 lecturas completas** de documentos, cuando casi siempre bastaba una sección.

Además, todos los agentes usaban el mismo modelo y esfuerzo sin importar la tarea, y el modelo más caro (Fable 5.1) podía usarse sin que el autor lo supiera.

## Fuente

`studio/docs/adr/0010-politica-de-modelos-y-autorizacion-de-fable.md:5`
