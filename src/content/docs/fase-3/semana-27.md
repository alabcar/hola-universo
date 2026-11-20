---
title: "Semana 27 · ¿Qué es una onda?"
description: "Fase 3 · La luz. Seno y coseno como funciones del tiempo y del espacio, amplitud, frecuencia y fase, superposición, interferencia, el experimento de Young y la contaminación lumínica."
sidebar:
  order: 27
  label: "27. ¿Qué es una onda?"
---

## La pregunta del cielo

Durante más de un siglo, los físicos discutieron qué era la luz. Newton pensaba que eran partículas diminutas, «corpúsculos», que salían disparadas de los objetos luminosos. Su contemporáneo Christiaan Huygens defendía que era una onda, como las olas en un estanque o el sonido en el aire. El prestigio de Newton inclinó la balanza hacia las partículas, hasta que en 1801 el médico y físico inglés Thomas Young hizo pasar luz por dos rendijas muy finas y obtuvo, en una pantalla, un patrón de bandas claras y oscuras. Dos haces de luz que se suman y dan oscuridad: eso solo lo pueden hacer las ondas.

La semana pasada usaste la longitud de onda para hablar del color. Esta semana aprendes qué es una onda de verdad: cómo se describe con matemáticas, qué significa que dos ondas interfieran y por qué esa interferencia es la huella dactilar de una onda. Al final, en el cielo, una cuestión práctica: cuánta luz artificial hay en el tuyo.

:::note[De dónde viene la palabra]
**Onda** viene del latín *unda*, «ola», de la que salen también *inundar* (llenar de olas), *ondular* y *abundar* (desbordarse, como el agua que rebosa). **Frecuencia** viene de *frequens*, «numeroso, repetido, concurrido»: algo frecuente es algo que se repite muchas veces. **Amplitud** viene de *amplus*, «ancho, grande».
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: el seno como función del tiempo y del espacio (40-45 min)

**Un vaivén.** En la semana 13 viste el seno y el coseno como coordenadas de un punto que gira en una circunferencia. Si miras ese punto de perfil, solo ves su altura, que sube y baja: $y = \sin\theta$. Si el punto gira con velocidad angular constante $\omega$, el ángulo crece con el tiempo, $\theta = \omega t$, y la altura oscila:

$$y(t) = A\sin(\omega t + \varphi).$$

Es la función de cualquier vaivén regular: un péndulo pequeño (semana 12), un muelle (semana 23), un punto de una cuerda de guitarra. Cada letra tiene un significado:

- **$A$, la amplitud**: lo lejos que llega la oscilación desde el centro. El seno va de −1 a 1, así que $A\sin$ va de $-A$ a $A$.
- **$T$, el periodo**: el tiempo que tarda en repetirse. Como el seno se repite cada $2\pi$ radianes, $\omega T = 2\pi$.
- **$f$, la frecuencia**: cuántas veces se repite por segundo, $f = 1/T$. Se mide en **hercios** (Hz): 1 Hz es una oscilación por segundo.
- **$\omega$, la frecuencia angular**: $\omega = 2\pi f$, en radianes por segundo.
- **$\varphi$, la fase inicial** (la letra griega fi): en qué punto del ciclo empieza la oscilación en $t = 0$. Un desfase de $\pi/2$ (90°) convierte un seno en un coseno.

**Una onda se mueve.** Una oscilación se queda en un sitio. Una **onda** es una oscilación que **viaja**: cada punto del medio oscila, y el patrón de crestas y valles se desplaza. Piensa en una ola en el mar: el agua sube y baja casi en el mismo sitio, pero la forma de la ola avanza hacia la playa. Una onda que avanza hacia la derecha se escribe

$$y(x, t) = A\sin(k x - \omega t + \varphi),$$

con dos números que describen el patrón:

- **$\lambda$, la longitud de onda**: la distancia entre dos crestas. Como el seno se repite cada $2\pi$, $k\lambda = 2\pi$, y $k = 2\pi/\lambda$ se llama **número de onda**.
- **La velocidad de la onda**, $v$: una cresta avanza una longitud de onda en cada periodo, así que $v = \lambda/T$, es decir,

$$v = \lambda f.$$

Es la relación fundamental de todas las ondas. Para la luz, $v = c$: cuanto menor es la longitud de onda, mayor es la frecuencia.

**Dos maneras de mirar una onda.** Una función de dos variables, $x$ y $t$, es difícil de dibujar. Se suele mirar de dos formas: una **foto** (fijas $t$ y dibujas la forma en el espacio, donde ves la longitud de onda) o un **registro** en un punto (fijas $x$ y dibujas cómo oscila con el tiempo, donde ves el periodo). El cuaderno de esta semana dibuja las dos.

:::note[De dónde viene la palabra]
El **hercio** (en inglés, *hertz*) lleva el nombre de Heinrich Hertz, el físico alemán que en 1887 produjo y detectó por primera vez ondas de radio en su laboratorio (semana 30). **Periodo**, como viste en la semana 4, es la «vuelta» que regresa al principio. **Fase**, en la semana 5, era «aparición»: la fase de una onda dice en qué momento de su ciclo «aparece».
:::

**Ejercicios**

1. Una oscilación tiene periodo 0,02 s. ¿Cuál es su frecuencia? ¿Y su frecuencia angular?
2. La nota la central de un piano vibra a 440 Hz. Con el sonido a 343 m/s en el aire, ¿cuál es su longitud de onda?
3. La luz verde tiene $\lambda = 530$ nm. ¿Cuál es su frecuencia?
4. ¿Qué diferencia hay entre $\sin(\omega t)$ y $\sin(\omega t + \pi)$?

<details>
<summary>Soluciones</summary>

1. $f = 1/0{,}02 =$ **50 Hz** (la frecuencia de la red eléctrica en España). $\omega = 2\pi \cdot 50 \approx$ **314 rad/s**.
2. $\lambda = v/f = 343/440 \approx$ **0,78 m**.
3. $f = c/\lambda = 3{,}00\times10^8 / 5{,}30\times10^{-7} \approx$ **5,7 × 10¹⁴ Hz**: más de quinientos billones de oscilaciones por segundo.
4. Un desfase de $\pi$ (media vuelta): cuando una tiene una cresta, la otra tiene un valle. Una es la otra cambiada de signo.

</details>

### Sesión 2 · Matemáticas: sumar ondas (35-40 min)

**El principio de superposición.** Cuando dos ondas pasan por el mismo sitio, sus efectos se **suman**: el desplazamiento total es la suma de los desplazamientos de cada una. Después de cruzarse, cada onda sigue su camino como si nada. Lo ves en un estanque cuando caen dos piedras: los anillos se atraviesan sin destruirse.

**Misma frecuencia: interferencia.** Si las dos ondas tienen la misma frecuencia y amplitud, el resultado depende de su desfase:

- **En fase** (desfase 0): crestas con crestas y valles con valles. La amplitud se duplica: **interferencia constructiva**.
- **En oposición** (desfase $\pi$): crestas con valles. Se anulan: **interferencia destructiva**.
- Con desfases intermedios, el resultado es otra onda de la misma frecuencia con una amplitud intermedia.

El desfase entre dos ondas que salen a la vez de dos puntos distintos depende de la **diferencia de caminos**: si una recorre una longitud de onda más que la otra, vuelven a estar en fase; si recorre media longitud de onda más, quedan en oposición.

**Frecuencias parecidas: pulsaciones.** Si las dos frecuencias son un poco distintas, $f_1$ y $f_2$, las ondas van entrando y saliendo de fase poco a poco: unas veces se refuerzan y otras se anulan. El resultado es una onda cuya amplitud sube y baja lentamente, con la frecuencia de **pulsación** $|f_1 - f_2|$. Los afinadores de guitarra lo usan: si dos cuerdas casi afinadas suenan a la vez, se oye un «uaa-uaa-uaa» que se hace más lento a medida que se igualan. Es la misma idea que el periodo sinódico de la semana 13 o las mareas vivas y muertas de la semana 21.

**Ejercicios**

1. Dos ondas de amplitud 1 se suman en fase. ¿Qué amplitud tiene el resultado? ¿Y si están en oposición?
2. Dos altavoces emiten la misma nota de longitud de onda 0,78 m. Estás a 3,00 m de uno y a 3,39 m del otro. ¿Oyes la nota reforzada o debilitada?
3. Dos diapasones vibran a 440 y 443 Hz. ¿Cuántas pulsaciones por segundo oyes?

<details>
<summary>Soluciones</summary>

1. En fase: **2**. En oposición: **0**.
2. La diferencia de caminos es 0,39 m, la mitad de 0,78: las ondas llegan en oposición y la nota se oye **debilitada**.
3. **3 pulsaciones por segundo**.

</details>

### Sesión 3 · Física: ondas, luz e interferencia (40-45 min)

**Qué viaja en una onda.** En una onda no viaja la materia: viaja la **energía** y la forma. Hay dos grandes tipos:

- **Ondas mecánicas**, que necesitan un medio material: el sonido (el aire se comprime y se expande), las olas, las ondas sísmicas, las de una cuerda.
- **Ondas electromagnéticas**, que no necesitan ningún medio y viajan por el vacío: la luz, las ondas de radio, los rayos X. Lo que oscila son campos eléctricos y magnéticos (semanas 29 y 30).

Además, una onda es **transversal** si el medio oscila perpendicular a la dirección en que avanza la onda (una cuerda, la luz) y **longitudinal** si oscila en la misma dirección (el sonido).

**El experimento de Young.** Si la luz es una onda, dos haces de luz que salen de dos rendijas muy próximas deben interferir. En la pantalla, en los puntos donde la diferencia de caminos desde las dos rendijas es un número entero de longitudes de onda, las ondas llegan en fase y hay una **franja brillante**; donde la diferencia es media longitud de onda (o una y media, o dos y media...), llegan en oposición y hay una **franja oscura**. Con dos rendijas separadas una distancia $d$ y una pantalla a una distancia $L$ mucho mayor, las franjas brillantes aparecen separadas

$$\Delta y \approx \frac{\lambda\,L}{d}.$$

(Lo deduces en el cuaderno con la aproximación de ángulos pequeños de la semana 6.) Con rendijas separadas 0,1 mm, una pantalla a 1 m y luz verde, las franjas están a unos 5 mm: se ven a simple vista. Young midió así, por primera vez, la longitud de onda de la luz.

**La difracción.** Una onda que pasa por una abertura o junto a un obstáculo se curva un poco hacia la zona de sombra: es la **difracción**. Se nota cuando la abertura es comparable a la longitud de onda. El sonido, con longitudes de onda de metros, dobla las esquinas (oyes a alguien que está en otra habitación); la luz, con longitudes de onda de micras, apenas lo hace, y por eso las sombras son nítidas. En la semana 28 verás que la difracción pone un límite a lo que puede distinguir cualquier telescopio.

**Colores sin pigmentos.** Los colores de una pompa de jabón, de una mancha de aceite en el suelo mojado o de la cara de un CD no vienen de ningún pigmento. Son interferencia: la luz reflejada por las dos caras de la película fina de jabón, o por las miles de pistas del CD, se suma en fase para unos colores y en oposición para otros, según el ángulo desde el que miras.

:::note[De dónde viene la palabra]
**Interferencia** se formó en el siglo XIX a partir del latín *inter*, «entre», y *ferire*, «golpear»: ondas que se golpean entre sí. El término lo usó el propio Young. **Difracción** lo acuñó el jesuita italiano Francesco Maria Grimaldi en un libro publicado en 1665, a partir de *diffringere*, «romper en pedazos»: la luz que roza un borde parece quebrarse en franjas.
:::

**Qué hacer**

1. Calcula la separación entre franjas para luz roja (650 nm), rendijas a 0,2 mm y una pantalla a 2 m.
2. Explica por qué, si la luz fuera un chorro de partículas, en el experimento de Young no deberían aparecer franjas oscuras en el centro de zonas iluminadas por las dos rendijas.
3. Una onda de radio de FM tiene una frecuencia de 100 MHz. ¿Cuál es su longitud de onda? ¿Por qué la radio «dobla» las colinas mejor que la luz?

### Sesión 4 · Astronomía y observación: la luz que sobra (30-45 min)

**Interferencia en casa.** Antes de salir, mira la cara grabada de un CD o un DVD bajo una lámpara: verás bandas de colores que cambian al inclinarlo. Haz pompas de jabón y fíjate en cómo cambian los colores a medida que la película se adelgaza, hasta que se vuelve negra justo antes de romperse (es tan fina que las dos reflexiones se anulan). Es interferencia de luz, a simple vista.

**¿Cuánta luz artificial hay en tu cielo?** La **contaminación lumínica** es la luz artificial que se escapa hacia el cielo, se dispersa en la atmósfera (semana 26) y lo ilumina como una niebla brillante. Es la razón de que desde una ciudad se vean unas decenas de estrellas en lugar de miles. Hay una forma sencilla de medirla, la que usa la campaña internacional *Globe at Night*:

1. Una noche sin Luna, con el cielo despejado, sal a un lugar sin farolas directas y espera al menos 15 minutos a que tus ojos se adapten a la oscuridad (no mires el móvil).
2. Busca Orión (en noviembre sale hacia las 21:00-22:00 y se ve bien a partir de medianoche; en enero y febrero, a primera hora de la noche).
3. Compara lo que ves con las cartas de magnitud de *Globe at Night*, que muestran Orión tal como se ve con distintas magnitudes límite (la magnitud límite, la de la estrella más débil que alcanzas a ver, la estudiarás en la semana 33). Elige la que se parezca más a tu cielo y apúntala.
4. Repite la observación desde un lugar más oscuro si puedes, y con los prismáticos 8×30: ¿cuántas estrellas más ves dentro del rectángulo de Orión?

**La luz blanca moderna dispersa más.** Las farolas antiguas de sodio daban una luz anaranjada; las de sodio de baja presión, casi de un solo color (lo verás en la semana 32). Las de LED blanco emiten mucho azul, y el azul se dispersa en el aire mucho más que el naranja (semana 26). Por eso, a igual potencia, la luz blanca fría ilumina más el cielo. Las normativas modernas recomiendan farolas que no envíen luz hacia arriba y tonos cálidos.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 27:

- dibuja una onda como foto en el espacio y como registro en el tiempo, y la anima paso a paso,
- suma ondas en fase, en oposición y con frecuencias parecidas, y mide la frecuencia de pulsación,
- deduce la separación de las franjas de Young y la comprueba simulando la intensidad en una pantalla,
- dibuja el patrón de interferencia de dos fuentes en un plano, como el de dos piedras en un estanque.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-27.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-27.ipynb)

## Qué has aprendido

- **La respuesta.** Una onda es una oscilación que viaja: cada punto del medio oscila y el patrón de crestas y valles avanza con una velocidad $v = \lambda f$. Lo que transporta es energía, no materia. Su firma inconfundible es la interferencia: dos ondas que se suman pueden reforzarse o anularse.
- **La luz.** El experimento de Young de 1801 demostró que la luz es una onda, con longitudes de onda de unos cientos de nanómetros y frecuencias de cientos de billones de hercios.
- **Las herramientas.** El seno como función del tiempo y del espacio; amplitud, periodo, frecuencia, frecuencia angular, fase, longitud de onda y número de onda; el principio de superposición; interferencia constructiva y destructiva; y pulsaciones.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**Cualquier forma es una suma de senos.** En 1807, el matemático francés Joseph Fourier propuso una idea que al principio pareció escandalosa: **cualquier** función periódica, por irregular que sea, se puede escribir como una suma de senos y cosenos con frecuencias múltiplos de la fundamental. Por ejemplo, una onda cuadrada, que salta de $+1$ a $-1$ cada medio periodo, es

$$\text{cuadrada}(t) = \frac{4}{\pi}\left(\sin\omega t + \frac{\sin 3\omega t}{3} + \frac{\sin 5\omega t}{5} + \frac{\sin 7\omega t}{7} + \dots\right).$$

Solo aparecen las frecuencias impares, con amplitudes que bajan como $1/n$. Con unos pocos términos ya se reconoce la forma; con muchos, se acerca tanto como quieras (salvo un pequeño sobresalto en los saltos, el **fenómeno de Gibbs**). Esa lista de amplitudes de cada frecuencia es el **espectro** de la señal.

Es una de las ideas más fértiles de la física y la ingeniería: los ecualizadores de música, la compresión MP3 y JPEG, el análisis de las mareas reales (semana 21) y la espectroscopia astronómica (semanas 31 y 32) se basan en descomponer señales en frecuencias.

**La identidad de las pulsaciones.** La suma de dos senos de frecuencias parecidas se puede reescribir con la identidad trigonométrica

$$\sin a + \sin b = 2\,\sin\frac{a+b}{2}\,\cos\frac{a-b}{2}.$$

Con $a = \omega_1 t$ y $b = \omega_2 t$, la suma es una oscilación rápida, con la frecuencia media, multiplicada por una envolvente lenta, $\cos\left(\frac{\omega_1 - \omega_2}{2} t\right)$. La envolvente tiene frecuencia $(f_1 - f_2)/2$, pero el oído percibe dos máximos de volumen por cada ciclo de la envolvente (uno con el coseno positivo y otro con el negativo), así que la frecuencia de pulsación es $|f_1 - f_2|$.

**Ejercicios**

1. Suma a mano (con calculadora) los cuatro primeros términos de la serie de la onda cuadrada en $\omega t = \pi/2$. ¿A qué valor te acercas?
2. Usa la identidad para escribir $\sin(10t) + \sin(12t)$ como un producto. ¿Cuál es la frecuencia angular de la envolvente?
3. Demuestra la identidad a partir de las fórmulas del seno de una suma y de una diferencia: $\sin(x \pm y) = \sin x\cos y \pm \cos x \sin y$. Pista: llama $x = (a+b)/2$ e $y = (a-b)/2$.

<details>
<summary>Soluciones</summary>

1. $\frac{4}{\pi}(1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7}) = \frac{4}{\pi} \cdot 0{,}7238 \approx$ **0,92**, acercándose a 1. (Los senos de $3\pi/2$ y $7\pi/2$ valen $-1$.)
2. $2\sin(11t)\cos(t)$. La envolvente tiene frecuencia angular **1 rad/s**.
3. Con $x + y = a$ y $x - y = b$: $\sin a + \sin b = \sin(x+y) + \sin(x-y) = 2\sin x \cos y$, porque los términos $\cos x \sin y$ se cancelan.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [16.2 Matemáticas de las ondas, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/16-2-matematicas-de-las-ondas). Español; la función de onda, la longitud de onda, el número de onda y la velocidad. Verificado el 20 de noviembre de 2026.
2. [16.5 Interferencia de ondas, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/16-5-interferencia-de-ondas). Español; superposición e interferencia. Verificado el 20 de noviembre de 2026.
3. [3.1 Interferencia de doble rendija de Young, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/3-1-interferencia-de-doble-rendija-de-young). Español; el experimento de 1801 con todo detalle. Verificado el 20 de noviembre de 2026.
4. [Globe at Night](https://globeatnight.org/). Campaña internacional para medir la contaminación lumínica con Orión y otras constelaciones; tiene cartas de magnitud. **(Sin verificar)**: lo he visto citado en materiales de la NASA, pero no he podido abrir la web.
5. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
