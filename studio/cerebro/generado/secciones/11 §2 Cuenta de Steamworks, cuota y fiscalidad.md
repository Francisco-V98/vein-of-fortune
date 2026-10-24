---
id: "doc-11-s02"
tipo: "seccion"
title: "2 · Cuenta de Steamworks, cuota y fiscalidad"
aliases: ["doc-11-s02"]
documento: "[[11 Legal y cumplimiento]]"
limpieza: 0
abiertos: 2
espera: 3
aplazado_a: ["[[F1-45 GodotSteam - inicializar Steam y probar en la Steam Deck]]", "[[F4-241 Decidir país fiscal y estructura (persona física o]]", "[[F5-22 Cuenta de Steamworks y alta de la aplicación]]"]
estado: "con-abiertos"
anterior: "[[11 §1 Lista de verificación por etapas (Steam como meta)]]"
siguiente: "[[11 §3 Página de tienda y revisión de Valve]]"
arriba: "[[11 Legal y cumplimiento]]"
fuente: "studio/docs/11-legal-y-cumplimiento.md:23"
generado: true
---

# 2 · Cuenta de Steamworks, cuota y fiscalidad

> Verificado el 2026-10-15 en la documentación oficial de Steamworks.

← [[11 §1 Lista de verificación por etapas (Steam como meta)]] · [[11 Legal y cumplimiento|↑ 11]] · [[11 §3 Página de tienda y revisión de Valve]] →

Verificado el 2026-10-15 en la documentación oficial de Steamworks.

| Tema | Lo que dice la fuente | Fuente |
|---|---|---|
| **Cuota por aplicación (Steam Direct)** | **100 USD** (o equivalente) por producto. Solo la paga un usuario con permiso de administrador; no se acepta saldo de la cartera de Steam. El crédito queda ligado a la cuenta de quien pagó | partner.steamgames.com/doc/gettingstarted/appfee |
| **Reembolso** | **No es reembolsable, pero se recupera**: se devuelve cuando el producto llega a **1.000 USD** de ingresos brutos ajustados en la tienda o en compras dentro del juego. Aparece como línea aparte en el informe mensual. Si el depósito se revierte o se marca como fraude, se pueden retener pagos | partner.steamgames.com/doc/gettingstarted/appfee y partner.steamgames.com/steamdirect |
| **Pasos del alta** | Firmar los acuerdos digitales (confidencialidad y Steam Distribution Agreement), pagar la cuota, completar datos bancarios, fiscales y de identidad, preparar la página y el build, pasar la revisión, cumplir los plazos de las primeras aplicaciones | partner.steamgames.com/doc/gettingstarted/onboarding |
| **Entrevista bancaria** | Hace falta número de cuenta, ruta bancaria y dirección del banco. El **titular de la cuenta debe coincidir con el nombre del alta**. Si no tienes cuenta adecuada, hay que abrirla antes | onboarding |
| **Entrevista fiscal e identidad** | Cuestionario fiscal que fija tu estatus y la retención. Personas de EE. UU. dan datos tipo W-9; ciudadanos o empresas de países con convenio, tipo W-8BEN. Se usa el **nombre legal**, no un alias. No se puede cambiar la información fiscal hasta terminar la verificación. Sin datos bancarios y fiscales válidos **no se puede publicar** | onboarding y partner.steamgames.com/doc/gettingstarted/faq |
| **Retención de impuestos** | Para extranjeros, la fuente cita una tasa de EE. UU. del **30 %** sobre la mayoría de ingresos de origen estadounidense, reducible o exenta por convenio. **Depende del país del autor** | doc/gettingstarted/faq |
| **Impuestos sobre la cuota** | Valve aplica IVA o similar donde corresponda; la factura va a la persona que pagó, no a una empresa, y no se emiten duplicados | appfee |
| **Plazos** | Los números **no coinciden** entre dos páginas oficiales. La página de alta dice: verificación fiscal de **10 a 15 días hábiles**, espera de **21 días** entre pagar la cuota y poder lanzar. La página de Steam Direct dice: verificación bancaria, fiscal y de identidad de **15 a 30 días** y espera de **30 días**. Ambas piden una página «Próximamente» pública **al menos 2 semanas** antes del lanzamiento | onboarding frente a partner.steamgames.com/steamdirect |
| **Porcentaje de ingresos** | 🟡 **30 %** para Valve en general; **25 %** sobre los ingresos que superen **10 millones de USD** por aplicación y **20 %** sobre los que superen **50 millones**. La página oficial del anuncio (título «New Revenue Share Tiers and other updates to the Steam Distribution Agreement», 2018) no se pudo leer; las cifras vienen de prensa que la cita. Verifica el porcentaje en el Steam Distribution Agreement que firmarás | steamcommunity.com/groups/steamworks/announcements/detail/1697191267930157838 (título) y prensa (por ejemplo bluesnews.com) |

**Planificación 🟡:** como el plazo oficial es incierto, planifica con el caso lento: cuota pagada y verificaciones terminadas **al menos 60 días antes** del lanzamiento y, para la página «Próximamente», antes de [[F4-240 Página «Próximamente» de Steam al final de F4|F4-240]] (ver sección 3). Mientras no exista la aplicación, las pruebas de GodotSteam usan una aplicación de prueba de Steam ⏳ [[F1-45 GodotSteam - inicializar Steam y probar en la Steam Deck|F1-45]].

- ⏳ [[F4-241 Decidir país fiscal y estructura (persona física o|F4-241]] **País de residencia fiscal del autor y estructura (persona física o sociedad):** lo resuelve el **autor** con un **contador local** antes de iniciar el alta. Decide qué formulario fiscal se usa, la retención y el nombre legal del alta. No se inventa aquí.
- ⏳ [[F5-22 Cuenta de Steamworks y alta de la aplicación|F5-22]] **Plazos reales** (21 o 30 días de espera; 10 a 15 días hábiles o hasta 30 días de verificación): los confirma el **autor** en Steamworks al iniciar el alta, o con soporte de Steamworks.

## Fuente

`studio/docs/11-legal-y-cumplimiento.md:23`
