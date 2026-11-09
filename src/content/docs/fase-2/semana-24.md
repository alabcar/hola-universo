---
title: "Semana 24 · ¿Puedo predecir dónde estará Marte dentro de un año?"
description: "Fase 2 · Órbitas. Repaso de la fase; integración numérica de órbitas y elección del método; condiciones iniciales a partir de elementos orbitales; comparar una simulación con las efemérides."
sidebar:
  order: 24
  label: "24. ¿Puedo predecir dónde estará Marte dentro de un año?"
---

## La pregunta del cielo

Has llegado al final de la fase de órbitas. Sabes por qué Marte retrocede en el cielo, por qué su órbita es una elipse, qué fuerza lo mueve, cómo se calcula su periodo y cómo se viaja hasta él. La pregunta de esta semana junta todo eso en un solo reto: **predecir dónde estará Marte dentro de un año**, con tu propio programa, y comprobarlo con Stellarium.

No es un ejercicio de juguete. Es lo que hacen, con más precisión y más cuerpos, los programas que calculan las **efemérides**: las tablas de posiciones de los astros que usan los observatorios, las agencias espaciales y el propio Stellarium. Partirás de unos pocos números por planeta, publicados por el Jet Propulsion Laboratory (JPL) de la NASA, simularás el Sol y seis planetas con la gravitación de Newton y comprobarás tu simulación con las fechas de las oposiciones de Marte que ya conoces. Si las acierta, podrás fiarte de ella para el futuro. Y descubrirás algo que saben bien los que calculan efemérides: el resultado depende tanto del método como de lo buenas que sean las condiciones iniciales.

Esta semana tiene menos teoría nueva y más práctica. Las dos sesiones de matemáticas son de repaso.

## Las cinco sesiones

### Sesión 1 · Matemáticas: repaso de la fase, primera parte (35-45 min)

Intenta resolver cada ejercicio sin mirar las semanas anteriores. Si te atascas, la semana entre paréntesis tiene la herramienta.

1. (Semana 13) Un punto está a 3 unidades del origen, con un ángulo de 240°. ¿Cuáles son sus coordenadas?
2. (Semana 14) Una órbita tiene perihelio a 0,9 ua y afelio a 1,5 ua. Calcula $a$, $e$ y el semieje menor $b$.
3. (Semana 15) Calcula $\log_{10}$ de $2 \times 10^{5}$ sabiendo que $\log_{10} 2 \approx 0{,}301$. ¿Cuánto vale $27^{2/3}$?
4. (Semana 16) Suma los vectores $(2, -1)$ y $(-5, 3)$ y calcula el módulo y el vector unitario de la suma.
5. (Semana 17) Despeja $r$ en $v = \sqrt{2GM/r}$.

<details>
<summary>Soluciones</summary>

1. $(3\cos 240^\circ, 3\sin 240^\circ) =$ **(−1,5, −2,60)**.
2. $a = (0{,}9 + 1{,}5)/2 =$ **1,2 ua**; $e = (1{,}5 - 0{,}9)/(1{,}5 + 0{,}9) =$ **0,25**; $b = a\sqrt{1 - e^2} \approx$ **1,16 ua**.
3. $\log_{10}(2 \times 10^{5}) = 0{,}301 + 5 =$ **5,301**. $27^{2/3} = (\sqrt[3]{27})^2 =$ **9**.
4. $(-3, 2)$, de módulo $\sqrt{13} \approx$ **3,61**; unitario $\approx$ **(−0,83, 0,55)**.
5. $v^2 = 2GM/r$, así que **$r = 2GM/v^2$**.

</details>

### Sesión 2 · Matemáticas: repaso de la fase, segunda parte (35-45 min)

1. (Semana 18) Resuelve $3x + 2y = 7$ y $x + 4y = 9$.
2. (Semana 19) Aplica $R(90^\circ)$ al vector $(2, 5)$. ¿Qué longitud tiene el resultado?
3. (Semana 20) Una masa de 3 kg está en $(0, 0)$ y otra de 1 kg en $(8, 4)$. ¿Dónde está el centro de masas?
4. (Semana 21) Calcula $1/\sqrt{1{,}02}$ con la aproximación binomial.
5. (Semana 22) Calcula $\dfrac{(3 \times 10^{4})^2}{6 \times 10^{-3}}$.
6. (Semana 23) Da un paso de Euler de tamaño $0{,}1$ para $dy/dt = -2y$ partiendo de $y(0) = 5$.

<details>
<summary>Soluciones</summary>

1. De la segunda, $x = 9 - 4y$; en la primera, $27 - 12y + 2y = 7$, así que **$y = 2$, $x = 1$**.
2. $R(90^\circ)(2, 5) =$ **(−5, 2)**. Longitud $\sqrt{29} \approx 5{,}39$, la misma que la del vector original.
3. $(3 \cdot (0,0) + 1 \cdot (8,4))/4 =$ **(2, 1)**.
4. $(1 + 0{,}02)^{-1/2} \approx 1 - 0{,}01 =$ **0,99** (exacto: 0,9901).
5. $9 \times 10^{8} / 6 \times 10^{-3} =$ **1,5 × 10¹¹**.
6. $y(0{,}1) \approx 5 + (-2 \cdot 5) \cdot 0{,}1 =$ **4**.

</details>

### Sesión 3 · Física: integrar órbitas numéricamente (35-45 min)

**El problema.** La ecuación del movimiento de los planetas es una ecuación diferencial (semana 23): cada planeta se acelera según dónde estén todos los demás. Con dos cuerpos tiene solución exacta, las elipses de Kepler. Con más, no, y hay que resolverla paso a paso. Eso es **integrar numéricamente**: partir del estado de hoy (posiciones y velocidades) y avanzar el reloj en pasos pequeños.

**Tres métodos que ya conoces.**

- **Euler** (semana 8): posición nueva con la velocidad vieja, velocidad nueva con la aceleración vieja. Es el más sencillo, pero en una órbita la energía crece a cada vuelta y el planeta se va alejando en espiral. Inservible para periodos largos.
- **Euler-Cromer** (semana 12): primero la velocidad nueva y, con ella, la posición. Un cambio mínimo que hace que la energía oscile en vez de crecer. Mucho mejor.
- **Verlet o *leapfrog*** (semana 17): medio paso de velocidad, un paso de posición, otro medio paso de velocidad. Con el mismo coste que Euler, el error es mucho menor, y la energía se conserva muy bien durante millones de pasos.

Los dos últimos pertenecen a una familia de métodos llamados **simplécticos**, que respetan la estructura de la mecánica de Newton. Sus errores no se acumulan en la energía, y por eso son los preferidos para simular el Sistema Solar durante millones de años. El error que sí cometen es un pequeño desfase: el planeta simulado va un poco adelantado o atrasado respecto al real. Ese desfase crece con el tiempo y se reduce con pasos más pequeños.

**El tamaño del paso.** Un paso más pequeño da menos error, pero más cálculos. Para Verlet, el error en la posición disminuye con el cuadrado del paso: si lo divides por 2, el error se divide por 4. Una regla práctica es usar al menos unos cien pasos por cada vuelta del cuerpo más rápido. Para Mercurio, que da la vuelta en 88 días, un paso de un día está bien.

**Las condiciones iniciales.** Para empezar la simulación hace falta la posición y la velocidad de cada planeta en un instante. Las agencias las publican en forma de **elementos orbitales**: los números que describen la elipse y dónde está el planeta en ella en una fecha concreta, llamada **época**. Para una órbita en el plano bastan cuatro:

- el semieje mayor $a$ y la excentricidad $e$, que dan el tamaño y la forma (semana 14);
- la **longitud del perihelio**, $\varpi$ (una «pi» con forma de omega), que dice hacia dónde apunta el eje mayor;
- la **longitud media**, $L$, que dice dónde está el planeta en su órbita en la época. Con $M = L - \varpi$ y la ecuación de Kepler de la semana 14 se obtiene su posición y su velocidad.

Usarás los elementos del JPL para la época J2000, el mediodía del 1 de enero de 2000, junto con lo que cambia cada uno por siglo (porque las perturbaciones los hacen derivar despacio). Con las dos cosas puedes calcular los elementos para cualquier fecha cercana y empezar la simulación cuando quieras. Las órbitas reales están un poco inclinadas entre sí (la de Marte, 1,85° respecto a la de la Tierra; la de Mercurio, 7°). Las ignoraremos y lo haremos todo en el plano de la eclíptica: es una aproximación, y verás cuánto cuesta.

**Qué esperar.** La simulación da longitudes **heliocéntricas** (vistas desde el Sol). Para saber dónde mirar en el cielo hay que pasar a **geocéntricas** restando la posición de la Tierra (semana 19), y después, si quieres, a ascensión recta y declinación con la rotación de la oblicuidad.

:::note[De dónde viene la palabra]
**Efeméride** viene del griego *ephēmerís*, «diario, registro de cada día», de *epí*, «sobre», y *hēméra*, «día». Las efemérides astronómicas eran tablas con la posición de los astros para cada día. La misma raíz da **efímero**, «que dura un día». **Época** viene del griego *epochḗ*, «detención, parada»: el instante en que se detiene el reloj para tomar las medidas. La palabra **integrar** la tienes explicada en la semana 11.
:::

**Qué hacer**

1. Si una simulación con paso de 2 días tiene un error de 1000 km en la posición de Marte al cabo de un año, ¿qué error esperas con un paso de medio día?
2. ¿Por qué no basta con las leyes de Kepler, sin simulación, para predecir la posición de Marte? ¿Cuánto crees que se equivocarían?

<details>
<summary>Soluciones</summary>

1. El paso se divide por 4, así que el error se divide por $4^2 = 16$: unos **60 km**.
2. Las leyes de Kepler tratan cada planeta como si solo existieran él y el Sol. Ignoran las perturbaciones de los demás planetas, sobre todo de Júpiter. Para Marte, en un año, el error es pequeño, del orden de un minuto de arco, pero crece con el tiempo. En el cuaderno lo mides comparando la simulación con y sin Júpiter.

</details>

### Sesión 4 · Astronomía y observación: comparar con las efemérides (30-45 min)

**Las efemérides de Stellarium.** Stellarium calcula las posiciones de los planetas con teorías planetarias muy precisas, construidas a partir de integraciones como la tuya pero con todos los cuerpos importantes, las inclinaciones, la relatividad y décadas de observaciones. Tu simulación es una versión simplificada de lo mismo, y puedes compararlas.

1. En Stellarium, selecciona Marte y busca en el panel de información sus **coordenadas eclípticas**. Si aparecen dos versiones, una «de la fecha» y otra «J2000», apunta la de J2000, que es el sistema en el que están los elementos del JPL. (Si no las ves, actívalas en las opciones del panel de información.)
2. Apunta la longitud eclíptica de Marte para tres fechas: hoy, dentro de tres meses y dentro de un año. Usa siempre la misma hora, por ejemplo las 00:00 UTC.
3. En el cuaderno, calcula la longitud geocéntrica de Marte para las mismas fechas y compara. ¿Cuántos grados de diferencia hay?

**Y en el cielo.** La predicción más bonita es la que puedes comprobar mirando. Tu programa también calcula la **elongación** de Marte (su separación del Sol en el cielo, semana 18): si es mayor de unos 30°, Marte se verá de noche. Comprueba que a principios de noviembre de 2026 está a unos 80° del Sol, visible de madrugada, y que en la oposición del 19 de febrero de 2027 está a 180°: visible toda la noche, alto hacia el sur a medianoche, en Leo.

### Sesión 5 · Proyecto en Python (45-60 min)

El proyecto final de la fase. El cuaderno de la semana 24:

- compara Euler y Verlet en la órbita de la Tierra durante cien años,
- calcula las posiciones y velocidades iniciales del Sol y seis planetas (de Mercurio a Saturno) a partir de los elementos orbitales del JPL para la época J2000,
- los simula juntos, con la gravitación de todos sobre todos, desde el año 2000 hasta 2028,
- **valida** la simulación: calcula las fechas de las oposiciones de Marte y las compara con las reales, y ve cómo el error se acumula a lo largo de los años,
- repite la simulación empezando hoy, con los elementos calculados para la fecha actual, y acierta la oposición del 19 de febrero de 2027 con un error de minutos,
- predice la longitud eclíptica, la ascensión recta, la declinación y la elongación de Marte para cualquier fecha, en particular dentro de un año,
- mide cuánto cambia la predicción si se quita Júpiter de la simulación.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-24.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-24.ipynb)

## Qué has aprendido

- **La respuesta.** Sí: con la ley de la gravitación, unos pocos números por planeta y un método de integración adecuado, se puede predecir dónde estará Marte dentro de un año con un error pequeño. Empezando la simulación con los datos de hoy, la oposición de 2027 sale con un error de minutos. Empezando en el año 2000, el error se ha acumulado hasta algo más de un día: las condiciones iniciales mandan.
- **El método.** Integrar una ecuación diferencial paso a paso con un método que conserve la energía (Verlet), a partir de condiciones iniciales tomadas de elementos orbitales publicados, y validar el resultado con observaciones conocidas antes de usarlo para predecir.
- **La fase entera.** Has pasado del movimiento aparente de los planetas en el cielo (semana 13) a las leyes que lo describen (Kepler, semanas 14 y 15), a la fuerza que lo causa (Newton, semanas 16 y 17) y a las herramientas para calcularlo en cualquier situación: viajes (18), cambios de coordenadas (19), dos cuerpos (20), mareas (21), masas (22), muchos cuerpos (23) y predicciones (24).

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Keplerian Elements for Approximate Positions of the Major Planets (JPL, NASA)](https://ssd.jpl.nasa.gov/planets/approx_pos.html). Inglés; la tabla de elementos orbitales que usa el cuaderno, con instrucciones para calcular posiciones aproximadas. **(Sin verificar)**: los valores del cuaderno los he escrito de memoria a partir de esta tabla; la simulación los valida con las fechas de las oposiciones de Marte.
2. [Sección 13.5, Leyes del movimiento planetario de Kepler, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-5-leyes-del-movimiento-planetario-de-kepler). Español; repaso de las leyes de Kepler y las órbitas. Verificado el 6 de noviembre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

Las fechas de las oposiciones de Marte con las que se valida la simulación las he comprobado en varias fuentes de divulgación astronómica el 6 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
