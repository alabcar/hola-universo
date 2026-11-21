---
title: "Semana 44 · ¿Qué cambia cuando algo va muy rápido?"
description: "Fase 4 · El universo grande. Álgebra con raíces y el factor de Lorentz, el reloj de luz y el teorema de Pitágoras, los postulados de la relatividad especial, la dilatación del tiempo y la contracción de longitudes, la energía relativista, los muones de los rayos cósmicos, el GPS y una cámara de niebla casera."
sidebar:
  order: 44
  label: "44. ¿Qué cambia cuando algo va muy rápido?"
---

## La pregunta del cielo

Ahora mismo, mientras lees esto, te atraviesan decenas de partículas por segundo llegadas del espacio. Son **muones**, unas partículas parecidas al electrón pero unas doscientas veces más pesadas, que se crean a unos 15 km de altura cuando los rayos cósmicos chocan con el aire. Un muon vive, de media, 2,2 millonésimas de segundo antes de desintegrarse. En ese tiempo, incluso a la velocidad de la luz, solo recorrería unos 660 metros. Y, sin embargo, llegan al suelo a miles.

La explicación la dio un empleado de una oficina de patentes de Berna, de 26 años, en 1905: Albert Einstein. Para un objeto que se mueve muy deprisa, el tiempo pasa más despacio. No es una ilusión ni un defecto de los relojes: el tiempo mismo es distinto según cómo te muevas. Esta semana, con poco más que el teorema de Pitágoras, entiendes por qué.

:::note[De dónde viene la palabra]
**Relatividad** viene de *relativus*, «que se refiere a otra cosa»: en la teoría de Einstein, el tiempo y las distancias se miden siempre respecto a un observador. (Einstein habría preferido llamarla «teoría de los invariantes», porque lo importante es lo que no cambia, como la velocidad de la luz.) **Muon** viene de la letra griega *mu* ($\mu$) y la terminación *-ón* de *electrón*: lo descubrieron Carl Anderson y Seth Neddermeyer en 1936, en los rayos cósmicos. **Éter** viene del griego *aithḗr*, «el aire puro de las alturas»: el medio invisible por el que se creía que viajaba la luz.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: el factor de Lorentz (35-45 min)

**Una fórmula que aparece en todas partes.** En la relatividad especial casi todo depende de un número, el **factor de Lorentz**:

$$\gamma = \frac{1}{\sqrt{1 - \dfrac{v^2}{c^2}}} = \frac{1}{\sqrt{1 - \beta^2}}, \qquad \beta = \frac{v}{c}.$$

$\beta$ (la letra griega beta) es la velocidad como fracción de la de la luz. Algunas propiedades que conviene ver con calma:

- Si $v = 0$, $\gamma = 1$. Para cualquier velocidad, $\gamma \geq 1$.
- Al acercarse $v$ a $c$, el denominador se acerca a cero y $\gamma$ crece sin límite. Para $v = c$ no está definido: ningún objeto con masa puede llegar a la velocidad de la luz.
- Para velocidades pequeñas, con la aproximación binomial de la semana 21, $(1 - \beta^2)^{-1/2} \approx 1 + \tfrac{1}{2}\beta^2$. Así que $\gamma - 1 \approx \tfrac{1}{2}\beta^2$: diminuto para todo lo cotidiano.

**Despejar.** A veces se conoce $\gamma$ y se quiere la velocidad. Elevando al cuadrado e invirtiendo, $1 - \beta^2 = 1/\gamma^2$, así que

$$\beta = \sqrt{1 - \frac{1}{\gamma^2}}.$$

**Ejercicios**

1. Calcula $\gamma$ para $\beta = 0{,}6$, $0{,}8$, $0{,}99$ y $0{,}999$.
2. ¿A qué velocidad hay que ir para que $\gamma = 2$? ¿Y para $\gamma = 10$?
3. Un avión de pasajeros va a 900 km/h (250 m/s). Calcula $\gamma - 1$ con la aproximación binomial.

<details>
<summary>Soluciones</summary>

1. $1/\sqrt{0{,}64} =$ **1,25**; $1/\sqrt{0{,}36} \approx$ **1,667**; $1/\sqrt{0{,}0199} \approx$ **7,09**; $1/\sqrt{0{,}001999} \approx$ **22,4**.
2. $\beta = \sqrt{1 - 1/4} \approx$ **0,866**; $\sqrt{1 - 1/100} \approx$ **0,995**.
3. $\beta = 250/3\times10^8 \approx 8{,}3\times10^{-7}$; $\gamma - 1 \approx \tfrac{1}{2}(8{,}3\times10^{-7})^2 \approx$ **3,5 × 10⁻¹³**.

</details>

### Sesión 2 · Matemáticas: el reloj de luz y Pitágoras (35-45 min)

**Un reloj sencillísimo.** Imagina un reloj formado por dos espejos paralelos, separados una distancia $L$, con un destello de luz que rebota entre ellos. Cada ida y vuelta es un «tic». Para alguien que viaja con el reloj, la luz recorre $2L$ en cada tic, que dura

$$\Delta\tau = \frac{2L}{c}.$$

Es el **tiempo propio**: el que marca el reloj para quien va con él.

**Visto desde fuera.** Ahora el reloj pasa por delante de ti a una velocidad $v$, moviéndose en horizontal mientras la luz rebota en vertical. Desde tu punto de vista, mientras la luz sube del espejo de abajo al de arriba, el reloj se ha desplazado: la luz recorre una **diagonal**. Si el viaje de ida dura para ti $\Delta t/2$, el reloj avanza $v\,\Delta t/2$ y la luz recorre $c\,\Delta t/2$. Por el teorema de Pitágoras (semana 7), con la altura $L$ como el otro cateto:

$$\left(\frac{c\,\Delta t}{2}\right)^2 = L^2 + \left(\frac{v\,\Delta t}{2}\right)^2.$$

Aquí está la clave de todo: **la luz va a la misma velocidad $c$ para ti que para el viajero** (el segundo postulado de la sesión 3). Como la diagonal es más larga que la altura y la velocidad es la misma, el tic dura más para ti. Despejando $\Delta t$:

$$\frac{\Delta t^2}{4}(c^2 - v^2) = L^2 \quad\Longrightarrow\quad \Delta t = \frac{2L}{c}\,\frac{1}{\sqrt{1 - v^2/c^2}} = \gamma\,\Delta\tau.$$

**El reloj que se mueve atrasa** en un factor $\gamma$. Y no es cosa de este reloj en particular: si los demás relojes del viajero (su reloj de pulsera, su corazón, sus muones) no atrasaran igual, el viajero podría saber que se mueve comparándolos, lo que contradice el primer postulado. Es el tiempo mismo el que pasa más despacio.

**Ejercicios**

1. Un muon vive 2,2 µs en su propio tiempo y viaja a $\beta = 0{,}9995$. ¿Cuánto vive visto desde el suelo? ¿Qué distancia recorre en ese tiempo?
2. Si $L = 1{,}5$ m, ¿cuánto dura un tic en el reloj de luz en reposo?
3. Repite el razonamiento para un tren que va a 300 km/h: ¿cuánto atrasa un reloj del tren al cabo de un año?

<details>
<summary>Soluciones</summary>

1. $\gamma = 1/\sqrt{1 - 0{,}9995^2} \approx 31{,}6$. Vive $2{,}2 \cdot 31{,}6 \approx$ **70 µs**, y recorre $0{,}9995 \cdot 3\times10^8 \cdot 70\times10^{-6} \approx$ **21 km**: suficiente para llegar al suelo.
2. $3/(3\times10^8) =$ **10 nanosegundos**.
3. $\beta \approx 2{,}8\times10^{-7}$, $\gamma - 1 \approx 3{,}9\times10^{-14}$; en un año ($3{,}16\times10^7$ s), unos **1,2 microsegundos**.

</details>

### Sesión 3 · Física: la relatividad especial (40-45 min)

**El problema del éter.** En el siglo XIX se pensaba que la luz, como el sonido, necesitaba un medio en el que propagarse, el **éter**, y que la Tierra se movía a través de él. Si era así, la velocidad de la luz medida en la Tierra debía variar un poco según la dirección, como notas el viento al correr. En 1887, Albert Michelson y Edward Morley lo midieron con un interferómetro (semana 27) capaz de detectar diferencias mínimas. No encontraron nada. La luz iba igual de deprisa en todas las direcciones.

**Los dos postulados (1905).** Einstein partió de dos principios:

1. **Las leyes de la física son las mismas para todos los observadores que se mueven a velocidad constante.** Ningún experimento, dentro de un tren sin ventanas que va suave y en línea recta, puede decirte si se mueve. Ya lo había dicho Galileo para la mecánica; Einstein lo extendió a toda la física.
2. **La velocidad de la luz en el vacío es la misma para todos esos observadores**, se muevan como se muevan respecto a la fuente.

El segundo parece imposible: si corres hacia un rayo de luz, ¿no debería venir hacia ti más deprisa? No. Y para que $c$ sea igual para todos, algo tiene que ceder: el tiempo y el espacio.

**Las consecuencias.**

- **Dilatación del tiempo**: un reloj que se mueve atrasa en un factor $\gamma$ (sesión 2).
- **Contracción de las longitudes**: un objeto que se mueve se ve más corto en la dirección del movimiento, en el mismo factor: $L = L_0/\gamma$.
- **La simultaneidad es relativa**: dos sucesos que son simultáneos para un observador pueden no serlo para otro que se mueve respecto al primero.
- **La energía**: un cuerpo de masa $m$ en reposo tiene una energía $E_0 = mc^2$ (la de la semana 34); moviéndose, $E = \gamma\,mc^2$. La energía cinética es $(\gamma - 1)\,mc^2$, que para velocidades pequeñas, con la aproximación binomial, es $\tfrac{1}{2}mv^2$: la fórmula de Newton (semana 12). Como $\gamma$ crece sin límite, acelerar algo hasta $c$ requeriría una energía infinita.

**Las pruebas.**

- **Los muones**: en 1941, Bruno Rossi y David Hall midieron cuántos muones llegaban a lo alto de una montaña y cuántos más abajo. Sin dilatación del tiempo, casi ninguno debería sobrevivir al descenso; llegaban muchos más, en la proporción que predice Einstein.
- **Los aceleradores**: en el Gran Colisionador de Hadrones del CERN, los protones van a más del 99,999999 % de la velocidad de la luz, con $\gamma$ de unos 7000. Los muones que se hacen girar en anillos de almacenamiento viven decenas de veces más de lo normal, como predice la teoría.
- **Los relojes en aviones**: en 1971, Joseph Hafele y Richard Keating dieron la vuelta al mundo en aviones comerciales con relojes atómicos y los compararon con los que se habían quedado en tierra. Las diferencias, de decenas o cientos de nanosegundos, coincidieron con la relatividad (la especial y la general, semana 45).
- **El GPS**: los relojes de los satélites, que se mueven a unos 3,9 km/s, atrasan por la relatividad especial unos 7 microsegundos al día; por la general, al estar más lejos de la Tierra, adelantan unos 45. En total, unos 38 µs al día. Si no se corrigiera, el error de posición crecería más de 10 km al día.

:::note[De dónde viene la palabra]
El **factor de Lorentz** lleva el nombre del físico neerlandés Hendrik Lorentz, que escribió las ecuaciones de la contracción antes que Einstein, en 1904, aunque las interpretaba como un efecto del éter sobre los objetos. **Postulado** viene del latín *postulare*, «pedir, reclamar»: algo que se pide que se acepte sin demostración, para construir sobre ello.
:::

**Qué hacer**

1. Una nave viaja a $0{,}8c$ hasta Próxima Centauri, a 4,24 años luz. ¿Cuánto dura el viaje para la Tierra? ¿Y para los viajeros?
2. Para los viajeros, ¿qué distancia hay hasta Próxima? (Pista: contracción de longitudes.) ¿Es coherente con su tiempo de viaje?
3. ¿Qué energía cinética tiene, en julios, una masa de 1 kg a $0{,}8c$? Compárala con $mc^2$.

### Sesión 4 · Astronomía y observación: los rayos cósmicos y una cámara de niebla (30-45 min)

**Partículas del espacio.** En 1912, el físico austriaco Victor Hess subió en globo hasta más de 5000 metros con un detector de radiación. Esperaba que la radiación disminuyera al alejarse del suelo (se creía que venía de las rocas). Aumentaba. Venía del espacio: los **rayos cósmicos**. Nobel de Física de 1936.

Los rayos cósmicos son sobre todo protones y núcleos atómicos que viajan casi a la velocidad de la luz. Muchos se aceleran en los restos de supernova de la semana 36; los más energéticos vienen de fuera de la galaxia, y su origen todavía se investiga, por ejemplo en el Observatorio Pierre Auger, en Argentina, que cubre 3000 km² con detectores. Cuando un rayo cósmico choca con un núcleo de la alta atmósfera, produce una **cascada** de partículas secundarias, entre ellas los muones. A nivel del mar, llega aproximadamente **un muon por centímetro cuadrado cada minuto**: por la palma de tu mano pasan varios por segundo.

**Construye una cámara de niebla.** Es el detector con el que se descubrieron el positrón y el muon, y se puede hacer en casa con material sencillo:

1. Un recipiente transparente con tapa (una pecera pequeña o una caja de plástico transparente), puesto boca abajo.
2. En el fondo de la caja (que queda arriba), una tira de fieltro o de esponja empapada de **alcohol isopropílico** de alta pureza (el de farmacia de 99 %).
3. La base de la cámara, una bandeja metálica pintada de negro mate, apoyada sobre **hielo seco** (dióxido de carbono sólido, a −78 °C).
4. Apaga la luz y alumbra de lado con una linterna potente.

Tras unos minutos, el alcohol se evapora arriba y cae hacia la base fría, donde forma una capa de vapor **sobresaturado**: a punto de condensarse. Cuando una partícula cargada la atraviesa, arranca electrones de las moléculas del aire y deja un rastro de iones sobre el que se condensan gotitas: verás estelas blancas y finas que aparecen y se desvanecen en un segundo. Las rectas y largas suelen ser muones; las cortas y gruesas, partículas alfa de la radiactividad natural; las retorcidas, electrones.

:::caution[Seguridad]
El hielo seco quema la piel por congelación: manéjalo siempre con guantes gruesos o pinzas, nunca lo encierres en un recipiente hermético (el gas puede hacerlo estallar) y trabaja en un lugar ventilado. El alcohol isopropílico es inflamable: nada de llamas ni fuentes de calor cerca.
:::

**Y los muones son relatividad en directo.** Cada estela recta que ves en la cámara es un muon que, sin la dilatación del tiempo, se habría desintegrado a kilómetros de altura.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 44:

- programa una calculadora del factor de Lorentz y la aplica a cosas que se mueven deprisa, del avión al Gran Colisionador de Hadrones,
- simula una lluvia de muones desde 15 km de altura y cuenta cuántos llegan al suelo con y sin dilatación del tiempo,
- calcula el desfase de los relojes del GPS,
- compara la energía cinética de Newton con la relativista,
- en el apartado opcional, comprueba la suma relativista de velocidades.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-44.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-44.ipynb)

## Qué has aprendido

- **La respuesta.** Cuando algo se mueve muy deprisa, su tiempo pasa más despacio y sus longitudes se acortan en la dirección del movimiento, en un factor $\gamma = 1/\sqrt{1 - v^2/c^2}$. Su energía crece sin límite al acercarse a $c$, que nada con masa puede alcanzar. Todo se deduce de que la velocidad de la luz es la misma para todos.
- **Las pruebas.** Los muones de los rayos cósmicos, los aceleradores, los relojes atómicos en aviones y el GPS.
- **Las herramientas.** El factor de Lorentz, despejar en expresiones con raíces, la aproximación binomial y el teorema de Pitágoras en el reloj de luz.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**Sumar velocidades.** Vas en un tren que avanza a $v$ y lanzas una pelota hacia delante a $u'$ respecto al tren. Para alguien en el andén, según Galileo y Newton, la pelota va a $u = u' + v$. Pero entonces, si lanzaras un destello de luz, iría a $c + v$, en contra del segundo postulado. La fórmula relativista es

$$u = \frac{u' + v}{1 + \dfrac{u'\,v}{c^2}}.$$

Para velocidades pequeñas, el denominador es casi 1 y vuelve la suma de siempre. Pero si $u' = c$:

$$u = \frac{c + v}{1 + v/c} = \frac{c\,(c + v)}{c + v} = c.$$

La luz va a $c$ para todos. Y dos velocidades menores que $c$ nunca suman más de $c$.

**El intervalo, lo que no cambia.** Dos observadores que se mueven uno respecto al otro miden tiempos y distancias distintos entre dos sucesos. Pero hay una combinación en la que siempre coinciden, el **intervalo**:

$$s^2 = (c\,\Delta t)^2 - (\Delta x)^2.$$

Es como el teorema de Pitágoras, pero con un signo menos: la geometría del **espacio-tiempo**, que el matemático Hermann Minkowski, antiguo profesor de Einstein, formuló en 1908. Por eso Einstein pensaba en «invariantes». En el reloj de luz, para el viajero $\Delta x = 0$ y $s = c\,\Delta\tau$; para ti, $(c\Delta t)^2 - (v\Delta t)^2 = c^2\Delta t^2(1 - \beta^2) = c^2\Delta\tau^2$. El mismo intervalo.

**Ejercicios**

1. Dos naves se alejan de la Tierra en sentidos opuestos, cada una a $0{,}9c$. ¿A qué velocidad se aleja una de la otra?
2. Desde una nave que va a $0{,}5c$ se dispara un proyectil hacia delante a $0{,}5c$ respecto a la nave. ¿A qué velocidad va respecto a la Tierra?
3. Comprueba que el intervalo de un rayo de luz que recorre una distancia $\Delta x = c\,\Delta t$ es cero, para cualquier observador.

<details>
<summary>Soluciones</summary>

1. $u = 1{,}8c/(1 + 0{,}81) \approx$ **0,9945 c**.
2. $u = c/(1 + 0{,}25) =$ **0,8 c**, no $c$.
3. $s^2 = c^2\Delta t^2 - c^2\Delta t^2 =$ **0**. Como el intervalo es el mismo para todos, cualquier otro observador también ve que la luz recorre una distancia $c$ por unidad de tiempo: es otra forma de decir el segundo postulado.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [5.3 Dilatación del tiempo, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/5-3-dilatacion-del-tiempo). Español; el reloj de luz, el experimento de los muones y la paradoja de los gemelos. Verificado el 20 de noviembre de 2026.
2. [5.5 La transformación de Lorentz, *Física universitaria* vol. 3 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-3/pages/5-5-la-transformacion-de-lorentz). Español; las ecuaciones completas y el espacio-tiempo, para el apartado opcional. Verificado el 20 de noviembre de 2026.
3. [Capítulo 24, Agujeros negros y espacio-tiempo curvo, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/24%3A_Agujeros_negros_y_espacio-tiempo_curvo). Español; empieza con un repaso de la relatividad especial antes de pasar a la general. Verificado el 20 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
