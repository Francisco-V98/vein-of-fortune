# 11 · Legal y cumplimiento

> **Aviso:** esto es una lista de verificación de trabajo, **no asesoría legal**. Los requisitos de las tiendas y las leyes cambian. Cada punto debe verificarse en la fuente oficial vigente al momento de publicar y, para temas fiscales y de propiedad intelectual, con un profesional local. El país de residencia del autor aún no está definido y afecta mucho la parte fiscal.

El proyecto es personal primero. Esta lista se activa por etapas: casi nada importa hasta que se piense publicar.

**Plataforma ✅ (decisión del autor, 2026-10-15, [ADR-0009](adr/0009-pc-primero-movil-despues.md)):** el juego sale primero en **PC (Windows y Linux)**, con **Steam** como meta (objetivo *Steam Deck Verified*) e **itch.io** para builds de prueba. El móvil (Google Play y App Store) llega **después de la 1.0** y su lista está en la sección «Fase móvil (después de la 1.0)», más abajo. GOG y Epic quedan fuera de la 1.0.

**Cómo leer las fuentes.** Lo marcado «verificado» se leyó en la fuente oficial indicada el **2026-10-15**; esa lectura la hizo una herramienta que resume páginas, así que **vuelve a leer la página oficial antes de pagar o enviar nada**. Dos páginas oficiales de Steamworks se contradicen en plazos (ver sección 2): se planifica con el caso más lento.

## 1 · Lista de verificación por etapas (Steam como meta)

| Etapa | Qué hacer | Tarea |
|---|---|---|
| **F0–F3** (personal) | Registro de licencias desde el primer asset (incluido lo provisional); no meter secretos ni datos personales; título provisional; pruebas en un PC Windows real y, si hay, en la Steam Deck (requisito de F1). Hasta aquí no se paga ni se abre ninguna cuenta; GodotSteam se prueba con una aplicación de prueba | F1-45 |
| **F3** (tajada) | Decidir si hay demo con el Acto I ⏳ F3-23. Borrador de política de privacidad antes de cualquier prueba externa (itch.io incluida) | F3-23 |
| **F4 · producción definitiva** | Probar PixelLab y registrar sus términos comerciales ⏳ F4-227 (**antes** de producir arte definitivo en lote). Integrar Steamworks detrás del puerto «plataforma/tienda»: nube ⏳ F4-234, logros ⏳ F4-235, Steam Input ⏳ F4-236, lista *Steam Deck Verified* ⏳ F4-239 | F4-227, F4-234 a F4-239 |
| **Final de F4** | **Página «Próximamente»** ⏳ F4-240 (decisión del autor: se abre con el juego casi completo y con arte definitivo). Para publicarla hacen falta, **antes**: cuenta de Steamworks con la cuota pagada y la aplicación creada, cápsulas y capturas reales, descripción, y 🟡 el cuestionario de contenido y la declaración de IA (ver secciones 2 a 5). Los plazos de Valve (verificación fiscal, espera tras pagar la cuota, revisión) obligan a **abrir la cuenta bastante antes** de F4-240 | F4-240. Esas tareas (F4-241, F5-22, F5-23, F5-24, F5-27, F5-28, F5-29, F5-30, F5-33, F5-34, F5-35, F5-43, F4-242 y F4-243) ya están en F4.19 antes de F4-240 y se ejecutan en ese orden |
| **F5 · legal y tienda** | Créditos ⏳ F5-25; registro final de licencias ⏳ F5-26; prueba cerrada con claves de Steam e itch.io ⏳ F5-31 (la cuenta, la privacidad, el EULA, el cuestionario, la clasificación, la marca y la declaración de IA ya se hicieron en F4.19) | F5-25, F5-26, F5-31 |
| **F5 · lanzamiento** | Build para Windows y Linux ⏳ F5-32; precio y DLC ⏳ F5-33 (la ficha ES/EN y las capturas ya están en F4.19: F5-33, F5-34, F5-35); tráiler del lanzamiento ⏳ F5-36; revisión de Valve del build y publicación ⏳ F5-37 y F5-57 | F5-32, F5-36, F5-37, F5-57 |
| **Después del lanzamiento** | Telemetría en producción y actualización de la política ⏳ F5-40, F5-41; casino ⏳ F6-13 | F5-40, F5-41, F6-13 |

## 2 · Cuenta de Steamworks, cuota y fiscalidad

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

**Planificación 🟡:** como el plazo oficial es incierto, planifica con el caso lento: cuota pagada y verificaciones terminadas **al menos 60 días antes** del lanzamiento y, para la página «Próximamente», antes de F4-240 (ver sección 3). Mientras no exista la aplicación, las pruebas de GodotSteam usan una aplicación de prueba de Steam ⏳ F1-45.

- ⏳ F4-241 **País de residencia fiscal del autor y estructura (persona física o sociedad):** lo resuelve el **autor** con un **contador local** antes de iniciar el alta. Decide qué formulario fiscal se usa, la retención y el nombre legal del alta. No se inventa aquí.
- ⏳ F5-22 **Plazos reales** (21 o 30 días de espera; 10 a 15 días hábiles o hasta 30 días de verificación): los confirma el **autor** en Steamworks al iniciar el alta, o con soporte de Steamworks.

## 3 · Página de tienda y revisión de Valve

Verificado el 2026-10-15 en partner.steamgames.com/doc/store/review_process, /coming_soon, /release_dates y /assets/standard.

| Requisito | Detalle |
|---|---|
| **Página «Próximamente»** | Crear la aplicación, completar todo lo de «Your Store Presence», marcar «Ready For Review» y, tras la aprobación, pulsar «Post as Coming Soon». Una aplicación nueva debe tenerla **al menos 2 semanas** antes del lanzamiento. Envíala a revisión **al menos 7 días hábiles** antes de querer que salga |
| **Revisión de la página y del build** | Típicamente **3 a 5 días hábiles** cada una (la página de alta dice «1 a 5 días»); Valve recomienda **planificar 7 días hábiles**. Valve ejecuta el juego, comprueba que la página y la configuración son correctas y que no es dañino. Una vez aprobado, **no hay que revisarlo de nuevo en cada actualización** |
| **Contenido de la página** | Solo funciones y contenido **disponibles en el lanzamiento**; lo planeado se marca como no lanzado. Todas las funciones listadas deben estar en el build. Descripción detallada y coherente, sin enlaces a otros sitios. El producto debe arrancar en **todos los sistemas operativos** que anuncies (Windows y Linux) |
| **Imágenes** | Cápsula de cabecera 920×430, pequeña 462×174, principal 1232×706 y vertical 748×896: el **título o logo debe ser legible** y sin más texto que el título. **Mínimo 5 capturas** de 1920×1080 (16:9), de **juego real** (nada de arte conceptual, escenas cinemáticas, premios ni textos de marketing); al menos 4 aptas para todas las edades |
| **Transacciones** | Cualquier compra dentro del juego debe usar la cartera de Steam. La v1 es de pago único, sin compras ni anuncios |
| **Fecha de lanzamiento** | La fecha se puede cambiar hasta 2 semanas antes; después se fija. Evita lanzar en fin de semana (el equipo de Steam no está disponible) |
| **Arte definitivo** | 🟡 Cápsulas y capturas con arte **definitivo**: la regla «nada provisional llega a la tienda» ([12](12-direccion-de-arte.md)) se aplica a la página «Próximamente». Hace falta el arte clave ⏳ F5-43 y las capturas ⏳ F5-35 antes de F4-240 |
| **Anuncios** | Steam no admite modelos con publicidad (lista de contenido no permitido); coherente con la v1 |

## 4 · Cuestionario de contenido y clasificación por edad

Verificado el 2026-10-15 en partner.steamgames.com/doc/gettingstarted/contentsurvey y /contentsurvey/germany.

| Tema | Detalle |
|---|---|
| **Cuestionario** | Tiene **tres partes obligatorias** (contenido general, contenido maduro e IA generativa) y debe completarse **antes de enviar a revisión**. El contenido general **genera clasificaciones para varios organismos regionales** que se muestran en la página. Hay que declarar todo el contenido adulto que exista en los builds, aunque no sea accesible. **Tras la aprobación, algunas respuestas no se pueden editar sin contactar con soporte de Steam** |
| **¿IARC, PEGI o ESRB para Steam?** | **No son obligatorios.** Steam genera las clasificaciones con su propio cuestionario. Si tienes una clasificación oficial, puedes introducirla en la sección «Ratings» de la aplicación (opcional). IARC es el sistema de Google Play y otras tiendas, no de Steam: ver «Fase móvil» |
| **Alemania (USK)** | Desde el **15 de noviembre de 2024** Steam no muestra en Alemania los juegos sin clasificación válida. La clasificación puede venir de la USK o del **proceso propio de Valve**, que usa el cuestionario. Solo se introduce un valor USK si la USK revisó esa versión exacta; una clasificación IARC de otra tienda **no** vale como USK. Hay contenido que no se puede vender en Alemania y debe declararse. Completar el cuestionario no garantiza disponibilidad |
| **Indonesia** | Existe la página «Age Ratings in Indonesia» (partner.steamgames.com/doc/gettingstarted/contentsurvey/indonesia); no se leyó su contenido. 🟡 Revísala en F5-28 |
| **Brasil y Corea** | ⏳ F5-28 **No se encontró documentación oficial de Steamworks** sobre requisitos propios. Valve citó leyes de Brasil y Alemania al anunciar las clasificaciones en 2024 (prensa), pero sin detalle oficial. Lo verifica el **autor en F5-28** con el cuestionario real de Steamworks y, si hace falta, con soporte de Steamworks |
| **Temas del juego** | Corrupción, extorsión, violencia y negocios ilegales influyen en la clasificación. Mundo y naciones **ficticios**, sin política real |
| **Público** | ✅ **El juego no se dirige a menores** (decisión del autor, 2026-10-13): los cuestionarios de edad y de público se contestan en consecuencia ⏳ F5-28. Si algún día se dirigiera a menores, aplicarían reglas mucho más estrictas |
| **Textos de usuario** | Nombres de personaje y tienda se validan (longitud, caracteres, filtro de palabras ofensivas) |

## 5 · Contenido generado por IA

Verificado el 2026-10-15 en partner.steamgames.com/doc/gettingstarted/contentsurvey (parte 3, «Generative Artificial Intelligence Content»).

| Tema | Detalle |
|---|---|
| **Qué se declara** | La IA usada para crear contenido **que viaja con el juego y consume el jugador**: arte, sonido, narrativa y localización. **No** se declara la IA como herramienta de eficiencia del desarrollo (por ejemplo, ayuda para programar) |
| **Contenido «pre-generado»** | Hecho con IA durante el desarrollo y entregado dentro del juego. Valve lo evalúa **igual que el contenido sin IA**: el juego no debe incluir material ilegal o que infrinja derechos y debe cumplir lo que prometes. 🟡 Según prensa (por ejemplo tbreak.com y tech-insider.org, enero de 2026), la declaración se muestra como nota pública en la página de tienda; confirma el formato en Steamworks |
| **Contenido «en vivo»** | Creado por IA mientras corre el juego. Exige describir las **barreras** que impiden generar contenido ilegal. **La v1 no tiene IA en vivo** 🟡 (no está en el diseño actual); si algún día se añadiera, habría que declararla y gestionar el costo por uso |
| **Excepción** | Valve no quiere por ahora IA en vivo para contenido sexual solo para adultos |
| **Qué cuenta en este proyecto** | 🟡 El **arte definitivo en PixelLab** (herramienta decidida por el autor) es contenido pre-generado: se **declara**. Las referencias provisionales no llegan a la tienda, pero su registro se mantiene. ❓ Falta decidir con el **autor** cómo se declaran los **textos, guiones y traducciones** si los redactan agentes de IA, y la **música y las voces** si se generan: son «narrativa», «localización» y «sonido». La recomendación es declarar con honestidad lo que corresponda; se decide **antes de producir** el contenido final, no al final |
| **Material de marketing** | 🟡 La prensa indica que el arte de la página de tienda generado con IA también se declara; la página oficial leída no lo dice. Trátalo como declarable |
| **Tarea** | Declaración formal ⏳ F5-30 (los hechos que se declaran dependen de lo producido en F4 y se toman del registro de licencias tal como esté al abrir la página; la versión final del registro es F5-26) |

## 6 · Documentos propios

| Documento | Necesidad |
|---|---|
| **Política de privacidad** | 🟡 Pública, en español e inglés ⏳ F5-23. Steam exige cumplir con la Steam Privacy Policy; la fuente leída no dice si la tienda pide una URL de privacidad propia: ⏳ F5-27 lo confirma el **autor** en el panel de Steamworks al preparar la página. Aunque no se recopilen datos, conviene tenerla y decirlo claramente |
| **Términos de uso / EULA** | 🟡 Recomendable, no se encontró que Steam lo exija (la página de alta no menciona un EULA propio) ⏳ F5-24 y F5-27. El Steam Subscriber Agreement ya rige la relación del jugador con Steam |
| **Créditos y licencias de terceros** | Obligatorio por licencias (Godot, GodotSteam, fuentes, assets, música) ⏳ F5-25 |
| **Política de reembolsos** | La gestiona Steam; verifica su política vigente al preparar la ficha ⏳ F5-33 |

## 7 · Propiedad intelectual y licencias

| Tema | Acción |
|---|---|
| **Nombre del juego y marca** | Buscar conflictos de marca y de nombre en tiendas antes de fijar el título. "Valdoria" es el nombre del mundo; el título es **Veta de Fortuna / Vein of Fortune**, pendiente de búsqueda de marca formal ⏳ F5-29. Hay que hacerla **antes de abrir la página «Próximamente»**, porque la página publica el nombre 🟡 |
| **Referencias** | Fallout, Dave the Diver, Papers, Please, Balatro son **inspiración de estilo**, no se copian nombres, personajes, arte ni sonidos |
| **Registro de licencias** | Tabla con: asset, fuente, licencia, uso comercial permitido, enlace y captura de los términos al momento de la descarga (`studio/data/assets.json`). **Una fuente sin licencia comercial clara no entra** |
| **Contenido generado con IA** | Revisar los términos comerciales de **cada herramienta y plan**. El arte generado íntegramente por IA puede no tener protección de derecho de autor en algunas jurisdicciones; el arte propio retocado ayuda |
| **PixelLab (arte definitivo)** | 🟡 Términos leídos el 2026-10-15 en pixellab.ai/termsofservice (versión «Last Updated: 2025-11-23»): conservas la propiedad de lo que creas (cláusulas 1.3 y 3.3) y se permite el uso comercial; **no puedes usar las imágenes para entrenar tus propios modelos** (1.2); el uso programático solo por su API oficial (2.2); el **usuario responde** de que el resultado no infrinja derechos de terceros (3.3); el servicio se da «tal cual», sin garantía (5.1); las funciones y los precios pueden cambiar (2.1). El texto leído **no distingue entre plan gratuito y de pago**. No garantiza protección de derecho de autor sobre lo generado. **Formalización:** captura de los términos y del plan elegido al hacer la prueba ⏳ F4-227; registro final ⏳ F5-26. Hasta F4-227 no se contrata ni se gastan créditos ([12](12-direccion-de-arte.md)) |
| **Herramienta de las referencias provisionales** | ⏳ F5-26 Las imágenes provisionales se generaron con gpt_image_2_5 vía Higgsfield; sus términos comerciales **no se leyeron**. Desde F0-35 el repositorio es público con el arte provisional marcado como IA y sin licencia de uso. Fuente secundaria (ayuda de Higgsfield, cláusula 4.4, 2026-10-24): no reclaman la propiedad y no restringen el uso comercial; pueden entrenar con el contenido. Falta leer los Términos completos y los del modelo; lo registra el **asesor legal** (por ejemplo, el hub o el README públicos) |
| **Software de terceros** | Godot (licencia MIT): incluir su aviso en los créditos. 🟡 **GodotSteam**: verifica su licencia al integrarlo ⏳ F1-45. El **SDK de Steamworks** se rige por el acuerdo de distribución de Valve (⏳ F5-22 lo lee el autor al firmar el alta). Revisa cada plugin o librería |
| **Voces** | Si algún día se usan voces, contratos o licencias claras; no clonar voces de personas reales sin permiso |

## 8 · Azar y casino (futuro)

| Tema | Nota |
|---|---|
| **Decisión del autor** ✅ (2026-10-13) | El **casino** (el Salón del Farol, [26](26-zonas-y-edificios.md)) llega en la V2.0, la primera actualización tras el lanzamiento, integrado de forma suave. Se acepta la clasificación que corresponda; **solo moneda del juego, sin dinero real**; probabilidades visibles; tope diario; y un interruptor para ocultar el azar |
| **La v1 no tiene azar** 🟡 (el casino va en V2.0, decisión del autor del 2026-10-13) | El cuestionario de Steam de la v1 se contesta **sin juegos de azar** (la v1 no los incluye). 🟡 Esto vale también para cualquier sorteo: la Lotería del Ministerio (F6-46) es azar y llega con el casino, no antes |
| **Política de Steam sobre azar simulado** | ⏳ F6-13 **No se pudo verificar.** Las páginas oficiales leídas (alta, Steam Direct y cuestionario) no mencionan el azar simulado ni el casino. Lo que sí dicen: el contenido debe cumplir las leyes de **cada jurisdicción** donde se ofrezca y las reglas de procesadores de pago, redes de tarjetas y bancos (lista de contenido no permitido, onboarding). Las preguntas exactas aparecen en el cuestionario real del panel de Steamworks. Lo verifica el **asesor legal** con el cuestionario real y con soporte de Steamworks al iniciar F6-13: fuente oficial partner.steamgames.com/doc/gettingstarted/onboarding (Rules and Guidelines) y el Steam Distribution Agreement |
| **Efecto en la clasificación** | 🟡 El azar simulado suele añadir un descriptor de contenido y subir la edad en los sistemas de clasificación; confirma el efecto en el cuestionario (ya aceptado por el autor) |
| **Cambiar el cuestionario tras publicar** | Como algunas respuestas no se editan sin soporte, el lanzamiento del casino implica **actualizar el cuestionario y avisar a Steam** antes de publicar la V2.0 ⏳ F6-13 |
| **Tarea** | Revisión de clasificación y políticas de las tiendas ⏳ F6-13 (la lista de la fase móvil se suma si el casino va a móvil) |

La decisión no cambia nada de lo que se construye en la v1 (la v1 no tiene azar), por eso se aplaza con su tarea.

## 9 · Protección de datos

- Con un juego **sin cuentas propias, sin anuncios y sin analíticas** en la v1, la carga es mínima: se declara que el juego no recopila datos.
- El juego usa servicios de Steam (nube, logros): esos datos los trata Steam bajo su política de privacidad. Aun así, la política propia debe decir qué guarda el juego (partidas locales y en la nube de Steam) y que no envía datos a terceros. 🟡
- **Nube y Hardcore ✅:** Auto-Cloud con una carpeta de guardados pequeños y hasta 5 partidas; en Hardcore manda el guardado **local**. La fuente confirma que el patrón de archivos de Auto-Cloud lo eliges tú: excluye la partida Hardcore. La fuente no da cuotas por defecto; las fijas en el panel de Steamworks ⏳ F4-234.
- Cualquier SDK o servicio que se agregue (analíticas, anuncios, reporte de fallos) **cambia la declaración** y puede activar leyes de protección de datos (por ejemplo, GDPR, LGPD, CCPA, según el público).
- Mantener un inventario de **qué datos entran y salen del equipo**, aunque sea "ninguno".

### Telemetría y privacidad 🟡

- La **telemetría local** (capa A, ver [10](10-tecnico-y-herramientas.md)) no envía datos: el probador decide si comparte el archivo. No incluye nombre de jugador ni de tienda.
- La **capa B** (datos de tienda) pasa de Play Vitals a lo que Steam entregue. ⏳ F5-40 No se verificó qué informes de fallos ofrece Steamworks: lo comprueba el **autor** con el panel de Steamworks.
- Si algún día se activa el **envío opcional** (capa C): consentimiento explícito, datos anónimos, actualización de la política de privacidad y del cuestionario ⏳ F5-41.
- Fichas de tienda y política de privacidad en **español e inglés**.

## 10 · Steam Deck, Steam Input y nube (cumplimiento)

Verificado el 2026-10-15 en partner.steamgames.com/doc/steamdeck/compat. Esto es un **resumen**; el detalle técnico vive en [10](10-tecnico-y-herramientas.md).

- **Entrada:** la configuración de mando por defecto debe dar acceso a **todo el contenido** sin tocar ajustes. Los glifos deben coincidir con el dispositivo activo (la fuente recomienda la API de Steam Input). El texto escrito necesita el teclado en pantalla de Steam o una entrada propia con mando ⏳ F4-236.
- **Pantalla:** resolución de **1280×800** (preferida) o 1280×720. Texto legible a unos 30 cm: altura mínima de **9 px** a 1280×800, **12 px** recomendado, y conviene un tamaño de texto ajustable ⏳ F4-239.
- **Fluidez:** sin avisos de que SteamOS o la GPU no son compatibles; si hay lanzador, debe navegarse con mando (se recomienda no tener lanzador). Rendimiento: **30 fps a 800p** por defecto.
- **Linux y Proton:** si hay build nativo de Linux, Valve lo prueba primero; si falla, prueba el de Windows con Proton y publica el mejor resultado. Los problemas bloqueantes dan el distintivo *No compatible*.
- **Revisión:** primero hay que pasar la revisión normal del build; se pide con «Steam Hardware Compatibility Review» (acceso limitado); resultados en ~1 semana.
- **Steam Input ⏳ F4-239:** la fuente dice que se recomienda; no se confirmó si es obligatorio para *Verified*. Lo confirma el **autor** en F4-239 con la lista oficial.

## 11 · Fiscalidad y estructura

| Tema | Nota |
|---|---|
| Ingresos | Steam paga a una cuenta bancaria cuyo titular coincide con el nombre del alta (sección 2). Depende del país |
| Persona física vs. sociedad | ⏳ F4-241 Decidir con un contador local **antes** de iniciar el alta de Steamworks (el nombre legal queda en el contrato) |
| Impuestos de venta/IVA | Normalmente los gestiona la tienda en sus mercados; verificar. La cuota de 100 USD lleva IVA donde corresponda |

## 12 · Fase móvil (después de la 1.0)

Se activa solo cuando la 1.0 esté publicada y estable en Steam ([ADR-0009](adr/0009-pc-primero-movil-despues.md)). Lo siguiente se conserva de la versión anterior de este documento y **debe volver a verificarse** en la fuente vigente cuando llegue el momento. Tareas: F6-18 a F6-23 (iOS) y F6-71 a F6-76 (Android).

### Cuentas de desarrollador

| Tienda | Qué hace falta | Nota |
|---|---|---|
| Google Play | Cuenta de desarrollador (pago único, ≈25 USD) y verificación de identidad ⏳ F6-75 | Las cuentas personales nuevas suelen requerir una **prueba cerrada con un mínimo de testers durante un tiempo** antes de producción. Verificar el requisito vigente ⏳ F6-76 |
| Apple | Apple Developer Program (≈99 USD/año) ⏳ F6-18 | Solo si se sale en iOS |

### Formularios de las tiendas móviles

- **Google Play:** declaración de seguridad de datos (*Data safety*), cuestionario de **clasificación de contenido** (IARC), público objetivo, declaraciones sobre anuncios y otros ⏳ F6-75.
- **Apple:** etiquetas de privacidad (*App Privacy*), clasificación por edad, declaración de cifrado ⏳ F6-22.
- **Telemetría de tienda móvil:** **Google Play Vitals** recopila datos de fallos por su cuenta; revisar cómo debe reflejarse en los formularios.
- **Claves y firma:** keystore de Android y su respaldo seguro ⏳ F6-71; firma de iOS ⏳ F6-19.
- **Prueba cerrada y revisión** de Google Play ⏳ F6-76; revisión de Apple ⏳ F6-23.
- **Casino en móvil:** las tiendas móviles tienen políticas propias sobre azar simulado; se revisan aparte si el casino llega a móvil.
- Coherencia: lo que se declare debe coincidir con lo que el juego realmente hace (**sin cuentas, sin anuncios, sin analíticas** en la v1).

## 13 · Calendario legal sugerido

| Momento | Qué hacer |
|---|---|
| Fases 0–3 (personal) | Registro de licencias desde el primer asset; no meter secretos ni datos personales; título provisional; decidir el país fiscal y la estructura con un contador (sin urgencia, pero antes de F4) |
| Antes de pruebas externas | Política de privacidad borrador; revisar términos de herramientas de IA |
| Inicio de F4 | Prueba de PixelLab y registro de sus términos ⏳ F4-227; búsqueda de marca formal si el nombre se va a publicar ⏳ F5-29 |
| Con tiempo antes de F4-240 | Cuenta de Steamworks, cuota, entrevista fiscal y bancaria; cuestionario de contenido, declaración de IA, privacidad |
| Final de F4 | Página «Próximamente» con arte definitivo ⏳ F4-240 |
| Antes de publicar | Créditos, registro final de licencias, revisión del build por Valve, cumplimiento de las políticas vigentes ⏳ F5-25, F5-26, F5-37 |
| Después de la 1.0 estable | Fase móvil (sección 12) y casino ⏳ F6-13 |

## Pendiente

- ⏳ F4-241 País de residencia fiscal del autor y estructura (persona física o sociedad): lo resuelve el autor con un contador local.
- ⏳ F5-29 Búsqueda de marca formal de «Veta de Fortuna / Vein of Fortune».
- ✅ El público objetivo no incluye menores (2026-10-13).
- ⏳ F4-227 Términos comerciales de PixelLab (ya leídos, pendiente de captura y plan) y ⏳ F5-30 declaración de IA de Steam.
- ❓ Cómo se declaran los textos, traducciones, música y voces si los produce IA: lo decide el autor antes de producir el contenido final.
- ⏳ F5-22 Plazos reales de Steamworks (21 o 30 días de espera; verificación de 10 a 15 días hábiles o hasta 30 días): los confirma el autor en el panel de Steamworks.
- ⏳ F5-28 Requisitos de clasificación de Brasil y Corea en Steam: los verifica el autor con el cuestionario real.
- ⏳ F6-13 Política de Steam sobre azar simulado con moneda del juego: la verifica el asesor legal con el cuestionario real y soporte de Steamworks.
- ⏳ F5-27 Si Steam exige URL de privacidad y EULA propios: el autor lo comprueba en el panel. ⏳ F4-239 Si Steam Input es obligatorio para *Verified*.
- ⏳ F5-26 Términos de gpt_image_2_5 vía Higgsfield, si algún provisional llegara a público.
- ⏳ F5-40 Qué informes de fallos ofrece Steam (capa B de telemetría).

## Fuentes verificadas (2026-10-15)

- Steamworks, alta: https://partner.steamgames.com/doc/gettingstarted/onboarding
- Cuota por aplicación: https://partner.steamgames.com/doc/gettingstarted/appfee
- Steam Direct: https://partner.steamgames.com/steamdirect
- Preguntas frecuentes (impuestos): https://partner.steamgames.com/doc/gettingstarted/faq
- Revisión de página y build: https://partner.steamgames.com/doc/store/review_process
- Página «Próximamente»: https://partner.steamgames.com/doc/store/coming_soon
- Fechas de lanzamiento: https://partner.steamgames.com/doc/store/release_dates
- Imágenes de tienda: https://partner.steamgames.com/doc/store/assets/standard
- Cuestionario de contenido e IA: https://partner.steamgames.com/doc/gettingstarted/contentsurvey
- Clasificación en Alemania: https://partner.steamgames.com/doc/gettingstarted/contentsurvey/germany
- Steam Deck: https://partner.steamgames.com/doc/steamdeck/compat
- Steam Cloud: https://partner.steamgames.com/doc/features/cloud
- Términos de PixelLab: https://www.pixellab.ai/termsofservice
