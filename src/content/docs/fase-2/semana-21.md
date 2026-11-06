---
title: "Semana 21 · ¿Por qué hay mareas?"
description: "Fase 2 · Órbitas. Aproximaciones, órdenes de magnitud y la aproximación binomial; la fuerza de marea; mareas vivas y muertas; efectos de marea en el Sistema Solar."
sidebar:
  order: 21
  label: "21. ¿Por qué hay mareas?"
---

## La pregunta del cielo

En cualquier puerto del Atlántico, el mar sube y baja dos veces al día. Desde la Antigüedad se sabía que el ritmo de las mareas seguía a la Luna: la pleamar se retrasa cada día unos 50 minutos, lo mismo que la salida de la Luna, y las mareas son más grandes con luna llena y luna nueva. Pero había un misterio: si la Luna atrae el agua, se entiende que suba el mar del lado de la Tierra que mira a la Luna. ¿Por qué sube también en el lado opuesto, el que le da la espalda? Así es: hay dos pleamares al día, no una.

Newton dio la respuesta: lo que produce las mareas no es la atracción de la Luna, sino la **diferencia** entre lo que atrae a un lado de la Tierra y a otro. Esa diferencia estira la Tierra en la dirección de la Luna, por los dos extremos a la vez. Para calcularla necesitas una herramienta muy útil en física: las aproximaciones, saber qué se puede despreciar y cuánto te equivocas al hacerlo.

## Las cinco sesiones

### Sesión 1 · Matemáticas: aproximaciones y órdenes de magnitud (30-40 min)

**Órdenes de magnitud.** El **orden de magnitud** de un número es la potencia de 10 más cercana: 3800 es del orden de $10^3$ o $10^4$, y 0,0027 del orden de $10^{-3}$. Trabajar con órdenes de magnitud permite responder preguntas difíciles con cálculos de cabeza. ¿Es importante este efecto o no? Si dos cantidades se diferencian en un factor 1000, casi seguro que la pequeña se puede ignorar. Si se diferencian en un factor 2, no.

El físico Enrico Fermi era famoso por estimar cualquier cosa así: cuántos afinadores de pianos hay en una ciudad, o la energía de una explosión a partir de lo lejos que volaban unos trozos de papel. A estas estimaciones se las llama **estimaciones de Fermi**. La clave es descomponer el problema en factores que sí se pueden estimar y no preocuparse por un factor 2 en cada uno.

**Cifras significativas.** Si un dato se conoce con dos cifras (la distancia a la Luna «unos 380 000 km»), no tiene sentido dar el resultado con siete. El resultado no es más preciso que el dato menos preciso.

**La aproximación binomial.** Si $x$ es un número pequeño comparado con 1, entonces

$$(1 + x)^n \approx 1 + n\,x.$$

Funciona con cualquier exponente $n$, entero, negativo o fraccionario. Pruébalo con números: $1{,}01^2 = 1{,}0201 \approx 1{,}02$; $\sqrt{1{,}02} = 1{,}00995 \approx 1{,}01$; $1/1{,}01 = 0{,}990099 \approx 0{,}99$. El error que cometes es del orden de $x^2$: si $x$ es 0,01, el error es de unas diezmilésimas. Para $n = 2$ se ve de dónde sale: $(1+x)^2 = 1 + 2x + x^2$, y si $x$ es pequeño, $x^2$ es mucho más pequeño todavía.

Esta aproximación aparece por todas partes en física, porque permite convertir fórmulas complicadas en otras lineales, fáciles de entender.

:::note[De dónde viene la palabra]
**Aproximar** viene del latín *approximare*, «acercarse», de *proximus*, «el más cercano». **Magnitud** viene de *magnitudo*, «grandeza», de *magnus*, «grande». **Estimar** viene de *aestimare*, «tasar, poner precio»: una estimación es una valoración, no una medida.
:::

**Ejercicios**

1. Calcula con la aproximación binomial $1{,}003^{10}$, $1/0{,}98$ y $\sqrt{1{,}06}$. Compara con la calculadora.
2. Estimación de Fermi: ¿cuántos latidos da un corazón humano en toda una vida? Da solo el orden de magnitud.
3. ¿Cuántas veces cabe la distancia Tierra-Luna (384 400 km) en la distancia Tierra-Sol (149,6 millones de km)? Responde primero de cabeza, con órdenes de magnitud, y luego con la calculadora.

<details>
<summary>Soluciones</summary>

1. $1{,}003^{10} \approx 1 + 10 \cdot 0{,}003 =$ **1,03** (exacto: 1,0304). $1/0{,}98 = (1 - 0{,}02)^{-1} \approx$ **1,02** (exacto: 1,0204). $\sqrt{1{,}06} \approx 1 + 0{,}06/2 =$ **1,03** (exacto: 1,0296).
2. Unos 70 latidos por minuto × 60 × 24 × 365 × 80 años $\approx 70 \cdot 5 \times 10^{5} \cdot 80 \approx 3 \times 10^{9}$: del orden de **tres mil millones**.
3. De cabeza: $10^{8} / 4\times10^{5} \approx 250$, del orden de cientos. Con la calculadora: **389 veces**.

</details>

### Sesión 2 · Matemáticas: la diferencia de dos atracciones (30-40 min)

Una masa $M$ (la Luna) está a una distancia $d$ del centro de la Tierra, de radio $R$. La aceleración que produce en el centro de la Tierra es $GM/d^2$. En el punto de la superficie más cercano, que está a $d - R$, es $GM/(d - R)^2$. La diferencia es la **aceleración de marea**:

$$\Delta a = \frac{GM}{(d - R)^2} - \frac{GM}{d^2}.$$

Restar dos números casi iguales es incómodo. Saca factor común $GM/d^2$ y escribe $(d - R)^2 = d^2(1 - R/d)^2$:

$$\Delta a = \frac{GM}{d^2}\left[\left(1 - \frac{R}{d}\right)^{-2} - 1\right].$$

Como $R/d$ es pequeño (para la Luna, $6371/384\,400 \approx 0{,}017$), aplica la aproximación binomial con $x = -R/d$ y $n = -2$: $(1 - R/d)^{-2} \approx 1 + 2R/d$. Queda

$$\Delta a \approx \frac{2\,G M R}{d^3}.$$

La fuerza de marea disminuye con el **cubo** de la distancia, no con el cuadrado. Esta es la clave de todo lo que sigue: alejarse un poco reduce mucho la marea.

**Ejercicios**

1. Calcula la aceleración de marea de la Luna en la Tierra. Datos: $GM_\text{L} = 4{,}90 \times 10^{12}$ m³/s², $R = 6{,}371 \times 10^{6}$ m, $d = 3{,}844 \times 10^{8}$ m. ¿Qué fracción de $g$ es?
2. Haz lo mismo para el Sol ($GM_\text{S} = 1{,}327 \times 10^{20}$ m³/s², $d = 1{,}496 \times 10^{11}$ m). ¿Cuántas veces mayor es la marea lunar que la solar?

<details>
<summary>Soluciones</summary>

1. $\Delta a = 2 \cdot 4{,}90\times10^{12} \cdot 6{,}371\times10^{6} / (3{,}844\times10^{8})^3 \approx$ **1,1 × 10⁻⁶ m/s²**, aproximadamente **una diezmillonésima** de $g$ ($1{,}1 \times 10^{-7}\,g$). Una fuerza diminuta, pero actúa sobre todo un océano.
2. $\Delta a \approx$ **5,0 × 10⁻⁷ m/s²**. La marea lunar es unas **2,2 veces** la solar, aunque el Sol atrae a la Tierra unas 180 veces más que la Luna: el Sol está tan lejos que su atracción es casi igual en los dos lados de la Tierra.

</details>

### Sesión 3 · Física: las fuerzas de marea (30-40 min)

**Por qué hay dos abultamientos.** Mira la Tierra desde el punto de vista de su centro, que cae hacia la Luna con la aceleración $GM/d^2$. El agua del lado cercano a la Luna es atraída **más** que el centro: se queda adelantada, hacia la Luna. El agua del lado lejano es atraída **menos** que el centro: se queda atrás, hacia fuera. Desde el centro de la Tierra, las dos se alejan. El resultado es que la Tierra (sobre todo los océanos, que se deforman con facilidad) se estira en la dirección de la Luna y forma dos abultamientos, uno a cada lado. En los lados perpendiculares, la marea tira hacia dentro y el agua baja.

**Dos mareas al día.** La Tierra gira bajo los dos abultamientos, y un punto de la costa pasa por los dos cada día: dos pleamares y dos bajamares. Pero como la Luna avanza en su órbita mientras tanto, el «día lunar» dura unas 24 h 50 min, y la pleamar se retrasa unos 50 minutos cada día. El intervalo entre dos pleamares es de unas 12 h 25 min.

**Mareas vivas y muertas.** El Sol produce sus propios abultamientos, unas 2,2 veces más pequeños. Con luna nueva y luna llena, el Sol, la Tierra y la Luna están alineados (en **sicigia**) y los abultamientos se suman: son las **mareas vivas**, con la mayor diferencia entre pleamar y bajamar. Con cuarto creciente y menguante, el Sol y la Luna forman un ángulo recto (en **cuadratura**), los abultamientos se contrarrestan en parte y se producen las **mareas muertas**. El ciclo completo se repite cada medio mes lunar, unos 14,8 días.

**La realidad es más complicada.** Los océanos no responden al instante. El agua tiene que moverse a través de cuencas con costas y fondos irregulares, y las mareas reales se retrasan respecto a la Luna y varían mucho de un lugar a otro. En mar abierto, la marea mide menos de un metro; en algunas bahías, la forma de la costa la amplifica, y en la bahía de Fundy, en Canadá, supera los 15 metros. En el Mediterráneo, un mar casi cerrado, es de solo unos decímetros.

**Las mareas en el Sistema Solar.** Las fuerzas de marea actúan sobre cualquier cuerpo extenso:

- La Tierra frena a la Luna con sus mareas sobre ella, y por eso la Luna gira sobre sí misma exactamente una vez por vuelta y nos muestra siempre la misma cara: está en **rotación síncrona**.
- Las mareas de la Luna frenan la rotación de la Tierra: los días se alargan unos 2 milisegundos por siglo. A cambio, la Luna se aleja de la Tierra unos 3,8 cm al año, medidos con láser desde la Tierra apuntando a los reflectores que dejaron las misiones Apolo.
- Io, la luna de Júpiter, se calienta por dentro con las mareas de Júpiter: es el cuerpo con más actividad volcánica del Sistema Solar.

:::note[De dónde viene la palabra]
**Marea** viene de *mar*, del latín *mare*. **Pleamar** es «mar llena» (*plena mar*) y **bajamar**, «mar baja». **Sicigia** viene del griego *syzygía*, «unión, yunta», de *syn*, «juntos», y *zygón*, «yugo»: el Sol, la Tierra y la Luna, uncidos en línea como bueyes bajo un mismo yugo. En inglés, las mareas vivas se llaman *spring tides*, y no tiene nada que ver con la primavera: viene de *spring* en el sentido de «brotar, saltar».
:::

**Qué hacer**

1. Explica con tus palabras, sin fórmulas, por qué hay pleamar en el lado de la Tierra opuesto a la Luna.
2. Si la Luna estuviera a la mitad de distancia, ¿cuántas veces mayores serían las mareas?
3. La Tierra también produce mareas en la Luna. Calcula la aceleración de marea de la Tierra sobre la Luna ($GM_\text{T} = 3{,}986 \times 10^{14}$ m³/s², radio lunar 1737 km) y compárala con la de la Luna sobre la Tierra.

<details>
<summary>Soluciones</summary>

1. La Luna atrae más al agua del lado cercano que al centro de la Tierra, y más al centro de la Tierra que al agua del lado lejano. Respecto al centro, el agua cercana se adelanta hacia la Luna y la lejana se queda atrás. Las dos se separan del centro: dos abultamientos.
2. Como la marea va con $1/d^3$, serían $2^3 =$ **8 veces** mayores.
3. $\Delta a = 2 \cdot 3{,}986\times10^{14} \cdot 1{,}737\times10^{6}/(3{,}844\times10^{8})^3 \approx$ **2,4 × 10⁻⁵ m/s²**, unas **22 veces** mayor que la de la Luna sobre la Tierra. Esa fuerza, actuando durante millones de años, acabó sincronizando la rotación de la Luna.

</details>

### Sesión 4 · Astronomía y observación: mareas y fases de la Luna (30-45 min)

**Comprueba la relación con una tabla de mareas.** Busca la tabla de mareas de un puerto del Atlántico o del Cantábrico (por ejemplo, de Cádiz, A Coruña o Santander) para el mes en curso. Puertos del Estado y el Instituto Hidrográfico de la Marina publican predicciones, y muchas webs de pesca y navegación las reproducen.

1. Apunta, para cada día, la diferencia entre la pleamar más alta y la bajamar más baja (la **amplitud** o **carrera** de marea).
2. Mira en Stellarium las fechas de luna nueva, cuarto creciente, luna llena y cuarto menguante de ese mes.
3. Dibuja la amplitud frente al día del mes y marca las fases. Las mayores amplitudes deberían caer uno o dos días **después** de la luna llena y la luna nueva; el retraso se debe a que el océano tarda en responder.
4. Mira la hora de la pleamar en días consecutivos. ¿Se retrasa unos 50 minutos cada día?

**Si vives junto al Mediterráneo**, notarás que la marea apenas existe: una cuenca casi cerrada, conectada al Atlántico solo por el estrecho de Gibraltar, no deja que se forme una marea grande. Allí, los cambios del nivel del mar por el viento y la presión atmosférica pueden ser mayores que la marea astronómica.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 21:

- compara la aproximación binomial con el cálculo exacto para distintos valores de $x$,
- calcula la aceleración de marea exacta y aproximada en varios puntos alrededor de la Tierra y la dibuja como flechas, donde aparecen los dos abultamientos,
- construye un modelo sencillo de marea sumando una onda lunar (periodo de 12 h 25 min) y una solar (12 h), y muestra el ciclo de mareas vivas y muertas,
- mide en la gráfica el periodo de ese ciclo y lo compara con la mitad del mes lunar.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-21.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-21.ipynb)

## Qué has aprendido

- **La respuesta.** Hay mareas porque la atracción de la Luna (y, en menor medida, la del Sol) no es igual en todos los puntos de la Tierra. La diferencia estira la Tierra en dirección a la Luna y forma dos abultamientos, uno a cada lado; al girar la Tierra bajo ellos, cada costa tiene dos pleamares al día. Las mareas son mayores en luna nueva y llena, cuando las del Sol y la Luna se suman.
- **La física.** La aceleración de marea vale aproximadamente $2GMR/d^3$: disminuye con el cubo de la distancia. Por eso la Luna, mucho más cercana, produce mareas mayores que el Sol, aunque el Sol nos atraiga mucho más.
- **Las herramientas.** Órdenes de magnitud, estimaciones de Fermi, cifras significativas y la aproximación binomial $(1 + x)^n \approx 1 + nx$.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 13.6, Fuerzas de marea, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-6-fuerzas-de-marea). Español; el origen de las mareas, las vivas y las muertas, y las mareas en Io y en estrellas dobles, con un ejemplo que compara la marea lunar y la solar. Verificado el 6 de noviembre de 2026.
2. [What are spring and neap tides? (NOAA, Servicio Oceánico Nacional de Estados Unidos)](https://oceanservice.noaa.gov/facts/springtide.html). Inglés, muy breve; mareas vivas y muertas con un esquema. Verificado el 6 de noviembre de 2026.
3. [Puertos del Estado](https://www.puertos.es/). Predicciones de marea de los puertos españoles. **(Sin verificar)**.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
