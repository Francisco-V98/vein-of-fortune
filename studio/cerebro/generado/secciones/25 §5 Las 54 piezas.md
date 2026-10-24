---
id: "doc-25-s05"
tipo: "seccion"
title: "5 · Las 54 piezas ✅"
aliases: ["doc-25-s05"]
documento: "[[25 Finales y epílogos]]"
limpieza: 100
abiertos: 0
espera: 3
aplazado_a: ["[[F4-109 Escalera de estatus y condiciones de ascenso]]", "[[F4-147 Colapso del mercado de la Aetherita]]", "[[F4-212 Textos finales de las 54 piezas de los epílogos]]"]
estado: "con-aplazados"
anterior: "[[25 §4 La cabecera]]"
siguiente: "[[25 §6 Cobertura de combinaciones]]"
arriba: "[[25 Finales y epílogos]]"
fuente: "studio/docs/25-finales-y-epilogos.md:107"
generado: true
---

# 5 · Las 54 piezas ✅

> Estado: que son 54, unas 17 por partida y el medio que narra cada pieza son decisión del autor (2026-10-12); el reparto por tema y qué lee…

← [[25 §4 La cabecera]] · [[25 Finales y epílogos|↑ 25]] · [[25 §6 Cobertura de combinaciones]] →

**Estado:** que son 54, unas 17 por partida y el medio que narra cada pieza son decisión del autor (2026-10-12); el reparto por tema y qué lee cada una los confirmó el 2026-10-16 ([[F0-80 Pasada de cierre - biblia, documentos de pasado, variantes|F0-80]]). Los textos de ejemplo son guía ⏳ [[F4-212 Textos finales de las 54 piezas de los epílogos|F4-212]]. Los estados `e-…` son los de la sección 8.

### 5.1 · Cómo se eligen

- Cada tema devuelve **una pieza** por partida, con una regla en orden: se aplica la primera que se cumple. Montenegro puede devolver dos (DU-04 solo si revelas).
- Por partida salen **17 piezas** (18 si revelas): 1 de cabecera, 8 de personajes (Reme, Esteban, Casilda, Quiroga, Lucía, Teo, Montenegro y la Unión), 3 de facciones, 2 de mundo, 2 de mercado y 1 de familia.
- Las piezas con dos líneas muestran **una** según la condición que se indica.

| Tema | Piezas | Reparto |
|---|---|---|
| Cabecera | H-01 a H-06 | 6 |
| Reme | RE-01 a RE-03 | 3 |
| Esteban | ES-01 a ES-04 | 4 |
| Casilda | CA-01 a CA-04 | 4 |
| Quiroga | QU-01 a QU-03 | 3 |
| Lucía | LU-01 a LU-04 | 4 |
| Teo | TE-01 a TE-03 | 3 |
| Montenegro | DU-01 a DU-04 | 4 |
| Unión | UN-01 a UN-03 | 3 |
| Facciones | FC-01 a FC-06 | 6 |
| Mundo | MU-01 a MU-06 | 6 |
| Mercado | ME-01 a ME-05 | 5 |
| Familia | FM-01 a FM-03 | 3 |
| **Total** | | **54** |

### 5.2 · Personajes

**Reme.** Siempre aliada y sin reproche ✅. Se elige por [[Bandera reme proteccion|f-reme-proteccion]]. El hueco `{facción-reme}` lo rellena `e-variante-reme`. Todas terminan con una **cola** según `e-abono`: si sigue, «Del giro de cada mes, doña Reme dice que no pregunta.»; si lo cortaron, «Del giro de cada mes, doña Reme dice que este mes no llegó.» ✅ (según `e-abono`, sección 8)

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| RE-01 | Proteger | [[Bandera reme proteccion\|f-reme-proteccion]], `e-variante-reme` | Voz | «Doña Reme sale de la cadena de `{facción-reme}`, que no se lo perdonará. Ella dice que no le pesa.» |
| RE-02 | Saldar | ídem | Voz | «Doña Reme ve cerrada su deuda con `{facción-reme}`. Se espera que siga atendiendo la ventanilla, con el café de siempre.» |
| RE-03 | Dejar | ídem | Voz | «Doña Reme conserva su casa de préstamos y se espera que ayude a `{nombre}` a su manera. Sin ruido y sin reproches.» |

**Esteban.** Se elige por `e-esteban`; si vendes al Consorcio, ES-04 manda sobre las demás.

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| ES-01 | Se une (tramo alto) | `e-esteban`, [[Bandera destino\|f-destino]] | Heraldo | **Si revelas:** «Esteban Arvel deja la dirección del Consorcio, pero asegura que la casa seguirá en pie. Se espera que declare sobre el fondo reservado.» **Si no:** «Esteban Arvel se aparta de la dirección del Consorcio, pero no explica por qué. Se espera que guarde silencio, por ahora.» |
| ES-02 | Se aparta (tramo medio) | `e-esteban` | Teletipo | «ESTEBAN ARVEL SE APARTA DE LOS NEGOCIOS FAMILIARES Y NO DICE POR QUÉ. SE ESPERA QUE LO DECIDA SOLO. SIN CONFIRMAR» |
| ES-03 | Defiende (tramo bajo) | `e-esteban` | Heraldo | «Esteban Arvel asume la defensa del Consorcio, pero evita hablar de los contratos de Sierra Alta.» |
| ES-04 | Vendes al Consorcio | [[Bandera comprador\|f-comprador]], `e-esteban` | Voz | **Si estaba en tramo alto:** «Esteban Arvel rompió con su casa, y su casa paga ahora el silencio de `{nombre}`. Se espera que no vuelva a firmar con su apellido.» **Si no:** «Esteban Arvel sabe lo que paga su apellido. Se espera que siga firmando, y que nadie le pregunte.» |

**Casilda.** Regla en orden: compradora, aliada, monopolio, resto.

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| CA-01 | Le vendes la verdad | [[Bandera comprador\|f-comprador]] | Teletipo | «CASILDA IBARRA GUARDA LO QUE COMPRÓ. SE ESPERA MÁS LUZ EN EL HOLLÍN, A SU PRECIO. SIN CONFIRMAR» |
| CA-02 | Te aliaste con Los Faroleros | [[Bandera alianza\|f-alianza]] | Teletipo | «LOS FAROLEROS EXTIENDEN SU LUZ POR LOS BARRIOS ALIADOS. LA DEUDA DE LUZ SE COBRA IGUAL. SIN CONFIRMAR» |
| CA-03 | Aceptaste o compartiste su monopolio | [[Bandera monopolio\|f-monopolio]], [[Bandera destino\|f-destino]] | Teletipo | **Si revelas:** «CASILDA IBARRA MANDA EN LOS ENCARGOS ESPECIALES DE AETHERITA. SE ESPERA QUE LA PRIMA CAIGA CON LA NOTICIA Y REBOTE DESPUÉS. SIN CONFIRMAR» **Si no:** «…SE ESPERA QUE LA PRIMA SE MANTENGA. SIN CONFIRMAR» |
| CA-04 | El resto | — | Voz | «Los Faroleros siguen cobrando la luz en el Hollín. Casilda Ibarra no pide que la quieran: pide que se pague a tiempo.» |

**Quiroga.** Se elige por [[Bandera archivo|f-archivo]]. Cubre [[Bandera quiroga salida|f-quiroga-salida]] con la segunda línea de QU-02.

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| QU-01 | Proteger el archivo | [[Bandera archivo\|f-archivo]] | Heraldo | «El inspector Quiroga se traslada a Puerto Meridiano, pero el Ministerio no explica qué pasará con sus expedientes.» |
| QU-02 | Usarlo | [[Bandera archivo\|f-archivo]], [[Bandera quiroga salida\|f-quiroga-salida]] | Heraldo / Voz | **Si no le cumpliste la salida:** «El Ministerio abre un expediente al inspector Quiroga por irregularidades, pero lo atribuye a actos aislados.» **Si le conseguiste el retiro:** (Voz) «El inspector Quiroga consigue su retiro antes de que lleguen los auditores. Sus expedientes, dicen, hablarán solos.» |
| QU-03 | Venderlo | [[Bandera archivo\|f-archivo]] | Teletipo | «EL ARCHIVO DEL INSPECTOR QUIROGA CAMBIÓ DE MANOS. QUIROGA NO CONTESTA. SE ESPERA QUE SU COMPRADOR LO USE A SU ANTOJO. SIN CONFIRMAR» |

**Lucía.** Cubre las cinco combinaciones decididas: tres si revelas y una (con dos líneas) si callas o vendes. No publica el acta en ninguna ✅.

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| LU-01 | Revelas y su tramo es alto: publica contigo | `e-lucia` | Teletipo | «LUCÍA MONTALVO PUBLICA LAS CINTAS JUNTO A `{nombre}`, HASTA DONDE LLEGAN. UNA SOLA VERSIÓN. LA COMISIÓN NO RESPONDE. SIN CONFIRMAR» |
| LU-02 | Revelas y su tramo es bajo: publica sin ti | `e-lucia` | Voz | «La Voz del Hollín publica antes que nadie la historia de Lucía Montalvo, y sin `{nombre}`. Se espera que el Heraldo la desmienta.» |
| LU-03 | Revelas y su tramo es medio: no publica, lo publicas tú | `e-lucia` | Voz | «`{nombre}` publica en La Voz del Hollín. Llega a pocos lectores, pero llega. Lucía Montalvo, por ahora, no dice nada.» |
| LU-04 | Callas o vendes | `e-lucia`, [[Bandera destino\|f-destino]] | Teletipo | **Tramo bajo, filtra:** «CIRCULA UNA VERSIÓN A MEDIAS SOBRE LA COMISIÓN. SIN PRUEBAS Y SIN CINTAS. LA FIRMA UNA PLUMA DEL TELETIPO. SIN CONFIRMAR» **Medio o alto, calla:** «LUCÍA MONTALVO PREPARA UNA HISTORIA Y NO LA PUBLICA. SU REDACTOR ESPERA. SIN CONFIRMAR» |

**Teo.** Se queda, se va o muere ✅. Lo calcula `e-teo` con la regla de [[23 Árbol de decisiones y consecuencias|23]]. Sin Teletipo.

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| TE-01 | Se queda | `e-teo` | Voz | «Teo Cárdenas sigue en el Hollín y se espera que vuelva al turno. Dice que ya no tiene nada que callar.» |
| TE-02 | Se va | `e-teo` | Voz | «Teo Cárdenas deja el Hollín. No dice adónde ni guarda rencor. Los suyos le dejan el sitio en la mesa.» |
| TE-03 | Muere | `e-teo` | Voz | «La Unión anuncia un acto en memoria de Teo Cárdenas, minero veterano. Se espera que acudan todos los que aprendieron con él.» |

**Montenegro.** Regla única, en este orden ✅: (1) vendes al Ministerio, DU-01; (2) si no, Unión alta y al menos 2 pruebas, DU-02; (3) en el resto, DU-03. DU-04 se suma si revelas. Nunca cae, no se arrepiente ni nombra sucesor ✅. Siempre se conservan al menos tres pruebas ([[23 Árbol de decisiones y consecuencias|23]], sección 8), así que en la práctica solo importa la Unión.

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| DU-01 | Te compra con el sello | [[Bandera comprador\|f-comprador]] | Heraldo | «El Ministerio informa de que `{nombre}` cuenta con el sello del ministro Montenegro, pero no precisa qué espera a cambio.» |
| DU-02 | Intenta borrarte y falla | `e-montenegro`, `e-union` | Teletipo | «MONTENEGRO INTENTA CERRAR LAS LICENCIAS DE `{tienda}`. LA UNIÓN SE PLANTA. SE ESPERA QUE NO LO LOGRE. SIN CONFIRMAR» |
| DU-03 | Te amenaza | `e-montenegro` | Heraldo | «El ministro Montenegro recuerda que las licencias se renuevan, pero no todas se renuevan igual. No hace más comentarios.» |
| DU-04 | Comunicado oficial, solo si revelas | [[Bandera destino\|f-destino]] | Heraldo | «El Ministerio informa de que el ministro Montenegro queda bajo investigación, pero continúa en funciones.» |

**Unión.** Se elige por `e-union`. Cubre todas las salidas, también las que no son revelar.

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| UN-01 | Tramo alto | `e-union`, [[Bandera destino\|f-destino]] | Voz | **Si revelas:** «La Unión se organiza para vigilar La Fosa junto a `{nombre}`. Se espera que los delegados pidan revisiones médicas en todos los turnos.» **Si no:** «La Unión sigue con `{nombre}` sin conocer toda la historia. Se espera que el Hollín trabaje, y que los delegados le guarden un sitio.» |
| UN-02 | Tramo medio | ídem | Voz | **Si revelas:** «La Unión ni acompaña ni combate a `{nombre}`. Los delegados esperan, y piden pruebas.» **Si no:** «La Unión trata a `{nombre}` como a un comerciante más. Se espera que cobre favores en la próxima huelga.» |
| UN-03 | Tramo bajo | ídem | Voz | **Si revelas:** «En el Hollín nadie respalda a `{nombre}`. La Unión se entera por el Heraldo y espera, con recelo, a ver quién habla primero.» **Si no:** «La Unión no olvida cómo actuó `{nombre}` en la huelga. Se espera que el Hollín se cierre despacio, sin ruido.» |

### 5.3 · Facciones, mundo, mercado y familia

**Facciones.** Salen tres por partida, una por facción aliable: la aliada o la no aliada, según [[Bandera alianza|f-alianza]]. Cada una tiene una línea si revelas y otra si no.

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| FC-01 | Consorcio aliado | [[Bandera alianza\|f-alianza]], [[Bandera destino\|f-destino]] | Heraldo | **Revelas:** «El Consorcio Arvel mantiene su alianza con `{nombre}`, pero pide que sus cuentas no se mezclen con las de la Comisión.» **No:** «El Consorcio Arvel renueva contratos con `{nombre}`, pero prefiere no hablar de sus cuentas.» |
| FC-02 | Consorcio no aliado | ídem | Heraldo | **Revelas:** «El Consorcio Arvel se declara ajeno a la Comisión, pero se espera que sus cuentas pasen por revisión.» **No:** «El Consorcio Arvel seguirá compitiendo por los contratos del Hollín, pero sin `{nombre}` en su mesa.» |
| FC-03 | Ministerio aliado | ídem | Heraldo | **Revelas:** «El Ministerio informa de que la licencia de `{nombre}` sigue vigente, pero se espera que revise su trato.» **No:** «El Ministerio mantiene la licencia ampliada de `{nombre}` y se espera que la renueve, pero le recuerda quién la firma.» |
| FC-04 | Ministerio no aliado | ídem | Heraldo | **Revelas:** «El Ministerio promete orden en el Hollín, pero se espera que apriete las inspecciones.» **No:** «El Ministerio sigue de cerca las licencias de `{nombre}`, pero no anuncia sanciones.» |
| FC-05 | Faroleros aliados | ídem | Teletipo | **Revelas:** «LOS FAROLEROS OFRECEN LUZ EN EL HOLLÍN SI EL MINISTERIO CORTA LA SUYA. SIN CONFIRMAR» **No:** «LOS FAROLEROS GUARDAN LA LUZ A `{nombre}`. LA DEUDA DE LUZ CRECE CON ELLA. SIN CONFIRMAR» |
| FC-06 | Faroleros no aliados | ídem | Teletipo | **Revelas:** «LOS FAROLEROS SE PREPARAN PARA LO QUE VENGA EN EL HOLLÍN. SIN CONFIRMAR» **No:** «LOS FAROLEROS SIGUEN COBRANDO LA LUZ EN EL HOLLÍN, CON O SIN `{nombre}`. SIN CONFIRMAR» |

**Mundo.** Dos por partida, según [[Bandera destino|f-destino]]. Si el país «sigue igual», se cuenta con esperanza y filo, no con cinismo.

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| MU-01 | Revelas: La Fosa y la Comisión | [[Bandera destino\|f-destino]] | Heraldo | «El Ministerio informa de que la Comisión del Éter colabora con las autoridades, pero sostiene que La Fosa es segura.» |
| MU-02 | Revelas: el país | [[Bandera destino\|f-destino]] | Voz | «¡Valdoria entera habla del mal del éter! El Hollín sabe cómo acaban los ruidos grandes, y esta vez no piensa callar.» |
| MU-03 | Callas: La Fosa | [[Bandera destino\|f-destino]] | Heraldo | «El Ministerio informa de que La Fosa opera con normalidad, pero amplía los relevos de turno.» |
| MU-04 | Callas: el país | [[Bandera destino\|f-destino]] | Voz | «En el Hollín sigue la tos y sigue el trabajo. Los mineros piden aire. De momento, el aire no llega.» |
| MU-05 | Vendes: lo vendido | [[Bandera destino\|f-destino]], [[Bandera comprador\|f-comprador]] | Teletipo / Heraldo | **Casilda:** «ALGO CAMBIÓ DE MANOS EN EL PUERTO. NADIE DICE QUÉ. LA LUZ NUEVA TIENE DUEÑA. SIN CONFIRMAR» **Consorcio:** «EL CONSORCIO ARVEL PAGA A QUIEN CALLA. NADIE DICE POR QUÉ. SIN CONFIRMAR» **Ministerio:** (Heraldo) «El Ministerio informa de que la Comisión mantiene sus reservas sobre La Fosa, pero agradece la colaboración de `{nombre}`.» |
| MU-06 | Vendes: el país | [[Bandera destino\|f-destino]] | Voz | «Valdoria sigue igual: los mismos contratos y los mismos apagones. Lo que cambia es quién guarda la llave.» |

**Mercado.** Una por salida (ME-01 a ME-03) y una de las dos restantes. Sin cifras ✅. Al revelar, la Aetherita cae, rebota y queda algo por debajo del precio de antes ✅; el rebote va en prospectivo y sin cifras. El tope diario de la Aetherita es del 15 % ✅ ([[28 Números base de la economía|28]]); la curva y el nivel exacto ⏳ [[F4-147 Colapso del mercado de la Aetherita|F4-147]].

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| ME-01 | Revelas | [[Bandera destino\|f-destino]] | Teletipo | «AETHERITA CAE POR TRAMOS DIARIOS. SE ESPERA QUE REBOTE Y QUEDE ALGO MÁS ABAJO. SIN CONFIRMAR» |
| ME-02 | Callas | [[Bandera destino\|f-destino]] | Heraldo | «La Aetherita se mantiene firme y se espera que siga al alza, pero el Heraldo recomienda prudencia.» |
| ME-03 | Vendes | [[Bandera destino\|f-destino]], [[Bandera comprador\|f-comprador]] | Teletipo / Heraldo | **Casilda:** «LOS ENCARGOS NEGROS DE AETHERITA LLEGAN MÁS A MENUDO AL PUERTO. CASILDA IBARRA SABE POR QUÉ. SIN CONFIRMAR» **Consorcio:** (Heraldo) «La Aetherita sube con las compras del Consorcio, pero el Heraldo no ve motivo de alarma.» **Ministerio:** (Heraldo) «La Aetherita se mantiene gracias a la cuota oficial, pero se espera que el Ministerio la vigile de cerca.» |
| ME-04 | Si Esteban no defiende: mercado negro | [[Bandera monopolio\|f-monopolio]] | Teletipo | **Aceptaste o compartiste:** «EL MERCADO NEGRO SE REACOMODA. SE ESPERA MÁS VIGILANCIA DE NOCHE. SIN CONFIRMAR» **Rechazaste:** «EL CONSORCIO Y EL MINISTERIO SE REPARTEN EL HUECO DEL MERCADO NEGRO. SIN CONFIRMAR» |
| ME-05 | Si Esteban defiende: hierro y cobre | `e-esteban` | Heraldo | «El hierro y el cobre se encarecen en Sierra Alta, pero el Consorcio atribuye el movimiento al calendario.» |

**Familia.** Se elige por [[Bandera familia|f-familia]]. La cuenta el narrador, con tuteo.

| ID | Cuándo | Lee | Medio | Ejemplo (guía) |
|---|---|---|---|---|
| FM-01 | Se lo contaste todo | [[Bandera familia\|f-familia]] | Narrador | «Llega una carta de Vega Mansa. Tu padre ya no la escribe con reproche. De la deuda con el banco agrario, dice que {deuda-familia}. Se espera tu visita cuando haya cosecha.» |
| FM-02 | A medias | [[Bandera familia\|f-familia]] | Narrador | «Llega una carta corta de Vega Mansa. En casa saben del puesto, no de la mina. De la deuda con el banco agrario, dice que {deuda-familia}. Se espera que pregunten más de lo que dices.» |
| FM-03 | Nada | [[Bandera familia\|f-familia]] | Narrador | «Después de semanas sin noticias, llega una carta de Vega Mansa. Tu padre no pregunta nada. De la deuda con el banco agrario, solo dice que {deuda-familia}. Se espera que escriba otra.» |

**La deuda del banco agrario ✅.** Las tres cartas cierran la deuda de la familia con una sola línea, sin cifras (decisión del autor, 2026-10-13). El hueco `{deuda-familia}` depende solo del **patrimonio con el que entras en el acta de calibración** ✅ (decisión del autor, 2026-10-16, [[F0-80 Pasada de cierre - biblia, documentos de pasado, variantes|F0-80]]), que se fija una vez al entrar y se guarda como `e-patrimonio-acta` (sección 8): si llega al piso de Magnate (≈ 250 000 esquirlas, [[28 Números base de la economía|28]]) dice «se paga», y si no llega dice «se alivia». Ya no depende del estatus al entrar: para llegar al IV hace falta ser Empresario (el círculo del III lo exige, [[24 Umbrales de acto|24]]), así que con ese criterio «se alivia» nunca habría salido. Magnate se concede **al cerrar** el acta, así que tampoco cuenta para la carta. El jugador medio llega a ≈ 280 000 al cerrar el IV ([[28 Números base de la economía|28]]), así que «se alivia» es la carta del jugador lento. No hay una acción de enviar dinero a casa ni una mecánica nueva. El patrimonio es efectivo más stock a valor justo, sin restar la deuda y sin bienes de consumo ✅; el umbral final lo fija ⏳ [[F4-109 Escalera de estatus y condiciones de ascenso|F4-109]].

---

## Fuente

`studio/docs/25-finales-y-epilogos.md:107`
