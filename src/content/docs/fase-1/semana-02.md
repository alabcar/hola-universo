---
title: "Semana 2 · ¿Cuánto mide el cielo?"
description: "Fase 1 · Principios básicos de astronomía. Ángulos, minutos y segundos de arco, el número π, radianes y tamaño aparente del Sol y de la Luna."
sidebar:
  order: 2
  label: "2. ¿Cuánto mide el cielo?"
---

## La pregunta del cielo

En el cielo no se miden metros, se miden ángulos. No sabes a simple vista si la Luna está a 380 000 km o a 38 000, pero sí puedes decir cuánto del cielo ocupa. Esa es la única medida que tienes directamente, y de ella se deduce casi todo lo demás. Un hecho curioso la acompaña: el Sol y la Luna, tan distintos, ocupan prácticamente el mismo trozo de cielo.

Esta semana aprendes qué es exactamente un ángulo y cómo se mide, a medirlos en el cielo con la mano, a calcularlos a partir de tamaños y distancias reales, y a responder por qué algunos eclipses de Sol son totales y otros dejan un anillo.

## Las cinco sesiones

### Sesión 1 · Matemáticas: grados, minutos y segundos de arco (35-40 min)

**Qué es un ángulo.** Un ángulo es la abertura entre dos líneas que salen de un mismo punto, el **vértice**. En el cielo, el vértice es tu ojo: cuando dices que dos estrellas están separadas 10°, hablas del ángulo que forman las dos líneas que van de tu ojo a cada estrella. No dice nada de lo lejos que están; solo de cuánto tienes que girar la mirada para pasar de una a otra.

**El grado.** La unidad más común es el grado. Una vuelta completa tiene 360°, media vuelta 180°, un ángulo recto 90°. El número 360 se remonta a la astronomía de Mesopotamia, que contaba en base 60 (los babilonios usaban el 60 como nosotros usamos el 10). Una explicación habitual de por qué eligieron 360 partes es que el Sol avanza entre las estrellas casi exactamente una de ellas cada día, porque el año tiene algo más de 360 días. Además, 360 se puede dividir exactamente entre 2, 3, 4, 5, 6, 8, 9, 10, 12, 15... lo que facilita mucho las cuentas sin decimales.

**Minutos y segundos de arco.** Los ángulos en astronomía suelen ser pequeños, así que el grado se divide, otra vez en base 60. Un grado tiene 60 **minutos de arco** (′) y un minuto tiene 60 **segundos de arco** (″). Es el mismo sistema que el de las horas, y por la misma razón histórica. Para pasar de grados, minutos y segundos a grados con decimales, se divide cada parte por lo que vale un grado:

$$31'\,56'' = \frac{31}{60} + \frac{56}{3600} \approx 0{,}5322^\circ.$$

Para el camino inverso, se multiplica la parte decimal por 60: $0{,}5322^\circ \cdot 60 = 31{,}93'$, y $0{,}93' \cdot 60 \approx 56''$.

**El cielo gira.** Un detalle útil: como la Tierra da una vuelta cada 24 horas, el cielo parece girar a su alrededor $360^\circ / 24 = 15^\circ$ por hora. Si una estrella está ahora en un punto, dentro de una hora estará 15° más al oeste.

:::note[De dónde viene la palabra]
**Minuto** y **segundo** vienen del latín medieval. Los astrónomos llamaban a la primera división del grado en 60 partes *pars minuta prima*, «primera parte pequeña», y a la siguiente división, *pars minuta secunda*, «segunda parte pequeña». De la primera quedó *minuto*, y de la segunda, *segundo*. Las mismas palabras pasaron a las horas. **Grado** viene del latín *gradus*, «paso, peldaño». **Ángulo** viene de *angulus*, «rincón, esquina».
:::

**Ejercicios (sin calculadora salvo el 1)**

1. Convierte 31′ 56″ a grados decimales.
2. ¿Cuántos minutos de arco son 0,5°?
3. ¿Cuántos segundos de arco tiene una circunferencia completa?
4. Suma 23° 44′ y 18° 29′.
5. ¿Cuántos grados se desplaza el cielo en 20 minutos?

<details>
<summary>Soluciones</summary>

1. 31/60 + 56/3600 ≈ 0,5167 + 0,0156 = 0,5322°.
2. 0,5 · 60 = 30′.
3. 360 · 60 · 60 = 1 296 000″.
4. 44′ + 29′ = 73′ = 1° 13′, así que 23° + 18° + 1° = 42° y quedan 13′: **42° 13′**.
5. 20 min = 1/3 de hora, y 15° · 1/3 = **5°**.

</details>

### Sesión 2 · Matemáticas: el número π, los radianes y el tamaño angular (35-45 min)

**El número π.** Si mides el contorno de cualquier círculo (una taza, una rueda, un plato) y lo divides por su diámetro, siempre sale el mismo número, un poco mayor que 3. Ese número se llama **pi** y se escribe $\pi$:

$$\pi = \frac{\text{circunferencia}}{\text{diámetro}} \approx 3{,}14159.$$

No depende del tamaño del círculo: es una propiedad de la forma. Por eso la longitud de una circunferencia de radio $r$ (y diámetro $2r$) es $2\pi r$. Sus cifras decimales no terminan nunca ni se repiten; para casi todos los cálculos de esta web bastan cuatro o cinco.

**El radián.** El grado es una unidad arbitraria: el 360 es una elección histórica. Hay una forma más natural de medir ángulos, que usa el propio círculo. Dibuja una circunferencia de radio $r$ y, desde el centro, abre un ángulo hasta que el arco que recorta mida exactamente lo mismo que el radio. Ese ángulo es **un radián**. Como la circunferencia completa mide $2\pi r$, caben en ella $2\pi$ radios: una vuelta completa son $2\pi$ radianes, unos 6,28. Por tanto

$$1\ \text{rad} = \frac{360^\circ}{2\pi} \approx 57{,}2958^\circ.$$

**Por qué es útil.** La ventaja del radián es que relaciona directamente ángulo y longitud. Un ángulo de $\theta$ radianes recorta, en una circunferencia de radio $r$, un arco de longitud

$$s = r\,\theta.$$

Con grados, esa fórmula necesitaría un factor $\pi/180$ incómodo. Por eso la física y la programación usan radianes casi siempre.

**El tamaño angular.** Ahora la aplicación. Un objeto de tamaño $d$ (la Luna, por ejemplo) está a una distancia $D$ de tu ojo. Imagina una circunferencia centrada en tu ojo con radio $D$: el objeto es casi un trocito de esa circunferencia. Si $D$ es mucho mayor que $d$, el segmento recto y el arco apenas se distinguen, y de $s = r\,\theta$ sale

$$\theta \approx \frac{d}{D} \quad (\text{en radianes}),$$

que se pasa a grados multiplicando por 57,2958. Es una aproximación, y en el cuaderno ves cuánto se equivoca: para ángulos pequeños, nada que se note.

**Ejemplo resuelto.** El diámetro del Sol es 1,3914 × 10⁶ km y su distancia media, 1,496 × 10⁸ km. Entonces $\theta \approx 1{,}3914\times10^{6} / 1{,}496\times10^{8} = 0{,}0093$ rad, es decir $0{,}0093 \cdot 57{,}2958 \approx 0{,}533^\circ \approx 32'$. Para la Luna: $3474 / 384\,400 = 0{,}00904$ rad $\approx 0{,}518^\circ \approx 31'$. Son casi iguales.

:::note[De dónde viene la palabra]
**Pi** es la letra griega *p*, inicial de *periphéreia*, «contorno, circunferencia» (de *perí*, «alrededor», y *phérein*, «llevar»). El matemático galés William Jones la usó para este número en 1706, y Leonhard Euler la popularizó unas décadas después. **Radián** viene de *radio*, del latín *radius*, «rayo, varilla de una rueda»: el ángulo que mide un radio. El nombre es reciente; se empezó a usar hacia 1873. **Diámetro** es griego: *diá*, «a través», y *métron*, «medida».
:::

**Ejercicios**

1. Expresa 0,0093 rad en minutos de arco.
2. ¿Qué ángulo abarca una barra de 1 m vista desde 100 m?
3. La Tierra mide 12 742 km de diámetro. ¿Qué ángulo abarcaría vista desde la Luna? ¿Cuántas veces mayor es que el que abarca la Luna vista desde la Tierra?
4. Un ojo sano resuelve aproximadamente 1 minuto de arco. ¿Qué tamaño mínimo debe tener un objeto a 1 km para distinguirse como tal?

<details>
<summary>Soluciones</summary>

1. 0,0093 · 57,2958 · 60 ≈ **32′**.
2. 1/100 = 0,01 rad ≈ **0,573°**, unos 34′.
3. 12 742 / 384 400 = 0,0331 rad ≈ **1,9°**, unas **3,7 veces** el ángulo de la Luna (0,518°).
4. 1′ = 1/60 · π/180 = 2,91 × 10⁻⁴ rad, y 1000 m · 2,91 × 10⁻⁴ ≈ **0,29 m**.

</details>

### Sesión 3 · Física: tamaño aparente y distancia (30-40 min)

**El tamaño aparente no es una propiedad del objeto.** Depende de cuánto mide y de a qué distancia está, y solo de su cociente $d/D$. Una moneda de 2 cm a 2 m de ti y un edificio de 20 m a 2 km se ven del mismo tamaño. Por eso, mirando el cielo, no puedes saber cuál de dos objetos es mayor si no sabes a qué distancia está cada uno.

El Sol es unas 400 veces mayor que la Luna y está unas 390 veces más lejos, de modo que su cociente $d/D$ es casi idéntico. Es una coincidencia sin explicación física conocida, y es la razón de que veas eclipses totales.

**Qué es un eclipse de Sol.** Un eclipse de Sol ocurre cuando la Luna pasa justo por delante del Sol, vista desde algún lugar de la Tierra. Solo puede pasar en luna nueva, cuando la Luna está entre la Tierra y el Sol (lo verás en la semana 5). Si la Luna parece más grande que el Sol, lo tapa entero y el eclipse es **total**: durante unos minutos se hace casi de noche y se ve la corona, la atmósfera exterior del Sol. Si parece más pequeña, deja un borde brillante alrededor y el eclipse es **anular**.

**Las distancias cambian.** Ninguna de las dos distancias es constante, porque las órbitas no son circulares sino ligeramente alargadas (elipses, que estudiarás en la semana 14). El punto de la órbita de la Luna más cercano a la Tierra se llama **perigeo**, y el más lejano, **apogeo**; para la Tierra alrededor del Sol se dice **perihelio** y **afelio**.

| Cuerpo | Distancia mínima | Distancia máxima | Diámetro aparente |
|---|---|---|---|
| Sol | 147,1 millones de km (perihelio) | 152,1 millones de km (afelio) | 31,4′ a 32,5′ |
| Luna | unos 356 400 km (perigeo) | unos 406 700 km (apogeo) | 29,4′ a 33,5′ |

(Los valores del Sol vienen de la ficha de la Tierra de la NASA. Los de la Luna son los habituales de las efemérides y varían de un ciclo a otro, así que son aproximados.) Los rangos se solapan. Si la Luna está cerca del perigeo, parece mayor que el Sol y puede tapar todo el disco (eclipse total); si está lejos, parece menor y deja un anillo (eclipse anular).

**La ilusión de la Luna.** Cerca del horizonte, la Luna parece mucho más grande que en lo alto del cielo, pero no lo es. Es una ilusión de la percepción, todavía discutida, y se comprueba tapándola con un dedo en los dos momentos. De hecho, en el horizonte la Luna está algo más lejos de ti que cuando está en lo alto: cuando está sobre tu cabeza te separa de ella la distancia al centro de la Tierra menos un radio terrestre, y en el horizonte, casi la distancia completa. La diferencia es de casi un radio terrestre, un 1,7 %, y su tamaño aparente en el horizonte es ligeramente menor.

:::note[De dónde viene la palabra]
**Eclipse** viene del griego *ékleipsis*, «abandono, desaparición», del verbo *ekleípein*, «dejar, faltar»: el Sol o la Luna desaparecen del cielo. **Anular** viene del latín *anulus*, «anillo pequeño», como el anillo que deja el Sol alrededor de la Luna. **Corona** es la palabra latina para «guirnalda, corona», por el halo que rodea al Sol tapado.
:::

**Qué hacer**

1. Verifica en tu cuaderno de notas que el cociente $d/D$ del Sol y de la Luna sale casi igual.
2. Calcula el tamaño aparente de la Luna en el perigeo y en el apogeo con la tabla y la fórmula $\theta \approx d/D$.
3. Responde por escrito: si la Luna se alejara el doble de la Tierra, ¿podría haber eclipses totales de Sol?

### Sesión 4 · Astronomía y observación (30-45 min)

**Tu mano es un instrumento de medida.** Con el brazo extendido, tu mano está a unos 55-65 cm del ojo. Por la fórmula $\theta \approx d/D$, a 57 cm de distancia un objeto de 1 cm abarca casi exactamente 1° (porque $1/57{,}3$ rad = 1°). Un dedo de 1,5 cm abarca un grado y medio; un puño de 10 cm, unos 10°. Y funciona para casi todo el mundo, porque quien tiene los brazos largos suele tener también las manos grandes. A brazo extendido, los valores habituales son:

| Parte de la mano | Ángulo aproximado |
|---|---|
| Punta del dedo índice | 1° |
| Dedos índice y corazón separados (en V) | 5° |
| Puño cerrado | 10° |
| Mano abierta, del pulgar al meñique | 20° |

La Luna llena ocupa unos 0,5°, es decir, la mitad de la punta de tu dedo. Estas reglas varían de una persona a otra, así que **calibra las tuyas**: el cuaderno de la sesión 5 te enseña cómo.

**Qué hacer**

1. Una noche con Luna visible, tapa el disco con la punta del dedo a brazo extendido y comprueba cuántas Lunas caben en un dedo.
2. Con Stellarium, busca dos estrellas brillantes de una constelación conocida, anota la separación que ves a simple vista y compárala con la que muestra el programa (la versión de escritorio incluye una herramienta para medir ángulos).
3. Si no es posible una noche despejada, mide con la mano objetos terrestres de tamaño y distancia conocidos, por ejemplo la altura de un edificio.

No hagas nunca estas medidas con el Sol, ni siquiera con la mano: no mires nunca directamente a él.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 2:

- convierte entre grados decimales y grados, minutos y segundos,
- implementa el tamaño angular con la aproximación $d/D$ y con la fórmula exacta, y compara ambas,
- dibuja el rango de tamaño aparente del Sol y de la Luna a lo largo de sus órbitas,
- calibra el ángulo de tu mano con tus propias medidas.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-02.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-02.ipynb)

La fórmula exacta usa la función arcotangente, que verás en las semanas 6 y 7. Por ahora es una caja negra para medir el error de la aproximación.

## Qué has aprendido

- **La respuesta.** El cielo se mide en ángulos. El Sol y la Luna ocupan casi el mismo ángulo, unos 0,5° (31′ a 32′) en promedio, y por eso hay eclipses totales cuando la Luna parece algo mayor y anulares cuando parece algo menor.
- **La causa.** El tamaño aparente depende solo del cociente entre tamaño y distancia, y como las distancias varían a lo largo de órbitas elípticas, también varía el ángulo.
- **Las herramientas.** Qué es un ángulo; grados, minutos y segundos de arco y su origen en base 60; el número $\pi$; el radián y la relación $s = r\theta$; la aproximación $\theta \approx d/D$ y cuándo vale; y la mano como instrumento de medida calibrado.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [La esfera celeste y la observación a simple vista, astronomas.org](https://astronomas.org/files/documents/learning/esfera_celeste.pdf). Español, PDF didáctico de la Universidad de Barcelona para Bachillerato, con las equivalencias de la mano y la construcción de una cruceta. Verificado el 31 de octubre de 2026.
2. [Apéndice C: notación científica, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_%28OpenStax%29/31%3A_Ap%C3%A9ndices/31.03%3A_Notaci%C3%B3n_cient%C3%ADfica_%28Ap%C3%A9ndice_C%29). Español, para repasar potencias de 10 si hace falta. Verificado el 31 de octubre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**: no he podido abrirlos desde mi entorno.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
