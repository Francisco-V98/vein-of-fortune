---
id: "doc-26-s01"
tipo: "seccion"
title: "1 · Estructura: mapa, zona y edificación ✅"
aliases: ["doc-26-s01"]
documento: "[[26 Zonas y edificios]]"
limpieza: 100
abiertos: 0
espera: 5
aplazado_a: ["[[F1-20 Flujo de traducción - extracción, traducción asistida por]]", "[[F4-152 Mapa de Valdoria interactivo - zonas con ratón]]", "[[F4-153 Estado visual del mapa - zonas bloqueadas y desbloqueadas]]", "[[F4-154 Viaje entre regiones - costo en dinero y zonas profundas]]", "[[F4-167 Navegación entre mapa, ciudad y edificios]]"]
estado: "con-aplazados"
siguiente: "[[26 §2 Catálogo de edificaciones por zona]]"
arriba: "[[26 Zonas y edificios]]"
fuente: "studio/docs/26-zonas-y-edificios.md:9"
generado: true
---

# 1 · Estructura: mapa, zona y edificación ✅

> 1. Mapa de Valdoria. Imagen ilustrada con las seis regiones tocables; las bloqueadas se ven apagadas (12, F4-152 y F4-153).

[[26 Zonas y edificios|↑ 26]] · [[26 §2 Catálogo de edificaciones por zona]] →

### 1.1 Los tres niveles ✅

1. **Mapa de Valdoria.** Imagen ilustrada con las seis regiones tocables; las bloqueadas se ven apagadas ([[12 Dirección de arte|12]], ⏳ [[F4-152 Mapa de Valdoria interactivo - zonas con ratón|F4-152]] y ⏳ [[F4-153 Estado visual del mapa - zonas bloqueadas y desbloqueadas|F4-153]]).
2. **Zona.** La región es la zona. Al hacer clic en ella (o elegirla con el mando) entras a la **vista de zona**: el asentamiento en isométrica, con sus edificaciones seleccionables ([[12 Dirección de arte|12]], perspectiva).
3. **Edificación.** Eliges a cuál entrar y ves **esa edificación por separado**, en vista interior en corte transversal, como la tienda. La boca de mina es una edificación más: al entrar a ella pasas a la vista lateral de la mina.

La navegación entre los tres niveles es ⏳ [[F4-167 Navegación entre mapa, ciudad y edificios|F4-167]].

### 1.2 Zona, asentamiento y zona de minado ✅

- **Zona** (del mapa) es la región con su asentamiento. **Zona de minado** son las seis de [[02 Extracción|02]]; cada una se entra por su **boca de mina**, dentro de un asentamiento.
- Cada zona tiene **un asentamiento**. **Villa Brasa atiende las dos zonas de minado del Hollín** (Galerías del Hollín y Cañón Ferroso): desde su vista de zona eliges una de las dos bocas. **Puerto Meridiano** es la zona de la capital y no tiene boca de mina.
- El asentamiento es donde se comercia, se contrata y se vive; la boca de mina es donde se extrae. Moverte entre zonas no gasta bloques pero cuesta un poco de dinero (billete o combustible), y ver las zonas en el mapa es gratis ✅ ([[01 Core loop y ciclo del día|01]]; decisión del autor, 2026-10-15). El trayecto cuesta entre 42 y 210 esquirlas, 0 entre las dos bocas de Villa Brasa y nada en el Acto I, porque todo ocurre en Villa Brasa ✅ ([[28 Números base de la economía|28]]). Las Cavernas y La Fosa son zonas profundas: 2 bloques, Tarde y Noche, y La Fosa solo abre 3 días por semana ✅: los días 2, 4 y 6 de cada semana, y el 7 queda libre para la cuota. Cómo se ve el viaje ⏳ [[F4-154 Viaje entre regiones - costo en dinero y zonas profundas|F4-154]].

| Zona (región) | Asentamiento | Bocas de mina | Se abre en el acto |
|---|---|---|---|
| Cuenca del Hollín | **Villa Brasa** | Galerías del Hollín; Cañón Ferroso (desde el II) | I |
| Sierra Alta | **Altafría** | Minas de Sierra Alta | II |
| Salares del Litoral | **Salinas Blancas** | Salares del Litoral | II |
| Cavernas de Cristal | campamento (ver 1.3) | Cavernas de Cristal | III |
| La Fosa | campamento de la Comisión (ver 1.3) | La Fosa del Éter | IV |
| Puerto Meridiano | la propia ciudad | ninguna | III |

Los nombres **Altafría** y **Salinas Blancas**, en español, los decidió el autor ✅; Altafría es el pueblo de empresa del Consorcio en Sierra Alta y Salinas Blancas es el puerto de los Salares, de los Faroleros y del contrabando ✅. En inglés, *Highchill* y *White Salt Flats* ([[18 Biblia narrativa|18]], 6.5) ⏳ [[F1-20 Flujo de traducción - extracción, traducción asistida por|F1-20]]. Los actos de la columna anterior ✅ siguen los de las zonas de minado, que no cambian ([[17 Mapa de historia|17]]): cada asentamiento abre con su zona.

### 1.3 Dos reglas dentro de la estructura ✅

- ✅ **Campamentos con nombre descriptivo.** Las Cavernas y la Fosa no tienen vivienda y su asentamiento es un campamento. Los nombres «el campamento de las Cavernas» y «el campamento de la Comisión» son definitivos (decisión del autor, 2026-10-16).
- ✅ **Horarios por bloque.** Cada edificación declara en qué bloques del día abre (mañana, tarde, noche); el bar de Los Faroleros y el Salón del Farol, solo de noche, como el mercado negro ([[03 Comercio y mercado|03]]). La tienda del jugador, en cambio, abre solo de mañana y de tarde: **nunca de noche** ✅ ([[01 Core loop y ciclo del día|01]]).

---

## Fuente

`studio/docs/26-zonas-y-edificios.md:9`
