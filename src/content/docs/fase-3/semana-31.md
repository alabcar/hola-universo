---
title: "Semana 31 · ¿Qué color tiene una estrella?"
description: "Fase 3 · La luz. Logaritmos para leer leyes de potencia, la radiación de cuerpo negro, la curva de Planck, la ley de Wien y la de Stefan-Boltzmann, la temperatura de las estrellas y sus colores a simple vista y con prismáticos."
sidebar:
  order: 31
  label: "31. ¿Qué color tiene una estrella?"
---

## La pregunta del cielo

Mira Orión en una noche de invierno. Arriba a la izquierda, Betelgeuse tiene un tono anaranjado, casi rojizo. Abajo a la derecha, Rigel es blanca azulada. No es una ilusión: las estrellas tienen colores distintos, y ese color dice algo muy preciso sobre ellas, su **temperatura**. Betelgeuse está a unos 3600 K en su superficie; Rigel, a unos 12 000 K.

¿Cómo se puede tomar la temperatura de algo que está a cientos de años luz? Esta semana descubres que todo cuerpo caliente brilla con un color que depende solo de su temperatura, como un hierro en la fragua, y que la forma de esa luz la describe una de las fórmulas más importantes de la física, la **curva de Planck**. Fue la fórmula que, sin que su autor lo buscara, abrió la puerta a la física cuántica.

:::note[De dónde viene la palabra]
**Color** viene del latín *color*, emparentado con *celare*, «ocultar, cubrir»: el color era lo que cubre la superficie de las cosas. **Temperatura** viene de *temperare*, «mezclar en la proporción justa, moderar» (la misma raíz que *templar* y *temperamento*): para los antiguos, el clima y el cuerpo dependían de la mezcla de calor y frío. **Incandescente** viene de *candere*, «brillar, ser blanco»: de ahí vienen también *candela*, *cándido* y *candidato*, porque en Roma los que aspiraban a un cargo vestían una toga blanqueada.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: logaritmos para leer leyes de potencia (35-45 min)

**Lo que ya sabes.** En la semana 15 viste el logaritmo en base 10 y que convierte productos en sumas y potencias en productos:

$$\log(x\,y) = \log x + \log y, \qquad \log(x^n) = n\log x.$$

En la semana 26 conociste el logaritmo natural, $\ln$, en base $e$. Esta semana los usas como herramienta de trabajo para las relaciones de la física de las estrellas, que casi siempre son **leyes de potencia**: una cantidad proporcional a otra elevada a un exponente.

**Cambiar de base.** Todos los logaritmos son proporcionales entre sí. Para pasar de una base a otra,

$$\log_b x = \frac{\ln x}{\ln b} = \frac{\log_{10} x}{\log_{10} b}.$$

En particular, $\ln x = \ln 10 \cdot \log_{10} x \approx 2{,}303\,\log_{10} x$. Por eso una calculadora con solo dos teclas de logaritmo sirve para cualquier base.

**Despejar exponentes.** Si la potencia que emite cada metro cuadrado de una estrella es proporcional a $T^4$ (lo verás en la sesión 2), ¿cuánto más caliente tiene que estar una estrella para emitir 10 veces más por metro cuadrado? Hay que resolver $x^4 = 10$, así que $x = 10^{1/4}$. Con logaritmos: $\log x = \tfrac{1}{4}\log 10 = 0{,}25$, y $x = 10^{0{,}25} \approx 1{,}78$. Un 78 % más caliente.

**Combinar leyes de potencia.** La potencia total de una estrella, su **luminosidad** $L$, es la de cada metro cuadrado por el área de la esfera: $L \propto R^2 T^4$. Tomando logaritmos,

$$\log L = 2\log R + 4\log T + \text{constante}.$$

Una relación con productos y potencias se ha convertido en una **suma**: duplicar el radio suma $2\log 2 \approx 0{,}6$ al logaritmo de la luminosidad; duplicar la temperatura suma $4\log 2 \approx 1{,}2$. Es exactamente lo que hace el diagrama de Hertzsprung-Russell de la semana 35, que dibuja $\log L$ frente a $\log T$.

**Ejercicios**

1. Calcula $\log_2 1000$ con la fórmula del cambio de base. ¿Cuántas veces hay que duplicar 1 para pasar de 1000?
2. Una estrella está al doble de temperatura que el Sol y tiene el mismo radio. ¿Cuántas veces más luminosa es?
3. Betelgeuse tiene una temperatura de unos 3600 K, frente a 5772 K del Sol, y su radio es de unos 750 radios solares. ¿Cuántas veces más luminosa que el Sol es? Hazlo con logaritmos.
4. ¿Qué temperatura necesita una estrella del mismo radio que el Sol para ser 100 veces más luminosa?

<details>
<summary>Soluciones</summary>

1. $\log_2 1000 = 3/\log_{10} 2 = 3/0{,}301 \approx$ **9,97**: diez duplicaciones ($2^{10} = 1024$).
2. $2^4 =$ **16 veces**.
3. $\log(L/L_\odot) = 2\log 750 + 4\log(3600/5772) = 2 \cdot 2{,}875 + 4 \cdot (-0{,}205) = 5{,}75 - 0{,}82 = 4{,}93$, así que $L \approx 10^{4{,}93} \approx$ **85 000 veces** la del Sol. Más fría, pero tan grande que brilla muchísimo más.
4. $T^4$ tiene que ser 100 veces mayor: $T = 5772 \cdot 100^{1/4} = 5772 \cdot 3{,}16 \approx$ **18 300 K**.

</details>

### Sesión 2 · Matemáticas: la curva de Planck, una potencia contra una exponencial (40-45 min)

**La fórmula.** La potencia que emite un cuerpo negro a temperatura $T$ en cada longitud de onda es

$$B_\lambda(T) = \frac{2hc^2}{\lambda^5}\;\frac{1}{e^{\,hc/(\lambda k_B T)} - 1},$$

donde $h$ es la constante de Planck (semana 30), $c$ la velocidad de la luz y $k_B = 1{,}381\times10^{-23}$ J/K la **constante de Boltzmann**, que convierte temperatura en energía. No hace falta memorizarla: lo importante es entender su forma.

**Una batalla entre dos factores.** La fórmula es el producto de dos cosas que ya conoces (semana 26):

- Una **potencia**, $1/\lambda^5$, que crece muchísimo hacia las longitudes de onda cortas.
- Un factor con una **exponencial**, $1/(e^{hc/\lambda k_B T} - 1)$, que hacia las longitudes de onda cortas se hunde a cero mucho más deprisa que cualquier potencia.

A longitudes de onda largas manda la potencia, que cae; a longitudes de onda cortas, la exponencial lo apaga todo. En medio hay un **máximo**. Si sube la temperatura, la exponencial tarda más en apagar la curva, y el máximo se desplaza hacia longitudes de onda más cortas.

**La ley de Wien.** La longitud de onda del máximo es inversamente proporcional a la temperatura:

$$\lambda_\text{máx}\,T = 2{,}898\times10^{-3}\ \text{m·K}.$$

Wilhelm Wien la encontró en 1893. Para el Sol, a 5772 K, el máximo cae en unos 502 nm, en el verde. Para una persona, a unos 310 K, en unos 9 µm, en el infrarrojo: brillas, pero no en una luz que tus ojos vean. Así funcionan las cámaras térmicas.

**La ley de Stefan-Boltzmann.** El área bajo la curva, la potencia total que emite cada metro cuadrado de superficie, crece con la cuarta potencia de la temperatura:

$$\frac{P}{A} = \sigma T^4, \qquad \sigma = 5{,}670\times10^{-8}\ \text{W/(m}^2\text{·K}^4).$$

Josef Stefan la dedujo de experimentos en 1879, y Ludwig Boltzmann la demostró en 1884. Para una estrella de radio $R$, la luminosidad es

$$L = 4\pi R^2\,\sigma T^4.$$

**Ejercicios**

1. ¿Dónde está el máximo de emisión de Betelgeuse (3600 K) y de Rigel (12 000 K)? ¿En qué región del espectro cae cada uno?
2. El filamento de una bombilla incandescente está a unos 2800 K. ¿Dónde está su máximo? ¿Por qué esas bombillas eran tan poco eficientes?
3. Calcula la luminosidad del Sol con $R = 6{,}96\times10^8$ m y $T = 5772$ K. Compárala con el valor de la semana 30.
4. El fondo cósmico de microondas tiene una temperatura de 2,725 K. ¿Dónde está su máximo?

<details>
<summary>Soluciones</summary>

1. Betelgeuse: $2{,}898\times10^{-3}/3600 \approx$ **805 nm**, en el infrarrojo cercano; Rigel: **242 nm**, en el ultravioleta. Las dos emiten luz visible, pero en los extremos de su curva.
2. **1,03 µm**, en el infrarrojo. La mayor parte de la energía sale como calor, no como luz visible: solo un pequeño porcentaje de su potencia era luz útil.
3. $4\pi(6{,}96\times10^8)^2 \cdot 5{,}670\times10^{-8} \cdot 5772^4 \approx$ **3,83 × 10²⁶ W**. Coincide.
4. $2{,}898\times10^{-3}/2{,}725 \approx$ **1,06 mm**: en las microondas, de ahí su nombre (semana 42).

</details>

### Sesión 3 · Física: la radiación de cuerpo negro (40-45 min)

**Todo lo que está caliente brilla.** Calienta un trozo de hierro: primero no ves nada, aunque notas el calor a distancia (es infrarrojo). Hacia los 800 K empieza a verse rojo oscuro; a 1200 K, naranja; a 1700 K, amarillo; por encima de 2500 K, blanco. Los herreros juzgaban la temperatura de la fragua por el color. Todos los cuerpos emiten radiación por el simple hecho de tener temperatura, porque sus átomos y sus cargas se agitan, y las cargas agitadas emiten ondas electromagnéticas (semana 30).

**El cuerpo negro.** En 1860, Gustav Kirchhoff imaginó un cuerpo ideal que absorbe toda la luz que le llega, sin reflejar nada: un **cuerpo negro**. Demostró que la luz que un cuerpo así emite al calentarse no depende de qué está hecho, solo de su temperatura. Un buen ejemplo es una cavidad con un agujero pequeño: la luz que entra por el agujero rebota dentro hasta ser absorbida. Las estrellas no son cuerpos negros perfectos, pero se parecen bastante.

**La catástrofe y el cuanto.** A finales del siglo XIX, la física clásica predecía que un cuerpo negro debía emitir una cantidad infinita de energía en el ultravioleta: lo que más tarde se llamó la **catástrofe ultravioleta**. En diciembre de 1900, Max Planck encontró la fórmula que encajaba con las medidas, pero para deducirla tuvo que suponer, «en un acto de desesperación», según sus palabras, que la energía se emite en paquetes de tamaño $hf$. Él mismo pensó que era un truco matemático. Cinco años después, Einstein se lo tomó en serio (los fotones de la semana 30), y en las dos décadas siguientes nació la mecánica cuántica (semana 46).

**Por qué no hay estrellas verdes.** El Sol emite el máximo en el verde, pero no lo vemos verde. Su curva es tan ancha que cubre todo el visible con intensidades parecidas, y el ojo, cuando recibe todos los colores mezclados, ve blanco. Una curva de Planck nunca es estrecha, así que las estrellas solo pueden ir del rojo anaranjado (las frías) al blanco azulado (las calientes), pasando por el amarillento y el blanco. Además, el ojo de noche es poco sensible al color: los conos, que distinguen colores, necesitan bastante luz, y solo en las estrellas más brillantes se aprecia el tono.

**La temperatura de algunas estrellas** (temperatura efectiva aproximada de la superficie):

| Estrella | Temperatura | Color a la vista |
|---|---|---|
| Betelgeuse (Orión) | ~3600 K | naranja rojizo |
| Antares (Escorpio) | ~3500 K | naranja rojizo |
| Aldebarán (Tauro) | ~3900 K | naranja |
| Arturo (Boyero) | ~4300 K | naranja claro |
| Sol | 5772 K | blanco (amarillento desde el suelo) |
| Proción (Can Menor) | ~6500 K | blanco amarillento |
| Vega (Lira) | ~9600 K | blanco azulado |
| Sirio (Can Mayor) | ~9900 K | blanco azulado |
| Rigel (Orión) | ~12 000 K | azul blanquecino |

Las clases espectrales que verás la semana que viene (O, B, A, F, G, K, M) ordenan las estrellas de las más calientes a las más frías.

:::note[De dónde viene la palabra]
El **kelvin**, la unidad de temperatura absoluta, lleva el nombre de William Thomson, lord Kelvin, que en 1848 propuso una escala que empieza en el **cero absoluto**, la temperatura más baja posible, a −273,15 °C. El título de lord lo tomó del río Kelvin, que pasa junto a la Universidad de Glasgow. Una diferencia de 1 K es igual a una de 1 °C, y se escribe «kelvin», sin «grados».
:::

**Qué hacer**

1. Ordena las estrellas de la tabla por la longitud de onda de su máximo.
2. Calcula la luminosidad de Sirio B, una enana blanca a unos 25 000 K con un radio de solo 0,0084 radios solares. ¿Es más o menos luminosa que el Sol? (Volverás a ella en la semana 36.)
3. Mira una vitrocerámica o un hornillo eléctrico mientras se calienta en la oscuridad: el color rojo oscuro aparece hacia los 800 K. ¿Dónde estaría el máximo de su emisión?

### Sesión 4 · Astronomía y observación: los colores de las estrellas (30-45 min)

**A simple vista.** En las noches de otoño e invierno tienes una paleta completa. Compara por parejas, mirando una y otra varias veces:

- **Betelgeuse y Rigel**, en Orión: naranja frente a blanco azulado. Es la pareja más clara del cielo.
- **Aldebarán y las Pléyades**, en Tauro: Aldebarán, el «ojo del toro», es naranja; las estrellas de las Pléyades, azuladas.
- **Capella**, en Auriga, casi en el cénit a medianoche: amarillenta, de un color parecido al del Sol.
- **Sirio**, que sale de madrugada en noviembre y a primera hora de la noche en enero y febrero: blanca azulada, y cuando está baja centellea en todos los colores. Ese parpadeo de colores no es de la estrella, sino de la atmósfera, que actúa como un prisma tembloroso.

**Con los prismáticos.** Los prismáticos recogen más luz y hacen que el color se aprecie mejor, sobre todo en estrellas menos brillantes. Un truco que usan los observadores: desenfoca un poco. La estrella se convierte en un disco pequeño, y el color se ve con más claridad que en un punto.

- **La estrella Granate (mu de Cefeo)**, en el norte, alta en las noches de otoño: una supergigante roja de las más rojas que se ven a simple vista o con prismáticos. William Herschel la llamó así por su color.
- **Albireo**, en la cabeza del Cisne, al oeste a primera hora de la noche en noviembre: una pareja de estrellas, una dorada y otra azul, separadas 34″. Con 8 aumentos y los prismáticos muy bien apoyados quizá las separes; con cualquier telescopio pequeño, sin duda.
- Recorre el **cinturón de Orión** y la espada: estrellas jóvenes y calientes, casi todas blanco azuladas.

**Apunta lo que ves.** Para cada estrella, escribe el color que percibes. Luego busca su temperatura en Stellarium (en la información de la estrella aparece su clase espectral y su índice de color B−V, que verás en la semana 33). ¿Coincide el orden?

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 31:

- dibuja la curva de Planck para varias temperaturas, en escala lineal y logarítmica,
- comprueba la ley de Wien buscando el máximo de cada curva,
- integra la curva numéricamente y comprueba en una gráfica log-log que el área crece como $T^4$,
- calcula el color de un cuerpo negro a cada temperatura y lo dibuja para una lista de estrellas,
- estima la temperatura de una estrella a partir del cociente de su brillo en dos colores, como hacen los astrónomos.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-31.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-31.ipynb)

## Qué has aprendido

- **La respuesta.** El color de una estrella lo decide la temperatura de su superficie, porque una estrella brilla como un cuerpo negro: las frías, de unos 3000 K, son anaranjadas; las calientes, de más de 10 000 K, blanco azuladas. Su luz sigue la curva de Planck.
- **Dos leyes muy útiles.** La de Wien ($\lambda_\text{máx}T$ constante) da la temperatura a partir del color, y la de Stefan-Boltzmann ($L = 4\pi R^2\sigma T^4$) une la luminosidad, el radio y la temperatura.
- **Las herramientas.** El cambio de base de los logaritmos, despejar exponentes, convertir leyes de potencia en sumas de logaritmos, y entender una curva como la competencia entre una potencia y una exponencial.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**De dónde sale la ley de Wien.** El máximo de la curva de Planck está donde su derivada se anula. Para simplificar, llama $x = hc/(\lambda k_B T)$: es la longitud de onda medida en unas unidades que dependen de la temperatura. Como $\lambda = hc/(x k_B T)$, la curva, en función de $x$, es proporcional a

$$f(x) = \frac{x^5}{e^x - 1}.$$

(Ojo: buscar el máximo en $x$ es lo mismo que buscarlo en $\lambda$, porque una es una función decreciente de la otra.) Derivando con la regla del cociente, $(u/v)' = (u'v - uv')/v^2$, y simplificando,

$$f'(x) = 0 \iff 5x^4(e^x - 1) = x^5 e^x \iff x = 5\,(1 - e^{-x}).$$

Esta ecuación no se puede despejar con las operaciones habituales: hay que resolverla **numéricamente**. Un método sencillo es la **iteración de punto fijo**: empiezas con un valor cualquiera, por ejemplo $x = 5$, lo metes a la derecha y obtienes uno nuevo, y repites.

- $x_1 = 5(1 - e^{-5}) = 4{,}9663$
- $x_2 = 5(1 - e^{-4{,}9663}) = 4{,}9651$
- $x_3 = 4{,}9651$...

En tres pasos tienes $x \approx 4{,}9651$. Deshaciendo el cambio, $\lambda_\text{máx}T = hc/(4{,}9651\,k_B) = 2{,}898\times10^{-3}$ m·K. La ley de Wien sale de la fórmula de Planck.

**De dónde sale el $T^4$.** La potencia total es el área bajo la curva, $\int_0^\infty B_\lambda\,d\lambda$. Si cambias la variable a $x = hc/(\lambda k_B T)$, todas las temperaturas salen fuera de la integral y queda

$$\int_0^\infty B_\lambda\,d\lambda = \text{(constantes)} \cdot T^4 \cdot \int_0^\infty \frac{x^3}{e^x - 1}\,dx.$$

La integral que queda es un número puro, que no depende de nada, y vale exactamente $\pi^4/15$ (el cuaderno lo comprueba numéricamente). Así que la potencia es proporcional a $T^4$, sin necesidad de calcular más. De esta cuenta sale también el valor de $\sigma$ a partir de $h$, $c$ y $k_B$.

**Ejercicios**

1. Haz la iteración de punto fijo para la ecuación $x = 3(1 - e^{-x})$, que da el máximo de la curva de Planck en frecuencia en lugar de en longitud de onda. ¿Qué valor sale? (Sorpresa: el máximo en frecuencia no está en la misma luz que el máximo en longitud de onda.)
2. Con $x = 2{,}821$, ¿a qué frecuencia está el máximo del Sol? ¿A qué longitud de onda corresponde esa frecuencia?
3. Comprueba que $f(x) = x^5/(e^x - 1)$ vale casi cero para $x = 0{,}1$ y para $x = 20$, y calcula $f(5)$.

<details>
<summary>Soluciones</summary>

1. Empezando en 3: $2{,}851$, $2{,}827$, $2{,}822$, $2{,}821$... converge a **2,821**.
2. $f = x k_B T/h = 2{,}821 \cdot 1{,}381\times10^{-23} \cdot 5772/6{,}626\times10^{-34} \approx$ **3,39 × 10¹⁴ Hz**, que corresponde a $c/f \approx$ **884 nm**, en el infrarrojo. El «color del máximo» depende de cómo repartas el espectro: no es una propiedad física de la estrella, mientras que la temperatura sí.
3. $f(0{,}1) \approx 10^{-5}/0{,}105 \approx 10^{-4}$; $f(20) \approx 3{,}2\times10^6/4{,}85\times10^8 \approx 0{,}007$; $f(5) \approx 3125/147{,}4 \approx$ **21,2**.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [17.2 Colores de las estrellas, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/17%3A_Analizando_Starlight/17.02%3A_Colores_de_Estrellas). Español; color, temperatura e índice de color. Verificado el 20 de noviembre de 2026.
2. [5.1 El comportamiento de la luz, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/05%3A_Radiaci%C3%B3n_y_espectros/5.01%3A_El_comportamiento_de_la_luz). Español; incluye la ley del inverso del cuadrado. Verificado el 20 de noviembre de 2026.
3. [6.1 Radiación de cuerpo negro, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/6-1-radiacion-de-cuerpo-negro). Español; la cavidad, las leyes de Wien y Stefan y la hipótesis de Planck, con ejemplos resueltos. Verificado el 20 de noviembre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
