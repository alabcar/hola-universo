---
title: "Semana 39 · ¿Cuántas estrellas hay cerca del Sol y de qué tipo?"
description: "Fase 4 · El universo grande. Estadística descriptiva: tablas de frecuencias, histogramas, media, mediana y desviación típica; el censo de las estrellas a menos de 10 pársecs, las enanas rojas y marrones, las poblaciones estelares, los sesgos de selección y las estrellas vecinas que puedes ver."
sidebar:
  order: 39
  label: "39. ¿Cuántas estrellas hay cerca del Sol y de qué tipo?"
---

## La pregunta del cielo

Si sales una noche despejada y cuentas las estrellas que ves, la mayoría serán estrellas luminosas a cientos de años luz: gigantes, supergigantes, estrellas blancas de tipo A y B. Podrías pensar que así son las estrellas típicas. Sería como juzgar cómo es la gente de un país por los que salen en televisión.

Para saber cómo es una estrella **típica**, hay que hacer un censo completo de un volumen: contar todas las estrellas que hay en una esfera alrededor del Sol, también las más débiles. Es lo que hicieron en 2021 un grupo de astrónomos europeos, con la participación del Centro de Astrobiología de Madrid, con los datos de Gaia: dentro de 10 pársecs (unos 33 años luz) hay unas 540 estrellas, enanas marrones y planetas conocidos, en unos 340 sistemas. Y la mayoría de esas estrellas no se ven a simple vista. Esta semana aprendes las herramientas de la estadística para describir una población, y las aplicas a la población de estrellas de nuestro vecindario.

:::note[De dónde viene la palabra]
**Estadística** viene del italiano *statista*, «hombre de Estado», y del alemán *Statistik*, término acuñado en el siglo XVIII para los datos que necesitaba el Estado: población, impuestos, cosechas. **Censo** viene del latín *census*, el recuento de ciudadanos y bienes que hacían en Roma los *censores*. **Población**, en estadística, es el conjunto entero que se estudia, y **muestra**, la parte que se observa.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: tablas, frecuencias e histogramas (35-45 min)

**Variables cualitativas y cuantitativas.** De cada estrella del censo tenemos datos de dos clases. Unos son **cualitativos** (o categóricos): el tipo espectral (O, B, A, F, G, K, M), la constelación. Otros son **cuantitativos**, números: la distancia, la magnitud absoluta, la temperatura.

**Tablas de frecuencias.** Para una variable cualitativa se cuenta cuántas veces aparece cada valor: es la **frecuencia absoluta**. Dividida por el total, la **frecuencia relativa**, que se suele dar en porcentaje. Por ejemplo, estas son las estrellas a menos de 10 pc del catálogo HYG que usa el cuaderno, por tipo espectral:

| Tipo | Número | Frecuencia relativa |
|---|---|---|
| A | 5 | 2 % |
| F | 8 | 3 % |
| G | 19 | 7 % |
| K | 55 | 20 % |
| M | 164 | 60 % |
| Enanas blancas | 16 | 6 % |
| Sin clasificar | 5 | 2 % |
| Total | 272 | 100 % |

(El catálogo HYG no incluye las enanas marrones ni algunas enanas rojas muy débiles, pero la proporción de tipos M coincide con la del censo de 2021, un 61 %.)

**Histogramas.** Para una variable cuantitativa, como la magnitud absoluta, no tiene sentido contar cada valor (casi nunca se repiten). Se agrupan en **intervalos** (en inglés, *bins*) y se cuenta cuántos datos caen en cada uno. El dibujo con una barra por intervalo es un **histograma**. La forma del histograma depende de la anchura de los intervalos: con intervalos muy anchos se pierde el detalle; con muy estrechos, todo es ruido. No hay una regla perfecta: se prueba.

**Ejercicios**

1. Con la tabla anterior, ¿qué porcentaje de las estrellas cercanas son más frías que el Sol (tipos K y M)? ¿Y cuántas son de tipo G, como el Sol?
2. Si en una esfera de 10 pc hay unas 330 estrellas y enanas marrones, ¿cuántas hay por pársec cúbico? ¿Y cuántas esperarías en una esfera de 20 pc, si la densidad fuera la misma?
3. En una muestra de 50 estrellas, 18 son de tipo G. ¿Qué frecuencia relativa tienen? ¿Se parece a la del censo? ¿Qué te dice eso de cómo se eligió la muestra?

<details>
<summary>Soluciones</summary>

1. $20 + 60 =$ **80 %**, y más si contaras las enanas marrones. De tipo G, solo un **7 %**.
2. Volumen: $\tfrac{4}{3}\pi\,10^3 \approx 4190$ pc³; densidad $330/4190 \approx$ **0,08 por pc³**, una cada 12 pc³. En 20 pc, el volumen es $2^3 = 8$ veces mayor: unas **2600**.
3. $18/50 =$ **36 %**, cinco veces más que en el censo. La muestra no es representativa: seguramente se eligieron estrellas brillantes, o parecidas al Sol a propósito.

</details>

### Sesión 2 · Matemáticas: media, mediana y desviación típica (35-45 min)

**Medidas de centro.** Para resumir una lista de números $x_1, x_2, \dots, x_N$ con uno solo:

- La **media** (aritmética): $\bar{x} = \frac{1}{N}\sum_{i=1}^{N} x_i$. La letra griega $\Sigma$ (sigma mayúscula) significa «suma»: suma todos los $x_i$, desde $i = 1$ hasta $N$.
- La **mediana**: el valor que queda en el medio cuando ordenas los datos. La mitad de los datos está por debajo y la mitad por encima.
- La **moda**: el valor (o el intervalo) más frecuente.

La media es sensible a los valores extremos; la mediana, no. Si en una sala con diez personas entra alguien con una fortuna enorme, la renta media se dispara, pero la mediana casi no cambia.

**Medidas de dispersión.** Dos poblaciones pueden tener la misma media y ser muy distintas. La **varianza** mide cuánto se apartan los datos de la media, como la media de los cuadrados de las desviaciones:

$$s^2 = \frac{1}{N-1}\sum_{i=1}^{N}(x_i - \bar{x})^2,$$

y la **desviación típica** $s$ es su raíz cuadrada, en las mismas unidades que los datos. (Se divide por $N - 1$ y no por $N$ porque la media se ha calculado con los mismos datos; para muestras grandes da igual.) Para una población con forma de campana, alrededor de dos tercios de los datos están a menos de una desviación típica de la media (lo verás en la semana 42).

Otra forma de describir la dispersión son los **cuartiles**: los valores que dejan por debajo el 25 %, el 50 % (la mediana) y el 75 % de los datos.

**Ejercicios**

1. Calcula la media, la mediana y la desviación típica de las magnitudes absolutas 1,4; 4,8; 5,7; 10,5; 13,2 (Sirio, el Sol, α Centauri B, una enana roja y la estrella de Barnard).
2. Añade Rigel ($M = -7$). ¿Cuánto cambian la media y la mediana?
3. ¿Por qué, para describir «la estrella típica» del vecindario, es mejor la mediana que la media de la luminosidad (no de la magnitud)?

<details>
<summary>Soluciones</summary>

1. Media: $35{,}6/5 =$ **7,12**. Mediana: **5,7**. Desviaciones: $-5{,}72; -2{,}32; -1{,}42; 3{,}38; 6{,}08$; cuadrados: $32{,}7; 5{,}4; 2{,}0; 11{,}4; 37{,}0$; suma $88{,}5$; $s^2 = 88{,}5/4 = 22{,}1$, $s \approx$ **4,7**.
2. Media: $28{,}6/6 \approx$ **4,77**; mediana, entre 4,8 y 5,7: **5,25**. La media baja más de dos magnitudes; la mediana, menos de media.
3. Porque las luminosidades abarcan muchos órdenes de magnitud: una sola estrella como Sirio pesa en la media de luminosidad más que cientos de enanas rojas. La mediana, en cambio, cae en una enana roja, que es lo típico.

</details>

### Sesión 3 · Física: el vecindario del Sol (35-45 min)

**El censo de 10 pársecs.** El trabajo de Céline Reylé y colaboradores, publicado en 2021, reunió todos los objetos conocidos a menos de 10 pc combinando Gaia con otros catálogos: unas 540 estrellas, enanas marrones y exoplanetas, en unos 340 sistemas. Sus conclusiones:

- **La mayoría son enanas rojas**: el 61 % de las estrellas y enanas marrones son de tipo M. Ninguna se ve a simple vista: la más brillante del vecindario apenas llega al límite.
- **El Sol no es una estrella media**: es más luminoso que alrededor del 90 % de sus vecinas.
- Hay una veintena de **enanas blancas** y decenas de **enanas marrones**.
- Alrededor de un **27 %** de los sistemas son dobles o múltiples.

**Las enanas marrones.** Son objetos con menos de unas 0,08 masas solares (unas 80 masas de Júpiter): no alcanzan la temperatura central para fundir hidrógeno de forma estable (semanas 34 y 35). Brillan débilmente en el infrarrojo, sobre todo por el calor de su contracción, y se van enfriando. Durante décadas solo eran una predicción. Las dos primeras se confirmaron en 1995: Gliese 229B, compañera de una enana roja, y **Teide 1**, en las Pléyades, descubierta por astrónomos del Instituto de Astrofísica de Canarias con el telescopio IAC-80 del Observatorio del Teide.

**Poblaciones estelares.** En 1944, Walter Baade aprovechó los apagones de guerra de Los Ángeles, que oscurecían el cielo del observatorio de Monte Wilson, para estudiar la galaxia de Andrómeda con un detalle sin precedentes. Vio que las estrellas se dividen en dos grandes familias:

- **Población I**: estrellas jóvenes o de edad intermedia, ricas en elementos pesados («metales», en la jerga astronómica: todo lo que no es hidrógeno o helio), en el disco y los brazos espirales. El Sol es una estrella de población I.
- **Población II**: estrellas viejas, pobres en metales, en el halo y los cúmulos globulares.

La diferencia es la historia química de la galaxia (semana 36): las estrellas que nacieron primero se formaron de gas casi sin metales; las que nacieron después, de gas ya enriquecido por generaciones de supernovas. Se habla también, de forma teórica, de una **población III**: las primeras estrellas, sin ningún metal, que nadie ha observado directamente.

**El sesgo de selección.** Las estrellas que ves en el cielo no son una muestra justa: un catálogo limitado en **magnitud aparente** (todas las estrellas más brillantes que cierta magnitud) está lleno de estrellas luminosas, que se ven desde lejos, y casi vacío de enanas rojas, que solo se ven si están muy cerca. Un catálogo limitado en **volumen** (todas las estrellas dentro de cierta distancia) es el único que da la proporción real. Confundirlos es uno de los errores más comunes al leer datos astronómicos (y no astronómicos).

:::note[De dónde viene la palabra]
**Media** viene del latín *medius*, «que está en medio». **Mediana**, de *medianus*, «del medio». **Moda** viene del francés *mode*, «manera, costumbre»: lo que más se lleva. **Varianza** es una palabra del siglo XX, de *variar*, propuesta por el estadístico Ronald Fisher en 1918. **Histograma** la usó Karl Pearson en 1891, probablemente a partir del griego *histós*, «mástil, palo vertical», y *grámma*, «dibujo»: un dibujo de barras.
:::

**Qué hacer**

1. Ordena de más a menos frecuentes en la galaxia: estrellas como el Sol, enanas rojas, gigantes rojas, supergigantes azules. Ordénalas después por lo frecuentes que son entre las estrellas visibles a simple vista.
2. ¿Por qué es más fácil completar un censo hasta 10 pc que hasta 100 pc?
3. Si las enanas marrones se enfrían con el tiempo, ¿por qué las más viejas son más difíciles de encontrar?

### Sesión 4 · Astronomía y observación: tus vecinas visibles (30-45 min)

**Pocas, pero se ven.** De los unos 340 sistemas a menos de 10 pc, solo unas cincuenta estrellas son más brillantes que la magnitud 6. Algunas visibles desde España en estas noches de otoño e invierno:

| Estrella | Distancia | Tipo | Dónde |
|---|---|---|---|
| Sirio | 8,6 años luz | A1 + enana blanca | Can Mayor |
| ε Eridani | 10,5 años luz | K2, con un planeta | Erídano, bajo al sur |
| Proción | 11,5 años luz | F5 + enana blanca | Can Menor |
| 61 Cygni | 11,4 años luz | K5 + K7 | Cisne |
| τ Ceti | 11,9 años luz | G8 | Ballena |
| η Cassiopeiae (Achird) | 19 años luz | G0 + K7 | Casiopea |
| Fomalhaut | 25 años luz | A3 | Pez Austral, bajo al sur a primera hora |
| Vega | 25 años luz | A0 | Lira, al oeste |

**Un ejercicio de imaginación.** Elige una de las estrellas de la tabla. Busca en Stellarium o en un mapa las enanas rojas que hay cerca de ella en el cielo y a una distancia parecida: no las verás, ni con los prismáticos, pero están ahí, y son la mayoría. Si tus ojos fueran mucho más sensibles, el cielo estaría lleno de puntos rojos débiles repartidos por todas partes, más que de estrellas blancas brillantes concentradas en la Vía Láctea.

**τ Ceti, una gemela algo mayor del Sol.** Es la estrella aislada más parecida al Sol entre las muy cercanas: algo menos masiva, más vieja y pobre en metales. En las noches de otoño está al sur, bajo la cabeza de la Ballena. Con magnitud 3,5, se ve desde un cielo suburbano. Mírala con los prismáticos y compárala con el Sol de la semana 34: así se vería el Sol desde 12 años luz, una estrella discreta de tercera magnitud.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 39:

- clasifica por tipo espectral las estrellas del catálogo HYG a menos de 10 pc y hace la tabla de frecuencias,
- dibuja histogramas de la magnitud absoluta con distintas anchuras de intervalo y calcula media, mediana, desviación típica y cuartiles,
- comprueba si el catálogo está completo comparando el número de estrellas con el que crecería como $r^3$,
- compara una muestra limitada en volumen con una limitada en magnitud aparente,
- incluye, como opción no probada, una consulta al archivo de Gaia de las estrellas a menos de 10 pc.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-39.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-39.ipynb)

## Qué has aprendido

- **La respuesta.** Dentro de 10 pársecs hay unas 540 estrellas, enanas marrones y planetas conocidos, en unos 340 sistemas. La gran mayoría de las estrellas son enanas rojas, invisibles a simple vista; el Sol es más luminoso que nueve de cada diez vecinas.
- **La lección.** Las estrellas que vemos no son las típicas: un catálogo limitado en brillo favorece a las luminosas. Solo un censo por volumen da la proporción real.
- **Las herramientas.** Tablas de frecuencias, histogramas, media, mediana, moda, varianza, desviación típica y cuartiles, y la idea de sesgo de selección.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**El sesgo de Malmquist.** Imagina que todas las estrellas de cierto tipo tienen magnitudes absolutas parecidas, repartidas en campana alrededor de un valor medio $M_0$ con una desviación típica $\sigma$. Si haces un catálogo de todas las que se ven más brillantes que cierta magnitud aparente, ¿cuál será la media de sus magnitudes absolutas?

No será $M_0$. Las más luminosas de ese tipo (con $M$ menor que $M_0$) se ven desde más lejos, y en un volumen mayor caben más estrellas. Así que en el catálogo hay más estrellas de las brillantes que de las débiles, y la media sale más brillante de lo que es. En 1922, el sueco Gunnar Malmquist calculó cuánto, para estrellas repartidas con densidad uniforme en el espacio:

$$\langle M\rangle_\text{catálogo} = M_0 - 1{,}38\,\sigma^2.$$

**Por qué aparece $1{,}38$.** El número de estrellas que ves hasta una magnitud aparente $m$ crece como el volumen, $d^3$. Para una estrella de magnitud absoluta $M$, la distancia máxima a la que la ves cumple $m - M = 5\log(d/10)$, así que $d \propto 10^{-0{,}2M}$ y el volumen $\propto 10^{-0{,}6M}$. Al multiplicar la campana de las $M$ por ese factor exponencial, la campana se desplaza hacia las $M$ pequeñas una cantidad $0{,}6\ln(10)\,\sigma^2 \approx 1{,}38\,\sigma^2$ (es una propiedad de las campanas de Gauss multiplicadas por exponenciales que puedes comprobar con el cuaderno).

Lo descubrió estudiando estrellas, pero el sesgo aparece en cualquier muestra seleccionada por un umbral: galaxias lejanas, encuestas, ensayos... El cuaderno lo comprueba con una simulación.

**Ejercicios**

1. Si las estrellas de un tipo tienen $\sigma = 0{,}5$ magnitudes, ¿cuánto más brillantes parecen, de media, en un catálogo limitado en magnitud aparente?
2. Si usaras esa magnitud media sesgada para calcular distancias, ¿saldrían mayores o menores de lo real? ¿Cuánto, en porcentaje, para $\sigma = 0{,}5$? (Pista: un error de $\Delta M$ en magnitud cambia la distancia en un factor $10^{0{,}2\Delta M}$.)
3. ¿Afecta este sesgo a un censo limitado en volumen, como el de 10 pc?

<details>
<summary>Soluciones</summary>

1. $1{,}38 \cdot 0{,}25 \approx$ **0,35 magnitudes** más brillantes.
2. Si crees que las estrellas son más luminosas de lo que son, calculas que están más lejos: **mayores**, en un factor $10^{0{,}2 \cdot 0{,}35} \approx 1{,}17$, un **17 %**.
3. **No**: en un censo por volumen están todas, brillantes y débiles, así que no hay selección por brillo (si el censo está completo).

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [The 10 parsec sample in the Gaia era (Reylé y colaboradores, 2021, *Astronomy & Astrophysics*)](https://arxiv.org/abs/2104.14972v2). Inglés; el artículo del censo, de acceso abierto. Nivel avanzado, pero la introducción y las figuras se entienden bien. Verificado el 20 de noviembre de 2026.
2. [18.1 Un censo estelar, *Astronomía* (OpenStax), capítulo 18, en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/18%3A_Las_Estrellas_-_Un_Censo_Celestial). Español; las estrellas cercanas, las más brillantes y por qué son distintas. Verificado el 20 de noviembre de 2026 (el capítulo).
3. [Capítulo 25, La Vía Láctea, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/25%3A_La_V%C3%ADa_L%C3%A1ctea). Español; poblaciones estelares. Verificado el 20 de noviembre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno. Los datos de estrellas proceden de la base HYG v4.1 (David Nash, CC BY-SA 4.0).
