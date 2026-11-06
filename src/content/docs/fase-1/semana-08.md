---
title: "Semana 8 · ¿Qué significa «moverse»?"
description: "Fase 1 · Principios básicos de astronomía. Ecuaciones lineales, despejar fórmulas con unidades, velocidad, aceleración y marcos de referencia."
sidebar:
  order: 8
  label: "8. ¿Qué significa «moverse»?"
---

## La pregunta del cielo

Ahora mismo estás sentado o de pie, y dirías que estás quieto. Pero la Tierra gira bajo ti a varios cientos de metros por segundo, y además recorre su órbita alrededor del Sol a casi 30 kilómetros por segundo. Ninguno de esos movimientos se nota. La pregunta es qué quiere decir exactamente «moverse», y la respuesta es: respecto a qué.

Esta semana aprendes el álgebra que permite despejar cualquier magnitud de una fórmula, la cinemática (el estudio del movimiento sin preguntar por sus causas), y calculas a qué velocidad vas realmente, según tu latitud y según el marco de referencia que elijas.

:::note[De dónde viene la palabra]
**Cinemática** viene del griego *kínēma*, «movimiento», de *kineîn*, «mover». De la misma raíz viene *cine*, abreviatura de *cinematógrafo*, «el que escribe el movimiento». **Velocidad** viene del latín *velox*, «rápido», y **aceleración**, de *accelerare*, «darse prisa», de *ad*, «hacia», y *celer*, «rápido». Esa misma *celer* aparece en la letra $c$ con la que se escribe la velocidad de la luz, según una explicación habitual: *celeritas*, «rapidez».
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: ecuaciones lineales (35-45 min)

**Qué es una ecuación.** Una **ecuación** es una igualdad en la que hay un número desconocido, la **incógnita**, que se suele llamar $x$. Resolverla es encontrar el valor de $x$ que hace verdadera la igualdad. Por ejemplo, en $3x + 7 = 22$ hay que encontrar el número que, multiplicado por 3 y sumándole 7, da 22.

**La balanza.** Piensa en una ecuación como una balanza en equilibrio: lo que hay a la izquierda del signo igual pesa lo mismo que lo que hay a la derecha. Si quitas lo mismo de los dos platos, o los divides los dos en el mismo número de partes, la balanza sigue equilibrada. Esa es la única regla: **lo que hagas a un lado, házselo al otro**. Despejar es usar esa regla para ir quitando lo que acompaña a la incógnita hasta dejarla sola:

$$3x + 7 = 22 \;\xrightarrow{\;-7\;}\; 3x = 15 \;\xrightarrow{\;\div 3\;}\; x = 5.$$

Se deshacen las operaciones en orden inverso al que se aplicaron a $x$: primero se multiplicó por 3 y luego se sumó 7, así que primero se resta 7 y luego se divide entre 3. Siempre puedes **comprobar** el resultado sustituyéndolo en la ecuación original: $3 \cdot 5 + 7 = 22$. Correcto.

Una ecuación es **lineal** si la incógnita aparece solo a la primera potencia: sin cuadrados, raíces ni divisiones por $x$. Las lineales tienen siempre una única solución (salvo casos raros) y se resuelven así, paso a paso.

**Fórmulas.** Con las fórmulas físicas pasa lo mismo, solo que todas las letras representan magnitudes. De $v = d/t$ (velocidad igual a distancia entre tiempo) puedes sacar la distancia multiplicando los dos lados por $t$: $d = v\,t$. Y el tiempo, dividiendo después entre $v$: $t = d/v$. Una sola fórmula sirve para tres preguntas.

**Las unidades son parte de la ecuación.** En una igualdad física, los dos lados tienen que tener las mismas unidades: no puedes igualar metros con segundos. Y las unidades se convierten multiplicando por un factor que vale 1. Como 1 km = 1000 m y 1 h = 3600 s:

$$1\ \frac{\text{km}}{\text{h}} = 1\ \frac{\text{km}}{\text{h}} \cdot \frac{1000\ \text{m}}{1\ \text{km}} \cdot \frac{1\ \text{h}}{3600\ \text{s}} = \frac{1000}{3600}\ \frac{\text{m}}{\text{s}} = \frac{1}{3{,}6}\ \frac{\text{m}}{\text{s}}.$$

Los kilómetros y las horas se cancelan como números. Por eso, para pasar de km/h a m/s se divide entre 3,6, y para el camino inverso se multiplica.

**Ejercicios**

1. Resuelve $3x + 7 = 22$ y $5 - 2x = 11$. Comprueba las dos soluciones.
2. La Tierra da una vuelta de 40 075 km en 86 164 s. ¿Qué velocidad lleva un punto del ecuador, en m/s y en km/h?
3. A 100 km/h, ¿cuánto tardarías en recorrer los 384 400 km que hay hasta la Luna?
4. Pasa 29,78 km/s a km/h.

<details>
<summary>Soluciones</summary>

1. $x = 5$. En la segunda: restas 5, $-2x = 6$, y divides entre −2: $x = -3$. Comprobación: $5 - 2 \cdot (-3) = 5 + 6 = 11$.
2. $40\,075\,000\ \text{m} / 86\,164\ \text{s} \approx$ **465,1 m/s**, que son unos **1674 km/h**.
3. $384\,400 / 100 = 3844$ h $\approx$ **160 días**.
4. $29{,}78 \cdot 3600 \approx$ **107 200 km/h**.

</details>

### Sesión 2 · Matemáticas: despejar fórmulas y ecuaciones con dos móviles (30-40 min)

**La ecuación de un movimiento uniforme.** Un cuerpo que se mueve en línea recta siempre a la misma velocidad hace un **movimiento uniforme**. Si en el instante $t = 0$ está en la posición $x_0$ y avanza con velocidad $v$, en el instante $t$ estará en

$$x = x_0 + v\,t.$$

Es una función lineal, como las de la semana 4: la posición inicial es la ordenada en el origen y la velocidad es la pendiente. Una velocidad negativa significa que el cuerpo se mueve hacia valores de $x$ decrecientes, es decir, hacia atrás. Si conoces tres de las cuatro magnitudes, despejas la cuarta: $t = (x - x_0)/v$, o $v = (x - x_0)/t$.

**Dos móviles.** Para saber cuándo se encuentran dos móviles, se escribe la posición de cada uno en función del tiempo y se igualan: en el momento del encuentro, los dos están en el mismo sitio. La ecuación que sale es lineal en $t$. Gráficamente, es el punto donde se cruzan las dos rectas de posición.

**Ejercicios**

1. Un cuerpo parte de $x_0 = 10$ m con $v = 4$ m/s. ¿Cuándo llega a $x = 250$ m?
2. Dos personas caminan una hacia otra. A parte de la posición 0 con 3 m/s y B parte de la posición 100 m con 2 m/s hacia A. ¿Cuándo y dónde se cruzan?
3. La velocidad de rotación a latitud $\varphi$ es $v = 465{,}1 \cos\varphi$ m/s (lo explicamos en la sesión 3). ¿A qué latitud vale 232,6 m/s?
4. ¿A qué velocidad debería ir un coche para dar la vuelta a la Tierra por el ecuador en 24 h?

<details>
<summary>Soluciones</summary>

1. $t = (250 - 10)/4 =$ **60 s**.
2. A está en $3t$ y B en $100 - 2t$ (su velocidad es negativa, porque va hacia valores menores de $x$). Igualando, $3t = 100 - 2t$, $5t = 100$, **$t = 20$ s**, en $x =$ **60 m**.
3. $\cos\varphi = 232{,}6/465{,}1 = 0{,}5$, luego $\varphi =$ **60°**.
4. $40\,075 / 24 \approx$ **1670 km/h**, casi la velocidad de rotación de la Tierra: quien volase hacia el oeste a esa velocidad sobre el ecuador vería el Sol casi quieto en el cielo.

</details>

### Sesión 3 · Física: velocidad, aceleración y marcos de referencia (40-45 min)

**Posición, velocidad y aceleración.** La posición $x(t)$ dice dónde está un cuerpo en cada instante. Para hablar de cambios se usa la letra griega delta mayúscula, $\Delta$, que significa «cambio de»: $\Delta x$ es lo que ha cambiado la posición y $\Delta t$, el tiempo que ha pasado. La **velocidad media** es el cambio de posición dividido entre el tiempo, $v = \Delta x/\Delta t$, y la **aceleración media** es el cambio de velocidad dividido entre el tiempo, $a = \Delta v/\Delta t$. La aceleración se mide en metros por segundo cada segundo, m/s²: una aceleración de 2 m/s² significa que la velocidad aumenta 2 m/s cada segundo.

**Velocidad y rapidez.** En el lenguaje diario se usan como sinónimos, pero en física la **velocidad** incluye la dirección: ir a 50 km/h hacia el norte no es lo mismo que ir a 50 km/h hacia el sur. La **rapidez** es solo el número. Por eso un cuerpo que gira en círculo a rapidez constante sí tiene una velocidad que cambia, porque cambia de dirección: tiene aceleración.

**El movimiento uniformemente acelerado.** Con aceleración constante $a$, la velocidad crece de forma lineal con el tiempo: $v(t) = v_0 + a\,t$. ¿Y la posición? Como la velocidad crece de manera uniforme, la velocidad media durante el intervalo es la media entre la inicial y la final, $(v_0 + v)/2$. La distancia recorrida es esa velocidad media por el tiempo:

$$\Delta x = \frac{v_0 + (v_0 + a\,t)}{2}\cdot t = v_0\,t + \tfrac{1}{2}\,a\,t^2 \quad\Longrightarrow\quad x(t) = x_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2.$$

Si dibujas la velocidad frente al tiempo, sale una recta, y la distancia recorrida es el **área** bajo esa recta (un trapecio). En la gráfica de posición, la pendiente es la velocidad; en la de velocidad, la pendiente es la aceleración y el área, la distancia. En las semanas 10 y 11 llevarás estas dos ideas al límite y obtendrás la derivada y la integral.

**Marcos de referencia.** La velocidad no es una propiedad de un cuerpo, sino de su relación con otro: siempre se mide respecto a algo, el **marco de referencia**. Una persona que camina por el pasillo de un tren a 5 km/h, en un tren que va a 100 km/h, va a 5 km/h respecto al tren y a 105 km/h respecto a las vías. Galileo lo planteó en 1632 con un barco: dentro de un camarote sin ventanas, nada de lo que hagas (dejar caer objetos, ver volar moscas, saltar) te permite saber si el barco está parado o se mueve a velocidad constante. Las leyes del movimiento son las mismas en los dos casos. Por eso tú no notas la velocidad de la Tierra. Algunas velocidades de referencia:

| Movimiento | Velocidad |
|---|---|
| Punto del ecuador por la rotación de la Tierra | 0,465 km/s (1674 km/h) |
| La Luna alrededor de la Tierra | 1,022 km/s |
| La Tierra alrededor del Sol | 29,78 km/s (107 200 km/h) |

(La velocidad orbital de la Tierra es la de la ficha de la NASA; la de la Luna es el valor habitual de las tablas de datos lunares; la del ecuador sale de dividir la circunferencia entre el día sidéreo.)

**Tu velocidad según la latitud.** Por la rotación, describes cada día un círculo alrededor del eje de la Tierra. En el ecuador, ese círculo tiene el radio de la Tierra, $R$; en los polos, radio cero. A latitud $\varphi$, el radio de tu círculo es la distancia de tu posición al eje, y forma un triángulo rectángulo con el radio de la Tierra como hipotenusa y el ángulo $\varphi$ en el centro: es el cateto contiguo, $R\cos\varphi$ (semana 7). Como tardas lo mismo en dar la vuelta que alguien del ecuador, tu velocidad es la del ecuador multiplicada por $\cos\varphi$: $0{,}465\cos\varphi$ km/s, unos 356 m/s a 40° de latitud. Tu velocidad respecto al Sol es la combinación de todas ellas, sumadas teniendo en cuenta sus direcciones (la suma de vectores la verás en la semana 9).

**¿Cómo sabemos que la Tierra gira?** Porque el cielo gira 15° por hora, pero eso se explicaría igual con una Tierra quieta y un cielo que da vueltas. La prueba mecánica la dio Léon Foucault en París, en 1851, con un péndulo muy largo: un péndulo oscila siempre en el mismo plano, y el suelo de la Tierra gira por debajo de él, así que, visto desde el suelo, el plano de oscilación va girando lentamente a lo largo del día.

**Una aceleración que no notas.** Un punto del ecuador, con $v = 465{,}1$ m/s y radio 6378 km, está cambiando de dirección continuamente, así que tiene aceleración. Apunta hacia el centro del círculo y vale $v^2/R \approx 0{,}034$ m/s², un 0,35 % de la gravedad. Es muy poca, y de ella hablaremos en la semana 9.

**Qué hacer**

1. Calcula tu velocidad respecto al centro de la Tierra, según tu latitud, con la fórmula de arriba.
2. Explica con tus palabras por qué «estar quieto» no tiene un sentido absoluto, con un ejemplo distinto del barco.

### Sesión 4 · Astronomía y observación (30-45 min)

**El giro del cielo.** El cielo da una vuelta de 360° en 24 horas, es decir, 15° por hora (semana 2). Compruébalo: una noche despejada, elige una estrella brillante (o un planeta) y marca su posición respecto a una referencia fija, como el marco de una ventana o la esquina de un edificio. Repite la medida cada 20 minutos durante una hora y mide con la mano el desplazamiento: debería ser unos 5° por cada 20 minutos (medio puño) para una estrella cercana al ecuador celeste. Si se mueve menos, ¿qué declinación tiene? (Pista: las estrellas cerca del polo describen círculos pequeños, igual que tú describes un círculo pequeño si vives cerca del polo.)

**En Stellarium.** Activa el movimiento rápido del tiempo con la cuadrícula ecuatorial y observa cómo todas las estrellas giran en círculos concéntricos alrededor del polo. Anota cuánto tarda la Polar en dar una vuelta y cuánto una estrella del ecuador.

**Cálculo.** Con la fórmula de la sesión 3, calcula tu velocidad por la rotación terrestre desde tu latitud. Suponiendo que una persona del ecuador y otra del polo tardan lo mismo en dar una vuelta alrededor del eje, ¿por qué una va a 1674 km/h y la otra a 0?

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 8:

- convierte velocidades entre km/h y m/s,
- calcula la velocidad de rotación según la latitud y la de la órbita terrestre,
- dibuja posición y velocidad de un movimiento uniforme y de uno acelerado,
- simula el movimiento paso a paso y mide cómo el error depende del tamaño del paso.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-08.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-08.ipynb)

La simulación por pasos es la técnica que usarás en las fases siguientes para calcular órbitas: avanzar el reloj un poco, actualizar la velocidad con la aceleración y la posición con la velocidad, y repetir.

## Qué has aprendido

- **La respuesta.** «Moverse» solo tiene sentido respecto a otro cuerpo. Mientras estás quieto respecto al suelo, te mueves a unos 356 m/s por la rotación de la Tierra (a 40° de latitud) y a casi 30 km/s por su órbita, y no lo notas porque esas velocidades son casi constantes.
- **La causa.** La velocidad se define como el cambio de posición entre el tiempo, y un cambio de velocidad (en valor o en dirección) se llama aceleración. Un movimiento sin aceleración es indistinguible del reposo.
- **Las herramientas.** Ecuaciones lineales y la regla de la balanza, despeje de fórmulas, conversión de unidades con factores que valen 1, las ecuaciones del movimiento uniforme y uniformemente acelerado (con su deducción), y la simulación paso a paso con su error.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 5.3, Segunda ley de Newton, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/5-3-segunda-ley-de-newton). Español; para la semana siguiente, pero introduce cómo la aceleración se relaciona con las fuerzas. Verificado el 31 de octubre de 2026.
2. [4.1 Earth and Sky, *Astronomy* (OpenStax)](https://openstax.org/books/astronomy/pages/4-1-earth-and-sky). Inglés; menciona el péndulo de Foucault de 1851 como prueba de la rotación de la Tierra. Verificado el 31 de octubre de 2026.
3. [Ficha de la Tierra, NASA NSSDCA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html). Inglés; velocidad orbital, día sidéreo y radio. **(Sin verificar)** directamente.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
5. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
