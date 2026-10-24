---
id: "doc-24-s05"
tipo: "seccion"
title: "5 · Los tramos de los medidores y lo que desbloquean ✅"
aliases: ["doc-24-s05"]
documento: "[[24 Umbrales de acto]]"
limpieza: 100
abiertos: 0
espera: 4
aplazado_a: ["[[F4-142 Acto IV - guion y escenas]]", "[[F4-61 Modelo de los cuatro medidores de relación]]"]
estado: "con-aplazados"
anterior: "[[24 §4 Las tres vías]]"
siguiente: "[[24 §6 Cómo alcanza cada medidor cada tramo]]"
arriba: "[[24 Umbrales de acto]]"
fuente: "studio/docs/24-umbrales-de-acto.md:89"
generado: true
---

# 5 · Los tramos de los medidores y lo que desbloquean ✅

> Estado: los tramos, los arranques y lo que desbloquea cada tramo de Esteban (en n-iv-esteban), Lucía, Teo y la Unión (en n-iv-montenegro y…

← [[24 §4 Las tres vías]] · [[24 Umbrales de acto|↑ 24]] · [[24 §6 Cómo alcanza cada medidor cada tramo]] →

**Estado:** los tramos, los arranques y lo que desbloquea cada tramo de Esteban (en [[Esteban descubre el fondo reservado|n-iv-esteban]]), Lucía, Teo y la Unión (en [[Montenegro se mueve contra ti|n-iv-montenegro]] y [[El destino de la Aetherita|n-iv-aetherita]]) son decisión del autor, igual que el castigo de que Montenegro solo pueda «borrarte» con la Unión alta; las reglas de lectura menores las confirmó el autor el 2026-10-16 ([[F0-80 Pasada de cierre - biblia, documentos de pasado, variantes|F0-80]]). Los movimientos de cada decisión ⏳ [[F4-61 Modelo de los cuatro medidores de relación|F4-61]].

| Tramo | Valor ✅ | Quién arranca aquí ✅ |
|---|---|---|
| **Bajo** | 0 a 34 | — |
| **Medio** | 35 a 54 | Unión (50), Lucía (50) y Esteban (40) |
| **Alto** | 55 a 100 | Teo (60) |

Los tramos están en `meta.tramos` de `decisions.json`. La pantalla muestra el tramo y su motivo, no la cifra ⏳ [[F4-61 Modelo de los cuatro medidores de relación|F4-61]].

| Medidor | Alto | Medio | Bajo |
|---|---|---|---|
| **Esteban** | Aval abierto ✅. En [[Esteban descubre el fondo reservado\|n-iv-esteban]] rompe con el Consorcio y te da el libro ✅ | Aval bloqueado, con el motivo ✅. En [[Esteban descubre el fondo reservado\|n-iv-esteban]] se aparta ✅ | Aval bloqueado ✅. En [[Esteban descubre el fondo reservado\|n-iv-esteban]] defiende al Consorcio ✅ |
| **Lucía** | Publica contigo ✅ y te da el reproductor ✅ | No publica, publicas tú con costo alto y poco alcance ✅. El reproductor lo entrega Reme ✅ | Publica en La Voz del Hollín sin ti ✅. El reproductor lo entrega Reme ✅ |
| **Teo** | Si hubo revisión, se queda ✅ | Si hubo revisión, se queda ✅ | Si hubo revisión, se va ✅ |
| **Unión** | Cuenta para la vía de relación ✅. En [[Montenegro se mueve contra ti\|n-iv-montenegro]], Montenegro intenta borrarte y falla ✅. En [[El destino de la Aetherita\|n-iv-aetherita]], la Unión sale contigo si revelas ✅ | No cuenta para la vía de relación ✅. Sin efecto propio en el IV ✅ | En [[El destino de la Aetherita\|n-iv-aetherita]], nadie te respalda en el Hollín si revelas ✅ |

- **Teo sin revisión muere, sea cual sea su tramo** ✅. Si el medidor y la revisión chocan, gana el no haberlo atendido ✅. Esto incluye la opción respetuosa «se lo propones y aceptas su no» ✅.
- **Esteban.** El aval se lee en el momento de elegir entrada ✅. Como [[Esteban te pide algo en la bolsa|n-iii-esteban-trato]] ocurre antes, el medidor ya trae lo que hiciste en la bolsa. Después de la entrada, el medidor de Esteban no se mueve, así que el tramo del IV es el de la entrada ⏳ [[F4-61 Modelo de los cuatro medidores de relación|F4-61]].
- **Lucía.** Antes de decidir sobre la Aetherita se te muestra quién publicaría, para elegir con aviso ✅ (decisión del autor, 2026-10-16; su implementación ⏳ [[F4-142 Acto IV - guion y escenas|F4-142]]). [[Quién publica|n-iv-lucia-publica]] se activa si la verdad sale.
- **Unión.** En [[Montenegro se mueve contra ti|n-iv-montenegro]], «borrarte» pide Unión alta y al menos dos pruebas, y falla ✅. Si vendes al Ministerio, te compra con el sello y esa regla manda primero ✅. Como siempre conservas al menos tres ([[23 Árbol de decisiones y consecuencias|23]], sección 8), en la práctica solo importa la Unión: es el castigo de quien tiene gente detrás ✅. Con Unión media o baja, y si no vendes al Ministerio, te amenaza ✅: la entrada que usaste ya no decide qué hace Montenegro. Su desenlace se decide al cerrar el acto, con el comprador ya fijado ✅ (decisión del autor, 2026-10-12). Los **empleados** solo **leen** el tramo de la Unión (modula su Lealtad); contratar, despedir o publicar una oferta no mueve el medidor ✅ (decisión del autor, 2026-10-15; [[04 Progresión y meta|04]]).
- **Montenegro** no tiene tramos ✅.

---

## Fuente

`studio/docs/24-umbrales-de-acto.md:89`
