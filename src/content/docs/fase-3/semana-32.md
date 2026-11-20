---
title: "Semana 32 · ¿De qué están hechas las estrellas si no puedo tocarlas?"
description: "Fase 3 · La luz. Leer un espectro, linealizar una ley y ajustar una recta, las leyes de Kirchhoff, las líneas de emisión y de absorción, los niveles de energía del átomo, la serie de Balmer, las clases espectrales y un espectroscopio casero."
sidebar:
  order: 32
  label: "32. ¿De qué están hechas las estrellas?"
---

## La pregunta del cielo

En 1835, el filósofo francés Auguste Comte puso un ejemplo de lo que la ciencia nunca podría saber: la composición química de las estrellas. Podríamos medir sus posiciones y sus movimientos, escribió, pero jamás sabríamos de qué están hechas, porque nunca podríamos ir a tomar una muestra.

Veinticinco años después, dos científicos de Heidelberg, el físico Gustav Kirchhoff y el químico Robert Bunsen, demostraron que se equivocaba. La luz de una estrella, descompuesta en sus colores, lleva escrita la lista de sus elementos químicos, como un código de barras. Esta semana aprendes a leer ese código. Es, probablemente, la herramienta más poderosa de toda la astronomía: de ella sale casi todo lo que sabemos de las estrellas, las galaxias y la expansión del universo.

:::note[De dónde viene la palabra]
**Átomo** viene del griego *átomos*, «que no se puede cortar», de *a-*, «sin», y *tomḗ*, «corte»: los filósofos griegos Leucipo y Demócrito imaginaron que la materia estaba hecha de partículas indivisibles. (Hoy sabemos que el átomo sí se puede dividir, pero el nombre se quedó.) **Elemento** viene del latín *elementum*, de origen incierto; se usaba para las letras del alfabeto y para los componentes básicos de las cosas. **Línea** viene de *linea*, «hilo de lino», de *linum*, «lino»: una línea era un hilo tenso.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: leer un espectro (35-40 min)

**Qué es la gráfica de un espectro.** Un **espectro** se dibuja como una gráfica: en el eje horizontal, la longitud de onda (en nanómetros, o en **ångströms**, Å, la unidad tradicional de los astrónomos: 1 nm = 10 Å); en el vertical, cuánta luz llega en cada longitud de onda, el **flujo**. Antes de mirar los detalles, pregúntate siempre tres cosas: qué hay en cada eje, en qué unidades y en qué escala (lineal o logarítmica).

**Los tres elementos de un espectro estelar:**

- **El continuo.** La forma suave de fondo, que sigue aproximadamente una curva de Planck (semana 31). Su forma da una primera idea de la temperatura.
- **Las líneas de absorción.** Hundimientos estrechos, donde llega menos luz. Cada una está en una longitud de onda concreta.
- **Las líneas de emisión.** Picos estrechos, donde llega más luz. En las estrellas normales son raras; abundan en las nebulosas.

**Normalizar.** Para comparar líneas se suele dividir el espectro por el continuo. El resultado, el **flujo normalizado**, vale 1 lejos de las líneas, y en cada línea baja hasta un valor menor. Si en el centro de una línea el flujo normalizado vale 0,4, la línea se ha «comido» el 60 % de la luz en esa longitud de onda: su **profundidad** es 0,6.

**Medir una línea.** De cada línea se miden tres cosas:

- su **posición**: la longitud de onda del mínimo, que identifica qué elemento la produce,
- su **profundidad**: cuánto baja,
- su **anchura**: lo más habitual es medirla a media profundidad (en inglés, *FWHM*, «anchura total a media altura»). Una línea ancha puede indicar gas caliente o denso, o una estrella que gira deprisa.

**Identificar.** Para saber qué elemento produce una línea, se compara su posición con tablas de laboratorio. Por ejemplo, estas son algunas de las líneas más intensas del espectro del Sol, que Joseph von Fraunhofer catalogó en 1814 y bautizó con letras:

| Línea de Fraunhofer | Longitud de onda | Elemento |
|---|---|---|
| C | 656,3 nm | hidrógeno (H-alfa) |
| D₁ y D₂ | 589,6 y 589,0 nm | sodio |
| b | 517-518 nm | magnesio |
| F | 486,1 nm | hidrógeno (H-beta) |
| H y K | 396,8 y 393,4 nm | calcio ionizado |

**Ejercicios**

1. Un espectro tiene un flujo de continuo de 250 unidades cerca de 656 nm y, en el centro de una línea, 90 unidades. ¿Flujo normalizado? ¿Profundidad?
2. Una línea baja desde 1 hasta 0,3 en flujo normalizado. A media profundidad, el flujo vale 0,65, y eso ocurre en 655,9 y 656,7 nm. ¿Qué anchura tiene? ¿Qué elemento puede ser?
3. Ves una pareja de líneas muy juntas, a 589,0 y 589,6 nm. ¿Qué elemento hay en esa estrella (o entre la estrella y tú)?

<details>
<summary>Soluciones</summary>

1. $90/250 =$ **0,36**; profundidad **0,64**.
2. La media profundidad es $1 - 0{,}7/2 = 0{,}65$. Anchura: $656{,}7 - 655{,}9 =$ **0,8 nm**. Está en 656,3 nm: **hidrógeno**, la línea H-alfa.
3. **Sodio**: es el doblete D.

</details>

### Sesión 2 · Matemáticas: linealizar y ajustar una recta (40-45 min)

**El enigma de Balmer.** En el espectro del hidrógeno, en el visible, aparecen cuatro líneas: 656,3 nm (rojo), 486,1 (azul verdoso), 434,0 (azul) y 410,2 (violeta). Más allá, en el ultravioleta cercano, siguen más, cada vez más juntas. En 1885, el profesor de instituto suizo Johann Balmer, jugando con los números, encontró una fórmula que las reproducía todas. Escrita como la reescribió Johannes Rydberg en 1888:

$$\frac{1}{\lambda} = R\left(\frac{1}{4} - \frac{1}{n^2}\right), \qquad n = 3, 4, 5, \dots$$

donde $R$ es una constante, la **constante de Rydberg**. La línea de 656,3 nm es $n = 3$; la de 486,1, $n = 4$; y así sucesivamente.

**Linealizar.** ¿Cómo comprobar la fórmula con datos y medir $R$? El truco, que ya usaste con los logaritmos en las semanas 15 y 26, es cambiar de variables para que la relación sea una **recta**. Llama $y = 1/\lambda$ y $x = 1/n^2$. La fórmula queda

$$y = \frac{R}{4} - R\,x,$$

una recta de pendiente $-R$ y ordenada en el origen $R/4$. Si dibujas $1/\lambda$ frente a $1/n^2$ y los puntos caen en una recta, la fórmula funciona; y la pendiente te da $R$.

**Ajustar una recta.** Los puntos reales nunca caen perfectamente en una recta: hay errores de medida. **Ajustar** es encontrar la recta que mejor pasa entre ellos. El criterio más usado es el de los **mínimos cuadrados**: para cada punto se calcula su **residuo**, la diferencia vertical entre el punto y la recta, y se elige la recta que hace mínima la suma de los cuadrados de los residuos. (Se elevan al cuadrado para que los residuos positivos y negativos no se anulen, y para castigar más los grandes.) Lo publicó Adrien-Marie Legendre en 1805; Gauss afirmó haberlo usado antes, en 1801, para recuperar la órbita de Ceres, el primer asteroide descubierto (hoy, planeta enano). Las fórmulas las verás en la semana 40; esta semana dejas que el ordenador lo haga y te fijas en lo importante: mirar los residuos. Si los residuos no se reparten al azar, sino con una forma, la ley no es una recta.

**Ejercicios**

1. Calcula $x = 1/n^2$ e $y = 1/\lambda$ (en nm⁻¹) para H-alfa ($n = 3$, 656,3 nm) y H-beta ($n = 4$, 486,1 nm).
2. Con esos dos puntos, calcula la pendiente de la recta que los une y, con ella, $R$. Pásalo a m⁻¹.
3. Con ese valor de $R$, predice la longitud de onda de la línea $n = 5$. Compárala con 434,0 nm.
4. ¿Qué longitud de onda tiene la línea con $n$ muy grande (el **límite de la serie**)?

<details>
<summary>Soluciones</summary>

1. H-alfa: $x = 0{,}1111$, $y = 1/656{,}3 = 0{,}0015237$ nm⁻¹. H-beta: $x = 0{,}0625$, $y = 0{,}0020572$ nm⁻¹.
2. Pendiente $= (0{,}0020572 - 0{,}0015237)/(0{,}0625 - 0{,}1111) = -0{,}010975$ nm⁻¹. $R \approx 0{,}010975$ nm⁻¹ $=$ **1,0975 × 10⁷ m⁻¹**.
3. $1/\lambda = 0{,}010975(0{,}25 - 0{,}04) = 0{,}0023048$, $\lambda \approx$ **433,9 nm**. Muy cerca.
4. Con $1/n^2 \to 0$: $1/\lambda = R/4$, $\lambda = 4/R \approx$ **364,5 nm**, en el ultravioleta cercano.

</details>

### Sesión 3 · Física: por qué cada elemento tiene sus líneas (40-45 min)

**Las tres leyes de Kirchhoff (1859).** Kirchhoff y Bunsen quemaron sustancias en la llama casi invisible del mechero que Bunsen había perfeccionado, y miraron la luz con un prisma. Resumieron lo que vieron en tres reglas:

1. Un sólido, un líquido o un gas denso, calientes, emiten un **espectro continuo**, sin líneas.
2. Un gas poco denso y caliente emite un **espectro de líneas de emisión**: solo unos colores concretos, distintos para cada elemento. El sodio da su doble línea amarilla; el hidrógeno, su serie de Balmer.
3. Si la luz de una fuente continua atraviesa un gas más frío, el gas **absorbe** justo los mismos colores que emitiría: aparecen **líneas oscuras**, en las mismas posiciones.

Las líneas oscuras del Sol eran, por tanto, la huella de los elementos de su atmósfera, más fría que la superficie que hay debajo. Kirchhoff encontró sodio, hierro, magnesio, calcio... los mismos elementos que en la Tierra.

**Por qué: los niveles de energía.** La explicación llegó en 1913 con el físico danés Niels Bohr. En un átomo, los electrones no pueden tener cualquier energía: solo unos valores concretos, los **niveles de energía**, como los peldaños de una escalera. Un electrón puede saltar de un peldaño a otro:

- si **baja** de un nivel alto a uno bajo, el átomo emite un fotón con la energía exacta de la diferencia, $hf = E_\text{alto} - E_\text{bajo}$ (semana 30): es una línea de emisión,
- si **absorbe** un fotón con exactamente esa energía, el electrón sube: es una línea de absorción.

Como cada elemento tiene su propia escalera, cada uno tiene su propio juego de líneas. En el hidrógeno, los niveles están en $E_n = -13{,}6\ \text{eV}/n^2$, y las líneas de Balmer son los saltos que acaban en el nivel $n = 2$. La fórmula de Balmer de la sesión 2 es la diferencia entre dos peldaños.

**Líneas que ya conoces.**

- **Las farolas de sodio de baja presión** (semana 27): casi toda su luz sale en el doblete del sodio, 589 nm. Por eso su luz es monocroma, de un solo color, y los objetos iluminados por ellas se ven sin color.
- **Las auroras** (semana 29): el verde es una línea del oxígeno a 557,7 nm, y el rojo, otra del oxígeno a 630,0 nm. Son transiciones muy lentas, que solo se dan en el aire enrarecido de la alta atmósfera, donde los átomos tardan mucho en chocar.
- **Las nebulosas**, como la de Orión (semana 35), brillan sobre todo en H-alfa: el rojo del hidrógeno.

**El helio, el elemento del Sol.** En el eclipse de 1868, el francés Jules Janssen y, poco después, el inglés Norman Lockyer vieron en el borde del Sol una línea amarilla, a 587,6 nm, que no correspondía a ningún elemento conocido. Lockyer la atribuyó a un elemento nuevo y lo llamó **helio**, del griego *hḗlios*, «Sol». No se encontró en la Tierra hasta 1895.

**Las clases espectrales.** A finales del siglo XIX, en el observatorio de Harvard, un equipo de mujeres, entre ellas Williamina Fleming, Antonia Maury y Annie Jump Cannon, clasificó cientos de miles de espectros. El orden definitivo, establecido por Cannon, va de las estrellas más calientes a las más frías:

**O B A F G K M**

Las O y B, azuladas, muestran sobre todo helio y líneas de hidrógeno débiles; las A, como Vega y Sirio, tienen las líneas de hidrógeno más intensas; las G, como el Sol, muestran sobre todo metales y calcio; las M, como Betelgeuse, bandas de moléculas como el óxido de titanio. En 1925, Cecilia Payne demostró en su tesis que esas diferencias se deben casi solo a la **temperatura**, no a la composición, y que las estrellas están hechas sobre todo de **hidrógeno y helio**, con solo un poco de todo lo demás (hoy sabemos que, en masa, el Sol es más o menos tres cuartos de hidrógeno y un cuarto de helio). Al principio casi nadie la creyó.

**Las líneas se mueven.** Si una estrella se acerca o se aleja, todas sus líneas se desplazan un poco hacia el azul o hacia el rojo: es el **efecto Doppler**, $\Delta\lambda/\lambda = v/c$. Con él se miden las velocidades de las estrellas, se descubren planetas (semana 47) y se descubrió que el universo se expande (semana 41).

:::note[De dónde viene la palabra]
**Espectroscopio** une *espectro* (semana 30) y el griego *skopeîn*, «mirar» (semana 28): el instrumento para mirar espectros. **Ion**, un átomo con electrones de más o de menos, viene del griego *ión*, «el que va»: lo propuso Faraday en 1834 para las partículas que viajan hacia un electrodo. El «calcio ionizado» de las líneas H y K ha perdido un electrón.
:::

**Qué hacer**

1. Calcula la energía en eV del fotón de H-alfa (656,3 nm) con la regla de la semana 30. Compárala con la diferencia $E_3 - E_2$ de la fórmula de Bohr.
2. Ordena estas estrellas por clase espectral, de la más caliente a la más fría: el Sol (G2), Betelgeuse (M1-2), Rigel (B8), Sirio (A1), Proción (F5), Aldebarán (K5).
3. Una línea de H-alfa de una estrella aparece en 656,5 nm en lugar de en 656,3. ¿Se acerca o se aleja? ¿A qué velocidad?

### Sesión 4 · Astronomía y observación: un espectroscopio casero (30-45 min)

**Un CD como red de difracción.** Las pistas de un CD son miles de surcos paralelos, separados 1,6 µm, que funcionan como una **red de difracción**: separan la luz en colores, como un prisma pero por interferencia (semana 27). Con un CD, una caja de cartón y cinta adhesiva puedes hacer un espectroscopio que muestra líneas de verdad.

**Cómo construirlo.**

1. Busca una caja alargada (de pasta, de cereales pequeña o un tubo de cartón) y tapa bien todo excepto los dos extremos.
2. En un extremo, haz una **rendija** muy fina: dos trozos de cartón o de cuchilla de afeitar envuelta, casi tocándose, dejando una abertura de menos de medio milímetro.
3. En el otro extremo, pega un trozo de CD (mejor sin la capa reflectante, que se quita con cinta adhesiva; si no, úsalo por reflexión) inclinado unos 45°, y haz un agujero para mirar.
4. Apunta la rendija a una fuente de luz y busca, mirando un poco de lado, la banda de colores.

**Qué mirar.**

- **Una bombilla incandescente o halógena**: un espectro **continuo**, sin líneas. Es la primera ley de Kirchhoff.
- **Un fluorescente o una bombilla de bajo consumo**: líneas de **emisión** muy claras del mercurio, en 436 nm (azul violeta) y 546 nm (verde), y otras de los fósforos que recubren el tubo. Es la segunda ley.
- **Una farola de sodio** (si queda alguna en tu zona): el doblete amarillo-naranja del sodio, casi solo.
- **Un LED blanco**: un pico azul y una banda ancha amarilla. El blanco de un LED es la mezcla de un LED azul y un recubrimiento que convierte parte del azul en amarillo.
- **El cielo de día**: apunta a una zona de cielo azul o a una nube blanca, **lejos del Sol**. Con una buena rendija, quizá distingas algunas de las rayas oscuras de Fraunhofer.

:::caution[Nunca mires al Sol]
Ni a simple vista, ni con el espectroscopio, ni con los prismáticos. La luz del Sol concentrada daña la retina en segundos, sin dolor y de forma permanente. Apunta siempre a otra zona del cielo.
:::

**Espectros profesionales.** El *Sloan Digital Sky Survey* (SDSS) ha publicado millones de espectros de estrellas, galaxias y cuásares, y tiene actividades educativas con una parte en español. En su herramienta de exploración puedes ver espectros reales, con sus líneas identificadas, y descargarlos.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 32:

- dibuja los niveles de energía del hidrógeno y las transiciones de las series de Lyman, Balmer y Paschen,
- ajusta una recta a las longitudes de onda medidas de las líneas de Balmer, obtiene la constante de Rydberg y dibuja los residuos,
- genera un espectro **sintético** de una estrella parecida al Sol (con líneas reales en sus posiciones reales, pero con profundidades y ruido inventados), lo normaliza y mide la posición, la profundidad y la anchura de las líneas,
- explica cómo cargar un espectro real descargado del SDSS (esa parte no está probada, porque requiere descargar el archivo).

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-32.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-32.ipynb)

## Qué has aprendido

- **La respuesta.** Las estrellas están hechas sobre todo de hidrógeno y helio, con pequeñas cantidades de los demás elementos. Lo sabemos porque cada elemento absorbe y emite luz solo en unas longitudes de onda concretas, que aparecen como líneas en el espectro.
- **Por qué.** Los electrones de un átomo solo pueden estar en ciertos niveles de energía. Al saltar entre ellos emiten o absorben fotones con la energía exacta de la diferencia.
- **Las herramientas.** Leer un espectro (continuo, líneas, normalización, profundidad, anchura), linealizar una ley con un cambio de variables y ajustar una recta por mínimos cuadrados mirando los residuos.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**El modelo de Bohr del átomo de hidrógeno.** Bohr imaginó el electrón girando en círculo alrededor del protón, atraído por la fuerza de Coulomb (semana 29). Para un círculo de radio $r$, la fuerza tiene que producir la aceleración hacia el centro $v^2/r$ (semana 9):

$$\frac{k e^2}{r^2} = \frac{m v^2}{r} \quad\Longrightarrow\quad m v^2 = \frac{k e^2}{r}.$$

La energía total es la cinética más la potencial eléctrica, que es $-ke^2/r$ (con signo menos porque se atraen, igual que la gravitatoria de la semana 17):

$$E = \tfrac{1}{2} m v^2 - \frac{k e^2}{r} = \frac{k e^2}{2r} - \frac{k e^2}{r} = -\frac{k e^2}{2r}.$$

Hasta aquí, física clásica: cualquier radio valdría. Bohr añadió una regla nueva, sin justificarla más que porque funcionaba: el **momento angular** del electrón, $m v r$, solo puede valer múltiplos enteros de $\hbar = h/2\pi$:

$$m v r = n\hbar, \qquad n = 1, 2, 3, \dots$$

Despejando $v = n\hbar/(mr)$ y sustituyendo en $mv^2 = ke^2/r$ sale $r_n = n^2 a_0$, con $a_0 = \hbar^2/(m k e^2) \approx 0{,}0529$ nm, el **radio de Bohr**. Y la energía:

$$E_n = -\frac{k e^2}{2 a_0}\,\frac{1}{n^2} \approx -\frac{13{,}6\ \text{eV}}{n^2}.$$

Al saltar de $n_i$ a $n_f$, el fotón emitido tiene $hc/\lambda = E_{n_i} - E_{n_f}$, es decir,

$$\frac{1}{\lambda} = \frac{13{,}6\ \text{eV}}{hc}\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right).$$

Es la fórmula de Rydberg, con $R = 13{,}6\ \text{eV}/(hc) \approx 1{,}097\times10^7$ m⁻¹: Bohr dedujo la constante que Balmer y Rydberg habían encontrado jugando con números. El modelo de Bohr es incorrecto en los detalles (los electrones no giran en órbitas, como verás en la semana 46), pero acierta en los niveles de energía del hidrógeno.

**Las series.** Los saltos que acaban en $n = 1$ forman la **serie de Lyman**, en el ultravioleta; los que acaban en $n = 2$, la de **Balmer**, en el visible; en $n = 3$, la de **Paschen**, en el infrarrojo.

**Ejercicios**

1. Calcula la longitud de onda de Lyman-alfa ($n = 2 \to 1$).
2. Calcula la de Paschen-alfa ($n = 4 \to 3$).
3. ¿Qué longitud de onda tiene un fotón con la energía justa para arrancar el electrón desde $n = 1$ (13,6 eV)? Los fotones con más energía que esa ionizan el hidrógeno.
4. Comprueba que $R = 13{,}6\ \text{eV}/(hc)$ da $1{,}097\times10^7$ m⁻¹.

<details>
<summary>Soluciones</summary>

1. $1/\lambda = R(1 - 1/4) = 0{,}75R$, $\lambda = 1/(0{,}75 \cdot 1{,}097\times10^7) \approx$ **121,5 nm**.
2. $1/\lambda = R(1/9 - 1/16) = 0{,}04861R$, $\lambda \approx$ **1875 nm**.
3. $\lambda = 1240/13{,}6 \approx$ **91,2 nm**. Es el **límite de Lyman**.
4. $13{,}6 \cdot 1{,}602\times10^{-19}/(6{,}626\times10^{-34} \cdot 2{,}998\times10^8) = 2{,}179\times10^{-18}/1{,}986\times10^{-25} \approx 1{,}097\times10^7$ m⁻¹.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [5.3 Espectroscopia en astronomía, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/05%3A_Radiaci%C3%B3n_y_espectros/5.03%3A_Espectroscopia_en_Astronom%C3%ADa). Español; Kirchhoff, Fraunhofer y los tres tipos de espectro. Verificado el 20 de noviembre de 2026.
2. [5.5 Formación de líneas espectrales, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/05%3A_Radiaci%C3%B3n_y_espectros/5.05%3A_Formaci%C3%B3n_de_L%C3%ADneas_Espectrales). Español; niveles de energía y líneas. Verificado el 20 de noviembre de 2026.
3. [17.3 Los espectros de las estrellas (y enanas marrones), *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/17%3A_Analizando_Starlight/17.03%3A_Los_espectros_de_las_estrellas_(y_enanas_marrones)). Español; las clases espectrales y su historia. Verificado el 20 de noviembre de 2026.
4. [6.4 Modelo de Bohr del átomo de hidrógeno, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/6-4-modelo-de-bohr-del-atomo-de-hidrogeno). Español; el modelo completo con ejemplos. Verificado el 20 de noviembre de 2026.
5. [SDSS Voyages](https://voyages.sdss.org/). Actividades educativas del *Sloan Digital Sky Survey*, con una sección en español sobre espectros. **(Sin verificar)**: he visto sus páginas en los buscadores, pero no he podido abrirlas.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
