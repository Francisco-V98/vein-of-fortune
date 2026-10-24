---
id: "doc-25-s08"
tipo: "seccion"
title: "8 · Estado legible que se guarda ✅"
aliases: ["doc-25-s08"]
documento: "[[25 Finales y epílogos]]"
limpieza: 100
abiertos: 0
espera: 2
aplazado_a: ["[[F2-01 Modelo de estado de partida y semilla]]", "[[F4-109 Escalera de estatus y condiciones de ascenso]]"]
estado: "con-aplazados"
anterior: "[[25 §7 Hilos abiertos y hilos que se cierran]]"
siguiente: "[[25 §9 Coste de producción]]"
arriba: "[[25 Finales y epílogos]]"
fuente: "studio/docs/25-finales-y-epilogos.md:336"
generado: true
---

# 8 · Estado legible que se guarda ✅

> Estado: que se guardan banderas, variante oculta y resultados de Esteban, Montenegro, Lucía y Teo con nombres estables, los nombres exactos…

← [[25 §7 Hilos abiertos y hilos que se cierran]] · [[25 Finales y epílogos|↑ 25]] · [[25 §9 Coste de producción]] →

**Estado:** que se guardan banderas, variante oculta y resultados de Esteban, Montenegro, Lucía y Teo con nombres estables, los nombres exactos de la tabla, que se añadan `e-union` y `e-abono`, y que el de Montenegro se fija al cerrar el acto con el comprador ya fijado son decisión del autor (2026-10-12); los valores los confirmó el 2026-10-16 ([[F0-80 Pasada de cierre - biblia, documentos de pasado, variantes|F0-80]]). No van a `decisions.json`: la validación del hub solo admite banderas de elección y medidores, y exige que alguna decisión las fije y las lea. Su modelo ⏳ [[F2-01 Modelo de estado de partida y semilla|F2-01]].

El motivo de guardarlos: en el sandbox los medidores se mueven, y el epílogo debe releerse desde el diario igual que se vio. Se fijan una vez y no se recalculan. Eso incluye la carta de Vega Mansa (FM-01 a FM-03): lee un estado fijado al entrar en el acta, el patrimonio de ese momento (`e-patrimonio-acta`), y no el patrimonio que tengas después en el sandbox ✅ (decisión del autor, 2026-10-16).

| Nombre | Valores | Cuándo se fija | Lo leen |
|---|---|---|---|
| `e-variante-reme` | consorcio, ministerio, faroleros | Al empezar la partida (el sorteo de [[22 Acto II - las tres variantes de Reme\|22]]) | RE-01 a RE-03 |
| `e-esteban` | se-une, se-aparta, defiende | Al resolver [[Esteban descubre el fondo reservado\|n-iv-esteban]] | ES-01 a ES-04, ME-05 |
| `e-montenegro` | compra, borra, amenaza | Al cerrar el IV, con el comprador ya fijado | DU-01 a DU-03 |
| `e-lucia` | contigo, voz, tu, filtra, calla | Al resolver [[Quién publica\|n-iv-lucia-publica]] | LU-01 a LU-04 |
| `e-teo` | queda, va, muere | Al resolver [[El destino de Teo\|n-iv-teo]] | TE-01 a TE-03 |
| `e-union` | alto, medio, bajo | Al cerrar el IV (congela [[Medidor Unión\|m-union]]) | H-01, H-02, DU-02, UN-01 a UN-03 |
| `e-abono` | sigue, cortado | Al fijar [[Bandera destino\|f-destino]] | Cola de RE-01 a RE-03 |
| `e-patrimonio-acta` | paga, alivia (según el patrimonio: ≈ 250 000 es el piso de Magnate de [[28 Números base de la economía\|28]]; umbral final ⏳ [[F4-109 Escalera de estatus y condiciones de ascenso\|F4-109]]) | Al entrar en el acta, antes de cerrar el IV | FM-01 a FM-03 (el hueco `{deuda-familia}`) |

---

## Fuente

`studio/docs/25-finales-y-epilogos.md:336`
