---
title: "Semana 14 · ¿Por qué las órbitas son elipses?"
description: "Fase 2 · Órbitas. La elipse, sus ejes, sus focos y su excentricidad; primera y segunda leyes de Kepler; perihelio y afelio."
sidebar:
  order: 14
  label: "14. ¿Por qué las órbitas son elipses?"
---

## La pregunta del cielo

Desde los griegos hasta Copérnico, todos los modelos del cielo usaron círculos. El círculo se consideraba la figura perfecta, la única digna de los cielos. Copérnico puso el Sol en el centro, pero mantuvo los círculos, y sus predicciones no eran mucho mejores que las de Ptolomeo.

A principios del siglo XVII, Johannes Kepler trabajó durante años con las observaciones de Marte de Tycho Brahe, las más precisas que se habían hecho a simple vista. Ningún círculo encajaba: siempre quedaba un error de unos 8 minutos de arco, un cuarto del tamaño de la Luna llena. Kepler confió en los datos de Tycho y abandonó el círculo. En 1609, en su *Astronomia nova*, publicó que Marte recorre una **elipse** con el Sol en uno de sus focos, y que no se mueve siempre a la misma velocidad.

Esta semana aprendes qué es exactamente una elipse, cómo se mide lo alargada que es y qué dicen las dos primeras leyes de Kepler. El *porqué* de las elipses llegará con Newton (semanas 16 y 17): una fuerza que se debilita con el cuadrado de la distancia produce exactamente esta figura.

## Las cinco sesiones

### Sesión 1 · Matemáticas: la elipse y sus partes (35-45 min)

**Definición.** Clava dos chinchetas en un tablero, separadas unos centímetros. Ata a ellas los extremos de un hilo más largo que la distancia entre las chinchetas. Tensa el hilo con un lápiz y da la vuelta completa manteniéndolo tenso. La curva que dibujas es una elipse. Las dos chinchetas son los **focos**, y la propiedad que has usado es la definición:

> Una **elipse** es el conjunto de puntos del plano cuya suma de distancias a dos puntos fijos (los focos) es constante.

Si juntas las dos chinchetas en una sola, el hilo siempre está a la misma distancia del centro: sale una circunferencia. La circunferencia es una elipse con los dos focos en el mismo sitio.

**Las partes.** La elipse tiene dos ejes de simetría que se cruzan en el **centro**:

- El **eje mayor** es el diámetro más largo; pasa por los dos focos. Su mitad se llama **semieje mayor** y se escribe $a$. Es el número más importante de una órbita: veremos que de él depende el periodo.
- El **eje menor** es el diámetro más corto, perpendicular al anterior. Su mitad es el **semieje menor**, $b$.
- La distancia del centro a cada foco se llama $c$.

Si pones el lápiz en un extremo del eje mayor, el hilo va de un foco a ese extremo y vuelve al otro foco: mide exactamente $2a$. Así que la constante de la definición es $2a$. Si pones el lápiz en un extremo del eje menor, el hilo forma dos triángulos rectángulos iguales, de catetos $b$ y $c$ e hipotenusa $a$. Por Pitágoras:

$$a^2 = b^2 + c^2.$$

**La ecuación.** Con el centro en el origen y el eje mayor sobre el eje $x$, los puntos de la elipse cumplen

$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1.$$

Si $a = b$, es la ecuación de una circunferencia de radio $a$. Para dibujarla en el ordenador es más cómodo escribir cada punto con un ángulo auxiliar $t$, como hiciste con la circunferencia la semana pasada: $x = a\cos t$, $y = b\sin t$. Es una circunferencia «aplastada» en vertical por el factor $b/a$.

**La excentricidad.** Para medir lo alargada que es una elipse se usa la **excentricidad**:

$$e = \frac{c}{a}.$$

Vale 0 en una circunferencia (los focos coinciden con el centro) y se acerca a 1 a medida que la elipse se estira. No depende del tamaño, solo de la forma: dos elipses con la misma excentricidad son la misma figura a distinta escala.

:::note[De dónde viene la palabra]
Las palabras **elipse**, **parábola** e **hipérbola** las fijó Apolonio de Perga hacia el 200 a. C., en su estudio de las secciones de un cono. Las tres vienen de una comparación entre áreas. *Parabolḗ* significa «poner al lado, comparar»: el área encaja exactamente. *Élleipsis* significa «falta, defecto»: el área se queda corta. *Hyperbolḗ* significa «exceso»: el área se pasa. De ahí también la *elipsis* gramatical (falta una palabra) y la *hipérbole* (exagerar).

**Foco** es una palabra latina que significa «hogar, fuego». Kepler la usó en 1604, en un libro de óptica, para el punto donde un espejo curvo concentra los rayos del Sol hasta quemar. **Excentricidad** viene de *ex*, «fuera de», y *centrum*, «centro»: lo lejos que está el foco del centro.
:::

**Ejercicios**

1. Una elipse tiene $a = 5$ y $b = 3$. Calcula $c$ y la excentricidad.
2. Una elipse tiene $a = 10$ y $e = 0{,}6$. ¿Cuánto vale $b$?
3. Si haces la elipse de las chinchetas con un hilo de 20 cm y las chinchetas a 12 cm, ¿cuánto miden los dos ejes?
4. ¿El punto $(4, 1{,}8)$ está sobre la elipse del ejercicio 1, dentro o fuera?

<details>
<summary>Soluciones</summary>

1. $c = \sqrt{a^2 - b^2} = \sqrt{25 - 9} =$ **4**, y $e = 4/5 =$ **0,8**.
2. $c = e\,a = 6$ y $b = \sqrt{100 - 36} =$ **8**.
3. El hilo mide $2a = 20$ cm, así que el eje mayor mide **20 cm**. Los focos están a $2c = 12$ cm, así que $c = 6$ y $b = \sqrt{100 - 36} = 8$: el eje menor mide **16 cm**.
4. $16/25 + 3{,}24/9 = 0{,}64 + 0{,}36 = 1$: está **sobre** la elipse.

</details>

### Sesión 2 · Matemáticas: la elipse vista desde un foco (30-40 min)

En una órbita, lo interesante no es el centro de la elipse, que está vacío, sino el foco, donde está el Sol. Necesitamos saber a qué distancia del foco está cada punto.

**Los dos extremos.** El punto de la elipse más cercano al foco es el extremo del eje mayor que queda de su lado, a una distancia $a - c$. El más lejano es el otro extremo, a $a + c$. Como $c = e\,a$:

$$r_\text{mín} = a(1 - e), \qquad r_\text{máx} = a(1 + e).$$

Y al revés: si mides la distancia mínima y la máxima, $a$ es su media, $a = (r_\text{mín} + r_\text{máx})/2$. Por eso al semieje mayor también se le llama **distancia media**.

**Cualquier punto.** Si mides el ángulo $\theta$ desde el foco, empezando en la dirección del punto más cercano, la distancia al foco es

$$r(\theta) = \frac{a(1 - e^2)}{1 + e\cos\theta}.$$

No hace falta que la memorices; basta con comprobar que tiene sentido. Con $\theta = 0$, $\cos\theta = 1$ y queda $a(1-e^2)/(1+e) = a(1-e)$, la distancia mínima (usando $1 - e^2 = (1-e)(1+e)$). Con $\theta = 180^\circ$, $\cos\theta = -1$ y queda $a(1+e)$, la máxima. Con $e = 0$ queda $r = a$ siempre: una circunferencia. Esta forma de escribir la elipse es la que sale directamente de las leyes de Newton.

**Ejercicios**

1. El cometa Halley tiene $a = 17{,}8$ ua y $e = 0{,}967$. ¿Cuánto se acerca al Sol y cuánto se aleja? Compara con las órbitas de la Tierra (1 ua) y de Neptuno (30 ua).
2. Una órbita tiene distancia mínima 2 ua y máxima 6 ua. Calcula $a$ y $e$.
3. Con $a = 1$ y $e = 0{,}5$, calcula $r$ para $\theta = 90^\circ$.

<details>
<summary>Soluciones</summary>

1. $r_\text{mín} = 17{,}8 \cdot 0{,}033 \approx$ **0,59 ua**, más cerca del Sol que Venus. $r_\text{máx} = 17{,}8 \cdot 1{,}967 \approx$ **35 ua**, más allá de Neptuno.
2. $a = (2 + 6)/2 =$ **4 ua**. De $a(1 - e) = 2$ sale $1 - e = 0{,}5$: **$e = 0{,}5$**.
3. $\cos 90^\circ = 0$, así que $r = a(1 - e^2) = 1 - 0{,}25 =$ **0,75**.

</details>

### Sesión 3 · Física: primera y segunda leyes de Kepler (30-40 min)

**Primera ley (1609).** *Cada planeta recorre una elipse, y el Sol está en uno de sus focos.* El otro foco está vacío: no hay nada en él.

El punto de la órbita más cercano al Sol es el **perihelio** y el más lejano, el **afelio**. La línea que los une es el eje mayor, también llamado **línea de los ápsides**. Para órbitas alrededor de la Tierra se dice **perigeo** y **apogeo**.

**Segunda ley (1609).** *La línea que une el Sol con el planeta barre áreas iguales en tiempos iguales.* Imagina un radio elástico que va del Sol al planeta y que va pintando la superficie que recorre. En un mes pinta siempre la misma área, esté donde esté el planeta. Cerca del perihelio el radio es corto, así que para pintar la misma área el planeta tiene que recorrer más arco: va más deprisa. Cerca del afelio el radio es largo y basta un arco corto: va más despacio.

En los dos extremos, la velocidad es perpendicular al radio y el área barrida en un instante es un triángulo de base $v\,\Delta t$ y altura $r$. Igualar las dos áreas da $r_\text{p}\,v_\text{p} = r_\text{a}\,v_\text{a}$, de donde

$$\frac{v_\text{p}}{v_\text{a}} = \frac{r_\text{a}}{r_\text{p}} = \frac{1 + e}{1 - e}.$$

Hoy sabemos que la segunda ley es la **conservación del momento angular**: la fuerza del Sol siempre apunta hacia el Sol y no puede hacer girar el planeta más deprisa ni más despacio alrededor de él.

**La Tierra.** La excentricidad de la órbita terrestre es pequeña, $e \approx 0{,}0167$. Su distancia al Sol varía entre unos 147,1 millones de km en el perihelio, a principios de enero, y unos 152,1 millones en el afelio, a principios de julio. En el hemisferio norte es invierno cuando estamos más cerca del Sol: las estaciones las produce la inclinación del eje (semana 1), no la distancia. Pero la segunda ley sí se nota: la Tierra va más deprisa en enero, y por eso el semestre de otoño e invierno del hemisferio norte (del equinoccio de septiembre al de marzo) dura unos 179 días, y el de primavera y verano, unos 186.

:::note[De dónde viene la palabra]
**Perihelio** y **afelio** son palabras griegas compuestas: *perí*, «alrededor, cerca», *apó*, «lejos de», y *hḗlios*, «Sol». Con *gê*, «Tierra», salen **perigeo** y **apogeo**. **Ápside** viene del griego *hapsís*, «arco, bóveda», y también «rueda»; de la misma palabra viene el *ábside* de las iglesias. **Órbita** viene del latín *orbita*, «rodada, el surco que deja una rueda en el camino», de *orbis*, «círculo, rueda». La palabra guarda la idea antigua de los círculos.
:::

**Qué hacer**

1. Calcula la razón entre la velocidad de la Tierra en el perihelio y en el afelio. ¿En qué porcentaje cambia?
2. Haz lo mismo para Mercurio ($e = 0{,}206$) y para el cometa Halley ($e = 0{,}967$).
3. Explica por qué la excentricidad de la Tierra no es la causa de las estaciones. Pista: ¿qué pasaría en el hemisferio sur si lo fuera?

<details>
<summary>Soluciones</summary>

1. $(1{,}0167)/(0{,}9833) \approx$ **1,034**: un 3,4 % más rápida en el perihelio. Con una velocidad media de 29,8 km/s, son unos 30,3 km/s en enero y 29,3 km/s en julio.
2. Mercurio: $1{,}206/0{,}794 \approx$ **1,52**. Halley: $1{,}967/0{,}033 \approx$ **60**: en el perihelio va unas sesenta veces más deprisa que en el afelio.
3. Si la distancia causara las estaciones, los dos hemisferios tendrían verano a la vez, en enero. Pero cuando en el hemisferio norte es invierno, en el sur es verano. Además, la variación de distancia es de solo un 3 %.

</details>

### Sesión 4 · Astronomía y observación: la excentricidad en el cielo (30-45 min)

Las órbitas de los planetas son elipses, pero casi todas muy parecidas a una circunferencia. Esta es la excentricidad de los ocho planetas según la hoja de datos de la NASA:

| Planeta | Excentricidad | Distancia mínima / máxima |
|---|---|---|
| Mercurio | 0,206 | 0,66 |
| Venus | 0,007 | 0,99 |
| Tierra | 0,017 | 0,97 |
| Marte | 0,094 | 0,83 |
| Júpiter | 0,049 | 0,91 |
| Saturno | 0,057 | 0,89 |
| Urano | 0,046 | 0,91 |
| Neptuno | 0,011 | 0,98 |

Si dibujaras la órbita de la Tierra con un compás, a escala, la diferencia con la elipse real sería menor que el grosor del trazo. Lo que sí se nota es que el Sol no está en el centro. Eso explica que Kepler necesitara datos tan buenos: con la excentricidad de Marte, el círculo falla por solo unos minutos de arco.

**Comprueba la excentricidad de la Tierra con Stellarium.** El tamaño aparente del Sol depende de la distancia, como viste en la semana 2. En Stellarium, selecciona el Sol (sin mirarlo nunca de verdad) y lee su **diámetro aparente** en el panel de información en dos fechas: el 3 de enero y el 4 de julio. Deberías encontrar unos 32′ 32″ y unos 31′ 28″. Con esos dos números:

1. Calcula la razón entre las dos distancias. Recuerda que el tamaño aparente es inversamente proporcional a la distancia.
2. Deduce la excentricidad con $r_\text{máx}/r_\text{mín} = (1+e)/(1-e)$. Despejando, $e = (k - 1)/(k + 1)$, donde $k$ es la razón.

Con los valores de arriba, $k = 1952/1888 \approx 1{,}034$ y $e \approx 0{,}017$. Acabas de medir la forma de la órbita de la Tierra con un programa de planetario y una regla de tres.

:::caution[Seguridad]
No mires nunca al Sol directamente, ni con prismáticos ni con telescopio sin un filtro solar homologado. Esta actividad se hace en Stellarium.
:::

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 14:

- dibuja elipses con distintas excentricidades y marca sus focos,
- comprueba con números que la suma de distancias a los focos es siempre $2a$,
- coloca un planeta en una órbita muy excéntrica, calcula su posición a intervalos de tiempo iguales y mide las áreas barridas para comprobar la segunda ley de Kepler.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-14.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-14.ipynb)

## Qué has aprendido

- **La respuesta.** Las órbitas son elipses porque así lo exigen los datos: Kepler lo descubrió al ver que ningún círculo encajaba con las observaciones de Marte. La causa física, una fuerza que disminuye con el cuadrado de la distancia, la encontró Newton y la verás en las próximas semanas.
- **Las leyes.** Primera: los planetas recorren elipses con el Sol en un foco. Segunda: el radio Sol-planeta barre áreas iguales en tiempos iguales, así que el planeta va más deprisa en el perihelio que en el afelio.
- **Las herramientas.** La elipse como suma constante de distancias, la relación $a^2 = b^2 + c^2$, la excentricidad $e = c/a$, las distancias $a(1 \pm e)$ y la ecuación vista desde el foco, $r = a(1-e^2)/(1 + e\cos\theta)$.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 13.5, Leyes del movimiento planetario de Kepler, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-5-leyes-del-movimiento-planetario-de-kepler). Español, nivel universitario con cálculo; las secciones cónicas, las tres leyes y las transferencias orbitales. Te servirá también para las semanas 15 y 18. Verificado el 6 de noviembre de 2026.
2. [Unidad 5: Las leyes del movimiento planetario (Proyecto PETeR, Instituto de Astrofísica de Canarias)](https://outreach.iac.es/peter/wp-content/uploads/2025/10/Unidad-5-Leyes-del-Movimiento_Intro.pdf). Español, nivel divulgativo; historia de Tycho, Kepler y Newton y las tres leyes. Verificado el 6 de noviembre de 2026.
3. [6.4 Leyes de Kepler, *Mecánica y relatividad* de Timon Idema (LibreTexts en español)](https://espanol.libretexts.org/Fisica/Libro%3A_Mecanica_y_Relatividad_(Idema)/06%3A_Movimiento_Planar_General/6.04%3A_Leyes_de_Kepler). Español, nivel universitario; demuestra las leyes de Kepler a partir de las de Newton. Para cuando quieras ir más lejos. Verificado el 6 de noviembre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

Las excentricidades de la tabla proceden de la hoja de datos planetarios de la NASA (NSSDC), tal como la reproducen varias páginas de divulgación. No he podido abrir la hoja original. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
