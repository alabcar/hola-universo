---
title: "Semana 23 · ¿Es estable el Sistema Solar?"
description: "Fase 2 · Órbitas. Ecuaciones diferenciales explicadas con intuición; perturbaciones, resonancias y caos; las resonancias del Sistema Solar; simulación de tres cuerpos."
sidebar:
  order: 23
  label: "23. ¿Es estable el Sistema Solar?"
---

## La pregunta del cielo

Las leyes de Kepler son exactas para dos cuerpos solos. Pero el Sistema Solar tiene ocho planetas, y cada uno tira de todos los demás. Júpiter empuja un poco a la Tierra cada vez que pasa cerca, y la Tierra a Marte. Son tirones pequeños, miles de veces más débiles que la atracción del Sol. La pregunta es si, sumados durante millones de años, pueden desordenarlo todo: sacar un planeta de su órbita, hacer que dos choquen o expulsar uno del Sistema Solar.

Newton ya se lo preguntó, y pensaba que de vez en cuando haría falta una intervención divina para recolocar los planetas. Un siglo después, Laplace y Lagrange creyeron demostrar que el sistema era estable. A finales del siglo XIX, Henri Poincaré descubrió que el problema de tres cuerpos no tiene solución general y que su movimiento puede ser **caótico**: impredecible a largo plazo, aunque esté gobernado por leyes exactas. La respuesta actual, con simulaciones por ordenador, es matizada, y la verás al final de la semana.

Esta semana aprendes qué es una ecuación diferencial, que es el lenguaje en el que están escritas todas estas leyes, qué son las perturbaciones y las resonancias, y simulas tres cuerpos.

## Las cinco sesiones

### Sesión 1 · Matemáticas: qué es una ecuación diferencial (35-45 min)

**Ecuaciones cuya incógnita es una función.** En las ecuaciones de la semana 18, la incógnita era un número. En una **ecuación diferencial**, la incógnita es una función, por ejemplo la posición de un planeta en cada instante, $x(t)$. Y la ecuación no dice cuánto vale la función, sino **cómo cambia**: relaciona la función con su derivada (semana 10), su ritmo de cambio.

**El ejemplo más sencillo: crecer en proporción a lo que hay.** Una población de bacterias crece más deprisa cuantas más bacterias hay. Si cada hora cada bacteria produce, en promedio, $k$ bacterias nuevas, el ritmo de cambio es proporcional a la población:

$$\frac{dN}{dt} = k\,N.$$

Se lee: «el ritmo de cambio de $N$ es $k$ veces $N$». La solución es la **función exponencial**: $N(t) = N_0\,e^{kt}$, donde $N_0$ es la población inicial y $e \approx 2{,}718$ es el número de Euler. Si $k$ es negativo, la ecuación describe algo que disminuye en proporción a lo que queda, como la desintegración radiactiva.

**Una ecuación diferencial es una receta para avanzar.** Aunque no sepas resolverla con una fórmula, la ecuación te dice siempre hacia dónde va la función desde donde está. Si conoces el valor ahora, sabes su ritmo de cambio ahora, y puedes dar un paso pequeño $\Delta t$:

$$N(t + \Delta t) \approx N(t) + \frac{dN}{dt}\,\Delta t = N(t) + k\,N(t)\,\Delta t.$$

Es el **método de Euler**, el que usaste en la semana 8. Repitiendo pasos se construye la solución entera. Por eso, en la práctica, las ecuaciones diferenciales difíciles se resuelven con ordenador.

**La segunda ley de Newton es una ecuación diferencial.** La aceleración es la derivada de la velocidad, y la velocidad, la derivada de la posición. Así que $\vec{F} = m\vec{a}$ dice cómo cambia la velocidad de un cuerpo según dónde esté. Para un planeta alrededor del Sol:

$$\frac{d^2\vec{r}}{dt^2} = -\frac{GM}{r^3}\,\vec{r}.$$

Es una ecuación diferencial **de segundo orden**, porque aparece la segunda derivada. Todas las simulaciones de órbitas que has hecho desde la semana 17 resuelven esta ecuación paso a paso.

**El oscilador.** Otro ejemplo fundamental: un muelle que tira hacia el centro con una fuerza proporcional a lo que se ha estirado, $F = -k x$. La ecuación es $\dfrac{d^2x}{dt^2} = -\omega^2 x$, con $\omega^2 = k/m$, y su solución es $x(t) = A\cos(\omega t + \varphi)$: una oscilación con la frecuencia angular $\omega$. Aparece en péndulos, cuerdas de guitarra, circuitos eléctricos, y también en las pequeñas oscilaciones de las órbitas alrededor de una órbita perfecta.

:::note[De dónde viene la palabra]
**Diferencial** viene del latín *differentia*, «diferencia». Leibniz, que inventó el cálculo a la vez que Newton e independientemente de él, escribía $dx$ para una diferencia infinitamente pequeña de $x$: la *d* es la inicial de *differentia*. Su notación, $dN/dt$, es la que ha sobrevivido. **Exponencial** viene de *exponente*: la variable está en el exponente. El número **$e$** lleva la inicial de Euler, que fue quien lo estudió a fondo y lo bautizó.
:::

**Ejercicios**

1. Una población de 1000 bacterias crece con $k = 0{,}2$ por hora. Da un paso de Euler de 1 hora. ¿Cuántas bacterias predice? ¿Y la fórmula exacta, $1000\,e^{0{,}2}$?
2. Con la misma población, da cinco pasos de Euler de 0,2 horas. ¿Te acercas más al valor exacto?
3. Un péndulo pequeño oscila con $\omega = 3$ rad/s. ¿Cuál es su periodo?

<details>
<summary>Soluciones</summary>

1. Euler: $1000 + 0{,}2 \cdot 1000 \cdot 1 =$ **1200**. Exacta: $1000\,e^{0{,}2} \approx$ **1221**.
2. Cada paso multiplica por $1{,}04$: $1000 \cdot 1{,}04^5 \approx$ **1217**. Más cerca: con pasos más pequeños, Euler se acerca a la solución exacta.
3. $T = 2\pi/\omega \approx$ **2,09 s**.

</details>

### Sesión 2 · Matemáticas: el empujón a tiempo, o qué es una resonancia (30-40 min)

**El columpio.** Para que un columpio suba mucho no hace falta empujar fuerte: hace falta empujar **en el momento justo**, una vez en cada oscilación, siempre en la misma fase. Cada empujón pequeño se suma al anterior, y la amplitud crece y crece. Si empujas a un ritmo distinto del natural del columpio, unas veces empujas a favor y otras en contra, y los empujones se cancelan.

Eso es una **resonancia**: un sistema que oscila con una frecuencia natural $\omega_0$ recibe un empuje periódico con una frecuencia $\omega$ igual o muy parecida a la suya. En el lenguaje de la sesión 1:

$$\frac{d^2x}{dt^2} = -\omega_0^2\,x + F\cos(\omega t).$$

Si $\omega$ es muy distinta de $\omega_0$, la oscilación se queda pequeña. Si $\omega = \omega_0$, la amplitud crece sin límite (en la realidad, el rozamiento la frena). En el cuaderno lo verás.

**Resonancias entre periodos.** En las órbitas, la resonancia aparece cuando los periodos de dos cuerpos están en una proporción de números enteros pequeños: 2:1, 3:2, 3:1. Si un asteroide da exactamente tres vueltas mientras Júpiter da una, los dos se encuentran siempre en los mismos puntos de la órbita del asteroide. Los tirones de Júpiter, que en una órbita cualquiera se repartirían al azar y se compensarían, se repiten una y otra vez en el mismo sitio y con la misma dirección, y se acumulan, como los empujones al columpio.

**Ejercicios**

1. Un asteroide está en resonancia 3:1 con Júpiter, que tarda 11,86 años. ¿Cuánto tarda el asteroide en dar la vuelta al Sol? ¿A qué distancia media está? (Usa la semana 15.)
2. ¿A qué distancia está la resonancia 2:1?

<details>
<summary>Soluciones</summary>

1. $T = 11{,}86/3 \approx 3{,}95$ años y $a = 3{,}95^{2/3} \approx$ **2,50 ua**.
2. $T = 5{,}93$ años y $a = 5{,}93^{2/3} \approx$ **3,28 ua**.

</details>

### Sesión 3 · Física: perturbaciones, resonancias y caos (35-45 min)

**Perturbaciones.** Una **perturbación** es una fuerza pequeña que se suma a la principal. La órbita de la Tierra es, ante todo, una elipse de Kepler alrededor del Sol, pero los demás planetas la deforman un poco: su excentricidad cambia lentamente a lo largo de cientos de miles de años, y su perihelio va girando. Durante siglos, los astrónomos calcularon estas perturbaciones a mano, con series de aproximaciones cada vez más largas.

El mayor éxito de este método fue el **descubrimiento de Neptuno**. Urano no se movía exactamente como predecían los cálculos, ni siquiera teniendo en cuenta a Júpiter y Saturno. Urbain Le Verrier, en Francia, supuso que la causa era un planeta desconocido más lejano y calculó dónde tenía que estar. El 23 de septiembre de 1846, Johann Galle lo encontró en el observatorio de Berlín a menos de un grado de la posición predicha. Un planeta descubierto con papel y lápiz.

**Resonancias que vacían.** El cinturón de asteroides, entre Marte y Júpiter, tiene huecos: distancias al Sol en las que casi no hay asteroides. Los descubrió Daniel Kirkwood en el siglo XIX y se llaman **huecos de Kirkwood**. Están justo en las resonancias con Júpiter: 3:1 (2,50 ua), 5:2 (2,82 ua), 7:3 (2,96 ua) y 2:1 (3,28 ua). Los tirones repetidos de Júpiter alargan las órbitas de los asteroides que caen allí hasta que cruzan la de Marte o la de la Tierra, y acaban expulsados o chocando. Muchos meteoritos que caen en la Tierra vienen de la resonancia 3:1. Algo parecido ocurre en los anillos de Saturno: la división de Cassini, el hueco oscuro más visible, coincide con una resonancia 2:1 con la luna Mimas.

**Resonancias que protegen.** No todas las resonancias desestabilizan. Plutón da dos vueltas al Sol mientras Neptuno da tres (resonancia 3:2). Aunque la órbita de Plutón cruza la de Neptuno, la resonancia hace que, cada vez que Plutón pasa por allí, Neptuno esté lejos: nunca se acercan a menos de unas 17 ua. Y las lunas de Júpiter Ío, Europa y Ganímedes tienen periodos en proporción 1:2:4, una **resonancia de Laplace** que se mantiene sola: si una se adelanta un poco, los tirones de las otras la corrigen. Esa resonancia mantiene un poco alargada la órbita de Ío, y las mareas que eso produce dentro de Ío alimentan sus volcanes (semana 21).

**Caos.** En 1889, Henri Poincaré ganó un premio convocado por el rey Óscar II de Suecia sobre la estabilidad del Sistema Solar. Al revisar su trabajo encontró un error, y al corregirlo descubrió algo mucho más profundo: en el problema de tres cuerpos, órbitas que empiezan casi igual pueden separarse cada vez más deprisa, de forma exponencial. Es lo que hoy se llama **caos**: el sistema sigue leyes exactas y deterministas, pero cualquier error mínimo en el punto de partida crece tanto que, pasado un tiempo, la predicción no vale.

**Entonces, ¿es estable?** Las simulaciones numéricas, empezando por las de Jacques Laskar en 1989, muestran que el Sistema Solar es caótico: el error en la posición de los planetas interiores se multiplica por 10 cada 10 millones de años, más o menos. Eso no significa que se vaya a desmontar. Significa que no se puede predecir dónde estará exactamente la Tierra en su órbita dentro de 100 millones de años. Los planetas exteriores son muy estables. El punto débil es Mercurio: en simulaciones publicadas en 2009 por Laskar y Gastineau, en torno al 1 % de los casos su órbita se alarga tanto en los próximos 5000 millones de años que podría chocar con Venus o con el Sol. En el 99 % restante, todo sigue más o menos como ahora hasta que el Sol se convierta en gigante roja.

:::note[De dónde viene la palabra]
**Perturbar** viene del latín *perturbare*, «desordenar del todo», de *per*, «completamente», y *turbare*, «agitar, enturbiar». **Resonancia** viene de *resonare*, «volver a sonar»: una cuerda que vibra sola cuando suena cerca su misma nota. **Caos** es el griego *cháos*, el abismo informe y vacío que, según Hesíodo, existía antes que todo lo demás. **Estable** viene de *stabilis*, «que se tiene en pie», de *stare*, «estar de pie».
:::

**Qué hacer**

1. Explica con tus palabras por qué una resonancia acumula los tirones y una órbita no resonante los compensa.
2. Neptuno tarda 164,8 años en dar la vuelta. Comprueba que el periodo de Plutón, 247,9 años, está en proporción 3:2.
3. Con los periodos de Ío (1,769 días), Europa (3,551 días) y Ganímedes (7,155 días), calcula los cocientes Europa/Ío y Ganímedes/Ío.

<details>
<summary>Soluciones</summary>

1. En una órbita no resonante, Júpiter encuentra al asteroide cada vez en un punto distinto de su órbita y le tira en direcciones distintas: unas veces lo acelera, otras lo frena, y en promedio no cambia nada. En resonancia, el encuentro se produce siempre en el mismo punto y el tirón va siempre en el mismo sentido, así que el efecto crece.
2. $247{,}9/164{,}8 \approx 1{,}504$, prácticamente **3/2**.
3. Europa/Ío $= 2{,}007$ y Ganímedes/Ío $= 4{,}045$: casi exactamente **1:2:4**.

</details>

### Sesión 4 · Astronomía y observación: una resonancia que se puede ver (30-45 min)

**Las lunas de Júpiter.** Con los prismáticos de la semana 22, sigue a Júpiter varias noches y apunta la posición de sus lunas. Con Stellarium puedes hacerlo de forma mucho más rápida y precisa: centra Júpiter, haz zoom hasta ver las cuatro lunas con su nombre y avanza el tiempo de hora en hora.

1. Mide cuánto tarda Ío en volver a la misma posición respecto a Júpiter, por ejemplo, a la máxima separación hacia el este. Repite con Europa. ¿Está uno en el doble del otro?
2. Busca un momento en que Ío y Europa estén alineadas del mismo lado de Júpiter (en **conjunción**). Fíjate en dónde está Ganímedes. Repite con otra conjunción de Ío y Europa. La resonancia de Laplace hace que las tres nunca estén alineadas a la vez del mismo lado de Júpiter.

**Los huecos de Kirkwood en una gráfica pública.** Busca una imagen del histograma de los semiejes mayores de los asteroides («huecos de Kirkwood» o «Kirkwood gaps»). Verás la distribución de asteroides con muescas en 2,50, 2,82, 2,96 y 3,28 ua. Es lo que vas a reproducir de forma simplificada en el cuaderno.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 23:

- resuelve con Euler la ecuación $dN/dt = kN$ y la compara con la exponencial, y dibuja su **campo de pendientes**,
- simula un oscilador empujado periódicamente y muestra que la amplitud crece mucho solo cuando el empuje va al ritmo natural (resonancia),
- simula un problema de tres cuerpos: el Sol, Júpiter y 161 asteroides sin masa entre 2 y 3,6 ua, durante 4000 años,
- mide cuánto cambia la excentricidad de cada asteroide y encuentra los picos justo en las resonancias con Júpiter, donde están los huecos de Kirkwood.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-23.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-23.ipynb)

## Qué has aprendido

- **La respuesta.** El Sistema Solar es caótico, pero estable a efectos prácticos. Las perturbaciones entre planetas cambian lentamente sus órbitas y hacen imposible predecir sus posiciones exactas más allá de unas decenas de millones de años, pero en la gran mayoría de las simulaciones no se pierde ningún planeta antes de que el Sol envejezca. El punto débil es Mercurio.
- **Las resonancias.** Cuando los periodos de dos cuerpos están en proporción de enteros pequeños, los tirones se acumulan. Unas veces vacían una región (huecos de Kirkwood, división de Cassini) y otras mantienen una configuración estable (Neptuno y Plutón, las lunas de Júpiter).
- **Las herramientas.** Qué es una ecuación diferencial, la exponencial como solución de $dN/dt = kN$, el oscilador y su solución con seno y coseno, el método de Euler como forma general de resolver ecuaciones diferenciales, y la idea de resonancia.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 13.5, Leyes del movimiento planetario de Kepler, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-5-leyes-del-movimiento-planetario-de-kepler). Español; las órbitas de dos cuerpos, el punto de partida sobre el que se calculan las perturbaciones. Verificado el 6 de noviembre de 2026.
2. [Orbital resonances of the Galilean moons of Jupiter (The Planetary Society)](https://planetary.org/space-images/orbital-resonances-of-galilean-moons). Inglés; una animación de la resonancia 1:2:4 de Ío, Europa y Ganímedes. Verificado el 6 de noviembre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

Los cocientes de los periodos de las lunas galileanas los he contrastado en una fuente universitaria el 6 de noviembre de 2026. Los datos sobre el caos del Sistema Solar resumen trabajos de investigación publicados; no he enlazado los artículos originales porque no he podido abrirlos.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
