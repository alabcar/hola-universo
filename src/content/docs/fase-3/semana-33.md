---
title: "Semana 33 · ¿Cuánto brilla una estrella de verdad?"
description: "Fase 3 · La luz. La escala de magnitudes de Pogson, la magnitud absoluta y el módulo de distancia, el pársec, la luminosidad frente al brillo aparente, el índice de color, la magnitud límite y cómo estimar magnitudes a ojo con Algol y la Osa Menor."
sidebar:
  order: 33
  label: "33. ¿Cuánto brilla una estrella de verdad?"
---

## La pregunta del cielo

Sirio es la estrella más brillante del cielo nocturno. Rigel, en Orión, parece algo más débil. Pero Rigel emite decenas de miles de veces más luz que Sirio: lo que pasa es que está unas cien veces más lejos. Lo que ves desde la Tierra, el **brillo aparente**, mezcla dos cosas: cuánta luz emite de verdad una estrella, su **luminosidad**, y a qué distancia está.

Esta semana aprendes a separarlas. Para eso necesitas la escala con la que los astrónomos miden el brillo, la de **magnitudes**, que tiene más de dos mil años, va «al revés» y es logarítmica. Una vez la domines, una sola resta te dirá a qué distancia está una estrella, si sabes cuánto brilla de verdad, o cuánto brilla, si sabes a qué distancia está.

:::note[De dónde viene la palabra]
**Magnitud**, como viste en la semana 21, viene de *magnitudo*, «grandeza». En astronomía se aplicó al brillo porque los antiguos pensaban que las estrellas más brillantes eran más grandes: las de «primera magnitud» eran las de primer tamaño. Ojo con los dos significados: en física, una magnitud es cualquier cantidad medible (masa, tiempo); en astronomía, también es la medida del brillo de un astro. **Luminosidad** viene de *lumen, luminis*, «luz», como *luminoso* y *alumbrar*.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: la escala de magnitudes (35-45 min)

**Una escala de hace dos mil años.** Hacia el 130 a. C., el astrónomo griego Hiparco hizo un catálogo de estrellas y las clasificó por su brillo en seis grupos: las más brillantes eran de **primera magnitud**, y las más débiles que se veían, de **sexta**. Ptolomeo recogió la escala en el *Almagesto*. Por eso la escala va al revés: **cuanto mayor es la magnitud, más débil es la estrella**.

**Pogson pone números.** En el siglo XIX, al medir el brillo con instrumentos, se vio que la escala de Hiparco no era lineal: una estrella de primera magnitud daba unas cien veces más luz que una de sexta, y cada paso de magnitud multiplicaba el brillo más o menos por el mismo factor. Es lo que esperarías si el ojo percibe los cocientes, no las diferencias (lo ves en el apartado opcional). En 1856, el astrónomo inglés Norman Pogson lo fijó: **5 magnitudes de diferencia son exactamente un factor 100 en flujo**. Así, una magnitud es un factor $100^{1/5} \approx 2{,}512$. Con logaritmos,

$$m_1 - m_2 = -2{,}5\,\log_{10}\frac{F_1}{F_2}, \qquad \frac{F_1}{F_2} = 10^{-0{,}4\,(m_1 - m_2)}.$$

El signo menos hace que la escala vaya al revés: más flujo, menos magnitud.

**Magnitudes negativas.** La escala se extendió hacia los objetos muy brillantes por debajo de cero:

| Objeto | Magnitud aparente |
|---|---|
| Sol | −26,7 |
| Luna llena | −12,7 |
| Venus en su máximo | −4,7 |
| Júpiter en oposición | hasta −2,9 |
| Sirio | −1,46 |
| Vega | 0,03 |
| Estrella Polar | 2,0 |
| Límite a simple vista en una ciudad | 3 a 4 |
| Límite a simple vista en un cielo muy oscuro | 6 a 6,5 |
| Límite con prismáticos 8×30 en un cielo oscuro | unos 9 |
| Límite del telescopio espacial James Webb | más de 29 |

**Ejercicios**

1. ¿Cuántas veces más brilla Sirio que la estrella Polar?
2. ¿Cuántas veces más luz nos llega del Sol que de la Luna llena?
3. Una estrella da 10 veces más flujo que otra. ¿Cuántas magnitudes las separan? ¿Y si da 1000 veces más?
4. Dos estrellas de magnitud 3 están tan juntas que se ven como una sola. ¿Qué magnitud tiene el conjunto? (Cuidado: las magnitudes no se suman; los flujos, sí.)

<details>
<summary>Soluciones</summary>

1. $\Delta m = 2{,}0 - (-1{,}46) = 3{,}46$, $10^{0{,}4 \cdot 3{,}46} = 10^{1{,}384} \approx$ **24 veces**.
2. $\Delta m = 14$, $10^{5{,}6} \approx$ **400 000 veces**.
3. $-2{,}5\log 10 =$ **−2,5 magnitudes**; con 1000, **−7,5**.
4. El flujo total es el doble: $m = 3 - 2{,}5\log 2 = 3 - 0{,}75 =$ **2,25**.

</details>

### Sesión 2 · Matemáticas: el pársec, la magnitud absoluta y el módulo de distancia (40-45 min)

**El pársec.** Los astrónomos miden las distancias a las estrellas cercanas con la **paralaje**: el pequeño vaivén aparente de una estrella cercana a lo largo del año, por el movimiento de la Tierra alrededor del Sol (lo estudiarás a fondo en la semana 37). Si una estrella está a una distancia tal que el radio de la órbita terrestre, 1 ua, se ve desde ella con un ángulo de un segundo de arco, decimos que está a un **pársec** (pc). Por la aproximación de ángulo pequeño (semana 2), $1''$ son $1/206\,265$ radianes, así que

$$1\ \text{pc} = 206\,265\ \text{ua} \approx 3{,}086\times10^{16}\ \text{m} \approx 3{,}26\ \text{años luz}.$$

Y si la paralaje es $p$ segundos de arco, la distancia en pársecs es $d = 1/p$. Ninguna estrella tiene una paralaje de 1″: la más cercana, Próxima Centauri, tiene 0,77″ y está a 1,30 pc.

**La magnitud absoluta.** Para comparar luminosidades hay que poner todas las estrellas a la misma distancia. Por convenio, la **magnitud absoluta** $M$ es la magnitud aparente que tendría una estrella si estuviera a **10 pársecs**. Como el flujo cae con el cuadrado de la distancia (semana 30), una estrella a una distancia $d$ tiene un flujo $(10/d)^2$ veces el que tendría a 10 pc. En magnitudes:

$$m - M = -2{,}5\log_{10}\left(\frac{10}{d}\right)^2 = 5\log_{10}\frac{d}{10\ \text{pc}}.$$

La diferencia $m - M$ se llama **módulo de distancia**: es otra forma de dar la distancia. Un módulo de 0 son 10 pc; de 5, 100 pc; de 10, 1000 pc. Despejando,

$$d = 10^{(m - M + 5)/5}\ \text{pc}.$$

**De la magnitud absoluta a la luminosidad.** El Sol tiene una magnitud absoluta visual de 4,83. Como las magnitudes son logaritmos de cocientes,

$$\frac{L}{L_\odot} = 10^{-0{,}4\,(M - 4{,}83)}.$$

(Esto vale para la luz visible; para la luminosidad total, en todas las longitudes de onda, se usan magnitudes **bolométricas**, que corrigen la luz que cae fuera del visible.)

**Ejercicios**

1. Sirio tiene $m = -1{,}46$ y está a 2,64 pc. ¿Cuál es su magnitud absoluta? ¿Cuántas veces más luminosa que el Sol es en el visible?
2. Rigel tiene $m = 0{,}13$ y está a unos 260 pc. Calcula $M$ y su luminosidad visual. ¿Cuántas veces más luminosa que Sirio es?
3. Una estrella igual que el Sol ($M = 4{,}83$) se ve con $m = 9{,}83$. ¿A qué distancia está? ¿La verías con tus prismáticos?
4. ¿Qué magnitud aparente tendría el Sol visto desde 10 pc? ¿Lo verías a simple vista desde una ciudad?

<details>
<summary>Soluciones</summary>

1. $M = -1{,}46 - 5\log(0{,}264) = -1{,}46 + 2{,}89 =$ **1,43**. $L/L_\odot = 10^{-0{,}4(1{,}43 - 4{,}83)} = 10^{1{,}36} \approx$ **23 veces**.
2. $M = 0{,}13 - 5\log 26 = 0{,}13 - 7{,}07 \approx$ **−6,9**. $L/L_\odot = 10^{0{,}4 \cdot 11{,}8} \approx$ **50 000 veces** (y más aún contando el ultravioleta, porque es muy caliente). Unas **2000 veces** más que Sirio.
3. $m - M = 5$: **100 pc**. Con magnitud 9,8 queda justo en el límite de unos 8×30 en un cielo muy oscuro: probablemente no.
4. **4,83**, por definición. Desde una ciudad, con un límite de 3 o 4, no lo verías; desde un cielo oscuro, sí, como una estrella discreta.

</details>

### Sesión 3 · Física: brillo aparente, luminosidad y color (35-45 min)

**Tres cantidades distintas.**

- La **luminosidad** $L$ es la potencia total que emite la estrella, en vatios. Es una propiedad de la estrella: no depende de quién la mire. La del Sol es $3{,}83\times10^{26}$ W (semana 30), y la de las demás estrellas se suele dar en luminosidades solares, $L_\odot$.
- El **flujo** o **brillo aparente** $F$ es la potencia que llega a cada metro cuadrado aquí, $F = L/(4\pi d^2)$. Depende de la distancia.
- La **magnitud aparente** $m$ es el flujo expresado en la escala logarítmica de Pogson; la **absoluta** $M$, la luminosidad expresada en esa misma escala.

**Lo que se interpone.** El polvo entre las estrellas absorbe y dispersa la luz, igual que la atmósfera (semana 26), y más el azul que el rojo. Eso hace que las estrellas lejanas se vean más débiles (**extinción interestelar**) y más rojas (**enrojecimiento**) de lo que son. Si no se corrige, la estrella parece más lejana de lo que está. Fue uno de los grandes errores de la astronomía de principios del siglo XX (semana 38).

**El índice de color.** Para medir el color de una estrella se mide su magnitud con dos filtros, el azul **B** (centrado en unos 440 nm) y el visual **V** (unos 550 nm), y se restan: el **índice de color** $B - V$. Es la versión en magnitudes del cociente entre dos filtros que usaste en el cuaderno de la semana 31. Por convenio, Vega tiene $B - V \approx 0$. Una estrella más azul que Vega tiene un índice negativo; una más roja, positivo:

| Estrella | $B - V$ | Temperatura |
|---|---|---|
| Rigel | −0,03 | ~12 000 K |
| Vega | 0,00 | ~9600 K |
| Proción | 0,42 | ~6500 K |
| Sol | 0,65 | 5772 K |
| Aldebarán | 1,54 | ~3900 K |
| Betelgeuse | 1,85 | ~3600 K |

Como el índice es una resta de magnitudes, es un cociente de flujos y **no depende de la distancia**. Es un termómetro que funciona a cualquier distancia (salvo por el enrojecimiento del polvo).

**La magnitud límite.** La estrella más débil que puedes ver depende del cielo (contaminación lumínica, Luna, altura de la estrella, transparencia), de tu ojo (adaptación a la oscuridad, edad) y del instrumento. Con un instrumento de diámetro $D$, la ganancia respecto al ojo con pupila $p$ es (semana 28)

$$\Delta m = 5\log_{10}\frac{D}{p},$$

porque la luz recogida va con $D^2$ y $2{,}5\log(D^2/p^2) = 5\log(D/p)$. Con 30 mm y una pupila de 7 mm, unas 3,2 magnitudes; con 6 mm, 3,5.

:::note[De dónde viene la palabra]
**Pársec** es una palabra inventada en 1913 por el astrónomo británico Herbert Hall Turner, uniendo **par**alaje y **sec**undo: la distancia de una paralaje de un segundo. **Absoluto** viene del latín *absolutus*, «desligado, acabado», de *absolvere*, «soltar»: una magnitud absoluta está desligada de la distancia. **Bolométrica** viene del **bolómetro**, el aparato que mide toda la radiación, inventado por Samuel Langley en 1878, del griego *bolḗ*, «rayo, lanzamiento».
:::

**Qué hacer**

1. Calcula cuántas veces más azul en flujo (cociente B/V) es una estrella con $B - V = -0{,}3$ que una con $B - V = 1{,}5$.
2. Una estrella está a 1000 pc detrás de una nube de polvo que absorbe 2 magnitudes. Su magnitud aparente es 12. Si olvidas el polvo, ¿qué distancia calcularías a partir de su magnitud absoluta conocida?
3. Con unos prismáticos 10×50 y una pupila de 6 mm, ¿cuántas magnitudes ganas? ¿Y con un telescopio de 200 mm?

### Sesión 4 · Astronomía y observación: estimar magnitudes a ojo (30-45 min)

**Tu magnitud límite con la Osa Menor.** La Osa Menor está siempre sobre el horizonte norte desde España, y sus estrellas tienen magnitudes muy repartidas. Sirve para medir la magnitud límite de tu cielo:

| Estrella | Magnitud aproximada |
|---|---|
| Polar (α UMi) | 2,0 |
| Kochab (β UMi) | 2,1 |
| Pherkad (γ UMi) | 3,0 |
| ε UMi | 4,2 |
| ζ UMi | 4,3 |
| δ UMi (Yildun) | 4,4 |
| η UMi | 4,9 |

Sal con los ojos adaptados a la oscuridad (al menos 15 minutos sin mirar luces) y mira cuáles ves. Si ves la Polar y las dos «guardas» (Kochab y Pherkad), pero ninguna más, tu límite está cerca de 3 o 3,5. Si ves η UMi, estás en un cielo de magnitud 5 o mejor. Usa Stellarium para identificar cada estrella. Repite con los prismáticos.

**El método de Argelander: estimar con dos estrellas de comparación.** El ojo no sabe decir «esta estrella es de magnitud 2,7», pero es muy bueno comparando. El método que usan los observadores de estrellas variables desde el siglo XIX es:

1. Busca dos estrellas de comparación de magnitud conocida, una algo más brillante (A) y otra algo más débil (B) que la que quieres medir (V).
2. Decide en qué fracción del camino de A a B está V. Por ejemplo, «V está a 3 décimos de A hacia B».
3. Calcula: $m_V = m_A + 0{,}3\,(m_B - m_A)$.

**Algol, la estrella que guiña.** En Perseo, alta en las noches de noviembre a febrero, está Algol (β Persei). Casi siempre brilla con magnitud 2,1, pero cada 2 días y 21 horas baja a 3,4 durante unas horas y vuelve a subir. No es que cambie su luz: es una **binaria eclipsante**, dos estrellas que giran una alrededor de la otra en un plano que vemos de canto, y la más débil tapa en parte a la más brillante. La periodicidad la midió en 1782 el joven sordo John Goodricke, que propuso esa explicación.

Estrellas de comparación cerca de Algol:

| Estrella | Magnitud aproximada |
|---|---|
| Almach (γ Andromedae) | 2,1 |
| ε Persei | 2,9 |
| δ Persei | 3,0 |
| κ Persei | 3,8 |

Estima la magnitud de Algol con el método de Argelander varias noches seguidas, a la misma hora, y apúntalo. Si una noche la ves claramente más débil que ε Persei, la has pillado en un mínimo. Las horas de los mínimos se publican en las efemérides de las revistas de astronomía y en algunas webs de observadores. Si sigues un mínimo entero, unas 10 horas, verás la estrella apagarse y volver a encenderse.

:::note[De dónde viene la palabra]
**Algol** viene del árabe *raʾs al-ghūl*, «la cabeza del demonio»: en la constelación de Perseo, representa la cabeza de la Medusa que lleva el héroe en la mano. No se sabe si su nombre tiene que ver con su variabilidad, que sí pudieron notar los antiguos. **Variable** viene de *variare*, «cambiar, mudar».
:::

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 33:

- programa un conversor entre cocientes de flujo y diferencias de magnitud, y entre magnitud aparente, absoluta y distancia,
- calcula la magnitud absoluta y la luminosidad de las estrellas más brillantes del cielo y las compara en una gráfica,
- estima la temperatura de una estrella a partir de su índice de color $B - V$,
- simula la curva de luz de una binaria eclipsante parecida a Algol, en flujo y en magnitudes.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-33.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-33.ipynb)

## Qué has aprendido

- **La respuesta.** El brillo que vemos (magnitud aparente) depende de la luminosidad de la estrella y de su distancia. La magnitud absoluta, el brillo que tendría a 10 pársecs, mide la luminosidad. Rigel brilla menos que Sirio en nuestro cielo, pero es miles de veces más luminosa.
- **Una escala al revés y logarítmica.** 5 magnitudes son un factor 100 en flujo; cuanto mayor es la magnitud, más débil es el objeto. El módulo de distancia, $m - M = 5\log(d/10\ \text{pc})$, une brillo, luminosidad y distancia.
- **Las herramientas.** La escala de Pogson, el pársec, la magnitud absoluta, el módulo de distancia, el índice de color y la estimación de magnitudes por comparación.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**Por qué los sentidos son logarítmicos.** En 1834, el fisiólogo alemán Ernst Weber observó que la diferencia mínima que notamos entre dos estímulos es proporcional al estímulo: si distingues 100 g de 102 g, distinguirás 1000 g de 1020 g, pero no de 1002 g. En 1860, Gustav Fechner dedujo de ahí que la **sensación** debe crecer con el **logaritmo** del estímulo: si cada escalón perceptible es un mismo **cociente**, $\Delta S \propto \Delta F/F$, sumando escalones (integrando, semana 11) se obtiene

$$S = k\,\ln\frac{F}{F_0},$$

donde $F_0$ es el umbral, el estímulo mínimo perceptible. Es la **ley de Weber-Fechner**. Las magnitudes de Hiparco eran, sin saberlo, una escala de sensación: el ojo había hecho el logaritmo. Lo mismo pasa con el oído: la escala de **decibelios** es $10\log_{10}(I/I_0)$, y cada 10 dB más es un sonido diez veces más intenso que se oye solo «un poco más fuerte».

La ley de Weber-Fechner es una aproximación: en 1957, Stanley Smith Stevens propuso que la sensación crece más bien como una potencia del estímulo, con un exponente que depende del sentido (para el brillo, en torno a 0,3 o 0,5). En los dos casos, el mensaje es el mismo: los sentidos comprimen enormemente los rangos de la naturaleza, y eso nos permite ver a la vez a pleno sol y a la luz de las estrellas, que es cientos de millones de veces más débil.

**Ejercicios**

1. ¿Cuántos decibelios más tiene un sonido 1000 veces más intenso que otro? ¿Cuántas magnitudes «más brillante» es una estrella que da 1000 veces más flujo? Compara las dos escalas: ¿cuántos decibelios equivalen a una magnitud?
2. Si la sensación de brillo siguiera la ley de Stevens con exponente 0,33, ¿cuántas veces más brillante «parecería» una estrella que da 100 veces más flujo?
3. La luz del Sol a mediodía (magnitud −26,7) y la de una estrella de magnitud 6. ¿Cuántos órdenes de magnitud las separan en flujo?

<details>
<summary>Soluciones</summary>

1. **30 dB** y **7,5 magnitudes**. Una magnitud es un factor 2,512, que en decibelios son $10\log 2{,}512 =$ **4 dB**.
2. $100^{0{,}33} \approx$ **4,6 veces**.
3. $\Delta m = 32{,}7$, cociente $10^{0{,}4 \cdot 32{,}7} = 10^{13{,}1}$: **13 órdenes de magnitud**.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [17.1 El brillo de las estrellas, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/17%3A_Analizando_Starlight/17.01%3A_El_brillo_de_las_estrellas). Español; luminosidad, brillo aparente y la escala de magnitudes. Verificado el 20 de noviembre de 2026.
2. [17.2 Colores de las estrellas, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/17%3A_Analizando_Starlight/17.02%3A_Colores_de_Estrellas). Español; filtros e índice de color. Verificado el 20 de noviembre de 2026.
3. [Capítulo 19, Distancias celestiales, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/19%3A_Distancias_Celestiales). Español; paralaje, pársec y escalera de distancias (lo retomarás en la semana 37). Verificado el 20 de noviembre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). Para identificar las estrellas de comparación y ver sus magnitudes. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
