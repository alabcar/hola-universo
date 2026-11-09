---
title: "Semana 11 · ¿Cuánto se acumula con el tiempo?"
description: "Fase 1 · Principios básicos de astronomía. La integral como área bajo la curva, el teorema fundamental del cálculo, distancia recorrida y horas de noche astronómica."
sidebar:
  order: 11
  label: "11. ¿Cuánto se acumula con el tiempo?"
---

## La pregunta del cielo

La derivada responde a «¿a qué ritmo cambia esto ahora?». La pregunta inversa es: si conozco el ritmo en cada instante, ¿cuánto se ha acumulado en total? A partir de la velocidad en cada momento, ¿qué distancia he recorrido? A partir de las horas de oscuridad de cada noche, ¿cuántas horas oscuras tiene un año?

Esta semana aprendes la **integral**, la operación inversa de la derivada, con la imagen del área bajo una curva. Y la aplicas a un problema para el aficionado a la astronomía: cuántas horas de noche realmente oscura hay en un año, y cómo cambian con la latitud.

## Las cinco sesiones

### Sesión 1 · Matemáticas: el área bajo una curva (40-45 min)

**Distancia y área.** Si un coche va a 50 km/h durante 3 horas, recorre $50 \cdot 3 = 150$ km. Dibuja la velocidad frente al tiempo: es una recta horizontal a la altura 50, y el producto $50 \cdot 3$ es el **área del rectángulo** de base 3 h y altura 50 km/h. Las unidades también encajan: km/h por h da km. La distancia recorrida es el área bajo la gráfica de la velocidad.

**Cuando la velocidad cambia.** Esa idea sigue valiendo, y es lo interesante. En la semana 8 viste que, si la velocidad crece de forma uniforme, la distancia es el área de un trapecio. ¿Y si la gráfica es una curva cualquiera? Corta el tiempo en intervalos muy cortos. En cada uno, la velocidad casi no cambia, así que la distancia recorrida en ese intervalo es casi el área de un rectángulo estrecho: velocidad por duración. La distancia total es, aproximadamente, la suma de las áreas de todos esos rectángulos. Para áreas de formas conocidas basta la geometría (rectángulo, triángulo, trapecio); para curvas hay que **aproximar**: cortar en tiras y sumar. Cuantas más tiras, y más estrechas, mejor sale.

**La integral definida.** Esa suma de tiras se llama **suma de Riemann**, por el matemático alemán Bernhard Riemann, que la formalizó en 1854. Su límite cuando las tiras se hacen infinitamente delgadas es la **integral definida** de la función $f$ entre $a$ y $b$, que se escribe

$$\int_a^b f(x)\,dx.$$

El símbolo $\int$ es una S alargada, de «suma». El $dx$ recuerda que cada tira tiene una anchura infinitamente pequeña, y los números $a$ y $b$ son los extremos del intervalo, los **límites de integración**. La idea es muy antigua: Arquímedes, en el siglo III a. C., calculó el área bajo una parábola llenándola con triángulos cada vez más pequeños.

:::note[De dónde viene la palabra]
**Integral** viene del latín *integer*, «entero, intacto» (como *íntegro* o *integridad*): integrar es reconstruir el todo a partir de sus partes infinitamente pequeñas. El nombre lo propuso Jakob Bernoulli en 1690. Leibniz había empezado por llamarla *summa*, «suma», y el signo $\int$ que inventó en 1675 es la *s* larga con la que se escribía *summa* en la letra de la época.
:::

**Ejercicios**

1. Un cuerpo acelera de 0 a 20 m/s en 10 s de forma lineal. ¿Qué distancia recorre?
2. Otro pasa de 10 a 30 m/s en 10 s de forma lineal. ¿Y este?
3. Aproxima el área bajo $y = x^2$ entre 0 y 3 con tres rectángulos de ancho 1, usando la altura en el extremo izquierdo y en el derecho. ¿Cuál es la media?
4. ¿Qué área hay bajo $y = 4$ entre $x=1$ y $x=6$?

<details>
<summary>Soluciones</summary>

1. Triángulo de base 10 y altura 20: $\tfrac{1}{2}\cdot 10 \cdot 20 =$ **100 m**.
2. Trapecio: $\tfrac{10+30}{2}\cdot 10 =$ **200 m**.
3. Izquierdo: $0 + 1 + 4 =$ **5** (se queda corto, porque la curva sube dentro de cada tira); derecho: $1 + 4 + 9 =$ **14** (se pasa); media: **9,5**. El valor exacto es 9: con más tiras el error baja.
4. Rectángulo de base 5 y altura 4: **20**.

</details>

### Sesión 2 · Matemáticas: la integral y la derivada (40-45 min)

**El problema.** Calcular áreas con tiras funciona, pero es costoso, y a mano solo da aproximaciones. La sorpresa que descubrieron Newton y Leibniz es que hay un atajo: **integrar es lo contrario de derivar**.

**Por qué.** Llama $A(x)$ al área bajo la curva de $f$ desde un punto fijo $a$ hasta $x$. Es una función: si mueves $x$ hacia la derecha, el área crece. ¿A qué ritmo crece? Si avanzas un poquito, $h$, el área aumenta en una tira estrecha de anchura $h$ y altura casi $f(x)$: el aumento es casi $f(x)\cdot h$. El ritmo de crecimiento es ese aumento dividido entre $h$, que tiende a $f(x)$ cuando $h$ tiende a cero. Es decir, la derivada de la función área es la función de la curva: $A'(x) = f(x)$.

**El teorema fundamental del cálculo.** Por tanto, para calcular un área basta con encontrar una función $F$ cuya derivada sea $f$ (se llama una **primitiva** de $f$) y restar sus valores en los extremos:

$$\int_a^b f(x)\,dx = F(b) - F(a), \qquad \text{si } F'(x) = f(x).$$

Es el **teorema fundamental del cálculo**, y une las dos mitades del cálculo: la derivada (ritmos) y la integral (acumulaciones). Una función tiene muchas primitivas, que se diferencian en una constante (porque la derivada de una constante es cero), pero esa constante desaparece al restar $F(b) - F(a)$.

**Primitivas de potencias.** Como ya sabes que la derivada de $x^n$ es $n x^{n-1}$, puedes ir al revés: la primitiva de $x^n$ es $x^{n+1}/(n+1)$. Compruébalo derivando: la derivada de $x^{n+1}/(n+1)$ es $(n+1)x^n/(n+1) = x^n$. Por ejemplo, $\int_0^3 x^2\,dx = 3^3/3 - 0 = 9$, el valor al que se acercaban las sumas de rectángulos de la sesión 1. Y con el movimiento de caída: si $v = g\,t$, la distancia es $\int_0^t g\,t'\,dt' = \tfrac{1}{2} g t^2$, el resultado de la semana 8. (La letra $t'$ es solo un nombre para la variable que recorre el intervalo, para no confundirla con el extremo $t$.)

**Ejercicios**

1. Calcula $\int_0^4 2x\,dx$ e interprétalo geométricamente.
2. Calcula $\int_0^3 x^2\,dx$ y compara con la sesión 1.
3. Una piedra cae con $v = 9{,}81\,t$. ¿Cuánto cae entre $t=0$ y $t=3$ s?
4. Un cuerpo tiene $v(t) = 6t - 4$. ¿Cuánto avanza entre $t = 0$ y $t = 2$ s?

<details>
<summary>Soluciones</summary>

1. $F(x) = x^2$, luego $F(4) - F(0) =$ **16**. Es el área de un triángulo de base 4 y altura 8.
2. $3^3/3 =$ **9**.
3. $\tfrac{1}{2} \cdot 9{,}81 \cdot 9 \approx$ **44,1 m**.
4. $F(t) = 3t^2 - 4t$: $F(2) - F(0) = 12 - 8 =$ **4 m**. (Ojo: durante los primeros 2/3 de segundo la velocidad es negativa y el cuerpo retrocede; la integral da el desplazamiento neto, descontando ese retroceso.)

</details>

### Sesión 3 · Física: acumular magnitudes (35-45 min)

La integral aparece cada vez que una cantidad se acumula a un ritmo que cambia:

- **Posición** = integral de la velocidad: $x(t) = x_0 + \int v\,dt$.
- **Velocidad** = integral de la aceleración: $v(t) = v_0 + \int a\,dt$.
- **Trabajo** = integral de la fuerza a lo largo de un recorrido: $W = \int F\,dx$. Con fuerza constante es $F\,d$, fuerza por distancia. Es el puente hacia la energía de la semana 12.

**Crepúsculos y noche.** Un lugar está de día mientras el Sol está sobre el horizonte. Pero el cielo no se oscurece de golpe al ponerse el Sol: la atmósfera sigue iluminada desde abajo y dispersa luz hacia el suelo. Se distinguen tres fases según cuánto ha bajado el Sol bajo el horizonte:

- el **crepúsculo civil** acaba cuando el Sol está 6° bajo el horizonte: hasta entonces se puede hacer casi cualquier cosa al aire libre sin luz artificial;
- el **náutico**, a 12°: hasta entonces, en el mar, todavía se distingue la línea del horizonte, y los navegantes podían medir la altura de las estrellas sobre ella;
- el **astronómico**, a 18°: solo entonces el cielo está completamente oscuro y se pueden ver los objetos más débiles.

Desde una latitud $\varphi$ y con la declinación del Sol $\delta$ de la semana 1, la altura del Sol en su punto más bajo (a medianoche solar, cuando cruza el meridiano por el norte, bajo el horizonte) es $\varphi + \delta - 90^\circ$. Es la misma idea que la altura máxima de la semana 3, mirando hacia el otro lado. El Sol baja de −18° solo si $\varphi + \delta < 72^\circ$. Si $\varphi + \delta \ge 72^\circ$, no hay noche astronómica: en junio ($\delta = 23{,}4^\circ$) eso ocurre en latitudes superiores a unos $48{,}6^\circ$ N, como París o Londres.

**La integral en el cielo.** El número de horas de noche astronómica de cada día varía con las estaciones. La suma de esas horas a lo largo del año es una integral: el área bajo la curva diaria. El cuaderno la calcula: a 40° de latitud son unas 3100 horas de noche astronómica al año, el 35 % del total, y esa cifra disminuye al subir de latitud (unas 3460 h en el ecuador y unas 1900 h a 70°).

:::note[De dónde viene la palabra]
**Crepúsculo** viene del latín *crepusculum*, de *creper*, «oscuro, dudoso»: la luz incierta entre el día y la noche. **Náutico** viene del griego *naútēs*, «marinero», de *naûs*, «nave». **Primitiva** viene de *primitivus*, «el primero, el original»: la función de la que se parte y cuya derivada es la que tienes.
:::

**Qué hacer**

1. Con la fórmula de la sesión 3, comprueba que a 55° N el Sol no baja de −18° el 21 de junio.
2. Explica por qué en una ciudad con mucha luz casi nunca llegas a ver el cielo de «noche astronómica».

### Sesión 4 · Astronomía y observación (30-45 min)

**Los crepúsculos en Stellarium.**

1. Fija tu lugar y tu fecha.
2. Avanza el tiempo desde el ocaso del Sol y anota la hora a la que la altura del Sol es −6°, −12° y −18°.
3. Calcula la duración de cada fase del crepúsculo (la diferencia entre horas consecutivas) y la duración total entre el ocaso y los −18°.
4. Compara con el modelo del cuaderno, que no incluye la refracción atmosférica (la atmósfera curva un poco la luz y hace que el Sol parezca algo más alto de lo que está, sobre todo cerca del horizonte).

**En el cielo.** Una tarde despejada, anota a qué hora ves salir la primera estrella (o planeta) brillante y a qué hora se apaga el brillo del cielo en el oeste. En una ciudad el crepúsculo astronómico es difícil de apreciar porque la contaminación lumínica ilumina el cielo toda la noche. Anota tus observaciones como una prueba de cómo de oscuro es tu cielo.

No mires nunca al Sol directamente.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 11:

- implementa la integral numérica por rectángulos y por trapecios y compara su error,
- calcula una distancia integrando una velocidad,
- calcula las horas de noche astronómica de cada día para tu latitud,
- integra a lo largo del año y compara el total entre latitudes.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-11.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-11.ipynb)

La fórmula de las horas de Sol por encima de una altura usa trigonometría esférica que aún no puedes demostrar: la usas como caja negra, y compruebas su resultado con Stellarium.

## Qué has aprendido

- **La respuesta.** Una cantidad acumulada es la integral del ritmo al que se acumula, y geométricamente es el área bajo la curva del ritmo. A 40° de latitud, un año tiene unas 3100 horas de noche astronómica según el modelo.
- **La causa.** La integral y la derivada son operaciones inversas: el área bajo una curva crece al ritmo que marca la propia curva. Derivando la posición sale la velocidad, e integrando la velocidad sale la posición.
- **Las herramientas.** Sumas de rectángulos y de trapecios, la integral definida y su notación, el teorema fundamental del cálculo y su razón de ser, las primitivas de las potencias, y el uso de la integral numérica para acumular una magnitud que cambia día a día.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [1.2 La integral definida, *Cálculo* vol. 2 (OpenStax)](https://openstax.org/books/c%C3%A1lculo-volumen-2/pages/1-2-la-integral-definida). Español, nivel universitario; explica el área bajo la curva y la integral definida con ejemplos de velocidad. Verificado el 31 de octubre de 2026.
2. [3Blue1Brown, Essence of calculus](https://3blue1brown.com/topics/calculus). Inglés; el capítulo sobre integración y el teorema fundamental del cálculo (capítulo 8) es el complemento visual. Visto en una búsqueda con ese contenido; no lo he abierto directamente. **(Sin verificar)**.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
