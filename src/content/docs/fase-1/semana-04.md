---
title: "Semana 4 · ¿Por qué cambian las constelaciones con las estaciones?"
description: "Fase 1 · Principios básicos de astronomía. Funciones, pendiente, división con resto y funciones periódicas; día sidéreo y qué parte del cielo se ve cada noche."
sidebar:
  order: 4
  label: "4. ¿Por qué cambian las constelaciones con las estaciones?"
---

## La pregunta del cielo

En una noche de enero, Orión domina el cielo del sur. En una de julio no se ve, y en su lugar están el Escorpión y el Triángulo de Verano. Las estrellas no se han movido: lo que cambia es qué parte del cielo tienes sobre la cabeza cuando es de noche. Y es la Tierra, que da la vuelta al Sol, la que decide cuál.

Esta semana vas a cuantificarlo: cuántos grados avanza el cielo cada día, por qué una estrella sale unos cuatro minutos antes cada noche, y qué constelaciones están mejor situadas cada mes del año. Por el camino aprendes dos ideas matemáticas que vas a usar todo el año: qué es una función y qué significa que algo sea periódico.

:::note[De dónde viene la palabra]
**Constelación** viene del latín *constellatio*, de *cum*, «con, junto», y *stella*, «estrella»: un grupo de estrellas. Las estrellas de una constelación no tienen por qué estar cerca unas de otras en el espacio; solo se ven en la misma dirección. Las figuras son antiquísimas, muchas de origen mesopotámico y griego, pero las 88 constelaciones oficiales las fijó la Unión Astronómica Internacional en 1922, y sus fronteras en 1930. Hoy una constelación es una región del cielo con límites precisos, como una provincia en un mapa.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: funciones, gráficas y pendiente (35-45 min)

**Qué es una función.** Una **función** es una regla que asigna a cada valor de una magnitud un único valor de otra. A cada día del año, la hora a la que sale el Sol; a cada hora de la noche, la altura de una estrella; a cada kilo de fruta, su precio. La magnitud que eliges tú (el día, la hora, los kilos) es la **variable independiente**, que se suele llamar $x$; la que resulta de aplicar la regla es la **variable dependiente**, $y$. Se escribe $y = f(x)$, que se lee «$y$ es función de $x$» o «efe de equis».

**La gráfica.** La **gráfica** de una función es esa regla dibujada en el plano cartesiano de la semana 3: para cada $x$ se marca el punto $(x, f(x))$, y todos esos puntos forman una línea. Saber leer una gráfica es saber extraer de ella cuánto vale la magnitud en un punto, si crece o decrece, a qué ritmo y dónde cambia de comportamiento.

**La función lineal.** La más sencilla tiene la forma

$$y = a\,x + b.$$

Su gráfica es una recta. El número $b$ es el valor de $y$ cuando $x = 0$: el punto donde la recta corta el eje vertical, la **ordenada en el origen**. El número $a$ es la **pendiente**: cuánto aumenta $y$ cuando $x$ aumenta una unidad. Si un taxi cobra 3 € al subir y 1,20 € por kilómetro, el precio es $y = 1{,}20\,x + 3$: la pendiente es el precio por kilómetro y la ordenada en el origen, la bajada de bandera. Una pendiente positiva sube, una negativa baja, y una pendiente cero es una recta horizontal: algo que no cambia.

La pendiente se calcula con dos puntos cualesquiera de la recta: es el cambio de $y$ dividido por el cambio de $x$,

$$a = \frac{y_2 - y_1}{x_2 - x_1}.$$

Es un **ritmo**: euros por kilómetro, grados por día, horas por día. Esa idea, el ritmo al que cambia una cosa respecto a otra, es la semilla de la derivada que verás en la semana 10.

**Un ejemplo del cielo.** La ascensión recta del Sol, tomando como origen el equinoccio de marzo (día 80 del año), crece de forma casi lineal: unas 24 h en 365,24 días. Su pendiente es $24/365{,}24 \approx 0{,}0657$ h por día, es decir, unos 3 min 56 s al día.

:::note[De dónde viene la palabra]
**Función** viene del latín *functio*, «cumplimiento, ejecución», de *fungi*, «desempeñar una tarea». Leibniz la empezó a usar en matemáticas a finales del siglo XVII para las magnitudes que dependen de un punto de una curva, y Euler, en el siglo XVIII, le dio un sentido cercano al actual. **Gráfica** viene del griego *gráphein*, que significaba a la vez «escribir» y «dibujar». **Lineal** viene de *linea*, «hilo de lino», y de ahí «línea recta», porque un hilo tenso marca una recta.
:::

**Ejercicios**

1. ¿Cuántos grados de ascensión recta avanza el Sol en un día? (Una hora equivale a 15°.)
2. Si el 21 de marzo (día 80) la AR del Sol es 0 h, ¿cuál es el día 140 (hacia el 20 de mayo), con la aproximación lineal?
3. Dibuja a mano esa recta entre el día 80 y el 445 (un año después) e interpreta su pendiente.
4. Una recta pasa por los puntos (2, 5) y (6, 13). Calcula su pendiente y su ordenada en el origen.

<details>
<summary>Soluciones</summary>

1. 0,0657 h · 15 ≈ **0,986°** al día. Es casi 1°, y de ahí viene la idea de que el Sol recorre unos 360° en unos 365 días.
2. 60 · 0,0657 = **3,94 h**, es decir, 3 h 56 min.
3. La recta sube de 0 h a 24 h en 365,24 días. Su pendiente es el ritmo al que el Sol avanza por el cielo, unos 4 minutos de AR al día.
4. Pendiente: (13 − 5)/(6 − 2) = **2**. Con $y = 2x + b$ y el punto (2, 5): 5 = 4 + b, luego **b = 1**.

</details>

### Sesión 2 · Matemáticas: periodicidad y el resto de una división (35-40 min)

**Cosas que se repiten.** Muchas magnitudes del cielo se repiten: el día, las fases de la Luna, las estaciones. Una función es **periódica** de periodo $T$ si cada vez que avanzas $T$ vuelves a encontrar el mismo valor:

$$f(x + T) = f(x).$$

La hora del reloj es periódica con periodo 24 horas; la fase de la Luna, con periodo de unos 29,5 días; la ascensión recta del Sol, con periodo de un año.

**La división con resto.** Para trabajar con cantidades periódicas hace falta una operación de la escuela que casi nunca se usa después: la división entera con resto. Al dividir 26 entre 24, cabe **1** vez y **sobran 2**: el cociente es 1 y el resto, 2. Comprobación: $26 = 1 \cdot 24 + 2$. El resto siempre está entre 0 y el divisor menos uno.

En matemáticas y en programación, el resto tiene un nombre y un símbolo propios: se llama **módulo** y se escribe $a \bmod n$ (en Python, `a % n`). Así, $26 \bmod 24 = 2$: si son las 26 horas contando desde la medianoche de ayer, en el reloj son las 2. Es la «aritmética del reloj»: cuando llegas a 24, vuelves a empezar.

Con números negativos, el resto se define para que siga estando entre 0 y $n - 1$: $-3 \bmod 24 = 21$, porque $-3 = (-1) \cdot 24 + 21$. En el reloj: tres horas antes de la medianoche son las 21.

**Diferencias en un círculo.** Otro uso del resto: la diferencia entre dos ascensiones rectas no es la resta directa. Entre 23 h y 1 h hay 2 h, no 22, porque puedes ir de una a otra por el camino corto, pasando por las 24 h. La diferencia correcta es el menor de $(a - b) \bmod 24$ y $24 - (a - b) \bmod 24$.

:::note[De dónde viene la palabra]
**Periodo** viene del griego *períodos*, «vuelta, circuito», de *perí*, «alrededor», y *hodós*, «camino»: el camino que da la vuelta y vuelve al principio. **Módulo** viene del latín *modulus*, «medida pequeña», diminutivo de *modus*, «medida». Carl Friedrich Gauss lo usó en 1801 en este sentido: dos números son iguales «módulo $n$» si dan el mismo resto al dividirlos por $n$. **Resto** viene de *restare*, «quedar, sobrar».
:::

**Ejercicios**

1. Calcula $50 \bmod 24$ y $-30 \bmod 24$.
2. ¿Qué diferencia hay entre Aldebarán (4,6 h) y Antares (16,5 h)? ¿Y entre Vega (18,6 h) y Aldebarán?
3. Si una función tiene periodo 12 y $f(5) = 3$, ¿cuánto vale $f(29)$?

<details>
<summary>Soluciones</summary>

1. $50 = 2 \cdot 24 + 2$, así que $50 \bmod 24 = 2$. Y $-30 = (-2) \cdot 24 + 18$, así que $-30 \bmod 24 = 18$.
2. Aldebarán–Antares: 11,9 h (la menor entre 11,9 y 12,1 h). Vega–Aldebarán: 14 h o 10 h, luego **10 h**.
3. 29 = 5 + 2·12, luego $f(29) = f(5) = 3$.

</details>

### Sesión 3 · Física: día sidéreo, día solar y año (35-45 min)

**Dos días distintos.** El **día solar** es el intervalo entre dos mediodías consecutivos, es decir, entre dos pasos del Sol por el meridiano. Dura 24 h en promedio. El **día sidéreo** es el intervalo entre dos pasos de una misma estrella por el meridiano: 23 h 56 min 4 s (23,9345 h según la NASA).

**Por qué son distintos.** Imagina la Tierra desde arriba, con un observador en el punto que mira al Sol a mediodía. La Tierra gira una vuelta completa (360°) en un día sidéreo, y el observador vuelve a mirar hacia la misma estrella lejana. Pero mientras tanto la Tierra ha avanzado casi 1° en su órbita alrededor del Sol, así que el Sol ya no está exactamente en la misma dirección: la Tierra tiene que girar ese grado de más para que vuelva a ser mediodía. Como la Tierra gira 1° en unos 4 minutos, el día solar es unos 4 minutos más largo que el sidéreo.

**La consecuencia que se ve.** Ese exceso hace que una estrella salga **4 minutos antes cada noche**: en un mes, unas 2 horas; en un año, un día entero. Un año contiene así 365,24 días solares y 366,24 días sidéreos: la Tierra da una vuelta más sobre sí misma respecto a las estrellas que respecto al Sol, porque una vuelta la «gasta» en dar la vuelta al Sol.

**Qué se ve a medianoche.** A medianoche estás en el lado de la Tierra opuesto al Sol, así que el cielo que tienes en el meridiano es el que está justo opuesto al Sol, a 12 h de ascensión recta de él. A mediodía, en cambio, el meridiano pasa por el Sol. Y cada hora que pasa, el cielo gira y una hora más de ascensión recta cruza el meridiano. Juntando las dos cosas, la ascensión recta que cruza el meridiano a la hora solar $t$ es

$$\alpha_{\text{meridiano}} = \alpha_\odot + (t - 12)\ \text{h},$$

donde $\alpha_\odot$ es la ascensión recta del Sol (el símbolo $\odot$, un círculo con un punto, es el signo antiguo del Sol). Comprueba que funciona: a mediodía ($t = 12$) da $\alpha_\odot$, el Sol; a medianoche ($t = 24$, o $t = 0$), da $\alpha_\odot \pm 12$ h. Como el Sol avanza unas 24 h de AR al año, la AR que culmina a medianoche cambia también 24 h al año. En enero el Sol está en AR ≈ 19 h, y a medianoche culmina lo que tiene AR ≈ 7 h: Sirio y Orión. En julio el Sol está en AR ≈ 6,7 h y a medianoche culmina AR ≈ 18,7 h: Vega.

**Año tropical y año sidéreo.** El año de las estaciones (de equinoccio a equinoccio) se llama **año tropical** y dura 365,2422 días; el **año sidéreo** (una vuelta respecto a las estrellas) dura 365,2564, unos 20 minutos más. La diferencia viene de la precesión del eje terrestre que viste en la semana 3. El calendario sigue el año tropical, para que las estaciones caigan siempre en las mismas fechas; por eso, a lo largo de los siglos, la fecha en que cada constelación culmina a medianoche se desplaza muy despacio.

:::note[De dónde viene la palabra]
**Culminar** viene del latín *culmen*, «cima, punto más alto», como *cumbre*: una estrella culmina cuando cruza el meridiano y alcanza su mayor altura. **Trópico** viene del griego *tropḗ*, «vuelta, giro»: en los solsticios el Sol «da la vuelta» y empieza a desplazarse en sentido contrario. Los trópicos de Cáncer y de Capricornio son las latitudes donde el Sol llega justo al cénit en esos días, y el año tropical es el que mide el ciclo de esas vueltas.
:::

**Qué hacer**

1. Comprueba con la aproximación de la sesión 1 cuánto debería avanzar una estrella en una semana: 7 · 3 min 56 s.
2. Explica por escrito por qué en una noche de invierno ves constelaciones distintas de las de verano, sin usar la palabra «órbita» más de una vez.
3. No confundas dos efectos distintos: las estaciones las produce la inclinación del eje (semana 1); el cambio de constelaciones lo produce la posición de la Tierra en su órbita. Si el eje no estuviera inclinado, ¿seguirían cambiando las constelaciones a lo largo del año?

### Sesión 4 · Astronomía y observación (30-45 min)

Con la guía de las dos primeras columnas de esta tabla (aproximada y para el hemisferio norte) y con Stellarium, identifica en el cielo lo que está mejor situado cada época.

| Primer día del mes | AR en el meridiano a medianoche solar | Constelaciones destacadas cerca |
|---|---|---|
| Diciembre–enero | 4,8–6,8 h | Tauro, Orión, Can Mayor |
| Febrero–marzo | 8,9–10,7 h | Cáncer, Leo |
| Abril–mayo | 12,7–14,7 h | Virgo, Boyero |
| Junio–julio | 16,7–18,7 h | Escorpión, Hércules, Lira |
| Agosto–septiembre | 20,7–22,8 h | Cisne, Águila, Pegaso |
| Octubre–noviembre | 0,8–2,8 h | Andrómeda, Casiopea, Aries, Perseo |

La AR sale de la fórmula de la sesión 3 y las constelaciones son orientativas: comprueba en Stellarium cuál cruza realmente el meridiano a la hora que elijas.

**Qué hacer**

1. En Stellarium, fija tu lugar y avanza el tiempo en incrementos de un mes, siempre a la misma hora solar. Anota qué constelación está sobre el meridiano sur cada vez.
2. Si el cielo está despejado, identifica una constelación de la tabla que corresponda a la época y apunta cuánto tarda otra en cruzar el meridiano detrás de ella.
3. Recuerda: la medianoche solar no es la del reloj. La hora oficial está fijada por zonas y, además, en verano se adelanta una hora. En la España peninsular, la medianoche solar cae alrededor de la 01:00 en invierno y de las 02:00 en verano, algo más tarde cuanto más al oeste estés.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 4:

- implementa el operador resto y la diferencia entre ascensiones rectas,
- calcula la ascensión recta aproximada del Sol para cada día del año,
- calcula qué AR culmina a la hora solar que elijas,
- dibuja la función periódica con las estrellas brillantes y lista cuáles están bien situadas cada mes.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-04.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-04.ipynb)

## Qué has aprendido

- **La respuesta.** A medianoche ves la parte del cielo opuesta al Sol, y el Sol se desplaza unos 4 minutos de ascensión recta cada día. Por eso la AR que culmina a medianoche cambia unas 2 h al mes y vuelve a empezar cada año.
- **La causa.** La Tierra gira sobre sí misma y además avanza en su órbita, lo que hace el día solar unos 4 minutos más largo que el sidéreo.
- **Las herramientas.** Qué es una función y cómo se lee su gráfica; la función lineal, su pendiente como ritmo de cambio y su ordenada en el origen; la división con resto y el módulo para trabajar con magnitudes circulares; las funciones periódicas; y la fórmula del meridiano a una hora dada.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [La esfera celeste y la observación a simple vista, astronomas.org](https://astronomas.org/files/documents/learning/esfera_celeste.pdf). Español, PDF didáctico que incluye el uso del planisferio, un instrumento que muestra el cielo de cada fecha y hora. Verificado el 31 de octubre de 2026.
2. [¿Qué causa las estaciones? NASA Space Place](https://spaceplace.nasa.gov/seasons/en), versión en español en [Space Place](https://spaceplace.nasa.gov/seasons/sp/). Para no confundir las estaciones (inclinación del eje) con los cambios de constelaciones (posición orbital). Verificado el 31 de octubre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
