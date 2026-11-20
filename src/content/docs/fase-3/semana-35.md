---
title: "Semana 35 · ¿Cómo nace, vive y muere una estrella?"
description: "Fase 3 · La luz. Gráficas log-log, líneas de radio constante, la relación masa-luminosidad y la vida de las estrellas, el diagrama de Hertzsprung-Russell con datos reales, el nacimiento de las estrellas, los cúmulos y su edad, y nebulosas y cúmulos para ver con prismáticos."
sidebar:
  order: 35
  label: "35. ¿Cómo nace, vive y muere una estrella?"
---

## La pregunta del cielo

Una estrella como el Sol vive unos 10 000 millones de años. Nadie puede ver nacer, envejecer y morir una estrella. Y, sin embargo, los astrónomos cuentan su vida con mucho detalle. ¿Cómo?

Imagina que tienes que averiguar cómo crece un árbol, pero solo puedes pasear una hora por un bosque. No verás crecer ninguno, pero verás brotes, árboles jóvenes, adultos, viejos y troncos caídos. Si cuentas cuántos hay de cada tipo y comparas sus tamaños, puedes reconstruir la vida de un árbol. Con las estrellas se hace lo mismo, y la herramienta para ordenarlas es una gráfica que inventaron por separado, hacia 1910, el danés Ejnar Hertzsprung y el estadounidense Henry Norris Russell: el **diagrama de Hertzsprung-Russell**, o diagrama HR. Esta semana lo dibujas con datos reales de casi tres mil estrellas.

:::note[De dónde viene la palabra]
**Nebulosa** viene del latín *nebula*, «niebla, nube»: manchas difusas en el cielo, como jirones de niebla. **Cúmulo** viene de *cumulus*, «montón» (de ahí *acumular* y las nubes cúmulo). **Pléyades** es un nombre griego, el de las siete hijas de Atlas y Pléyone; su origen es dudoso: se ha relacionado con *peleiádes*, «palomas», y con *pleîn*, «navegar», porque su aparición al amanecer marcaba en Grecia el comienzo de la temporada de navegación.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: leer gráficas log-log (35-45 min)

**Un recordatorio.** En la semana 15 viste que una **ley de potencias**, $y = a\,x^n$, se convierte en una recta si dibujas $\log y$ frente a $\log x$:

$$\log y = \log a + n\log x.$$

La **pendiente** de la recta es el exponente $n$. Por eso los astrónomos dibujan casi todo en ejes logarítmicos: las propiedades de las estrellas van desde una diezmilésima hasta un millón de veces las del Sol, y muchas de sus relaciones son leyes de potencias.

**Los ejes del diagrama HR.** Tiene dos versiones equivalentes:

- La de los **observadores**: magnitud absoluta $M$ (semana 33) en el eje vertical, con las brillantes arriba, e índice de color $B - V$ (semana 33) en el horizontal, con las azules a la izquierda.
- La de los **teóricos**: $\log(L/L_\odot)$ en el eje vertical y $\log T$ en el horizontal, pero con la temperatura **creciendo hacia la izquierda**, por tradición, para que se parezca a la de los observadores.

Las dos son gráficas log-log: la magnitud absoluta es $-2{,}5$ veces el logaritmo de la luminosidad, y el índice de color depende del logaritmo de la temperatura (más o menos).

**Las líneas de radio constante.** De la ley de Stefan-Boltzmann (semana 31), $L = 4\pi R^2\sigma T^4$. En unidades solares,

$$\log\frac{L}{L_\odot} = 2\log\frac{R}{R_\odot} + 4\log\frac{T}{T_\odot}.$$

Para un radio fijo, esto es una **recta** de pendiente 4 en el diagrama de los teóricos. Todas las estrellas de igual radio están en una misma recta diagonal: las de arriba a la derecha son enormes (frías pero muy luminosas, solo pueden serlo por su tamaño), y las de abajo a la izquierda, diminutas (calientes pero poco luminosas).

**Ejercicios**

1. Una estrella tiene la misma temperatura que el Sol y es 100 veces más luminosa. ¿Qué radio tiene?
2. Betelgeuse tiene unos 3600 K y una luminosidad total de unas 100 000 $L_\odot$. ¿Qué radio tiene, en radios solares y en unidades astronómicas ($1\ \text{ua} = 215\,R_\odot$)?
3. Sirio B, la compañera de Sirio, tiene unos 25 000 K y 0,025 $L_\odot$. ¿Qué radio tiene? Compáralo con la Tierra ($R_\oplus = 0{,}0092\,R_\odot$).

<details>
<summary>Soluciones</summary>

1. $L \propto R^2$ a igual temperatura: $R = \sqrt{100} =$ **10 radios solares**.
2. $R/R_\odot = \sqrt{L/L_\odot}\,(T_\odot/T)^2 = \sqrt{10^5} \cdot (5772/3600)^2 \approx 316 \cdot 2{,}57 \approx$ **810 radios solares**, unas **3,8 ua**. Puesta en el lugar del Sol, llegaría más allá de la órbita de Marte.
3. $R/R_\odot = \sqrt{0{,}025}\cdot(5772/25\,000)^2 \approx 0{,}158 \cdot 0{,}0533 \approx$ **0,0084**: un poco menos que la Tierra.

</details>

### Sesión 2 · Matemáticas: la masa decide la vida (35-40 min)

**La relación masa-luminosidad.** Arthur Eddington descubrió en 1924, con estrellas dobles cuyas masas se conocían por sus órbitas (semana 22), que en las estrellas de la secuencia principal la luminosidad depende de la masa con una ley de potencias aproximada:

$$\frac{L}{L_\odot} \approx \left(\frac{M}{M_\odot}\right)^{3{,}5}.$$

El exponente no es exacto: varía entre 3 y 4 según el rango de masas. Pero el mensaje es enorme. Una estrella con el doble de masa que el Sol brilla unas $2^{3{,}5} \approx 11$ veces más; una de 10 masas solares, unas 3000 veces más.

**La duración de la vida.** En la semana 34 viste que el combustible de una estrella va como su masa, y que lo gasta al ritmo de su luminosidad. Así que su vida va como

$$t \propto \frac{M}{L} \propto \frac{M}{M^{3{,}5}} = M^{-2{,}5}, \qquad t \approx 10^{10}\ \text{años}\cdot\left(\frac{M}{M_\odot}\right)^{-2{,}5}.$$

Las estrellas grandes tienen más combustible, pero lo queman muchísimo más deprisa. Una de 10 masas solares vive unos 30 millones de años; una de 0,2 masas solares, más de 500 000 millones de años según la fórmula (y en realidad aún más, porque las enanas rojas mezclan todo su gas por convección y aprovechan casi todo su hidrógeno), mucho más que la edad del universo. Ninguna enana roja ha muerto todavía.

**Ejercicios**

1. ¿Cuánto vive una estrella de 2 masas solares? ¿Y una de 20?
2. Despeja: ¿qué masa tiene una estrella de la secuencia principal que vive 1000 millones de años?
3. En una gráfica log-log de $L$ frente a $M$, ¿qué pendiente tiene la relación? ¿Y en una de $t$ frente a $M$?

<details>
<summary>Soluciones</summary>

1. $10^{10}\cdot2^{-2{,}5} \approx$ **1800 millones de años**; $10^{10}\cdot20^{-2{,}5} \approx$ **5,6 millones de años**.
2. $M^{-2{,}5} = 0{,}1$, $M = 0{,}1^{-0{,}4} = 10^{0{,}4} \approx$ **2,5 masas solares**.
3. **3,5** y **−2,5**.

</details>

### Sesión 3 · Física: el diagrama HR y la vida de las estrellas (40-45 min)

**Lo que muestra el diagrama.** Si colocas miles de estrellas en el diagrama HR, no se reparten al azar. Se agrupan en unas pocas zonas:

- **La secuencia principal**, una banda diagonal desde arriba a la izquierda (azules, calientes y luminosas) hasta abajo a la derecha (rojas, frías y débiles). Aquí está el 90 % de las estrellas, incluido el Sol. Son estrellas que funden hidrógeno en su núcleo, y su posición en la banda la decide la **masa**: las de arriba son las de más masa.
- **Las gigantes y supergigantes**, arriba a la derecha: frías pero muy luminosas, y por tanto enormes, como Aldebarán, Arturo o Betelgeuse.
- **Las enanas blancas**, abajo a la izquierda: calientes pero débiles, del tamaño de la Tierra, como Sirio B.

**Por qué el 90 % está en la secuencia principal.** Porque es la etapa más larga de la vida de una estrella: la de fundir hidrógeno en el núcleo. Las demás son etapas más cortas. Es como si en tu paseo por el bosque vieras sobre todo árboles adultos: no porque no haya brotes, sino porque un árbol pasa mucho más tiempo siendo adulto que siendo brote.

**El nacimiento.** Las estrellas nacen en **nubes moleculares**: nubes frías (unos 10 K) y relativamente densas de hidrógeno molecular y polvo, como la que hay detrás de la nebulosa de Orión. Si una parte de la nube es lo bastante masiva y fría, su gravedad vence a la presión del gas y se contrae (lo ves en el apartado opcional). Al contraerse se calienta (semana 34) y forma una **protoestrella**, rodeada de un **disco** de gas y polvo que gira; de ese disco nacen los planetas. Cuando el centro llega a unos 10 millones de grados, se enciende la fusión del hidrógeno, y la estrella entra en la secuencia principal. Un viento intenso barre los restos de la nube, y el gas que queda, iluminado por las estrellas jóvenes y calientes, brilla en rojo de hidrógeno (semana 32): es una **nebulosa de emisión**, como M42.

**La vejez.** Cuando se agota el hidrógeno del núcleo, el núcleo de helio se contrae y se calienta, el hidrógeno empieza a arder en una capa a su alrededor, y las capas externas se hinchan y se enfrían: la estrella se convierte en una **gigante roja**, y en el diagrama se va hacia arriba a la derecha. Al Sol le pasará dentro de unos 5000 millones de años: llegará a tener unas cien o doscientas veces su radio actual, y probablemente engullirá a Mercurio y a Venus. Después fundirá helio en carbono y oxígeno durante un tiempo. Lo que pasa al final depende de la masa (semana 36).

**Los cúmulos, relojes de estrellas.** En un **cúmulo**, todas las estrellas nacieron a la vez, de la misma nube, y están a la misma distancia. Su diagrama HR es una foto de estrellas de distintas masas con la misma edad. Las de más masa, que viven menos, ya han salido de la secuencia principal; las de menos, siguen en ella. El punto donde la secuencia se dobla hacia las gigantes, el **punto de desvío**, marca la edad del cúmulo: es la masa cuya vida coincide con la edad. Así se miden, por ejemplo:

| Cúmulo | Edad aproximada | Distancia aproximada |
|---|---|---|
| Pléyades (M45) | unos 100 millones de años | 136 pc (444 años luz) |
| Híades (alrededor de Aldebarán) | unos 650 millones de años | 47 pc (153 años luz) |
| Pesebre (M44) | unos 600-700 millones de años | 180 pc |
| M67 | unos 4000 millones de años | unos 850 pc |

(Aldebarán no pertenece a las Híades: está a menos de la mitad de distancia, en la misma dirección.)

:::note[De dónde viene la palabra]
**Gigante** viene del griego *gígas, gígantos*, los gigantes de la mitología, hijos de la Tierra. **Enano** viene del latín *nanus*, del griego *nânos*: de ahí también *nano-*, el prefijo de «una milmillonésima». **Secuencia** viene de *sequi*, «seguir»: una fila de cosas que se siguen unas a otras. Las letras **M** de M42 o M45 vienen del catálogo de Charles Messier, un cazador de cometas francés que entre 1758 y 1781 apuntó un centenar de manchas difusas del cielo para no confundirlas con cometas. Sin pretenderlo, hizo una lista de los objetos más bonitos para pequeños telescopios.
:::

**Qué hacer**

1. Una estrella está en la secuencia principal con 3 masas solares. ¿Qué luminosidad tiene? ¿Cuánto vive?
2. En el diagrama de un cúmulo, el punto de desvío está en estrellas de 2,5 masas solares. ¿Qué edad tiene el cúmulo? ¿A qué cúmulo de la tabla se parece?
3. ¿Por qué no hay estrellas en la secuencia principal con más de unas 150 masas solares ni con menos de unas 0,08? (Pista para la segunda: piensa en la temperatura central de la semana 34.)

### Sesión 4 · Astronomía y observación: viveros y cementerios de estrellas (30-45 min)

Las noches de otoño e invierno son las mejores para ver estrellas jóvenes. Con tus prismáticos 8×30, desde un lugar algo oscuro:

- **Las Pléyades (M45)**, en Tauro: unas decenas de estrellas azuladas en lugar de las seis o siete a simple vista. Son estrellas jóvenes y calientes, de tipo B. En fotografías de larga exposición aparecen envueltas en un velo azul: polvo que refleja su luz (una **nebulosa de reflexión**), que no forma parte de su nube de origen, sino de una nube por la que pasan ahora.
- **Las Híades**, la «V» de estrellas alrededor de Aldebarán: un cúmulo más viejo y más cercano, tan grande que llena el campo de los prismáticos. Compara su color con el de las Pléyades: hay más estrellas amarillentas y alguna gigante naranja.
- **La nebulosa de Orión (M42)**, bajo el cinturón, a partir de las 22:00 en noviembre: una mancha de luz con varias estrellas dentro. Es la región de formación de estrellas masivas más cercana, a unos 400 pc. En el centro hay un pequeño grupo de estrellas jóvenes y muy calientes, el **Trapecio**, que ilumina el gas; con 8 aumentos se ve como una estrella algo «gorda».
- **El cúmulo doble de Perseo**, entre Perseo y Casiopea: dos cúmulos jóvenes a unos 2300 pc, uno junto al otro.
- **M36, M37 y M38**, en Auriga, y **M35**, a los pies de Géminis: manchas granulosas, cúmulos de cientos de estrellas a entre unos 800 y 1400 pársecs.
- **El Pesebre (M44)**, en Cáncer, sale en noviembre hacia medianoche: un enjambre de estrellas que a simple vista es una mancha y con prismáticos se resuelve.

**Dos consejos.** Para los objetos débiles, usa la **visión lateral**: mira un poco al lado del objeto, no directamente. Los bastones, las células de la retina más sensibles a la luz débil, abundan fuera del centro de la retina, donde están los conos (semana 31). Y dibuja lo que ves: un círculo, las estrellas principales y la forma de la mancha. Dibujar te obliga a mirar con atención, y en una segunda noche verás más.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 35:

- carga casi tres mil estrellas reales de la base de datos HYG (las que están a menos de 25 pc y las más brillantes que la magnitud 4) y dibuja su diagrama HR,
- marca estrellas conocidas y dibuja líneas de radio constante,
- ajusta en una gráfica log-log la relación masa-luminosidad con masas de estrellas dobles,
- simula el diagrama HR de un cúmulo de estrellas de distintas edades y ve cómo baja el punto de desvío.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-35.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-35.ipynb)

## Qué has aprendido

- **La respuesta.** Las estrellas nacen de nubes frías de gas y polvo que se contraen por su gravedad, pasan la mayor parte de su vida en la secuencia principal fundiendo hidrógeno y, al agotarlo, se hinchan como gigantes. La masa lo decide todo: cuánto brillan, cuánto viven y cómo mueren.
- **Cómo lo sabemos.** Ordenando muchas estrellas en el diagrama HR y comparando cúmulos de distintas edades, como quien estudia un bosque.
- **Las herramientas.** Las gráficas log-log, las líneas de radio constante en el diagrama HR, la relación masa-luminosidad y la vida de una estrella como ley de potencias.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**¿Cuándo se colapsa una nube? La masa de Jeans.** Una nube de gas tiene dos tendencias opuestas: la gravedad intenta comprimirla y la agitación térmica de sus moléculas intenta dispersarla. En 1902, James Jeans calculó cuándo gana la gravedad.

Para una nube esférica de masa $M$, radio $R$ y temperatura $T$:

- su energía gravitatoria es del orden de $\frac{3}{5}\frac{GM^2}{R}$,
- su energía térmica es $\frac{3}{2}N k_B T$, con $N = M/(\mu m_H)$ partículas, donde $m_H$ es la masa del átomo de hidrógeno y $\mu$ la masa media de una partícula en esas unidades (unos 2,3 en una nube molecular, porque el hidrógeno va en moléculas H₂ y hay algo de helio).

Un resultado de la mecánica, el **teorema del virial**, dice que una nube en equilibrio tiene una energía gravitatoria igual al doble de la térmica. Si la gravitatoria es mayor, la nube se colapsa:

$$\frac{3}{5}\frac{GM^2}{R} > 3\frac{M}{\mu m_H}k_B T \quad\Longrightarrow\quad M > \frac{5 k_B T R}{G \mu m_H}.$$

Escribiendo el radio en función de la densidad, $R = (3M/(4\pi\rho))^{1/3}$, y despejando $M$, sale la **masa de Jeans**:

$$M_J = \left(\frac{5 k_B T}{G \mu m_H}\right)^{3/2}\left(\frac{3}{4\pi\rho}\right)^{1/2}.$$

Las nubes **frías** y **densas** tienen una masa de Jeans pequeña y se fragmentan en estrellas; las calientes y diluidas, no. Por eso las estrellas nacen en los rincones más fríos y oscuros de la galaxia.

**Ejercicios**

1. Calcula $M_J$ para un núcleo de nube molecular con $T = 10$ K y $10^{10}$ moléculas por metro cúbico (es decir, $10^4$ por centímetro cúbico), con $\mu = 2{,}3$ y $m_H = 1{,}67\times10^{-27}$ kg. Pásalo a masas solares.
2. ¿Cómo cambia $M_J$ si la nube está a 100 K y es cien veces menos densa?
3. Despeja $M$ en la desigualdad $M^{2/3} > \frac{5 k_B T}{G \mu m_H}\left(\frac{3}{4\pi\rho}\right)^{1/3}$ para comprobar la fórmula de $M_J$.

<details>
<summary>Soluciones</summary>

1. $\rho = 10^{10}\cdot2{,}3\cdot1{,}67\times10^{-27} = 3{,}8\times10^{-17}$ kg/m³. $5k_BT/(G\mu m_H) = 6{,}9\times10^{-22}/2{,}56\times10^{-37} = 2{,}7\times10^{15}$; elevado a 3/2, $1{,}4\times10^{23}$. $(3/(4\pi\rho))^{1/2} = 7{,}9\times10^7$. $M_J \approx 1{,}1\times10^{31}$ kg, unas **5 masas solares**.
2. Diez veces más caliente multiplica por $10^{3/2} \approx 32$; cien veces menos densa, por $\sqrt{100} = 10$. En total, unas **320 veces más**: unas 1700 masas solares. Una nube así no forma estrellas sueltas.
3. Elevando los dos lados a 3/2: $M > \left(\frac{5 k_B T}{G \mu m_H}\right)^{3/2}\left(\frac{3}{4\pi\rho}\right)^{1/2}$.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [18.4 El diagrama H-R, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/18%3A_Las_Estrellas_-_Un_Censo_Celestial/18.04%3A_El_diagrama_H-R). Español; el diagrama, la secuencia principal y las enanas blancas. Verificado el 20 de noviembre de 2026.
2. [18.2 Medición de masas estelares, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/18%3A_Las_Estrellas_-_Un_Censo_Celestial/18.02%3A_Medici%C3%B3n_de_masas_estelares). Español; estrellas dobles y la relación masa-luminosidad. Verificado el 20 de noviembre de 2026.
3. [Capítulo 21, El nacimiento de las estrellas, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/21%3A_El_nacimiento_de_las_estrellas_y_el_descubrimiento_de_planetas_fuera_del_Sistema_Solar). Español; nubes moleculares, protoestrellas y discos. Verificado el 20 de noviembre de 2026.
4. [Capítulo 22, Estrellas de la adolescencia a la vejez, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/22%3A_Estrellas_de_la_Adolescencia_a_la_Vejez). Español; gigantes rojas y diagramas HR de cúmulos. Verificado el 20 de noviembre de 2026.
5. Base de datos HYG, de David Nash (Astronexus), en [codeberg.org/astronexus/hyg](https://codeberg.org/astronexus/hyg). Licencia CC BY-SA 4.0. El cuaderno usa un subconjunto descrito en la carpeta de datos del repositorio. **(Sin verificar** la web de Codeberg; los datos se han obtenido de su copia de archivo en GitHub).

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno. Los datos de estrellas proceden de la base HYG v4.1 (David Nash, CC BY-SA 4.0).
