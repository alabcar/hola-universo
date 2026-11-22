---
title: "Semana 45 · ¿Por qué se curva la luz cerca de una masa?"
description: "Fase 4 · El universo grande. Geometría sobre una esfera: geodésicas y triángulos de más de 180°; el principio de equivalencia, la gravedad como curvatura del espacio-tiempo, el eclipse de 1919, la precesión de Mercurio, el corrimiento gravitatorio y las lentes gravitacionales en imágenes de Webb y Euclid."
sidebar:
  order: 45
  label: "45. ¿Por qué se curva la luz cerca de una masa?"
---

## La pregunta del cielo

El 29 de mayo de 1919 hubo un eclipse total de Sol. Dos expediciones británicas, una en la isla de Príncipe, frente a la costa de África, dirigida por Arthur Eddington, y otra en Sobral, en Brasil, fotografiaron las estrellas que se veían junto al Sol oscurecido, en la constelación de Tauro. Meses después las compararon con fotografías del mismo campo de estrellas tomadas de noche, sin el Sol delante. Las estrellas junto al borde del Sol aparecían desplazadas hacia fuera, alrededor de 1,75 segundos de arco: justo lo que predecía una teoría publicada cuatro años antes por Albert Einstein, según la cual la gravedad no es una fuerza, sino la curvatura del espacio y del tiempo.

Cuando se anunció, en noviembre de 1919, Einstein se hizo famoso de la noche a la mañana. Esta semana entiendes qué significa que el espacio esté curvado, por qué eso desvía la luz, y cómo los astrónomos usan hoy esas desviaciones como telescopios naturales para ver galaxias que de otro modo serían invisibles.

:::note[De dónde viene la palabra]
**Geodésica** viene del griego *geōdaisía*, «división de la tierra», de *gê*, «tierra», y *daíein*, «dividir»: la geodesia es la ciencia que mide la forma de la Tierra, y una geodésica era la línea más corta entre dos puntos de su superficie. Hoy se llama así a la línea «más recta posible» en cualquier espacio curvo. **Gravitatorio** viene de *gravitas*, «pesadez» (semana 16).
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: geometría sobre una esfera (35-45 min)

**La línea más recta en una superficie curva.** En un plano, la línea más corta entre dos puntos es una recta. Sobre la superficie de una esfera no hay rectas: la línea más corta entre dos puntos es un arco de **círculo máximo**, un círculo cuyo centro es el centro de la esfera, como el ecuador o los meridianos. Esas líneas son las **geodésicas** de la esfera.

Por eso los vuelos de Madrid a Nueva York, o de Europa a Japón, se curvan hacia el norte en un mapa plano: siguen un círculo máximo, que en la esfera es lo más recto posible, aunque el mapa lo deforme.

**Triángulos que suman más de 180°.** Dibuja sobre una esfera un triángulo con lados que sean geodésicas: sal del polo norte por un meridiano hasta el ecuador, recorre un cuarto del ecuador y vuelve al polo por otro meridiano. Los tres ángulos son rectos: **270°**. En una esfera, los ángulos de un triángulo siempre suman más de 180°, y el exceso es proporcional al área del triángulo:

$$\alpha + \beta + \gamma - \pi = \frac{\text{área}}{R^2}.$$

(Ángulos en radianes.) Es la **curvatura** de la superficie. Lo sorprendente es que se puede medir **desde dentro**, sin salir de la superficie: unas hormigas planas que vivieran en ella podrían descubrir que su mundo es curvo midiendo triángulos grandes. Fue la gran idea de Gauss y de su alumno Bernhard Riemann en el siglo XIX: un espacio puede ser curvo por sí mismo, sin estar metido en otro.

**Rectas paralelas que se cruzan.** En la esfera, dos geodésicas que salen paralelas del ecuador (dos meridianos) acaban encontrándose en los polos. Sin que nada las empuje, solo por la forma del espacio. Recuérdalo, porque es la clave de la sesión 3.

**Ejercicios**

1. Comprueba la fórmula del exceso con el triángulo de tres ángulos rectos: ¿qué fracción de la esfera ocupa? ¿Cuánto vale su área?
2. Un triángulo sobre la Tierra ($R = 6371$ km) tiene un área de 10 000 km². ¿Cuánto suman sus ángulos?
3. ¿Por qué no notamos la curvatura de la Tierra al medir los ángulos de un triángulo dibujado en un campo de fútbol?

<details>
<summary>Soluciones</summary>

1. Es **un octavo** de la esfera: área $4\pi R^2/8 = \pi R^2/2$. Exceso: $\pi/2$, es decir, $270^\circ - 180^\circ = 90^\circ$. Coincide.
2. Exceso: $10\,000/6371^2 \approx 2{,}46\times10^{-4}$ rad $\approx 0{,}014^\circ$, unos 51″. Suman **180,014°**.
3. Su área (unos 7000 m²) es tan pequeña comparada con $R^2$ que el exceso es de unas **decenas de millonésimas de segundo de arco**: imposible de medir.

</details>

### Sesión 2 · Matemáticas: cuánto se desvía la luz (35-40 min)

**El ángulo de desviación.** Según la relatividad general, un rayo de luz que pasa a una distancia mínima $b$ de una masa $M$ se desvía un ángulo

$$\alpha = \frac{4GM}{c^2\,b}$$

(en radianes). Fíjate en que $2GM/c^2$ es el radio de Schwarzschild de la semana 36: la desviación es el doble del cociente entre el radio de Schwarzschild y la distancia del rayo. Una masa muy compacta y un rayo que pasa muy cerca, mucha desviación.

Curiosamente, con la gravedad de Newton, tratando la luz como partículas que caen, sale la mitad: $2GM/(c^2 b)$. Ya lo había calculado el alemán Johann von Soldner en 1801. El eclipse de 1919 servía para distinguir entre la predicción de Newton y la de Einstein.

**Las lentes gravitacionales.** Si una masa (una estrella, una galaxia, un cúmulo) está casi exactamente delante de una fuente lejana, la luz de la fuente puede llegarnos por varios caminos, curvados alrededor de la masa. Vemos varias imágenes de la misma fuente, deformadas en arcos, o incluso un anillo completo si la alineación es perfecta: un **anillo de Einstein**. Su radio angular es

$$\theta_E = \sqrt{\frac{4GM}{c^2}\,\frac{D_{ls}}{D_l\,D_s}},$$

donde $D_l$ es la distancia a la lente, $D_s$ a la fuente y $D_{ls}$ entre la lente y la fuente.

**Ejercicios**

1. Calcula la desviación de un rayo que roza el borde del Sol: $M = 1{,}99\times10^{30}$ kg, $b = 6{,}96\times10^8$ m. Pásala a segundos de arco. ¿Cuánto daría la fórmula de Newton?
2. ¿Cuánto se desvía un rayo que roza la Tierra ($M = 5{,}97\times10^{24}$ kg, $b = 6{,}37\times10^6$ m)?
3. Una galaxia de $10^{12}$ masas solares a 1 Gpc hace de lente para otra a 2 Gpc ($D_{ls} \approx 1$ Gpc, $1\ \text{Gpc} = 3{,}09\times10^{25}$ m). Con $4GM_\odot/c^2 = 5{,}9$ km, ¿qué radio de Einstein tiene?

<details>
<summary>Soluciones</summary>

1. $4 \cdot 6{,}67\times10^{-11} \cdot 1{,}99\times10^{30}/(9\times10^{16} \cdot 6{,}96\times10^8) \approx 8{,}5\times10^{-6}$ rad $\approx$ **1,75″**. Newton: **0,87″**.
2. $\approx 2{,}8\times10^{-9}$ rad, unos **0,0006″**.
3. $\theta_E = \sqrt{5{,}9\times10^{15}\ \text{m} \cdot 1/(2 \cdot 3{,}09\times10^{25}\ \text{m})} \approx \sqrt{9{,}5\times10^{-11}} \approx 9{,}8\times10^{-6}$ rad $\approx$ **2″**: el tamaño típico de las lentes de galaxias.

</details>

### Sesión 3 · Física: la gravedad como geometría (40-45 min)

**El pensamiento más feliz.** En 1907, sentado en la oficina de patentes de Berna, Einstein tuvo lo que más tarde llamó «el pensamiento más feliz de mi vida»: una persona que cae libremente no siente su propio peso. Dentro de un ascensor que cae, todo flota; dentro de una nave que acelera en el espacio vacío, todo cae hacia el suelo como si hubiera gravedad. Desde dentro, sin mirar fuera, es imposible distinguir la gravedad de una aceleración. Es el **principio de equivalencia**.

**De ahí sale la curvatura de la luz.** Dentro de la nave que acelera, un rayo de luz que entra por una ventana lateral recorre la cabina en línea recta para alguien de fuera, pero, como la nave acelera hacia arriba mientras tanto, para los de dentro el rayo cae en una curva hacia el suelo. Si gravedad y aceleración son equivalentes, la gravedad también tiene que curvar la luz.

**La gravedad es curvatura.** En 1915, tras años de trabajo con la geometría de Riemann, Einstein publicó la **relatividad general**. Su idea central: la masa y la energía curvan el **espacio-tiempo** (el espacio y el tiempo juntos, semana 44), y los cuerpos libres, sin fuerzas, siguen sus geodésicas, las líneas «más rectas posible». La Tierra no gira alrededor del Sol porque una fuerza tire de ella, sino porque sigue la línea más recta en un espacio-tiempo curvado por el Sol. Como los meridianos que salen paralelos y se juntan en el polo: nada los empuja, es la geometría.

**Las pruebas.**

- **La precesión de Mercurio.** La órbita de Mercurio no es una elipse fija: su perihelio avanza poco a poco. La mayor parte se explica por la atracción de los demás planetas, pero en 1859 Urbain Le Verrier encontró un sobrante que nadie explicaba (con medidas posteriores, unos 43 segundos de arco por siglo) (hasta se propuso un planeta invisible, Vulcano). La relatividad general predice exactamente esos 43″. Einstein lo calculó en noviembre de 1915 y escribió que le dio palpitaciones.
- **La desviación de la luz**, en el eclipse de 1919, y desde entonces con precisión mucho mayor midiendo la desviación de las ondas de radio de cuásares lejanos al pasar junto al Sol.
- **El tiempo y la gravedad.** Cerca de una masa, el tiempo pasa más despacio. En 1959, Robert Pound y Glen Rebka lo midieron en una torre de 22,5 m de la Universidad de Harvard: la luz que bajaba llegaba con la frecuencia un poquito aumentada. Los relojes del GPS lo notan cada día (semana 44).
- **Las ondas gravitacionales** (semana 36) y las imágenes de los agujeros negros, un siglo después.

**Tres tipos de lentes gravitacionales.**

- **Lentes fuertes**: imágenes múltiples, arcos y anillos alrededor de galaxias y cúmulos masivos. La primera, un cuásar doble, se descubrió en 1979. El **anillo de Einstein** casi perfecto que el telescopio Euclid de la ESA encontró en 2025 en la galaxia NGC 6505, a unos 590 millones de años luz, es la luz de otra galaxia, a unos 4400 millones de años luz, curvada alrededor de la primera.
- **Lentes débiles**: deformaciones diminutas de las formas de millones de galaxias del fondo, que solo se notan estadísticamente. Permiten hacer mapas de la materia oscura (semana 43). Es uno de los objetivos principales de Euclid.
- **Microlentes**: cuando una estrella pasa por delante de otra más lejana, la luz de esta aumenta y disminuye durante días o semanas. Si la estrella que hace de lente tiene un planeta, aparece un pico adicional breve: así se han descubierto exoplanetas (semana 47).

:::note[De dónde viene la palabra]
**Lente** es «lenteja» (semana 28): una lente gravitacional no tiene forma de lenteja, pero, como una lente de vidrio, desvía y concentra la luz. **Precesión** viene de *praecedere*, «ir delante»: el perihelio de Mercurio se adelanta un poco en cada vuelta.
:::

**Qué hacer**

1. Explica con tus palabras por qué un astronauta en la Estación Espacial Internacional flota, aunque allí la gravedad de la Tierra es casi el 90 % de la que hay en el suelo.
2. ¿Por qué hacía falta un eclipse total para medir la desviación de la luz en 1919?
3. Si una estrella que hace de microlente tarda 30 días en pasar por delante de otra, ¿por qué un planeta de esa estrella produce un pico de solo horas o días?

### Sesión 4 · Astronomía y observación: lentes gravitacionales en imágenes públicas (30-45 min)

Las lentes gravitacionales no se pueden ver con prismáticos: hacen falta telescopios espaciales. Pero las imágenes son públicas, y aprender a mirarlas es parte de la astronomía moderna.

**El primer campo profundo del Webb.** En julio de 2022, el telescopio espacial James Webb publicó una imagen del cúmulo de galaxias **SMACS 0723**, tal como era hace unos 4600 millones de años. Ábrela a pantalla completa en la página de la ESA y busca:

- **Los arcos**: galaxias del fondo estiradas en forma de arco alrededor del centro del cúmulo. Algunas aparecen repetidas, la misma galaxia en dos o tres sitios.
- **Las galaxias del cúmulo**: los puntos y óvalos amarillentos, casi redondos, que forman la lente.
- **Las estrellas**: las pocas fuentes con picos de difracción en forma de estrella de seis puntas son estrellas de nuestra propia galaxia, en primer plano (los picos los produce la forma hexagonal del espejo del Webb; recuerda la difracción de la semana 27).

**El anillo de Euclid.** En la imagen de NGC 6505 que publicó la ESA en febrero de 2025, el anillo es fino, casi perfecto y rodea el núcleo de la galaxia. Fíjate en el color: el anillo es más azulado que la galaxia que hace de lente. Es otra galaxia, mucho más lejana, con más estrellas jóvenes.

**Una lente de cristal en casa.** Mira una luz lejana a través del pie redondo de una copa de vino, o del fondo de un vaso grueso: moviéndolo, verás la luz convertirse en arcos, en imágenes dobles y, si la alineas bien, en un anillo. El pie de una copa tiene una forma que desvía la luz de manera parecida a como lo hace una masa puntual (más cuanto más cerca del centro), y por eso imita bien las lentes gravitacionales.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 45:

- calcula ángulos de desviación y radios de Einstein para el Sol, una estrella, una galaxia y un cúmulo,
- traza rayos a través de una lente puntual y de una galaxia (modelo de esfera isoterma) y genera las imágenes de una galaxia de fondo: arcos, imágenes dobles y anillos,
- dibuja la curva de luz de una microlente, con y sin un planeta,
- en el apartado opcional, calcula la precesión de Mercurio.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-45.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-45.ipynb)

## Qué has aprendido

- **La respuesta.** La luz se curva cerca de una masa porque la masa curva el espacio-tiempo, y la luz sigue la línea más recta posible en un espacio curvo. Junto al Sol, la desviación es de 1,75″, el doble de lo que daría la gravedad de Newton; lo confirmó el eclipse de 1919.
- **Las lentes.** Galaxias y cúmulos desvían la luz de lo que hay detrás y producen arcos, imágenes múltiples y anillos. Sirven para ver galaxias lejanísimas, pesar la materia oscura y descubrir planetas.
- **Las herramientas.** Las geodésicas, la geometría de una esfera (triángulos que suman más de 180°), el principio de equivalencia y las fórmulas de la desviación y del radio de Einstein.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**La precesión de Mercurio.** La relatividad general predice que el perihelio de un planeta avanza, en cada vuelta, un ángulo

$$\Delta\varphi = \frac{6\pi\,G M}{c^2\,a\,(1 - e^2)}$$

(en radianes), donde $M$ es la masa del Sol, $a$ el semieje mayor de la órbita y $e$ su excentricidad (semana 14). Como siempre, $GM/c^2$ es medio radio de Schwarzschild: el efecto es grande para órbitas pequeñas y excéntricas cerca de masas grandes.

**La ecuación de la lente.** Para una lente puntual, si la fuente está a un ángulo $\beta$ de la línea que une al observador con la lente, las imágenes aparecen en los ángulos $\theta$ que cumplen

$$\beta = \theta - \frac{\theta_E^2}{\theta}.$$

Multiplicando por $\theta$ queda una ecuación de segundo grado (semana 9): $\theta^2 - \beta\theta - \theta_E^2 = 0$, con dos soluciones,

$$\theta_\pm = \frac{\beta \pm \sqrt{\beta^2 + 4\theta_E^2}}{2}.$$

Siempre hay **dos imágenes**: una fuera del radio de Einstein, del mismo lado que la fuente, y otra dentro, del lado opuesto. Si $\beta = 0$, las dos se funden en el anillo de radio $\theta_E$.

**Ejercicios**

1. Calcula la precesión de Mercurio por vuelta con $GM_\odot = 1{,}327\times10^{20}$ m³/s², $a = 5{,}79\times10^{10}$ m y $e = 0{,}206$. Mercurio da una vuelta cada 88 días: ¿cuánto suma en un siglo, en segundos de arco?
2. Haz lo mismo para la Tierra ($a = 1{,}496\times10^{11}$ m, $e = 0{,}017$, una vuelta al año).
3. Una fuente está a $\beta = \theta_E/2$. ¿Dónde aparecen sus dos imágenes, en unidades de $\theta_E$?

<details>
<summary>Soluciones</summary>

1. $\Delta\varphi = 6\pi \cdot 1{,}327\times10^{20}/(9\times10^{16} \cdot 5{,}79\times10^{10} \cdot 0{,}958) \approx 5{,}0\times10^{-7}$ rad por vuelta. En un siglo hay $36\,525/88 \approx 415$ vueltas: $2{,}08\times10^{-4}$ rad $\approx$ **43″**. Exactamente el sobrante de Le Verrier.
2. $\approx 1{,}9\times10^{-7}$ rad por vuelta; en un siglo, **3,8″**, mucho menos, porque la órbita es mayor y casi circular.
3. $\theta_\pm = (0{,}5 \pm \sqrt{0{,}25 + 4})/2 = (0{,}5 \pm 2{,}06)/2$: **1,28** $\theta_E$ y **−0,78** $\theta_E$ (al otro lado de la lente).

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Webb's First Deep Field (ESA)](https://www.esa.int/media/webb-s-first-deep-field). Inglés; la imagen del cúmulo SMACS 0723 en alta resolución, con su descripción. Verificado el 20 de noviembre de 2026.
2. [Webb ofrece la imagen infrarroja más profunda del universo hasta la fecha (NASA Ciencia)](https://ciencia.nasa.gov/universo/webb-ofrece-la-imagen-infrarroja-mas-profunda-del-universo-hasta-la-fecha/). Español; la misma imagen, explicada. Verificado el 20 de noviembre de 2026.
3. [Euclid discovers a stunning Einstein ring (ESA)](https://www.esa.int/Science_Exploration/Space_Science/Euclid/Euclid_discovers_a_stunning_Einstein_ring). Inglés; el anillo de NGC 6505, con imágenes descargables. Verificado el 20 de noviembre de 2026.
4. [Capítulo 24, Agujeros negros y espacio-tiempo curvo, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/24%3A_Agujeros_negros_y_espacio-tiempo_curvo). Español; el principio de equivalencia, el espacio-tiempo curvo y las pruebas de la relatividad general. Verificado el 20 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros: enlaza a las de la ESA y la NASA para que las veas en su web, con sus créditos. Las gráficas las genera el cuaderno.
