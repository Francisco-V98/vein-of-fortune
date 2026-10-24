---
id: "adr-0004-consecuencias"
tipo: "seccion"
title: "Consecuencias"
aliases: ["adr-0004-consecuencias"]
documento: "[[ADR-0004 Comunicación entre módulos por api pública y eventos de dominio]]"
abiertos: 0
espera: 0
estado: "limpia"
anterior: "[[ADR-0004 §Alternativas consideradas]]"
arriba: "[[ADR-0004 Comunicación entre módulos por api pública y eventos de dominio]]"
fuente: "studio/docs/adr/0004-comunicacion-entre-modulos.md:18"
generado: true
---

# Consecuencias

> Los módulos se prueban aislados y se reordenan sin romper a otros. Hay que cuidar que los eventos no se conviertan en un grafo oculto; el…

← [[ADR-0004 §Alternativas consideradas]] · [[ADR-0004 Comunicación entre módulos por api pública y eventos de dominio|↑ ADR-0004]]

Los módulos se prueban aislados y se reordenan sin romper a otros. Hay que cuidar que los eventos no se conviertan en un grafo oculto; el verificador exige declarar las dependencias.

## Fuente

`studio/docs/adr/0004-comunicacion-entre-modulos.md:18`
