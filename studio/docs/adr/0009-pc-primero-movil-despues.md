# ADR-0009 · PC primero (Steam) y móvil después

**Estado:** ✅ Aceptada · **Fecha:** 2026-10-15

## Contexto

Hasta ahora el plan era **Android primero**: el juego se diseñaba para pantalla táctil, con resolución y zona segura pensadas para teléfonos, pruebas en el Android del autor y Play Vitals como telemetría de tienda ([ADR-0001](0001-godot-como-motor.md), [ADR-0007](0007-telemetria-por-capas.md)). El autor cambió la prioridad el 2026-10-15: el juego se lanza primero en PC y Steam es la tienda objetivo. Observación del análisis: el juego maneja mucha información a la vez (mercado, noticias, contratos, ventanas densas) y eso se aprovecha mejor con hover, tooltips y atajos.

## Decisión ✅

Decisiones del autor (2026-10-15):

1. **El juego se lanza primero en PC**, compatible y preparado para Steam. El móvil (Android e iOS) llega **después de que el juego esté completo en PC**: la 1.0 publicada y estable en Steam.
2. **Plataformas de la 1.0:** Windows y Linux. macOS queda para después de la 1.0. El motor sigue siendo Godot 4.x.
3. **Steam Deck:** se apunta a la categoría *Verified*: mando completo, sin HUD táctil y texto legible en 1280×800.
4. **Tiendas:** Steam como meta; itch.io para builds de prueba. GOG y Epic quedan fuera de la 1.0.
5. **Controles:** ratón y teclado principales (hover, tooltips, atajos y ventanas de información densas), con **mando completo**. La interfaz táctil queda como un **adaptador futuro** para el móvil; no se construye HUD táctil ahora.
6. **Nube y partidas:** Steam Auto-Cloud con una carpeta de guardados pequeños y hasta **5 partidas**. En Hardcore manda el guardado **local**: no se puede restaurar desde la nube tras morir.
7. **Página de Steam («Próximamente»):** se abre al final de F4, con el juego casi completo. Se mantiene la regla de arte «nada provisional llega a la tienda»: la página usa arte definitivo.
8. **Pruebas:** en un **PC Windows real** (el autor lo tiene o lo consigue) y en la Steam Deck si la hay. Es un requisito de F1. El autor trabaja en Mac, así que ese PC es indispensable.
9. **Sin cambio:** pago único, sin anuncios ni compras dentro del juego; autoguardado instantáneo (la Steam Deck suspende el juego en cualquier momento).

Decisiones técnicas que acompañan la decisión (cerradas en F0-57, 2026-10-24):

- ✅ **GodotSteam** es la herramienta de Steamworks (decisión del autor), siempre detrás del puerto de plataforma/tienda ([14](../14-arquitectura-y-modularidad.md)) y con un **adaptador nulo** siempre disponible, de modo que el juego también corra sin Steam (itch.io y pruebas). Su licencia se verifica al integrarlo (⏳ F1-45).
- ✅ Integración continua con exportación a **Windows y Linux** y build reproducible por línea de comandos, consecuencia de las plataformas de la 1.0; la implementa ⏳ F1-26.
- ✅ La capa B de telemetría pasa a ser lo que entregue Steam (ya enmendada en [ADR-0007](0007-telemetria-por-capas.md)); su alcance real se verifica en la fuente vigente al llegar a ⏳ F5-40.
- ✅ El **PC Windows real** para pruebas ya está disponible (autor, 2026-10-24): el requisito de F1 del punto 8 está cumplido.

Aplazado con su tarea (⏳): resolución base y modo ventana ✅ 640×360 (2026-10-24, cierra F1-06; [ADR-0011](0011-exploracion-caminable-tren-y-minas.md)); precio y DLC ⏳ F5-33, F6-01 y F6-61; demo con el Acto I ⏳ F3-23; declaración de IA de Steam y términos de PixelLab ⏳ F4-227.

## Alternativas descartadas

| Alternativa | Por qué se descarta |
|---|---|
| **Android primero** (el plan anterior) | Descartada por el autor. Obligaba a decisiones móviles (zona segura 20:9, HUD táctil, gamas de Android) que condicionaban una interfaz con mucha información |
| **Solo Windows** | El autor incluyó Linux; además es la base de la Steam Deck, así que dejarlo fuera complicaría el objetivo *Verified* |
| **Con macOS en la 1.0** | Aplazada por el autor hasta después de la 1.0; además implicaría firma y notarización de Apple, que se estudian al abrir esa plataforma |
| **Móvil y PC a la vez** | El autor decidió terminar primero el juego en PC; hacerlo a la vez duplicaría el diseño de la interfaz y las pruebas |
| **GOG y Epic en la 1.0** | Más trámites sin beneficio claro antes de publicar en Steam |

## Consecuencias

- **Arquitectura:** el diseño por puertos y adaptadores ([ADR-0003](0003-arquitectura-modular.md)) ya separa el dominio de la entrada, el almacenamiento y la plataforma. Se añaden los puertos de **plataforma/tienda** (logros, nube, actualizaciones) y de **pantalla** (resolución, ventana, escala). El módulo `market` y el resto del dominio no cambian.
- **Camino al móvil:** el dominio no usa `Input`, `OS` ni `DisplayServer` (los símbolos prohibidos ya los bloquea el verificador). Llevar el juego al móvil será añadir adaptadores (táctil, háptica, almacenamiento y ciclo de vida de Android e iOS), no tocar módulos. Mientras tanto, la capa de acciones evita decisiones que solo funcionen con ratón.
- **Interfaz:** hover, tooltips y atajos pasan a ser parte de la interfaz principal; el foco y el mando completo siguen siendo obligatorios (Steam Deck).
- **Guardado:** carpeta de guardados pequeños y estable para Auto-Cloud, hasta 5 partidas, y política de Hardcore local ([10](../10-tecnico-y-herramientas.md)).
- **QA:** la matriz de dispositivos pasa a ser una matriz de PC y los presupuestos de rendimiento se miden en PC (⏳ F1-44). Lo específico de Android se conserva como «Fase móvil» ([16](../16-calidad-y-qa.md)).
- **Legal:** aparecen Steam Direct, entrevista fiscal, cuestionario de contenido y declaración de IA; desaparecen Google Play Data safety y la prueba cerrada ([11](../11-legal-y-cumplimiento.md)).
- **Resolución:** las preguntas de 480×270 y zona segura 20:9 eran móviles y se rehicieron con el enfoque de PC: ✅ resolución base **640×360** con escala entera y bandas (autor, 2026-10-24, cierra F1-06).
- **Deuda:** el trabajo de Android (JDK, SDK, keystore, APK, `versionCode`, backup de Android, Play Vitals) no se pierde: queda documentado en la sección «Fase móvil (después de la 1.0)» de [10](../10-tecnico-y-herramientas.md) y [16](../16-calidad-y-qa.md).
