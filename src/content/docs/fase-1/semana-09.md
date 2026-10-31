---
title: "Semana 9 · ¿Qué hace falta para cambiar un movimiento?"
description: "Fase 1 · Principios básicos de astronomía. Funciones cuadráticas, vectores y las tres leyes de Newton."
sidebar:
  order: 9
  label: "9. ¿Qué hace falta para cambiar un movimiento?"
---

## La pregunta del cielo

Durante casi dos mil años se creyó que mantener un movimiento exigía un esfuerzo continuo: un carro se para si dejas de empujarlo. Pero los planetas llevan miles de millones de años moviéndose sin que nada los empuje. Newton resolvió la aparente contradicción con una idea que parece simple y no lo es: **no hace falta una fuerza para mantener un movimiento, hace falta una fuerza para cambiarlo.** El carro se para porque algo lo frena (el rozamiento), no porque se le acabe el impulso.

Esta semana aprendes las tres leyes de Newton, las matemáticas que necesitas para usarlas (funciones cuadráticas y vectores) y las pruebas en una simulación de caída y de lanzamiento. Al final comprobarás un cálculo clásico que ata la caída de una piedra a la órbita de la Luna.

## Las cinco sesiones

### Sesión 1 · Matemáticas: funciones cuadráticas (30-40 min)

Una **función cuadrática** tiene la forma $y = ax^2 + bx + c$ y su gráfica es una parábola. Aparece siempre que algo se acelera de forma constante: la distancia recorrida en una caída libre es $y = \tfrac{1}{2} g t^2$. Para resolver $ax^2 + bx + c = 0$ se usa

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.$$

Puede tener dos soluciones, una o ninguna según el signo de $b^2 - 4ac$. Y el vértice de la parábola, su valor máximo o mínimo, está en $x = -b/(2a)$.

**Ejercicios**

1. Resuelve $x^2 - 5x + 6 = 0$.
2. Una piedra cae desde 20 m. ¿Cuánto tarda en llegar al suelo? ¿A qué velocidad llega? (Usa $g = 9{,}81$ m/s².)
3. Se lanza una piedra hacia arriba a 10 m/s. Su altura es $y = 10t - \tfrac{1}{2} \cdot 9{,}81\,t^2$. ¿Cuándo y a qué altura alcanza el máximo?
4. ¿Cuántas soluciones tiene $x^2 + 2x + 5 = 0$?

<details>
<summary>Soluciones</summary>

1. $x = (5 \pm \sqrt{25 - 24})/2$, es decir, **$x = 2$ y $x = 3$**.
2. $t = \sqrt{2 \cdot 20/9{,}81} \approx$ **2,02 s**, y $v = g\,t \approx$ **19,8 m/s** (unos 71 km/h).
3. El vértice está en $t = -b/(2a) = 10/9{,}81 \approx$ **1,02 s**, y la altura es $10 \cdot 1{,}02 - 4{,}905 \cdot 1{,}02^2 \approx$ **5,10 m**.
4. $b^2 - 4ac = 4 - 20 < 0$: **ninguna** solución real.

</details>

### Sesión 2 · Matemáticas: vectores (30-40 min)

Una **magnitud escalar** se describe con un número (la masa, el tiempo). Una **magnitud vectorial** necesita un módulo y una dirección: la velocidad, la fuerza, la aceleración. En el plano, un vector se escribe con sus dos **componentes**, $(v_x, v_y)$: cuánto vale a lo largo de cada eje. De un vector de módulo $v$ y ángulo $\theta$ sobre el eje horizontal:

$$v_x = v\cos\theta, \qquad v_y = v\sin\theta, \qquad v = \sqrt{v_x^2 + v_y^2}.$$

Los vectores se **suman componente a componente**: $(a_x, a_y) + (b_x, b_y) = (a_x + b_x,\ a_y + b_y)$. Y se multiplican por un número multiplicando cada componente.

**Ejercicios**

1. Suma $(3, 4)$ y $(1, -2)$. ¿Cuánto vale el módulo de $(3, 4)$?
2. Una fuerza de 10 N forma un ángulo de 30° con el suelo. ¿Cuánto valen sus componentes horizontal y vertical?
3. Dos fuerzas perpendiculares de 3 N y 4 N actúan sobre un cuerpo. ¿Cuánto vale la fuerza total?
4. Un balón se lanza a 20 m/s con un ángulo de 60°. ¿Cuáles son las componentes de su velocidad inicial?

<details>
<summary>Soluciones</summary>

1. $(3,4)+(1,-2) =$ **(4, 2)**, y $|(3,4)| = \sqrt{9+16} =$ **5**.
2. $F_x = 10\cos 30^\circ \approx$ **8,66 N** y $F_y = 10\sin 30^\circ =$ **5 N**.
3. $\sqrt{3^2 + 4^2} =$ **5 N**.
4. $v_x = 20\cos 60^\circ =$ **10 m/s** y $v_y = 20\sin 60^\circ \approx$ **17,3 m/s**.

</details>

### Sesión 3 · Física: las tres leyes de Newton (30-40 min)

**Primera ley (inercia).** Si la fuerza neta sobre un cuerpo es cero, su velocidad no cambia: si estaba en reposo, sigue en reposo; si se movía, sigue en línea recta a velocidad constante. Todo cambio de velocidad, ya sea de módulo o de dirección, necesita una causa.

**Segunda ley.** La fuerza neta sobre un cuerpo es igual a su masa por su aceleración:

$$\vec{F} = m\,\vec{a}.$$

Es una relación entre vectores: la aceleración tiene la dirección de la fuerza. La unidad de fuerza es el **newton**: $1\ \text{N} = 1\ \text{kg}\cdot\text{m/s}^2$. A mayor masa, menos se acelera un cuerpo con la misma fuerza.

**Tercera ley (acción y reacción).** Si un cuerpo A ejerce una fuerza sobre B, B ejerce sobre A una fuerza igual en módulo y de sentido contrario: $\vec{F}_{AB} = -\vec{F}_{BA}$. Actúan sobre cuerpos distintos, por eso no se anulan entre sí.

**Masa y peso.** La masa mide la cantidad de materia (y la inercia); el peso es la fuerza con la que un astro atrae un cuerpo: $W = m\,g$. Tu masa es la misma en la Luna y en la Tierra; tu peso no.

**Aplicado al cielo.** El Sistema Solar no necesita motores. Un planeta lleva su velocidad desde que se formó y la sigue conservando; lo que cambia su dirección a cada instante es la **fuerza gravitatoria** del Sol (fase 2). Newton comprobó incluso que la fuerza que hace caer una manzana y la que mantiene a la Luna en su órbita son la misma: la aceleración que necesita la Luna para describir su órbita ($v^2/r$) coincide, con un 1 % de error, con la de la gravedad terrestre debilitada con el cuadrado de la distancia. El cuaderno lo calcula.

**Qué hacer**

1. Explica con tus palabras por qué un astronauta que suelta un objeto en el espacio exterior, lejos de cualquier astro, lo ve moverse en línea recta a velocidad constante.
2. En una colisión entre una persona y un camión, ¿cómo comparan las fuerzas que se ejercen? ¿Y las aceleraciones?

### Sesión 4 · Astronomía y observación (30-45 min)

**Sigue un planeta durante varias semanas.** En Stellarium, busca un planeta que sea visible a simple vista en las próximas semanas (los planetas brillantes son fáciles de ver incluso desde una ciudad con mucha luz) y anota su posición respecto a las estrellas de fondo cada semana: dibuja las estrellas cercanas y marca el planeta con la fecha. Verás que se mueve despacio sobre el fondo de estrellas, sin que nada lo empuje, cumpliendo la primera ley. En la semana 13 explicarás por qué a veces parece ir hacia atrás.

**Observación de la inercia en casa.** Pon una moneda sobre una tarjeta encima de un vaso y tira de la tarjeta con un golpe seco. Explica el resultado con las leyes de Newton.

No mires nunca al Sol directamente.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 9:

- simula una caída libre con el método de Euler y mide cómo cambia el error al reducir el paso,
- resuelve un lanzamiento descomponiendo la velocidad en sus componentes,
- dibuja trayectorias con distintos ángulos y comprueba que 45° da el mayor alcance,
- repite el cálculo de Newton para la Luna y la caída de una piedra.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-09.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-09.ipynb)

## Qué has aprendido

- **La respuesta.** Para cambiar un movimiento hace falta una fuerza neta, y el cambio es proporcional a ella e inversamente proporcional a la masa: $\vec{F} = m\vec{a}$. Sin fuerza, el movimiento continúa en línea recta a velocidad constante.
- **La causa.** Los cuerpos tienen inercia, y los frenos de la vida diaria (rozamiento, resistencia del aire) ocultan esa propiedad.
- **Las herramientas.** Funciones cuadráticas y la fórmula para resolverlas, vectores con sus componentes y su suma, y el método de Euler con la dependencia del error con el paso.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 5.3, Segunda ley de Newton, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/5-3-segunda-ley-de-newton). Español, nivel universitario con cálculo; la segunda ley con ejemplos. Verificado el 31 de octubre de 2026.
2. [Resumen del capítulo 5, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/5-resumen). Español; resume las tres leyes, masa y peso. Visto en una búsqueda con ese contenido; no lo he abierto directamente. **(Sin verificar)**.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
