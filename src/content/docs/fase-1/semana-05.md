---
title: "Semana 5 · ¿Por qué la Luna cambia de forma?"
description: "Fase 1 · Principios básicos de astronomía. Fracciones, ángulos y la geometría Sol-Tierra-Luna que produce las fases."
sidebar:
  order: 5
  label: "5. ¿Por qué la Luna cambia de forma?"
---

## La pregunta del cielo

La Luna es el objeto más fácil de observar: no hace falta instrumento, se ve desde cualquier ciudad y cambia cada noche. Pasa de una uña fina a un disco completo y vuelve a empezar en unas cuatro semanas. Mucha gente cree que la causa es la sombra de la Tierra sobre la Luna. No lo es: esa sombra solo cae sobre ella en un eclipse lunar, que es raro.

Esta semana explicas las fases con una sola idea geométrica y la usas para calcular, con unas pocas líneas de Python, qué fase tiene la Luna cualquier día.

## Las cinco sesiones

### Sesión 1 · Matemáticas: fracciones y porcentajes (30-35 min)

Una **fracción** $a/b$ expresa una parte de un todo. Un **porcentaje** es una fracción de denominador 100: $0{,}25 = 25/100 = 25\,\%$. Las fases de la Luna se describen con dos fracciones distintas y es fácil confundirlas:

- la fracción **del ciclo** transcurrida, desde luna nueva hasta la siguiente (0 a 1),
- la fracción **del disco** iluminada (0 a 1).

El **cuarto creciente** ocurre cuando ha pasado una cuarta parte del ciclo, y en ese momento está iluminada la **mitad** del disco. El nombre se refiere al ciclo, no al disco.

**Ejercicios**

1. ¿Qué porcentaje del ciclo han transcurrido cuando la Luna tiene 10 días de edad (un ciclo dura 29,53 días)?
2. Un disco tiene el 85 % iluminado. ¿Qué fracción queda en sombra? Exprésala como fracción simplificada.
3. Si en un cuarto creciente se ve iluminada la mitad del disco, ¿qué fracción del disco estará iluminada una semana más tarde, en luna llena?
4. Calcula $\tfrac{1}{4} \cdot 29{,}53$ y compáralo con la edad del cuarto creciente que da el cuaderno (7,38 d).

<details>
<summary>Soluciones</summary>

1. 10 / 29,53 ≈ 0,339 = **33,9 %**.
2. 100 % − 85 % = 15 % = 15/100 = **3/20**.
3. Todo el disco: **1** (100 %). Del cuarto (la mitad) a la llena (todo) hay una semana, y ahí la fracción iluminada pasa de 1/2 a 1.
4. 29,53 / 4 = **7,38 días**: coincide.

</details>

### Sesión 2 · Matemáticas: ángulos y proporciones (30-40 min)

La posición de la Luna respecto al Sol se describe con un ángulo, la **elongación** $\varepsilon$: el que forman las direcciones Tierra–Sol y Tierra–Luna. Vale 0° en luna nueva (la Luna está del lado del Sol) y 180° en luna llena (justo opuesta). Como el ciclo completo son 360° y dura 29,53 días, la elongación crece de forma proporcional al tiempo:

$$\varepsilon = 360^\circ \cdot \frac{\text{edad}}{29{,}53}.$$

El ritmo es $360/29{,}53 \approx 12{,}2^\circ$ por día. La fracción del disco iluminada es $k = (1 - \cos\varepsilon)/2$; el coseno lo estudiarás en la semana 7. Por ahora comprueba con la calculadora que da 0, 0,5 y 1 en 0°, 90° y 180°.

**Ejercicios**

1. ¿Cuántos grados de elongación hay a los 5 días de luna nueva?
2. ¿A qué edad la elongación es de 90°? ¿Y de 270°?
3. Con la calculadora, halla $k$ para $\varepsilon = 45^\circ$.
4. ¿Cuántos grados recorre la Luna respecto al Sol en un día? ¿Y en una hora?

<details>
<summary>Soluciones</summary>

1. 360 · 5 / 29,53 ≈ **61°**.
2. 90° es un cuarto del ciclo, es decir, **7,38 días**, y 270° son tres cuartos, **22,15 días**.
3. $\cos 45^\circ \approx 0{,}7071$, luego $k = (1 - 0{,}7071)/2 \approx 0{,}146$, un **14,6 %**.
4. En un día, 360/29,53 ≈ **12,2°**; en una hora, 12,2 / 24 ≈ **0,51°** (el diámetro aparente de la Luna: la Luna se desplaza su propio diámetro cada hora respecto al Sol).

</details>

### Sesión 3 · Física: geometría Sol–Tierra–Luna (30-40 min)

La Luna no emite luz propia: refleja la del Sol, y siempre tiene iluminada una mitad, la que mira al Sol. Lo que cambia es **cuánto de esa mitad vemos desde la Tierra**, y eso depende de la elongación:

- **Luna nueva** (ε = 0°): la mitad iluminada mira hacia el lado contrario al nuestro. No la vemos, y sale y se pone con el Sol.
- **Cuarto creciente** (ε = 90°): vemos la mitad del disco iluminada. Sale hacia el mediodía y se pone hacia la medianoche.
- **Luna llena** (ε = 180°): vemos todo el disco. Sale al ponerse el Sol y se pone al salir el Sol.
- **Cuarto menguante** (ε = 270°): de nuevo la mitad del disco. Sale hacia la medianoche y se pone hacia el mediodía.

**Dos periodos.** La Luna da una vuelta a la Tierra respecto a las estrellas en 27,32 días (mes sidéreo). Las fases tardan 29,53 días (mes sinódico), unos dos días más, porque mientras tanto la Tierra avanza unos 29° en su órbita alrededor del Sol y la Luna tiene que recorrer ese ángulo adicional para alcanzar la misma posición respecto al Sol.

**Por qué sale unos 50 minutos más tarde cada día.** La Luna se desplaza respecto al Sol unos 12,2° al día, y como el cielo gira 1° cada 4 minutos, eso son $12{,}2 \cdot 4 \approx 49$ minutos.

**Por qué no hay eclipse todos los meses.** La órbita de la Luna está inclinada unos 5° respecto al plano de la órbita terrestre, por lo que normalmente la sombra de la Tierra pasa por encima o por debajo de la Luna llena, y la de la Luna, por encima o por debajo de la Tierra en luna nueva.

**Qué hacer**

1. Explica con un dibujo, sin consultar, las cuatro fases de la lista anterior con las posiciones de Sol, Tierra y Luna vistas desde arriba.
2. Para el dibujo, el vídeo de NASA (recurso 1) muestra cómo cambia la vista de la mitad iluminada.

### Sesión 4 · Astronomía y observación (30-45 min)

**En el cielo.** Durante una semana, a la misma hora, dibuja la Luna y la posición que ocupa respecto a una referencia del paisaje (un edificio, un árbol). Anota la fecha, la hora, la forma, y si puedes, a qué hora sale o se pone. Con ello comprobarás el retraso de unos 50 minutos diarios.

**En Stellarium.**

1. Fija tu lugar y avanza la fecha de un día en un día durante un mes. Anota la forma de la Luna y su hora de salida.
2. Anota la fecha de las cuatro fases principales (nueva, cuarto creciente, llena y cuarto menguante).
3. Tras la sesión 5, compara esas fechas con las del modelo.

En el hemisferio norte la Luna creciente se ilumina por la derecha y la menguante por la izquierda; en el hemisferio sur es al revés. Una regla orientativa para el hemisferio norte: una Luna iluminada por la derecha, con forma de "D", es creciente, y una iluminada por la izquierda, con forma de "C", es menguante. No es una definición, solo un recordatorio.

No mires nunca al Sol directamente.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 5:

- calcula la edad de la Luna a partir de una luna nueva de referencia y el periodo sinódico,
- calcula la elongación y la fracción iluminada,
- dibuja la forma del disco iluminado para cualquier edad,
- obtiene la fase de la fecha que elijas y estima la próxima luna llena.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-05.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-05.ipynb)

El modelo supone que la Luna se mueve con regularidad. En realidad su velocidad varía y las fases reales pueden adelantarse o retrasarse hasta unas 14 horas respecto al modelo. Mide ese desfase con Stellarium.

## Qué has aprendido

- **La respuesta.** La Luna siempre tiene la mitad iluminada, pero desde la Tierra vemos una parte distinta de ella según el ángulo entre la Luna y el Sol. Ese ángulo crece 360° en 29,53 días.
- **La causa.** La Luna orbita la Tierra y la Tierra orbita el Sol, y la fase depende solo de la geometría de las tres posiciones, no de la sombra de la Tierra.
- **Las herramientas.** Fracciones y porcentajes (cuidado con "cuarto"), proporcionalidad entre tiempo y ángulo, y un modelo de ciclo medio que se puede contrastar con una medida independiente.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Our World: Moon Phases, NASA Science (eClips)](https://science.nasa.gov/eclips/videos/moon-phases/). Inglés, vídeo educativo con animaciones y preguntas de discusión; la página no indica la duración del vídeo. Verificado el 31 de octubre de 2026.
2. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
3. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las fases dibujadas en el cuaderno son de elaboración propia.
