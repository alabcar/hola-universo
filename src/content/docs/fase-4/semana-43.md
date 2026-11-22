---
title: "Semana 43 · ¿De qué está hecho el universo?"
description: "Fase 4 · El universo grande. Exponenciales: discos de galaxias y expansión acelerada; las curvas de rotación de Vera Rubin, la materia oscura de Zwicky, las lentes y el cúmulo Bala, la energía oscura y la expansión acelerada, la composición del universo y galaxias espirales para observar."
sidebar:
  order: 43
  label: "43. ¿De qué está hecho el universo?"
---

## La pregunta del cielo

Todo lo que has estudiado hasta ahora, las estrellas, los planetas, el gas, el polvo, tú mismo, está hecho de átomos: protones, neutrones y electrones. Parece natural pensar que el universo está hecho de eso. Pero las cuentas no salen.

Las galaxias giran demasiado deprisa para la masa que se ve en ellas. Los cúmulos de galaxias se mantienen unidos con una masa que no está en ninguna parte. La luz de las galaxias lejanas se curva como si hubiera más masa de la que brilla. Y el universo, en lugar de frenar su expansión por la gravedad, la está acelerando. Según las medidas actuales, los átomos son solo un 5 % del contenido del universo. El 95 % restante tiene dos nombres, **materia oscura** y **energía oscura**, que en realidad son dos maneras de decir que no sabemos qué es. Esta semana ves las pruebas, y por qué los astrónomos se las toman en serio.

:::note[De dónde viene la palabra]
**Materia** viene del latín *materia*, «madera de construcción», de *mater*, «madre»: la sustancia de la que se hacen las cosas. **Oscura**, en «materia oscura», no significa negra, sino que no emite ni absorbe luz: es invisible a todas las longitudes de onda. La expresión la usó por primera vez Fritz Zwicky en 1933, en alemán: *dunkle Materie*.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: las galaxias espirales son exponenciales (35-45 min)

**Un repaso.** En la semana 26 viste la función exponencial: $e^{-x}$ decrece de forma que cada vez que $x$ aumenta en una cantidad fija, el valor se divide por el mismo factor. Y viste que, tomando logaritmos, una exponencial se convierte en una recta: si $y = A\,e^{-x/h}$, entonces $\ln y = \ln A - x/h$.

**El disco de una espiral.** En 1970, el astrónomo australiano Ken Freeman observó que el brillo de los discos de las galaxias espirales disminuye hacia fuera de forma exponencial:

$$I(r) = I_0\,e^{-r/h},$$

donde $I_0$ es el brillo en el centro y $h$, la **escala de longitud** del disco: la distancia a la que el brillo se divide por $e \approx 2{,}718$. En la Vía Láctea, $h$ es de unos 2,5 a 3 kpc. A cuatro escalas de longitud del centro, el brillo es ya menos del 2 % del central: el disco visible parece acabarse, aunque, como verás, la galaxia no se acaba ahí.

**Medir $h$ con una recta.** Si mides el brillo a varias distancias del centro y dibujas $\ln I$ frente a $r$, sale una recta de pendiente $-1/h$. Ajustándola (semana 40), obtienes $h$. El cuaderno lo hace.

**La masa del disco.** Si la masa sigue a la luz, la masa del disco también cae de forma exponencial, y la masa total es finita: sumando anillos (integrando, semana 11), la masa de un disco exponencial infinito es $M = 2\pi\,\Sigma_0\,h^2$, donde $\Sigma_0$ es la densidad superficial en el centro. Y la mayor parte de esa masa está dentro de unas pocas escalas de longitud.

**Ejercicios**

1. En un disco con $h = 3$ kpc, ¿a qué fracción del brillo central baja a 6 kpc? ¿Y a 12 kpc?
2. Mides $I(2\ \text{kpc}) = 50$ y $I(8\ \text{kpc}) = 5$ (en unidades arbitrarias). ¿Cuánto vale $h$?
3. Para un disco exponencial, la fracción de la masa dentro de un radio $r$ es $1 - (1 + r/h)\,e^{-r/h}$. ¿Qué fracción hay dentro de $4h$?

<details>
<summary>Soluciones</summary>

1. $e^{-2} \approx$ **13,5 %**; $e^{-4} \approx$ **1,8 %**.
2. $\ln(50/5) = \ln 10 = (8 - 2)/h$, así que $h = 6/2{,}303 \approx$ **2,6 kpc**.
3. $1 - 5\,e^{-4} = 1 - 5 \cdot 0{,}0183 \approx$ **91 %**.

</details>

### Sesión 2 · Matemáticas: crecimiento exponencial y expansión acelerada (35-40 min)

**Crecer en proporción a lo que hay.** Una cantidad que crece a un ritmo proporcional a sí misma, $\frac{dy}{dt} = k\,y$, crece de forma exponencial: $y(t) = y_0\,e^{kt}$. Es la ecuación del interés compuesto, de una población de bacterias con comida ilimitada y, como verás, del universo dominado por la energía oscura. Su característica es el **tiempo de duplicación**: el tiempo que tarda en duplicarse, que es siempre el mismo,

$$t_2 = \frac{\ln 2}{k} \approx \frac{0{,}693}{k}.$$

**Un universo que se acelera.** La constante de Hubble es el ritmo relativo de crecimiento del universo: $H = \dot{a}/a$ (semana 41). Si $H$ fuera constante, sería la ecuación anterior con $k = H$, y el factor de escala crecería de forma exponencial: $a(t) \propto e^{Ht}$. Hasta hace unos miles de millones de años no era así: la gravedad de la materia frenaba la expansión. Pero la materia se diluye al expandirse el universo, y la energía oscura, según todo lo que se sabe, no (o casi no). Por eso, desde hace unos 5000 millones de años, domina la energía oscura y la expansión se acelera. En el futuro lejano, el universo crecerá de forma casi exponencial, duplicando su tamaño cada unos 12 000 millones de años.

**Ejercicios**

1. Una cantidad crece un 7 % al año. ¿Cuánto tarda en duplicarse? (Regla práctica: 70 dividido por el porcentaje.)
2. Si $H$ fuera constante e igual a 56 km/s/Mpc (el valor al que tiende con la energía oscura), ¿cuánto vale $1/H$ en años? ¿Y el tiempo de duplicación?
3. ¿Cuántas veces habrá crecido el universo, en ese régimen, al cabo de 100 000 millones de años?

<details>
<summary>Soluciones</summary>

1. $\ln 2/\ln(1{,}07) \approx$ **10,2 años** (la regla da 10).
2. $1/H = 3{,}086\times10^{19}/56 \approx 5{,}5\times10^{17}$ s $\approx$ **17 500 millones de años**; $t_2 = 0{,}693 \cdot 17\,500 \approx$ **12 100 millones de años**.
3. $100/12{,}1 \approx 8{,}3$ duplicaciones: $2^{8{,}3} \approx$ **300 veces**.

</details>

### Sesión 3 · Física: lo que no se ve (40-45 min)

**Zwicky y el cúmulo de Coma (1933).** El astrónomo suizo Fritz Zwicky midió las velocidades de las galaxias del cúmulo de Coma, un enjambre de más de mil galaxias. Se movían tan deprisa (unos 1000 km/s) que la gravedad de las galaxias visibles no podía mantenerlas juntas: el cúmulo debería haberse disgregado hace mucho. Calculó que hacía falta cientos de veces más masa de la que brillaba. Casi nadie le hizo caso durante cuarenta años.

**Vera Rubin y las curvas de rotación (década de 1970).** La astrónoma estadounidense Vera Rubin y su colaborador Kent Ford midieron, con el efecto Doppler (semana 41), la velocidad de giro de las estrellas y el gas en Andrómeda y en muchas otras galaxias espirales, a distintas distancias del centro. Si casi toda la masa estuviera donde está la luz, en el disco exponencial, más allá de unas pocas escalas de longitud la velocidad debería bajar como en el Sistema Solar, $v \propto 1/\sqrt{r}$ (semana 17). No bajaba: se mantenía **plana** hasta donde se podía medir, y con el gas de hidrógeno, en radio a 21 cm (semana 30), se pudo medir mucho más lejos que las estrellas. Con $M(<r) = v^2 r/G$ (semana 38), una velocidad constante significa una masa que crece en proporción a la distancia, mucho más allá de donde acaba la luz. Cada galaxia está envuelta en un **halo de materia oscura** varias veces más masivo que todas sus estrellas.

**Más pruebas, independientes entre sí.**

- **Las lentes gravitacionales** (semana 45): la masa curva la luz. La forma en que los cúmulos de galaxias deforman las imágenes de las galaxias del fondo permite pesarlos, y salen mucho más masivos de lo que se ve.
- **El cúmulo Bala**: en 2006 se publicó el estudio de dos cúmulos de galaxias que chocaron hace unos 150 millones de años. El gas caliente de los dos (que es la mayor parte de su materia normal, visible en rayos X) se frenó en el choque y quedó en el centro; pero la masa medida con lentes gravitacionales está en otro sitio, con las galaxias, que se atravesaron sin chocar. La mayor parte de la masa no es el gas: es algo que atraviesa sin rozarse, como la materia oscura.
- **El fondo cósmico** (semana 42): el tamaño y la altura de los picos de su espectro de potencias dependen de cuánta materia normal y cuánta oscura había. Sale unas cinco veces más oscura que normal.

**¿Qué es la materia oscura?** No se sabe. No puede ser materia normal escondida (estrellas muy débiles, planetas sueltos, gas frío): la nucleosíntesis primordial (semana 42) limita cuánta materia normal puede haber, y no alcanza. Lo más aceptado es que se trata de alguna partícula todavía desconocida que solo interactúa por la gravedad (y quizá muy débilmente de otras formas). Decenas de experimentos la buscan, de momento sin éxito. Una alternativa minoritaria propone que no hay materia oscura, sino que la gravedad funciona de otra manera a aceleraciones muy pequeñas (la teoría MOND, propuesta por Mordehai Milgrom en 1983); explica bien las curvas de rotación, pero tiene dificultades con los cúmulos y el fondo cósmico.

**La energía oscura (1998).** Dos equipos internacionales usaron supernovas de tipo Ia (semana 41) como candelas estándar para medir cómo se frenaba la expansión del universo. Encontraron lo contrario: las supernovas lejanas se veían más débiles de lo esperado, es decir, más lejos. La expansión se está **acelerando**. Saul Perlmutter, Brian Schmidt y Adam Riess recibieron por ello el Nobel de Física de 2011. Lo que causa la aceleración se llama **energía oscura**. La explicación más sencilla es la **constante cosmológica** que Einstein había introducido en 1917 y luego retirado: una energía propia del espacio vacío, igual en todas partes y en todo momento. En 2024 y 2025, el cartografiado de galaxias DESI encontró indicios, todavía no concluyentes, de que la energía oscura podría estar debilitándose con el tiempo. La misión Euclid de la ESA, lanzada en 2023, está haciendo un mapa de miles de millones de galaxias para estudiar las dos cosas oscuras.

**La receta del universo.** Según los resultados finales de Planck (2018), combinados con otras medidas:

| Componente | Fracción |
|---|---|
| Materia normal (átomos) | ~5 % |
| Materia oscura | ~27 % |
| Energía oscura | ~68 % |

De la materia normal, solo una pequeña parte está en estrellas; la mayor parte es gas difuso entre las galaxias.

:::note[De dónde viene la palabra]
**Cúmulo Bala** es la traducción del nombre inglés *Bullet Cluster*, por la forma de bala del gas de uno de los cúmulos al atravesar al otro. **Constante cosmológica**: la letra con la que se escribe, $\Lambda$ (lambda mayúscula), da nombre al modelo cosmológico estándar, «Lambda-CDM»: constante cosmológica más materia oscura fría (*cold dark matter*).
:::

**Qué hacer**

1. Una estrella gira a 220 km/s a 8 kpc del centro de una galaxia y otra a 220 km/s a 20 kpc. ¿Cuánta masa hay dentro de cada órbita? ¿Cuánta entre las dos?
2. Si la materia oscura es un 27 % y la normal un 5 %, ¿cuántas veces más materia oscura que normal hay?
3. Explica por qué el cúmulo Bala es una prueba más difícil de explicar sin materia oscura que una curva de rotación.

### Sesión 4 · Astronomía y observación: galaxias espirales (30-45 min)

**Andrómeda (M31)**, otra vez, pero con otros ojos. Fue una de las galaxias cuya rotación midieron Rubin y Ford en 1970. El óvalo que ves con los prismáticos es su disco, inclinado unos 77° respecto a nosotros, y la mancha brillante del centro, su bulbo. Fíjate en cómo el brillo disminuye desde el centro hacia fuera de forma gradual: es el perfil exponencial de la sesión 1. Y piensa que la galaxia entera, con su billón de estrellas, aproximadamente, está dentro de un halo de materia oscura mucho más grande y más masivo que lo que ves.

**El Triángulo (M33)**, la otra espiral del Grupo Local, tiene una de las curvas de rotación planas más claras que se conocen. Desde un cielo oscuro, búscala con los prismáticos al otro lado de Mirach (semana 40).

**NGC 253** en el Escultor (semana 41), vista casi de canto: con unos prismáticos se ve un huso alargado. En las fotografías aparecen bandas de polvo a lo largo del disco.

**Tú también estás en un halo.** La Vía Láctea tiene su propio halo de materia oscura. Si la materia oscura es una partícula, en este momento atraviesan tu cuerpo, sin tocarlo, muchísimas de ellas, a unos cientos de kilómetros por segundo. No las notas, igual que no notas los neutrinos del Sol (semana 34).

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 43:

- genera el perfil de brillo **simulado** de un disco exponencial con ruido y mide su escala de longitud con una recta en escala logarítmica,
- calcula la curva de rotación que tendría una galaxia solo con su bulbo y su disco visibles,
- la compara con una curva de rotación **simulada** plana, ajusta un halo de materia oscura y calcula cuánta masa hace falta,
- dibuja el crecimiento del factor de escala con y sin energía oscura en un modelo sencillo.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-43.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-43.ipynb)

## Qué has aprendido

- **La respuesta.** Los átomos son solo un 5 % del universo. Un 27 % es materia oscura, que no emite luz pero se nota por su gravedad en la rotación de las galaxias, en los cúmulos, en las lentes gravitacionales y en el fondo cósmico. El 68 % restante es energía oscura, que acelera la expansión. No sabemos qué son ninguna de las dos.
- **Cómo lo sabemos.** Por varias pruebas independientes que apuntan a lo mismo: curvas de rotación planas, cúmulos que no se deshacen, lentes, el cúmulo Bala, el fondo cósmico y las supernovas lejanas.
- **Las herramientas.** La función exponencial y su escala, el ajuste de una exponencial con logaritmos, el crecimiento exponencial y el tiempo de duplicación, y la masa encerrada a partir de la velocidad de rotación.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**Pesar un cúmulo como Zwicky: el teorema del virial.** Para un sistema de muchos cuerpos ligados por la gravedad que lleva mucho tiempo en equilibrio (un cúmulo de galaxias, un cúmulo globular), el **teorema del virial** dice que, de media,

$$2K + U = 0,$$

donde $K$ es la energía cinética total y $U$ la energía potencial gravitatoria total (negativa). Lo usaste en la semana 35 para la masa de Jeans.

Para un cúmulo de masa $M$ y radio $R$, aproximadamente esférico y uniforme, $U \approx -\frac{3}{5}\frac{GM^2}{R}$. Si las galaxias se mueven con una dispersión de velocidades $\sigma$ a lo largo de la visual (lo que se mide con el efecto Doppler), la velocidad cuadrática media en tres dimensiones es $3\sigma^2$ y $K = \frac{1}{2}M\cdot3\sigma^2$. Sustituyendo:

$$3M\sigma^2 = \frac{3}{5}\frac{GM^2}{R} \quad\Longrightarrow\quad M = \frac{5\,\sigma^2 R}{G}.$$

**El problema de la masa que falta.** Comparando esa masa con la luminosidad del cúmulo se obtiene la **relación masa-luminosidad**, $M/L$. Para el Sol vale 1 (en unidades solares); para una población normal de estrellas, unas pocas unidades. Para los cúmulos de galaxias sale de cientos.

**Ejercicios**

1. Calcula la masa del cúmulo de Coma con $\sigma = 1000$ km/s y $R = 2$ Mpc ($6{,}2\times10^{22}$ m). Pásala a masas solares.
2. Si la luminosidad del cúmulo es de unos $5\times10^{12}\,L_\odot$, ¿qué relación masa-luminosidad tiene?
3. Si la masa de las estrellas de un cúmulo fuera unas 3 veces su luminosidad en unidades solares, ¿qué fracción de la masa estaría en estrellas?

<details>
<summary>Soluciones</summary>

1. $M = 5 \cdot (10^6)^2 \cdot 6{,}2\times10^{22}/6{,}67\times10^{-11} \approx 4{,}6\times10^{45}$ kg, unos **2 × 10¹⁵ masas solares**.
2. $M/L \approx 2\times10^{15}/5\times10^{12} =$ **unos 400**.
3. $3/400 \approx$ **menos del 1 %**. El resto es gas caliente (unas pocas veces más que las estrellas) y, sobre todo, materia oscura.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Capítulo 28, La evolución y distribución de las galaxias, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/28%3A_La_evoluci%C3%B3n_y_distribuci%C3%B3n_de_las_galaxias). Español; cúmulos de galaxias, materia oscura y estructura a gran escala. Verificado el 20 de noviembre de 2026.
2. [Capítulo 29, El Big Bang, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/29%3A_El_Big_Bang). Español; la expansión acelerada y la energía oscura. Verificado el 20 de noviembre de 2026.
3. [Capítulo 26, Galaxias, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/26%3A_Galaxias). Español; la masa de las galaxias y su materia oscura. Verificado el 20 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
