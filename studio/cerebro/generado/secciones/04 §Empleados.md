---
id: "doc-04-empleados"
tipo: "seccion"
title: "Empleados ✅"
aliases: ["doc-04-empleados"]
documento: "[[04 Progresión y meta]]"
limpieza: 100
abiertos: 0
espera: 12
aplazado_a: ["[[F4-244 Bolsa de la Unión]]", "[[F4-245 Mejora de la tienda y desbloqueo de «Contratar»]]", "[[F4-90 Contratos por tiempo - duración, salario y vencimiento]]", "[[F4-93 Avisos agrupados de contratos por vencer]]", "[[F4-94 Sección de empleos del periódico]]", "[[F4-95 Anuncios propios en periódicos]]", "[[F4-96 Sesgo político de los candidatos según el medio]]", "[[F4-97 Información oculta de candidatos y referencias]]", "[[F4-99 Minero automático - expediciones sin minijuego]]"]
estado: "con-aplazados"
anterior: "[[04 §Stats del jugador]]"
siguiente: "[[04 §Estilo de vida y estatus]]"
arriba: "[[04 Progresión y meta]]"
fuente: "studio/docs/04-progresion-y-meta.md:33"
generado: true
---

# Empleados ✅

> Estado: confirmado que aparecen a mitad del juego, cuándo se abre «Contratar», para qué sirven, los roles, las stats de empleado, los…

← [[04 §Stats del jugador]] · [[04 Progresión y meta|↑ 04]] · [[04 §Estilo de vida y estatus]] →

**Estado:** confirmado que aparecen a mitad del juego, cuándo se abre «Contratar», para qué sirven, los roles, las stats de empleado, los contratos por tiempo, los canales de contratación y cómo leen a la Unión; los detalles de contrato ⏳ [[F4-90 Contratos por tiempo - duración, salario y vencimiento|F4-90]] y ⏳ [[F4-93 Avisos agrupados de contratos por vencer|F4-93]]. Las reglas de equilibrio (más abajo) están confirmadas por el autor (2026-10-15); las cifras base están acordadas ✅ ([[28 Números base de la economía|28]]) y el comportamiento del Minero automático ⏳ [[F4-99 Minero automático - expediciones sin minijuego|F4-99]].

✅ Aparecen **a mitad del juego**, no hace falta un imperio para tener trabajadores. Pueden **minar** y **atender la tienda**. Tienen stats de eficiencia y se pueden mejorar (inspiración: Dave the Diver).

### Cuándo se puede contratar ✅

Decisión del autor (2026-10-15):

- ✅ El botón **«Contratar»** se abre **al cerrar el Acto I** y **también exige una mejora de la tienda**. La mejora **se compra en la propia tienda, desde el Acto II, con dinero** (la tienda sigue sin abrirse de noche, [[01 Core loop y ciclo del día|01]]). Es el **Puesto ampliado** y cuesta **3 500 esquirlas** ✅ ([[03 Comercio y mercado|03]], [[28 Números base de la economía|28]]); ⏳ [[F4-245 Mejora de la tienda y desbloqueo de «Contratar»|F4-245]] lo construye.
- ✅ En el Acto I el botón está **bloqueado** y su motivo es esa mejora de la tienda pendiente (el Acto I no la ofrece). El Acto I solo ofrece el primer contacto: la ficha de un candidato ([[27 Guion del Acto I, día a día|27]], sección 15).
- ✅ Se empieza con **Minero** y **Dependiente**. El **Analista** llega en el Acto III.
- ✅ Los empleados **nunca extraen Aetherita**: la extrae solo el jugador, y se vende por la Comisión del Éter, un canal legal con tope, o por encargos especiales raros del mercado negro ([[03 Comercio y mercado|03]], [[28 Números base de la economía|28]]).

### Para qué sirven ✅

El día tiene solo 3 bloques para el jugador ([[01 Core loop y ciclo del día|01]]). Los empleados son la forma de **crecer por encima de ese límite**: el jugador usa sus bloques en lo valioso y delega lo rutinario.

### Roles iniciales ✅

| Rol | Hace | Libera |
|---|---|---|
| **Minero** | Va solo a una zona ya desbloqueada y trae menas | Un bloque de expedición |
| **Dependiente** | Atiende clientes y repone estantes | Un bloque de tienda |
| **Guardia** | Reduce el riesgo de saqueos | Seguridad |
| **Refinador** | Funde y refina | Tiempo en el taller |
| **Analista** | Aporta información de mercado (capa 3) | Lectura del mercado |

Los cinco roles están en el glosario ([[18 Biblia narrativa|18]], 6.8).

### Stats de empleado ✅

| Stat | Efecto |
|---|---|
| **Eficiencia** | Rendimiento y velocidad |
| **Cuidado** | Menos daño a menas y menos desgaste de herramientas |
| **Lealtad** | Probabilidad de robar, renunciar, sobornarse o sumarse a una huelga. Es un dato oculto |

Suben por uso y con entrenamiento (coherente con las stats del jugador).

### Consecuencias de los malos stats ✅

Un empleado productivo es una ventaja, pero con malos stats es **contraproducente**: puede robar, dejarse sobornar, dañar menas o gastar herramientas. El empleado es una decisión de riesgo, no solo un bono.

### Los empleados y la Unión ✅

Decisión del autor (2026-10-15): los empleados solo **leen el tramo de la Unión** (bajo, medio o alto, [[24 Umbrales de acto|24]]) y eso **modula su Lealtad**. **Contratar, despedir o publicar una oferta no mueve el medidor de la Unión** ni ningún otro: los medidores solo se mueven por las decisiones de la historia.

### Contratos ✅

Ningún empleado dura para siempre. Cada uno trabaja con un **contrato por tiempo**:

- El jugador lo crea (duración y salario).
- Puede **despedirlo** antes de tiempo.
- Al terminar el contrato, el empleado **se va o renueva**.

Detalles:

| Elemento | Regla |
|---|---|
| Duración | ✅ Corta (**7 días**), media (**14**) o larga (**30**); son 1,5 h, 3 h y 6,5 h de juego con el día de 13 minutos. Su vencimiento ⏳ [[F4-90 Contratos por tiempo - duración, salario y vencimiento\|F4-90]] |
| Contrato corto | Flexible, pero salario más alto (**×1,30** el de 7 días, **×1,12** el de 14, ×1,00 el de 30 ✅) y renegociación frecuente ⏳ [[F4-90 Contratos por tiempo - duración, salario y vencimiento\|F4-90]] |
| Contrato largo | Salario más bajo y estabilidad, pero despedir cuesta más ⏳ [[F4-90 Contratos por tiempo - duración, salario y vencimiento\|F4-90]] |
| Despido anticipado | Cuesta una indemnización de `salario × días que faltan × φ`, con φ = **0,25** (7 días), **0,40** (14) o **0,60** (30) ✅. Despedir el primer día de un contrato de 30 días cuesta ≈ 17 días de salario. Despedir no mueve el medidor de la Unión, con o sin causa |
| Renovación | Depende de Lealtad, salario, trato y del tramo de la Unión. Se negocia con **Labia** |
| Se va | Puede irse a la competencia (por ejemplo, al Consorcio Arvel) |
| Avisos | Aviso en pantalla unos días antes de que venza, agrupados en el resumen del día para no saturar al jugador (en PC no hay notificaciones del sistema) |

- ✅ **Salarios** (por día, en un contrato de 30 días; los de 7 y 14 días llevan el modificador de arriba): Minero **N1 70 · N2 90 · N3 200 · N4 600 · N5 720 esquirlas**; Dependiente 160 en el Acto II, 620 en el III y 2 800 en el IV; el Refinador cobra igual que el Dependiente, el Guardia el 60 % y el Analista el 140 % (900 en el III y 3 900 en el IV). Cuánto dura cada contrato frente a los minutos por día está en [[01 Core loop y ciclo del día|01]] y [[17 Mapa de historia|17]] ([[28 Números base de la economía|28]]).
- ✅ **Entrenamiento:** subir un nivel cuesta **8 veces el salario diario del nivel siguiente** y 3 días de baja; además el empleado sube 1 nivel por cada 40 días trabajados sin entrenar.

Esto crea una tensión interesante: **entrenar a un empleado es una inversión que puede irse con él**. Se mitiga con contratos largos, bonos de permanencia y buen trato.

### Contratación ✅

Como en Dave the Diver, hay que invertir para contratar. Canales:

| Canal | Cómo funciona |
|---|---|
| **Sección de empleos del periódico** | Se ve gente que busca trabajo; cambia cada día |
| **Anuncio propio** | El jugador paga por publicar (rol, salario ofrecido); llegan candidatos en unos días |
| **Bolsa de la Unión** | Candidatos más fiables y más caros, con condiciones. Está en la sede de la Unión, en la V1 ([[26 Zonas y edificios\|26]]); su construcción es ⏳ [[F4-244 Bolsa de la Unión\|F4-244]] |
| **Recomendaciones** | Vía conexiones. Es **evolutivo**: llega más adelante, sin versión fija ([[26 Zonas y edificios\|26]]) |

✅ Estos cuatro canales están decididos. La tarifa de contratar es de **3 días de salario** por la sección de empleos del periódico, **6 días** por un anuncio propio (llegan 1–3 candidatos en 2–4 días) y **10 días** más un 15 % de salario por la Bolsa de la Unión ✅. ⏳ [[F4-94 Sección de empleos del periódico|F4-94]] La sección de empleos y ⏳ [[F4-95 Anuncios propios en periódicos|F4-95]] los anuncios propios se construyen con sus tareas.

### El periódico importa ✅

Según el periódico, el anuncio o el candidato puede estar **inclinado políticamente** ([[07 Sociedad, poder y eventos|07]]). Dónde publicas **no mueve ningún medidor**: solo cambia el perfil de los candidatos.

| Medio | Perfil de candidatos |
|---|---|
| El Heraldo Meridiano (oficialista) | Ordenados, afines al Ministerio; menos probables de sumarse a huelgas |
| La Voz del Hollín (sindical) | Más lealtad a la Unión y más combativos; pueden sumarse a huelgas |
| Teletipo Meridiano (rápido, sin confirmar) | Más variedad y más incertidumbre: el perfil puede no ser exacto |

⏳ [[F4-96 Sesgo político de los candidatos según el medio|F4-96]] El perfil exacto de candidatos por medio.

### Información sobre candidatos ✅

Se aplica el pilar «la información es poder»: del candidato se ven al inicio solo estimaciones. La **Lealtad** y otros datos están ocultos. Contratar a ciegas es una apuesta. ⏳ [[F4-97 Información oculta de candidatos y referencias|F4-97]] Cómo se descubren (referencias, entrevistas o tu **Ojo/Labia**).

### Reglas de equilibrio ✅

- ✅ Un Minero empleado rinde **menos que el jugador** en promedio y no juega el minijuego: su Eficiencia va del **30 % (N1) al 50 % (N5)** de lo que sacaría el jugador, y escala igual con sus skills. Un Minero N1 aporta cerca del 6 % de un día del jugador en el Acto II, y su salario es ≈ 59 % de lo que aporta (en el Acto II el par previsto de la regla G1, de 40–60 %, es el N2, con ≈ 50 %; el N1 solo debe quedar por debajo del 100 %, [[28 Números base de la economía|28]]). El **entrenamiento** lo sube de nivel (arriba).
- ✅ Los minerales de **nivel alto** solo los extraen empleados **muy entrenados** y con la **herramienta adecuada**; los **básicos** los extrae cualquiera. La **Aetherita**, nunca (ni siquiera con el canal legal del Acto IV: solo la extrae el jugador). «Nivel alto» son los **niveles N4 y N5** (pueden extraer minerales de nivel 4: las gemas); N1 y N2 llegan al nivel 2, y N3 al 3. Cuánto entrenamiento exigen está en el costo de subir de nivel (arriba).
- ✅ Cuestan salario diario y contratación (arriba); cantidad limitada por espacio: la plantilla máxima sube con el nivel de la tienda (0 · 2 · 3 · 5 · 7 empleados, y de ellos 0 · 1 · 2 · 3 · 4 Mineros). En el **Acto IV** su papel es residual: no se toca la economía del IV. ✅ Si el jugador envía a un Minero a una zona agotada, **el juego le avisa con la pérdida estimada antes de enviarlo, pero lo deja decidir** (decisión del autor, 2026-10-16; [[28 Números base de la economía|28]]).
- ✅ En **zonas peligrosas** un Minero puede **herirse** (queda inactivo unos días) o **perder la carga** de esa expedición. La probabilidad de herida por expedición va del 1,5 % en las Galerías al 12 % en La Fosa (3 % en el Cañón, 4 % en la Sierra y los Salares, 7 % en las Cavernas), con 3 a 8 días de baja, y la de perder la carga es 1,5 veces esa cifra ✅ ([[28 Números base de la economía|28]]).
- ✅ Los empleados conectan con la sociedad: la **Lealtad** se ve afectada por el tramo de la Unión ✅, por la alianza que elijas y por las huelgas.

⚠️ Riesgo: que la automatización haga irrelevante al jugador. Por eso el diseño busca que delegar sea rentable pero que lo mejor siga requiriendo al jugador.

## Fuente

`studio/docs/04-progresion-y-meta.md:33`
