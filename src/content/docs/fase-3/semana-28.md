---
title: "Semana 28 · ¿Cómo funciona un telescopio?"
description: "Fase 3 · La luz. Reflexión y refracción, la ley de Snell, lentes y espejos, la ecuación de las lentes delgadas, aumentos, pupila de salida, captación de luz y resolución, con los prismáticos 8×30 como laboratorio."
sidebar:
  order: 28
  label: "28. ¿Cómo funciona un telescopio?"
---

## La pregunta del cielo

En el otoño de 1609, Galileo Galilei apuntó al cielo un tubo con dos lentes que él mismo había pulido. En pocos meses vio montañas y cráteres en la Luna, cuatro lunas alrededor de Júpiter (semana 22), las fases de Venus y miles de estrellas donde a simple vista no había nada. Ningún instrumento ha cambiado tanto, en tan poco tiempo, lo que la humanidad sabía del universo.

Unos prismáticos 8×30 son, en esencia, dos telescopios pequeños pegados. Esta semana entiendes cómo funcionan: cómo se dobla la luz al pasar por un vidrio, cómo una lente forma una imagen, qué significan los dos números grabados en ellos y qué es lo que de verdad importa en un telescopio (spoiler: no son los aumentos).

:::note[De dónde viene la palabra]
**Telescopio** viene del griego *tēle*, «lejos», y *skopeîn*, «mirar, observar»: «el que mira lejos». La palabra la propuso el matemático griego Giovanni Demisiani en 1611, en un banquete en Roma en honor de Galileo; hasta entonces se le llamaba *perspicillum* o «anteojo». **Lente** viene del latín *lens, lentis*, «lenteja», por su forma abombada por las dos caras. **Espejo** viene de *speculum*, de *specere*, «mirar», la misma raíz de *especular* y de *espectro* (semana 30).
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: rayos, reflexión y la ley de Snell (40-45 min)

**El rayo de luz.** Cuando los objetos son mucho mayores que la longitud de onda de la luz, se puede olvidar que es una onda y tratarla como **rayos**: líneas rectas que indican hacia dónde viaja. Es la **óptica geométrica**, y con ella se diseñan todas las lentes y los espejos.

**La normal.** Para describir qué le pasa a un rayo al llegar a una superficie se usa la **normal**: la recta perpendicular a la superficie en el punto donde llega el rayo. Los ángulos se miden siempre respecto a la normal, no respecto a la superficie.

**Reflexión.** Un rayo que rebota en un espejo sale con el mismo ángulo con el que llegó:

$$\theta_\text{reflejado} = \theta_\text{incidente}.$$

**Refracción y la ley de Snell.** Un rayo que pasa del aire al vidrio, o del aire al agua, se dobla. En la semana 25 viste que la luz viaja más despacio en esos medios, y el índice de refracción $n = c/v$ mide cuánto. La regla que dice cuánto se dobla es la **ley de Snell**:

$$n_1 \sin\theta_1 = n_2 \sin\theta_2.$$

Al entrar en un medio más denso ópticamente (con $n$ mayor), el rayo se acerca a la normal; al salir, se aleja. Una imagen ayuda a entender por qué: una fila de personas que camina en diagonal desde el asfalto hacia la arena. Los que pisan antes la arena frenan antes, y la fila entera gira.

**Reflexión total.** Al pasar de un medio más denso a uno menos denso (del vidrio al aire), el rayo se aleja de la normal. Si el ángulo de llegada es grande, el de salida tendría que superar 90°, lo que es imposible: el rayo no sale y se refleja entero. Es la **reflexión total interna**. Ocurre a partir de un **ángulo crítico** $\theta_c$ con $\sin\theta_c = n_2/n_1$; para el vidrio ($n \approx 1{,}5$) y el aire, unos 42°. Así funcionan la fibra óptica y los prismas de los prismáticos.

**Ejercicios**

1. Un rayo llega del aire ($n = 1$) al agua ($n = 1{,}33$) con 30° respecto a la normal. ¿Con qué ángulo sigue dentro del agua?
2. ¿Y si llega con 60°?
3. Calcula el ángulo crítico entre el agua y el aire. ¿Qué ve un buceador si mira hacia arriba con un ángulo mayor?
4. Un prisma de vidrio de los prismáticos tiene caras a 45°. Un rayo entra perpendicular a una cara y llega a la cara inclinada con 45°. ¿Sale o se refleja?

<details>
<summary>Soluciones</summary>

1. $\sin\theta_2 = \sin 30^\circ / 1{,}33 = 0{,}376$, así que $\theta_2 \approx$ **22,1°**.
2. $\sin\theta_2 = 0{,}866/1{,}33 = 0{,}651$, $\theta_2 \approx$ **40,6°**.
3. $\sin\theta_c = 1/1{,}33$, $\theta_c \approx$ **48,8°**. Más allá, el buceador ve la superficie como un espejo que refleja el fondo.
4. 45° es mayor que el ángulo crítico del vidrio (unos 42°): **se refleja entero**. Por eso los prismas funcionan como espejos perfectos, sin perder luz.

</details>

### Sesión 2 · Matemáticas: lentes, imágenes y aumentos (40-45 min)

**Una lente convergente.** Una lente más gruesa en el centro que en los bordes dobla los rayos hacia su eje, por la ley de Snell aplicada en sus dos caras. Los rayos que llegan paralelos al eje (de un objeto muy lejano, como una estrella) se juntan en un punto, el **foco**, a una distancia de la lente llamada **distancia focal**, $f$. Cuanto más curvada es la lente, menor es $f$.

**La ecuación de las lentes delgadas.** Un objeto a una distancia $d_o$ de la lente forma una imagen a una distancia $d_i$ al otro lado, con

$$\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}.$$

Para un objeto muy lejano, $1/d_o \approx 0$ y la imagen se forma en el foco: $d_i = f$. El tamaño de la imagen sale de triángulos semejantes (semana 6): un rayo que pasa por el centro de la lente no se desvía, y la imagen es al objeto lo que $d_i$ es a $d_o$.

**Un telescopio refractor.** Tiene dos lentes. La primera, el **objetivo**, grande y de distancia focal larga $F$, forma en su foco una imagen pequeña del objeto lejano. La segunda, el **ocular**, de distancia focal corta $f$, funciona como una lupa para mirar esa imagen de cerca. Un objeto que a simple vista abarca un ángulo pequeño $\alpha$ se ve a través del telescopio con un ángulo $\beta$ mayor. El cociente es el **aumento**:

$$M = \frac{\beta}{\alpha} = \frac{F}{f}.$$

(Sale de dos triángulos que comparten la imagen intermedia: su tamaño es $F\alpha$ visto desde el objetivo y $f\beta$ visto desde el ocular.) Cambiando el ocular, cambia el aumento.

**Lo que dicen los números de unos prismáticos.** «8×30» significa **8 aumentos** y objetivos de **30 mm** de diámetro. Con esos dos números se calcula casi todo:

- **Captación de luz.** La luz que recoge un instrumento es proporcional al área de su abertura, es decir, al cuadrado del diámetro $D$. La pupila del ojo, de noche, mide unos 7 mm en una persona joven y algo menos con la edad (unos 5 o 6 mm a partir de los 40 o 50 años). Con 30 mm frente a 7 mm, los prismáticos recogen $(30/7)^2 \approx 18$ veces más luz que el ojo desnudo.
- **Pupila de salida.** Es el diámetro del haz de luz que sale por el ocular: $D/M = 30/8 = 3{,}75$ mm. Si es mayor que tu pupila, parte de la luz se desperdicia. Por eso unos 10×50 (pupila de salida de 5 mm) son buenos para la noche, y unos 8×30 son más versátiles y ligeros.
- **Campo de visión.** Suele venir grabado en grados (por ejemplo, 7,5°) o en metros a 1000 m (por ejemplo, 131 m a 1000 m, que equivale a 7,5°, por la aproximación de la semana 2). Es el trozo de cielo que abarcas, unas 15 Lunas llenas.
- **Resolución.** Es el ángulo más pequeño entre dos estrellas que un instrumento puede separar. Por la difracción en la abertura (semana 27), una estrella no se ve como un punto, sino como un pequeño disco con anillos, el **disco de Airy**. Dos estrellas se separan si sus discos no se solapan demasiado, lo que da

$$\theta_\text{mín} \approx 1{,}22\,\frac{\lambda}{D} \quad \text{(radianes)}, \qquad \text{o, en la práctica,} \quad \theta_\text{mín} \approx \frac{116''}{D\ \text{(mm)}}$$

(la segunda forma, empírica, es el **límite de Dawes**). Para 30 mm, unos 4″; aunque con solo 8 aumentos, el límite lo pone tu ojo (que separa más o menos 1′): $60''/8 \approx 7{,}5''$.

**Ejercicios**

1. Un telescopio tiene un objetivo de 900 mm de focal y oculares de 25 mm y 10 mm. ¿Qué aumentos da con cada uno?
2. ¿Cuántas veces más luz recoge un telescopio de 130 mm que tus prismáticos de 30 mm?
3. ¿Qué pupila de salida tienen unos 10×50? ¿Y unos 7×50?
4. ¿Qué resolución tiene, según Dawes, un telescopio de 130 mm? ¿Podría separar dos estrellas a 2″?

<details>
<summary>Soluciones</summary>

1. $900/25 =$ **36 aumentos** y $900/10 =$ **90 aumentos**.
2. $(130/30)^2 \approx$ **19 veces**.
3. $50/10 =$ **5 mm** y $50/7 \approx$ **7,1 mm** (este último solo aprovecha bien la luz con pupilas muy dilatadas, típicas de gente joven).
4. $116/130 \approx$ **0,9″**: sí, podría separarlas, si la atmósfera está tranquila.

</details>

### Sesión 3 · Física: refractores, reflectores y lo que importa (35-45 min)

**El primer anteojo.** Los primeros anteojos aparecieron en los Países Bajos: en octubre de 1608, el fabricante de lentes Hans Lippershey pidió una patente para uno. Galileo supo de ellos en 1609 y fabricó los suyos, con un objetivo convergente y un ocular divergente, que daba la imagen derecha; llegó a unos 20 aumentos. En 1611, Kepler propuso usar un ocular convergente, que da la imagen invertida pero un campo mucho mayor. Casi todos los telescopios de lentes desde entonces siguen su diseño.

**El problema del color.** El índice de refracción del vidrio depende un poco del color: el azul se dobla más que el rojo. Por eso un prisma separa la luz blanca en colores, como en el arcoíris (es la **dispersión cromática**, la otra «dispersión» de la semana 26). En una lente, eso hace que cada color se enfoque a una distancia distinta, y las estrellas brillantes se ven rodeadas de un halo de color: es la **aberración cromática**. Se corrige combinando dos vidrios distintos en el objetivo (un **acromático**), invento del siglo XVIII.

**Los reflectores.** En 1668, Isaac Newton resolvió el problema de otra manera: cambió la lente objetivo por un espejo cóncavo, que refleja todos los colores igual. Un pequeño espejo plano inclinado saca la luz hacia un lado del tubo, donde está el ocular. Es el **telescopio newtoniano**, todavía hoy el más barato por centímetro de abertura. Todos los grandes telescopios del mundo son reflectores, porque un espejo se puede sujetar por detrás y fabricar mucho más grande que una lente: el Gran Telescopio Canarias, en La Palma, tiene un espejo de 10,4 m formado por 36 piezas hexagonales.

**Los prismáticos por dentro.** Un telescopio de Kepler da la imagen invertida, lo que no importa para mirar estrellas, pero sí para mirar paisajes. Los prismáticos le dan la vuelta con dos prismas en cada lado, que reflejan la luz por reflexión total (sesión 1). Ese diseño, de Ignazio Porro (1854), es el que da a muchos prismáticos su forma de «Z». Los prismas también pliegan el camino de la luz, y por eso los prismáticos son más cortos que la distancia focal de sus objetivos.

**Qué importa en un telescopio.** El número que más se anuncia en los telescopios baratos son los aumentos («¡600×!»), y es el menos importante. Los aumentos los cambias con el ocular. Lo que no puedes cambiar es la **abertura**, el diámetro del objetivo, que decide cuánta luz recoge (lo débil que puedes ver) y cuánto detalle puede mostrar (su resolución). Una regla práctica: el aumento máximo útil es de unas 2 veces el diámetro en milímetros (unos 260 aumentos para un telescopio de 130 mm), y solo en noches de atmósfera muy estable. Para un primer telescopio, los aficionados suelen recomendar un reflector de unos 130 a 200 mm sobre una montura sencilla, antes que un telescopio pequeño con muchos aumentos.

:::note[De dónde viene la palabra]
**Prisma** viene del griego *prîsma*, «cosa aserrada», del verbo *prízein*, «serrar»: un bloque cortado con caras planas. **Ocular** viene de *oculus*, «ojo»: la lente junto al ojo. **Objetivo**, la lente que mira al objeto. **Aberración**, como viste en la semana 25, es «desviarse».
:::

**Qué hacer**

1. Explica por qué un telescopio de 200 mm a 50 aumentos muestra más estrellas débiles que uno de 60 mm a 200 aumentos.
2. Calcula el aumento máximo útil de unos prismáticos de 30 mm y comprueba que 8 aumentos queda muy por debajo. ¿Por qué no hacen prismáticos de 60 aumentos?
3. Busca en tus prismáticos el campo de visión grabado. Si viene en metros a 1000 m, pásalo a grados.

### Sesión 4 · Astronomía y observación: tus prismáticos como instrumento (30-45 min)

**Medir su campo.** Busca dos estrellas de separación conocida, por ejemplo las dos estrellas de los extremos del cinturón de Orión (Alnitak y Mintaka, a unos 2,7°), o mide en Stellarium la separación de dos estrellas cercanas. Mira cuántas veces caben en el campo de los prismáticos y estima el campo en grados. Compáralo con el valor grabado.

**Cuánto más ves.** Elige una zona pequeña del cielo, como el interior del cuadrado de Pegaso (en otoño, alto a primera hora de la noche) o la zona de las Pléyades. Cuenta las estrellas que ves a simple vista y luego con los prismáticos. Según el cálculo de la sesión 2, los prismáticos te dan unas 3 magnitudes más (semana 33): en un cielo oscuro, eso multiplica por más de diez el número de estrellas visibles.

**Un recorrido para noches de otoño e invierno** (todos visibles con 8×30, incluso desde una ciudad, si apoyas bien los prismáticos):

- **Las Pléyades**, en Tauro: un racimo de unas decenas de estrellas azuladas en lugar de las seis o siete que ves a simple vista.
- **La Luna**, unos días después del cuarto creciente: los cráteres cerca de la línea entre la luz y la sombra, donde las sombras son largas.
- **Júpiter** y sus lunas (semana 22).
- **La nebulosa de Orión** (M42), bajo el cinturón: una mancha de luz difusa alrededor de varias estrellas. Es una región donde nacen estrellas (semana 35).
- **El cúmulo doble de Perseo**, entre Perseo y Casiopea: dos cúmulos de estrellas que caben juntos en el campo.

**Consejos prácticos.** Apoya los prismáticos (en una valla, en el techo de un coche, contra un poste) o siéntate y apoya los codos en las rodillas: el temblor de las manos es lo que más limita a 8 aumentos. Enfoca primero el ojo izquierdo con la rueda central y luego el derecho con el ajuste del ocular derecho. Y **nunca** los apuntes al Sol: concentran su luz y pueden dejarte ciego al instante.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 28:

- calcula con la ley de Snell la trayectoria de un rayo a través de un prisma, para varios colores,
- dibuja los rayos principales de una lente y comprueba la ecuación de las lentes delgadas,
- programa una calculadora de instrumentos (aumento, pupila de salida, captación de luz, magnitud límite aproximada y resolución) y la aplica al ojo, a tus prismáticos y a varios telescopios,
- dibuja el disco de Airy de una estrella para distintas aberturas.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-28.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-28.ipynb)

## Qué has aprendido

- **La respuesta.** Un telescopio recoge la luz con una lente o un espejo grande (el objetivo), que forma una imagen pequeña del objeto lejano en su foco, y la amplía con una lente pequeña (el ocular). Lo que importa es el diámetro del objetivo: decide cuánta luz recoge y cuánto detalle puede separar. Los aumentos solo dependen del ocular.
- **Tus prismáticos 8×30.** 8 aumentos, objetivos de 30 mm, unas 18 veces más luz que el ojo, unas 3 magnitudes más de alcance y un campo de unos 7 u 8 grados: un instrumento excelente para cúmulos, la Luna, las lunas de Júpiter y la Vía Láctea.
- **Las herramientas.** La ley de la reflexión, la ley de Snell, la reflexión total, la ecuación de las lentes delgadas, el aumento como cociente de focales, y las fórmulas de captación de luz y resolución.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**La ley de Snell sale de un principio de mínimo.** En 1662, Pierre de Fermat propuso que la luz, para ir de un punto a otro, sigue el camino que **tarda menos tiempo**. Es el **principio de Fermat**, y de él se deducen la reflexión y la refracción.

Un socorrista está en la playa, en el punto A, y tiene que llegar a un bañista en el agua, en el punto B. Corre más deprisa por la arena ($v_1$) que nada en el agua ($v_2$). ¿Por dónde debe entrar al agua? La línea recta no es lo más rápido: conviene recorrer un poco más de arena y un poco menos de agua. Pon la orilla en el eje $x$, A a una altura $a$ sobre la orilla, B a una profundidad $b$ bajo ella, y una distancia horizontal $L$ entre los dos. Si entra al agua en el punto $x$, el tiempo total es

$$t(x) = \frac{\sqrt{a^2 + x^2}}{v_1} + \frac{\sqrt{b^2 + (L - x)^2}}{v_2}.$$

El camino más rápido está donde la derivada se anula (semana 10). Derivando (con la regla de la cadena: la derivada de $\sqrt{u}$ es $u'/(2\sqrt{u})$):

$$\frac{dt}{dx} = \frac{x}{v_1\sqrt{a^2 + x^2}} - \frac{L - x}{v_2\sqrt{b^2 + (L-x)^2}} = 0.$$

Pero $x/\sqrt{a^2 + x^2}$ es el seno del ángulo $\theta_1$ que forma el primer tramo con la normal a la orilla, y el otro cociente es $\sin\theta_2$. Así que

$$\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2},$$

y como $v = c/n$, sale $n_1\sin\theta_1 = n_2\sin\theta_2$: la ley de Snell. La luz «resuelve» el problema del socorrista. Este tipo de principio, en el que la naturaleza elige el camino que hace mínima (o estacionaria) una cantidad, reaparece en toda la física, de la mecánica a la relatividad.

:::note[De dónde viene la palabra]
La **regla de la cadena** se llama así porque encadena derivadas: si una función depende de otra que depende de la variable, la derivada total es el producto de las derivadas de cada eslabón.
:::

**Ejercicios**

1. Comprueba con el principio de Fermat la ley de la reflexión: un rayo va de A a B rebotando en un espejo plano. ¿Dónde está el punto de rebote más corto? Pista: refleja B al otro lado del espejo; el camino más corto hasta el reflejo es una recta.
2. El socorrista corre a 7 m/s y nada a 2 m/s. Si sale de la orilla corriendo con un ángulo de 60° respecto a la normal, ¿con qué ángulo debe nadar?
3. Calcula la derivada de $\sqrt{a^2 + x^2}$ con la regla de la cadena.

<details>
<summary>Soluciones</summary>

1. El reflejo B′ de B está al otro lado del espejo, a la misma distancia. Cualquier camino A → espejo → B mide lo mismo que A → espejo → B′, y el más corto es la recta de A a B′. Esa recta cruza el espejo en un punto donde, por los ángulos opuestos por el vértice, el ángulo de llegada es igual al de salida.
2. $\sin\theta_2 = \sin 60^\circ \cdot 2/7 \approx 0{,}247$, así que $\theta_2 \approx$ **14,3°**: casi recto hacia el bañista.
3. Con $u = a^2 + x^2$, $u' = 2x$, y la derivada es $2x/(2\sqrt{a^2 + x^2}) = x/\sqrt{a^2 + x^2}$.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [6.1 Telescopios, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/06%3A_Instrumentos_astron%C3%B3micos/6.01%3A_Telescopios). Español; refractores, reflectores, captación de luz y resolución. Verificado el 20 de noviembre de 2026.
2. [2.4 Lentes delgadas, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/2-4-lentes-delgadas). Español; diagramas de rayos y la ecuación de las lentes delgadas. Verificado el 20 de noviembre de 2026.
3. [2.8 Microscopios y telescopios, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/2-8-microscopios-y-telescopios). Español; el aumento de un telescopio y los diseños newtoniano y Cassegrain. Verificado el 20 de noviembre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
