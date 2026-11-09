---
title: "Semana 5 · ¿Por qué la Luna cambia de forma?"
description: "Fase 1 · Principios básicos de astronomía. Fracciones, porcentajes, ángulos proporcionales al tiempo y la geometría Sol-Tierra-Luna que produce las fases."
sidebar:
  order: 5
  label: "5. ¿Por qué la Luna cambia de forma?"
---

## La pregunta del cielo

La Luna es el objeto más fácil de observar: no hace falta instrumento, se ve desde cualquier ciudad y cambia cada noche. Pasa de una uña fina a un disco completo y vuelve a empezar en unas cuatro semanas. Mucha gente cree que la causa es la sombra de la Tierra sobre la Luna. No lo es: esa sombra solo cae sobre ella en un eclipse lunar, que es raro.

Esta semana explicas las fases con una sola idea geométrica y la usas para calcular, con unas pocas líneas de Python, qué fase tiene la Luna cualquier día.

:::note[De dónde viene la palabra]
**Mes** y **Luna** están emparentados desde muy antiguo. El latín *mensis*, «mes», y el griego *mḗn*, «mes», y *mḗnē*, «Luna», vienen de una misma raíz indoeuropea relacionada con «medir»: la Luna fue el primer reloj para medir el tiempo largo. En inglés se ve aún más claro: *moon* y *month*. **Lunes** es el «día de la Luna», del latín *dies Lunae*. **Fase** viene del griego *phásis*, «aparición», del verbo *phaínein*, «mostrar, hacer visible»: cada fase es una forma de aparecer.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: fracciones y porcentajes (35-40 min)

**Qué es una fracción.** Una **fracción** $a/b$ expresa una parte de un todo. El número de abajo, el **denominador**, dice en cuántas partes iguales se divide el todo; el de arriba, el **numerador**, cuántas de esas partes se toman. En $3/4$, el todo se divide en cuatro partes y se toman tres. Una fracción es también una división: $3/4 = 3 \div 4 = 0{,}75$.

**Fracciones equivalentes.** Si multiplicas o divides el numerador y el denominador por el mismo número, la fracción no cambia: $1/2 = 2/4 = 50/100$. Es como cortar cada trozo de una tarta en dos: tienes el doble de trozos, cada uno de la mitad de tamaño, y la misma cantidad de tarta. **Simplificar** una fracción es dividir arriba y abajo por un número común hasta que no se pueda más: $15/100 = 3/20$, dividiendo los dos entre 5.

**Porcentajes.** Un **porcentaje** es una fracción de denominador 100: $0{,}25 = 25/100 = 25\,\%$. Para pasar de una fracción o un decimal a porcentaje se multiplica por 100; para el camino inverso, se divide. Los porcentajes sirven para comparar partes de todos distintos con una misma medida.

**Dos fracciones que se confunden.** Las fases de la Luna se describen con dos fracciones distintas, y es fácil confundirlas:

- la fracción **del ciclo** transcurrida, desde luna nueva hasta la siguiente (de 0 a 1),
- la fracción **del disco** iluminada (de 0 a 1).

El **cuarto creciente** ocurre cuando ha pasado una cuarta parte del ciclo, y en ese momento está iluminada la **mitad** del disco. El nombre se refiere al ciclo, no al disco: «cuarto» porque es el primer cuarto del mes lunar.

:::note[De dónde viene la palabra]
**Fracción** viene del latín *fractio*, «rotura», de *frangere*, «romper» (como *fractura* o *fragmento*): un número roto en partes. **Numerador** viene de *numerare*, «contar»: cuenta cuántas partes hay. **Denominador** viene de *denominare*, «dar nombre»: el número de abajo da nombre a las partes (tercios, cuartos, quintos...). **Porcentaje** viene de *por ciento*, del latín *per centum*, «por cada cien». El símbolo % surgió de abreviar a mano la expresión italiana *per cento*.
:::

**Ejercicios**

1. ¿Qué porcentaje del ciclo han transcurrido cuando la Luna tiene 10 días de edad (un ciclo dura 29,53 días)?
2. Un disco tiene el 85 % iluminado. ¿Qué fracción queda en sombra? Exprésala como fracción simplificada.
3. Si en un cuarto creciente se ve iluminada la mitad del disco, ¿qué fracción del disco estará iluminada una semana más tarde, en luna llena?
4. Calcula $\tfrac{1}{4} \cdot 29{,}53$ y compáralo con la edad del cuarto creciente que da el cuaderno (7,38 d).

<details>
<summary>Soluciones</summary>

1. 10 / 29,53 ≈ 0,339 = **33,9 %**.
2. 100 % − 85 % = 15 % = 15/100 = **3/20** (dividiendo arriba y abajo entre 5).
3. Todo el disco: **1** (100 %). Del cuarto (la mitad) a la llena (todo) hay una semana, y ahí la fracción iluminada pasa de 1/2 a 1.
4. 29,53 / 4 = **7,38 días**: coincide.

</details>

### Sesión 2 · Matemáticas: ángulos proporcionales al tiempo (30-40 min)

**La elongación.** La posición de la Luna respecto al Sol se describe con un ángulo, la **elongación** $\varepsilon$ (la letra griega épsilon): el ángulo que forman, vistas desde la Tierra, la dirección hacia el Sol y la dirección hacia la Luna. Vale 0° en luna nueva, cuando la Luna está en la misma dirección que el Sol, y 180° en luna llena, cuando está justo en la dirección opuesta.

**Proporcional al tiempo.** Si una cantidad avanza siempre al mismo ritmo, lo que ha avanzado es proporcional al tiempo que ha pasado: en el doble de tiempo, el doble de recorrido. Es una función lineal, como en la semana 4, con ordenada en el origen cero. Como el ciclo completo son 360° y dura 29,53 días, la elongación (en el modelo sencillo, con un ritmo constante) es

$$\varepsilon = 360^\circ \cdot \frac{\text{edad}}{29{,}53},$$

donde la **edad** de la Luna son los días transcurridos desde la última luna nueva. La fracción $\text{edad}/29{,}53$ es la fracción del ciclo de la sesión 1, y multiplicarla por 360° la convierte en un ángulo. El ritmo es $360/29{,}53 \approx 12{,}2^\circ$ por día.

**La fracción iluminada.** La fracción del disco iluminada se calcula con la fórmula $k = (1 - \cos\varepsilon)/2$. El coseno lo estudiarás en la semana 7; por ahora basta con comprobar con la calculadora que da 0, 0,5 y 1 en 0°, 90° y 180°, que es lo que esperas en luna nueva, cuarto y llena. Fíjate en que la fracción iluminada **no** crece de forma proporcional al tiempo: a los 45° (una octava parte del ciclo) solo está iluminado un 15 % del disco, no un 25 %.

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

### Sesión 3 · Física: geometría Sol–Tierra–Luna (35-45 min)

**Siempre media Luna iluminada.** La Luna no emite luz propia: refleja la del Sol, como cualquier piedra. Y una esfera iluminada desde un lado tiene siempre iluminada exactamente una mitad, la que mira al Sol. Haz la prueba en una habitación a oscuras con una lámpara y una pelota: la pelota siempre tiene media cara iluminada, pero según desde dónde la mires ves toda esa cara, una parte o nada. Lo que cambia a lo largo del mes es **cuánto de esa mitad vemos desde la Tierra**, y eso depende de la elongación.

**Las fases, una a una.** Con el Sol muy lejos a un lado, la Tierra en el centro y la Luna dando vueltas a su alrededor en sentido contrario a las agujas del reloj (vista desde el norte):

- **Luna nueva** (ε = 0°): la Luna está entre la Tierra y el Sol, y su mitad iluminada mira hacia el lado contrario al nuestro. No la vemos, y además sale y se pone con el Sol, así que está en el cielo de día, perdida en su resplandor.
- **Creciente** (entre 0° y 90°): vemos un borde iluminado, cada día más ancho. Se ve al atardecer, hacia el oeste.
- **Cuarto creciente** (ε = 90°): vemos la mitad del disco iluminada. Como está 90° al este del Sol, y el cielo gira 90° en unas 6 horas, sale unas 6 horas después que el Sol, hacia el mediodía, y se pone hacia la medianoche.
- **Gibosa creciente** (entre 90° y 180°): más de medio disco iluminado.
- **Luna llena** (ε = 180°): la Tierra está entre el Sol y la Luna, y vemos toda la mitad iluminada. Está justo opuesta al Sol: sale al ponerse el Sol y se pone al salir el Sol. Es la única fase que se ve toda la noche.
- **Gibosa menguante**, **cuarto menguante** (ε = 270°, sale hacia la medianoche y se pone hacia el mediodía) y **menguante**, de madrugada, hasta volver a la luna nueva.

**Dos meses distintos.** Ocurre lo mismo que con el día solar y el sidéreo de la semana 4. La Luna da una vuelta a la Tierra respecto a las estrellas en 27,32 días: el **mes sidéreo**. Pero las fases tardan 29,53 días en repetirse: el **mes sinódico**, unos dos días más. La razón es que, mientras la Luna da su vuelta, la Tierra avanza en su órbita y el Sol se desplaza en el cielo casi 1° al día: a lo largo de un mes sinódico, unos 29°. Para volver a la misma posición respecto al Sol, la Luna tiene que recorrer esos 29° de más, y a su ritmo de unos 13° al día respecto a las estrellas eso le cuesta algo más de dos días.

**Por qué sale unos 50 minutos más tarde cada día.** La Luna se desplaza respecto al Sol unos 12,2° al día hacia el este, y como el cielo gira 1° cada 4 minutos, el cielo tiene que girar ese ángulo de más para traerla de nuevo al horizonte: $12{,}2 \cdot 4 \approx 49$ minutos. Es un promedio; según la época del año, el retraso real varía bastante.

**Por qué no hay eclipse todos los meses.** Un eclipse de Sol ocurre cuando la sombra de la Luna cae sobre la Tierra, y un eclipse de Luna, cuando la sombra de la Tierra cae sobre la Luna. Las dos cosas solo pueden pasar con los tres cuerpos alineados: en luna nueva y en luna llena. Pero la órbita de la Luna está inclinada unos 5° respecto al plano de la órbita terrestre, así que normalmente la Luna pasa un poco por encima o por debajo de la línea Sol-Tierra, y las sombras no se tocan. Solo hay eclipse cuando la luna nueva o la llena coinciden con uno de los dos puntos donde la órbita de la Luna cruza el plano de la de la Tierra. Eso pasa en dos temporadas al año, y por eso hay entre cuatro y siete eclipses al año, no veinticuatro.

:::note[De dónde viene la palabra]
**Creciente** y **menguante** vienen del latín *crescere*, «crecer», y *minuere*, «disminuir» (de la misma raíz que *menos* y *minúsculo*). **Gibosa** viene de *gibbus*, «joroba»: una Luna abombada, con más de medio disco iluminado. **Elongación** viene de *elongare*, «alejar»: lo que un astro se aleja del Sol en el cielo.
:::

**Qué hacer**

1. Explica con un dibujo, sin consultar, las fases de la lista anterior con las posiciones de Sol, Tierra y Luna vistas desde arriba.
2. Haz la prueba de la lámpara y la pelota: sostén la pelota con el brazo extendido, gira sobre ti mismo y mira cómo cambia la parte iluminada.
3. Para el dibujo, el vídeo de NASA (recurso 1) muestra cómo cambia la vista de la mitad iluminada.

### Sesión 4 · Astronomía y observación (30-45 min)

**En el cielo.** Durante una semana, a la misma hora, dibuja la Luna y la posición que ocupa respecto a una referencia del paisaje (un edificio, un árbol). Anota la fecha, la hora, la forma, y si puedes, a qué hora sale o se pone. Con ello comprobarás el retraso diario.

**La luz cenicienta.** En los días cercanos a la luna nueva, cuando la Luna es un creciente muy fino al atardecer, fíjate en el resto del disco: se ve en un gris tenue. Es luz del Sol reflejada por la Tierra que ilumina la parte oscura de la Luna y vuelve hacia nosotros. Leonardo da Vinci lo explicó así a principios del siglo XVI. Vista desde la Luna, la Tierra estaría entonces casi «llena».

**En Stellarium.**

1. Fija tu lugar y avanza la fecha de un día en un día durante un mes. Anota la forma de la Luna y su hora de salida.
2. Anota la fecha de las cuatro fases principales (nueva, cuarto creciente, llena y cuarto menguante).
3. Tras la sesión 5, compara esas fechas con las del modelo.

En el hemisferio norte la Luna creciente se ilumina por la derecha y la menguante por la izquierda; en el hemisferio sur es al revés. Una regla orientativa para el hemisferio norte: una Luna iluminada por la derecha, con forma de «D», es creciente, y una iluminada por la izquierda, con forma de «C», es menguante. No es una definición, solo un recordatorio.

No mires nunca al Sol directamente.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 5:

- calcula la edad de la Luna a partir de una luna nueva de referencia y el periodo sinódico,
- calcula la elongación y la fracción iluminada,
- dibuja la forma del disco iluminado para cualquier edad,
- obtiene la fase de la fecha que elijas y estima la próxima luna llena.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-05.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-05.ipynb)

El modelo supone que la Luna se mueve con regularidad. En realidad su velocidad varía (su órbita es una elipse, y va más deprisa cuando está más cerca de la Tierra, como verás en la semana 14), y las fases reales pueden adelantarse o retrasarse hasta unas 14 horas respecto al modelo. Mide ese desfase con Stellarium.

## Qué has aprendido

- **La respuesta.** La Luna siempre tiene la mitad iluminada, pero desde la Tierra vemos una parte distinta de ella según el ángulo entre la Luna y el Sol. Ese ángulo crece 360° en 29,53 días.
- **La causa.** La Luna orbita la Tierra y la Tierra orbita el Sol, y la fase depende solo de la geometría de las tres posiciones, no de la sombra de la Tierra. La sombra solo interviene en los eclipses, que exigen además que la Luna cruce el plano de la órbita terrestre.
- **Las herramientas.** Fracciones, fracciones equivalentes y porcentajes (cuidado con «cuarto»), proporcionalidad entre tiempo y ángulo, y un modelo de ciclo medio que se puede contrastar con una medida independiente.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Our World: Moon Phases, NASA Science (eClips)](https://science.nasa.gov/eclips/videos/moon-phases/). Inglés, vídeo educativo con animaciones y preguntas de discusión; la página no indica la duración del vídeo. Verificado el 31 de octubre de 2026.
2. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
3. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las fases dibujadas en el cuaderno son de elaboración propia.
