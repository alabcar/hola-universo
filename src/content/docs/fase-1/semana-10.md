---
title: "Semana 10 · ¿Qué velocidad lleva algo en un instante concreto?"
description: "Fase 1 · Principios básicos de astronomía. Pendiente, límite y derivada como velocidad instantánea."
sidebar:
  order: 10
  label: "10. ¿Qué velocidad lleva algo en un instante concreto?"
---

## La pregunta del cielo

El velocímetro de un coche marca una velocidad *ahora*. Pero la velocidad es una distancia dividida entre un tiempo, y en un instante no pasa tiempo ni se recorre distancia: sale $0/0$. ¿Cómo puede tener sentido? Es la paradoja que se resolvió con la idea central del cálculo, y que Newton necesitaba para describir las órbitas, donde la velocidad cambia constantemente.

Esta semana aprendes qué es una derivada, con una imagen (la pendiente de una curva) y con números (la velocidad media en intervalos cada vez más pequeños), y la usas en el cielo: ¿a qué ritmo se mueve el Sol hacia el norte y el sur a lo largo del año?

## Las cinco sesiones

### Sesión 1 · Matemáticas: pendiente, secante y tangente (30-40 min)

La **pendiente** de una recta es lo que sube cuando avanzas una unidad: $m = \Delta y/\Delta x$. Para una curva, la pendiente cambia de un punto a otro. Entre dos puntos de la curva puedes trazar la recta que los une, la **secante**, y calcular su pendiente. Si acercas un punto al otro, la secante gira y se acerca a una recta que solo toca la curva en ese punto, la **tangente**. La pendiente de la tangente es lo que llamamos la **derivada** en el punto.

Con la posición de una piedra que cae, $s(t) = 4{,}9\,t^2$ metros, la pendiente de la secante entre $t=1$ y $t = 1 + h$ es la velocidad media en ese intervalo:

$$\frac{s(1+h) - s(1)}{h} = \frac{4{,}9\,(1+h)^2 - 4{,}9}{h} = 4{,}9\,(2 + h) = 9{,}8 + 4{,}9\,h.$$

Cuando $h$ se acerca a cero, esa expresión se acerca a 9,8. Se dice que el **límite** es 9,8, y es la **velocidad instantánea** en $t = 1$. Nunca hay que dividir por cero: se simplifica antes y se observa a qué valor tiende lo que queda.

**Ejercicios**

1. Calcula $9{,}8 + 4{,}9\,h$ para $h = 1$, $0{,}1$ y $0{,}01$.
2. Una función tiene $f(2) = 5$ y $f(3) = 11$. ¿Cuál es la pendiente de la secante entre esos puntos?
3. Para $f(x) = x^2$, calcula la pendiente de la secante entre $x = 3$ y $x = 3 + h$, y deduce la pendiente de la tangente en $x = 3$.

<details>
<summary>Soluciones</summary>

1. **14,7**, **10,29** y **9,849** m/s.
2. $(11-5)/(3-2) =$ **6**.
3. $\dfrac{(3+h)^2 - 9}{h} = \dfrac{6h + h^2}{h} = 6 + h$, que tiende a **6** cuando $h \to 0$.

</details>

### Sesión 2 · Matemáticas: derivadas de funciones sencillas (30-40 min)

El proceso de la sesión 1 se puede generalizar. Para $f(x) = x^2$, la secante entre $x$ y $x+h$ tiene pendiente $(2x\,h + h^2)/h = 2x + h$, que tiende a $2x$. Se escribe $f'(x) = 2x$. Hay una regla general para potencias: la derivada de $x^n$ es $n\,x^{n-1}$. Y dos propiedades que la completan:

- la derivada de una suma es la suma de las derivadas,
- la derivada de un número por una función es ese número por la derivada.

| $f(x)$ | $c$ (constante) | $x$ | $x^2$ | $x^3$ |
|---|---|---|---|---|
| $f'(x)$ | 0 | 1 | $2x$ | $3x^2$ |

La derivada de una constante es 0 porque no cambia. Aplicado a una caída libre: de $s = \tfrac{1}{2}\,g\,t^2$ sale $v = s' = g\,t$, y derivando otra vez, la aceleración $a = v' = g$.

**Ejercicios**

1. Deriva $5x^2$, $3x^3 - 2x$ y $x^2 + 4x - 7$.
2. Un cuerpo tiene posición $x(t) = 3t^2 - 4t + 1$. ¿Cuánto valen su velocidad y su aceleración en $t = 2$?
3. ¿Para qué valor de $x$ se anula la derivada de $x^2 - 6x + 5$? ¿Qué punto de la parábola es?

<details>
<summary>Soluciones</summary>

1. $10x$; $9x^2 - 2$; $2x + 4$.
2. $v(t) = 6t - 4$, luego $v(2) =$ **8**; $a(t) = 6$, es decir, **6** (constante).
3. $2x - 6 = 0$ cuando $x = $ **3**: es el **vértice**, el mínimo de la parábola. Donde la derivada se anula, la función se detiene para dar la vuelta.

</details>

### Sesión 3 · Física: velocidad instantánea (30-40 min)

La **velocidad instantánea** es la derivada de la posición respecto al tiempo, y la **aceleración instantánea** es la derivada de la velocidad:

$$v = \frac{dx}{dt}, \qquad a = \frac{dv}{dt} = \frac{d^2x}{dt^2}.$$

Todas las medidas de velocidad que has hecho hasta ahora eran medias, promediadas sobre un intervalo. Un velocímetro hace el mismo truco: mide cuánto avanza la rueda en un intervalo muy corto y divide. En una órbita, la velocidad cambia continuamente de dirección, y por eso no se puede describir una órbita sin esta herramienta.

**Cuándo la derivada es cero.** En un máximo o un mínimo de una función, la tangente es horizontal y la derivada vale cero. En la declinación del Sol (semana 1), eso ocurre en los solsticios: durante unos días la declinación apenas cambia, y de ahí viene el nombre (*solsticio*, «Sol quieto»). El ritmo máximo, en los equinoccios, es de unos 0,4° al día.

**En el cielo.** La Luna avanza respecto a las estrellas unos 13,2° al día de media (360°/27,32 días), pero su velocidad real no es constante: es mayor cerca del perigeo y menor cerca del apogeo, porque la órbita es elíptica (semana 14).

**Qué hacer**

1. Dibuja a mano la posición de la piedra, $s = 4{,}9\,t^2$, entre $t=0$ y $t=3$, y traza con regla las tangentes en $t = 1$ y $t = 2$. Mide sus pendientes y compáralas con 9,8 y 19,6.
2. Explica por escrito qué significa que la velocidad instantánea sea cero y la aceleración no lo sea (por ejemplo, la piedra lanzada hacia arriba en el punto más alto).

### Sesión 4 · Astronomía y observación (30-45 min)

**La Luna entre noches.** Si hay Luna visible, mide con la mano (semana 2) su separación respecto a una estrella cercana, y repite la medida a la misma hora una noche después. El desplazamiento será de unos 13° respecto a las estrellas (más de un puño). Eso es una velocidad media de un día.

**Cada vez más cerca del instante, en Stellarium.**

1. Elige una fecha y la Luna. Anota su ascensión recta.
2. Avanza el tiempo 1 día, 1 hora, 10 minutos y 1 minuto, y anota cuánto cambia la ascensión recta en cada caso.
3. Calcula la velocidad media en cada intervalo (cambio de AR entre el tiempo transcurrido) y comprueba que los valores convergen. Esa es la velocidad instantánea de la Luna.

**Los solsticios.** Si mides el punto de salida del Sol cada semana contra una referencia del paisaje, verás que al acercarse el solsticio de diciembre su desplazamiento semanal se reduce: la derivada se acerca a cero.

No mires nunca al Sol directamente.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 10:

- calcula la velocidad media de una piedra en intervalos cada vez más pequeños y observa el límite,
- implementa una función que calcula la derivada numérica de cualquier función,
- estudia cómo depende el error del paso $h$, con sus límites en la precisión del ordenador,
- aplica la derivada a la declinación del Sol y dibuja su ritmo diario durante un año.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-10.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-10.ipynb)

## Qué has aprendido

- **La respuesta.** La velocidad instantánea es el límite de la velocidad media cuando el intervalo tiende a cero. Es la derivada de la posición respecto al tiempo, y geométricamente la pendiente de la tangente.
- **La causa.** Aunque en un instante no se recorra distancia, la velocidad media sobre intervalos cada vez más pequeños se acerca a un valor concreto, y ese valor es lo que mide un velocímetro.
- **Las herramientas.** Pendiente, secante y tangente; el límite como valor al que se acerca una expresión; las derivadas de potencias; y la derivada numérica con su error.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [3.1 Definir la derivada, *Cálculo* vol. 1 (OpenStax)](https://openstax.org/books/c%C3%A1lculo-volumen-1/pages/3-1-definir-la-derivada). Español, nivel universitario; define la derivada como límite y distingue velocidad media e instantánea. Verificado el 31 de octubre de 2026.
2. [The paradox of the derivative, capítulo 2 de *Essence of calculus*, 3Blue1Brown](https://3blue1brown.com/lessons/derivatives). Inglés, lección con texto y vídeo, explica con imágenes la idea de velocidad instantánea. No he podido confirmar si hay subtítulos en español. Verificado el 31 de octubre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
