---
title: "Semana 30 · ¿Es la luz una onda electromagnética?"
description: "Fase 3 · La luz. Las leyes de Maxwell en dibujos, la onda electromagnética, la ley del inverso del cuadrado, la velocidad de la luz a partir de constantes eléctricas, el espectro electromagnético, los fotones y el cielo en radio, infrarrojo y rayos X."
sidebar:
  order: 30
  label: "30. ¿Es la luz una onda electromagnética?"
---

## La pregunta del cielo

En 1865, el físico escocés James Clerk Maxwell terminó de reunir en unas pocas ecuaciones todo lo que se sabía de la electricidad y el magnetismo. Al combinarlas, encontró que predecían ondas: perturbaciones de los campos eléctrico y magnético que se propagan solas por el espacio vacío. Calculó su velocidad a partir de dos constantes medidas en el laboratorio con cables, imanes y condensadores, y le salió unos 310 000 km/s. Era, con el margen de error de la época, la velocidad de la luz que había medido Fizeau (semana 25). Maxwell concluyó que la luz tenía que ser una de esas ondas.

En la semana 27 viste que la luz es una onda, y en la 29, qué son los campos. Esta semana los juntas: la luz es una onda de campos eléctricos y magnéticos, y lo que tus ojos ven es solo una franja estrecha de un abanico inmenso, el **espectro electromagnético**, que va de las ondas de radio a los rayos gamma. El universo emite en todo ese abanico, y la astronomía moderna lo mira entero.

:::note[De dónde viene la palabra]
**Espectro** viene del latín *spectrum*, «aparición, imagen, fantasma», de *specere*, «mirar» (la misma raíz que *espejo*, semana 28). Newton usó la palabra en 1671 para la banda de colores que salía de su prisma: una imagen fantasmal proyectada en la pared. **Radiación** viene de *radius*, que en latín era el radio de una rueda y también un rayo de luz: lo que sale en línea recta desde un centro.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: campos en dibujos y la ley del inverso del cuadrado (35-45 min)

**Las cuatro leyes del electromagnetismo, en dibujos.** Las ecuaciones de Maxwell se escriben con un cálculo que no necesitas para entender lo que dicen. Con las líneas de campo de la semana 29, se resumen así:

1. **Las cargas son fuentes del campo eléctrico.** Las líneas de campo eléctrico salen de las cargas positivas y terminan en las negativas.
2. **No hay fuentes del campo magnético.** Las líneas de campo magnético no empiezan ni terminan en ningún sitio: siempre se cierran sobre sí mismas. Es otra forma de decir que no existen polos magnéticos sueltos.
3. **Un campo magnético que cambia crea un campo eléctrico** que da vueltas a su alrededor. Es la inducción de Faraday.
4. **Una corriente crea un campo magnético** que da vueltas a su alrededor (Ørsted y Ampère). Maxwell añadió la pieza que faltaba: **un campo eléctrico que cambia también crea un campo magnético**, aunque no haya corriente.

Las leyes 3 y 4 son la clave. Un campo eléctrico que cambia crea un campo magnético que cambia, que crea un campo eléctrico que cambia... La perturbación se sostiene a sí misma y avanza, sin cargas ni cables. Eso es una **onda electromagnética**.

**Cómo es la onda.** En una onda electromagnética que avanza en una dirección:

- el campo eléctrico $\vec{E}$ y el magnético $\vec{B}$ oscilan **perpendiculares** a la dirección de avance (es una onda transversal) y perpendiculares entre sí,
- los dos oscilan **en fase**, con la misma forma $\sin(kx - \omega t)$ de la semana 27,
- sus tamaños están ligados: $E = c\,B$,
- la dirección en la que oscila el campo eléctrico es la **polarización** de la luz (semana 26).

**La ley del inverso del cuadrado.** Una fuente que emite luz en todas direcciones, como una estrella, reparte su potencia $L$ (en vatios) sobre esferas cada vez mayores. A una distancia $r$, la esfera tiene un área $4\pi r^2$, y la potencia que llega a cada metro cuadrado, la **intensidad** o **flujo**, es

$$F = \frac{L}{4\pi r^2}.$$

Al doble de distancia, la luz se reparte en cuatro veces más área: llega la cuarta parte. Es la misma geometría que la del campo gravitatorio (semana 29), y la base de cómo se miden las distancias a las estrellas por su brillo (semana 33).

**Ejercicios**

1. El Sol emite $L = 3{,}83\times10^{26}$ W. ¿Cuánta potencia llega a cada metro cuadrado a 1 ua ($1{,}496\times10^{11}$ m)?
2. ¿Y a la distancia de Júpiter, 5,2 ua? ¿Y a la de la Voyager 1, unas 173 ua?
3. Un campo eléctrico de la luz solar vale unos 1000 V/m. ¿Cuánto vale su campo magnético? Compáralo con el de la Tierra (unos 50 µT).

<details>
<summary>Soluciones</summary>

1. $3{,}83\times10^{26}/(4\pi \cdot (1{,}496\times10^{11})^2) \approx$ **1360 W/m²**. Es la **constante solar**: unos 14 bombillas antiguas de 100 W por metro cuadrado, antes de cruzar la atmósfera.
2. $1360/5{,}2^2 \approx$ **50 W/m²** en Júpiter; $1360/173^2 \approx$ **0,045 W/m²** en la Voyager 1.
3. $B = E/c = 1000/(3\times10^8) \approx 3{,}3\times10^{-6}$ T, unos **3 µT**: unas quince veces menos que el campo de la Tierra, pero oscilando cientos de billones de veces por segundo.

</details>

### Sesión 2 · Matemáticas: la velocidad de la luz y el espectro en escala logarítmica (35-40 min)

**La velocidad de la luz sale de la electricidad.** La ley de Coulomb (semana 29) se suele escribir con la constante $k = 1/(4\pi\varepsilon_0)$, donde $\varepsilon_0 \approx 8{,}854\times10^{-12}$ C²/(N·m²) es la **permitividad del vacío**: mide cómo responde el vacío a las cargas. La fuerza entre corrientes tiene otra constante, $\mu_0 \approx 1{,}2566\times10^{-6}$ N/A², la **permeabilidad del vacío**. Maxwell encontró que sus ondas viajan a

$$c = \frac{1}{\sqrt{\mu_0\,\varepsilon_0}}.$$

Hazlo con la calculadora: $\mu_0\varepsilon_0 \approx 1{,}1127\times10^{-17}$ s²/m², su raíz es $3{,}3356\times10^{-9}$ s/m, y su inverso, $2{,}998\times10^8$ m/s. La velocidad de la luz estaba escondida en dos medidas de laboratorio que no tenían nada que ver con la luz.

**Un abanico de veinte órdenes de magnitud.** Todas las ondas electromagnéticas viajan a $c$ en el vacío y cumplen $c = \lambda f$. Lo único que las distingue es la longitud de onda (o la frecuencia), y el abanico es enorme:

| Región | Longitud de onda típica | Frecuencia típica | Del tamaño de... |
|---|---|---|---|
| Radio | 1 m - 1 km | 300 kHz - 300 MHz | un edificio |
| Microondas | 1 mm - 1 m | 300 MHz - 300 GHz | una mano |
| Infrarrojo | 750 nm - 1 mm | 300 GHz - 400 THz | una célula |
| Visible | 380 - 750 nm | 400 - 790 THz | una bacteria |
| Ultravioleta | 10 - 380 nm | | un virus |
| Rayos X | 0,01 - 10 nm | | un átomo |
| Rayos gamma | menos de 0,01 nm | | un núcleo atómico |

(Los límites entre regiones son convenios: el espectro es continuo.) Para dibujar algo que va de kilómetros a billonésimas de metro hace falta una **escala logarítmica** (semana 26): cada marca del eje es diez veces la anterior. En esa escala, toda la luz visible ocupa una franja estrechísima.

**Ejercicios**

1. Una emisora de FM emite a 100 MHz. ¿Cuál es su longitud de onda?
2. El wifi y los hornos de microondas funcionan a unos 2,45 GHz. ¿Longitud de onda?
3. ¿Cuántos órdenes de magnitud hay entre una onda de radio de 1 km y un rayo gamma de $10^{-12}$ m?
4. ¿Qué fracción del intervalo logarítmico entre 1 km y $10^{-12}$ m ocupa la luz visible?

<details>
<summary>Soluciones</summary>

1. $3\times10^8/10^8 =$ **3 m**.
2. $3\times10^8/2{,}45\times10^9 \approx$ **12,2 cm**.
3. De $10^3$ a $10^{-12}$: **15 órdenes de magnitud** (y el espectro real se extiende todavía más por los dos lados).
4. El visible va de $\log_{10}(3{,}8\times10^{-7}) = -6{,}42$ a $\log_{10}(7{,}5\times10^{-7}) = -6{,}12$: unas 0,3 unidades de 15, es decir, **un 2 %** del eje.

</details>

### Sesión 3 · Física: el espectro electromagnético y los fotones (40-45 min)

**Un abanico que se descubrió poco a poco.**

- **Infrarrojo (1800).** William Herschel, el descubridor de Urano, separó la luz del Sol con un prisma y puso termómetros en cada color. El que estaba más allá del rojo, donde no se veía nada, se calentaba más. Había luz invisible.
- **Ultravioleta (1801).** Un año después, Johann Wilhelm Ritter encontró, más allá del violeta, una luz invisible que ennegrecía el cloruro de plata más deprisa que la luz visible.
- **Radio (1887).** Heinrich Hertz produjo ondas electromagnéticas con chispas en un circuito y las detectó con una antena al otro lado del laboratorio. Midió su longitud de onda y su velocidad: eran las ondas de Maxwell, como la luz pero de longitudes de onda de metros.
- **Rayos X (1895).** Wilhelm Röntgen descubrió una radiación que atravesaba la carne y no los huesos. Les llamó X, la incógnita, porque no sabía qué eran.
- **Rayos gamma (1900).** Paul Villard los encontró en la radiactividad del radio; resultaron ser ondas electromagnéticas de longitud de onda aún menor.

Todo eso es la misma cosa que la luz: ondas electromagnéticas de distintas longitudes de onda. Lo que llamamos «luz» es solo la parte que detectan nuestros ojos, seguramente porque es la región en la que más emite el Sol y la que mejor atraviesa la atmósfera y el agua.

**Las ventanas de la atmósfera.** La atmósfera no es transparente a todo. Deja pasar el visible (la **ventana óptica**) y las ondas de radio de entre unos milímetros y unas decenas de metros (la **ventana de radio**). El vapor de agua absorbe casi todo el infrarrojo, el ozono absorbe el ultravioleta (por suerte para nuestra piel) y los rayos X y gamma no llegan al suelo. Por eso los telescopios de rayos X, de gamma y de buena parte del infrarrojo tienen que estar en el espacio, y los de infrarrojo en tierra se ponen en montañas muy secas.

**Onda y partícula: el fotón.** En 1900, Max Planck, para explicar el color de los cuerpos calientes (semana 31), tuvo que suponer que la luz se emite en paquetes de energía. En 1905, Albert Einstein fue más allá: la luz **es** un chorro de paquetes, que hoy llamamos **fotones**, y cada uno lleva una energía proporcional a su frecuencia,

$$E = h\,f, \qquad h = 6{,}626\times10^{-34}\ \text{J·s},$$

donde $h$ es la **constante de Planck**. ¿Entonces la luz es onda o partícula? Las dos cosas: se propaga como una onda (interfiere, como en el experimento de Young) y se emite y se absorbe en paquetes, como partículas. En física atómica, la energía se mide en **electronvoltios** (eV): $1\ \text{eV} = 1{,}602\times10^{-19}$ J. Una regla muy cómoda:

$$E\ (\text{eV}) \approx \frac{1240}{\lambda\ (\text{nm})}.$$

Un fotón de luz roja (700 nm) lleva unos 1,8 eV; uno de violeta (400 nm), unos 3,1 eV. Por eso el ultravioleta, con fotones de más energía, puede romper moléculas de la piel y la luz roja no. Y por eso las ondas de radio, aunque sean muy intensas, no tienen fotones con energía para romper nada.

:::note[De dónde viene la palabra]
**Infrarrojo** lleva el prefijo latino *infra*, «por debajo»: por debajo del rojo en frecuencia. **Ultravioleta** lleva *ultra*, «más allá»: más allá del violeta. **Fotón** viene del griego *phōs, phōtós*, «luz», como *fotografía* («escritura con luz»). La palabra la popularizó el químico estadounidense Gilbert Lewis en 1926.
:::

**Qué hacer**

1. Calcula la energía en eV de un fotón de una emisora de FM (3 m), de microondas (12 cm), de luz verde (530 nm) y de rayos X (0,1 nm).
2. **Medir la velocidad de la luz con un horno de microondas.** Las microondas forman dentro del horno una onda estacionaria, con puntos calientes separados media longitud de onda. Quita el plato giratorio (para que la comida no se mueva), pon dentro un plato con una tableta de chocolate o una capa de queso rallado y calienta **solo 15 o 20 segundos**. Aparecerán zonas fundidas. Mide la distancia entre dos zonas fundidas vecinas, $d$: la longitud de onda es $2d$. La frecuencia viene en la etiqueta del horno (normalmente 2450 MHz). Calcula $c = 2\,d\,f$. No hagas funcionar nunca el horno vacío.

### Sesión 4 · Astronomía y observación: el cielo invisible (30-45 min)

**Cada longitud de onda, un universo distinto.** Si tus ojos vieran otras regiones del espectro, el cielo nocturno sería irreconocible:

- **En radio**, lo más brillante sería el centro de la Vía Láctea, en Sagitario. Karl Jansky lo descubrió por accidente en 1932, buscando el origen de unas interferencias en las comunicaciones transatlánticas. Verías también el gas de hidrógeno frío entre las estrellas, que emite en una longitud de onda de 21 cm (detectada en 1951), y un resplandor uniforme en todas direcciones: el **fondo cósmico de microondas**, la luz más antigua del universo, descubierta en 1965 (semana 42).
- **En infrarrojo**, el polvo que en el visible tapa la luz se vuelve transparente o brilla él mismo. Las nubes donde nacen estrellas, como la de Orión, resplandecerían (semana 35). El telescopio espacial James Webb, lanzado en diciembre de 2021, con un espejo de 6,5 m, observa en el infrarrojo.
- **En rayos X**, verías gas a millones de grados: la corona del Sol, restos de supernovas, gas que cae en agujeros negros (semana 36). Los observan telescopios en órbita como Chandra (NASA) y XMM-Newton (ESA), ambos lanzados en 1999.
- **En rayos gamma**, los fenómenos más violentos: explosiones de estrellas, chorros de galaxias activas.

**Explora con ESASky.** La Agencia Espacial Europea tiene un portal gratuito, **ESASky**, que muestra todo el cielo en distintas longitudes de onda con datos de muchas misiones, desarrollado en su centro de astronomía espacial cerca de Madrid. Prueba esto:

1. Busca **M42** (la nebulosa de Orión). Cambia entre la vista en visible, en infrarrojo y en rayos X. ¿Qué aparece y qué desaparece?
2. Busca **M31** (Andrómeda) y compara el visible con el infrarrojo lejano: en el infrarrojo destacan los anillos de polvo donde se forman estrellas.
3. Mira el cielo entero en microondas (Planck): la banda de la Vía Láctea y, fuera de ella, el fondo cósmico.

**Y esta noche.** Sal a ver Orión (a partir de las 22:00 en noviembre) y localiza la nebulosa bajo el cinturón, con los prismáticos. Lo que ves es la luz visible del gas iluminado por estrellas jóvenes. Recuerda que, en infrarrojo, toda la constelación está envuelta en nubes de polvo que brillan.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 30:

- calcula $c$ a partir de $\mu_0$ y $\varepsilon_0$,
- dibuja una onda electromagnética en tres dimensiones, con los campos eléctrico y magnético,
- dibuja el espectro electromagnético en escala logarítmica, con la franja visible en color y una curva esquemática de las ventanas de la atmósfera,
- calcula la energía de los fotones de cada región,
- en el apartado opcional, simula la ecuación de ondas en una cuerda.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-30.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-30.ipynb)

## Qué has aprendido

- **La respuesta.** Sí: la luz es una onda de campos eléctricos y magnéticos que se sostienen el uno al otro y viajan por el vacío a $c = 1/\sqrt{\mu_0\varepsilon_0}$. Y a la vez se emite y se absorbe en paquetes, los fotones, con energía $E = hf$.
- **El espectro.** Radio, microondas, infrarrojo, visible, ultravioleta, rayos X y gamma son la misma cosa con distinta longitud de onda. La atmósfera solo deja pasar algunas; para las demás hay que salir al espacio.
- **Las herramientas.** La ley del inverso del cuadrado, la escala logarítmica para cantidades que abarcan muchos órdenes de magnitud y la conversión entre longitud de onda, frecuencia y energía.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**La ecuación de ondas.** Una onda $y(x, t)$ depende de dos variables. Para derivarla respecto a una de ellas dejando fija la otra se usan las **derivadas parciales**, que se escriben con una $\partial$ redondeada: $\partial y/\partial t$ es cómo cambia $y$ con el tiempo en un punto fijo, y $\partial y/\partial x$, cómo cambia con la posición en un instante fijo. Las derivadas segundas, $\partial^2 y/\partial t^2$ y $\partial^2 y/\partial x^2$, son la aceleración del punto y la **curvatura** de la forma de la onda.

Casi todas las ondas de la física, desde una cuerda de guitarra hasta la luz, cumplen la **ecuación de ondas**, propuesta por Jean le Rond d'Alembert en 1747 para las cuerdas vibrantes:

$$\frac{\partial^2 y}{\partial t^2} = v^2\,\frac{\partial^2 y}{\partial x^2}.$$

Dice algo intuitivo: cada trocito de cuerda se acelera en proporción a lo curvada que está la cuerda a su alrededor. Donde la cuerda forma una cresta, se acelera hacia abajo; donde forma un valle, hacia arriba.

Comprueba que la onda de la semana 27 la cumple. Con $y = A\sin(kx - \omega t)$:

$$\frac{\partial^2 y}{\partial t^2} = -\omega^2 A\sin(kx - \omega t), \qquad \frac{\partial^2 y}{\partial x^2} = -k^2 A\sin(kx - \omega t).$$

La ecuación se cumple si $\omega^2 = v^2 k^2$, es decir, si $v = \omega/k = \lambda f$. Lo que Maxwell hizo, combinando sus cuatro leyes, fue llegar a esta misma ecuación para el campo eléctrico, con $v^2 = 1/(\mu_0\varepsilon_0)$. Por eso supo que sus ondas viajaban a esa velocidad.

D'Alembert encontró además la solución general: **cualquier** forma que se desplace sin deformarse, $y = f(x - vt)$, la cumple, sea un seno, un pulso o una forma cualquiera. Y como la ecuación es **lineal** (solo aparece $y$, no $y^2$ ni otras potencias), la suma de dos soluciones también es solución: es el principio de superposición de la semana 27.

**Ejercicios**

1. Calcula $\partial y/\partial x$ y $\partial y/\partial t$ para $y = x^2 t + 3t$.
2. Comprueba que el pulso $y = e^{-(x - vt)^2}$ cumple la ecuación de ondas. Pista: llama $u = x - vt$ y usa la regla de la cadena (semana 28): $\partial u/\partial x = 1$, $\partial u/\partial t = -v$.
3. ¿Cumple la ecuación de ondas $y = \sin(kx)\cos(\omega t)$ con $\omega = vk$? ¿Qué tipo de onda es? Pista: usa la identidad de la semana 27 al revés.

<details>
<summary>Soluciones</summary>

1. $\partial y/\partial x = 2xt$; $\partial y/\partial t = x^2 + 3$.
2. Con $y = e^{-u^2}$, cada derivada respecto a $x$ da un factor 1 y cada derivada respecto a $t$, un factor $-v$. Así que $\partial^2 y/\partial t^2 = v^2\,d^2y/du^2$ y $\partial^2 y/\partial x^2 = d^2y/du^2$: se cumple sin calcular nada más.
3. Sí: $\partial^2 y/\partial t^2 = -\omega^2 y$ y $\partial^2 y/\partial x^2 = -k^2 y$. Es una **onda estacionaria**, la suma de dos ondas iguales que viajan en sentidos opuestos: $\sin(kx)\cos(\omega t) = \tfrac{1}{2}[\sin(kx - \omega t) + \sin(kx + \omega t)]$. Tiene puntos fijos (nodos) donde $\sin(kx) = 0$. Es la onda del horno de microondas y de una cuerda de guitarra.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [16.1 Ecuaciones de Maxwell y ondas electromagnéticas, *Física universitaria* vol. 2 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-2/pages/16-1-ecuaciones-de-maxwell-y-ondas-electromagneticas). Español; las cuatro ecuaciones y cómo Hertz confirmó la predicción. Verificado el 20 de noviembre de 2026.
2. [16.5 El espectro electromagnético, *Física universitaria* vol. 2 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-2/pages/16-5-el-espectro-electromagnetico). Español; cada región del espectro y sus usos. Verificado el 20 de noviembre de 2026.
3. [5.2 El espectro electromagnético, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/05%3A_Radiaci%C3%B3n_y_espectros/5.02%3A_El_espectro_electromagn%C3%A9tico). Español; el espectro visto desde la astronomía, con las ventanas de la atmósfera. Verificado el 20 de noviembre de 2026.
4. [Explora el cosmos con ESASky (ESA)](https://www.esa.int/Space_in_Member_States/Spain/Explora_el_cosmos_con_ESASky). Español; presentación del portal. El portal está en [sky.esa.int](https://sky.esa.int/). Verificado el 20 de noviembre de 2026 (la presentación; el portal, **sin verificar**).
5. [6.5 Observaciones fuera de la atmósfera terrestre, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/06%3A_Instrumentos_astron%C3%B3micos/6.05%3A_Observaciones_fuera_de_la_atm%C3%B3sfera_terrestre). Español; telescopios espaciales de infrarrojo, rayos X y gamma. Verificado el 20 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
