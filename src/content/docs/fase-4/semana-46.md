---
title: "Semana 46 · ¿Qué es la mecánica cuántica?"
description: "Fase 4 · El universo grande. Probabilidad, números complejos como flechas y la fórmula de Euler; el efecto fotoeléctrico, la longitud de onda de De Broglie, la doble rendija partícula a partícula, la función de onda y la regla de Born, el principio de incertidumbre, los niveles de energía como ondas estacionarias y la exclusión de Pauli; y las líneas prohibidas del «nebulio»."
sidebar:
  order: 46
  label: "46. ¿Qué es la mecánica cuántica?"
---

## La pregunta del cielo

En la semana 32 viste que los átomos solo emiten y absorben luz de colores muy concretos, y que el modelo de Bohr lo explicaba suponiendo que los electrones solo pueden tener ciertas energías. Pero ¿por qué? Bohr lo había impuesto sin justificarlo. Y en las semanas 34 y 36 apareció dos veces una física extraña: el efecto túnel que permite al Sol fundir hidrógeno, y la presión cuántica que sostiene a las enanas blancas.

La explicación es la **mecánica cuántica**, construida entre 1900 y 1930 por una generación de físicos que tuvieron que abandonar ideas que parecían evidentes. La versión corta: las partículas, como los electrones, también son ondas, y lo que esas ondas describen no es dónde está la partícula, sino la **probabilidad** de encontrarla en cada sitio. Esta semana es un primer vistazo, sin el aparato matemático completo, pero con las dos herramientas que lo hacen posible: la probabilidad y los números complejos.

:::note[De dónde viene la palabra]
**Cuántico** viene del latín *quantum*, «cuánto», «qué cantidad»: Max Planck llamó *Quantum* (en alemán) a los paquetes de energía de su fórmula de 1900 (semana 31). **Probabilidad** viene de *probabilis*, «que se puede probar o aprobar», de *probare*: lo probable era, al principio, lo digno de crédito. **Complejo** viene de *complexus*, «entrelazado»: un número complejo entrelaza dos números en uno.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: probabilidad (35-40 min)

**Qué es una probabilidad.** La probabilidad de un suceso es un número entre 0 (imposible) y 1 (seguro) que mide cuánto esperamos que ocurra. Una forma de entenderla es por frecuencias: si repites un experimento muchísimas veces, la probabilidad es la fracción de veces que ocurre el suceso. La probabilidad de sacar un 3 con un dado es $1/6$ porque, en miles de tiradas, sale más o menos una de cada seis veces.

**Las dos reglas básicas.**

- **Regla de la suma** («o»): si dos sucesos no pueden ocurrir a la vez, la probabilidad de que ocurra uno u otro es la suma. Sacar un 1 o un 2: $1/6 + 1/6 = 1/3$.
- **Regla del producto** («y»): si dos sucesos son independientes, la probabilidad de que ocurran los dos es el producto. Sacar dos seises con dos dados: $1/6 \cdot 1/6 = 1/36$.

Las probabilidades de todos los resultados posibles suman 1.

**Probabilidades sobre un continuo.** Para una cantidad que puede tomar cualquier valor, como la posición de un electrón en una pantalla, no tiene sentido la probabilidad de un punto exacto, sino la de un intervalo. Se describe con una **densidad de probabilidad**, como la campana de Gauss de la semana 42: el área bajo la curva entre dos valores es la probabilidad de caer entre ellos.

**El valor esperado.** Si un resultado $x_i$ tiene probabilidad $p_i$, el **valor esperado** es $\langle x \rangle = \sum p_i\,x_i$: la media que obtendrías repitiendo muchas veces. El de un dado es $(1 + 2 + 3 + 4 + 5 + 6)/6 = 3{,}5$, un valor que nunca sale.

**Ejercicios**

1. ¿Qué probabilidad hay de sacar al menos un seis en dos tiradas de un dado? (Pista: calcula la del suceso contrario.)
2. Lanzas una moneda 10 veces. ¿Qué probabilidad hay de que salgan 10 caras?
3. Una partícula está en una caja de 1 m y su densidad de probabilidad es uniforme. ¿Qué probabilidad hay de encontrarla en los primeros 20 cm?

<details>
<summary>Soluciones</summary>

1. La de no sacar ninguno es $(5/6)^2 = 25/36$. La de sacar al menos uno, $1 - 25/36 = 11/36 \approx$ **0,31**.
2. $(1/2)^{10} = 1/1024 \approx$ **0,001**.
3. **0,2**.

</details>

### Sesión 2 · Matemáticas: números complejos como flechas (40-45 min)

**Un número cuyo cuadrado es negativo.** Ningún número real elevado al cuadrado da −1. En el siglo XVI, los matemáticos italianos que resolvían ecuaciones de tercer grado se encontraron con raíces de números negativos en mitad de las cuentas, y descubrieron que, si seguían adelante como si existieran, llegaban a soluciones correctas. Se inventó un número, $i$, con $i^2 = -1$. Descartes los llamó, con desprecio, «imaginarios» en 1637, y el nombre se quedó.

**Flechas en un plano.** Un **número complejo** es $z = a + b\,i$, con $a$ y $b$ reales. La mejor forma de pensarlo es como una **flecha** en un plano: $a$ es la coordenada horizontal (la **parte real**) y $b$ la vertical (la **parte imaginaria**). Una flecha también se describe por su longitud y su ángulo:

- el **módulo**, $|z| = \sqrt{a^2 + b^2}$ (Pitágoras),
- la **fase**, el ángulo $\varphi$ que forma con el eje horizontal.

**Sumar y multiplicar.**

- **Sumar** complejos es sumar flechas, punta con cola, como los vectores de la semana 9.
- **Multiplicar** complejos es multiplicar sus longitudes y **sumar sus ángulos**. Multiplicar por $i$ es girar 90°: por eso $i \cdot i = -1$ (dos giros de 90°, media vuelta).

**La fórmula de Euler.** Una flecha de longitud 1 y ángulo $\varphi$ tiene coordenadas $(\cos\varphi, \sin\varphi)$ (semana 13). Leonhard Euler descubrió en 1748 una forma compacta de escribirla:

$$e^{i\varphi} = \cos\varphi + i\sin\varphi.$$

Cualquier complejo es $z = |z|\,e^{i\varphi}$. Y una onda que oscila, $\cos(kx - \omega t)$ (semana 27), es la parte real de una flecha que gira, $e^{i(kx - \omega t)}$. Con $\varphi = \pi$ sale la que se suele considerar la fórmula más bella de las matemáticas: $e^{i\pi} + 1 = 0$.

**Por qué la física cuántica necesita flechas.** En la mecánica cuántica, cada forma posible de que ocurra algo tiene una **amplitud**, que es un número complejo: una flecha. Si un suceso puede ocurrir de dos maneras que no se distinguen, **se suman las flechas**, y la probabilidad es el **cuadrado de la longitud** de la flecha resultante. Dos flechas iguales en la misma dirección suman una flecha el doble de larga: probabilidad cuatro veces mayor. Dos flechas iguales en sentidos opuestos se anulan: probabilidad cero. Es la interferencia de la semana 27, pero con probabilidades.

**Ejercicios**

1. Calcula el módulo de $3 + 4i$.
2. Multiplica $(1 + i)(1 - i)$. ¿Qué sale? Interprétalo con longitudes y ángulos.
3. Suma las flechas $e^{i\cdot0}$ y $e^{i\pi}$. ¿Y $e^{i\cdot0}$ y $e^{i\pi/2}$? Calcula en cada caso el cuadrado del módulo de la suma.

<details>
<summary>Soluciones</summary>

1. $\sqrt{9 + 16} =$ **5**.
2. $1 - i + i - i^2 = 1 + 1 =$ **2**. Cada factor mide $\sqrt{2}$, con ángulos de +45° y −45°: el producto mide 2 con ángulo 0°.
3. $1 + (-1) = 0$: probabilidad **0**. $1 + i$: módulo $\sqrt{2}$, cuadrado **2**, la suma de las dos probabilidades por separado (cuando las fases difieren 90°, no hay interferencia neta).

</details>

### Sesión 3 · Física: partículas que son ondas (40-45 min)

**La luz, en paquetes (1905).** Al iluminar un metal, la luz arranca electrones: es el **efecto fotoeléctrico**. Lo extraño es que la luz roja, por intensa que sea, no arranca ninguno, y la luz ultravioleta, por débil que sea, sí. Einstein lo explicó en 1905: la luz llega en fotones de energía $hf$ (semana 30), y cada electrón necesita un fotón con energía suficiente; muchos fotones flojos no suman. Por esto, no por la relatividad, recibió el Nobel de 1921.

**La materia, en ondas (1924).** El francés Louis de Broglie propuso en su tesis doctoral la idea simétrica: si las ondas de luz se comportan como partículas, quizá las partículas se comportan como ondas, con una longitud de onda

$$\lambda = \frac{h}{p} = \frac{h}{m\,v}.$$

En 1927, Clinton Davisson y Lester Germer en Estados Unidos, y George Paget Thomson en Escocia, hicieron pasar electrones por cristales y obtuvieron patrones de difracción, como los de la luz. Los electrones eran ondas.

**La doble rendija, de uno en uno.** El experimento de Young (semana 27) se ha repetido con electrones, átomos y hasta moléculas de cientos de átomos. En 1989, en Japón, Akira Tonomura y su equipo lo hicieron enviando los electrones **de uno en uno**, con mucho tiempo entre cada uno. Cada electrón llega a la pantalla como una partícula: un punto en un sitio concreto. Pero, a medida que se acumulan miles de puntos, van dibujando las franjas de interferencia. Cada electrón, solo, interfiere consigo mismo: «pasa por las dos rendijas» como una onda y llega como una partícula. Y si se intenta averiguar por cuál de las dos pasa, las franjas desaparecen.

**La función de onda y la regla de Born.** En 1926, Erwin Schrödinger escribió la ecuación que gobierna las ondas de materia. Su solución, la **función de onda** $\psi$, es un número complejo en cada punto. Ese mismo año, Max Born propuso cómo interpretarla: $|\psi|^2$ es la **densidad de probabilidad** de encontrar la partícula en cada sitio. La física cuántica no dice dónde llegará el próximo electrón: dice, con una precisión extraordinaria, cómo se repartirán muchos.

**El principio de incertidumbre (1927).** Werner Heisenberg demostró que no se pueden conocer a la vez, con precisión arbitraria, la posición y el momento (la masa por la velocidad) de una partícula:

$$\Delta x\,\Delta p \geq \frac{\hbar}{2}, \qquad \hbar = \frac{h}{2\pi}.$$

No es un defecto de los instrumentos: una onda muy localizada en el espacio está hecha de muchas longitudes de onda distintas (como las series de Fourier de la semana 27), es decir, de muchos momentos distintos.

**Por qué los niveles de energía son discretos.** Una cuerda de guitarra sujeta por los dos extremos solo puede vibrar con ondas estacionarias que encajen en ella: media longitud de onda, una, una y media... (semana 30). Un electrón atrapado en un átomo es una onda atrapada, y solo puede estar en las ondas estacionarias que «caben» alrededor del núcleo. Cada una tiene una energía distinta: los niveles de Bohr. Para una partícula en una caja de longitud $L$, encajan $\lambda = 2L/n$, y con la fórmula de De Broglie las energías salen

$$E_n = \frac{n^2 h^2}{8 m L^2}, \qquad n = 1, 2, 3, \dots$$

**El principio de exclusión (1925).** Wolfgang Pauli descubrió que dos electrones no pueden ocupar el mismo estado cuántico. Por eso los electrones de un átomo no se amontonan en el nivel más bajo, sino que van llenando niveles cada vez más altos: de ahí sale la tabla periódica y toda la química. Y de ahí sale también la presión que sostiene a las enanas blancas (semana 36): los electrones, apretados, no pueden ocupar los mismos estados y se resisten.

**Y está en todas partes.** La mecánica cuántica es la teoría más precisa jamás comprobada, y sin ella no existirían los transistores (ni los ordenadores ni los móviles), los láseres, los LED ni la resonancia magnética. Qué significa exactamente, qué «es» la función de onda antes de medir, sigue siendo objeto de debate entre físicos y filósofos, con varias interpretaciones que dan las mismas predicciones.

:::note[De dónde viene la palabra]
**Imaginario**, como se ha dicho, viene de Descartes, que lo usó como despectivo en *La Géométrie* (1637). **Incertidumbre** viene de *incertus*, «no decidido», de *cernere*, «separar, distinguir». **Función de onda**: *función* viene de *functio*, «desempeño» (semana 4). El nombre de **ecuación de Schrödinger** se lo dieron otros; él la llamó «ecuación de ondas».
:::

**Qué hacer**

1. Calcula la longitud de onda de De Broglie de un electrón ($9{,}11\times10^{-31}$ kg) a $10^6$ m/s. Compárala con el tamaño de un átomo (0,1 nm).
2. Calcula la de una pelota de tenis de 58 g a 50 m/s. ¿Por qué no vemos a las pelotas difractarse?
3. Explica con flechas por qué, en la doble rendija, hay puntos de la pantalla donde no llega nunca ningún electrón.

### Sesión 4 · Astronomía y observación: las líneas prohibidas y el «nebulio» (30-45 min)

**Un elemento que no existía.** En 1864, el astrónomo inglés William Huggins apuntó un espectroscopio a la nebulosa del Ojo de Gato, una nebulosa planetaria en Draco (semana 36). Esperaba un espectro continuo, de estrellas sin resolver; vio líneas brillantes, como las de un gas. Una de las más intensas, verde, a 500,7 nm, no coincidía con ningún elemento conocido. Como había pasado con el helio en el Sol (semana 32), se propuso un elemento nuevo, el **nebulio**.

**Mecánica cuántica.** El nebulio no existe. En 1927, el estadounidense Ira Bowen demostró, con la nueva mecánica cuántica, que esas líneas son del oxígeno ionizado dos veces (O²⁺, que los astrónomos escriben [O III]) en transiciones **prohibidas**: saltos entre niveles que las reglas cuánticas hacen tan improbables que, en la Tierra, el átomo choca con otro y pierde la energía antes de emitir. En el gas enrarecido de una nebulosa, donde un átomo puede pasar mucho tiempo sin chocar, hay tiempo de sobra y la línea brilla. Es la misma línea de [O III] que usaste en el cuaderno de la semana 41, y el verde de las auroras (semana 29) es otra línea prohibida, la del oxígeno neutro a 557,7 nm.

**Qué puedes observar.**

- **El espectroscopio casero** de la semana 32: vuelve a mirar un fluorescente, una farola o un letrero de neón, y piensa que cada línea es un salto de un electrón entre dos ondas estacionarias de un átomo.
- **La nebulosa de Orión (M42)**, con los prismáticos: se ve gris, porque el ojo de noche apenas distingue colores (semana 31). Con un telescopio de cierta abertura, muchos observadores la ven verdosa: es la luz de [O III], la línea del nebulio, más intensa para el ojo que el rojo del hidrógeno.
- **La nebulosa Dumbbell (M27)** y la **del Anillo (M57)** (semana 36): con un telescopio pequeño también se aprecia un tono verdoso. Con prismáticos, solo su forma.

**La línea de 21 cm.** Una transición cuántica más: el electrón y el protón del átomo de hidrógeno tienen una propiedad cuántica, el **espín**, que puede estar «alineado» o «desalineado». El salto entre las dos situaciones emite una onda de radio de 21 cm (semana 30). Es tan improbable que un átomo tarda de media unos diez millones de años en hacerlo, pero hay tanto hidrógeno en la galaxia que la línea es intensa. Con ella se han hecho los mapas de los brazos espirales de la Vía Láctea y las curvas de rotación de la semana 43.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 46:

- juega con números complejos en Python: suma, producto, módulo, fase y la fórmula de Euler,
- calcula el patrón de la doble rendija sumando las amplitudes complejas de los dos caminos,
- simula la llegada de electrones de uno en uno y ve aparecer las franjas, y lo compara con lo que pasa si se sabe por qué rendija pasa cada uno,
- dibuja los niveles de energía y las funciones de onda de una partícula en una caja.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-46.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-46.ipynb)

## Qué has aprendido

- **La respuesta.** La mecánica cuántica es la física de lo muy pequeño. La luz llega en paquetes y la materia se comporta como una onda. Esas ondas, descritas por números complejos, dan la probabilidad de encontrar una partícula en cada sitio: se suman las amplitudes y se eleva al cuadrado. Los niveles de energía de los átomos son las ondas estacionarias que caben en ellos.
- **En el cielo.** Las líneas espectrales, las líneas prohibidas de las nebulosas, la línea de 21 cm del hidrógeno, la fusión en el Sol y la presión de las enanas blancas son física cuántica.
- **Las herramientas.** Las reglas de la probabilidad, el valor esperado, los números complejos como flechas, la fórmula de Euler y la idea de amplitud de probabilidad.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**El tamaño del átomo, con el principio de incertidumbre.** ¿Por qué el electrón del hidrógeno no cae sobre el protón, si se atraen? Según la física clásica, debería caer en espiral emitiendo luz, en una fracción de segundo. La física cuántica lo impide, y se puede ver con una estimación.

Si el electrón está confinado en una región de tamaño $r$, su momento tiene una incertidumbre de al menos $\hbar/r$ (más o menos), y por tanto una energía cinética de al menos

$$K \approx \frac{p^2}{2m} \approx \frac{\hbar^2}{2 m r^2}.$$

Cuanto más lo encierras, más energía cinética tiene. La energía potencial eléctrica, en cambio, es $U = -ke^2/r$ (semana 32): más negativa cuanto más cerca. La energía total,

$$E(r) \approx \frac{\hbar^2}{2 m r^2} - \frac{k e^2}{r},$$

tiene un **mínimo**. Derivando e igualando a cero (semana 10):

$$\frac{dE}{dr} = -\frac{\hbar^2}{m r^3} + \frac{k e^2}{r^2} = 0 \quad\Longrightarrow\quad r = \frac{\hbar^2}{m k e^2} = a_0 \approx 0{,}053\ \text{nm}.$$

¡El radio de Bohr de la semana 32! Y sustituyendo, $E(a_0) = -\frac{k e^2}{2 a_0} \approx -13{,}6$ eV, la energía del nivel fundamental. El átomo tiene el tamaño que tiene por un equilibrio entre la atracción eléctrica, que quiere encoger al electrón, y el principio de incertidumbre, que lo impide. Sin la mecánica cuántica, la materia no sería estable.

**Ejercicios**

1. Calcula $a_0 = \hbar^2/(m k e^2)$ con $\hbar = 1{,}055\times10^{-34}$ J·s, $m = 9{,}11\times10^{-31}$ kg, $k = 8{,}99\times10^9$ y $e = 1{,}602\times10^{-19}$ C.
2. Calcula $E(a_0) = -ke^2/(2a_0)$ en julios y en electronvoltios.
3. Haz la misma estimación para un electrón confinado en un núcleo ($r = 10^{-15}$ m): ¿qué energía cinética tendría, en MeV? ¿Por qué eso indica que en los núcleos no hay electrones?

<details>
<summary>Soluciones</summary>

1. $(1{,}055\times10^{-34})^2/(9{,}11\times10^{-31} \cdot 8{,}99\times10^9 \cdot (1{,}602\times10^{-19})^2) \approx 5{,}3\times10^{-11}$ m $=$ **0,053 nm**.
2. $8{,}99\times10^9 \cdot (1{,}602\times10^{-19})^2/(2 \cdot 5{,}3\times10^{-11}) \approx 2{,}18\times10^{-18}$ J $\approx$ **13,6 eV** (con signo menos).
3. Con la fórmula de la energía cinética de Newton sale un disparate, unos $6\times10^{-9}$ J (decenas de miles de MeV), muchísimo más que la energía en reposo del electrón, 0,51 MeV: hay que usar la relatividad (semana 44), con $E \approx pc \approx \hbar c/r \approx 3\times10^{-11}$ J, unos **200 MeV**. Ninguna fuerza del núcleo podría retener un electrón con esa energía.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [6.4 Modelo de Bohr del átomo de hidrógeno, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/6-4-modelo-de-bohr-del-atomo-de-hidrogeno). Español; el puente entre las líneas espectrales y la mecánica cuántica. Verificado el 20 de noviembre de 2026.
2. [8.1 El átomo de hidrógeno, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/8-1-el-atomo-de-hidrogeno). Español; el modelo de Schrödinger frente al de Bohr y los números cuánticos. Verificado el 20 de noviembre de 2026.
3. [6.1 Radiación de cuerpo negro, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/6-1-radiacion-de-cuerpo-negro). Español; el capítulo 6 entero, «Fotones y ondas de materia», sigue con el efecto fotoeléctrico y la dualidad onda-partícula. Verificado el 20 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
