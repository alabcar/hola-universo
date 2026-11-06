---
title: "Semana 20 · ¿Dónde está el punto en torno al que giran dos cuerpos?"
description: "Fase 2 · Órbitas. Medias ponderadas y centro de masas; el problema de los dos cuerpos; el baricentro del Sistema Solar; estrellas dobles."
sidebar:
  order: 20
  label: "20. ¿Dónde está el punto en torno al que giran dos cuerpos?"
---

## La pregunta del cielo

Hasta ahora has puesto el Sol quieto en el centro y los planetas girando a su alrededor. Pero la tercera ley de Newton dice que si el Sol tira de Júpiter, Júpiter tira del Sol con la misma fuerza. El Sol también tiene que moverse. Lo que ocurre de verdad es que **los dos giran alrededor de un punto común**, el centro de masas, que no está en el centro del Sol.

Ese pequeño bamboleo del Sol no es una curiosidad: medir el bamboleo de otras estrellas es una de las formas de descubrir planetas a su alrededor (lo verás en la semana 47). Y en las estrellas dobles, donde las dos masas son parecidas, el efecto es enorme: las dos estrellas dan vueltas una alrededor de la otra, y de su movimiento se deducen sus masas. Así se han pesado la mayoría de las estrellas cuya masa conocemos con precisión.

Esta semana aprendes a calcular el centro de masas, que es una media ponderada, y lo que significa para el movimiento de dos cuerpos que se atraen.

## Las cinco sesiones

### Sesión 1 · Matemáticas: medias ponderadas (30-40 min)

**La media de siempre.** La media de varios números es su suma dividida por cuántos hay. La media de 4, 6 y 8 es 6. Cada número cuenta lo mismo.

**Cuando no todos cuentan igual.** Si en un curso el examen final vale el triple que un trabajo, no tiene sentido hacer la media normal. Se usa una **media ponderada**: cada valor $x_i$ se multiplica por su **peso** $w_i$, se suma todo y se divide por la suma de los pesos:

$$\bar{x} = \frac{w_1 x_1 + w_2 x_2 + \dots + w_n x_n}{w_1 + w_2 + \dots + w_n}.$$

Con un trabajo de 8 (peso 1) y un examen de 5 (peso 3), la media ponderada es $(8 + 15)/4 = 5{,}75$, más cerca de la nota que más pesa. Esa es la propiedad clave: la media ponderada siempre queda entre el valor más pequeño y el más grande, y más cerca de los valores con más peso.

**El balancín.** Dos niños en un balancín se equilibran si el más pesado se sienta más cerca del eje. Arquímedes lo formuló en el siglo III a. C. como la **ley de la palanca**: hay equilibrio cuando $m_1\,d_1 = m_2\,d_2$, siendo $d_1$ y $d_2$ las distancias de cada uno al punto de apoyo. Ese punto de apoyo es el **centro de masas** de los dos niños. Si los colocas en una recta, en las posiciones $x_1$ y $x_2$, el centro de masas está en la media de las posiciones ponderada por las masas:

$$x_\text{cm} = \frac{m_1 x_1 + m_2 x_2}{m_1 + m_2}.$$

Puedes comprobar que cumple la ley de la palanca. Si los niños pesan 20 y 30 kg y están en $x = 0$ y $x = 3$ m, el centro de masas está en $x = 90/50 = 1{,}8$ m: a 1,8 m del ligero y a 1,2 m del pesado, y $20 \cdot 1{,}8 = 30 \cdot 1{,}2 = 36$.

:::note[De dónde viene la palabra]
**Ponderar** viene del latín *ponderare*, «pesar», de *pondus*, «peso» (de ahí también *ponderoso* y *libra*, en el sentido de *pondo*, la unidad de peso romana). Una media ponderada es literalmente una media «pesada». **Baricentro**, otro nombre del centro de masas, viene del griego *barýs*, «pesado» (como en *barómetro*, «medidor del peso del aire»), y *kéntron*, «aguijón», la punta fija del compás alrededor de la cual se traza el círculo. **Centro** viene de la misma palabra.
:::

**Ejercicios**

1. Calcula la media ponderada de 7 (peso 2), 9 (peso 1) y 4 (peso 3).
2. Una barra ligera de 2 m tiene una masa de 1 kg en un extremo y otra de 4 kg en el otro. ¿Dónde hay que sujetarla para que quede en equilibrio?
3. La Tierra tiene 81,3 veces la masa de la Luna, y la distancia entre sus centros es de 384 400 km. ¿A qué distancia del centro de la Tierra está el centro de masas? ¿Está dentro o fuera de la Tierra (radio 6371 km)?

<details>
<summary>Soluciones</summary>

1. $(14 + 9 + 12)/6 = 35/6 \approx$ **5,83**.
2. Con la masa de 1 kg en $x = 0$ y la de 4 kg en $x = 2$: $x_\text{cm} = 8/5 =$ **1,6 m** del extremo ligero, a 0,4 m del pesado.
3. Con la Tierra en 0 y la Luna en 384 400 km: $x_\text{cm} = 384\,400 \cdot 1/(81{,}3 + 1) \approx$ **4670 km** del centro de la Tierra. Está **dentro** de la Tierra, a unos 1700 km bajo la superficie.

</details>

### Sesión 2 · Matemáticas: el centro de masas con vectores (30-35 min)

En el plano o en el espacio se hace lo mismo con los vectores de posición:

$$\vec{r}_\text{cm} = \frac{m_1\vec{r}_1 + m_2\vec{r}_2}{m_1 + m_2},$$

componente a componente. Para más cuerpos, se suman todos los términos $m_i\vec{r}_i$ y se divide por la masa total.

**Dos cuerpos: una forma útil.** Llama $\vec{r} = \vec{r}_2 - \vec{r}_1$ al vector que va del cuerpo 1 al cuerpo 2, y $M = m_1 + m_2$ a la masa total. Con un poco de álgebra:

$$\vec{r}_1 = \vec{r}_\text{cm} - \frac{m_2}{M}\,\vec{r}, \qquad \vec{r}_2 = \vec{r}_\text{cm} + \frac{m_1}{M}\,\vec{r}.$$

Cada cuerpo está, respecto al centro de masas, a una fracción de la separación total, y **esa fracción es la masa del otro**. El cuerpo pesado está cerca del centro de masas y el ligero, lejos. Las dos distancias están en proporción inversa a las masas: $d_1/d_2 = m_2/m_1$.

**Ejercicios**

1. Dos masas de 2 kg y 6 kg están en $(0, 0)$ y $(4, 4)$. Calcula el centro de masas.
2. Tres masas iguales están en los vértices de un triángulo: $(0, 0)$, $(6, 0)$ y $(0, 3)$. ¿Dónde está su centro de masas?

<details>
<summary>Soluciones</summary>

1. $(2 \cdot (0,0) + 6 \cdot (4,4))/8 = (24, 24)/8 =$ **(3, 3)**: a tres cuartos del camino, del lado de la masa grande.
2. $((0 + 6 + 0)/3,\ (0 + 0 + 3)/3) =$ **(2, 1)**.

</details>

### Sesión 3 · Física: el problema de los dos cuerpos (35-45 min)

**El centro de masas no se acelera.** En un sistema aislado de dos cuerpos, las únicas fuerzas son las que se hacen entre sí, iguales y opuestas. Si sumas las dos ecuaciones $m_1\vec{a}_1 = \vec{F}$ y $m_2\vec{a}_2 = -\vec{F}$, las fuerzas se anulan: $m_1\vec{a}_1 + m_2\vec{a}_2 = 0$. Eso significa que el centro de masas no tiene aceleración. Está quieto o se mueve en línea recta a velocidad constante, haga lo que haga cada cuerpo. Es el punto natural para poner el origen.

**Cada uno gira alrededor del centro de masas.** Visto desde el centro de masas, los dos cuerpos recorren elipses con la misma forma y la misma excentricidad, cada una con un foco en el centro de masas, y con tamaños en proporción inversa a sus masas. Siempre están en lados opuestos del centro de masas y tardan exactamente lo mismo en dar la vuelta.

**Kepler, versión completa.** La separación entre los dos cuerpos también describe una elipse, de semieje mayor $a$ (la suma de los semiejes de las dos elipses). Y la tercera ley de Kepler, en su forma exacta, depende de la **suma** de las masas:

$$T^2 = \frac{4\pi^2}{G\,(m_1 + m_2)}\,a^3.$$

Cuando un cuerpo es mucho más pequeño que el otro, como un planeta frente al Sol, su masa apenas cuenta y se recupera la ley de siempre. Pero si se conocen $T$ y $a$ de una estrella doble, la ley da la masa total del par. Y si además se mide qué fracción de la separación está cada estrella del centro de masas, se obtiene la masa de cada una.

**El bamboleo del Sol.** La masa de Júpiter es 1/1048 de la del Sol. El centro de masas Sol-Júpiter está a $5{,}2\ \text{ua} / 1049 \approx 742\,000$ km del centro del Sol, un poco **por fuera** de su superficie (el radio del Sol es de 696 000 km). El Sol describe un pequeño círculo alrededor de ese punto cada 11,9 años, a unos 12,5 m/s, la velocidad de un coche por ciudad. Con todos los planetas juntos, el movimiento del Sol alrededor del centro de masas del Sistema Solar es una curva enredada, que a veces lo saca más de un radio solar del centro y a veces lo deja casi encima.

**Qué hacer**

1. Calcula la velocidad del Sol alrededor del centro de masas Sol-Júpiter. Júpiter va a 13,1 km/s.
2. ¿Dónde está el centro de masas Sol-Tierra? La Tierra tiene $3{,}0 \times 10^{-6}$ veces la masa del Sol.
3. En la estrella doble Sirio, la separación media entre las dos estrellas es de unas 19,8 ua y el periodo, de unos 50,1 años. Calcula la masa total en masas solares (con $T$ en años, $a$ en ua y masas en masas solares, la ley queda $T^2 = a^3/(m_1 + m_2)$).

<details>
<summary>Soluciones</summary>

1. Las velocidades están en la misma proporción que las distancias: $13{,}1\ \text{km/s} / 1048 \approx$ **12,5 m/s**.
2. A $1{,}496 \times 10^{8}\ \text{km} \cdot 3{,}0\times10^{-6} \approx$ **450 km** del centro del Sol: en su interior, muy cerca del centro.
3. $m_1 + m_2 = a^3/T^2 = 19{,}8^3 / 50{,}1^2 \approx 7762/2510 \approx$ **3,1 masas solares**. Midiendo las dos órbitas por separado se sabe que Sirio A tiene unas 2 masas solares y su compañera, Sirio B, una enana blanca, aproximadamente 1.

</details>

### Sesión 4 · Astronomía y observación: estrellas dobles (30-45 min)

Muchas estrellas que a simple vista parecen una sola son en realidad dos o más. Algunas solo están en la misma dirección por casualidad, a distancias muy distintas (**dobles ópticas**). Otras están unidas por la gravedad y giran alrededor de su centro de masas (**binarias**). En la Vía Láctea, una gran parte de las estrellas como el Sol tienen al menos una compañera.

**Mizar y Alcor, a simple vista.** En la Osa Mayor (el Carro), la estrella central del mango es Mizar. Si tienes buena vista y el cielo no es muy luminoso, verás pegada a ella una estrella más débil, Alcor, a unos 12 minutos de arco: un poco menos de la mitad del diámetro de la Luna. Con prismáticos se separan sin problemas. Con un telescopio pequeño, Mizar se desdobla a su vez en dos estrellas. En noviembre, desde latitudes como las de España, la Osa Mayor está baja en el norte al anochecer y sube durante la noche; no se pone nunca.

**Sirio.** La estrella más brillante del cielo nocturno tiene una compañera, Sirio B, una enana blanca diez mil veces más débil, muy difícil de ver incluso con telescopio por el deslumbramiento de Sirio A. Su existencia se dedujo en 1844 antes de verla: Friedrich Bessel notó que Sirio se bamboleaba en el cielo con un periodo de unos 50 años, señal de una compañera invisible. Es el mismo razonamiento que se usa hoy con los exoplanetas. Sirio sale a medianoche en noviembre y domina el cielo de las noches de invierno.

**En Stellarium.** Busca Mizar y acércate con el zoom: verás que Stellarium la muestra como doble. Mira también Albireo, en el Cisne, una pareja famosa por el contraste de colores (amarilla y azul) que se separa con un telescopio pequeño. Lee en el panel de información la separación angular entre las componentes.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 20:

- calcula centros de masas con NumPy,
- simula dos cuerpos que se atraen, con el método de Verlet de la semana 17, para distintas proporciones de masas,
- comprueba que el centro de masas no se acelera y que los dos cuerpos dan vueltas a su alrededor con el mismo periodo,
- mide el periodo en la simulación y lo compara con la tercera ley de Kepler con la suma de las masas,
- dibuja el bamboleo del Sol producido por Júpiter.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-20.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-20.ipynb)

## Qué has aprendido

- **La respuesta.** Dos cuerpos que se atraen giran alrededor de su centro de masas, la media de sus posiciones ponderada por sus masas. El centro de masas no se acelera, y cada cuerpo está de él a una distancia inversamente proporcional a su masa. La Tierra y la Luna giran alrededor de un punto que está dentro de la Tierra; el Sol y Júpiter, alrededor de un punto que está justo fuera del Sol.
- **La física.** La tercera ley de Kepler exacta depende de la suma de las masas: $T^2 = 4\pi^2 a^3 / (G(m_1 + m_2))$. Con ella se pesan las estrellas dobles.
- **Las herramientas.** Media ponderada, ley de la palanca, centro de masas con vectores y la descomposición de las posiciones en centro de masas más posición relativa.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 13.4, Órbita satelital y energía, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-4-orbita-satelital-y-energia). Español; incluye el caso de dos cuerpos que giran alrededor de su centro de masas, con el ejemplo de la Tierra y la Luna. Verificado el 6 de noviembre de 2026.
2. [Sección 13.5, Leyes del movimiento planetario de Kepler, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-5-leyes-del-movimiento-planetario-de-kepler). Español; explica que en un sistema de dos cuerpos cada uno recorre una cónica con el centro de masas en el foco. Verificado el 6 de noviembre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

Los datos de Sirio (periodo, separación y masas) son aproximados y los he escrito de memoria. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
