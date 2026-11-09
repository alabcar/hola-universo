---
title: "Semana 10 · ¿Qué velocidad lleva algo en un instante concreto?"
description: "Fase 1 · Principios básicos de astronomía. Pendiente, secante y tangente, el límite, la derivada y sus reglas, y la velocidad instantánea."
sidebar:
  order: 10
  label: "10. ¿Qué velocidad lleva algo en un instante concreto?"
---

## La pregunta del cielo

El velocímetro de un coche marca una velocidad *ahora*. Pero la velocidad es una distancia dividida entre un tiempo, y en un instante no pasa tiempo ni se recorre distancia: sale $0/0$. ¿Cómo puede tener sentido? El filósofo griego Zenón de Elea ya planteó el problema en el siglo V a. C. con su paradoja de la flecha: en cada instante, una flecha en vuelo ocupa un lugar fijo, igual a su tamaño, así que en ese instante está quieta; y si está quieta en todos los instantes, ¿cuándo se mueve?

La respuesta llegó más de dos mil años después, con la idea central del **cálculo**, que Newton y Leibniz desarrollaron de forma independiente en la segunda mitad del siglo XVII (y que les llevó a una larga disputa sobre quién lo había inventado primero). Newton lo necesitaba para describir las órbitas, donde la velocidad cambia en cada instante.

Esta semana aprendes qué es una derivada, con una imagen (la pendiente de una curva) y con números (la velocidad media en intervalos cada vez más pequeños), y la usas en el cielo: ¿a qué ritmo se mueve el Sol hacia el norte y el sur a lo largo del año?

:::note[De dónde viene la palabra]
**Cálculo** viene del latín *calculus*, «piedrecita», diminutivo de *calx*, «piedra caliza». Los romanos contaban con piedrecitas sobre un tablero o un ábaco, y *calculare* pasó a significar «contar». La misma palabra se usa en medicina para las piedras del riñón. Al cálculo de Newton y Leibniz se le llamó durante mucho tiempo **cálculo infinitesimal**, porque trabaja con cantidades «infinitamente pequeñas».
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: pendiente, secante, tangente y límite (40-45 min)

**La pendiente de una recta**, como viste en la semana 4, es lo que sube cuando avanzas una unidad: $m = \Delta y/\Delta x$. Una recta tiene la misma pendiente en todos sus puntos. Una curva, no: la parábola de una piedra que cae empieza casi plana y se va empinando. ¿Qué significa la pendiente de una curva en un punto?

**La secante.** Elige dos puntos de la curva y traza la recta que los une: es una **secante**. Su pendiente se calcula como la de cualquier recta, y es la pendiente media de la curva entre esos dos puntos. Si la curva es la posición de un cuerpo frente al tiempo, la pendiente de la secante es la **velocidad media** entre los dos instantes.

**La tangente.** Ahora deja fijo el primer punto y acerca el segundo cada vez más. La secante gira y se acerca a una recta que solo roza la curva en ese punto: la **tangente**. Su pendiente es la pendiente de la curva en el punto, y se llama **derivada**.

**Con números.** La posición de una piedra que cae es $s(t) = 4{,}9\,t^2$ metros (es $\tfrac{1}{2} g t^2$ con $g = 9{,}8$ m/s²). La pendiente de la secante entre $t = 1$ y $t = 1 + h$, donde $h$ es un intervalo de tiempo pequeño, es la velocidad media en ese intervalo:

$$\frac{s(1+h) - s(1)}{h} = \frac{4{,}9\,(1+h)^2 - 4{,}9}{h} = \frac{4{,}9\,(1 + 2h + h^2) - 4{,}9}{h} = \frac{4{,}9\,(2h + h^2)}{h} = 4{,}9\,(2 + h).$$

En el último paso se ha dividido entre $h$, cosa que se puede hacer mientras $h$ no sea cero. El resultado, $9{,}8 + 4{,}9\,h$, tiene sentido para cualquier $h$, y cuando $h$ se hace cada vez más pequeño se acerca a 9,8: con $h = 0{,}1$ da 10,29; con $h = 0{,}01$, 9,849; con $h = 0{,}001$, 9,8049.

**El límite.** Se dice que el **límite** de esa expresión, cuando $h$ tiende a cero, es 9,8, y se escribe $\lim_{h \to 0}$. Es el valor al que se acerca tanto como quieras haciendo $h$ suficientemente pequeño. Esa es la **velocidad instantánea** en $t = 1$: 9,8 m/s. Así se resuelve la paradoja: nunca se divide por cero. Se calcula la velocidad media en un intervalo, se simplifica, y se observa a qué valor tiende cuando el intervalo se encoge. Un instante no tiene velocidad «por sí solo»; la tiene como límite de lo que pasa a su alrededor.

:::note[De dónde viene la palabra]
**Límite** viene del latín *limes, limitis*, «sendero que separa dos campos, frontera». En las fronteras del Imperio romano se llamaba *limes* a la línea fortificada. **Secante** viene de *secare*, «cortar» (como *sección* o *segmento*): la recta que corta la curva en dos puntos. La **tangente**, como viste en la semana 6, es «la que toca».
:::

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

### Sesión 2 · Matemáticas: derivadas de funciones sencillas (40-45 min)

**La derivada como función.** El proceso de la sesión 1 se puede hacer en cualquier punto $x$, no solo en $x = 3$. Para $f(x) = x^2$, la secante entre $x$ y $x+h$ tiene pendiente

$$\frac{(x+h)^2 - x^2}{h} = \frac{x^2 + 2xh + h^2 - x^2}{h} = 2x + h,$$

que tiende a $2x$. El resultado es otra función, que da la pendiente en cada punto: la **función derivada**. Se escribe $f'(x) = 2x$ (se lee «efe prima de equis»). En $x = 3$, la pendiente es 6, como en el ejercicio anterior; en $x = 0$, es 0 (la parábola está plana en el fondo); en $x = -1$, es $-2$ (baja).

**Lo mismo con $x^3$.** Primero hay que desarrollar $(x + h)^3 = (x+h)(x+h)(x+h) = x^3 + 3x^2h + 3xh^2 + h^3$. Entonces la pendiente de la secante es

$$\frac{(x+h)^3 - x^3}{h} = \frac{3x^2h + 3xh^2 + h^3}{h} = 3x^2 + 3xh + h^2,$$

y cuando $h$ tiende a cero, todos los términos con $h$ desaparecen: queda $3x^2$.

**La regla de las potencias.** El patrón se repite: la derivada de $x^2$ es $2x$, la de $x^3$ es $3x^2$, y en general la derivada de $x^n$ es $n\,x^{n-1}$. El exponente baja a multiplicar y se le resta uno. Y dos propiedades la completan, que puedes comprobar con el mismo método:

- la derivada de una suma es la suma de las derivadas;
- la derivada de un número por una función es ese número por la derivada (si una función es el triple de otra, su pendiente también es el triple).

| $f(x)$ | $c$ (constante) | $x$ | $x^2$ | $x^3$ |
|---|---|---|---|---|
| $f'(x)$ | 0 | 1 | $2x$ | $3x^2$ |

La derivada de una constante es 0 porque no cambia: su gráfica es una recta horizontal. La de $x$ es 1 porque su gráfica es una recta de pendiente 1. Aplicado a una caída libre: de $s = \tfrac{1}{2}\,g\,t^2$ sale $v = s' = \tfrac{1}{2}\,g \cdot 2t = g\,t$, y derivando otra vez, la aceleración $a = v' = g$. Las fórmulas de la semana 8 salen ahora de una sola regla.

**Dos notaciones.** La notación $f'(x)$ es de Lagrange, de finales del siglo XVIII. Leibniz escribía la derivada de $y$ respecto a $x$ como $\dfrac{dy}{dx}$, donde $dy$ y $dx$ representan cambios infinitamente pequeños de $y$ y de $x$: recuerda que es un cociente de cambios, el límite de $\Delta y/\Delta x$. En física se usan las dos.

:::note[De dónde viene la palabra]
**Derivada** viene del latín *derivare*, «desviar el agua de un río, sacar un canal», de *de*, «desde», y *rivus*, «arroyo». Una función derivada «sale» de otra como un canal sale de un río. Lagrange le dio este nombre en 1797. Newton, en cambio, llamaba a las derivadas **fluxiones**, de *fluxio*, «flujo»: imaginaba las magnitudes fluyendo con el tiempo.
:::

**Ejercicios**

1. Deriva $5x^2$, $3x^3 - 2x$ y $x^2 + 4x - 7$.
2. Un cuerpo tiene posición $x(t) = 3t^2 - 4t + 1$. ¿Cuánto valen su velocidad y su aceleración en $t = 2$?
3. ¿Para qué valor de $x$ se anula la derivada de $x^2 - 6x + 5$? ¿Qué punto de la parábola es?

<details>
<summary>Soluciones</summary>

1. $10x$; $9x^2 - 2$; $2x + 4$.
2. $v(t) = 6t - 4$, luego $v(2) =$ **8**; $a(t) = 6$, es decir, **6** (constante).
3. $2x - 6 = 0$ cuando $x = $ **3**: es el **vértice**, el mínimo de la parábola. Coincide con la fórmula $x = -b/(2a) = 6/2$ de la semana 9. Donde la derivada se anula, la función se detiene para dar la vuelta.

</details>

### Sesión 3 · Física: velocidad instantánea (35-40 min)

**Las definiciones.** La **velocidad instantánea** es la derivada de la posición respecto al tiempo, y la **aceleración instantánea** es la derivada de la velocidad:

$$v = \frac{dx}{dt}, \qquad a = \frac{dv}{dt} = \frac{d^2x}{dt^2}.$$

La notación $\dfrac{d^2x}{dt^2}$ se lee «derivada segunda de $x$ respecto a $t$»: derivar dos veces. Todas las medidas de velocidad que has hecho hasta ahora eran medias, promediadas sobre un intervalo. Un velocímetro hace el mismo truco que la sesión 1: mide cuánto avanza la rueda en un intervalo muy corto y divide. En una órbita, la velocidad cambia continuamente de dirección, y por eso no se puede describir una órbita sin esta herramienta.

**Cuándo la derivada es cero.** En un máximo o un mínimo de una función, la tangente es horizontal y la derivada vale cero. En la declinación del Sol (semana 1), eso ocurre en los solsticios: durante unos días la declinación apenas cambia, y de ahí viene el nombre (*solsticio*, «Sol quieto»). En cambio, en los equinoccios la declinación pasa por cero con la pendiente máxima: el Sol se desplaza hacia el norte o hacia el sur unos 0,4° al día, casi su propio diámetro. Por eso la duración del día cambia muy deprisa en marzo y en septiembre, y casi nada en junio y en diciembre.

**En el cielo.** La Luna avanza respecto a las estrellas unos 13,2° al día de media (360°/27,32 días), pero su velocidad real no es constante: es mayor cerca del perigeo y menor cerca del apogeo, porque la órbita es elíptica (semana 14). Una velocidad media no basta para describirla: hace falta la instantánea.

**Qué hacer**

1. Dibuja a mano la posición de la piedra, $s = 4{,}9\,t^2$, entre $t=0$ y $t=3$, y traza con regla las tangentes en $t = 1$ y $t = 2$. Mide sus pendientes y compáralas con 9,8 y 19,6.
2. Explica por escrito qué significa que la velocidad instantánea sea cero y la aceleración no lo sea (por ejemplo, la piedra lanzada hacia arriba en el punto más alto).

### Sesión 4 · Astronomía y observación (30-45 min)

**La Luna entre noches.** Si hay Luna visible, mide con la mano (semana 2) su separación respecto a una estrella cercana, y repite la medida a la misma hora una noche después. El desplazamiento será de unos 13° respecto a las estrellas (más de un puño). Eso es una velocidad media de un día.

**Cada vez más cerca del instante, en Stellarium.**

1. Elige una fecha y la Luna. Anota su ascensión recta.
2. Avanza el tiempo 1 día, 1 hora, 10 minutos y 1 minuto, y anota cuánto cambia la ascensión recta en cada caso.
3. Calcula la velocidad media en cada intervalo (cambio de AR entre el tiempo transcurrido) y comprueba que los valores convergen, es decir, que se acercan a un valor fijo. Esa es la velocidad instantánea de la Luna.

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
- **La causa.** Aunque en un instante no se recorra distancia, la velocidad media sobre intervalos cada vez más pequeños se acerca a un valor concreto, y ese valor es lo que mide un velocímetro. Así se resuelve la paradoja de Zenón.
- **Las herramientas.** Pendiente, secante y tangente; el límite como valor al que se acerca una expresión; la derivada como función; la regla de las potencias deducida para $x^2$ y $x^3$; las notaciones $f'$ y $dy/dx$; y la derivada numérica con su error.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [3.1 Definir la derivada, *Cálculo* vol. 1 (OpenStax)](https://openstax.org/books/c%C3%A1lculo-volumen-1/pages/3-1-definir-la-derivada). Español, nivel universitario; define la derivada como límite y distingue velocidad media e instantánea. Verificado el 31 de octubre de 2026.
2. [The paradox of the derivative, capítulo 2 de *Essence of calculus*, 3Blue1Brown](https://3blue1brown.com/lessons/derivatives). Inglés, lección con texto y vídeo, explica con imágenes la idea de velocidad instantánea. No he podido confirmar si hay subtítulos en español. Verificado el 31 de octubre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
