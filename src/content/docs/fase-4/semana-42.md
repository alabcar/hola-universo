---
title: "Semana 42 · ¿Qué pasó al principio?"
description: "Fase 4 · El universo grande. Distribuciones de probabilidad, la campana de Gauss y el teorema central del límite; el Big Bang, la nucleosíntesis primordial, la recombinación y el fondo cósmico de microondas; COBE, WMAP y Planck; y la paradoja de la noche oscura."
sidebar:
  order: 42
  label: "42. ¿Qué pasó al principio?"
---

## La pregunta del cielo

Si las galaxias se alejan unas de otras (semana 41), en el pasado estaban más juntas. Y si retrocedes lo suficiente, todo lo que hoy forma el universo observable estaba comprimido en un estado muchísimo más denso y caliente. ¿Hay forma de comprobarlo? ¿Queda alguna huella de aquella época?

Queda, y está por todas partes. En 1965, dos radioastrónomos de los laboratorios Bell en Nueva Jersey, Arno Penzias y Robert Wilson, intentaban eliminar un ruido molesto de su antena: un siseo débil que llegaba igual de todas las direcciones, de día y de noche, en cualquier época del año. Revisaron los cables, apuntaron a todas partes y hasta limpiaron los excrementos de las palomas que anidaban en la antena. El ruido seguía ahí. Era la luz más antigua del universo: el resplandor de cuando todo el cosmos era una bola de gas incandescente, estirado por la expansión hasta las microondas. Esta semana viajas al principio, y aprendes la estadística que hace falta para leer ese resplandor.

:::note[De dónde viene la palabra]
**Big Bang**, «gran estallido», lo dijo por primera vez el astrónomo británico Fred Hoyle en un programa de radio de la BBC en 1949, y no precisamente como elogio: él defendía la teoría rival, la del universo estacionario. El nombre es engañoso, porque no fue una explosión en un punto del espacio, sino una expansión de todo el espacio. **Primordial** viene de *primordium*, «el principio», de *primus*, «primero», y *ordiri*, «empezar a tejer».
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: distribuciones y la campana de Gauss (40-45 min)

**De un histograma a una distribución.** En la semana 39 dibujaste histogramas. Si tienes muchísimos datos y haces los intervalos cada vez más estrechos, el contorno del histograma (dividido por el total para que el área sea 1) se convierte en una curva suave: la **función de densidad de probabilidad**. El área bajo la curva entre dos valores es la probabilidad de que un dato caiga entre ellos.

**La campana de Gauss.** La distribución más importante es la **normal** o **gaussiana**:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\;e^{-\frac{(x-\mu)^2}{2\sigma^2}},$$

una campana simétrica centrada en la media $\mu$, con una anchura dada por la desviación típica $\sigma$. El factor de delante hace que el área total sea 1. Una regla para recordar:

- entre $\mu - \sigma$ y $\mu + \sigma$ cae el **68 %** de los datos,
- entre $\mu - 2\sigma$ y $\mu + 2\sigma$, el **95 %**,
- entre $\mu - 3\sigma$ y $\mu + 3\sigma$, el **99,7 %**.

Por eso, en la semana 41, una diferencia de 5σ entre dos medidas era tan llamativa: por puro azar, ocurre menos de una vez en un millón.

**Por qué aparece en todas partes.** El **teorema central del límite** dice que, si sumas muchas cantidades aleatorias independientes, sea cual sea su distribución, la suma tiende a una campana de Gauss. Un solo dado da una distribución plana (cada número tiene la misma probabilidad); la suma de dos dados ya es un triángulo; la de diez dados es casi una campana perfecta. Los errores de medida, que son la suma de muchas pequeñas perturbaciones, suelen ser gaussianos por eso. Y las pequeñas variaciones de temperatura del fondo cósmico, también.

**Ejercicios**

1. Las alturas de un grupo de adultos siguen una campana con $\mu = 170$ cm y $\sigma = 8$ cm. ¿Qué porcentaje mide más de 186 cm?
2. Una medida da $2{,}7255 \pm 0{,}0006$ K. ¿Entre qué valores está el valor verdadero con un 95 % de probabilidad?
3. ¿Qué probabilidad tiene un dato gaussiano de caer a más de 3σ de la media, por cualquiera de los dos lados?

<details>
<summary>Soluciones</summary>

1. 186 es $\mu + 2\sigma$. Fuera de $\pm 2\sigma$ queda el 5 %, la mitad por cada lado: **2,5 %**.
2. $\pm 2\sigma$: entre **2,7243 y 2,7267 K**.
3. $100 - 99{,}7 =$ **0,3 %**, unas 3 veces de cada mil.

</details>

### Sesión 2 · Matemáticas: un mapa hecho de ondas (35-40 min)

**Las manchas del fondo cósmico.** El fondo cósmico tiene casi la misma temperatura en todas direcciones: 2,7255 K. Pero no exactamente: hay manchas un poquito más calientes y un poquito más frías, de unas decenas de millonésimas de grado. Si haces un histograma de las temperaturas de todos los puntos del mapa (restando la media), sale una campana de Gauss casi perfecta, con una desviación típica de unas decenas de microkelvin. Es una variación de una parte en cien mil: como si la superficie de una piscina olímpica tuviera olas de una décima de milímetro.

**¿Qué tamaño tienen las manchas?** La campana dice cuánto varía la temperatura, pero no si las manchas son grandes o pequeñas. Para eso se usa la idea de Fourier de la semana 27: cualquier mapa se puede descomponer en una suma de ondas de distintos tamaños, y se mide cuánta variación aporta cada tamaño. Esa lista es el **espectro de potencias** del mapa. En el del fondo cósmico, el pico más alto está en manchas de **alrededor de un grado** (dos Lunas llenas).

**Por qué un grado.** Las manchas son ondas de sonido que recorrían el gas caliente del universo primitivo, y el tamaño de la mayor que tuvo tiempo de formarse antes de que el universo se volviera transparente se puede calcular con física conocida. El ángulo con el que vemos hoy ese tamaño depende de la **geometría** del universo, como un objeto de tamaño conocido visto a través de una lupa o de un cristal plano. Que salga un grado indica que el universo es **plano** (sus triángulos suman 180°, semana 45), o muy cerca de serlo.

**Ejercicios**

1. Si la temperatura media es 2,7255 K y las variaciones típicas son de 30 µK, ¿cuál es la variación relativa?
2. ¿A cuántos grados de temperatura media equivaldría esa variación relativa en una habitación a 20 °C (293 K)?
3. Un mapa de todo el cielo tiene $4\pi$ estereorradianes, unos 41 000 grados cuadrados. ¿Cuántas manchas de 1° × 1° caben, más o menos?

<details>
<summary>Soluciones</summary>

1. $30\times10^{-6}/2{,}7255 \approx$ **1,1 × 10⁻⁵**, una cienmilésima.
2. $293 \cdot 1{,}1\times10^{-5} \approx$ **0,003 grados**: tres milésimas.
3. Unas **41 000**: el fondo cósmico es un mapa con decenas de miles de «píxeles» independientes de información.

</details>

### Sesión 3 · Física: los primeros 380 000 años (40-45 min)

**El universo caliente.** En 1948, George Gamow y sus colaboradores Ralph Alpher y Robert Herman calcularon qué habría pasado si el universo hubiera empezado muy denso y caliente. La temperatura de la radiación baja al expandirse el universo: las longitudes de onda se estiran con el factor de escala (semana 41), y por la ley de Wien (semana 31), la temperatura va como $T \propto 1 + z$. Hacia atrás, sin límite aparente.

**Los primeros minutos.** Durante los primeros minutos, el universo era un reactor nuclear a mil millones de grados. Los protones y neutrones se fundieron en núcleos ligeros hasta que la expansión los enfrió demasiado para seguir: es la **nucleosíntesis primordial**. El cálculo predice que, en masa, debía quedar un **75 % de hidrógeno y un 25 % de helio**, con trazas de deuterio y litio. Es exactamente la composición del gas más primitivo que se observa en el universo, y la del Sol corregida por lo que han fabricado las estrellas (semana 32). Es una de las grandes pruebas del Big Bang.

**El universo se vuelve transparente.** Durante unos cientos de miles de años, el universo era un gas de núcleos y electrones sueltos, tan caliente como el interior de una estrella. La luz no podía viajar: chocaba una y otra vez con los electrones libres, como en el interior del Sol (semana 34), y el universo era opaco, como una niebla luminosa. Cuando la temperatura bajó a unos **3000 K**, unos **380 000 años** después del principio, los electrones se unieron a los núcleos para formar átomos neutros (los físicos llaman a esto, impropiamente, **recombinación**), y la luz quedó libre. Desde entonces viaja sin chocar.

Esa luz salió de todas partes a la vez, como el resplandor de un cuerpo negro a 3000 K. Pero desde entonces el universo se ha expandido unas 1100 veces, así que nos llega estirada a microondas, como un cuerpo negro a $3000/1100 \approx 2{,}7$ K: el **fondo cósmico de microondas**. Cuando lo miras, ves la «superficie» de aquella niebla, como cuando ves la superficie de una nube.

**Cómo se ha medido.**

- **1965**: Penzias y Wilson lo detectan por accidente. Muy cerca, en Princeton, el grupo de Robert Dicke lo estaba buscando a propósito; al enterarse, Dicke comentó a su equipo: «Chicos, se nos han adelantado». Penzias y Wilson recibieron el Nobel de Física en 1978.
- **1990**: el satélite **COBE** de la NASA mide su espectro y resulta ser el cuerpo negro más perfecto jamás medido en la naturaleza, con una temperatura de 2,725 K (hoy, 2,7255). En 1992 detecta por primera vez las pequeñas manchas. Nobel de Física de 2006 para John Mather y George Smoot.
- **2001-2010**: **WMAP** (NASA) hace mapas más finos.
- **2009-2013**: **Planck** (ESA) hace el mapa definitivo, con resultados finales en 2018. De él salen la edad del universo (13 800 millones de años), su composición (semana 43) y su geometría plana.

**Las manchas son las semillas.** Las zonas un poco más densas del universo primitivo, que vemos como manchas en el fondo cósmico, fueron atrayendo más materia por su gravedad durante cientos de millones de años, hasta formar las primeras estrellas y galaxias. Las manchas de una cienmilésima son las semillas de todas las estructuras del universo, incluida la Vía Láctea.

**El dipolo: nos movemos.** El fondo cósmico es un poco más caliente en una dirección del cielo (hacia la constelación de Leo y la Copa) y un poco más frío en la opuesta, unos 3,4 milésimas de grado. Es el efecto Doppler (semana 41) de nuestro movimiento respecto al fondo: el Sol se mueve a unos 370 km/s respecto a él. Hay, por tanto, un sistema de referencia en el que el universo «está quieto».

:::note[De dónde viene la palabra]
**Anisotropía** es la palabra técnica para las manchas del fondo cósmico: del griego *an-*, «no», *ísos*, «igual», y *trópos*, «dirección»: que no es igual en todas las direcciones. **Nucleosíntesis** une *núcleo* (semana 34) y el griego *sýnthesis*, «composición»: la fabricación de núcleos.
:::

**Qué hacer**

1. ¿A qué temperatura estaba el fondo cósmico cuando las galaxias con $z = 3$ emitieron su luz? ¿Y en la recombinación, con $z = 1100$?
2. Con la ley de Wien, ¿dónde estaba el máximo de la radiación en la recombinación? ¿Qué color tendría?
3. Calcula el dipolo: $\Delta T = T\,v/c$ con $v = 370$ km/s.

### Sesión 4 · Astronomía y observación: ¿por qué es oscura la noche? (30-45 min)

**La paradoja de Olbers.** Sal una noche y hazte una pregunta que parece tonta: ¿por qué el cielo nocturno es oscuro? Si el universo fuera infinito, eterno e inmutable, y estuviera lleno de estrellas por todas partes, en cualquier dirección que miraras tu mirada acabaría tropezando con la superficie de una estrella, como en un bosque muy grande cualquier línea de visión acaba en un tronco. El cielo entero debería brillar como la superficie del Sol. La pregunta la planteó Kepler en 1610, y la popularizó el médico alemán Heinrich Olbers en 1823.

**La respuesta** está en esta fase. El universo tiene una **edad finita**: la luz de las estrellas más lejanas no ha tenido tiempo de llegar, y las estrellas no han existido siempre. Y el universo **se expande**: la luz de lo muy lejano llega debilitada y desplazada al rojo. Curiosamente, el primero en intuir la respuesta correcta fue el escritor Edgar Allan Poe, en su ensayo *Eureka* de 1848.

Pero la noche no es del todo oscura: en microondas, el cielo entero brilla de forma uniforme a 2,7 K. Si tus ojos vieran microondas, la noche sería un resplandor tenue sin una sola sombra. El cielo **es** el resplandor de una superficie caliente que nos rodea por todas partes, como pedía la paradoja, pero tan estirado por la expansión que ya no se ve.

**Mirarlo de otra manera.** Esta noche, mira una zona oscura del cielo, entre las estrellas, por ejemplo hacia el polo norte galáctico o fuera de la Vía Láctea (semana 38). Piensa que en esa dirección hay galaxias a miles de millones de años luz y, detrás de ellas, el fondo cósmico, la luz más antigua que puede verse.

**El fondo en la televisión.** En los televisores antiguos, de antena y tubo, cuando no había señal, la pantalla se llenaba de «nieve». Alrededor de un 1 % de esa nieve eran fotones del fondo cósmico captados por la antena.

**El mapa de Planck.** En ESASky (semana 30) puedes ver el cielo entero tal como lo vio Planck. Busca el mapa en microondas: la banda de la Vía Láctea molesta (emite en esas frecuencias), pero fuera de ella aparece el moteado del fondo cósmico.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 42:

- comprueba el teorema central del límite sumando dados y la regla del 68-95-99,7,
- dibuja el espectro del fondo cósmico a 2,7255 K y ajusta la temperatura a unos datos **simulados** con la precisión de COBE,
- calcula la temperatura del fondo en el pasado y dónde estaba su máximo,
- genera un mapa **simulado** de manchas gaussianas con un tamaño típico de un grado, comprueba que su histograma es una campana y añade el dipolo de nuestro movimiento,
- en el apartado opcional, calcula cuántos fotones del fondo cósmico hay en cada centímetro cúbico.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-42.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-42.ipynb)

## Qué has aprendido

- **La respuesta.** El universo empezó hace unos 13 800 millones de años en un estado muy denso y caliente, y desde entonces se expande y se enfría. En los primeros minutos se formaron el hidrógeno y el helio; unos 380 000 años después se volvió transparente, y esa luz nos llega hoy como el fondo cósmico de microondas, un cuerpo negro casi perfecto a 2,7 K.
- **Las semillas.** Las pequeñísimas variaciones del fondo cósmico, de una cienmilésima, son el origen de todas las galaxias.
- **Las herramientas.** Las distribuciones de probabilidad, la campana de Gauss, la regla del 68-95-99,7, el teorema central del límite y la idea de descomponer un mapa en ondas de distintos tamaños.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**Por qué un cuerpo negro sigue siéndolo al expandirse.** Imagina el universo lleno de radiación de cuerpo negro a temperatura $T_1$. El universo se expande un factor $s$: todas las longitudes de onda se multiplican por $s$, y el volumen, por $s^3$. ¿Sigue siendo un cuerpo negro?

La densidad de fotones con longitud de onda entre $\lambda$ y $\lambda + d\lambda$ en un cuerpo negro es proporcional a

$$\frac{1}{\lambda^4}\,\frac{1}{e^{hc/(\lambda k_B T)} - 1}\,d\lambda.$$

Tras la expansión, los fotones que tenían longitud de onda $\lambda$ tienen ahora $\lambda' = s\lambda$ (y el intervalo, $d\lambda' = s\,d\lambda$), y están repartidos en un volumen $s^3$ veces mayor. La nueva densidad es la vieja dividida por $s^3$:

$$\frac{1}{s^3}\cdot\frac{1}{(\lambda'/s)^4}\,\frac{1}{e^{hc\,s/(\lambda' k_B T_1)} - 1}\,\frac{d\lambda'}{s} = \frac{1}{\lambda'^4}\,\frac{1}{e^{hc/(\lambda' k_B T_1/s)} - 1}\,d\lambda'.$$

Las potencias de $s$ se cancelan exactamente, y queda la misma fórmula con una temperatura $T_2 = T_1/s$. **Un cuerpo negro que se expande sigue siendo un cuerpo negro**, más frío. Por eso el fondo cósmico conserva su forma perfecta de curva de Planck después de que el universo haya crecido mil veces.

**Cuántos fotones hay.** Integrando la densidad de fotones en todas las longitudes de onda (con el mismo cambio de variable de la semana 31), sale

$$n_\gamma = 16\pi\,\zeta(3)\left(\frac{k_B T}{h c}\right)^3 \approx 20{,}3\,T^3\ \text{fotones/cm}^3,$$

con $T$ en kelvin, donde $\zeta(3) \approx 1{,}202$ es un número que aparece en esa integral. Para $T = 2{,}7255$ K, unos 411 fotones por centímetro cúbico. Hay unos mil millones de fotones del fondo cósmico por cada protón del universo.

**Ejercicios**

1. Comprueba que $20{,}3 \cdot 2{,}7255^3 \approx 411$.
2. ¿Cuántos fotones del fondo cósmico hay en tu habitación (unos 30 m³)?
3. ¿Cuántos fotones por centímetro cúbico había en la recombinación, con $z = 1100$? (Pista: $T$ se multiplica por $1 + z$.)

<details>
<summary>Soluciones</summary>

1. $2{,}7255^3 \approx 20{,}25$; $20{,}3 \cdot 20{,}25 \approx$ **411**.
2. $30\ \text{m}^3 = 3\times10^7\ \text{cm}^3$; $411 \cdot 3\times10^7 \approx$ **1,2 × 10¹⁰ fotones**: doce mil millones.
3. $411 \cdot 1101^3 \approx$ **5,5 × 10¹¹ por cm³**.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Capítulo 29, El Big Bang, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/29%3A_El_Big_Bang). Español; el universo primitivo, la nucleosíntesis, el fondo cósmico y sus anisotropías. Verificado el 20 de noviembre de 2026.
2. [Explora el cosmos con ESASky (ESA)](https://www.esa.int/Space_in_Member_States/Spain/Explora_el_cosmos_con_ESASky). Español; desde el portal se puede ver el cielo de Planck. Verificado el 20 de noviembre de 2026.
3. [6.1 Radiación de cuerpo negro, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/6-1-radiacion-de-cuerpo-negro). Español; para repasar la curva de Planck. Verificado el 20 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
