---
title: "Semana 4 · ¿Por qué cambian las constelaciones con las estaciones?"
description: "Fase 1 · Principios básicos de astronomía. Funciones periódicas, día sidéreo y qué parte del cielo se ve cada noche."
sidebar:
  order: 4
  label: "4. ¿Por qué cambian las constelaciones con las estaciones?"
---

## La pregunta del cielo

En una noche de enero, Orión domina el cielo del sur. En una de julio no se ve, y en su lugar están el Escorpión y el Triángulo de Verano. Las estrellas no se han movido: lo que cambia es qué parte del cielo tienes sobre la cabeza cuando es de noche. Y es la Tierra, que da la vuelta al Sol, la que decide cuál.

Esta semana vas a cuantificarlo: cuántos grados avanza el cielo cada día, por qué una estrella sale unos cuatro minutos antes cada noche, y qué constelaciones están mejor situadas cada mes del año.

## Las cinco sesiones

### Sesión 1 · Matemáticas: funciones y gráficas (30-40 min)

Una **función** es una regla que asigna a cada valor de una magnitud un valor de otra: a cada día del año, la ascensión recta del Sol; a cada hora, la altura de una estrella. La **gráfica** es esa regla dibujada en el plano cartesiano de la semana 3. Saber leer una gráfica es saber extraer de ella cuánto vale la magnitud en un punto, si crece o decrece, a qué ritmo (la pendiente) y dónde cambia de comportamiento.

Una función **lineal** tiene la forma $y = a x + b$: su gráfica es una recta de pendiente $a$. La ascensión recta del Sol, tomando como origen el equinoccio de marzo (día 80), crece de forma casi lineal: unas 24 h en 365,24 días, es decir, $24/365{,}24 \approx 0{,}0657$ h por día, o unos 3 min 56 s.

**Ejercicios**

1. ¿Cuántos grados de ascensión recta avanza el Sol en un día? (Una hora equivale a 15°.)
2. Si el 21 de marzo (día 80) la AR del Sol es 0 h, ¿cuál es el día 140 (hacia el 20 de mayo), con la aproximación lineal?
3. Dibuja a mano esa recta entre el día 80 y el 445 (un año después) e interpreta su pendiente.

<details>
<summary>Soluciones</summary>

1. 0,0657 h · 15 ≈ **0,986°** al día. Es casi 1°, y de ahí viene la idea de que el Sol recorre unos 360° en unos 365 días.
2. 60 · 0,0657 = **3,94 h**, es decir, 3 h 56 min.
3. La recta sube de 0 h a 24 h en 365,24 días. Su pendiente es el ritmo al que el Sol avanza por el cielo, unos 4 minutos de AR al día.

</details>

### Sesión 2 · Matemáticas: periodicidad y operador resto (30-40 min)

Las magnitudes del cielo se repiten. La ascensión recta vuelve a empezar al llegar a 24 h, igual que las horas del reloj. El modo de expresarlo es la operación **resto** (o módulo): $a \bmod n$ es lo que sobra de dividir $a$ entre $n$. Así $26 \bmod 24 = 2$, y con valores negativos $-3 \bmod 24 = 21$. Una función es **periódica** de periodo $T$ si $f(x + T) = f(x)$: la ascensión recta del meridiano a medianoche, como función del día, es periódica con periodo de un año.

Otro uso del resto: la diferencia entre dos AR no es la resta directa. Entre 23 h y 1 h hay 2 h, no 22. La diferencia correcta es el menor de $(a - b) \bmod 24$ y $24 - (a - b) \bmod 24$.

**Ejercicios**

1. Calcula $50 \bmod 24$ y $-30 \bmod 24$.
2. ¿Qué diferencia hay entre Aldebarán (4,6 h) y Antares (16,5 h)? ¿Y entre Vega (18,6 h) y Aldebarán?
3. Si una función tiene periodo 12 y $f(5) = 3$, ¿cuánto vale $f(29)$?

<details>
<summary>Soluciones</summary>

1. $50 \bmod 24 = 2$ y $-30 \bmod 24 = 18$ (porque $-30 + 48 = 18$).
2. Aldebarán–Antares: 11,9 h (la menor entre 11,9 y 12,1 h). Vega–Aldebarán: 14 h o 10 h, luego **10 h**.
3. 29 = 5 + 2·12, luego $f(29) = f(5) = 3$.

</details>

### Sesión 3 · Física: día sidéreo, día solar y año (30-40 min)

El **día solar** es el intervalo entre dos mediodías consecutivos (el Sol en el meridiano), de 24 h en promedio. El **día sidéreo** es el intervalo entre dos pasos de una misma estrella por el meridiano: 23 h 56 min 4 s (23,9345 h según la NASA). La Tierra, en un día, además de girar sobre sí misma avanza casi 1° en su órbita, así que tiene que girar un poco más de 360° para que el Sol vuelva al meridiano. Ese exceso de unos 4 minutos es lo que hace que una estrella salga **4 minutos antes cada noche**: en un mes, unas 2 horas; en un año, un día entero. Un año contiene así 365,24 días solares y 366,24 días sidéreos.

**Consecuencia.** El cielo que ves a medianoche está justo opuesto al Sol. Como el Sol avanza por el cielo unos 24 h de AR al año, la AR que culmina a medianoche cambia también 24 h al año:

$$\alpha_{\text{meridiano}} = \alpha_\odot + (t - 12)\ \text{h},$$

con $t$ la hora solar. En enero el Sol está en AR ≈ 19 h, y a medianoche culmina lo que tiene AR ≈ 7 h: Sirio y Orión. En julio el Sol está en AR ≈ 6,7 h y a medianoche culmina AR ≈ 18,7 h: Vega.

**Año tropical y año sidéreo.** El año de las estaciones (de equinoccio a equinoccio) dura 365,2422 días; el año sidéreo (una vuelta respecto a las estrellas) 365,2564, unos 20 minutos más. La diferencia viene de la precesión del eje terrestre. A lo largo de los siglos, la fecha en que cada constelación culmina a medianoche se desplaza muy despacio por esa razón.

**Qué hacer**

1. Comprueba con la aproximación de la sesión 1 cuánto debería avanzar una estrella en una semana: 7 · 3 min 56 s.
2. Explica por escrito por qué en una noche de invierno ves constelaciones distintas de las de verano, sin usar la palabra "órbita" más de una vez.

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
3. Recuerda: la medianoche solar no es la del reloj. En España, con horario de verano, está hacia las 02:00.

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
- **Las herramientas.** Funciones lineales y periódicas, el operador resto para medir diferencias circulares, y la fórmula del meridiano a una hora dada.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [La esfera celeste y la observación a simple vista, astronomas.org](https://astronomas.org/files/documents/learning/esfera_celeste.pdf). Español, PDF didáctico que incluye el uso del planisferio, un instrumento que muestra el cielo de cada fecha y hora. Verificado el 31 de octubre de 2026.
2. [¿Qué causa las estaciones? NASA Space Place](https://spaceplace.nasa.gov/seasons/en), versión en español en [Space Place](https://spaceplace.nasa.gov/seasons/sp/). Para no confundir las estaciones (inclinación del eje) con los cambios de constelaciones (posición orbital). Verificado el 31 de octubre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
