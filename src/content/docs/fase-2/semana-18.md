---
title: "Semana 18 · ¿Cómo se viaja de un planeta a otro?"
description: "Fase 2 · Órbitas. Sistemas de ecuaciones; energía de una órbita y ecuación de la vis viva; transferencia de Hohmann; ventanas de lanzamiento a Marte."
sidebar:
  order: 18
  label: "18. ¿Cómo se viaja de un planeta a otro?"
---

## La pregunta del cielo

Para ir de una ciudad a otra se apunta hacia el destino y se avanza. Para ir de la Tierra a Marte, eso no funciona. Al despegar, la nave ya va a casi 30 km/s alrededor del Sol, porque lleva la velocidad de la Tierra. Y Marte no está quieto esperando: también da vueltas, más despacio. Además, el combustible es muy caro de llevar: cada kilo que se gasta en frenar o acelerar es un kilo menos de instrumentos.

En 1925 el ingeniero alemán Walter Hohmann publicó la forma más barata de pasar de una órbita circular a otra: una media elipse que toca la órbita de salida en su perihelio y la de llegada en su afelio. Dos encendidos del motor, uno al salir y otro al llegar, y el resto del viaje, meses, sin gastar nada, cayendo alrededor del Sol según las leyes de Kepler. Pero hay que salir en el momento justo, para que Marte esté allí cuando llegue la nave. Esos momentos son las **ventanas de lanzamiento**, y se abren una vez cada 26 meses.

Esta semana calculas el viaje completo. Necesitas resolver sistemas de ecuaciones y una fórmula nueva para la velocidad en una órbita elíptica.

## Las cinco sesiones

### Sesión 1 · Matemáticas: sistemas de ecuaciones (35-45 min)

**El problema.** Con una ecuación puedes despejar una incógnita. Pero muchas veces hay dos incógnitas a la vez, y cada ecuación por separado no basta para encontrarlas. Si sabes que dos números suman 10, hay infinitas parejas posibles. Si además sabes que su diferencia es 2, solo hay una: 6 y 4. Un **sistema de ecuaciones** es un conjunto de ecuaciones que deben cumplirse a la vez. En general, para encontrar $n$ incógnitas hacen falta $n$ ecuaciones independientes (que no digan lo mismo con otras palabras).

**Método de sustitución.** Despeja una incógnita en una de las ecuaciones y sustituye el resultado en la otra. Te queda una sola ecuación con una sola incógnita.

> $x + y = 10$ y $x - y = 2$. De la primera, $y = 10 - x$. En la segunda: $x - (10 - x) = 2$, es decir, $2x = 12$, $x = 6$. Y entonces $y = 4$.

**Método de reducción.** Suma o resta las ecuaciones (multiplicadas antes por algún número si hace falta) para que una incógnita desaparezca.

> Sumando las dos ecuaciones anteriores: $2x = 12$. Directamente $x = 6$.

**Sistemas no lineales.** Si las incógnitas aparecen al cuadrado o multiplicadas entre sí, el método de sustitución sigue funcionando, aunque las cuentas sean más largas. Es el caso que vas a necesitar: en una órbita elíptica, las velocidades en el perihelio y en el afelio cumplen dos leyes de conservación a la vez.

:::note[De dónde viene la palabra]
**Sistema** viene del griego *sýstēma*, «conjunto, cosa compuesta de partes», de *synístēmi*, «poner junto». Las ecuaciones de un sistema se cumplen juntas. **Incógnita** viene del latín *incognita*, «cosa desconocida». La costumbre de llamar $x$ a la incógnita se extendió con Descartes en el siglo XVII, que usaba las últimas letras del alfabeto para lo desconocido y las primeras para lo conocido.
:::

**Ejercicios**

1. Resuelve $2x + 3y = 12$ y $x - y = 1$.
2. Un tren sale a 80 km/h y, una hora después, otro sale del mismo sitio a 120 km/h por la misma vía. Plantea un sistema para saber cuándo y dónde lo alcanza.
3. Resuelve $x\,y = 12$ y $x + y = 7$, con $x > y$.

<details>
<summary>Soluciones</summary>

1. De la segunda, $x = 1 + y$. En la primera: $2 + 2y + 3y = 12$, así que $y = 2$ y $x = 3$.
2. Con $t$ el tiempo desde la salida del segundo tren y $d$ la distancia: $d = 80(t + 1)$ y $d = 120\,t$. Igualando, $120t = 80t + 80$: **$t = 2$ h y $d = 240$ km**.
3. $y = 7 - x$ y $x(7 - x) = 12$, es decir, $x^2 - 7x + 12 = 0$, con soluciones 3 y 4. Con $x > y$: **$x = 4$, $y = 3$**.

</details>

### Sesión 2 · Matemáticas: las velocidades en una elipse, por sustitución (30-40 min)

En la semana 14 viste que en el perihelio y el afelio se cumple $r_\text{p}\,v_\text{p} = r_\text{a}\,v_\text{a}$ (segunda ley de Kepler). Y en la semana 17, que la energía por unidad de masa, $\tfrac{1}{2}v^2 - GM/r$, se conserva. Son dos ecuaciones con dos incógnitas, $v_\text{p}$ y $v_\text{a}$:

$$r_\text{p}\,v_\text{p} = r_\text{a}\,v_\text{a}, \qquad \tfrac{1}{2}v_\text{p}^2 - \frac{GM}{r_\text{p}} = \tfrac{1}{2}v_\text{a}^2 - \frac{GM}{r_\text{a}}.$$

Despeja $v_\text{a} = v_\text{p}\,r_\text{p}/r_\text{a}$ de la primera y sustitúyelo en la segunda. Tras agrupar (merece la pena que lo hagas tú con lápiz, despacio) sale

$$v_\text{p}^2 = \frac{GM}{a}\cdot\frac{r_\text{a}}{r_\text{p}}, \qquad \text{con } a = \frac{r_\text{p} + r_\text{a}}{2}.$$

Este resultado es un caso particular de una fórmula que vale en **cualquier punto** de una órbita elíptica, la ecuación de la **vis viva**:

$$v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right).$$

Compruébalo: en el perihelio, $2/r_\text{p} - 1/a = (2a - r_\text{p})/(a\,r_\text{p}) = r_\text{a}/(a\,r_\text{p})$, porque $2a - r_\text{p} = r_\text{a}$. Y en una órbita circular, $r = a$ y queda $v^2 = GM/r$, la de la semana 17.

**Ejercicios**

1. Usa la vis viva para calcular la velocidad de la Tierra en el perihelio ($r = 0{,}983$ ua) y en el afelio ($r = 1{,}017$ ua), sabiendo que $a = 1$ ua y que la velocidad en una órbita circular de 1 ua es 29,78 km/s. Pista: escribe $v^2 = v_\text{c}^2\,(2/r - 1)$, con $r$ en ua.
2. ¿Qué velocidad tendría que llevar un objeto a 1 ua del Sol para que su órbita tuviera $a = 2$ ua?

<details>
<summary>Soluciones</summary>

1. Perihelio: $v = 29{,}78\sqrt{2/0{,}983 - 1} \approx$ **30,29 km/s**. Afelio: $v = 29{,}78\sqrt{2/1{,}017 - 1} \approx$ **29,28 km/s**.
2. $v = 29{,}78\sqrt{2/1 - 1/2} = 29{,}78\sqrt{1{,}5} \approx$ **36,5 km/s**.

</details>

### Sesión 3 · Física: energía orbital y transferencia de Hohmann (35-45 min)

**La energía depende solo de $a$.** Multiplicando la vis viva por $m/2$ y restando la energía potencial, la energía total de un cuerpo en órbita es

$$E = -\frac{G M m}{2a}.$$

No depende de la excentricidad: todas las órbitas con el mismo semieje mayor tienen la misma energía (y el mismo periodo, por la tercera ley de Kepler). Para subir a una órbita más grande hay que **aumentar** la energía, es decir, acelerar.

**La transferencia de Hohmann.** Para ir de una órbita circular de radio $r_1$ a otra de radio $r_2$ mayor:

1. **Primer encendido**, en la órbita de salida: se acelera en la dirección del movimiento. La nave pasa de la velocidad circular $v_1 = \sqrt{GM/r_1}$ a la del perihelio de una elipse con $r_\text{p} = r_1$ y $r_\text{a} = r_2$. El aumento de velocidad es $\Delta v_1$.
2. **Viaje sin motor** por media elipse, desde el perihelio hasta el afelio. Dura medio periodo de la elipse de transferencia, cuyo semieje mayor es $a_\text{t} = (r_1 + r_2)/2$:
$$t = \tfrac{1}{2}\,T_\text{t} = \pi\sqrt{\frac{a_\text{t}^3}{GM}}.$$
3. **Segundo encendido**, en el afelio: la nave llega más despacio que la velocidad circular de la órbita de destino, y hay que acelerar otra vez, $\Delta v_2$, para quedarse en ella.

**De la Tierra a Marte.** Con órbitas circulares de 1 y 1,524 ua: $a_\text{t} = 1{,}262$ ua y el viaje dura $\tfrac{1}{2}\cdot 1{,}262^{3/2} \approx 0{,}709$ años, unos **259 días**. Con la vis viva: la nave debe salir a 32,7 km/s respecto al Sol, unos 2,95 km/s más que la Tierra, y llega a Marte a 21,5 km/s, cuando Marte va a 24,1 km/s: necesita 2,6 km/s más para quedarse en su órbita.

Estos impulsos son respecto al Sol. En la práctica, la nave sale desde una órbita baja alrededor de la Tierra, y antes tiene que escapar de la gravedad terrestre. Por conservación de la energía, si la nave debe salir de la influencia de la Tierra con una velocidad sobrante $v_\infty = 2{,}95$ km/s, en la órbita baja necesita $v = \sqrt{v_\infty^2 + v_\text{esc}^2}$, con $v_\text{esc} = 10{,}85$ km/s a 400 km. Sale unos 11,2 km/s, así que el encendido desde la órbita baja es de unos **3,6 km/s**.

**El momento de salir.** La nave tarda 259 días en recorrer 180° alrededor del Sol. En ese tiempo, Marte avanza $360^\circ \cdot 259/687 \approx 136^\circ$. Para que Marte esté en el punto de llegada, al salir debe ir por delante de la Tierra $180^\circ - 136^\circ = 44^\circ$. Esa configuración se repite cada periodo sinódico: **cada 780 días, unos 26 meses**.

:::note[De dónde viene la palabra]
**Vis viva** es latín: «fuerza viva». Así llamó Leibniz, hacia 1686, a la cantidad $m v^2$, el doble de lo que hoy llamamos energía cinética, cuando todavía no existía la palabra *energía*. El nombre ha sobrevivido en la mecánica celeste para esta ecuación. **Delta** ($\Delta$) es la letra griega D, inicial de *diaphorá*, «diferencia»: $\Delta v$ se lee «delta uve» y significa «cambio de velocidad». En astronáutica, el *delta-v* es la moneda con la que se pagan los viajes.
:::

**Qué hacer**

1. Calcula la duración de una transferencia de Hohmann de la Tierra a Venus (0,723 ua) y de la Tierra a Júpiter (5,203 ua).
2. ¿Con qué ángulo debe ir Júpiter por delante de la Tierra al salir? Júpiter tarda 11,86 años en dar la vuelta.
3. Una misión tripulada a Marte con transferencias de Hohmann debe esperar en Marte a que vuelva a abrirse la ventana de regreso. Sin calcularlo, ¿será la espera de días, de semanas o de más de un año? Pista: piensa en dónde está la Tierra cuando la nave llega a Marte.

<details>
<summary>Soluciones</summary>

1. Venus: $a_\text{t} = 0{,}862$ ua, $t = \tfrac{1}{2}\cdot 0{,}862^{3/2} \approx 0{,}40$ años, unos **146 días**. Júpiter: $a_\text{t} = 3{,}10$ ua, $t = \tfrac{1}{2}\cdot 3{,}10^{3/2} \approx$ **2,7 años**.
2. En 2,73 años Júpiter avanza $360^\circ \cdot 2{,}73/11{,}86 \approx 83^\circ$, así que debe ir **97°** por delante.
3. **Más de un año**, unos 450-500 días. Al llegar a Marte, la Tierra, que es más rápida, ya le ha adelantado y está muy por delante. Para volver hay que esperar a que la Tierra dé casi otra vuelta y quede en la posición adecuada.

</details>

### Sesión 4 · Astronomía y observación: ventanas de lanzamiento a Marte (30-45 min)

**El calendario de Marte.** Las ventanas de lanzamiento caen unos meses antes de cada oposición, porque la nave debe salir cuando Marte va unos 44° por delante y llegar cuando la Tierra ya ha pasado a Marte. Las sondas de los últimos años lo muestran bien: la *InSight* de la NASA salió en mayo de 2018 y la *Perseverance*, en julio de 2020, separadas por 26 meses.

**Hazlo tú.** La próxima oposición de Marte es el 19 de febrero de 2027.

1. La Tierra le saca a Marte unos 0,46° al día (semana 13). ¿Cuántos días antes de la oposición iba Marte 44° por delante?
2. ¿Qué fecha da eso? Compárala con el día de hoy.

<details>
<summary>Solución</summary>

1. $44^\circ / 0{,}46^\circ \approx$ **96 días**.
2. 96 días antes del 19 de febrero de 2027 es mediados de **noviembre de 2026**. En este modelo sencillo, la ventana está abierta ahora mismo. Las ventanas reales duran varias semanas y se calculan con las órbitas elípticas e inclinadas; la de este ciclo, según la prensa especializada, cae a finales de 2026.

</details>

**En Stellarium.** Pon una fecha de mediados de noviembre de 2026, busca Marte y el Sol y mide su separación en el cielo (la herramienta de medir ángulos de la versión de escritorio sirve, o compara sus coordenadas). En la oposición estarán a 180°; con Marte 44° por delante de la Tierra en su órbita, la separación aparente en el cielo es bastante menor de 180°, porque Marte está más lejos que el Sol. En el cuaderno calculas cuánto.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 18:

- resuelve con NumPy el sistema de las velocidades en el perihelio y el afelio y lo compara con la vis viva,
- calcula la transferencia de Hohmann de la Tierra a cada planeta: duración, impulsos y ángulo de salida,
- dibuja el viaje a Marte día a día, con la Tierra, Marte y la nave, para ver que llegan juntos,
- calcula la separación en el cielo entre el Sol y Marte el día de salida.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-18.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-18.ipynb)

## Qué has aprendido

- **La respuesta.** Se viaja de un planeta a otro cayendo alrededor del Sol. La forma más barata es la transferencia de Hohmann: media elipse tangente a las dos órbitas, con un impulso al salir y otro al llegar. A Marte se tarda unos 259 días, y solo se puede salir cuando Marte va unos 44° por delante de la Tierra, una vez cada 26 meses.
- **La física.** La energía de una órbita depende solo de su semieje mayor, $E = -GMm/(2a)$, y la velocidad en cualquier punto sale de la vis viva, $v^2 = GM(2/r - 1/a)$.
- **Las herramientas.** Sistemas de ecuaciones por sustitución y por reducción, también no lineales, y el uso combinado de dos leyes de conservación para encontrar dos incógnitas.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 13.5, Leyes del movimiento planetario de Kepler, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-5-leyes-del-movimiento-planetario-de-kepler). Español; el apartado «Transferencias orbitales» calcula una transferencia de Hohmann a Marte paso a paso. Verificado el 6 de noviembre de 2026.
2. [Sección 13.4, Órbita satelital y energía, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-4-orbita-satelital-y-energia). Español; la energía de una órbita. Verificado el 6 de noviembre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

Las fechas de lanzamiento de *InSight* y *Perseverance* y la de la próxima oposición de Marte las he comprobado en fuentes de divulgación el 6 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
