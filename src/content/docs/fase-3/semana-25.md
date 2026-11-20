---
title: "Semana 25 · ¿Cuánto tarda la luz en llegar?"
description: "Fase 3 · La luz. Unidades de distancia astronómicas, el año luz, retrasos de señales, la medida de Rømer, la historia de la velocidad de la luz y mirar al pasado."
sidebar:
  order: 25
  label: "25. ¿Cuánto tarda la luz en llegar?"
---

## La pregunta del cielo

El 18 de noviembre de 2026, la sonda Voyager 1, lanzada en 1977, llegó a un día luz de la Tierra: unos 25 900 millones de kilómetros. Desde ese momento, cualquier orden que le envíen tarda un día entero en llegar, y su respuesta, otro día en volver. Es el objeto fabricado por el ser humano que más lejos ha llegado, y aun así la luz recorre esa distancia en lo que tardamos en dormir y vivir un día.

Cuando miras la Luna, la ves como era hace poco más de un segundo. El Sol, como era hace ocho minutos. Sirio, como era hace casi nueve años. La galaxia de Andrómeda, la cosa más lejana que se puede ver a simple vista, como era hace dos millones y medio de años, antes de que existiera nuestra especie. **Mirar lejos es mirar al pasado.** La luz es el único mensajero que nos llega de casi todo el universo, y tiene una velocidad finita.

Esta fase entera trata de la luz: qué es, cómo viaja, qué nos cuenta de lo que la emitió. Empieza por lo más básico: cuánto tarda en llegar, y cómo se descubrió que tardaba algo.

:::note[De dónde viene la palabra]
**Luz** viene del latín *lux, lucis*, de una raíz indoeuropea que significa «brillar». De la misma familia son *lúcido*, *lucir* y *lucero*. Los romanos llamaban *Lucifer*, «el portador de la luz» (de *lux* y *ferre*, «llevar»), al lucero del alba, el planeta Venus cuando se ve antes de amanecer. Solo mucho después el nombre pasó a la tradición cristiana con otro sentido.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: distancias que se miden en tiempo (35-45 min)

**Una distancia que es un tiempo.** Si algo viaja siempre a la misma velocidad, distancia y tiempo son intercambiables: puedes decir que Valencia está «a tres horas y media de Madrid en coche», y todo el mundo entiende una distancia. La luz viaja en el vacío siempre a la misma velocidad,

$$c = 299\,792\,458\ \text{m/s} \approx 3{,}00 \times 10^8\ \text{m/s},$$

así que en astronomía se usan distancias medidas en tiempo de luz. Un **segundo luz** es la distancia que recorre la luz en un segundo: casi 300 000 km, siete veces y media la vuelta a la Tierra. Un **minuto luz**, 60 veces más; una **hora luz**, 3600 veces más, y así sucesivamente.

**El año luz.** El **año luz** es la distancia que recorre la luz en un año. Para que sea una unidad exacta, se toma el año juliano de 365,25 días:

$$1\ \text{año luz} = c \cdot 365{,}25 \cdot 86\,400\ \text{s} \approx 9{,}461 \times 10^{15}\ \text{m} \approx 9{,}46 \times 10^{12}\ \text{km}.$$

Cuidado: el año luz es una **distancia**, no un tiempo, aunque se defina con uno. Decir «Sirio está a 8,6 años luz» significa que su luz tarda 8,6 años en llegar, y que la vemos como era hace 8,6 años.

**Cambiar de unidad sin perderse.** Las tres unidades de distancia astronómicas más usadas son el kilómetro, la unidad astronómica (ua, la distancia media Tierra-Sol, $1{,}496 \times 10^8$ km) y el año luz. Para pasar de una a otra se multiplica por un factor que vale 1, como en la semana 8, y se trabaja con potencias de 10 (semana 1):

$$1\ \text{año luz} = \frac{9{,}461 \times 10^{12}\ \text{km}}{1{,}496 \times 10^{8}\ \text{km/ua}} \approx 63\,240\ \text{ua}.$$

**Una escala logarítmica de distancias.** Las distancias del universo abarcan tantos órdenes de magnitud que en una regla normal no caben: si la Luna estuviera a 1 cm del origen, Andrómeda estaría a 600 000 km, más allá de la Luna de verdad. En la semana 15 aprendiste la solución: una escala logarítmica, en la que cada marca vale diez veces la anterior. En ella, el tiempo que tarda la luz en llegar desde cada objeto se reparte cómodamente: segundos para la Luna, minutos para el Sol, horas para los planetas exteriores, años para las estrellas cercanas y millones de años para las galaxias.

| Objeto | Distancia (aprox.) | La luz tarda |
|---|---|---|
| La Luna | 384 400 km | 1,28 s |
| El Sol | 1 ua | 8 min 19 s |
| Júpiter (según la posición) | 4,2 a 6,2 ua | 35 a 52 min |
| Voyager 1 (noviembre de 2026) | 173 ua | 1 día |
| Próxima Centauri, la estrella más cercana | 4,24 años luz | 4,24 años |
| Sirio | 8,6 años luz | 8,6 años |
| Galaxia de Andrómeda | 2,5 millones de años luz | 2,5 millones de años |

**Ejercicios**

1. Calcula cuántos kilómetros son un minuto luz y una hora luz.
2. ¿Cuántos minutos tarda la luz en llegar del Sol a la Tierra? ¿Y de Neptuno (30 ua)?
3. Expresa 4,24 años luz en kilómetros y en ua.
4. La sonda Voyager 1 tardó 49 años en llegar a un día luz. ¿Cuánto tardaría, a la misma velocidad media, en llegar a Próxima Centauri?

<details>
<summary>Soluciones</summary>

1. Minuto luz: $3 \times 10^5\ \text{km/s} \cdot 60\ \text{s} =$ **1,8 × 10⁷ km**, unos 18 millones. Hora luz: **1,08 × 10⁹ km**, unos mil millones.
2. $1{,}496 \times 10^{8}\ \text{km} / 2{,}998 \times 10^{5}\ \text{km/s} \approx 499$ s $\approx$ **8,3 min**. Neptuno: $30 \cdot 499$ s $\approx 15\,000$ s $\approx$ **4,2 horas**.
3. $4{,}24 \cdot 9{,}46 \times 10^{12} \approx$ **4,0 × 10¹³ km**, y $4{,}24 \cdot 63\,240 \approx$ **268 000 ua**.
4. Próxima está a $4{,}24 \cdot 365{,}25 \approx 1550$ días luz. A un día luz cada 49 años, tardaría unos $1550 \cdot 49 \approx$ **76 000 años**.

</details>

### Sesión 2 · Matemáticas: retrasos que dependen de la distancia (30-40 min)

**Una señal que llega tarde.** Si un suceso ocurre en el instante $t_0$ a una distancia $d$ de ti, no te enteras hasta el instante

$$t_\text{observado} = t_0 + \frac{d}{c}.$$

El término $d/c$ es el **tiempo de luz**. Si la distancia cambia con el tiempo, el retraso también cambia, y sucesos que ocurren con un ritmo perfectamente regular te llegan con un ritmo irregular.

**El razonamiento de Rømer.** Ío, la luna de Júpiter más cercana al planeta, da una vuelta cada 1,769 días (semana 22). En cada vuelta pasa por detrás de Júpiter, entra en su sombra y desaparece: es un **eclipse** de Ío, un reloj natural que se puede cronometrar desde la Tierra con un telescopio. En la década de 1670, el astrónomo danés Ole Rømer, que trabajaba en el Observatorio de París, notó que los eclipses no llegaban con un ritmo constante. Cuando la Tierra se alejaba de Júpiter, se iban retrasando; cuando se acercaba, se adelantaban. En 1676 propuso la explicación: la luz tarda un tiempo en cruzar la distancia extra.

Con números actuales: la distancia Tierra-Júpiter varía entre unos 4,2 ua (en la oposición, con los dos del mismo lado del Sol) y unos 6,2 ua (en la conjunción, al otro lado del Sol). La diferencia es de unos 2 ua, el diámetro de la órbita terrestre. Un eclipse observado en la conjunción llega con un retraso adicional de

$$\Delta t = \frac{2\ \text{ua}}{c} = \frac{2{,}99 \times 10^{11}\ \text{m}}{3{,}00 \times 10^8\ \text{m/s}} \approx 1000\ \text{s} \approx 16{,}6\ \text{min}$$

respecto a uno observado en la oposición. Rømer estimó unos 22 minutos; el error venía de la precisión de los relojes y de las observaciones de la época. Pero la idea era correcta, y Christiaan Huygens la usó para calcular la primera estimación de la velocidad de la luz: unos 220 000 km/s, del orden correcto.

**Ejercicios**

1. Un suceso en Marte ocurre a las 12:00:00 en el reloj de la Tierra, cuando Marte está a 1,5 ua. ¿A qué hora lo vemos?
2. Si la Tierra se aleja de Júpiter a unos 30 km/s (la velocidad orbital terrestre, en el peor caso), ¿cuánto aumenta la distancia en una vuelta de Ío? ¿Cuántos segundos se retrasa cada eclipse respecto al anterior?
3. Con el retraso de 22 minutos de Rømer y el diámetro de la órbita terrestre real, ¿qué velocidad de la luz sale?

<details>
<summary>Soluciones</summary>

1. $1{,}5 \cdot 499$ s $\approx 750$ s $= 12$ min 30 s: a las **12:12:30**.
2. En 1,769 días ($1{,}53 \times 10^5$ s), la distancia aumenta $30 \cdot 1{,}53\times10^5 \approx 4{,}6 \times 10^{6}$ km, y el eclipse se retrasa $4{,}6\times10^6 / 3\times10^5 \approx$ **15 s**. Pequeño para un solo eclipse, pero los retrasos se acumulan durante meses: esa acumulación es lo que notó Rømer.
3. $2{,}99 \times 10^{11}\ \text{m} / 1320\ \text{s} \approx$ **2,3 × 10⁸ m/s**, un 25 % menos que el valor real.

</details>

### Sesión 3 · Física: la historia de una velocidad (35-45 min)

**¿Instantánea?** Durante siglos se pensó que la luz no tardaba nada: Aristóteles, y mucho después Kepler y Descartes, la consideraban instantánea. Galileo dudaba, y en 1638 propuso un experimento: dos personas con linternas tapadas en dos colinas; la primera destapa la suya, y la segunda destapa la suya en cuanto ve la luz de la primera. Midiendo el tiempo de ida y vuelta se obtendría la velocidad. No funcionó: con las colinas a un par de kilómetros, la luz tarda unas millonésimas de segundo, y lo que se mide es el tiempo de reacción de las personas.

**Los astrónomos, primero.** La primera medida la dio el cielo, porque solo allí hay distancias lo bastante grandes: Rømer en 1676, con las lunas de Júpiter. En 1729, James Bradley encontró una segunda prueba astronómica, la **aberración de la luz**: las estrellas parecen desplazarse un poco a lo largo del año en la dirección del movimiento de la Tierra, como la lluvia que parece caer inclinada cuando corres (lo calculas en «Para ir más lejos»). De ese desplazamiento sacó un valor muy cercano al real.

**Los laboratorios, después.** En 1849, Hippolyte Fizeau midió la velocidad de la luz en la Tierra por primera vez. Envió un haz de luz entre los dientes de una rueda dentada que giraba deprisa, hasta un espejo a unos 8,6 km, y de vuelta. Si la rueda giraba a la velocidad justa, la luz que salía por un hueco volvía cuando ya había llegado el diente siguiente, y quedaba tapada. Con la velocidad de la rueda, el número de dientes y la distancia, obtuvo unos 313 000 km/s. En 1862, Léon Foucault (el del péndulo, semana 8) usó un espejo giratorio y obtuvo 298 000 km/s, muy cerca del valor actual. Albert Michelson refinó el método durante cincuenta años.

**Un valor exacto, por definición.** Desde 1983, la velocidad de la luz en el vacío no se mide: se define. Vale exactamente $299\,792\,458$ m/s, y el **metro** se define a partir de ella como la distancia que recorre la luz en $1/299\,792\,458$ de segundo. Medir una distancia es, hoy, medir un tiempo.

**En la materia, más despacio.** En el agua, en el vidrio o en el aire, la luz viaja más despacio que en el vacío. El cociente entre las dos velocidades es el **índice de refracción**, $n = c/v$: unos 1,0003 en el aire, 1,33 en el agua y alrededor de 1,5 en el vidrio. Este frenazo es lo que hace que la luz se doble al cambiar de medio, y en él se basan las lentes de la semana 28.

**Un límite universal.** Ningún objeto, señal o información puede viajar más deprisa que la luz en el vacío. Es uno de los pilares de la relatividad de Einstein (semana 44), y tiene una consecuencia práctica para la exploración espacial: una sonda lejana no se puede pilotar en directo. Los rovers de Marte reciben las órdenes con entre 3 y 22 minutos de retraso, y por eso tienen que tomar muchas decisiones solos.

:::note[De dónde viene la palabra]
La **c** de la velocidad de la luz se suele explicar como la inicial del latín *celeritas*, «rapidez» (semana 8). **Refracción** viene de *refractus*, participio de *refringere*, «romper, quebrar»: la luz parece quebrarse al pasar del aire al agua, como un lápiz metido en un vaso. **Metro**, del griego *métron*, «medida», como viste en la semana 1.
:::

**Qué hacer**

1. Calcula cuánto tarda la luz en recorrer 2 km, la distancia entre las colinas de Galileo, y compáralo con un tiempo de reacción humano (unos 0,2 s).
2. ¿Cuánto tarda en llegar una orden a un rover de Marte cuando Marte está en la oposición (unos 0,5 ua en las mejores) y en la conjunción (unos 2,5 ua)?
3. ¿A qué velocidad viaja la luz en el agua?

### Sesión 4 · Astronomía y observación: una máquina del tiempo esta noche (30-45 min)

Esta semana vas a hacer una lista de lo que ves en el cielo y de cuándo salió la luz que te llega de cada cosa.

1. Abre Stellarium y elige seis objetos visibles esta noche desde tu lugar: la Luna si está, un planeta, y varias estrellas brillantes de distinta distancia. Algunas buenas candidatas para las noches de otoño e invierno: Vega, Capella, Aldebarán, Betelgeuse, Sirio (de madrugada en otoño, a primera hora de la noche en invierno) y las Pléyades.
2. Selecciona cada uno y lee su distancia en el panel de información. Para las estrellas, Stellarium la da en años luz; para los planetas, en ua (multiplica por 8,3 para tenerla en minutos luz).
3. Para cada estrella, resta su distancia en años luz al año actual: es el año en que salió de la estrella la luz que estás viendo. Apunta qué ocurría ese año.
4. Si el cielo está despejado, sal a mirarlos. Con los prismáticos 8×30, las Pléyades son un espectáculo.

**Distancias aproximadas** para comparar con Stellarium (las de las estrellas lejanas tienen incertidumbres grandes, y distintas fuentes dan valores distintos):

| Estrella | Distancia aproximada |
|---|---|
| Sirio | 8,6 años luz |
| Vega | 25 años luz |
| Arturo | 37 años luz |
| Capella | 43 años luz |
| Aldebarán | 65 años luz |
| Pléyades | unos 440 años luz |
| Betelgeuse | entre unos 500 y 700 años luz |

**Andrómeda, a simple vista.** Si alguna noche vas a un lugar con el cielo oscuro, busca la galaxia de Andrómeda (M31), a unos 2,5 millones de años luz: es una mancha alargada y tenue en la constelación de Andrómeda, cerca de Casiopea, y en otoño pasa casi por el cénit a primera hora de la noche. En un cielo urbano luminoso no se ve a simple vista, pero los prismáticos 8×30 pueden mostrar su núcleo como una manchita difusa. Esa luz salió de Andrómeda cuando en la Tierra todavía no existía el *Homo sapiens*.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 25:

- programa una calculadora de tiempo de luz para cualquier distancia, en cualquier unidad,
- dibuja en escala logarítmica las distancias de la Luna a Andrómeda,
- simula los eclipses de Ío vistos desde la Tierra a lo largo de un año, con las órbitas de la Tierra y de Júpiter, y reproduce el adelanto y el retraso que vio Rømer,
- recupera la velocidad de la luz a partir de esos retrasos.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-25.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-25.ipynb)

## Qué has aprendido

- **La respuesta.** La luz tarda 1,3 segundos en llegar desde la Luna, 8 minutos y 19 segundos desde el Sol, años desde las estrellas y millones de años desde las galaxias. Lo que vemos en el cielo es siempre una imagen del pasado, y cuanto más lejos miramos, más atrás en el tiempo.
- **La historia.** La velocidad de la luz se midió primero en el cielo, porque solo allí hay distancias suficientes: Rømer en 1676 con los eclipses de Ío y Bradley en 1729 con la aberración. Después llegaron Fizeau, Foucault y Michelson en el laboratorio. Hoy es un valor exacto que define el metro.
- **Las herramientas.** Distancias medidas en tiempo de luz, el año luz y su conversión a km y ua, el tiempo de luz como retraso que depende de la distancia, y el uso de una escala logarítmica para abarcar muchos órdenes de magnitud.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**La aberración de la luz.** Cuando caminas bajo una lluvia que cae en vertical, tienes que inclinar el paraguas hacia delante: respecto a ti, las gotas llegan inclinadas. La velocidad de las gotas respecto a ti es la suma vectorial (semana 9) de su velocidad respecto al suelo, $\vec{u}$ hacia abajo, y de tu velocidad cambiada de signo, $-\vec{v}$. Si $\vec{v}$ es perpendicular a $\vec{u}$, el ángulo de inclinación $\alpha$ cumple

$$\tan\alpha = \frac{v}{u}.$$

Con la luz de una estrella pasa lo mismo. La Tierra se mueve a $v \approx 29{,}8$ km/s alrededor del Sol, y la luz llega a $c$. Para una estrella en la dirección perpendicular al movimiento de la Tierra, el telescopio tiene que inclinarse un ángulo

$$\alpha \approx \frac{v}{c} = \frac{29{,}8}{299\,792} \approx 9{,}94 \times 10^{-5}\ \text{rad} \approx 20{,}5''.$$

(Para un ángulo tan pequeño, la tangente y el ángulo en radianes son prácticamente iguales: semana 6.) Como la dirección del movimiento de la Tierra da una vuelta completa en un año, cada estrella describe en el cielo una pequeña figura de 20,5″ de «radio»: un círculo para las estrellas cercanas al polo de la eclíptica, una elipse en las demás, y un segmento para las que están sobre la eclíptica.

Bradley lo descubrió en 1725-1728 mientras buscaba otra cosa: la paralaje de las estrellas (semana 37), que sería la prueba de que la Tierra gira alrededor del Sol. La aberración resultó ser, a su vez, la primera prueba directa de ese movimiento, unos 110 años antes de que se midiera la primera paralaje. Midiendo $\alpha$ y conociendo $v$, Bradley obtuvo $c = v/\alpha$.

En sentido estricto, la fórmula exacta sale de la relatividad (semana 44) y es algo distinta, pero para $v$ mucho menor que $c$ la diferencia es inapreciable.

:::note[De dónde viene la palabra]
**Aberración** viene del latín *aberrare*, «desviarse, extraviarse», de *ab*, «lejos de», y *errare*, «vagar»: la luz parece llegar desviada de su dirección verdadera. La misma palabra se usa para los defectos de las lentes (semana 28).
:::

**Ejercicios**

1. La Tierra también gira sobre sí misma: en el ecuador, a 0,465 km/s (semana 8). ¿Qué aberración produce ese movimiento? Se llama **aberración diurna**.
2. Una nave viaja a 0,1 $c$. ¿Qué ángulo de aberración ve para una estrella perpendicular a su movimiento, con la fórmula aproximada $\tan\alpha = v/c$?
3. Supón que una medida antigua diera $\alpha \approx 20{,}2''$, un poco menos que el valor actual. ¿Qué velocidad de la luz saldría con $v = 29{,}8$ km/s?

<details>
<summary>Soluciones</summary>

1. $0{,}465/299\,792 \approx 1{,}55 \times 10^{-6}$ rad $\approx$ **0,32″**, unas 64 veces menos que la anual.
2. $\tan\alpha = 0{,}1$, luego $\alpha \approx$ **5,7°**. A esas velocidades, el cielo entero se deforma hacia delante.
3. $20{,}2'' = 20{,}2/206\,265 \approx 9{,}79\times10^{-5}$ rad, y $c = 29{,}8 / 9{,}79\times10^{-5} \approx$ **304 000 km/s**.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [1.1 La propagación de la luz, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/1-1-la-propagacion-de-la-luz). Español, nivel universitario; la velocidad de la luz, el método de Rømer con las lunas de Júpiter y el índice de refracción. Verificado el 20 de noviembre de 2026.
2. [5.1 El comportamiento de la luz, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/05%3A_Radiaci%C3%B3n_y_espectros/5.01%3A_El_comportamiento_de_la_luz). Español; qué es la luz y cómo se propaga, como introducción a toda la fase. Verificado el 20 de noviembre de 2026.
3. [How Far Away Is Voyager 1? One Light-Day, Explained (NASA)](https://svs.gsfc.nasa.gov/15120). Inglés; vídeo y animaciones sobre el hito del día luz. Verificado el 20 de noviembre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

Los datos del hito de la Voyager 1 (fecha, unos 25 900 millones de km y 173 ua) proceden de la NASA y de la revista EarthSky, consultadas el 20 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
