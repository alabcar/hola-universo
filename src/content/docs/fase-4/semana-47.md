---
title: "Semana 47 · ¿Cómo sabemos que hay planetas en otras estrellas?"
description: "Fase 4 · El universo grande. Señal y ruido, plegar una curva en fase y buscar periodos; los métodos de la velocidad radial y de los tránsitos, 51 Pegasi b, Kepler, TESS y el Webb; la zona habitable; estrellas con planetas visibles con prismáticos y la ciencia ciudadana con datos de TESS."
sidebar:
  order: 47
  label: "47. ¿Cómo sabemos que hay planetas en otras estrellas?"
---

## La pregunta del cielo

Durante siglos fue una especulación: ¿tienen planetas las demás estrellas? Giordano Bruno lo afirmó en el siglo XVI; muchos lo pensaron después. Pero un planeta es mil millones de veces más débil que su estrella y está, visto desde aquí, pegado a ella. Verlo directamente parecía imposible.

En octubre de 1995, dos astrónomos suizos, Michel Mayor y Didier Queloz, anunciaron que la estrella **51 Pegasi**, visible a simple vista en el cuadrado de Pegaso, se acercaba y se alejaba de nosotros a unos 50 m/s, la velocidad de un coche por autopista, con un periodo de 4,2 días. Algo la hacía bailar: un planeta como Júpiter, pero tan cerca de su estrella que daba una vuelta en cuatro días. Treinta años después, el 8 de octubre de 2026, el archivo de exoplanetas de la NASA contaba **6445 planetas confirmados**. Esta semana aprendes cómo se encuentran, y analizas tú mismo una curva de luz.

:::note[De dónde viene la palabra]
**Exoplaneta** une el prefijo griego *éxō*, «fuera», y *planeta*, «errante» (semana 13): un planeta de fuera del Sistema Solar. **Tránsito** viene de *transitus*, «paso», de *transire*, «pasar al otro lado»: el paso de un planeta por delante del disco de su estrella. 51 Pegasi y su planeta recibieron en 2015, por votación pública de la Unión Astronómica Internacional, los nombres de **Helvetios** (por el pueblo celta de la actual Suiza) y **Dimidium** («mitad» en latín, porque tiene la mitad de masa que Júpiter, aproximadamente).
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: señal, ruido y plegar en fase (35-45 min)

**Señal y ruido.** Cuando un planeta pasa por delante de una estrella como el Sol, le tapa una fracción minúscula de la luz: un 1 % si es como Júpiter, un 0,008 % si es como la Tierra. Las medidas del brillo de una estrella tienen siempre un **ruido**: variaciones aleatorias por la propia estrella, el instrumento o la atmósfera. La pregunta es siempre si la **señal** que buscas es mayor que el ruido. Se mide con el **cociente señal-ruido**: la profundidad de la señal dividida por la desviación típica del ruido. Por debajo de 1, la señal está escondida; para estar razonablemente seguros, los astrónomos piden 7 o más.

**Promediar ayuda.** Si cada medida tiene un ruido $\sigma$, la media de $N$ medidas tiene un ruido $\sigma/\sqrt{N}$ (semana 40). Un tránsito que dura 3 horas, medido cada 2 minutos, tiene 90 medidas: su profundidad se mide con un ruido $\sqrt{90} \approx 9{,}5$ veces menor que el de cada medida.

**Plegar en fase.** Si un planeta pasa por delante cada $P$ días, puedes sumar todos sus tránsitos «doblando» los datos: para cada medida, en lugar del tiempo $t$, usas la **fase**, el resto de dividir el tiempo por el periodo,

$$\text{fase} = \frac{t - t_0}{P} \bmod 1,$$

un número entre 0 y 1 que dice en qué momento del ciclo está. Es la aritmética modular de la semana 4, la del reloj. Si el periodo es el correcto, todos los tránsitos caen uno encima de otro y la señal se refuerza. Si no, se dispersan y se borran.

**Ejercicios**

1. Un tránsito tiene una profundidad de 0,1 % y cada medida tiene un ruido de 0,5 %. ¿Cuál es el cociente señal-ruido de una medida? ¿Cuántas medidas dentro del tránsito necesitas para llegar a 7?
2. Un planeta tiene $P = 3{,}5$ días y $t_0 = 1{,}2$ días. ¿En qué fase está una medida tomada en $t = 10$ días?
3. ¿Por qué un planeta con un periodo de un año es tan difícil de detectar con una misión que observa cada zona del cielo durante 27 días?

<details>
<summary>Soluciones</summary>

1. $0{,}1/0{,}5 =$ **0,2**. Con $N$ medidas, $0{,}2\sqrt{N} = 7$, así que $N = 35^2 =$ **1225 medidas**.
2. $(10 - 1{,}2)/3{,}5 = 2{,}514$; el resto es **0,514**: a mitad de su órbita (justo enfrente del tránsito, como mucho).
3. Porque en 27 días solo hay un 7 % de probabilidad de que el tránsito caiga dentro, y aunque caiga, solo se vería uno: hacen falta al menos dos o tres para estar seguros del periodo.

</details>

### Sesión 2 · Matemáticas: buscar periodos y ajustar un modelo (35-45 min)

**Buscar el periodo a ciegas.** Si no sabes el periodo, puedes probar muchos. Para cada periodo de prueba, pliegas los datos y miras si aparece una caída. El método más usado para tránsitos, el **ajuste de caja** (en inglés, *Box Least Squares*), modela el tránsito como una caja: un brillo constante con un escalón hacia abajo durante un rato. Para cada periodo, busca la caja que mejor encaja, y calcula cuánto mejora el ajuste respecto a una línea plana. Dibujando esa mejora frente al periodo sale un **periodograma**: el periodo verdadero aparece como un pico (y también sus mitades y sus dobles, que hay que saber reconocer).

**Ajustar un modelo que no es una recta.** En la semana 40 ajustaste rectas con fórmulas. Muchos modelos no son rectas: un tránsito, una curva de velocidad radial, una curva de Planck (semana 42). La idea es la misma: elegir los parámetros que hacen mínimo el $\chi^2$ (semana 41). Cuando no hay fórmula, se buscan con el ordenador: probando una cuadrícula de valores, como hiciste con la curva de rotación de la semana 43, o con métodos que van «bajando» hacia el mínimo. Las herramientas profesionales hacen eso mismo, de forma más eficiente.

**Ejercicios**

1. Un periodograma tiene picos en 2,0, 4,0 y 8,0 días. ¿Cuál puede ser el periodo verdadero? ¿Cómo lo decidirías?
2. Al plegar con un periodo un poco equivocado, ¿qué le pasa a la forma del tránsito plegado?
3. ¿Por qué un ajuste por cuadrícula con 3 parámetros y 100 valores de cada uno es lento? ¿Cuántas combinaciones hay?

<details>
<summary>Soluciones</summary>

1. Puede ser **4 días** (con 2 como su mitad y 8 como su doble), u 8 días con alguna otra señal. Lo decidiría plegando con cada uno: con el doble del verdadero, la mitad de los tránsitos caen en fase 0,5, y la caja solo encaja con la mitad de los datos; con la mitad, en una de cada dos vueltas no hay tránsito.
2. Los tránsitos de los extremos de los datos se desplazan unos respecto a otros: el tránsito plegado sale **más ancho y menos profundo**, emborronado.
3. $100^3 =$ **un millón** de combinaciones, cada una con un cálculo de $\chi^2$ sobre todos los datos.

</details>

### Sesión 3 · Física: los métodos (40-45 min)

**La velocidad radial.** Un planeta y su estrella giran alrededor de su centro de masas común (semana 20). La estrella describe una pequeña órbita, y se acerca y se aleja de nosotros periódicamente. Con el efecto Doppler (semana 41), sus líneas espectrales se desplazan un poquito al azul y al rojo. Júpiter hace que el Sol se mueva a unos 12,5 m/s; la Tierra, a solo 9 cm/s. Los mejores espectrógrafos actuales, como ESPRESSO en el Very Large Telescope de Chile, llegan a medir variaciones de unas decenas de centímetros por segundo. Este método da el periodo y una **masa mínima** del planeta (porque, si la órbita está inclinada, solo vemos la parte de la velocidad que va en nuestra dirección).

**Los tránsitos.** Si la órbita está casi de canto, el planeta pasa por delante de la estrella en cada vuelta y le tapa un poco de luz. La profundidad del tránsito es la fracción del disco tapada:

$$\delta = \left(\frac{R_p}{R_\star}\right)^2.$$

Con el radio de la estrella (de su tipo espectral, semana 35), sale el **radio del planeta**. El periodo y la tercera ley de Kepler (semana 15) dan el tamaño de la órbita. Si además se mide la velocidad radial, se tienen la masa y el radio: la **densidad**, que dice si el planeta es rocoso, de agua o de gas. El primer tránsito se observó en 1999, en el planeta HD 209458 b. Las misiones espaciales Kepler (NASA, 2009-2018) y TESS (NASA, desde 2018) han encontrado así la mayoría de los planetas conocidos.

**Las atmósferas.** Durante un tránsito, una pequeña parte de la luz de la estrella atraviesa la atmósfera del planeta. Comparando el espectro dentro y fuera del tránsito, se ven las líneas de las moléculas de la atmósfera. En 2022, el telescopio James Webb detectó así, por primera vez sin ambigüedad, dióxido de carbono en la atmósfera de un exoplaneta, WASP-39 b.

**Otros métodos.** Las **microlentes** (semana 45), la **imagen directa** (fotografiar el planeta tapando la luz de la estrella con un coronógrafo, posible para planetas jóvenes, calientes y lejos de su estrella), la **astrometría** (medir el vaivén de la estrella en el cielo; los datos de Gaia DR4, previstos para diciembre de 2026, incluirán candidatos detectados así) y el cronometraje de **púlsares**: los primeros exoplanetas confirmados, en 1992, giraban alrededor de un púlsar (semana 36).

**Lo que hemos aprendido.** Los sistemas planetarios son muy distintos del nuestro. Hay **júpiteres calientes**, como 51 Pegasi b, gigantes gaseosos más cerca de su estrella que Mercurio del Sol. Los planetas más comunes en la galaxia parecen ser los **supertierras** y **minineptunos**, de entre una y cuatro veces el radio de la Tierra, un tipo que no existe en el Sistema Solar. Y hay sistemas compactos como **TRAPPIST-1**, una enana roja a 40 años luz con siete planetas del tamaño de la Tierra, todos más cerca de su estrella que Mercurio del Sol.

**La zona habitable.** Es la franja de distancias a una estrella en la que un planeta rocoso, con una atmósfera adecuada, podría tener agua líquida en su superficie. Como el flujo de la estrella cae con el cuadrado de la distancia (semana 30), su distancia escala como la raíz de la luminosidad: alrededor de una enana roja está muy cerca; alrededor de una estrella caliente, muy lejos. Estar en la zona habitable no significa tener vida, ni siquiera agua: Venus y Marte están en el borde de la del Sol.

:::note[De dónde viene la palabra]
**Velocidad radial** es la velocidad a lo largo del **radio** visual, la línea que une la estrella con nosotros (del latín *radius*, semana 30). **Habitable** viene de *habitare*, «vivir en un sitio». **Coronógrafo** une *corona* (semana 34) y *gráphein*, «escribir, dibujar»: lo inventó en 1930 el francés Bernard Lyot para fotografiar la corona del Sol sin esperar a un eclipse, tapando el disco solar dentro del telescopio.
:::

**Qué hacer**

1. ¿Qué profundidad tendría el tránsito de Júpiter ($R = 71\,500$ km) por delante del Sol ($R = 696\,000$ km)? ¿Y el de la Tierra ($R = 6371$ km)?
2. Un planeta transita delante de una enana roja de 0,2 radios solares con una profundidad del 0,5 %. ¿Qué radio tiene, en radios terrestres?
3. ¿Por qué es mucho más fácil encontrar planetas del tamaño de la Tierra alrededor de enanas rojas que alrededor de estrellas como el Sol, con los dos métodos?

### Sesión 4 · Astronomía y observación: estrellas con planetas (30-45 min)

Varias estrellas con planetas se ven a simple vista o con prismáticos. Sus planetas, nunca: son demasiado débiles y están demasiado cerca de la estrella. Pero puedes mirar las estrellas sabiendo lo que tienen.

| Estrella | Magnitud | Dónde (noches de noviembre) | Qué tiene |
|---|---|---|---|
| 51 Pegasi (Helvetios) | 5,5 | En el cuadrado de Pegaso, cerca de su lado oeste, a primera hora | El primer planeta de una estrella como el Sol (1995) |
| υ Andromedae | 4,1 | En Andrómeda, cerca de la galaxia M31 | El primer sistema con varios planetas (1999) |
| γ Cephei (Errai) | 3,2 | En Cefeo, alta al norte | Un gigante gaseoso en un sistema doble |
| ε Eridani | 3,7 | Erídano, bajo al sur | Un gigante gaseoso, a 10,5 años luz |
| Pólux | 1,1 | Géminis, desde medianoche | Un gigante gaseoso alrededor de una gigante naranja |

**51 Pegasi con prismáticos.** Está a unos 50 años luz y es una estrella parecida al Sol, algo más vieja. Desde una ciudad cuesta verla a simple vista; con los prismáticos, búscala con Stellarium entre las estrellas del cuadrado. Piensa que a su alrededor gira, cada cuatro días, un planeta de la mitad de masa que Júpiter a unos 1000 °C.

**Ciencia ciudadana.** Los datos de TESS son públicos, y miles de voluntarios los revisan en internet buscando tránsitos que se les escapan a los programas automáticos, en el proyecto *Planet Hunters TESS* de la plataforma Zooniverse. No hace falta telescopio ni saber programar: se trata de mirar curvas de luz y marcar las caídas. Con lo que sabes de esta semana, puedes participar.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 47:

- genera una curva de luz **simulada**, como las de TESS (27 días de datos cada 2 minutos), con un planeta en tránsito escondido en el ruido,
- busca el periodo con un ajuste de caja, pliega los datos y mide la profundidad y la duración del tránsito,
- calcula el radio del planeta y el tamaño de su órbita,
- ajusta una curva de velocidad radial simulada y obtiene la masa mínima del planeta,
- incluye, como opción no probada, la descarga de una curva de luz real de TESS con la biblioteca `lightkurve`.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-47.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-47.ipynb)

## Qué has aprendido

- **La respuesta.** Los planetas de otras estrellas se detectan sobre todo de forma indirecta: por el vaivén que producen en su estrella (velocidad radial, con el efecto Doppler) y por la pequeña sombra que proyectan al pasar por delante (tránsitos). Juntos dan la masa, el radio y la densidad del planeta. Hay ya más de 6000 confirmados.
- **Lo que hay.** Una enorme variedad de sistemas, muy distintos del nuestro: júpiteres calientes, supertierras, minineptunos, sistemas compactos alrededor de enanas rojas.
- **Las herramientas.** El cociente señal-ruido, la reducción del ruido al promediar, el plegado en fase, la búsqueda de periodos y el ajuste de modelos no lineales por mínimos cuadrados.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**Cuánto se mueve la estrella.** Un planeta de masa $m$ y una estrella de masa $M$ giran alrededor de su centro de masas en órbitas circulares (semana 20). El momento lineal se equilibra: $M\,v_\star = m\,v_p$. La velocidad del planeta en su órbita de radio $a$ y periodo $P$ es $v_p = 2\pi a/P$, y por la tercera ley de Kepler (semana 15, con $m \ll M$), $a = \left(GMP^2/4\pi^2\right)^{1/3}$. Combinando:

$$v_\star = \frac{m}{M}\,\frac{2\pi a}{P} = m\left(\frac{2\pi G}{P}\right)^{1/3} M^{-2/3}.$$

Si la órbita está inclinada un ángulo $i$ respecto a la visual (con $i = 90°$ de canto), solo vemos la componente $K = v_\star \sin i$, la **semiamplitud** de la curva de velocidad radial. En unidades cómodas:

$$K \approx 28{,}4\ \text{m/s}\;\frac{m\sin i}{M_\text{Júpiter}}\left(\frac{P}{1\ \text{año}}\right)^{-1/3}\left(\frac{M}{M_\odot}\right)^{-2/3}.$$

La señal es mayor para planetas masivos, cercanos (periodo corto) y estrellas poco masivas: justo lo que favorece encontrar primero júpiteres calientes y planetas alrededor de enanas rojas.

**Ejercicios**

1. Calcula $K$ para Júpiter y el Sol ($P = 11{,}86$ años, $\sin i = 1$).
2. Calcula $K$ para la Tierra y el Sol ($m = 1/318$ masas de Júpiter, $P = 1$ año).
3. 51 Pegasi tiene $M = 1{,}1\,M_\odot$, y su planeta, $P = 4{,}23$ días y $K = 56$ m/s. ¿Cuánto vale $m \sin i$?

<details>
<summary>Soluciones</summary>

1. $28{,}4 \cdot 11{,}86^{-1/3} = 28{,}4/2{,}28 \approx$ **12,5 m/s**.
2. $28{,}4/318 \approx$ **0,09 m/s**: 9 centímetros por segundo.
3. $P = 4{,}23/365{,}25 = 0{,}0116$ años, $P^{-1/3} \approx 4{,}42$; $1{,}1^{-2/3} \approx 0{,}94$. $m\sin i = 56/(28{,}4 \cdot 4{,}42 \cdot 0{,}94) \approx$ **0,47 masas de Júpiter**. De ahí su nombre, Dimidium.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Noticias del Archivo de Exoplanetas de la NASA](https://exoplanetarchive.ipac.caltech.edu/docs/exonews_archive.html). Inglés; el recuento oficial de planetas confirmados, actualizado cada semana. Verificado el 20 de noviembre de 2026.
2. [Capítulo 21, El nacimiento de las estrellas y el descubrimiento de planetas fuera del Sistema Solar, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/21%3A_El_nacimiento_de_las_estrellas_y_el_descubrimiento_de_planetas_fuera_del_Sistema_Solar). Español; los métodos de detección y los resultados. Verificado el 20 de noviembre de 2026.
3. [Capítulo 30, La vida en el universo, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/30%3A_La_vida_en_el_universo). Español; zonas habitables y la búsqueda de vida. Verificado el 20 de noviembre de 2026.
4. *Planet Hunters TESS*, en la plataforma de ciencia ciudadana Zooniverse (zooniverse.org). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
