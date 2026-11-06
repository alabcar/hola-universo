---
title: "Semana 9 · ¿Qué hace falta para cambiar un movimiento?"
description: "Fase 1 · Principios básicos de astronomía. Funciones cuadráticas y la fórmula para resolverlas, vectores y las tres leyes de Newton."
sidebar:
  order: 9
  label: "9. ¿Qué hace falta para cambiar un movimiento?"
---

## La pregunta del cielo

Durante casi dos mil años se creyó que mantener un movimiento exigía un esfuerzo continuo: un carro se para si dejas de empujarlo. Era la física de Aristóteles, y encajaba con la experiencia diaria. Pero los planetas llevan miles de millones de años moviéndose sin que nada los empuje. Galileo, a principios del siglo XVII, empezó a sospechar que el sentido común se equivocaba, y Newton resolvió la contradicción en 1687, en sus *Principios matemáticos de la filosofía natural*, con una idea que parece simple y no lo es: **no hace falta una fuerza para mantener un movimiento, hace falta una fuerza para cambiarlo.** El carro se para porque algo lo frena (el rozamiento), no porque se le acabe el impulso.

Esta semana aprendes las tres leyes de Newton, las matemáticas que necesitas para usarlas (funciones cuadráticas y vectores) y las pruebas en una simulación de caída y de lanzamiento. Al final comprobarás un cálculo clásico que ata la caída de una piedra a la órbita de la Luna.

## Las cinco sesiones

### Sesión 1 · Matemáticas: funciones cuadráticas (40-45 min)

**Qué es.** Una **función cuadrática** es una función en la que la variable aparece elevada al cuadrado:

$$y = ax^2 + bx + c,$$

con $a$ distinto de cero (si $a$ fuera cero, sería la función lineal de la semana 4). Su gráfica es una curva llamada **parábola**: con forma de U si $a$ es positivo, y de U invertida si es negativo. El nombre lo explicaremos en la semana 14, cuando aparezca junto a la elipse y la hipérbola.

**Por qué importa aquí.** Aparece siempre que algo se acelera de forma constante. En la semana 8 viste que, con aceleración constante, la posición es $x = x_0 + v_0 t + \tfrac{1}{2} a t^2$: una función cuadrática del tiempo. La distancia recorrida en una caída libre desde el reposo es $y = \tfrac{1}{2} g t^2$, donde $g \approx 9{,}81$ m/s² es la aceleración de la gravedad. Y la trayectoria de una piedra lanzada es una parábola.

**El vértice.** La parábola tiene un punto más bajo (si $a > 0$) o más alto (si $a < 0$), el **vértice**, donde deja de bajar y empieza a subir, o al revés. Está en

$$x = -\frac{b}{2a}.$$

En un lanzamiento hacia arriba, el vértice es el punto más alto que alcanza la piedra.

**Resolver la ecuación cuadrática.** Muchas preguntas físicas acaban en encontrar los valores de $x$ que hacen $ax^2 + bx + c = 0$, por ejemplo, cuándo llega al suelo una piedra. Gráficamente, son los puntos donde la parábola corta el eje horizontal. La solución es la **fórmula general**:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.$$

El signo $\pm$ significa que hay dos soluciones posibles, una con $+$ y otra con $-$.

**De dónde sale.** No hace falta memorizarla sin entenderla. Se obtiene **completando el cuadrado**, usando que $(x + k)^2 = x^2 + 2kx + k^2$ (semana 7). Divide todo entre $a$ y pasa $c/a$ al otro lado: $x^2 + \tfrac{b}{a}x = -\tfrac{c}{a}$. El lado izquierdo es el principio de $(x + \tfrac{b}{2a})^2$; le falta el término $(\tfrac{b}{2a})^2$. Súmalo a los dos lados:

$$\left(x + \frac{b}{2a}\right)^2 = \frac{b^2}{4a^2} - \frac{c}{a} = \frac{b^2 - 4ac}{4a^2}.$$

Ahora haz la raíz cuadrada a los dos lados (con los dos signos posibles, porque tanto $3^2$ como $(-3)^2$ dan 9) y despeja $x$. Sale la fórmula.

**El discriminante.** La cantidad bajo la raíz, $b^2 - 4ac$, se llama **discriminante** y decide cuántas soluciones hay. Si es positiva, hay dos (la parábola corta el eje dos veces); si es cero, una (lo toca en el vértice); si es negativa, ninguna real, porque no existe la raíz cuadrada de un número negativo entre los números reales (la parábola no llega al eje).

:::note[De dónde viene la palabra]
**Cuadrática** viene de *quadratus*, «cuadrado», porque la variable está elevada al cuadrado. **Vértice** viene del latín *vertex*, «remolino, coronilla, cumbre», de *vertere*, «girar»: el punto donde la curva da la vuelta. **Discriminante** viene de *discriminare*, «separar, distinguir»: el número que distingue entre los tres casos.
:::

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

### Sesión 2 · Matemáticas: vectores (35-40 min)

**Escalares y vectores.** Una **magnitud escalar** se describe con un número y su unidad: la masa, el tiempo, la temperatura. Una **magnitud vectorial** necesita además una dirección: no basta con decir que empujas con 10 newtons, hay que decir hacia dónde. Son vectores la posición, la velocidad, la aceleración y la fuerza. Un vector se dibuja como una flecha: su longitud es el **módulo** (cuánto vale) y su orientación, la dirección y el sentido.

**Componentes.** Para calcular con vectores se colocan unos ejes, como en la semana 3, y cada vector se describe por cuánto avanza a lo largo de cada eje: sus **componentes**, $(v_x, v_y)$. Si conoces el módulo $v$ y el ángulo $\theta$ que forma con el eje horizontal, la flecha es la hipotenusa de un triángulo rectángulo cuyos catetos son las componentes. Con la trigonometría de la semana 7:

$$v_x = v\cos\theta, \qquad v_y = v\sin\theta, \qquad v = \sqrt{v_x^2 + v_y^2}.$$

La última fórmula es el teorema de Pitágoras.

**Sumar vectores.** Los vectores se **suman componente a componente**: $(a_x, a_y) + (b_x, b_y) = (a_x + b_x,\ a_y + b_y)$. Gráficamente, se pone el origen de la segunda flecha en la punta de la primera, y la suma va del origen de la primera a la punta de la segunda. Por eso dos fuerzas de 3 N y 4 N pueden sumar 7 N (si empujan en la misma dirección), 1 N (si empujan en sentidos opuestos) o 5 N (si son perpendiculares). Un vector se multiplica por un número multiplicando cada componente: se alarga o se acorta sin cambiar de dirección.

**Por qué importa aquí.** Cuando varias fuerzas actúan a la vez sobre un cuerpo, lo que cuenta es su suma vectorial, la **fuerza neta** o **resultante**. Y en un lanzamiento, el movimiento horizontal y el vertical se pueden estudiar por separado, cada uno con su componente: la gravedad solo afecta a la vertical.

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

En la semana 16 volverás a los vectores con más detalle, para sumar las atracciones del Sol y la Tierra sobre la Luna.

### Sesión 3 · Física: las tres leyes de Newton (40-45 min)

**Qué es una fuerza.** Una **fuerza** es un empujón o un tirón: lo que hace una mano, un muelle, un imán o la gravedad sobre un cuerpo. Es un vector, porque tiene dirección. No se ve directamente; se reconoce por su efecto: cambiar el movimiento de un cuerpo o deformarlo.

**Primera ley (inercia).** Si la fuerza neta sobre un cuerpo es cero, su velocidad no cambia: si estaba en reposo, sigue en reposo; si se movía, sigue en línea recta a velocidad constante. Todo cambio de velocidad, ya sea de rapidez o de dirección, necesita una causa.

Galileo llegó a esta idea con un experimento mental. Deja rodar una bola por una rampa: sube por otra rampa enfrente casi hasta la misma altura. Si la segunda rampa es menos inclinada, la bola recorre más camino para llegar a esa altura. Y si la segunda rampa fuera horizontal, la bola no llegaría nunca a la altura de partida: seguiría rodando para siempre, si nada la frenara. En la vida diaria siempre hay algo que frena (el rozamiento con el suelo, la resistencia del aire), y por eso la primera ley va contra la intuición.

**Segunda ley.** La fuerza neta sobre un cuerpo es igual a su masa por su aceleración:

$$\vec{F} = m\,\vec{a}.$$

Es una relación entre vectores: la aceleración tiene la misma dirección que la fuerza. Léela de dos maneras. Con la misma masa, una fuerza doble produce una aceleración doble. Con la misma fuerza, una masa doble se acelera la mitad: la **masa** mide cuánto se resiste un cuerpo a cambiar su movimiento, su inercia. Empujar un carro de la compra vacío o lleno es la diferencia. La unidad de fuerza es el **newton**: 1 N es la fuerza que da a 1 kg una aceleración de 1 m/s², es decir, $1\ \text{N} = 1\ \text{kg}\cdot\text{m/s}^2$. Una manzana pequeña pesa más o menos 1 N.

**Tercera ley (acción y reacción).** Si un cuerpo A ejerce una fuerza sobre B, B ejerce sobre A una fuerza igual en módulo y de sentido contrario: $\vec{F}_{AB} = -\vec{F}_{BA}$. Cuando caminas, empujas el suelo hacia atrás y el suelo te empuja hacia delante; un cohete empuja los gases hacia abajo y los gases empujan el cohete hacia arriba. Las dos fuerzas actúan sobre cuerpos distintos, y por eso no se anulan entre sí.

**Masa y peso.** La masa mide la cantidad de materia (y la inercia) y se mide en kilogramos; el **peso** es la fuerza con la que un astro atrae un cuerpo, y se mide en newtons: $W = m\,g$. Tu masa es la misma en la Luna y en la Tierra; tu peso no: en la Luna es unas seis veces menor. Cuando una báscula dice «70 kg», en realidad mide tu peso y lo convierte suponiendo la gravedad de la Tierra.

**Aplicado al cielo.** El Sistema Solar no necesita motores. Un planeta lleva su velocidad desde que se formó y la sigue conservando; lo que cambia su dirección a cada instante es la **fuerza gravitatoria** del Sol (fase 2). Newton comprobó incluso que la fuerza que hace caer una manzana y la que mantiene a la Luna en su órbita son la misma: la aceleración que necesita la Luna para describir su órbita ($v^2/r$, semana 8) coincide, con un 1 % de error, con la de la gravedad terrestre debilitada con el cuadrado de la distancia. El cuaderno lo calcula.

:::note[De dónde viene la palabra]
**Inercia** viene del latín *iners*, «inactivo, perezoso», de *in*, «sin», y *ars*, «habilidad, oficio»: algo que no hace nada por sí mismo. Kepler usó la palabra para la «pereza» de los cuerpos, y Newton habló de *vis inertiae*, la «fuerza de inercia». **Fuerza** viene del latín tardío *fortia*, de *fortis*, «fuerte». La unidad **newton** se adoptó oficialmente en 1948, en honor de Isaac Newton. **Kilogramo** junta el *khílioi* griego, «mil», con *grámma*, que en griego era «letra» y también una pequeña unidad de peso.
:::

**Qué hacer**

1. Explica con tus palabras por qué un astronauta que suelta un objeto en el espacio exterior, lejos de cualquier astro, lo ve moverse en línea recta a velocidad constante.
2. En una colisión entre una persona y un camión, ¿cómo comparan las fuerzas que se ejercen? ¿Y las aceleraciones?
3. Calcula tu peso en newtons en la Tierra y en la Luna ($g_\text{Luna} \approx 1{,}62$ m/s²).

### Sesión 4 · Astronomía y observación (30-45 min)

**Sigue un planeta durante varias semanas.** En Stellarium, busca un planeta que sea visible a simple vista en las próximas semanas (los planetas brillantes son fáciles de ver incluso desde una ciudad con mucha luz) y anota su posición respecto a las estrellas de fondo cada semana: dibuja las estrellas cercanas y marca el planeta con la fecha. Verás que se mueve despacio sobre el fondo de estrellas, sin que nada lo empuje hacia delante: solo la gravedad del Sol curva su camino. En la semana 13 explicarás por qué a veces parece ir hacia atrás.

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
- **La causa.** Los cuerpos tienen inercia, y los frenos de la vida diaria (rozamiento, resistencia del aire) ocultan esa propiedad. Por eso la física de Aristóteles parecía correcta durante tantos siglos.
- **Las herramientas.** Funciones cuadráticas, su vértice, la fórmula para resolverlas (y de dónde sale) y el discriminante; vectores con sus componentes y su suma; y el método de Euler con la dependencia del error con el paso.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 5.3, Segunda ley de Newton, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/5-3-segunda-ley-de-newton). Español, nivel universitario con cálculo; la segunda ley con ejemplos. Verificado el 31 de octubre de 2026.
2. [Resumen del capítulo 5, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/5-resumen). Español; resume las tres leyes, masa y peso. Visto en una búsqueda con ese contenido; no lo he abierto directamente. **(Sin verificar)**.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
