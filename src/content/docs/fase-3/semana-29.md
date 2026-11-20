---
title: "Semana 29 · ¿Por qué se atraen los imanes?"
description: "Fase 3 · La luz. Campos escalares y vectoriales, líneas de campo, el campo de un dipolo, carga eléctrica y ley de Coulomb, corrientes e imanes, el campo magnético de la Tierra, el viento solar y las auroras."
sidebar:
  order: 29
  label: "29. ¿Por qué se atraen los imanes?"
---

## La pregunta del cielo

Acerca dos imanes y notarás que se atraen o se repelen sin tocarse, a través del aire, de un papel o de tu mano. Una brújula apunta al norte en cualquier parte del mundo, como si algo invisible tirara de ella. Y en las noches de tormenta solar, el cielo de las regiones polares se llena de cortinas de luz verde y roja que se mueven en silencio.

Las tres cosas tienen la misma raíz: el **campo magnético**. Esta semana aprendes qué es un campo, cómo se dibuja, qué tienen que ver la electricidad y el magnetismo (resultaron ser la misma cosa) y por qué las auroras aparecen cerca de los polos. Es la preparación para la gran pregunta de la semana que viene: ¿qué es, de verdad, la luz?

:::note[De dónde viene la palabra]
**Imán** llega del francés *aimant*, y este del latín *adamas, adamantis*, «diamante, acero muy duro», del griego *adámas*, «indomable». En la Edad Media el nombre del metal más duro pasó a la piedra que atrae el hierro, quizá ayudado por el parecido con el francés *aimer*, «amar». **Magnetismo** viene del griego *magnḗtis líthos*, «piedra de Magnesia», una región donde abundaba la magnetita (hay dos lugares antiguos con ese nombre, uno en Grecia y otro en la actual Turquía). **Brújula** viene del italiano *bussola*, «cajita»: la aguja imantada se guardaba en una caja de madera de boj.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: campos escalares y vectoriales (35-45 min)

**Un campo es un mapa.** En física, un **campo** es una cantidad que tiene un valor en cada punto del espacio. Ya conoces dos tipos sin saberlo:

- Un **campo escalar** da un número en cada punto. El mapa de temperaturas del telediario es un campo escalar: en cada lugar, una temperatura. Se dibuja con colores o con **curvas de nivel** que unen los puntos con el mismo valor, como las isobaras o las curvas de altitud de un mapa topográfico.
- Un **campo vectorial** da un vector en cada punto: un tamaño y una dirección (semana 9). El mapa del viento es un campo vectorial: en cada lugar, hacia dónde sopla y con qué fuerza. Se dibuja con flechas.

**El campo gravitatorio.** En la semana 16 viste que la Tierra atrae a la Luna con una fuerza $F = GMm/r^2$. Si divides esa fuerza por la masa del objeto atraído, te queda algo que solo depende de la Tierra y del lugar:

$$g = \frac{F}{m} = \frac{GM}{r^2}.$$

Es el **campo gravitatorio** de la Tierra. En cada punto del espacio, es un vector que apunta hacia el centro de la Tierra, con un tamaño que disminuye con el cuadrado de la distancia. En la superficie vale 9,8 m/s². Pensar en campos cambia la pregunta: en lugar de «¿cómo puede la Tierra tirar de la Luna a distancia?», la Tierra crea un campo a su alrededor, y la Luna responde al campo que hay **donde ella está**.

**Líneas de campo.** Una forma muy útil de dibujar un campo vectorial es con **líneas de campo**: curvas que, en cada punto, siguen la dirección del vector. Donde las líneas se juntan, el campo es intenso; donde se separan, es débil. Las líneas del campo gravitatorio de la Tierra son rectas que entran radialmente en ella, como las púas de un erizo, más juntas cerca y más separadas lejos.

**Superposición.** Si hay varias masas, el campo total en un punto es la **suma vectorial** de los campos de cada una, igual que se suman las ondas (semana 27).

**Ejercicios**

1. ¿Cuánto vale el campo gravitatorio de la Tierra a la distancia de la Luna, unos 60 radios terrestres?
2. A mitad de camino entre la Tierra y la Luna, los dos campos apuntan en sentidos opuestos. ¿Cuál es mayor? (La Tierra tiene unas 81 veces la masa de la Luna.)
3. ¿En qué punto entre la Tierra y la Luna se anulan los dos campos? Pista: $81/x^2 = 1/(D - x)^2$, con $D$ la distancia Tierra-Luna.

<details>
<summary>Soluciones</summary>

1. $9{,}8/60^2 \approx$ **0,0027 m/s²**.
2. A la misma distancia, el de la Tierra es **81 veces mayor**.
3. Tomando raíces, $9/x = 1/(D - x)$, así que $9(D - x) = x$ y $x = 0{,}9\,D$: a **nueve décimas** del camino, unos 346 000 km de la Tierra.

</details>

### Sesión 2 · Matemáticas: el campo de un dipolo (35-45 min)

**Dos cargas opuestas.** La electricidad tiene algo que la gravedad no tiene: hay dos tipos de carga, positiva y negativa. Las del mismo signo se repelen y las de signo contrario se atraen. Una carga positiva y una negativa, iguales y muy próximas, forman un **dipolo**. Un imán, como verás en la sesión 3, se comporta igual: tiene un polo norte y un polo sur.

**Por qué el dipolo es más débil de lejos.** Pon una carga $+q$ y una $-q$ separadas una distancia $d$, y mira el campo en un punto sobre la línea que las une, a una distancia $r$ del centro, mucho mayor que $d$. La carga positiva está a $r - d/2$ y la negativa a $r + d/2$, y sus campos tienen sentidos opuestos (con $k$ una constante que verás en la sesión 3):

$$E = \frac{kq}{(r - d/2)^2} - \frac{kq}{(r + d/2)^2}.$$

Es la misma resta que en la fuerza de marea de la semana 21, y se resuelve con la misma aproximación binomial. Sacando $r^2$ factor común, $(1 \mp d/2r)^{-2} \approx 1 \pm d/r$, y

$$E \approx \frac{kq}{r^2}\left[\left(1 + \frac{d}{r}\right) - \left(1 - \frac{d}{r}\right)\right] = \frac{2kqd}{r^3}.$$

El campo de un dipolo cae con el **cubo** de la distancia, no con el cuadrado: desde lejos, las dos cargas casi se anulan, y solo queda una pequeña diferencia. El producto $p = qd$ se llama **momento dipolar**. Lo mismo vale para un imán: si te alejas al doble de distancia, su campo se divide por ocho. Por eso un imán de nevera sujeta un papel pero no atrae un clip a un palmo.

**La forma de las líneas.** Las líneas de un dipolo salen de la carga positiva (o del polo norte), se abren en arcos y vuelven a la negativa (o al polo sur). Es la forma que dibujan las limaduras de hierro alrededor de un imán, y la forma del campo magnético de la Tierra. El cuaderno de esta semana la dibuja.

:::note[De dónde viene la palabra]
**Campo** viene del latín *campus*, «llanura, terreno abierto». Michael Faraday hablaba en el siglo XIX de «líneas de fuerza», y la palabra *field* para el espacio donde actúan se generalizó en su época: una extensión llena de algo, como un campo de trigo. **Dipolo** es «dos polos», del griego *di-*, «dos».
:::

**Ejercicios**

1. El campo magnético de la Tierra vale unos 50 µT (microteslas) en su superficie. Si se comporta como un dipolo, ¿cuánto vale a 2 radios terrestres del centro? ¿Y a 10?
2. Comprueba numéricamente la aproximación: con $kq = 1$, $d = 1$ y $r = 10$, calcula la resta exacta y compárala con $2/r^3$.
3. Si un imán pequeño atrae un clip a 1 cm con una fuerza justa para levantarlo, ¿con qué fracción de esa fuerza lo atrae a 3 cm, suponiendo que el campo cae como $1/r^3$? (La fuerza sobre el clip cae todavía más deprisa, porque el clip se imanta menos.)

<details>
<summary>Soluciones</summary>

1. A 2 radios, $50/8 \approx$ **6 µT**; a 10 radios, $50/1000 =$ **0,05 µT** (50 nT).
2. $1/9{,}5^2 - 1/10{,}5^2 = 0{,}011080 - 0{,}009070 = 0{,}002010$. La aproximación da $2/1000 = 0{,}002$: un error de medio por ciento.
3. Como mucho, $1/27$ de la fuerza: el campo baja a $1/27$ y la fuerza sobre el clip, todavía más. El clip ya no sube.

</details>

### Sesión 3 · Física: electricidad y magnetismo, una sola cosa (40-45 min)

**La carga eléctrica.** Frota un globo en el pelo y atraerá trocitos de papel. Lo que pasa es que el frotamiento arranca **electrones** de un material y los deja en otro: el que gana electrones queda con carga negativa y el que los pierde, con carga positiva. La carga se mide en **culombios** (C), y la del electrón es $-1{,}602\times10^{-19}$ C. En 1785, Charles-Augustin de Coulomb midió con una balanza de torsión la fuerza entre dos cargas:

$$F = k\,\frac{q_1 q_2}{r^2}, \qquad k \approx 8{,}99\times10^9\ \text{N·m²/C²}.$$

Es la **ley de Coulomb**, con la misma forma que la gravitación de Newton. Pero con una diferencia enorme de intensidad: entre un protón y un electrón, la fuerza eléctrica es unas $2\times10^{39}$ veces mayor que la gravitatoria. Si la gravedad gobierna el universo a gran escala es solo porque los cuerpos grandes tienen casi exactamente tantas cargas positivas como negativas, y la electricidad se anula.

**Ørsted, 1820.** Durante siglos se pensó que electricidad y magnetismo eran fenómenos distintos. En 1820, el danés Hans Christian Ørsted, durante una clase, vio que una aguja imantada se desviaba al pasar corriente por un cable cercano. Una **corriente eléctrica**, que no es más que cargas en movimiento, crea un campo magnético. En pocas semanas, André-Marie Ampère en París encontró que dos cables con corriente se atraen o se repelen como imanes.

**Entonces, ¿qué es un imán?** Un imán es un material donde muchísimas «corrientes» atómicas, sobre todo el giro de los electrones, están alineadas. Cada una es un minúsculo dipolo magnético, y juntas forman uno grande. Por eso, si partes un imán por la mitad, no obtienes un polo norte y un polo sur separados, sino dos imanes completos: no existen polos magnéticos sueltos (los físicos los llaman **monopolos** y nunca han encontrado ninguno). Las líneas de campo magnético siempre se cierran sobre sí mismas.

**La fuerza sobre una carga en movimiento.** Un campo magnético no hace nada a una carga quieta. Sobre una carga que se mueve con velocidad $v$, ejerce una fuerza **perpendicular** a la vez a la velocidad y al campo, de tamaño

$$F = q\,v\,B\,\sin\theta,$$

donde $B$ es la intensidad del campo magnético (en **teslas**, T) y $\theta$ el ángulo entre la velocidad y el campo. Como la fuerza siempre es perpendicular a la velocidad, no cambia la rapidez de la carga, solo su dirección: la hace girar. Una partícula cargada que entra en un campo magnético da vueltas en espiral alrededor de las líneas de campo, como una cuenta ensartada en un hilo. Esa idea explica las auroras.

**Faraday, 1831.** Si una corriente crea un campo magnético, ¿un campo magnético puede crear una corriente? Michael Faraday descubrió que sí, pero solo si el campo **cambia**: al mover un imán dentro de una bobina de cable, aparece una corriente. Es la **inducción**, en la que se basan los generadores eléctricos. Electricidad y magnetismo resultaron ser dos caras de una sola cosa, el **electromagnetismo**, y la semana que viene verás que la luz es precisamente eso.

:::note[De dónde viene la palabra]
**Electricidad** viene del griego *ḗlektron*, «ámbar». Se atribuye a Tales de Mileto, hacia el 600 a. C., la observación de que el ámbar frotado atrae pajitas. En 1600, el médico inglés William Gilbert inventó el adjetivo latino *electricus*, «como el ámbar», en su libro *De magnete*, donde también propuso que la Tierra entera es un gran imán. **Electrón** lo propuso George Johnstone Stoney en 1891. **Corriente**, del latín *currere*, «correr».
:::

**El imán más grande que pisas.** La Tierra tiene un campo magnético parecido al de un dipolo, generado por el movimiento del hierro líquido de su núcleo externo, que funciona como una dinamo. Vale entre 25 y 65 µT en la superficie. Su eje está inclinado unos grados respecto al de rotación, y el **polo norte magnético** (hacia donde apunta la brújula) no coincide con el geográfico: está en el Ártico y se desplaza decenas de kilómetros al año. Por eso la brújula no apunta exactamente al norte verdadero; el ángulo entre las dos direcciones se llama **declinación magnética** y cambia según el lugar y los años. Curiosidad: el polo que atrae al norte de la brújula es, en términos de imanes, un polo **sur**.

**Qué hacer**

1. Calcula la fuerza de Coulomb entre un protón y un electrón separados $5{,}3\times10^{-11}$ m (el tamaño del átomo de hidrógeno).
2. Calcula la fuerza gravitatoria entre los mismos (masas $1{,}67\times10^{-27}$ kg y $9{,}11\times10^{-31}$ kg) y el cociente entre las dos.
3. Explica por qué una brújula cerca de un altavoz o de la puerta de una nevera apunta a donde no debe.

### Sesión 4 · Astronomía y observación: el viento solar y las auroras (30-45 min)

**El viento solar.** La capa externa del Sol, la **corona**, está a más de un millón de grados y no puede quedarse quieta: se escapa continuamente en todas direcciones, en forma de **viento solar**, un gas de protones y electrones que llega a la Tierra a entre 300 y 800 km/s, con unas pocas partículas por centímetro cúbico. A 400 km/s tarda unos 4 días en recorrer 1 ua. Las erupciones del Sol, como las **eyecciones de masa coronal**, lanzan nubes mucho más densas y rápidas, que pueden llegar en uno a tres días.

**El escudo.** El campo magnético de la Tierra desvía el viento solar: como sus partículas tienen carga, no pueden cruzar las líneas de campo y las rodean. Así se forma la **magnetosfera**, una burbuja comprimida por el lado del Sol (hasta unos 10 radios terrestres) y estirada en una larga cola por el lado de la noche. Sin ella, el viento solar habría erosionado buena parte de nuestra atmósfera, como parece haber ocurrido en Marte.

**Las auroras.** Parte de las partículas consiguen entrar por la cola de la magnetosfera, se aceleran y caen en espiral a lo largo de las líneas de campo, que bajan hacia la Tierra cerca de los polos magnéticos. A entre 100 y 300 km de altura chocan con los átomos y las moléculas de la atmósfera y les dan energía, que estos devuelven como luz de colores muy concretos (en la semana 32 entenderás por qué son tan concretos):

- **verde**, el color más común, del oxígeno atómico, hacia los 100-250 km,
- **rojo**, también del oxígeno, en las partes más altas,
- **azul y violeta**, del nitrógeno, en los bordes inferiores.

Las auroras se concentran en un anillo, el **óvalo auroral**, alrededor de cada polo magnético: sobre Noruega, Islandia, Canadá o Alaska en el norte. Cuando llega una tormenta magnética fuerte, el óvalo se ensancha hacia el ecuador. En la gran tormenta de mayo de 2024, la más intensa en dos décadas, se vieron auroras rojizas desde toda España. En la de 1859, el **evento de Carrington**, se vieron casi en el trópico, y los cables del telégrafo echaron chispas.

**Qué puedes hacer tú.**

1. Mira dónde está el polo norte geográfico con la estrella Polar (semana 3) y compárala con lo que marca una brújula, o la del móvil, que lleva un sensor de campo magnético. En la España peninsular, hoy, la diferencia es pequeña, del orden de un grado.
2. Sigue el **índice Kp**, que mide de 0 a 9 la agitación del campo magnético terrestre. Lo publican los servicios de clima espacial, como el de la NOAA. Para ver auroras desde España hace falta un Kp de 8 o 9: ocurre pocas veces en cada ciclo solar, sobre todo cerca del máximo (el último fue hacia 2024-2025).
3. Si hay alerta de tormenta fuerte, busca un lugar oscuro con horizonte norte despejado. Las auroras a baja latitud suelen ser un resplandor rojizo bajo, débil a la vista; los prismáticos no ayudan mucho, porque son extensas.
4. **Experimento de Ørsted en casa.** Pon una brújula sobre la mesa y un cable eléctrico fino encima, en la dirección norte-sur. Toca un momento los extremos del cable con los polos de una pila de 1,5 V: la aguja se desvía. Hazlo solo uno o dos segundos (la pila se calienta en cortocircuito) y nunca con baterías de litio, de móvil o de coche.

:::note[De dónde viene la palabra]
**Aurora** era la diosa romana del amanecer, y su nombre significa «alba». La expresión *aurora borealis*, «amanecer del norte», se suele atribuir a Galileo, hacia 1619, aunque también se ha atribuido al francés Pierre Gassendi. **Boreal** viene de Bóreas, el dios griego del viento del norte; su opuesto es *austral*, de *auster*, el viento del sur.
:::

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 29:

- dibuja el campo de una carga, de dos cargas iguales y de un dipolo con flechas y líneas de campo,
- comprueba que el campo del dipolo cae como $1/r^3$ en una gráfica logarítmica,
- dibuja las líneas del campo magnético de la Tierra como un dipolo y marca dónde tocan el suelo,
- simula una partícula cargada en un campo magnético y la ve girar en espiral alrededor de las líneas de campo.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-29.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-29.ipynb)

## Qué has aprendido

- **La respuesta.** Los imanes se atraen porque cada uno crea un campo magnético a su alrededor y responde al campo del otro. Ese campo nace de cargas eléctricas en movimiento: en un imán, de los electrones de sus átomos, alineados. Electricidad y magnetismo son una sola interacción, el electromagnetismo.
- **El cielo.** La Tierra es un gran imán que desvía el viento solar. Las partículas que se cuelan bajan en espiral por las líneas de campo hacia los polos y encienden la atmósfera: son las auroras.
- **Las herramientas.** Campos escalares y vectoriales, líneas de campo, superposición, el campo de un dipolo (que cae como $1/r^3$), la ley de Coulomb y la fuerza magnética sobre una carga en movimiento.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**El producto vectorial.** La fuerza magnética es perpendicular a la velocidad y al campo a la vez. La operación matemática que fabrica un vector perpendicular a otros dos es el **producto vectorial**, $\vec{a}\times\vec{b}$. Su tamaño es $|\vec{a}|\,|\vec{b}|\sin\theta$ (el área del paralelogramo que forman), su dirección es perpendicular a los dos, y su sentido lo da la **regla de la mano derecha**: si los dedos de la mano derecha giran de $\vec{a}$ hacia $\vec{b}$ por el camino más corto, el pulgar apunta hacia $\vec{a}\times\vec{b}$. En componentes:

$$\vec{a}\times\vec{b} = (a_y b_z - a_z b_y,\; a_z b_x - a_x b_z,\; a_x b_y - a_y b_x).$$

Dos propiedades: $\vec{a}\times\vec{b} = -\,\vec{b}\times\vec{a}$ (el orden importa), y $\vec{a}\times\vec{a} = 0$. Con él, la fuerza magnética se escribe de forma compacta, la **fuerza de Lorentz**:

$$\vec{F} = q\,\vec{v}\times\vec{B}.$$

**El radio de giro.** Si la velocidad es perpendicular al campo, la fuerza magnética es la que obliga a la partícula a girar: produce la aceleración hacia el centro, $v^2/r$, de cualquier movimiento circular (semanas 9 y 17). Así que $q v B = m v^2/r$. Despejando,

$$r = \frac{m v}{|q| B}, \qquad T = \frac{2\pi r}{v} = \frac{2\pi m}{|q| B}.$$

Es el **radio de Larmor** (o de giro), y $T$ el periodo de **ciclotrón**. Fíjate en algo sorprendente: el periodo no depende de la velocidad. Una partícula más rápida da vueltas más grandes, pero tarda lo mismo. En eso se basan los ciclotrones, los primeros aceleradores de partículas. Si la velocidad tiene además una componente a lo largo del campo, esa parte no siente fuerza, y la partícula avanza mientras gira: una **hélice**.

**Ejercicios**

1. Calcula $\vec{a}\times\vec{b}$ para $\vec{a} = (1, 0, 0)$ y $\vec{b} = (0, 1, 0)$. Comprueba que el resultado es perpendicular a los dos.
2. Un protón del viento solar (masa $1{,}67\times10^{-27}$ kg) viaja a 400 km/s perpendicular al campo magnético interplanetario, que vale unos 5 nT. ¿Cuál es su radio de giro?
3. Un electrón de una aurora ($9{,}11\times10^{-31}$ kg) se mueve a $10^7$ m/s en un campo de 50 µT. ¿Radio y periodo de giro?

<details>
<summary>Soluciones</summary>

1. $(0\cdot0 - 0\cdot1,\; 0\cdot0 - 1\cdot0,\; 1\cdot1 - 0\cdot0) = (0, 0, 1)$. Su producto escalar con $\vec{a}$ y con $\vec{b}$ es cero: es perpendicular a los dos.
2. $r = 1{,}67\times10^{-27} \cdot 4\times10^5 / (1{,}602\times10^{-19} \cdot 5\times10^{-9}) \approx$ **830 km**.
3. $r = 9{,}11\times10^{-31} \cdot 10^7/(1{,}602\times10^{-19} \cdot 5\times10^{-5}) \approx$ **1,1 m**. $T = 2\pi m/(qB) \approx$ **0,7 µs**: más de un millón de vueltas por segundo.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [5.3 Ley de Coulomb, *Física universitaria* vol. 2 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-2/pages/5-3-ley-de-coulomb). Español; la fuerza entre cargas con ejemplos resueltos. Verificado el 20 de noviembre de 2026.
2. [11.2 Campos y líneas magnéticas, *Física universitaria* vol. 2 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-2/pages/11-2-campos-y-lineas-magneticas). Español; la fuerza sobre una carga en movimiento, la regla de la mano derecha y las líneas de campo. Verificado el 20 de noviembre de 2026.
3. [Capítulo 15, El Sol, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/15%3A_El_sol-_Una_estrella_de_jard%C3%ADn-variedad). Español; la corona, el viento solar y el clima espacial. Verificado el 20 de noviembre de 2026.
4. [Una guía sobre el ciclo solar y el clima espacial (NOAA)](https://www.nesdis.noaa.gov/una-guia-sobre-el-ciclo-solar-y-el-clima-espacial). Español; tormentas solares y geomagnéticas. Verificado el 20 de noviembre de 2026.
5. Para seguir el índice Kp, el Centro de Predicción del Clima Espacial de la NOAA (*Space Weather Prediction Center*, swpc.noaa.gov) publica previsiones de auroras. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
