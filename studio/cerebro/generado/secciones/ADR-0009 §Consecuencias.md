---
id: "adr-0009-consecuencias"
tipo: "seccion"
title: "Consecuencias"
aliases: ["adr-0009-consecuencias"]
documento: "[[ADR-0009 PC primero (Steam) y móvil después]]"
abiertos: 0
espera: 1
aplazado_a: ["[[F1-44 Presupuestos de rendimiento medidos en PC]]"]
estado: "con-aplazados"
anterior: "[[ADR-0009 §Alternativas descartadas]]"
arriba: "[[ADR-0009 PC primero (Steam) y móvil después]]"
fuente: "studio/docs/adr/0009-pc-primero-movil-despues.md:41"
generado: true
---

# Consecuencias

← [[ADR-0009 §Alternativas descartadas]] · [[ADR-0009 PC primero (Steam) y móvil después|↑ ADR-0009]]

- **Arquitectura:** el diseño por puertos y adaptadores ([[ADR-0003 Arquitectura modular por cortes verticales y capas|ADR-0003]]) ya separa el dominio de la entrada, el almacenamiento y la plataforma. Se añaden los puertos de **plataforma/tienda** (logros, nube, actualizaciones) y de **pantalla** (resolución, ventana, escala). El módulo `market` y el resto del dominio no cambian.
- **Camino al móvil:** el dominio no usa `Input`, `OS` ni `DisplayServer` (los símbolos prohibidos ya los bloquea el verificador). Llevar el juego al móvil será añadir adaptadores (táctil, háptica, almacenamiento y ciclo de vida de Android e iOS), no tocar módulos. Mientras tanto, la capa de acciones evita decisiones que solo funcionen con ratón.
- **Interfaz:** hover, tooltips y atajos pasan a ser parte de la interfaz principal; el foco y el mando completo siguen siendo obligatorios (Steam Deck).
- **Guardado:** carpeta de guardados pequeños y estable para Auto-Cloud, hasta 5 partidas, y política de Hardcore local ([[10 Técnico y herramientas|10]]).
- **QA:** la matriz de dispositivos pasa a ser una matriz de PC y los presupuestos de rendimiento se miden en PC (⏳ [[F1-44 Presupuestos de rendimiento medidos en PC|F1-44]]). Lo específico de Android se conserva como «Fase móvil» ([[16 Calidad y QA|16]]).
- **Legal:** aparecen Steam Direct, entrevista fiscal, cuestionario de contenido y declaración de IA; desaparecen Google Play Data safety y la prueba cerrada ([[11 Legal y cumplimiento|11]]).
- **Resolución:** las preguntas de 480×270 y zona segura 20:9 eran móviles y se rehacen con el enfoque de PC en [[F1-06 Resolución base, escalado entero y modos de pantalla|F1-06]].
- **Deuda:** el trabajo de Android (JDK, SDK, keystore, APK, `versionCode`, backup de Android, Play Vitals) no se pierde: queda documentado en la sección «Fase móvil (después de la 1.0)» de [[10 Técnico y herramientas|10]] y [[16 Calidad y QA|16]].

## Fuente

`studio/docs/adr/0009-pc-primero-movil-despues.md:41`
