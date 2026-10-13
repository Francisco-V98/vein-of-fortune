# 11 · Legal y cumplimiento

> **Aviso:** esto es una lista de verificación de trabajo, **no asesoría legal**. Los requisitos de las tiendas y las leyes cambian. Cada punto debe verificarse en la fuente oficial vigente al momento de publicar y, para temas fiscales y de propiedad intelectual, con un profesional local. El país de residencia del autor aún no está definido y afecta mucho la parte fiscal.

El proyecto es personal primero. Esta lista se activa por etapas: casi nada importa hasta que se piense publicar.

## 1 · Cuentas de desarrollador

| Tienda | Qué hace falta | Nota |
|---|---|---|
| Google Play | Cuenta de desarrollador (pago único, ≈25 USD) y verificación de identidad | Las cuentas personales nuevas suelen requerir una **prueba cerrada con un mínimo de testers durante un tiempo** antes de producción. Verificar el requisito vigente |
| Apple | Apple Developer Program (≈99 USD/año) | Solo si se sale en iOS |
| Steam (futuro) | Cuota por aplicación | Exige declarar el uso de IA |

## 2 · Documentos propios

| Documento | Necesidad |
|---|---|
| **Política de privacidad** | Se necesita un enlace público para publicar. Aunque no se recopilen datos, conviene tenerla y decirlo claramente |
| **Términos de uso / EULA** | Recomendable, no siempre obligatorio |
| **Créditos y licencias de terceros** | Obligatorio por licencias (Godot, fuentes, assets, música) |
| **Política de reembolsos** | La gestionan las tiendas |

## 3 · Formularios de las tiendas

- **Google Play:** declaración de seguridad de datos (*Data safety*), cuestionario de **clasificación de contenido**, público objetivo, declaraciones sobre anuncios y otros.
- **Apple:** etiquetas de privacidad (*App Privacy*), clasificación por edad, declaración de cifrado.

Coherencia: lo que se declare debe coincidir con lo que el juego realmente hace (**sin cuentas, sin anuncios, sin analíticas** en la v1).

## 4 · Propiedad intelectual

| Tema | Acción |
|---|---|
| **Nombre del juego y marca** | Buscar conflictos de marca y de nombre en tiendas antes de fijar el título. "Valdoria" es el nombre del mundo; el título es **Veta de Fortuna / Vein of Fortune**, pendiente de búsqueda de marca formal |
| **Referencias** | Fallout, Dave the Diver, Papers, Please, Balatro son **inspiración de estilo**, no se copian nombres, personajes, arte ni sonidos |
| **Registro de licencias** | Tabla con: asset, fuente, licencia, uso comercial permitido, enlace y captura de los términos al momento de la descarga |
| **Contenido generado con IA** | Revisar los términos comerciales de **cada herramienta y plan**. El arte generado íntegramente por IA puede no tener protección de derecho de autor en algunas jurisdicciones; el arte propio retocado ayuda |
| **Software de terceros** | Godot (licencia MIT): incluir su aviso de licencia en la pantalla de créditos. Revisar cada plugin o librería |
| **Voces** | Si algún día se usan voces, contratos o licencias claras; no clonar voces de personas reales sin permiso |

## 5 · Contenido y clasificación por edad

| Tema | Nota |
|---|---|
| Temas del juego | Corrupción, extorsión, violencia y negocios ilegales influyen en la clasificación por edad. Mundo y naciones **ficticios**, sin política real |
| Juegos de azar simulados | El **casino** será una de las primeras actualizaciones tras el lanzamiento, integrado de forma suave. Afecta la clasificación por edad y tiene políticas propias en las tiendas. **Decisión del autor:** se acepta la clasificación que corresponda. Solo moneda del juego, sin dinero real. Revisar los requisitos vigentes antes de implementarlo |
| Público | Definir si el juego está dirigido o no a menores. Si se dirige a menores aplican reglas mucho más estrictas |
| Textos generados o de usuario | Nombres de personaje y tienda se validan (longitud, caracteres, filtro de palabras ofensivas) |

## 6 · Protección de datos

- Con un juego **sin cuentas, sin anuncios y sin analíticas**, la carga es mínima: se declara que no se recopilan datos.
- Cualquier SDK o servicio que se agregue (analíticas, anuncios, nube, reporte de fallos) **cambia la declaración** y puede activar leyes de protección de datos (por ejemplo, GDPR, LGPD, CCPA, según el público).
- Mantener un inventario de **qué datos entran y salen del dispositivo**, aunque sea "ninguno".

### Telemetría y privacidad 🟡

- La **telemetría local** (capa A, ver [10](10-tecnico-y-herramientas.md)) no envía datos: el probador decide si comparte el archivo. No incluye nombre de jugador ni de tienda.
- **Google Play Vitals** recopila datos de fallos por su cuenta; revisar cómo debe reflejarse en los formularios.
- Si algún día se activa el **envío opcional** (capa C): consentimiento explícito, datos anónimos, actualización de la política de privacidad y de los formularios.
- Fichas de tienda y política de privacidad en **español e inglés**.

## 7 · Fiscalidad y estructura

| Tema | Nota |
|---|---|
| Ingresos | Las tiendas piden información fiscal para pagar. Depende del país |
| Persona física vs. sociedad | Decidir con un contador local antes de cobrar |
| Impuestos de venta/IVA | Normalmente los gestiona la tienda en sus mercados; verificar |

## 8 · Calendario legal sugerido

| Momento | Qué hacer |
|---|---|
| Fases 0–2 (personal) | Registro de licencias desde el primer asset; no meter secretos ni datos personales; elegir título provisional |
| Antes de pruebas externas | Política de privacidad borrador; revisar términos de herramientas de IA |
| Antes de la prueba cerrada en Google Play | Cuenta de desarrollador, formularios, política de privacidad pública, clasificación |
| Antes de publicar | Búsqueda de marca, créditos, revisión fiscal, cumplimiento de las políticas vigentes |
| Antes de Steam o iOS | Requisitos específicos de cada plataforma |

## Pendiente

- ❓ País de residencia del autor.
- ⏳ F5-29 Búsqueda de marca formal de «Veta de Fortuna / Vein of Fortune».
- ❓ Si el público objetivo incluye menores.
- ❓ Herramientas de IA concretas y sus términos comerciales.
