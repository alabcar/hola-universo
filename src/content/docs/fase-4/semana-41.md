---
title: "Semana 41 · ¿Se está expandiendo el universo?"
description: "Fase 4 · El universo grande. Errores aleatorios y sistemáticos, barras de error y ajustes ponderados, el efecto Doppler y el corrimiento al rojo, Slipher, Lemaître y Hubble, la ley de Hubble-Lemaître, la expansión del espacio, la edad del universo, la tensión de Hubble y galaxias para ver con prismáticos."
sidebar:
  order: 41
  label: "41. ¿Se está expandiendo el universo?"
---

## La pregunta del cielo

Entre 1912 y 1917, el astrónomo estadounidense Vesto Slipher consiguió algo muy difícil para la época: fotografiar los espectros de las nebulosas espirales, tan débiles que cada placa necesitaba noches enteras de exposición. Encontró que sus líneas espectrales estaban desplazadas, casi todas hacia el rojo. Según el efecto Doppler, eso significaba que se alejaban, algunas a más de 1000 km/s, velocidades enormes para cualquier objeto conocido entonces.

Cuando Hubble demostró que esas nebulosas eran galaxias lejanas (semana 40), alguien tenía que unir las dos cosas. En 1927, el sacerdote y físico belga Georges Lemaître, y en 1929, de forma independiente y con más datos, Hubble, encontraron que **cuanto más lejos está una galaxia, más deprisa se aleja**. El universo se está expandiendo. Esta semana entiendes qué significa eso, cómo se mide y por qué de ahí sale la edad del universo.

:::note[De dónde viene la palabra]
**Cosmos** viene del griego *kósmos*, «orden, adorno»: Pitágoras habría sido el primero en llamar así al universo, por su orden y su belleza (de la misma raíz es *cosmética*, el arte de adornar). **Cosmología** es el estudio del cosmos como un todo. **Expansión** viene de *expandere*, «desplegar, extender». El **efecto Doppler** lleva el nombre del físico austriaco Christian Doppler, que lo propuso en 1842.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: errores, barras de error y ajustes ponderados (40-45 min)

**Dos tipos de error.** Toda medida tiene incertidumbre, y conviene distinguir dos clases:

- Los **errores aleatorios** cambian de una medida a otra, unas veces por arriba y otras por abajo. Se reducen repitiendo y promediando: el error de una media de $N$ medidas independientes es $\sigma/\sqrt{N}$ (semana 40).
- Los **errores sistemáticos** desplazan todas las medidas en el mismo sentido: un instrumento mal calibrado, una corrección olvidada (como el polvo, semana 38, o la calibración de las cefeidas de Hubble, semana 40). No se reducen promediando. Son los más peligrosos, porque no se ven en los datos.

**Barras de error.** En una gráfica, cada punto se dibuja con una **barra de error** que indica su incertidumbre, normalmente $\pm 1\sigma$: el intervalo en el que, si el error es gaussiano, está el valor verdadero con una probabilidad de unos dos tercios (semana 42). Dos medidas cuyas barras se solapan ampliamente son compatibles; si están separadas varias $\sigma$, hay un problema.

**Ajustar con errores distintos.** Si unos puntos se conocen mejor que otros, no es justo que cuenten igual en el ajuste. En lugar de minimizar la suma de los cuadrados de los residuos, se minimiza la suma de los cuadrados de los residuos **divididos por sus errores**:

$$\chi^2 = \sum_{i=1}^{N}\left(\frac{y_i - (a + b\,x_i)}{\sigma_i}\right)^2.$$

Es el **ajuste ponderado**, y la cantidad se llama **chi cuadrado** ($\chi$ es la letra griega ji). Los puntos con error pequeño pesan más. Además, $\chi^2$ sirve para juzgar el ajuste: si el modelo es bueno y los errores están bien estimados, cada término vale, de media, alrededor de 1, y $\chi^2$ sale parecido al número de puntos menos el de parámetros ajustados. Si sale mucho mayor, o el modelo falla o los errores están subestimados.

**Ejercicios**

1. Mides la distancia a una galaxia con cinco cefeidas, y cada una tiene un error del 10 %. ¿Cuál es el error de la media? ¿Y si el error de calibración de la ley de Leavitt es del 3 %, sistemático?
2. Dos medidas de una misma constante dan $67{,}4 \pm 0{,}5$ y $73{,}0 \pm 1{,}0$. ¿A cuántas desviaciones típicas están una de otra? (La incertidumbre de la diferencia es $\sqrt{\sigma_1^2 + \sigma_2^2}$.)
3. Ajustas una recta a 12 puntos y obtienes $\chi^2 = 31$. ¿Qué te dice?

<details>
<summary>Soluciones</summary>

1. Aleatorio: $10/\sqrt{5} \approx 4{,}5$ %. El sistemático no baja: el total es aproximadamente $\sqrt{4{,}5^2 + 3^2} \approx$ **5,4 %**.
2. Diferencia: 5,6; incertidumbre: $\sqrt{0{,}25 + 1} \approx 1{,}12$. Están a unas **5 desviaciones típicas**: muy improbable por azar. Es la «tensión de Hubble» de la sesión 3.
3. Con 12 puntos y 2 parámetros esperarías $\chi^2 \approx 10$. 31 es unas tres veces más: o la recta no describe bien los datos, o los errores son mayores de lo que se ha dicho.

</details>

### Sesión 2 · Matemáticas: el corrimiento al rojo (35-40 min)

**El efecto Doppler.** Cuando una ambulancia se acerca, su sirena suena más aguda; cuando se aleja, más grave. Las crestas de las ondas que emite mientras se acerca salen cada vez más cerca de ti, y te llegan más juntas: más frecuencia. Al alejarse, más separadas. En 1845, el holandés Christophorus Buys Ballot lo comprobó con trompetistas tocando una nota fija en un tren en marcha y músicos con buen oído junto a la vía.

Con la luz pasa lo mismo. Si una fuente se aleja a una velocidad $v$ pequeña comparada con $c$, la longitud de onda que recibes es un poco mayor que la emitida:

$$\frac{\lambda_\text{obs} - \lambda_\text{emi}}{\lambda_\text{emi}} = \frac{v}{c}.$$

**El corrimiento al rojo.** Los astrónomos llaman $z$ a ese cociente:

$$z = \frac{\lambda_\text{obs} - \lambda_\text{emi}}{\lambda_\text{emi}}, \qquad 1 + z = \frac{\lambda_\text{obs}}{\lambda_\text{emi}}.$$

Si $z > 0$, la luz llega desplazada hacia el rojo (la fuente se aleja); si $z < 0$, hacia el azul (se acerca). Para $z$ pequeño, $v \approx c\,z$. Lo bueno de $z$ es que **todas** las líneas de un espectro se desplazan en el mismo factor $1 + z$, así que basta identificar un patrón conocido, como la serie de Balmer (semana 32), para medirlo.

**Ejercicios**

1. La línea H-alfa (656,3 nm) de una galaxia se ve en 669,4 nm. ¿Cuánto vale $z$? ¿A qué velocidad se aleja?
2. Andrómeda tiene $z \approx -0{,}001$. ¿Se acerca o se aleja? ¿A qué velocidad?
3. Una galaxia tiene $z = 0{,}5$. ¿Dónde aparecerá su línea H-beta (486,1 nm)? ¿La verías todavía en el visible?

<details>
<summary>Soluciones</summary>

1. $z = 13{,}1/656{,}3 \approx$ **0,020**; $v \approx 0{,}020 \cdot 300\,000 \approx$ **6000 km/s**.
2. **Se acerca**, a unos **300 km/s** respecto al Sol (en parte es el movimiento del propio Sol alrededor de la galaxia; respecto a la Vía Láctea, unos 110 km/s).
3. $486{,}1 \cdot 1{,}5 \approx$ **729 nm**: en el rojo extremo, casi en el infrarrojo.

</details>

### Sesión 3 · Física: la expansión del universo (40-45 min)

**La ley de Hubble-Lemaître.** Si dibujas la velocidad de alejamiento de las galaxias frente a su distancia, los puntos se alinean en una recta que pasa por el origen:

$$v = H_0\,d.$$

La pendiente, $H_0$, es la **constante de Hubble**. Se mide en kilómetros por segundo por megapársec (km/s/Mpc): cuántos km/s más deprisa se aleja una galaxia por cada millón de pársecs más lejos que está. Lemaître dedujo la relación de la teoría de Einstein en 1927 y la estimó con los datos de Slipher y Hubble; Hubble la estableció con sus propios datos en 1929. En 2018, la Unión Astronómica Internacional recomendó llamarla **ley de Hubble-Lemaître** para reconocer a los dos.

El primer valor de Hubble, unos 500 km/s/Mpc, era unas siete veces demasiado grande, por el mismo error de calibración de las cefeidas que le hizo subestimar la distancia a Andrómeda (semana 40). Hoy el valor está alrededor de **70 km/s/Mpc**.

**No es que las galaxias huyan de nosotros.** La ley no dice que estemos en el centro de nada. Imagina un bizcocho con pasas que sube en el horno: todas las pasas se separan unas de otras, y desde cualquier pasa, las demás se alejan más deprisa cuanto más lejos están. Cualquier observador en cualquier galaxia ve la misma ley. Lo que se expande es el **espacio** entre las galaxias (las galaxias mismas, y los átomos, los planetas y las personas, no se expanden: los mantiene unidos su propia gravedad o sus fuerzas eléctricas).

**El corrimiento cosmológico.** Por eso, el corrimiento al rojo de las galaxias lejanas no es exactamente un efecto Doppler: la longitud de onda de la luz se **estira** con el espacio mientras viaja. Si el universo era, cuando salió la luz, un factor $1 + z$ más pequeño que hoy, la luz llega con su longitud de onda multiplicada por $1 + z$. Por eso hay galaxias con $z$ mayor que 1, incluso con $z$ mayor que 14 (observadas por el telescopio James Webb), sin que nada viaje más deprisa que la luz.

**La edad del universo.** Si las galaxias se han alejado siempre a la misma velocidad, el tiempo que llevan separándose es la distancia entre la velocidad: $t = d/v = 1/H_0$. Es el **tiempo de Hubble**. Con $H_0 = 70$ km/s/Mpc:

$$\frac{1}{H_0} = \frac{3{,}086\times10^{19}\ \text{km}}{70\ \text{km/s}} \approx 4{,}4\times10^{17}\ \text{s} \approx 14\,000\ \text{millones de años}.$$

La expansión no ha ido siempre a la misma velocidad (se frenó al principio y ahora se acelera, semana 43), pero por casualidad la edad calculada con los modelos completos, unos **13 800 millones de años**, está muy cerca.

**La tensión de Hubble.** Hay dos maneras de medir $H_0$. Una, con la escalera de distancias (paralajes, cefeidas, supernovas de tipo Ia) en el universo cercano: el equipo SH0ES obtuvo en 2022 unos $73{,}0 \pm 1{,}0$ km/s/Mpc. Otra, con el fondo cósmico de microondas (semana 42) y el modelo cosmológico estándar: la misión Planck dio en 2018 unos $67{,}4 \pm 0{,}5$. La diferencia, de unas 5 desviaciones típicas, es la **tensión de Hubble**. Otros equipos, con otras candelas estándar, obtienen valores intermedios. Nadie sabe todavía si hay un error sistemático escondido en alguna de las medidas o si falta algo en el modelo del universo. Es uno de los problemas abiertos más vivos de la cosmología.

:::note[De dónde viene la palabra]
**Megapársec**: el prefijo *mega-* viene del griego *mégas*, «grande», y en el sistema internacional significa un millón. 1 Mpc son 3,26 millones de años luz. **Supernova de tipo Ia**: la «I» indica que su espectro no tiene hidrógeno, y la «a», que tiene silicio. Son explosiones de enanas blancas que superan el límite de Chandrasekhar (semana 36) y, como todas estallan con una masa parecida, tienen luminosidades parecidas: buenas candelas estándar, visibles a miles de millones de años luz.
:::

**Qué hacer**

1. Una galaxia está a 100 Mpc. ¿A qué velocidad se aleja, con $H_0 = 70$? ¿Qué $z$ tiene?
2. Calcula $1/H_0$ en años para $H_0 = 67{,}4$ y para $H_0 = 73$. ¿Cuánto cambia la edad estimada?
3. Explica por qué la ley de Hubble-Lemaître no funciona para Andrómeda.

### Sesión 4 · Astronomía y observación: galaxias con prismáticos (30-45 min)

Además de Andrómeda y el Triángulo (semana 40), desde un cielo oscuro y con unos prismáticos 8×30 se pueden ver otras galaxias brillantes. Todas son manchitas tenues, y para verlas hacen falta paciencia, visión lateral y unos prismáticos bien apoyados.

- **M81 y M82**, en la Osa Mayor: dos galaxias juntas, a unos 12 millones de años luz, que caben en el mismo campo. M81 es una espiral (magnitud 6,9) que se ve como una mancha ovalada; M82, alargada y más débil (8,4), está deformada por el tirón gravitatorio de M81 y forma estrellas a un ritmo frenético. La Osa Mayor está baja al norte a primera hora de la noche en noviembre y sube durante la madrugada; en primavera está alta toda la noche. Se encuentran prolongando hacia el noroeste la diagonal del «carro» que va de Phecda a Dubhe.
- **NGC 253**, en el Escultor: una galaxia espiral muy alargada, de magnitud 7, a unos 11 millones de años luz. Está baja al sur en las noches de otoño (desde el sur de la península se ve mejor). Búscala a partir de Diphda (β Ceti), la estrella brillante de la Ballena.
- **M31, M32 y M33**: repítelas en una noche mejor que la de la semana pasada.

**Lo que no se ve.** Con los prismáticos verás galaxias, pero no su corrimiento al rojo: hace falta un espectrógrafo. Sí puedes pensar en él: la luz de M81 llega estirada un poco más de lo que llegaría si la galaxia estuviera quieta. En galaxias tan cercanas, sus movimientos propios dentro de su grupo pesan tanto como la expansión; la ley de Hubble-Lemaître se nota bien a partir de decenas de megapársecs.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 41:

- genera el espectro **sintético** de una galaxia con líneas de hidrógeno y oxígeno, lo desplaza al rojo y mide $z$ comparando las líneas,
- construye un diagrama de Hubble **simulado** con galaxias que tienen velocidades peculiares y errores en la distancia, y ajusta $H_0$ con barras de error y un ajuste ponderado,
- calcula $\chi^2$ y la edad del universo con su incertidumbre,
- dibuja los dos valores de la tensión de Hubble con sus barras de error.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-41.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-41.ipynb)

## Qué has aprendido

- **La respuesta.** Sí: las galaxias se alejan unas de otras con una velocidad proporcional a su distancia, $v = H_0 d$, con $H_0 \approx 70$ km/s/Mpc. No es una explosión desde un centro: es el espacio entre las galaxias el que crece. De $1/H_0$ sale que el universo tiene unos 14 000 millones de años.
- **Cómo se mide.** Con el corrimiento al rojo de las líneas espectrales, $1 + z = \lambda_\text{obs}/\lambda_\text{emi}$, y con distancias de la escalera de distancias.
- **Las herramientas.** Errores aleatorios y sistemáticos, barras de error, ajustes ponderados y el chi cuadrado.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**El Doppler relativista.** La fórmula $z = v/c$ solo vale para velocidades pequeñas. Con la relatividad especial (semana 44), para una fuente que se aleja en línea recta a velocidad $v = \beta c$, el corrimiento es

$$1 + z = \sqrt{\frac{1 + \beta}{1 - \beta}}.$$

Para $\beta$ pequeño, con la aproximación binomial (semana 21), $\sqrt{(1+\beta)/(1-\beta)} \approx (1 + \beta/2)(1 + \beta/2) \approx 1 + \beta$, y vuelve a salir $z \approx \beta$. Pero cuando $\beta \to 1$, $z \to \infty$: con movimientos en el espacio, cualquier $z$ es posible sin superar la velocidad de la luz.

**El factor de escala.** Para la expansión, la descripción correcta es otra. Los cosmólogos describen el tamaño del universo con un número, el **factor de escala** $a(t)$, que hoy vale 1 y valía menos en el pasado: cuando $a = 0{,}5$, todas las distancias entre galaxias lejanas eran la mitad. La luz se estira con él, así que

$$1 + z = \frac{1}{a(t_\text{emi})}.$$

Una galaxia con $z = 3$ emitió su luz cuando el universo era cuatro veces más pequeño. La constante de Hubble es el ritmo relativo al que crece el factor de escala hoy: $H_0 = \dot{a}/a$, con el punto indicando la derivada respecto al tiempo (semana 10).

**Ejercicios**

1. Despeja $\beta$ en la fórmula del Doppler relativista y calcula qué velocidad haría falta para $z = 1$ con un movimiento en el espacio.
2. ¿Qué tamaño tenía el universo, respecto al actual, cuando emitieron su luz las galaxias con $z = 1$, $z = 3$ y $z = 14$?
3. Comprueba la aproximación $\sqrt{(1+\beta)/(1-\beta)} \approx 1 + \beta$ con $\beta = 0{,}01$ y con $\beta = 0{,}5$.

<details>
<summary>Soluciones</summary>

1. $(1+z)^2 = (1+\beta)/(1-\beta)$, así que $\beta = \frac{(1+z)^2 - 1}{(1+z)^2 + 1}$. Para $z = 1$: $\beta = 3/5 =$ **0,6**, el 60 % de la velocidad de la luz.
2. $1/2$, $1/4$ y $1/15$ del tamaño actual.
3. Con 0,01: $\sqrt{1{,}01/0{,}99} = 1{,}01005$ frente a 1,01 (excelente). Con 0,5: $\sqrt{3} = 1{,}732$ frente a 1,5 (un 13 % de error).

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Capítulo 26, Galaxias, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/26%3A_Galaxias). Español; incluye la ley de Hubble y la expansión. Verificado el 20 de noviembre de 2026.
2. [5.6 El efecto Doppler, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/05%3A_Radiaci%C3%B3n_y_espectros/5.06%3A_El_efecto_Doppler). Español; el efecto Doppler en la luz con ejemplos. Verificado el 20 de noviembre de 2026.
3. [Capítulo 29, El Big Bang, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/29%3A_El_Big_Bang). Español; la expansión, la edad del universo y su geometría. Verificado el 20 de noviembre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). Para localizar M81, M82 y NGC 253. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
