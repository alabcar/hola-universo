---
title: "Semana 19 · ¿Cómo cambio de mapa sin perder el cielo?"
description: "Fase 2 · Órbitas. Matrices, producto de matriz por vector y matrices de rotación; cambio de sistema de referencia; coordenadas eclípticas."
sidebar:
  order: 19
  label: "19. ¿Cómo cambio de mapa sin perder el cielo?"
---

## La pregunta del cielo

En la semana 3 aprendiste a situar una estrella con dos sistemas de coordenadas: altura y azimut, que dependen de dónde y cuándo miras, y ascensión recta y declinación, ligadas al ecuador celeste. Pero cuando se estudian los planetas, ninguno de los dos es cómodo. Los planetas se mueven casi en un mismo plano, el de la órbita de la Tierra, y ese plano está inclinado 23,44° respecto al ecuador celeste. Para ellos se usa un tercer sistema, las **coordenadas eclípticas**, con el ecuador sustituido por la eclíptica.

Una misma estrella tiene así tres juegos de coordenadas, y el cielo es el mismo. Cambiar de sistema es como cambiar de mapa: los lugares no se mueven, cambian las líneas de la cuadrícula. Las matemáticas que hacen ese cambio son las **matrices**, y en concreto las **matrices de rotación**. Son también la herramienta básica de los gráficos por ordenador, de la robótica y de la navegación de las naves espaciales.

## Las cinco sesiones

### Sesión 1 · Matemáticas: matrices y rotaciones en el plano (35-45 min)

**Qué es una matriz.** Una **matriz** es una tabla rectangular de números, ordenados en filas y columnas. Una matriz de 2 × 2 tiene dos filas y dos columnas:

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}.$$

Por sí sola es solo una tabla. Lo interesante es lo que hace cuando la **multiplicas por un vector**.

**Matriz por vector.** Para multiplicar $A$ por un vector $(x, y)$, cada fila de la matriz se combina con el vector: se multiplican los números que ocupan la misma posición y se suman.

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} a\,x + b\,y \\ c\,x + d\,y \end{pmatrix}.$$

El resultado es otro vector. Así, una matriz es una **máquina de transformar vectores**: entra un vector y sale otro. Por ejemplo, $\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$ duplica cualquier vector, y $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ lo refleja como en un espejo sobre el eje $x$.

**La idea clave: las columnas.** Multiplica $A$ por $(1, 0)$: sale $(a, c)$, la primera columna. Multiplícala por $(0, 1)$: sale $(b, d)$, la segunda. Las columnas de una matriz te dicen a dónde van a parar los dos vectores de los ejes. Y como cualquier vector es una combinación de esos dos, con eso basta para saber qué hace la matriz con todo el plano.

**La matriz de rotación.** Busquemos la matriz que gira todo el plano un ángulo $\theta$ en sentido contrario a las agujas del reloj. El vector $(1, 0)$, girado $\theta$, va a parar a $(\cos\theta, \sin\theta)$: es la definición de la semana 13. El vector $(0, 1)$, que está a 90°, va a parar al ángulo $90^\circ + \theta$, es decir, a $(-\sin\theta, \cos\theta)$. Esas son las dos columnas:

$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$

Una rotación no cambia la longitud de los vectores ni los ángulos entre ellos. Solo los gira.

**Encadenar transformaciones.** Si primero giras $\alpha$ y luego $\beta$, el resultado es girar $\alpha + \beta$. En lenguaje de matrices, aplicar una tras otra equivale a multiplicar las matrices entre sí, $R(\beta)\,R(\alpha) = R(\alpha + \beta)$. El **producto de dos matrices** se calcula combinando cada fila de la primera con cada columna de la segunda, igual que con un vector. Y para deshacer un giro se gira en sentido contrario: la **matriz inversa** de $R(\theta)$ es $R(-\theta)$, que resulta ser la misma matriz con filas y columnas intercambiadas (su **traspuesta**).

:::note[De dónde viene la palabra]
**Matriz** viene del latín *matrix*, «madre que cría» y también «útero», de *mater*, «madre». En español conserva ese sentido en anatomía y en imprenta, donde la matriz es el molde del que salen las letras. El matemático inglés James Joseph Sylvester la usó en 1850 para estas tablas de números porque de ellas se «engendraban» los determinantes, que era lo que entonces le interesaba. **Rotación** viene de *rota*, «rueda», como *rotonda* o *rodar*.
:::

**Ejercicios**

1. Multiplica $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ por $(1, -1)$.
2. Escribe $R(90^\circ)$ y aplícala a $(3, 1)$. Dibuja los dos vectores para comprobarlo.
3. Aplica $R(30^\circ)$ a $(2, 0)$.
4. Calcula el producto $R(90^\circ)\,R(90^\circ)$. ¿Qué transformación es?

<details>
<summary>Soluciones</summary>

1. $(1 \cdot 1 + 2 \cdot (-1),\ 3 \cdot 1 + 4 \cdot (-1)) =$ **(−1, −1)**.
2. $R(90^\circ) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, y $R(90^\circ)(3, 1) =$ **(−1, 3)**: el vector ha girado un cuarto de vuelta hacia la izquierda.
3. $(2\cos 30^\circ, 2\sin 30^\circ) \approx$ **(1,73, 1)**.
4. $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$: un giro de **180°**, que cambia de signo los dos componentes.

</details>

### Sesión 2 · Matemáticas: rotaciones en el espacio (30-40 min)

**Coordenadas cartesianas en el cielo.** Las coordenadas del cielo son ángulos sobre una esfera, pero para girarlas conviene pasarlas a un vector de tres componentes. Una estrella con ascensión recta $\alpha$ y declinación $\delta$ está en la dirección

$$x = \cos\delta\cos\alpha, \qquad y = \cos\delta\sin\alpha, \qquad z = \sin\delta.$$

Es un vector de longitud 1 que apunta hacia la estrella. El eje $x$ apunta al **punto Aries** (el equinoccio de marzo, donde $\alpha = 0$ y $\delta = 0$), el eje $z$ al polo norte celeste y el eje $y$ completa el trío, hacia $\alpha = 6^\text{h}$. Para volver a los ángulos: $\delta = \arcsin z$ y $\alpha$ = `arctan2(y, x)`.

**Girar alrededor de un eje.** En el espacio se gira alrededor de un eje. Un giro alrededor del eje $x$ deja quieta la componente $x$ y gira el plano $yz$ como en la sesión 1. Su matriz es de 3 × 3:

$$R_x(\varepsilon) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\varepsilon & \sin\varepsilon \\ 0 & -\sin\varepsilon & \cos\varepsilon \end{pmatrix}.$$

(Los signos de los senos están cambiados respecto a la sesión 1 porque aquí no giramos los vectores, sino los **ejes**, en el sentido contrario. Es la misma rotación vista desde el otro lado.)

**El ecuador y la eclíptica.** Los dos planos se cortan en la línea de los equinoccios, que es justamente el eje $x$. El sistema eclíptico se obtiene inclinando el ecuatorial alrededor de ese eje un ángulo $\varepsilon = 23{,}44^\circ$, la **oblicuidad de la eclíptica** (la inclinación del eje de la Tierra que conoces desde la semana 1). Por tanto, para pasar de coordenadas ecuatoriales a eclípticas:

$$\begin{pmatrix} x' \\ y' \\ z' \end{pmatrix} = R_x(\varepsilon)\begin{pmatrix} x \\ y \\ z \end{pmatrix},$$

y luego la **latitud eclíptica** es $\beta = \arcsin z'$ y la **longitud eclíptica**, $\lambda$ = `arctan2(y', x')`.

**Ejercicios**

1. El punto del solsticio de junio tiene $\alpha = 90^\circ$ y $\delta = +23{,}44^\circ$. Calcula su vector $(x, y, z)$, aplícale $R_x(23{,}44^\circ)$ y comprueba que cae en la eclíptica ($\beta = 0$) con $\lambda = 90^\circ$.
2. El polo norte de la eclíptica tiene $\alpha = 270^\circ$ ($18^\text{h}$) y $\delta = 66{,}56^\circ$. Comprueba que, tras el giro, $z' = 1$.

<details>
<summary>Soluciones</summary>

1. $(x, y, z) = (0,\ \cos 23{,}44^\circ,\ \sin 23{,}44^\circ) \approx (0,\ 0{,}917,\ 0{,}398)$. Tras el giro: $x' = 0$, $y' = 0{,}917 \cdot 0{,}917 + 0{,}398 \cdot 0{,}398 \approx 1$, $z' = -0{,}917 \cdot 0{,}398 + 0{,}398 \cdot 0{,}917 = 0$. Así que $\beta = 0$ y $\lambda = 90^\circ$.
2. $(x, y, z) = (0,\ -\cos 66{,}56^\circ,\ \sin 66{,}56^\circ) \approx (0,\ -0{,}398,\ 0{,}917)$. Entonces $z' = 0{,}398 \cdot 0{,}398 + 0{,}917 \cdot 0{,}917 \approx$ **1**: es el polo de la eclíptica.

</details>

### Sesión 3 · Física: cambiar de sistema de referencia (30-40 min)

**Un vector, muchas descripciones.** Un vector, como la posición de Marte o la dirección de una estrella, existe independientemente de los ejes que uses. Las componentes, en cambio, dependen de los ejes. Cambiar de sistema de referencia es calcular las componentes nuevas a partir de las viejas. Hay tres tipos de cambio que aparecen una y otra vez en astronomía:

- **Traslación:** cambiar el origen. Para pasar de posiciones respecto al Sol (**heliocéntricas**) a posiciones respecto a la Tierra (**geocéntricas**) se resta el vector de la Tierra: $\vec{r}_\text{geo} = \vec{r}_\text{helio} - \vec{r}_\text{Tierra}$. Lo hiciste en la semana 13 para ver el retroceso de Marte.
- **Rotación:** cambiar la orientación de los ejes, sin mover el origen. Es el paso de coordenadas ecuatoriales a eclípticas, o de ecuatoriales a altura y azimut (que gira con la Tierra y depende de tu latitud).
- **Sistemas en movimiento:** si un sistema se mueve respecto a otro, las velocidades también cambian: $\vec{v}' = \vec{v} - \vec{V}$, donde $\vec{V}$ es la velocidad de un sistema respecto al otro (semana 8). Si además un sistema gira, aparecen fuerzas aparentes, como la de Coriolis, que desvía los vientos y las corrientes marinas en la Tierra.

**Lo que no cambia.** Las distancias entre puntos y los ángulos entre direcciones son iguales en todos los sistemas. Las leyes de la física tampoco cambian: la gravitación de Newton es la misma vista desde el Sol o desde la Tierra, aunque las ecuaciones parezcan más sencillas en un sistema que en otro. Por eso se elige siempre el sistema más cómodo para cada problema: el heliocéntrico para calcular órbitas, el geocéntrico para saber dónde mirar en el cielo y el horizontal para saber si una estrella está por encima del horizonte.

**El camino completo.** Para saber hacia dónde mirar para ver Marte, un programa de planetario como Stellarium hace una cadena de cambios: posición heliocéntrica eclíptica de Marte y de la Tierra (de sus órbitas) → resta (geocéntrica eclíptica) → giro de $\varepsilon$ (geocéntrica ecuatorial: ascensión recta y declinación) → giro según la hora y tu latitud (altura y azimut). En el cuaderno de esta semana y en el de la semana 24 haces los primeros pasos de esa cadena.

**Qué hacer**

1. Un barco navega a 10 km/h hacia el este y un pasajero camina por la cubierta a 4 km/h hacia el norte. ¿A qué velocidad y en qué dirección se mueve el pasajero respecto al agua?
2. La Tierra está en $(1, 0)$ ua y Marte en $(0, 1{,}5)$ ua respecto al Sol. ¿Qué vector va de la Tierra a Marte? ¿A qué distancia está Marte?

<details>
<summary>Soluciones</summary>

1. $(10, 4)$ km/h, de módulo $\sqrt{116} \approx$ **10,8 km/h**, a unos **22°** al norte del este.
2. $(0 - 1,\ 1{,}5 - 0) =$ **(−1, 1,5)**, a $\sqrt{1 + 2{,}25} \approx$ **1,80 ua**.

</details>

### Sesión 4 · Astronomía y observación: la eclíptica en el cielo (30-45 min)

**Qué es la eclíptica.** Es el camino que sigue el Sol entre las estrellas a lo largo del año, reflejo del movimiento de la Tierra a su alrededor. Como las órbitas de los planetas y de la Luna están poco inclinadas respecto a la de la Tierra (unos pocos grados como mucho), los planetas y la Luna se ven siempre cerca de la eclíptica. La franja de unos ocho grados a cada lado es el **zodiaco**, y las constelaciones que atraviesa son las zodiacales.

**En Stellarium.** Activa la línea de la **eclíptica** y, si quieres, la cuadrícula de coordenadas eclípticas (en el menú de opciones del cielo y de las marcas). Después:

1. Busca los planetas visibles esta noche y comprueba que todos están cerca de la línea de la eclíptica.
2. Busca la Luna y mira cuánto se aparta de la eclíptica. Repite una semana después: verás que oscila hasta unos 5° a cada lado, porque su órbita está inclinada unos 5°.
3. Selecciona una estrella brillante cerca de la eclíptica, como Régulo (en Leo) o Spica (en Virgo), y anota sus coordenadas ecuatoriales y eclípticas, que Stellarium muestra en el panel de información. Las usarás en el cuaderno para comprobar tu programa.

**A simple vista.** Al anochecer, en otoño, la eclíptica forma un ángulo pequeño con el horizonte del oeste; en primavera, un ángulo grande. Es una consecuencia directa de la inclinación de 23,44°, y explica por qué la Luna creciente se ve más alta al atardecer en primavera que en otoño.

:::note[De dónde viene la palabra]
**Eclíptica** viene del griego *ekleiptikós*, «de los eclipses», de *ékleipsis*, «desaparición, abandono». Es la línea en la que tienen que estar el Sol y la Luna para que haya un eclipse. **Zodiaco** viene del griego *zōidiakòs kýklos*, «círculo de las figurillas», de *zōídion*, diminutivo de *zôon*, «animal»: la mayoría de sus constelaciones representan animales.
:::

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 19:

- multiplica matrices y vectores con NumPy (el operador `@`) y comprueba que $R(\beta)R(\alpha) = R(\alpha+\beta)$,
- gira una figura en el plano para ver cómo actúa una matriz de rotación,
- programa el paso de coordenadas ecuatoriales a eclípticas y su inverso, y lo comprueba con los puntos de la sesión 2 y con una estrella,
- dibuja el ecuador celeste en coordenadas eclípticas y la eclíptica en coordenadas ecuatoriales, para ver la sinusoide que forma una respecto a la otra.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-19.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-19.ipynb)

## Qué has aprendido

- **La respuesta.** Para cambiar de mapa sin perder el cielo se aplica una transformación: una traslación si cambia el origen y una rotación si cambia la orientación de los ejes. Las coordenadas eclípticas se obtienen de las ecuatoriales girando 23,44° alrededor de la línea de los equinoccios.
- **Lo que se conserva.** Las distancias, los ángulos y las leyes físicas son los mismos en todos los sistemas. Se elige el sistema que hace el problema más sencillo.
- **Las herramientas.** Matrices, el producto de matriz por vector, el significado de las columnas de una matriz, la matriz de rotación en el plano y en el espacio, el producto de matrices como composición de transformaciones y la inversa de una rotación.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [La esfera celeste y la observación a simple vista, astronomas.org](https://astronomas.org/files/documents/learning/esfera_celeste.pdf). Español, PDF didáctico para Bachillerato; repasa las coordenadas ecuatoriales y horizontales que ya usaste en la semana 3. Verificado el 31 de octubre de 2026.
2. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

Las coordenadas de las estrellas que usa el cuaderno son aproximadas y las he escrito de memoria: compruébalas en Stellarium.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
