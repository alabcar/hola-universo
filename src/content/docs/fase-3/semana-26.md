---
title: "Semana 26 · ¿Por qué el cielo es azul y el Sol se pone rojo?"
description: "Fase 3 · La luz. La función exponencial y el logaritmo natural, potencias frente a exponenciales, masa de aire, color y longitud de onda, y la dispersión de Rayleigh."
sidebar:
  order: 26
  label: "26. ¿Por qué el cielo es azul y el Sol se pone rojo?"
---

## La pregunta del cielo

El espacio es negro. En la Luna, que no tiene atmósfera, el cielo es negro incluso a mediodía, con el Sol brillando en él. En la Tierra, en cambio, el cielo de día es azul, y al atardecer el Sol se vuelve naranja y rojo. La diferencia es el aire.

La pregunta parece sencilla y no lo es. Leonardo da Vinci ya sospechaba que el azul tenía que ver con el aire iluminado delante de la oscuridad del espacio. John Tyndall, hacia 1870, reprodujo el azul del cielo en el laboratorio iluminando nieblas de partículas muy finas. Y Lord Rayleigh, en 1871, dio la explicación cuantitativa: las moléculas del aire desvían la luz azul mucho más que la roja. La misma idea explica a la vez el cielo azul, el Sol rojo del ocaso, las nubes blancas y el cielo de Marte.

Esta semana necesitas dos herramientas matemáticas: la función exponencial, que describe cómo se apaga la luz al atravesar el aire, y las potencias, que describen cómo depende eso del color.

:::note[De dónde viene la palabra]
**Azul** viene del árabe *lāzaward*, y este del persa *lāžward*, el nombre de una región de Asia Central de donde se extraía una piedra azul intensa, el **lapislázuli** («piedra de lāzaward»). Con ella se fabricó durante siglos el pigmento azul más caro de la pintura, el azul ultramar, que se usaba para los mantos de las vírgenes medievales. **Atmósfera** viene del griego *atmós*, «vapor», y *sphaîra*, «esfera»: la esfera de vapor que envuelve la Tierra.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: la exponencial y el logaritmo natural (40-45 min)

**Perder siempre la misma fracción.** Imagina que cada kilómetro de aire deja pasar el 90 % de la luz que le llega. Tras un kilómetro queda el 90 %; tras dos, el 90 % del 90 %, es decir, el 81 %; tras tres, el 72,9 %. No se pierde la misma **cantidad** en cada tramo, sino la misma **fracción**. Tras $x$ kilómetros queda

$$I(x) = I_0 \cdot 0{,}9^{\,x},$$

donde $I_0$ es la intensidad inicial. La variable está en el exponente: es una **función exponencial**. Es la misma estructura que el crecimiento de las bacterias de la semana 23, pero hacia abajo: un **decaimiento exponencial**.

**El número $e$.** Cualquier exponencial se puede escribir con una base fija, el número $e \approx 2{,}718$ que conociste en la semana 23. Así, $0{,}9^x = e^{-k x}$ para un $k$ adecuado, y la ley de la luz que atraviesa un medio queda

$$I(x) = I_0\,e^{-k x}.$$

El número $k$ es el **coeficiente de extinción**: cuanto mayor, más deprisa se apaga la luz. Se usa la base $e$ porque es la que sale de forma natural de la ecuación diferencial $dI/dx = -k\,I$: «cada tramo pequeño quita una fracción $k\,dx$ de lo que hay». En «Para ir más lejos» lo ves con detalle.

**El logaritmo natural.** Para despejar el exponente hace falta la operación inversa de $e^x$: el **logaritmo natural**, $\ln$. Es como el $\log_{10}$ de la semana 15, pero en base $e$: $\ln y = x$ significa $e^x = y$. Tiene las mismas propiedades: $\ln(a b) = \ln a + \ln b$ y $\ln(a^n) = n \ln a$. Además, $\ln 1 = 0$ y $\ln e = 1$. Con él, de $0{,}9 = e^{-k}$ sale $k = -\ln 0{,}9 \approx 0{,}105$ por kilómetro. Y si tomas logaritmos en $I = I_0 e^{-kx}$:

$$\ln I = \ln I_0 - k\,x,$$

que es una **recta** en $x$, de pendiente $-k$. Es el mismo truco que en la semana 15: un logaritmo convierte una relación complicada en una recta, que se reconoce y se mide fácilmente.

**El espesor mitad.** ¿Cuánto hay que atravesar para quedarse con la mitad? Si $e^{-kx} = 1/2$, entonces $x = \ln 2/k \approx 0{,}693/k$. Es la misma idea que el periodo de semidesintegración de un elemento radiactivo.

**Potencia frente a exponencial.** No confundas $x^4$ con $4^x$. En una **potencia** la variable está en la base y el exponente es fijo; en una **exponencial**, al revés. Las dos crecen, pero de formas muy distintas: una exponencial acaba superando a cualquier potencia. En esta semana aparecen las dos: la exponencial para cómo se apaga la luz con el camino recorrido, y una potencia, $1/\lambda^4$, para cómo depende del color.

**Ejercicios**

1. Si cada kilómetro deja pasar el 80 % de la luz, ¿qué fracción queda tras 5 km? ¿Cuánto vale $k$?
2. Calcula $\ln 1$, $\ln e^3$ y, con la calculadora, $\ln 10$.
3. Con $k = 0{,}2$ por km, ¿cuál es el espesor mitad?
4. ¿Qué es mayor para $x = 10$: $x^4$ o $2^x$? ¿Y para $x = 20$?

<details>
<summary>Soluciones</summary>

1. $0{,}8^5 \approx$ **0,33**, un 33 %. $k = -\ln 0{,}8 \approx$ **0,223** por km.
2. **0**, **3** y **2,303**. (Por eso $\ln x = 2{,}303\,\log_{10} x$.)
3. $0{,}693/0{,}2 \approx$ **3,5 km**.
4. Para $x = 10$: $10^4 = 10\,000$ y $2^{10} = 1024$: gana la potencia. Para $x = 20$: $20^4 = 160\,000$ y $2^{20} \approx 1\,050\,000$: gana la exponencial, y a partir de ahí ya no la alcanza nunca.

</details>

### Sesión 2 · Matemáticas: la masa de aire (30-40 min)

**Cuánto aire atraviesa la luz.** La luz de un astro que está en el cénit atraviesa el espesor mínimo de atmósfera. Si el astro está más bajo, la luz entra inclinada y recorre más aire. Se llama **masa de aire**, $X$, al cociente entre el aire que atraviesa y el que atravesaría en el cénit: vale 1 en el cénit y crece hacia el horizonte.

**Con trigonometría.** Si imaginas la atmósfera como una capa plana de espesor $H$, un rayo que llega con una altura $h$ sobre el horizonte forma un triángulo rectángulo: el espesor $H$ es el cateto opuesto al ángulo $h$, y el camino recorrido $L$ es la hipotenusa. Por la definición del seno (semana 7), $\sin h = H/L$, así que

$$X = \frac{L}{H} = \frac{1}{\sin h}.$$

A 30° de altura, $X = 2$: la luz atraviesa el doble de aire. A 10°, casi 6. En el horizonte, esta fórmula daría infinito, porque supone una atmósfera plana e infinita. La atmósfera real es curva, como la Tierra, y la masa de aire en el horizonte es de unas 38.

**Juntar las dos ideas.** Si en el cénit la atmósfera deja pasar una fracción $e^{-\tau}$ (el número $\tau$, la letra griega tau, se llama **profundidad óptica**), con una masa de aire $X$ deja pasar

$$\frac{I}{I_0} = e^{-\tau X}.$$

La profundidad óptica depende del color, como verás en la sesión 3. Y la masa de aire multiplica su efecto.

**Ejercicios**

1. Calcula la masa de aire a 90°, 45°, 20° y 5° de altura con la fórmula plana.
2. Si $\tau = 0{,}2$, ¿qué fracción de la luz llega con el astro en el cénit? ¿Y a 20° de altura?
3. ¿Y con el Sol en el horizonte, con $X = 38$?

<details>
<summary>Soluciones</summary>

1. **1**, **1,41**, **2,92** y **11,5**. (La de 5° ya se aparta de la real, que es de unos 10,4.)
2. $e^{-0{,}2} \approx$ **0,82** y $e^{-0{,}2 \cdot 2{,}92} \approx$ **0,56**.
3. $e^{-0{,}2 \cdot 38} = e^{-7{,}6} \approx$ **0,0005**: la luz se reduce dos mil veces. Por eso el Sol poniente deslumbra mucho menos. Aun así, no lo mires fijamente, y nunca con prismáticos ni telescopio.

</details>

### Sesión 3 · Física: el color y la dispersión de Rayleigh (40-45 min)

**La luz blanca es una mezcla.** En 1666, Isaac Newton hizo pasar un rayo de Sol por un prisma de vidrio y obtuvo una banda de colores: rojo, naranja, amarillo, verde, azul y violeta. Después, con un segundo prisma, volvió a juntarlos en luz blanca. La conclusión: la luz blanca no es «pura», sino una mezcla de todos los colores.

**El color es una longitud de onda.** En la semana siguiente verás con detalle qué es una onda. Por ahora basta esta idea: la luz es una onda, y cada color corresponde a una **longitud de onda** distinta, la distancia entre dos crestas consecutivas, que se escribe $\lambda$ (la letra griega lambda). Las longitudes de onda visibles van de unos 380 nanómetros (violeta) a unos 750 (rojo). Un nanómetro es una millonésima de milímetro (semana 1), así que son ondas diminutas: en el grosor de una hoja de papel caben unas 200.

**Desviar la luz.** Cuando la luz atraviesa el aire, choca con moléculas de nitrógeno y oxígeno, mucho más pequeñas que su longitud de onda. Cada molécula absorbe un poco de la luz y la reemite en todas direcciones: la **dispersa**. Rayleigh demostró que, para partículas mucho más pequeñas que la longitud de onda, la cantidad de luz dispersada es proporcional a

$$\frac{1}{\lambda^4}.$$

Es una potencia con exponente $-4$, muy sensible al color. El azul, de unos 450 nm, se dispersa $(700/450)^4 \approx 5{,}9$ veces más que el rojo, de unos 700 nm.

**El cielo azul.** Cuando miras a cualquier parte del cielo que no sea el Sol, ves luz solar que alguna molécula ha desviado hacia ti. Como el azul se desvía mucho más que el rojo, esa luz es azulada. Sin aire no hay nada que desvíe la luz hacia ti, y el cielo es negro, como en la Luna.

**¿Por qué no violeta?** El violeta se dispersa todavía más que el azul. Pero la luz del Sol trae menos violeta que azul, la capa alta de la atmósfera absorbe parte del violeta y del ultravioleta, y nuestros ojos son mucho menos sensibles al violeta. La suma de todo se ve azul celeste.

**El Sol rojo.** Al atardecer, la luz del Sol atraviesa unas 38 veces más aire que a mediodía (sesión 2). Por el camino pierde casi todo el azul, que se dispersa hacia los lados (y colorea de azul el cielo de otros lugares, donde todavía es de día), y llega sobre todo el rojo y el naranja. Por el mismo motivo, la Luna llena recién salida se ve anaranjada, y las estrellas cerca del horizonte se ven más débiles y más rojizas.

**Las nubes blancas.** Las gotas de agua de una nube son mucho más grandes que la longitud de onda de la luz, y dispersan todos los colores casi por igual (es la **dispersión de Mie**, por Gustav Mie, que la estudió en 1908). Por eso las nubes son blancas o grises, no azules.

**El cielo de Marte.** En Marte, el polvo fino en suspensión tiene partículas de un tamaño parecido a la longitud de onda de la luz, y se comporta de otra manera: el cielo de día es de un color tostado, y los atardeceres son azulados alrededor del Sol. Las fotos de los rovers lo muestran.

**Un aviso de vocabulario.** En español, la palabra **dispersión** se usa para dos fenómenos distintos: la desviación de la luz por partículas (lo que estudias hoy, en inglés *scattering*) y la separación de colores en un prisma (en inglés *dispersion*, que verás en la semana 28). Fíjate en el contexto.

:::note[De dónde viene la palabra]
**Dispersión** viene del latín *dispergere*, «esparcir», de *dis*, «en distintas direcciones», y *spargere*, «sembrar a voleo». **Ocaso** viene de *occasus*, «caída», del verbo *occidere*, «caer», como **occidente**, el lado por donde el Sol «cae». **Oriente** viene de *oriri*, «levantarse, nacer»: el lado por donde nace el Sol, como en *origen*.
:::

**Qué hacer**

1. Calcula cuántas veces más se dispersa la luz violeta (400 nm) que la roja (700 nm).
2. Explica por qué los astronautas en la Luna veían el cielo negro con el Sol en lo alto.
3. Explica por qué el humo de una hoguera se ve azulado sobre un fondo oscuro y amarillento cuando miras el Sol a través de él.

### Sesión 4 · Astronomía y observación: los colores del cielo (30-45 min)

**El cielo no es uniforme.** Un día despejado, fíjate en tres cosas, sin mirar nunca directamente al Sol:

1. El cielo es de un azul más intenso lejos del Sol, a unos 90° de él, y más blanquecino cerca del horizonte, donde la luz ha atravesado más aire y se ha mezclado.
2. Con unas gafas de sol **polarizadas** (muchas de las de conducir o de pesca lo son), mira una zona del cielo a 90° del Sol y gira la cabeza o las gafas: el cielo se oscurece y se aclara. La luz dispersada por las moléculas sale **polarizada**, vibrando en una dirección preferente, sobre todo a 90° del Sol. Algunos insectos, como las abejas, se orientan con este patrón.
3. Al atardecer, fíjate en los colores del horizonte del oeste y del este. En el este, frente a la puesta, a veces se ve una banda rosada sobre una franja gris azulada: la franja gris es la sombra de la Tierra proyectada sobre la atmósfera, y la banda rosada se llama **cinturón de Venus**.

**De noche.** Elige una estrella brillante que esté saliendo o poniéndose y compárala con una estrella parecida que esté alta. La baja se ve más débil, a menudo más rojiza, y centellea más. Mide sus alturas con la mano (semana 2) y calcula sus masas de aire.

**La Luna saliente.** La próxima luna llena, mírala salir: anaranjada al principio y cada vez más blanca a medida que sube. Es la misma física que el Sol poniente, sin ningún peligro para la vista.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 26:

- compara potencias y exponenciales, y transforma una exponencial en una recta con el logaritmo natural,
- calcula la masa de aire con la fórmula plana y con una fórmula realista que tiene en cuenta la curvatura de la atmósfera,
- calcula la profundidad óptica de Rayleigh para cada color y la luz del Sol que llega a cada altura,
- dibuja el color aproximado del Sol desde el mediodía hasta la puesta.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-26.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-26.ipynb)

## Qué has aprendido

- **La respuesta.** El cielo es azul porque las moléculas del aire dispersan la luz del Sol en todas direcciones, y dispersan mucho más el azul que el rojo (en proporción a $1/\lambda^4$). El Sol se pone rojo porque su luz atraviesa entonces decenas de veces más aire y pierde casi todo el azul por el camino.
- **Lo que explica a la vez.** Las nubes blancas (gotas grandes que dispersan todos los colores igual), la luna anaranjada al salir, las estrellas más débiles cerca del horizonte, la polarización del cielo y el cielo negro de la Luna.
- **Las herramientas.** La función exponencial y el decaimiento exponencial, el logaritmo natural, el espesor mitad, la diferencia entre potencias y exponenciales, y la masa de aire calculada con trigonometría.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**De dónde sale la exponencial.** Un rayo de luz de intensidad $I$ atraviesa una capa fina de aire de espesor $dx$. La capa le quita una fracción proporcional a su espesor: $dI = -k\,I\,dx$. Dividiendo por $dx$:

$$\frac{dI}{dx} = -k\,I.$$

Es la ecuación diferencial de la semana 23 con el signo cambiado, y su solución es $I = I_0\,e^{-kx}$: puedes comprobarlo derivando, porque la derivada de $e^{-kx}$ es $-k\,e^{-kx}$. Esta ley tiene varios nombres según la disciplina: **ley de Beer-Lambert** en química, **ley de Bouguer** en astronomía. Pierre Bouguer la usó en 1729 para medir cuánta luz absorbe la atmósfera.

**Medir la atmósfera con una estrella.** Si mides el brillo de una estrella a lo largo de una noche, a medida que sube o baja, $\ln I = \ln I_0 - \tau X$: al dibujar $\ln I$ frente a la masa de aire sale una recta de pendiente $-\tau$. Prolongándola hasta $X = 0$ obtienes $I_0$, el brillo que tendría la estrella **fuera** de la atmósfera, aunque nunca hayas salido de ella. Así se calibraban las medidas astronómicas desde tierra.

**Por qué $1/\lambda^4$: el argumento de Rayleigh.** Rayleigh llegó a la ley con un razonamiento de dimensiones, sin resolver ninguna ecuación. La onda dispersada por una partícula pequeña de volumen $V$, a una distancia $r$, tiene una amplitud proporcional a $V$ (más materia, más reemisión) e inversamente proporcional a $r$ (la energía se reparte en esferas cada vez más grandes, semana 16, y la amplitud va con la raíz de la energía). Pero el cociente amplitud dispersada / amplitud incidente no puede tener unidades. $V/r$ tiene unidades de longitud al cuadrado, y la única longitud que queda en el problema es la longitud de onda. Así que el cociente tiene que ser proporcional a $V/(r\,\lambda^2)$. La intensidad va con el cuadrado de la amplitud, es decir, con $V^2/(r^2\lambda^4)$. Ahí está el $1/\lambda^4$. Este tipo de razonamiento, el **análisis dimensional**, es una herramienta muy potente para adivinar leyes físicas antes de calcularlas.

**Ejercicios**

1. Comprueba que $I = I_0 e^{-kx}$ cumple $dI/dx = -kI$.
2. Una estrella tiene, en magnitudes relativas, un brillo $I = 0{,}80$ con masa de aire 1,2 y $I = 0{,}62$ con masa de aire 2,5. Calcula $\tau$ y el brillo fuera de la atmósfera.
3. Con el argumento de Rayleigh, ¿cómo cambia la luz dispersada si el volumen de la partícula se duplica?

<details>
<summary>Soluciones</summary>

1. $dI/dx = I_0 \cdot (-k)\,e^{-kx} = -k\,I$.
2. $\ln 0{,}80 = -0{,}223$ y $\ln 0{,}62 = -0{,}478$. Pendiente: $(-0{,}478 + 0{,}223)/(2{,}5 - 1{,}2) \approx -0{,}196$, así que **$\tau \approx 0{,}196$**. Ordenada: $\ln I_0 = -0{,}223 + 0{,}196 \cdot 1{,}2 \approx 0{,}012$, así que **$I_0 \approx 1{,}01$**.
3. La intensidad va con $V^2$: se multiplica por **4**. Por eso las partículas un poco mayores dispersan mucho más, hasta que alcanzan el tamaño de la longitud de onda y la ley de Rayleigh deja de valer.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [1.7 Polarización, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/1-7-polarizacion). Español, nivel universitario; incluye la polarización por dispersión, la que se ve en el cielo con gafas polarizadas. Verificado el 20 de noviembre de 2026.
2. [1.5 Dispersión, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/1-5-dispersion). Español; la separación de colores en un prisma y el arcoíris (la otra «dispersión»). Verificado el 20 de noviembre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
