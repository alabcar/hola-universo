---
title: "Semana 13 · ¿Por qué algunos planetas parecen ir hacia atrás?"
description: "Fase 2 · Órbitas. Seno y coseno en la circunferencia, movimiento circular, velocidad angular, periodo sinódico y movimiento retrógrado."
sidebar:
  order: 13
  label: "13. ¿Por qué algunos planetas parecen ir hacia atrás?"
---

## La pregunta del cielo

Si apuntas cada semana la posición de Marte respecto a las estrellas de fondo, verás que casi siempre avanza hacia el este, poco a poco. Pero una vez cada dos años, más o menos, se frena, se para, retrocede hacia el oeste durante unos dos meses, vuelve a pararse y sigue su camino. Dibuja un bucle en el cielo.

Durante casi dos mil años, este bucle fue el gran problema de la astronomía. El modelo de Ptolomeo (siglo II), con la Tierra quieta en el centro, lo explicaba añadiendo círculos sobre círculos: los **epiciclos**. Funcionaba, pero era complicado. En 1543 Copérnico propuso algo más sencillo: el Sol en el centro y la Tierra como un planeta más. Con esa idea, el bucle deja de ser un misterio y se convierte en un efecto de perspectiva.

Esta semana vas a demostrarlo con matemáticas. Necesitas describir un movimiento circular con números (seno, coseno y velocidad angular) y combinar dos de ellos: el de la Tierra y el de Marte.

:::note[De dónde viene la palabra]
**Planeta** viene del griego *planḗtēs*, «errante, vagabundo», del verbo *planáomai*, «andar sin rumbo». Para los griegos, las estrellas eran fijas y unos pocos puntos de luz «vagaban» entre ellas: el Sol, la Luna, Mercurio, Venus, Marte, Júpiter y Saturno. **Retrógrado** viene del latín *retrogradus*: *retro*, «hacia atrás», y *gradi*, «caminar». El movimiento normal, hacia el este, se llama **directo** o **prógrado**.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: seno y coseno en la circunferencia (35-45 min)

**Punto de partida.** En la fase 1 usaste el seno y el coseno en triángulos rectángulos: en un triángulo con un ángulo $\theta$, el seno es el cateto opuesto dividido por la hipotenusa y el coseno, el cateto contiguo dividido por la hipotenusa. Esa definición solo sirve para ángulos entre 0° y 90°, porque un triángulo rectángulo no puede tener un ángulo de 120°. Para describir algo que gira y da vueltas completas hace falta una definición que funcione con cualquier ángulo.

**La circunferencia unidad.** Dibuja unos ejes $x$ e $y$ y una circunferencia de radio 1 con el centro en el origen. Desde el eje $x$ positivo, gira un ángulo $\theta$ en sentido contrario a las agujas del reloj (por convenio, ese es el sentido positivo). Llegas a un punto $P$ de la circunferencia. Por definición:

$$\cos\theta = \text{coordenada } x \text{ de } P, \qquad \sin\theta = \text{coordenada } y \text{ de } P.$$

Si el ángulo está entre 0° y 90°, esto coincide con la definición del triángulo: el radio es la hipotenusa (vale 1), la $x$ es el cateto contiguo y la $y$, el opuesto. Pero ahora vale para cualquier ángulo:

- A 90° estás arriba del todo: $P = (0, 1)$, así que $\cos 90^\circ = 0$ y $\sin 90^\circ = 1$.
- A 180° estás a la izquierda: $P = (-1, 0)$, así que $\cos 180^\circ = -1$ y $\sin 180^\circ = 0$.
- A 270° estás abajo: $\cos 270^\circ = 0$, $\sin 270^\circ = -1$.
- A 360° vuelves al principio, y todo se repite. Por eso se dice que el seno y el coseno son funciones **periódicas**, con periodo 360°.

El seno y el coseno pueden ser negativos: solo indican hacia qué lado del eje estás. Y como $P$ está en una circunferencia de radio 1, por el teorema de Pitágoras siempre se cumple $\cos^2\theta + \sin^2\theta = 1$.

**Si el radio no es 1**, todo se multiplica por el radio: un punto a distancia $r$ del centro y con ángulo $\theta$ tiene coordenadas

$$x = r\cos\theta, \qquad y = r\sin\theta.$$

Esta es la herramienta de la semana: con un radio y un ángulo sabes dónde está un planeta en un plano.

**Radianes, otra vez.** En la semana 2 viste que un radián es el ángulo cuyo arco mide lo mismo que el radio, y que una vuelta son $2\pi$ radianes. Python, y casi toda la física, trabaja en radianes: `np.cos(np.pi)` vale $-1$, pero `np.cos(180)` no es el coseno de 180°.

:::note[De dónde viene la palabra]
**Seno** tiene una historia enrevesada. Los matemáticos indios lo llamaban *jyā*, «cuerda de arco». Los árabes lo transcribieron como *jiba*, que en la escritura árabe sin vocales se confundía con *jaib*, «bolsillo, pliegue». En el siglo XII se tradujo al latín como *sinus*, que significa «pliegue, bahía». **Coseno** es una abreviatura de *complementi sinus*, «seno del complemento», porque $\cos\theta = \sin(90^\circ - \theta)$. **Radián** viene de radio, del latín *radius*, «rayo, varilla de rueda».
:::

**Ejercicios**

1. Sin calculadora, di el signo del seno y del coseno de 135°, 200° y 300°. Pista: ¿en qué cuadrante está cada ángulo?
2. Pasa a radianes 90°, 45° y 30°. Pasa a grados $\pi/3$ y $3\pi/2$.
3. Un punto está a 5 unidades del origen con un ángulo de 210°. ¿Cuáles son sus coordenadas?
4. Un punto tiene coordenadas $(-1, 1)$. ¿A qué distancia está del origen y con qué ángulo?

<details>
<summary>Soluciones</summary>

1. 135° está en el segundo cuadrante (arriba a la izquierda): **coseno negativo, seno positivo**. 200° está en el tercero (abajo a la izquierda): **los dos negativos**. 300° está en el cuarto (abajo a la derecha): **coseno positivo, seno negativo**.
2. 90° = $\pi/2$, 45° = $\pi/4$, 30° = $\pi/6$. $\pi/3$ = 60° y $3\pi/2$ = 270°.
3. $x = 5\cos 210^\circ = 5 \cdot (-0{,}866) \approx$ **−4,33**, $y = 5\sin 210^\circ = 5 \cdot (-0{,}5) =$ **−2,5**.
4. Distancia $\sqrt{1 + 1} = \sqrt{2} \approx$ **1,41**. Está arriba a la izquierda, en la diagonal, así que el ángulo es **135°**.

</details>

### Sesión 2 · Matemáticas: el movimiento circular uniforme (30-40 min)

Un cuerpo que recorre una circunferencia siempre a la misma rapidez hace un **movimiento circular uniforme**. Si tarda un tiempo $T$ (el **periodo**) en dar una vuelta, el ángulo que gira por unidad de tiempo es siempre el mismo. Se llama **velocidad angular** y se escribe con la letra griega omega:

$$\omega = \frac{360^\circ}{T} \quad \text{o, en radianes,} \quad \omega = \frac{2\pi}{T}.$$

Si en el instante $t = 0$ el cuerpo estaba en el ángulo $\theta_0$, en el instante $t$ estará en $\theta(t) = \theta_0 + \omega t$, y su posición será

$$x(t) = r\cos(\theta_0 + \omega t), \qquad y(t) = r\sin(\theta_0 + \omega t).$$

Dos fórmulas y cuatro números ($r$, $T$, $\theta_0$ y el tiempo) describen el movimiento completo. Es una idealización: las órbitas reales son elipses (semana 14), pero para casi todos los planetas la diferencia es pequeña.

**Velocidad angular y velocidad lineal.** Si el cuerpo gira un ángulo $\Delta\theta$ en radianes, recorre un arco de longitud $r\,\Delta\theta$ (es la definición de radián). Por tanto su rapidez a lo largo de la circunferencia es $v = r\,\omega$. Dos planetas pueden tener la misma velocidad angular y rapideces distintas, si están a distinta distancia.

**Ejemplo.** La Tierra da una vuelta al Sol en 365,25 días: $\omega = 360^\circ / 365{,}25\ \text{d} \approx 0{,}986^\circ$ por día, casi un grado al día. Marte tarda 687 días: $\omega \approx 0{,}524^\circ$ por día. La Tierra gira casi el doble de rápido.

**Ejercicios**

1. Calcula la velocidad angular de Venus, que tarda 224,7 días, en grados por día.
2. La Tierra está a 1,496 × 10⁸ km del Sol. ¿A qué rapidez se mueve en su órbita, en km/s? (Un año son 3,156 × 10⁷ s.)
3. Un punto gira con $r = 2$, $T = 8$ s y empieza en $\theta_0 = 0$. ¿Dónde está en $t = 2$ s? ¿Y en $t = 3$ s?

<details>
<summary>Soluciones</summary>

1. $360 / 224{,}7 \approx$ **1,602° por día**.
2. $v = 2\pi r / T = 2\pi \cdot 1{,}496\times10^{8} / 3{,}156\times10^{7} \approx$ **29,8 km/s**, unos 107 000 km/h.
3. $\omega = 360^\circ/8 = 45^\circ$ por segundo. En $t = 2$ s el ángulo es 90°: el punto está en **(0, 2)**. En $t = 3$ s es 135°: $(2\cos 135^\circ, 2\sin 135^\circ) \approx$ **(−1,41, 1,41)**.

</details>

### Sesión 3 · Física: velocidad angular relativa y periodo sinódico (30-40 min)

**Dos relojes distintos.** El tiempo que tarda un planeta en dar una vuelta completa al Sol, medido respecto a las estrellas, es su **periodo sidéreo** (del latín *sidus, sideris*, «estrella»). Pero desde la Tierra no vemos eso directamente: vemos cuándo se repite la misma configuración Sol-Tierra-planeta. Por ejemplo, cuánto pasa entre dos **oposiciones** de Marte, cuando Marte está justo al lado contrario del Sol en nuestro cielo. Ese tiempo es el **periodo sinódico** (del griego *sýnodos*, «reunión, encuentro»).

**El razonamiento de los dos corredores.** Piensa en dos corredores en una pista circular. El de dentro (la Tierra) da una vuelta cada $T_1$ y el de fuera (Marte), cada $T_2$, más lento. Cada día, el de dentro gana sobre el de fuera un ángulo igual a la diferencia de sus velocidades angulares:

$$\omega_\text{rel} = \omega_1 - \omega_2 = \frac{360^\circ}{T_1} - \frac{360^\circ}{T_2}.$$

Vuelven a estar alineados cuando el de dentro le ha sacado una vuelta entera (360°) al de fuera. Ese tiempo, el periodo sinódico $S$, cumple $\omega_\text{rel}\,S = 360^\circ$. Dividiendo todo entre 360°:

$$\frac{1}{S} = \frac{1}{T_1} - \frac{1}{T_2}.$$

Para la Tierra y Marte: $1/S = 1/365{,}25 - 1/687{,}0 = 0{,}0027379 - 0{,}0014556 = 0{,}0012823$ por día, así que $S \approx$ **780 días**, unos dos años y dos meses. Es el ritmo de las oposiciones de Marte, de sus bucles retrógrados y de las ventanas de lanzamiento de las misiones a Marte (semana 18).

**Por qué hay bucle.** En la oposición, la Tierra y Marte están del mismo lado del Sol y la Tierra, que va por dentro y más rápido, adelanta a Marte. Como cuando adelantas a un coche más lento en la autopista: aunque los dos vais hacia delante, a ti te parece que el otro va hacia atrás respecto al paisaje del fondo. Aquí el paisaje son las estrellas. Lejos de la oposición, la Tierra está al otro lado del Sol y ya no adelanta a Marte de forma visible: Marte vuelve a avanzar sobre el fondo.

Para los planetas interiores (Mercurio y Venus) ocurre lo mismo, pero el que adelanta es el planeta: su bucle se produce cerca de la **conjunción inferior**, cuando pasa entre la Tierra y el Sol.

**Qué hacer**

1. Calcula el periodo sinódico de Júpiter (periodo sidéreo 4332,6 días). ¿Por qué se parece tanto a un año?
2. Para un planeta interior la fórmula es $1/S = 1/T_\text{planeta} - 1/T_\text{Tierra}$. Calcula el de Venus (224,7 días).
3. Explica con tus palabras por qué un planeta muy lejano, como Neptuno, tiene un periodo sinódico de solo un año y dos días.

<details>
<summary>Soluciones</summary>

1. $1/S = 1/365{,}25 - 1/4332{,}6 = 0{,}0027379 - 0{,}0002308 = 0{,}0025071$, así que $S \approx$ **399 días**. Júpiter se mueve tan despacio que la Tierra casi lo «encuentra» en el mismo sitio al cabo de un año: solo hace falta un mes más para alcanzarlo.
2. $1/S = 1/224{,}7 - 1/365{,}25 = 0{,}0044504 - 0{,}0027379 = 0{,}0017125$, así que $S \approx$ **584 días**.
3. Neptuno tarda casi 165 años en dar la vuelta. En un año apenas se mueve unos 2°, así que la Tierra, tras su vuelta completa, solo necesita un par de días más para volver a alinearse con él.

</details>

### Sesión 4 · Astronomía y observación: seguir un planeta (30-45 min)

**Con Stellarium.** Abre Stellarium (web o escritorio) y busca Marte. Activa los nombres de las estrellas y de las constelaciones y cambia la fecha en la ventana de fecha y hora (en la versión de escritorio se abre con F5). En la versión de escritorio, las teclas `]` y `[` avanzan y retroceden una semana; si no te funcionan, mira la lista de atajos en la ayuda (F1). Para ver el bucle con claridad, deja siempre la misma hora (por ejemplo, las 00:00) y cambia solo la fecha.

Marte llega a la oposición el **19 de febrero de 2027**, en la constelación de Leo. Su bucle retrógrado se extiende unas semanas antes y después de esa fecha. En Stellarium:

1. Pon la fecha del 1 de noviembre de 2026 y anota la posición de Marte respecto a las estrellas de Leo.
2. Avanza de dos en dos semanas hasta mayo de 2027 y apunta cada vez su posición en un dibujo.
3. Marca las dos fechas en las que Marte parece detenerse (los **puntos estacionarios**) y comprueba que la oposición queda entre las dos.

**A simple vista.** Desde finales de 2026, Marte se ve después de medianoche como un punto anaranjado que no centellea tanto como las estrellas. A medida que se acerca la oposición, sale cada vez más pronto y brilla más. Si tienes paciencia, apunta su posición respecto a las estrellas cercanas una noche despejada cada dos semanas: es exactamente lo que hacían los astrónomos antiguos, y funciona bien incluso con un cielo urbano luminoso, porque Marte es muy brillante.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 13:

- dibuja puntos en la circunferencia unidad para que veas el seno y el coseno como coordenadas,
- mueve la Tierra y Marte en órbitas circulares con las fórmulas de la sesión 2,
- calcula en qué dirección se ve Marte desde la Tierra día a día y dibuja su **longitud** sobre el fondo de estrellas, donde aparece el retroceso,
- mide en la simulación la duración del retroceso y el tiempo entre dos bucles, y lo compara con el periodo sinódico calculado a mano.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-13.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-13.ipynb)

## Qué has aprendido

- **La respuesta.** Los planetas no retroceden: es un efecto de perspectiva. Cuando la Tierra, que va por dentro y más rápido, adelanta a un planeta exterior, ese planeta parece moverse hacia atrás respecto a las estrellas de fondo. Ocurre alrededor de la oposición, una vez cada periodo sinódico.
- **El trasfondo histórico.** Explicar el bucle sin mover la Tierra exigía epiciclos. Con el Sol en el centro, el bucle sale solo. Fue uno de los argumentos más fuertes a favor del modelo de Copérnico.
- **Las herramientas.** El seno y el coseno como coordenadas en la circunferencia, válidos para cualquier ángulo; la posición $(r\cos\theta, r\sin\theta)$; la velocidad angular $\omega = 2\pi/T$ y la relación $v = r\omega$; y la fórmula del periodo sinódico, $1/S = 1/T_1 - 1/T_2$.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Marte y Júpiter, *Física: de observadores de estrellas a naves espaciales* (CK-12, LibreTexts en español)](https://espanol.libretexts.org/Bookshelves/Educacion_Basica/Libro%3A_Fisica_-_De_Stargazers_a_Starships_(CK-12)/23%3A_Los_Planetas/23.02%3A_Marte_y_J%C3%BApiter). Español, nivel divulgativo; explica por qué los planetas exteriores retroceden cerca de la oposición y los interiores, cerca de la conjunción inferior. Verificado el 6 de noviembre de 2026.
2. [Oposición, glosario de la Oficina de Astronomía para la Educación de la UAI (astro4edu)](https://astro4edu.org/es/resources/glossary/term/228/). Español; definición breve de oposición y su relación con el movimiento retrógrado. Verificado el 6 de noviembre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

La fecha de la oposición de Marte (19 de febrero de 2027) la he comprobado en varias fuentes de divulgación astronómica el 6 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
