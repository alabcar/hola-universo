---
title: "Semana 11 · ¿Cuánto se acumula con el tiempo?"
description: "Fase 1 · Principios básicos de astronomía. Integral como área bajo la curva, distancia recorrida y horas de noche astronómica."
sidebar:
  order: 11
  label: "11. ¿Cuánto se acumula con el tiempo?"
---

## La pregunta del cielo

La derivada responde a «¿a qué ritmo cambia esto ahora?». La pregunta inversa es: si conozco el ritmo en cada instante, ¿cuánto se ha acumulado en total? A partir de la velocidad en cada momento, ¿qué distancia he recorrido? A partir de las horas de oscuridad de cada noche, ¿cuántas horas oscuras tiene un año?

Esta semana aprendes la **integral**, la operación inversa de la derivada, con la imagen del área bajo una curva. Y la aplicas a un problema para el aficionado a la astronomía: cuántas horas de noche realmente oscura hay en un año, y cómo cambian con la latitud.

## Las cinco sesiones

### Sesión 1 · Matemáticas: el área bajo una curva (30-40 min)

Si un coche va a 50 km/h durante 3 horas, recorre $50 \cdot 3 = 150$ km, que es el **área del rectángulo** de base 3 h y altura 50 km/h en la gráfica de velocidad frente a tiempo. Esa idea sigue valiendo cuando la velocidad cambia: la distancia es el área entre la gráfica de $v(t)$ y el eje horizontal. Para áreas de formas conocidas basta geometría (rectángulo, triángulo, trapecio); para curvas hay que **aproximar**: cortar en tiras y sumar las áreas. Cuantas más tiras, mejor sale.

Esa suma es una **suma de Riemann**, y su límite cuando las tiras se hacen infinitamente delgadas es la **integral definida**, que se escribe $\int_a^b f(x)\,dx$.

**Ejercicios**

1. Un cuerpo acelera de 0 a 20 m/s en 10 s de forma lineal. ¿Qué distancia recorre?
2. Otro pasa de 10 a 30 m/s en 10 s de forma lineal. ¿Y este?
3. Aproxima el área bajo $y = x^2$ entre 0 y 3 con tres rectángulos de ancho 1, usando la altura en el extremo izquierdo y en el derecho. ¿Cuál es la media?
4. ¿Qué área hay bajo $y = 4$ entre $x=1$ y $x=6$?

<details>
<summary>Soluciones</summary>

1. Triángulo de base 10 y altura 20: $\tfrac{1}{2}\cdot 10 \cdot 20 =$ **100 m**.
2. Trapecio: $\tfrac{10+30}{2}\cdot 10 =$ **200 m**.
3. Izquierdo: $0 + 1 + 4 =$ **5**; derecho: $1 + 4 + 9 =$ **14**; media: **9,5**. El valor exacto es 9: con más tiras el error baja.
4. Rectángulo de base 5 y altura 4: **20**.

</details>

### Sesión 2 · Matemáticas: la integral y la derivada (30-40 min)

Calcular áreas con tiras es costoso. La clave es que **integrar es lo contrario de derivar**: si $F'(x) = f(x)$, entonces

$$\int_a^b f(x)\,dx = F(b) - F(a).$$

Es el **teorema fundamental del cálculo**. Como ya sabes que la derivada de $x^n$ es $n x^{n-1}$, la integral de $x^n$ es $x^{n+1}/(n+1)$. Por ejemplo, $\int_0^3 x^2\,dx = 3^3/3 - 0 = 9$, el valor al que se acercaban las sumas de rectángulos de la sesión 1. Y con el movimiento de caída: si $v = g\,t$, la distancia es $\int_0^t g\,t'\,dt' = \tfrac{1}{2} g t^2$, el resultado de la semana 8.

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
4. $F(t) = 3t^2 - 4t$: $F(2) - F(0) = 12 - 8 =$ **4 m**.

</details>

### Sesión 3 · Física: acumular magnitudes (30-40 min)

La integral aparece cada vez que una cantidad se acumula a un ritmo que cambia:

- **Posición** = integral de la velocidad: $x(t) = x_0 + \int v\,dt$.
- **Velocidad** = integral de la aceleración: $v(t) = v_0 + \int a\,dt$.
- **Trabajo** = integral de la fuerza a lo largo de un recorrido: $W = \int F\,dx$. Con fuerza constante es $F\,d$. Es el puente hacia la energía de la semana 12.

**Crepúsculos y noche.** Un lugar está de día mientras el Sol está sobre el horizonte. Pero el cielo no se oscurece de golpe: el **crepúsculo civil** acaba cuando el Sol está 6° bajo el horizonte, el **náutico** a 12° y el **astronómico** a 18°. Solo entonces el cielo está completamente oscuro y se pueden ver los objetos más débiles. Desde una latitud $\varphi$ y con la declinación del Sol $\delta$ de la semana 1, la altura del Sol en su punto más bajo (a medianoche solar) es $\varphi + \delta - 90^\circ$, y llega a bajar de −18° solo si $\varphi + \delta < 72^\circ$. Si $\varphi + \delta \ge 72^\circ$, no hay noche astronómica: en junio ($\delta = 23{,}4^\circ$) eso ocurre en latitudes superiores a unos $48{,}6^\circ$ N.

El número de horas de noche astronómica de cada día varía con las estaciones. La suma de esas horas a lo largo del año es una integral: el área bajo la curva diaria. El cuaderno la calcula: a 40° de latitud son unas 3100 horas de noche astronómica al año, el 35 % del total, y esa cifra disminuye al subir de latitud (unas 3460 h en el ecuador y unas 1900 h a 70°).

**Qué hacer**

1. Con la fórmula de la sesión 3, comprueba que a 55° N el Sol no baja de −18° el 21 de junio.
2. Explica por qué en una ciudad con mucha luz casi nunca llegas a ver el cielo de «noche astronómica».

### Sesión 4 · Astronomía y observación (30-45 min)

**Los crepúsculos en Stellarium.**

1. Fija tu lugar y tu fecha.
2. Avanza el tiempo desde el ocaso del Sol y anota la hora a la que la altura del Sol es −6°, −12° y −18°.
3. Calcula la duración de cada fase del crepúsculo (la diferencia entre horas consecutivas) y la duración total entre el ocaso y los −18°.
4. Compara con el modelo del cuaderno, que no incluye la refracción atmosférica.

**En el cielo.** Una tarde despejada, anota a qué hora ves salir la primera estrella (o planeta) brillante y a qué hora se apaga el brillo del cielo en el oeste. En una ciudad el crepúsculo astronómico es difícil de apreciar porque la contaminación lumínica ilumina el cielo toda la noche. Anota tus observaciones como una prueba de cómo de oscuro es tu cielo.

No mires nunca al Sol directamente.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 11:

- implementa la integral numérica por rectángulos y por trapecios y compara su error,
- calcula una distancia integrando una velocidad,
- calcula las horas de noche astronómica de cada día para tu latitud,
- integra a lo largo del año y compara el total entre latitudes.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-11.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-11.ipynb)

La fórmula de las horas de Sol por encima de una altura usa trigonometría esférica que aún no puedes demostrar: la usas como caja negra, y comprueba su resultado con Stellarium.

## Qué has aprendido

- **La respuesta.** Una cantidad acumulada es la integral del ritmo al que se acumula, y geométricamente es el área bajo la curva del ritmo. A 40° de latitud, un año tiene unas 3100 horas de noche astronómica según el modelo.
- **La causa.** La integral y la derivada son operaciones inversas: derivando la posición sale la velocidad, e integrando la velocidad sale la posición.
- **Las herramientas.** Sumas de rectángulos y de trapecios, el teorema fundamental del cálculo, y el uso de la integral numérica para acumular una magnitud que cambia día a día.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [1.2 La integral definida, *Cálculo* vol. 2 (OpenStax)](https://openstax.org/books/c%C3%A1lculo-volumen-2/pages/1-2-la-integral-definida). Español, nivel universitario; explica el área bajo la curva y la integral definida con ejemplos de velocidad. Verificado el 31 de octubre de 2026.
2. [3Blue1Brown, Essence of calculus](https://3blue1brown.com/topics/calculus). Inglés; el capítulo sobre integración y el teorema fundamental del cálculo (capítulo 8) es el complemento visual. Visto en una búsqueda con ese contenido; no lo he abierto directamente. **(Sin verificar)**.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
