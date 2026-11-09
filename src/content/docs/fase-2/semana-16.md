---
title: "Semana 16 · ¿Qué tira de la Luna?"
description: "Fase 2 · Órbitas. Vectores, suma de fuerzas y componentes; la ley de la gravitación universal de Newton; la prueba de la Luna y el inverso del cuadrado."
sidebar:
  order: 16
  label: "16. ¿Qué tira de la Luna?"
---

## La pregunta del cielo

En la semana 9 viste la primera ley de Newton: sin una fuerza, un cuerpo sigue en línea recta a velocidad constante. Pero la Luna no va en línea recta: da vueltas alrededor de la Tierra. Algo cambia la dirección de su velocidad en cada instante, y ese algo tiene que tirar de ella hacia la Tierra.

La idea genial de Newton fue que esa fuerza es la misma que hace caer una manzana. No hay una física para el cielo y otra para la Tierra: la gravedad es **universal**. Toda masa atrae a toda otra masa, y la atracción se debilita con el cuadrado de la distancia. Con esa ley, publicada en 1687 en los *Principia*, Newton explicó a la vez la caída de los cuerpos, las órbitas de los planetas, las leyes de Kepler, las mareas y la forma de la Tierra.

Esta semana aprendes la ley de la gravitación y las matemáticas para usarla con varios cuerpos a la vez: los vectores. Y repites el cálculo con el que Newton comprobó que la Luna «cae» hacia la Tierra.

## Las cinco sesiones

### Sesión 1 · Matemáticas: vectores (35-45 min)

**Escalares y vectores.** Algunas magnitudes quedan completamente descritas con un número y su unidad: una masa de 3 kg, un tiempo de 10 s, una temperatura de 20 °C. Se llaman **escalares**. Otras necesitan además una dirección: no basta con decir que empujas con 10 newtons, hay que decir hacia dónde. Se llaman **vectores**. La posición, la velocidad, la aceleración y la fuerza son vectores.

Un vector se dibuja como una flecha. Su longitud es el **módulo** (lo grande que es) y su orientación, la **dirección y el sentido**. Se escribe con una flecha encima, $\vec{F}$, y su módulo, sin flecha o entre barras: $F = |\vec{F}|$.

**Componentes.** Para calcular con vectores se colocan unos ejes y se describe cada vector por cuánto avanza en cada eje: sus **componentes**. En el plano, $\vec{v} = (v_x, v_y)$. Si conoces el módulo $v$ y el ángulo $\theta$ que forma con el eje $x$, las componentes son las de la semana 13:

$$v_x = v\cos\theta, \qquad v_y = v\sin\theta,$$

y al revés, el módulo sale de Pitágoras, $v = \sqrt{v_x^2 + v_y^2}$, y el ángulo, de la arcotangente (en Python, `np.arctan2(vy, vx)`).

**Operaciones.** Todo se hace componente a componente:

- **Suma:** $(a_x, a_y) + (b_x, b_y) = (a_x + b_x,\ a_y + b_y)$. Gráficamente, se pone el segundo vector a continuación del primero y la suma va del origen del primero al final del segundo.
- **Resta:** igual, restando. El vector que va de un punto $A$ a un punto $B$ es $\vec{B} - \vec{A}$: «a dónde llego menos de dónde salgo».
- **Multiplicar por un número:** $k\,(a_x, a_y) = (k a_x, k a_y)$. Cambia el módulo, no la dirección (si $k$ es negativo, invierte el sentido).

**Vector unitario.** Un vector de módulo 1 solo indica una dirección. Se obtiene dividiendo cualquier vector por su módulo: $\hat{u} = \vec{v}/v$. Se escribe con un acento circunflejo, «u gorro». Es muy útil para escribir fuerzas: «una fuerza de módulo $F$ en la dirección de $\hat{u}$» es simplemente $F\,\hat{u}$.

**Por qué importa aquí.** Cuando varias fuerzas actúan sobre un cuerpo, lo que cuenta para la segunda ley de Newton es la **fuerza neta**: la suma vectorial de todas ellas. Dos fuerzas de 3 N y 4 N pueden dar una neta de 7 N, de 1 N o de 5 N, según cómo apunten.

:::note[De dónde viene la palabra]
**Vector** es una palabra latina que significa «el que lleva, el que transporta», del verbo *vehere*, «llevar» (de la misma raíz que *vehículo*). En astronomía antigua, el *radius vector* era la línea imaginaria que «lleva» al planeta alrededor del Sol, la de la segunda ley de Kepler. William Rowan Hamilton le dio su sentido matemático moderno hacia 1845. **Escalar** viene de *scala*, «escalera»: una magnitud que solo sube o baja por una escala de números.
:::

**Ejercicios**

1. Calcula $(3, -1) + (2, 5)$, $(3, -1) - (2, 5)$ y $4\,(0{,}5, -2)$.
2. Un punto $A$ está en $(1, 2)$ y otro $B$ en $(4, 6)$. Calcula el vector de $A$ a $B$, su módulo y el vector unitario en esa dirección.
3. Sobre un cuerpo actúan una fuerza de 10 N hacia la derecha y otra de 10 N que forma 120° con la primera. ¿Cuánto vale la fuerza neta y hacia dónde apunta?

<details>
<summary>Soluciones</summary>

1. $(5, 4)$, $(1, -6)$ y $(2, -8)$.
2. $\vec{AB} = (4 - 1, 6 - 2) =$ **(3, 4)**, de módulo **5**. El unitario es $(3/5, 4/5) =$ **(0,6, 0,8)**.
3. Componentes: $(10, 0)$ y $(10\cos 120^\circ, 10\sin 120^\circ) = (-5, 8{,}66)$. La suma es $(5, 8{,}66)$, de módulo $\sqrt{25 + 75} =$ **10 N**, y apunta a **60°** del eje $x$, justo en la bisectriz de las dos fuerzas.

</details>

### Sesión 2 · Matemáticas: proporcionalidad inversa y el inverso del cuadrado (30-40 min)

**Proporcionalidad inversa.** Dos magnitudes son **inversamente proporcionales** si al multiplicar una por un número, la otra queda dividida por ese número: $y = k/x$. Si una magnitud es inversamente proporcional al **cuadrado** de otra, $y = k/x^2$, al duplicar $x$, $y$ se divide por 4; al triplicarla, por 9; al multiplicarla por 10, por 100.

**Por qué el cuadrado.** Piensa en una bombilla en el centro de una esfera. Toda su luz atraviesa la esfera. Si la esfera tiene el doble de radio, su superficie ($4\pi r^2$) es cuatro veces mayor, y la misma luz se reparte en cuatro veces más superficie: cada metro cuadrado recibe la cuarta parte. Cualquier cosa que salga de un punto y se reparta por igual en todas las direcciones se debilita con el cuadrado de la distancia. Es la ley de la luz (fase 3) y, según Newton, la de la gravedad.

**Ejercicios**

1. Si la intensidad de una fuente a 1 m es 36 unidades, ¿cuánto vale a 2 m, a 3 m y a 6 m?
2. Una fuerza inversamente proporcional al cuadrado de la distancia vale 100 N a 1000 km. ¿A qué distancia vale 1 N?
3. La Tierra recibe del Sol unos 1361 W por metro cuadrado. Júpiter está a 5,2 ua. ¿Cuánto recibe Júpiter por metro cuadrado?

<details>
<summary>Soluciones</summary>

1. **9**, **4** y **1** unidades.
2. Para que la fuerza se divida por 100, la distancia se multiplica por $\sqrt{100} = 10$: **10 000 km**.
3. $1361 / 5{,}2^2 \approx$ **50 W/m²**.

</details>

### Sesión 3 · Física: la gravitación universal (30-40 min)

**La ley.** Dos masas puntuales $m_1$ y $m_2$ separadas una distancia $r$ se atraen con una fuerza de módulo

$$F = G\,\frac{m_1\,m_2}{r^2},$$

dirigida a lo largo de la línea que las une. Cada masa tira de la otra con la misma fuerza y en sentido contrario: es la tercera ley de Newton. La Tierra tira de ti con tu peso, y tú tiras de la Tierra con la misma fuerza; la diferencia es que a la Tierra esa fuerza no la acelera de forma apreciable, porque su masa es enorme.

**La constante $G$.** Vale $G = 6{,}674 \times 10^{-11}\ \text{N}\cdot\text{m}^2/\text{kg}^2$. Es un número diminuto: dos masas de 1 kg a 1 m se atraen con $6{,}7 \times 10^{-11}$ N, lo que pesa un grano de polen. La gravedad solo es importante cuando al menos una de las masas es astronómica. Newton no pudo medir $G$. La primera medida precisa de la atracción entre masas de laboratorio la hizo Henry Cavendish en 1798, con una balanza de torsión, y la usó para calcular la densidad media de la Tierra. Por eso se dice que Cavendish «pesó la Tierra».

**Cuerpos esféricos.** La ley es para masas puntuales, pero Newton demostró que una esfera atrae a los cuerpos de fuera como si toda su masa estuviera en su centro. Por eso, para la Tierra, $r$ es la distancia a su centro, no a su superficie.

**La gravedad en la superficie.** Un cuerpo de masa $m$ en la superficie de un planeta de masa $M$ y radio $R$ sufre una fuerza $F = GMm/R^2$. Por la segunda ley, su aceleración es $F/m$:

$$g = \frac{G M}{R^2}.$$

La masa del cuerpo que cae se ha simplificado. Es la explicación de que todos los cuerpos caigan igual en el vacío, lo que Galileo había observado. Con la masa y el radio de la Tierra ($5{,}972 \times 10^{24}$ kg y 6371 km) sale $g \approx 9{,}82$ m/s².

**La prueba de la Luna.** Newton razonó así. La Luna está a unos 60 radios terrestres del centro de la Tierra (384 400 km / 6371 km ≈ 60,3). Si la gravedad disminuye con el cuadrado de la distancia, allí la aceleración de la gravedad terrestre debe ser $g/60{,}3^2 \approx 9{,}81 / 3636 \approx 0{,}00270$ m/s². Por otro lado, la Luna da una vuelta en 27,32 días por una órbita casi circular. En la semana 9 viste que un cuerpo en órbita circular tiene una aceleración hacia el centro $v^2/r$, con $v = 2\pi r/T$, es decir, $4\pi^2 r / T^2$. Con $r = 3{,}844 \times 10^8$ m y $T = 2{,}36 \times 10^6$ s sale $0{,}00272$ m/s². Los dos números coinciden con un error menor del 1 %. La Luna cae hacia la Tierra, igual que una manzana, solo que va tan deprisa de lado que nunca llega.

:::note[De dónde viene la palabra]
**Gravedad** viene del latín *gravitas*, «pesadez», de *gravis*, «pesado». La misma raíz da *grave* (un asunto pesado, serio) y *agravar*. Newton escribió los *Principia* en latín y usó esa palabra, *gravitas*, para la atracción que estaba describiendo. **Masa** viene del latín *massa*, «bulto, pasta», a su vez del griego *mâza*, una especie de torta de harina de cebada amasada. **Universal** es la clave de la ley: la misma para la manzana, la Luna y los planetas.
:::

**Qué hacer**

1. Calcula la fuerza con que la Tierra atrae a la Luna. Datos: $M_\text{T} = 5{,}972 \times 10^{24}$ kg, $M_\text{L} = 7{,}35 \times 10^{22}$ kg, $r = 3{,}844 \times 10^8$ m.
2. Calcula la fuerza con que el Sol atrae a la Luna ($M_\text{S} = 1{,}989 \times 10^{30}$ kg, distancia $1{,}496 \times 10^{11}$ m). ¿Es mayor o menor que la de la Tierra? ¿Por qué, entonces, la Luna no se va con el Sol?
3. Calcula la gravedad en la superficie de la Luna ($R = 1737$ km). ¿Cuántas veces menor es que en la Tierra?

<details>
<summary>Soluciones</summary>

1. $F = 6{,}674\times10^{-11} \cdot 5{,}972\times10^{24} \cdot 7{,}35\times10^{22} / (3{,}844\times10^{8})^2 \approx$ **1,98 × 10²⁰ N**.
2. $F \approx$ **4,4 × 10²⁰ N**, unas **2,2 veces mayor**. La Luna no se va porque el Sol tira casi igual de la Tierra y de la Luna, que están juntas: las dos caen alrededor del Sol a la vez, como una pareja, y la Luna gira alrededor de la Tierra mientras tanto. Lo que separa a la Luna de la Tierra no es la fuerza del Sol, sino la *diferencia* entre cómo tira de una y de otra, que es pequeña. Esa diferencia tiene nombre: es la fuerza de marea (semana 21).
3. $g_\text{L} = G \cdot 7{,}35\times10^{22} / (1{,}737\times10^{6})^2 \approx$ **1,62 m/s²**, unas **6 veces menor**.

</details>

### Sesión 4 · Astronomía y observación: la Luna cayendo (30-45 min)

La Luna avanza alrededor de la Tierra unos 13° al día respecto a las estrellas, algo más de medio grado por hora: más o menos su propio diámetro cada hora. Ese avance es el resultado de dos cosas: la velocidad que lleva de lado y la caída hacia la Tierra que curva su camino.

**Observación a simple vista.** Elige una noche con Luna cerca de alguna estrella brillante o de un planeta (Stellarium te dice cuándo). Mira la Luna dos o tres veces a lo largo de la noche, con una hora o dos de separación, y apunta su posición respecto a la estrella. Comprobarás que se desplaza hacia el este, en sentido contrario al movimiento diario del cielo.

1. Calcula cuánto debería haberse movido en el tiempo transcurrido (unos 0,55° por hora).
2. Mídelo con la mano extendida, como en la semana 2: un dedo meñique abarca aproximadamente 1°.

**Cálculo: cuánto cae la Luna.** En un minuto, la Luna recorre unos 61 km de su órbita. Si no hubiera gravedad, seguiría en línea recta y se alejaría de la Tierra. La gravedad la desvía hacia el centro una distancia $\tfrac{1}{2}a\,t^2$, con $a = 0{,}0027$ m/s² y $t = 60$ s: unos **4,9 m** cada minuto. Una manzana en la Tierra cae 4,9 m en el primer segundo. La Luna cae lo mismo en un minuto, 60 veces más tiempo: $60^2 = 3600$ veces menos aceleración, a 60 veces más distancia. Es el razonamiento de Newton en una sola frase.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 16:

- define vectores con NumPy y practica suma, módulo y vector unitario,
- programa una función que calcula la fuerza gravitatoria (como vector) que un cuerpo ejerce sobre otro,
- suma las fuerzas del Sol y de la Tierra sobre la Luna en distintas posiciones de su órbita,
- calcula la gravedad en la superficie de varios planetas,
- repite la prueba de la Luna de Newton.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-16.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-16.ipynb)

## Qué has aprendido

- **La respuesta.** De la Luna tira la gravedad de la Tierra, la misma fuerza que hace caer los objetos al suelo, debilitada con el cuadrado de la distancia. La Luna está cayendo continuamente hacia la Tierra, pero su velocidad lateral la hace caer «alrededor».
- **La ley.** $F = G\,m_1 m_2 / r^2$, igual para todos los cuerpos del universo. En la superficie de un planeta da $g = GM/R^2$, independiente de la masa del cuerpo que cae.
- **Las herramientas.** Vectores, sus componentes, su suma y el vector unitario; la proporcionalidad inversa al cuadrado y su origen geométrico.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 13.1, Ley de la gravitación universal de Newton, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-1-ley-de-la-gravitacion-universal-de-newton). Español, nivel universitario; la historia de la gravitación, la ley con ejemplos y el experimento de Cavendish. Verificado el 6 de noviembre de 2026.
2. [Unidad 5: Las leyes del movimiento planetario (Proyecto PETeR, Instituto de Astrofísica de Canarias)](https://outreach.iac.es/peter/wp-content/uploads/2025/10/Unidad-5-Leyes-del-Movimiento_Intro.pdf). Español, divulgativo; Newton y la gravitación universal en su contexto histórico. Verificado el 6 de noviembre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

Las masas y los radios de los planetas son valores redondeados de la hoja de datos planetarios de la NASA. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
