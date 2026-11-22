---
title: "Semana 40 · ¿Hay más galaxias aparte de la nuestra?"
description: "Fase 4 · El universo grande. Rectas y regresión lineal por mínimos cuadrados, el coeficiente de correlación, la ley de Leavitt, el Gran Debate de 1920, Hubble y la distancia a Andrómeda, los tipos de galaxias, el Grupo Local y cómo encontrar Andrómeda a simple vista y con prismáticos."
sidebar:
  order: 40
  label: "40. ¿Hay más galaxias aparte de la nuestra?"
---

## La pregunta del cielo

En una noche oscura de otoño, entre Casiopea y el cuadrado de Pegaso, se ve a simple vista una manchita alargada y tenue. El astrónomo persa al-Sufi la describió hacia el año 964 como una «pequeña nube». Es la galaxia de Andrómeda, y la luz que ves salió de ella hace unos dos millones y medio de años, cuando en África empezaban a aparecer los primeros humanos del género *Homo*. Es lo más lejano que puedes ver a simple vista sin ayuda de nada.

Hace solo cien años, nadie sabía qué era. Muchos astrónomos pensaban que las «nebulosas espirales» eran nubes de gas dentro de nuestra galaxia, y que la Vía Láctea era todo el universo. Otros creían que eran galaxias como la nuestra, «universos isla», una idea que había propuesto el filósofo Immanuel Kant en 1755. La pregunta se resolvió en 1925 con una recta: la de la relación entre el periodo y la luminosidad de las cefeidas. Esta semana aprendes a ajustar rectas como es debido y descubres que vives en una galaxia entre cientos de miles de millones.

:::note[De dónde viene la palabra]
**Andrómeda** era, en el mito griego, la princesa encadenada a una roca como ofrenda a un monstruo marino y salvada por Perseo; su madre era Casiopea y su padre, Cefeo (semana 37), y todos están juntos en esta zona del cielo. El nombre se interpreta como «la que piensa como un hombre» o «la que gobierna a los hombres», del griego *anḗr, andrós*, «hombre», y *médomai*, «pensar, gobernar». **Regresión** viene de *regressus*, «vuelta atrás»: el estadístico Francis Galton la usó en 1886 al ver que los hijos de padres muy altos tienden a ser altos, pero menos que sus padres, «regresan» hacia la media. El nombre se quedó para todo ajuste de una recta a unos datos.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: la recta que mejor se ajusta (40-45 min)

**Una recta.** En la semana 4 viste la función lineal $y = a + b\,x$: $b$ es la **pendiente** (cuánto sube $y$ por cada unidad de $x$) y $a$ la **ordenada en el origen** (el valor de $y$ cuando $x = 0$). En la semana 32 ajustaste una recta con el ordenador. Esta semana ves cómo se calcula.

**Los residuos.** Tienes $N$ puntos $(x_i, y_i)$. Para una recta cualquiera, el **residuo** de cada punto es lo que se aparta de ella en vertical: $e_i = y_i - (a + b\,x_i)$. El método de los **mínimos cuadrados** elige la recta que hace mínima la suma de los cuadrados de los residuos,

$$S(a, b) = \sum_{i=1}^{N}\left(y_i - a - b\,x_i\right)^2.$$

**Las fórmulas.** El mínimo se encuentra derivando (lo haces en el apartado opcional), y la solución es sorprendentemente sencilla. Con las medias $\bar{x}$ e $\bar{y}$:

$$b = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}, \qquad a = \bar{y} - b\,\bar{x}.$$

La segunda dice que la recta pasa siempre por el punto medio $(\bar{x}, \bar{y})$. La primera compara cómo varían juntas $x$ e $y$ (el numerador) con cuánto varía $x$ sola (el denominador).

**Cómo de buena es la recta: el coeficiente de correlación.** El **coeficiente de correlación** de Pearson,

$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2\,\sum (y_i - \bar{y})^2}},$$

va de −1 a 1. Vale 1 si los puntos están exactamente en una recta que sube, −1 si en una que baja, y 0 si no hay relación lineal. Su cuadrado, $r^2$, es la fracción de la variación de $y$ que explica la recta. Una advertencia clásica: una correlación alta no prueba que $x$ cause $y$; solo que van juntas.

**Ejercicios**

Con los puntos $(1, 2)$, $(2, 3)$, $(3, 5)$, $(4, 6)$:

1. Calcula $\bar{x}$, $\bar{y}$, $b$ y $a$.
2. Calcula los residuos y comprueba que suman cero (siempre ocurre con mínimos cuadrados).
3. Calcula $r$.

<details>
<summary>Soluciones</summary>

1. $\bar{x} = 2{,}5$, $\bar{y} = 4$. Desviaciones de $x$: $-1{,}5; -0{,}5; 0{,}5; 1{,}5$; de $y$: $-2; -1; 1; 2$. Numerador: $3 + 0{,}5 + 0{,}5 + 3 = 7$. Denominador: $2{,}25 + 0{,}25 + 0{,}25 + 2{,}25 = 5$. **$b = 1{,}4$**, **$a = 4 - 1{,}4 \cdot 2{,}5 = 0{,}5$**.
2. Recta: $1{,}9; 3{,}3; 4{,}7; 6{,}1$. Residuos: $0{,}1; -0{,}3; 0{,}3; -0{,}1$. Suman **0**.
3. $\sum(y_i - \bar{y})^2 = 4 + 1 + 1 + 4 = 10$. $r = 7/\sqrt{5 \cdot 10} \approx$ **0,99**.

</details>

### Sesión 2 · Matemáticas: la ley de Leavitt como recta (35-40 min)

**Linealizar otra vez.** Leavitt vio que el brillo de las cefeidas crecía con el periodo, pero no en línea recta. Al dibujar la magnitud frente al **logaritmo** del periodo, los puntos se alineaban. Hoy, con distancias calibradas por paralaje (con el telescopio espacial Hubble y con Gaia), la relación en luz visible es aproximadamente

$$M_V \approx -2{,}43\,(\log_{10} P - 1) - 4{,}05,$$

con $P$ en días. (Es la calibración publicada en 2007 por Fritz Benedict y colaboradores con paralajes del telescopio Hubble; hay otras, en otros filtros, más precisas.) Una cefeida de 10 días tiene $M_V \approx -4{,}05$, unas 3500 veces la luminosidad del Sol en el visible; una de 30 días, más de una magnitud más brillante.

**Del periodo a la distancia.** El método es:

1. Mides el periodo $P$ de la cefeida observando su curva de luz durante semanas (no depende de la distancia).
2. Con la recta, calculas su magnitud absoluta $M$.
3. Mides su magnitud aparente media $m$.
4. El módulo de distancia $m - M$ te da la distancia (semana 33), corrigiendo la extinción del polvo si hace falta.

**La dispersión y el error.** Las cefeidas reales no caen exactamente en la recta: tienen una dispersión de unas 0,2 magnitudes en el visible, porque no todas tienen la misma temperatura ni la misma composición. Una sola cefeida da una distancia con un error de un 10 % (por la propagación de la semana 37). Con muchas cefeidas de la misma galaxia, el error de la media baja como $1/\sqrt{N}$: con 25, a un 2 %.

**Ejercicios**

1. ¿Qué magnitud absoluta tiene una cefeida de 30 días según la fórmula?
2. Esa cefeida se ve con $m = 19{,}6$. ¿A qué distancia está? (Ignora el polvo.)
3. Si la dispersión de una cefeida es de 0,2 magnitudes, ¿qué error relativo en la distancia produce? ¿Y con la media de 16 cefeidas?

<details>
<summary>Soluciones</summary>

1. $\log 30 = 1{,}477$; $M = -2{,}43 \cdot 0{,}477 - 4{,}05 \approx$ **−5,21**.
2. $m - M = 24{,}81$; $d = 10^{(24{,}81 + 5)/5} = 10^{5{,}96} \approx$ **920 000 pc**, unos 3 millones de años luz.
3. $10^{0{,}2 \cdot 0{,}2} - 1 \approx$ **9,6 %**; con 16, $0{,}2/\sqrt{16} = 0{,}05$ magnitudes, un **2,3 %**.

</details>

### Sesión 3 · Física: el universo de las galaxias (40-45 min)

**El Gran Debate.** El 26 de abril de 1920, en la Academia Nacional de Ciencias de Washington, Harlow Shapley y Heber Curtis discutieron sobre el tamaño del universo. Shapley, que acababa de medir la galaxia con los cúmulos globulares (semana 38), la creía enorme, y pensaba que las nebulosas espirales eran nubes dentro de ella. Curtis defendía que eran galaxias como la nuestra, muy lejanas. Los dos tenían razón en parte y se equivocaban en parte: Shapley acertaba en el tamaño de la Vía Láctea y la posición del Sol; Curtis, en las espirales.

**Hubble lo resuelve.** En octubre de 1923, Edwin Hubble fotografió Andrómeda con el telescopio de 2,5 m de Monte Wilson, el mayor del mundo entonces, y encontró en ella una estrella variable. Tachó la «N» de nova que había escrito en la placa y escribió «VAR!». Era una cefeida, con un periodo de unos 31 días. Con la ley de Leavitt, calculó una distancia de unos 900 000 años luz: muchas veces mayor que el tamaño de la Vía Láctea según cualquiera. Lo anunció a principios de 1925. Andrómeda era otra galaxia.

(Hubble se quedó corto: hoy sabemos que Andrómeda está a unos 2,5 millones de años luz. En 1952, Walter Baade descubrió que hay dos tipos de cefeidas con relaciones periodo-luminosidad distintas, y que se habían mezclado en la calibración. De golpe, todas las distancias extragalácticas se duplicaron con creces.)

**Tipos de galaxias.** Hubble también las clasificó por su forma, en un esquema que se suele dibujar como un diapasón:

- **Elípticas**: esferas o balones de estrellas viejas, rojizas, con muy poco gas. Van de casi esféricas (E0) a muy alargadas (E7).
- **Espirales**: un disco con brazos y un bulbo, como la Vía Láctea y Andrómeda. Las **espirales barradas** tienen una barra central de la que salen los brazos.
- **Lenticulares**: un disco sin brazos, a medio camino.
- **Irregulares**: sin forma definida, como las Nubes de Magallanes.

**El Grupo Local.** La Vía Láctea, Andrómeda y la galaxia del Triángulo (M33) son las tres espirales de un pequeño grupo de galaxias ligadas por la gravedad, el **Grupo Local**, con unas ochenta galaxias enanas más. Andrómeda se acerca a nosotros a unos 110 km/s. Durante años se dio por hecho que las dos galaxias chocarían dentro de unos 4500 millones de años y se fundirían en una gran elíptica; un estudio de 2025, con datos de Gaia y del Hubble y teniendo en cuenta la atracción de M33 y de la Gran Nube de Magallanes, rebajó a más o menos la mitad la probabilidad de que se fusionen en los próximos 10 000 millones de años. Si chocan, las estrellas apenas lo harán entre sí: están tan separadas que las galaxias se atravesarán como dos enjambres.

**Cuántas hay.** Las imágenes más profundas, como los campos profundos del Hubble y del James Webb, muestran galaxias en cada rincón del cielo, por pequeño que sea. Las estimaciones del número de galaxias en el universo observable van de unos cientos de miles de millones a uno o dos billones, según cuántas galaxias muy débiles y pequeñas se cuenten.

:::note[De dónde viene la palabra]
**Lineal** viene de *linea*, «hilo» (semana 32): una relación lineal es la que se dibuja como un hilo tenso. **Correlación** une el prefijo *co-*, «junto», y *relatio*, «relación»: dos cosas que varían relacionadas. **Elíptica**, de la elipse de la semana 14, que viene del griego *élleipsis*, «falta»: a la elipse le «falta» algo para ser circunferencia.
:::

**Qué hacer**

1. Si Andrómeda se acerca a 110 km/s y está a 2,5 millones de años luz, ¿cuánto tardaría en llegar si fuera en línea recta a velocidad constante? (Con la gravedad, acelera y tarda menos.)
2. Hubble usó una calibración que daba a sus cefeidas una magnitud absoluta 1,5 magnitudes más débil de lo real. ¿En qué factor se equivocó en la distancia?
3. Explica con tus palabras por qué una sola cefeida bastó para resolver el Gran Debate.

### Sesión 4 · Astronomía y observación: Andrómeda (30-45 min)

**Noviembre es el mejor mes.** A primera hora de la noche, Andrómeda está casi en el cénit. Para encontrarla:

1. Busca el **cuadrado de Pegaso**, cuatro estrellas de segunda magnitud que forman un gran cuadrado alto al sur.
2. Desde la esquina noreste del cuadrado, Alpheratz, sigue hacia el noreste una fila de estrellas: δ Andromedae y luego **Mirach** (β And), de segunda magnitud.
3. Desde Mirach, sube hacia el noroeste a μ And (cuarta magnitud) y, a la misma distancia, a ν And (quinta). Justo al lado de ν está **M31**.

**A simple vista**, desde un cielo oscuro, es una mancha alargada del tamaño de la Luna o más. Desde un cielo suburbano, solo con visión lateral, y desde una ciudad, normalmente nada.

**Con los prismáticos** se ve el núcleo brillante y un halo alargado que se extiende más de 2° si el cielo es oscuro (en fotografías de larga exposición ocupa unas seis Lunas llenas). Con mucha paciencia y un cielo muy oscuro, quizá distingas M32, una pequeña mancha redonda al sur del núcleo: una galaxia satélite.

**El Triángulo (M33)**, a la misma distancia del otro lado de Mirach, es un reto: es casi tan grande como M31, pero su luz está muy repartida y su brillo superficial es muy bajo. En un cielo rural oscuro, con prismáticos, se ve como un resplandor redondo y difuso.

**Piénsalo.** Los fotones que entran en tu ojo llevan dos millones y medio de años viajando. Cuando salieron de Andrómeda, no había nadie para recibirlos.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 40:

- programa el ajuste por mínimos cuadrados con las fórmulas de la sesión 1 y lo compara con `np.polyfit`,
- calcula el coeficiente de correlación y analiza los residuos,
- genera un conjunto **simulado** de cefeidas cercanas con distancias de paralaje y la dispersión real de la ley de Leavitt, y ajusta la recta,
- aplica la recta a cefeidas simuladas de una galaxia lejana y calcula su distancia con su incertidumbre,
- muestra el error que se comete al extrapolar la recta fuera del rango de periodos calibrados.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-40.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-40.ipynb)

## Qué has aprendido

- **La respuesta.** Sí: la Vía Láctea es una galaxia entre cientos de miles de millones. La prueba llegó en 1925, cuando Hubble encontró cefeidas en Andrómeda y, con la ley de Leavitt, midió que estaba mucho más lejos que cualquier parte de nuestra galaxia. Hoy sabemos que está a unos 2,5 millones de años luz.
- **El universo de las galaxias.** Hay galaxias elípticas, espirales, lenticulares e irregulares, agrupadas en grupos y cúmulos. La nuestra pertenece al Grupo Local, con Andrómeda y el Triángulo.
- **Las herramientas.** La regresión lineal por mínimos cuadrados, el coeficiente de correlación, el análisis de residuos y la propagación del error de una calibración a una distancia.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**Deducir las fórmulas de los mínimos cuadrados.** $S(a, b)$ es una función de dos variables. En su mínimo, las derivadas parciales respecto a cada una (semana 30) son cero. Derivando con la regla de la cadena (semana 28):

$$\frac{\partial S}{\partial a} = -2\sum (y_i - a - b x_i) = 0, \qquad \frac{\partial S}{\partial b} = -2\sum x_i\,(y_i - a - b x_i) = 0.$$

La primera ecuación dice que **los residuos suman cero**. Dividiendo por $N$: $\bar{y} - a - b\bar{x} = 0$, es decir, $a = \bar{y} - b\bar{x}$. Sustituyendo $a$ en la segunda:

$$\sum x_i\,\big((y_i - \bar{y}) - b\,(x_i - \bar{x})\big) = 0.$$

Como $\sum \bar{x}\,(y_i - \bar{y}) = 0$ y $\sum \bar{x}\,(x_i - \bar{x}) = 0$ (las desviaciones respecto a la media suman cero), puedes cambiar $x_i$ por $(x_i - \bar{x})$ delante sin alterar nada, y despejar:

$$b = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}.$$

Estas dos ecuaciones se llaman **ecuaciones normales**. Que el punto crítico es un mínimo (y no un máximo) se ve porque $S$ es una suma de cuadrados: crece sin límite al alejarte de la mejor recta.

**El error de la pendiente.** Si los residuos tienen una dispersión típica $s$, la pendiente tiene una incertidumbre

$$\sigma_b = \frac{s}{\sqrt{\sum (x_i - \bar{x})^2}}.$$

Dice dos cosas útiles: la pendiente se conoce mejor con más puntos y, sobre todo, con puntos **más repartidos** en $x$. Para calibrar la ley de Leavitt interesa tener cefeidas de periodos muy distintos.

**Ejercicios**

1. Comprueba con los cuatro puntos de la sesión 1 que $\sum x_i e_i = 0$ (la segunda ecuación normal).
2. Con esos puntos, los residuos tienen una suma de cuadrados de 0,2. Usando $s^2 = \sum e_i^2/(N-2)$ (se divide por $N - 2$ porque se han ajustado dos parámetros), calcula $s$ y $\sigma_b$.
3. Si duplicas el rango de $x$ (puntos en 2, 4, 6 y 8) con la misma dispersión, ¿cómo cambia $\sigma_b$?

<details>
<summary>Soluciones</summary>

1. $1 \cdot 0{,}1 + 2\cdot(-0{,}3) + 3 \cdot 0{,}3 + 4\cdot(-0{,}1) = 0{,}1 - 0{,}6 + 0{,}9 - 0{,}4 =$ **0**.
2. $s^2 = 0{,}2/2 = 0{,}1$, $s \approx 0{,}316$. $\sigma_b = 0{,}316/\sqrt{5} \approx$ **0,14**: la pendiente es $1{,}4 \pm 0{,}14$.
3. $\sum (x_i - \bar{x})^2$ se multiplica por 4, así que $\sigma_b$ se **divide por 2**.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Capítulo 26, Galaxias, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/26%3A_Galaxias). Español; el descubrimiento de las galaxias, sus tipos, sus propiedades y la escala de distancias extragaláctica. Verificado el 20 de noviembre de 2026.
2. [Capítulo 19, Distancias celestiales, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/19%3A_Distancias_Celestiales). Español; las estrellas variables como medidoras de distancias y la historia de Leavitt. Verificado el 20 de noviembre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). Para practicar el salto de estrella en estrella hasta M31 y M33. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
