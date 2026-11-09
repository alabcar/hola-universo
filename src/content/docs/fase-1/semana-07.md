---
title: "Semana 7 · ¿A qué distancia está la Luna y cómo lo sabemos?"
description: "Fase 1 · Principios básicos de astronomía. El teorema de Pitágoras, seno, coseno y tangente, paralaje y geometría de los eclipses."
sidebar:
  order: 7
  label: "7. ¿A qué distancia está la Luna y cómo lo sabemos?"
---

## La pregunta del cielo

Esa distancia no se puede medir con una cinta métrica ni se deduce de lo que ves. Se obtiene con un truco geométrico: mirar el mismo objeto desde dos lugares distintos y comparar. Es la misma idea que usa tu cerebro para calcular la distancia de lo que tienes delante con dos ojos, y es la base de casi todas las medidas de distancia en astronomía.

Esta semana estudias el teorema de Pitágoras y las tres funciones trigonométricas fundamentales, aprendes qué es la paralaje, y calculas la distancia a la Luna por tres caminos independientes: la paralaje, la geometría de la sombra de la Tierra en un eclipse y el tiempo de ida y vuelta de un pulso de luz.

## Las cinco sesiones

### Sesión 1 · Matemáticas: Pitágoras, seno, coseno y tangente (40-45 min)

**El teorema de Pitágoras.** En un triángulo rectángulo con catetos $a$ y $b$ e hipotenusa $c$:

$$a^2 + b^2 = c^2.$$

El cuadrado de un número es ese número multiplicado por sí mismo, y se llama así porque es el área de un cuadrado con ese lado. El teorema dice que el área del cuadrado construido sobre la hipotenusa es igual a la suma de las áreas de los cuadrados construidos sobre los catetos. El caso más conocido es el triángulo de lados 3, 4 y 5: $9 + 16 = 25$.

Hay cientos de demostraciones. Una de las más claras es esta. Dibuja un cuadrado grande de lado $a + b$ y coloca dentro, en las cuatro esquinas, cuatro copias del triángulo, de manera que sus hipotenusas formen un cuadrado inclinado en el centro, de lado $c$. El área del cuadrado grande se puede contar de dos formas: como $(a + b)^2$, o como cuatro triángulos (cada uno de área $ab/2$) más el cuadrado central, $c^2$. Igualando:

$$(a + b)^2 = 4 \cdot \frac{ab}{2} + c^2 \quad \Longrightarrow \quad a^2 + 2ab + b^2 = 2ab + c^2 \quad \Longrightarrow \quad a^2 + b^2 = c^2.$$

(El paso de en medio usa que $(a + b)^2 = (a + b)(a + b) = a^2 + 2ab + b^2$: cada término del primer paréntesis se multiplica por cada término del segundo.)

**Seno, coseno y tangente.** En la semana 6 viste que, en un triángulo rectángulo, los cocientes entre lados dependen solo de los ángulos. Hay tres cocientes con nombre propio. Para un ángulo agudo $\alpha$:

$$\sin\alpha = \frac{\text{cateto opuesto}}{\text{hipotenusa}},\qquad \cos\alpha = \frac{\text{cateto contiguo}}{\text{hipotenusa}},\qquad \tan\alpha = \frac{\text{cateto opuesto}}{\text{cateto contiguo}} = \frac{\sin\alpha}{\cos\alpha}.$$

El seno y el coseno siempre están entre 0 y 1 (para ángulos agudos), porque los catetos son más cortos que la hipotenusa. Leídos al revés, dicen cómo calcular un cateto: si conoces la hipotenusa $c$ y el ángulo, el cateto opuesto mide $c\sin\alpha$ y el contiguo, $c\cos\alpha$.

**Una consecuencia de Pitágoras.** Divide los dos lados de $a^2 + b^2 = c^2$ por $c^2$: queda $(a/c)^2 + (b/c)^2 = 1$, es decir,

$$\sin^2\alpha + \cos^2\alpha = 1,$$

donde $\sin^2\alpha$ significa $(\sin\alpha)^2$. Valores que conviene saber:

| Ángulo | 0° | 30° | 45° | 60° | 90° |
|---|---|---|---|---|---|
| Seno | 0 | 0,5 | 0,707 | 0,866 | 1 |
| Coseno | 1 | 0,866 | 0,707 | 0,5 | 0 |

El de 30° se ve con un triángulo equilátero de lado 2 partido por la mitad: queda un triángulo rectángulo con hipotenusa 2 y el cateto opuesto al ángulo de 30° de longitud 1, así que $\sin 30^\circ = 1/2$. Y la tabla tiene una simetría: el seno de un ángulo es el coseno de su complementario ($\sin 30^\circ = \cos 60^\circ$), porque en un triángulo rectángulo el cateto opuesto a un ángulo agudo es el contiguo al otro. El coseno es el que aparecía en la fórmula de la fracción iluminada de la Luna de la semana 5, $k = (1 - \cos\varepsilon)/2$: ahora ya puedes calcularlo a mano para 0°, 60° y 90°. (Para 120° y 180°, ángulos mayores de 90°, necesitas una definición más amplia, que verás en la fase 2; de momento usa la calculadora.)

:::note[De dónde viene la palabra]
**Teorema** viene del griego *theṓrēma*, «lo que se contempla», de *theōreîn*, «mirar, observar» (como *teatro* y *teoría*): una verdad que se ve después de demostrarla. El teorema lleva el nombre de Pitágoras (siglo VI a. C.), pero una tablilla de Babilonia de hacia el 1800 a. C. ya recoge ternas de números que lo cumplen, más de mil años antes. **Seno** tiene una historia de malentendidos: los matemáticos indios lo llamaban *jyā*, «cuerda de arco»; los árabes lo transcribieron como *jība*, que sin vocales se confundía con *jayb*, «pliegue, bolsillo»; y en el siglo XII se tradujo al latín como *sinus*, «pliegue, seno». **Coseno** es una abreviatura de *complementi sinus*, «seno del complemento».
:::

**Ejercicios**

1. Una escalera de 5 m se apoya formando 60° con el suelo. ¿A qué altura llega y a qué distancia de la pared está su base?
2. Un triángulo rectángulo tiene hipotenusa 10 y un ángulo de 30°. ¿Cuánto miden los catetos?
3. Un triángulo rectángulo tiene catetos de 6 y 8. ¿Cuánto mide la hipotenusa?
4. Calcula $k = (1 - \cos\varepsilon)/2$ para $\varepsilon = 60^\circ$ y, con la calculadora, para $\varepsilon = 120^\circ$.
5. Comprueba con la calculadora que $\sin^2 37^\circ + \cos^2 37^\circ = 1$.

<details>
<summary>Soluciones</summary>

1. Altura $= 5\sin 60^\circ \approx$ **4,33 m**; base $= 5\cos 60^\circ =$ **2,5 m**.
2. $10\sin 30^\circ =$ **5** y $10\cos 30^\circ \approx$ **8,66**.
3. $\sqrt{36 + 64} = \sqrt{100} =$ **10**. Es el triángulo 3-4-5 multiplicado por 2.
4. Con 60°: $k = (1 - 0{,}5)/2 =$ **0,25**; con 120°, la calculadora da $\cos 120^\circ = -0{,}5$, y $k = (1 + 0{,}5)/2 =$ **0,75**.
5. $0{,}6018^2 + 0{,}7986^2 = 0{,}3622 + 0{,}6378 = 1{,}000$.

</details>

### Sesión 2 · Matemáticas: resolver triángulos y paralaje (35-40 min)

**Resolver un triángulo.** Resolver un triángulo rectángulo es hallar todos sus lados y ángulos conociendo solo dos datos (sin contar el ángulo recto). Si conoces la hipotenusa y un ángulo, los catetos son $c\sin\alpha$ y $c\cos\alpha$; si conoces un cateto y un ángulo, usas la tangente; si conoces los dos catetos, el ángulo es la arcotangente de su cociente y la hipotenusa sale de Pitágoras. El otro ángulo agudo es siempre $90^\circ$ menos el primero.

**La paralaje.** Pon el pulgar delante de la cara y míralo primero con un ojo y luego con el otro: parece saltar respecto al fondo. Ese salto aparente es la **paralaje**. Ocurre con cualquier objeto visto desde dos lugares distintos, y es mayor cuanto más cerca está el objeto y cuanto más separados están los dos puntos de vista.

Con números: dos observadores separados una distancia $B$ (la **línea de base**) miran un objeto lejano. Lo ven en direcciones que difieren un ángulo $p$, la paralaje. Los dos observadores y el objeto forman un triángulo **isósceles** (con dos lados iguales), de base $B$ y con el ángulo $p$ en el vértice del objeto. Si lo partes por la mitad con una línea desde el objeto hasta el centro de la base, quedan dos triángulos rectángulos, cada uno con un cateto $B/2$, el otro cateto $D$ (la distancia) y un ángulo $p/2$ en el objeto. Por la tangente:

$$\tan\frac{p}{2} = \frac{B/2}{D} \quad \Longrightarrow \quad D = \frac{B/2}{\tan(p/2)} \approx \frac{B}{p}\quad(p \text{ en radianes}),$$

donde la aproximación es la misma que en las semanas 2 y 6. Cuanto mayor es la línea de base, mayor el ángulo y más fácil de medir; cuanto más lejos está el objeto, menor el ángulo.

:::note[De dónde viene la palabra]
**Paralaje** viene del griego *parállaxis*, «cambio, alternancia», de *parallássein*, «cambiar, desplazar»: el objeto cambia de sitio según desde dónde lo mires. **Isósceles** viene de *ísos*, «igual», y *skélos*, «pierna»: un triángulo de dos piernas iguales.
:::

**Ejercicios**

1. Dos personas separadas 10 m ven una torre con una paralaje de 0,5°. ¿A qué distancia está?
2. La paralaje horizontal de la Luna (el ángulo bajo el que se vería desde ella el radio de la Tierra, de 6378 km) es de unos 57′ de arco. ¿A qué distancia está? (En este caso, el radio de la Tierra es el cateto opuesto y la distancia es la hipotenusa, así que $\sin p = R/D$.)
3. Un objeto está a 100 m y observas con una base de 6,5 cm (la distancia entre tus ojos). ¿Qué paralaje obtienes?
4. Con una base de un diámetro terrestre (12 756 km), ¿qué paralaje tendría una estrella a 4 años luz? (1 año luz ≈ 9,46 × 10¹² km)

<details>
<summary>Soluciones</summary>

1. $10/(2\tan 0{,}25^\circ) \approx$ **1146 m**.
2. $p = 57/60 = 0{,}95^\circ$, $\sin 0{,}95^\circ \approx 0{,}01658$, luego $D = 6378/0{,}01658 \approx$ **384 700 km**, unos 60 radios terrestres.
3. $p \approx 0{,}065/100 = 6{,}5 \times 10^{-4}$ rad $\approx$ **0,037°** (unos 2,2′).
4. $D \approx 3{,}8 \times 10^{13}$ km, luego $p \approx 12\,756 / 3{,}8\times10^{13} \approx 3{,}4\times 10^{-10}$ rad $\approx$ **0,00007″**. Imposible de medir con esa base: para las estrellas hace falta una línea de base mucho mayor (en la semana 37 usarás la órbita de la Tierra).

</details>

### Sesión 3 · Física: tres formas de medir la distancia (35-45 min)

**1. Paralaje.** Dos observadores en lugares muy distintos de la Tierra (a unos miles de kilómetros uno del otro) miden a la vez la posición de la Luna respecto a las estrellas de fondo, y la diferencia de posición da la paralaje. Con un radio terrestre como línea de base, la paralaje es de unos 57′, y de ella sale una distancia de unos 60 radios terrestres, 384 000 km. La medida requiere precisión: 1′ de error en esa paralaje se convierte en unos 7000 km de error en la distancia. Ya en el siglo II, Ptolomeo obtuvo con métodos de este tipo unos 59 radios terrestres para la distancia media de la Luna.

**2. Geometría del eclipse.** El Sol ilumina la Tierra, y detrás de la Tierra queda una zona de sombra. Como el Sol es mucho mayor que la Tierra, los rayos que pasan rozando los bordes de la Tierra se van cerrando y la zona de sombra completa, la **umbra**, tiene forma de cono que se estrecha con la distancia. Alrededor hay una zona de sombra parcial, la **penumbra**, desde donde solo se ve tapada una parte del Sol. En un eclipse de Luna, la Luna atraviesa ese cono. A la altura de la Luna, el cono mide unas 2,65 veces el diámetro lunar: sale de triángulos semejantes con los radios del Sol y de la Tierra y la distancia entre ellos (semana 6). El cuaderno hace el cálculo. Medir en un eclipse real ese cociente permite deducir cuánto mide la Luna comparada con la Tierra y, con su tamaño angular (semana 2), su distancia. Aristarco de Samos, en el siglo III a. C., ya usó este razonamiento y concluyó que la Luna mide aproximadamente un tercio del diámetro de la Tierra; el valor actual es algo más de una cuarta parte.

**3. Pulso de luz.** Los retrorreflectores (espejos que devuelven la luz exactamente por donde ha llegado) dejados en la Luna por las misiones Apolo y por otras misiones permiten medir con láser el tiempo que tarda un pulso de luz en ir y volver. Con la velocidad de la luz, $c = 299\,792{,}458$ km/s, la distancia es $D = c\,t/2$: se divide entre 2 porque la luz hace el camino dos veces. Para 384 400 km, el viaje de ida y vuelta tarda unos 2,564 s, y las medidas actuales alcanzan precisiones del orden de centímetros.

Las tres medidas dan el mismo resultado, y esa coincidencia entre métodos independientes es lo que da confianza en cada uno.

:::note[De dónde viene la palabra]
**Umbra** es la palabra latina para «sombra», y **penumbra** se formó con *paene*, «casi», y *umbra*: «casi sombra». Kepler usó el término en 1604. **Láser** es una sigla inglesa: *Light Amplification by Stimulated Emission of Radiation*, «amplificación de luz por emisión estimulada de radiación». Como *radar*, se usa tanto que ya se escribe como una palabra corriente.
:::

**Qué hacer**

1. Explica por escrito por qué la paralaje de la Luna se mide mejor con una línea de base grande que pequeña.
2. Calcula cuántos kilómetros recorre la luz en 1 segundo y cuántas veces daría la vuelta a la Tierra (usa la circunferencia de la semana 6).

### Sesión 4 · Astronomía y observación (30-45 min)

**La paralaje con tu cuerpo.** Extiende el brazo y levanta el pulgar. Cierra un ojo y luego el otro, y observa cómo salta el pulgar respecto a un fondo lejano. Mide con la regla de la mano (semana 2) cuántos grados salta, y con la distancia entre tus ojos (unos 6,5 cm) calcula a qué distancia está tu pulgar con $D = B/p$. Compruébalo con una cinta métrica.

**El movimiento de la Luna entre las estrellas.** Una noche con Luna visible, anota su posición respecto a una estrella cercana, y vuelve a mirar una hora más tarde. La Luna se mueve unos 0,5° por hora respecto a las estrellas (su propio diámetro), mucho más deprisa que cualquier planeta. Mídelo con la mano y con Stellarium.

**En Stellarium.** Elige la fecha de un eclipse de Luna (búscala en una fuente fiable, como el calendario de eclipses de la NASA o de un observatorio) y observa en el programa cómo la Luna cruza la sombra de la Tierra. Estima cuántos diámetros lunares mide la sombra y compáralo con 2,65.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 7:

- implementa seno, coseno y tangente en grados y una función que resuelve triángulos rectángulos,
- calcula distancias por paralaje, exacta y aproximada,
- obtiene la distancia a la Luna por paralaje, y estudia cuánto se equivoca si la paralaje se mide mal,
- calcula la sombra de la Tierra a la distancia de la Luna,
- calcula la distancia a partir del tiempo de ida y vuelta de un pulso láser.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-07.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-07.ipynb)

## Qué has aprendido

- **La respuesta.** La Luna está a unos 384 400 km de media, unos 60 radios terrestres. Se mide por paralaje, por geometría de eclipses y por el tiempo de ida y vuelta de un pulso láser, y los tres métodos coinciden.
- **La causa.** Un objeto visto desde dos lugares distintos aparece en direcciones diferentes, y el ángulo entre ellas, junto con la distancia entre los lugares, determina la distancia al objeto.
- **Las herramientas.** El teorema de Pitágoras y una demostración; seno, coseno y tangente, y la relación $\sin^2\alpha + \cos^2\alpha = 1$; resolución de triángulos rectángulos; y el cálculo de cómo un error pequeño en un ángulo se amplifica en la distancia.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Fases de la Luna, NASA Science (eClips)](https://science.nasa.gov/eclips/videos/moon-phases/). Inglés, vídeo educativo con animaciones del sistema Sol-Tierra-Luna; útil para visualizar la geometría de las tres posiciones. Verificado el 31 de octubre de 2026.
2. [Experimentos para medir la Tierra, UNAM (fascículo de Geociencias)](https://tellus.geociencias.unam.mx/wp-content/uploads/2020/01/libro6_medicion_tierra.pdf). Español; incluye la geometría de las sombras de la que sale el tamaño de la Tierra. Verificado el 31 de octubre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
