---
title: "Semana 8 · ¿Qué significa «moverse»?"
description: "Fase 1 · Principios básicos de astronomía. Álgebra básica, velocidad, aceleración y marcos de referencia."
sidebar:
  order: 8
  label: "8. ¿Qué significa «moverse»?"
---

## La pregunta del cielo

Ahora mismo estás sentado o de pie, y dirías que estás quieto. Pero la Tierra gira bajo ti a varios cientos de metros por segundo, y además recorre su órbita alrededor del Sol a casi 30 kilómetros por segundo. Ninguno de esos movimientos se nota. La pregunta es qué quiere decir exactamente «moverse», y la respuesta es: respecto a qué.

Esta semana aprendes el álgebra que permite despejar cualquier magnitud de una fórmula, la cinemática (el estudio del movimiento sin preguntar por sus causas), y calculas a qué velocidad vas realmente, según tu latitud y según el marco de referencia que elijas.

## Las cinco sesiones

### Sesión 1 · Matemáticas: ecuaciones lineales (30-40 min)

Una **ecuación** es una igualdad con una incógnita. Es **lineal** si la incógnita aparece solo a la primera potencia. Se resuelve **despejando**: aplicando a los dos lados la misma operación hasta dejar la incógnita sola. Si $3x + 7 = 22$, restas 7 a cada lado ($3x = 15$) y divides entre 3 ($x = 5$). Con las fórmulas físicas pasa lo mismo: de $v = d/t$ sacas $d = v\,t$ y $t = d/v$.

Un detalle práctico: las **unidades** son parte de la ecuación. Para pasar de km/h a m/s divides entre 3,6, porque 1 km/h = 1000 m / 3600 s. Y en una ecuación todos los términos deben tener las mismas unidades.

**Ejercicios**

1. Resuelve $3x + 7 = 22$ y $5 - 2x = 11$.
2. La Tierra da una vuelta de 40 075 km en 86 164 s. ¿Qué velocidad lleva un punto del ecuador, en m/s y en km/h?
3. A 100 km/h, ¿cuánto tardarías en recorrer los 384 400 km que hay hasta la Luna?
4. Pasa 29,78 km/s a km/h.

<details>
<summary>Soluciones</summary>

1. $x = 5$ y $x = -3$.
2. $40\,075\,000\ \text{m} / 86\,164\ \text{s} \approx$ **465,1 m/s**, que son unos **1674 km/h**.
3. $384\,400 / 100 = 3844$ h $\approx$ **160 días**.
4. $29{,}78 \cdot 3600 \approx$ **107 200 km/h**.

</details>

### Sesión 2 · Matemáticas: despejar fórmulas y ecuaciones con dos móviles (30-40 min)

La ecuación de un movimiento uniforme es $x = x_0 + v\,t$, donde $x_0$ es la posición inicial. Si conoces tres de las cuatro magnitudes, despejas la cuarta: $t = (x - x_0)/v$, o $v = (x - x_0)/t$.

Para saber cuándo se cruzan dos móviles se iguala su posición: la ecuación que sale es lineal en $t$.

**Ejercicios**

1. Un cuerpo parte de $x_0 = 10$ m con $v = 4$ m/s. ¿Cuándo llega a $x = 250$ m?
2. Dos personas caminan una hacia otra. A parte de la posición 0 con 3 m/s y B parte de la posición 100 m con 2 m/s hacia A. ¿Cuándo y dónde se cruzan?
3. La velocidad de rotación a latitud $\varphi$ es $v = 465{,}1 \cos\varphi$ m/s. ¿A qué latitud vale 232,6 m/s?
4. ¿A qué velocidad debería ir un coche para dar la vuelta a la Tierra por el ecuador en 24 h?

<details>
<summary>Soluciones</summary>

1. $t = (250 - 10)/4 =$ **60 s**.
2. A está en $3t$ y B en $100 - 2t$. Igualando, $5t = 100$, **$t = 20$ s**, en $x =$ **60 m**.
3. $\cos\varphi = 232{,}6/465{,}1 = 0{,}5$, luego $\varphi =$ **60°**.
4. $40\,075 / 24 \approx$ **1670 km/h**, casi la velocidad de rotación de la Tierra: quien volase hacia el oeste a esa velocidad vería el Sol casi quieto en el cielo.

</details>

### Sesión 3 · Física: velocidad, aceleración y marcos de referencia (30-40 min)

**Posición, velocidad y aceleración.** La posición $x(t)$ dice dónde está un cuerpo en cada instante. La **velocidad media** es el cambio de posición dividido entre el tiempo, $v = \Delta x/\Delta t$, y la **aceleración media** el cambio de velocidad entre el tiempo, $a = \Delta v/\Delta t$. Con aceleración constante $a$ (movimiento uniformemente acelerado):

$$v(t) = v_0 + a\,t, \qquad x(t) = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2.$$

En la gráfica de posición, la pendiente es la velocidad; en la de velocidad, la pendiente es la aceleración. En la semana 10 llevarás esa idea al límite y obtendrás la derivada.

**Marcos de referencia.** La velocidad no es una propiedad de un cuerpo, sino de su relación con otro: siempre se mide respecto a algo. Galileo lo vio con el barco: dentro de un camarote sin ventanas, no hay forma de saber si el barco se mueve a velocidad constante. Por eso tú no notas la velocidad de la Tierra. Algunas velocidades de referencia:

| Movimiento | Velocidad |
|---|---|
| Punto del ecuador por la rotación de la Tierra | 0,465 km/s (1674 km/h) |
| La Luna alrededor de la Tierra | 1,022 km/s |
| La Tierra alrededor del Sol | 29,78 km/s (107 200 km/h) |

(La velocidad orbital de la Tierra es la de la ficha de la NASA; la de la Luna es el valor habitual de las tablas de datos lunares; la del ecuador sale de dividir la circunferencia entre el día sidéreo.) Y tú, a latitud $\varphi$, te mueves por la rotación a $0{,}465\cos\varphi$ km/s: unos 356 m/s a 40° de latitud. Tu velocidad respecto al Sol es la suma vectorial de todas ellas (la suma de vectores la verás en la semana 9).

**¿Cómo sabemos que la Tierra gira?** Porque el cielo gira 15° por hora, pero eso se explicaría igual con una Tierra quieta. La prueba mecánica la dio el péndulo de Foucault en 1851, cuyo plano de oscilación va girando con respecto al suelo.

**Una aceleración que no notas.** Una velocidad constante en módulo pero que cambia de dirección implica aceleración. Un punto del ecuador, con $v = 465{,}1$ m/s y radio 6 378 km, tiene una aceleración hacia el centro $v^2/R \approx 0{,}034$ m/s², un 0,35 % de la gravedad. Es muy poca, y de ella hablaremos en la semana 9.

**Qué hacer**

1. Calcula tu velocidad respecto al centro de la Tierra, según tu latitud, con la fórmula de arriba.
2. Explica con tus palabras por qué «estar quieto» no tiene un sentido absoluto, con un ejemplo distinto del barco.

### Sesión 4 · Astronomía y observación (30-45 min)

**El giro del cielo.** El cielo da una vuelta de 360° en 24 horas, es decir, 15° por hora (semana 2). Compruébalo: una noche despejada, elige una estrella brillante (o un planeta) y marca su posición respecto a una referencia fija, como el marco de una ventana o la esquina de un edificio. Repite la medida cada 20 minutos durante una hora y mide con la mano el desplazamiento: debería ser unos 5° por cada 20 minutos (medio puño) para una estrella cercana al ecuador celeste. Si se mueve menos, ¿qué declinación tiene?

**En Stellarium.** Activa el movimiento rápido del tiempo con la cuadrícula ecuatorial y observa cómo todas las estrellas giran en círculos concéntricos alrededor del polo. Anota cuánto tarda la Polar en dar una vuelta y cuánto una estrella del ecuador.

**Cálculo.** Con la fórmula de la sesión 3, calcula tu velocidad por la rotación terrestre desde tu latitud. Suponiendo que una persona del ecuador y otra del polo tardan lo mismo en dar una vuelta alrededor del eje, ¿por qué una va a 1674 km/h y la otra a 0?

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 8:

- convierte velocidades entre km/h y m/s,
- calcula la velocidad de rotación según la latitud y la de la órbita terrestre,
- dibuja posición y velocidad de un movimiento uniforme y de uno acelerado,
- simula el movimiento paso a paso y mide cómo el error depende del tamaño del paso.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-08.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-08.ipynb)

La simulación por pasos es la técnica que usarás en las fases siguientes para calcular órbitas: avanzar el reloj un poco y actualizar velocidad y posición.

## Qué has aprendido

- **La respuesta.** «Moverse» solo tiene sentido respecto a otro cuerpo. Mientras estás quieto respecto al suelo, te mueves a unos 356 m/s por la rotación de la Tierra (a 40° de latitud) y a casi 30 km/s por su órbita, y no lo notas porque esas velocidades son casi constantes.
- **La causa.** La velocidad se define como el cambio de posición entre el tiempo, y un cambio de velocidad se llama aceleración. Un movimiento sin aceleración es indistinguible del reposo.
- **Las herramientas.** Ecuaciones lineales y despeje de fórmulas con unidades, las ecuaciones del movimiento uniforme y uniformemente acelerado, y la simulación paso a paso con su error.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 5.3, Segunda ley de Newton, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/5-3-segunda-ley-de-newton). Español; para la semana siguiente, pero introduce cómo la aceleración se relaciona con las fuerzas. Verificado el 31 de octubre de 2026.
2. [4.1 Earth and Sky, *Astronomy* (OpenStax)](https://openstax.org/books/astronomy/pages/4-1-earth-and-sky). Inglés; menciona el péndulo de Foucault de 1851 como prueba de la rotación de la Tierra. Verificado el 31 de octubre de 2026.
3. [Ficha de la Tierra, NASA NSSDCA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html). Inglés; velocidad orbital, día sidéreo y radio. **(Sin verificar)** directamente.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
5. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
