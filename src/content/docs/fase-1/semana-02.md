---
title: "Semana 2 · ¿Cuánto mide el cielo?"
description: "Fase 1 · Principios básicos de astronomía. Ángulos, radianes y tamaño aparente del Sol y de la Luna."
sidebar:
  order: 2
  label: "2. ¿Cuánto mide el cielo?"
---

## La pregunta del cielo

En el cielo no se miden metros, se miden ángulos. No sabes a simple vista si la Luna está a 380 000 km o a 38 000, pero sí puedes decir cuánto del cielo ocupa. Esa es la única medida que tienes directamente, y de ella se deduce casi todo lo demás. Un hecho curioso la acompaña: el Sol y la Luna, tan distintos, ocupan prácticamente el mismo trozo de cielo.

Esta semana aprendes a medir ángulos en el cielo con la mano, a calcularlos a partir de tamaños y distancias reales, y a responder por qué algunos eclipses de Sol son totales y otros dejan un anillo.

## Las cinco sesiones

### Sesión 1 · Matemáticas: grados, minutos y segundos de arco (30-35 min)

Un ángulo se mide en grados. Una circunferencia completa tiene 360°, un grado se divide en 60 **minutos de arco** (′) y cada minuto en 60 **segundos de arco** (″). Los ángulos en astronomía son tan pequeños que los minutos y los segundos de arco son de uso diario. Un detalle útil: como la Tierra da una vuelta cada 24 horas, el cielo se desplaza 360° / 24 = 15° por hora.

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

### Sesión 2 · Matemáticas: radianes y tamaño angular (30-40 min)

Un **radián** es el ángulo que abarca un arco de longitud igual al radio. Como la circunferencia mide $2\pi r$, una vuelta completa son $2\pi$ radianes, y por tanto

$$1\ \text{rad} = \frac{360^\circ}{2\pi} \approx 57{,}2958^\circ.$$

La ventaja del radián es que relaciona directamente ángulo y longitud. Un objeto de tamaño $d$ visto desde una distancia $D$ mucho mayor abarca un ángulo

$$\theta \approx \frac{d}{D} \quad (\text{en radianes}),$$

que se pasa a grados multiplicando por 57,2958. Es una aproximación, y en el cuaderno ves cuánto se equivoca: para ángulos pequeños, nada que se note.

**Ejemplo resuelto.** El diámetro del Sol es 1,3914 × 10⁶ km y su distancia media, 1,496 × 10⁸ km. Entonces $\theta \approx 1{,}3914\times10^{6} / 1{,}496\times10^{8} = 0{,}0093$ rad, es decir $0{,}0093 \cdot 57{,}2958 \approx 0{,}533^\circ \approx 32'$. Para la Luna: $3474 / 384\,400 = 0{,}00904$ rad $\approx 0{,}518^\circ \approx 31'$. Son casi iguales.

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

El tamaño aparente de un objeto no es una propiedad suya: depende de cuánto mide y de a qué distancia está. El Sol es unas 400 veces mayor que la Luna y está unas 390 veces más lejos, de modo que su cociente $d/D$ es casi idéntico. Es una coincidencia sin explicación física conocida, y es la razón de que veas eclipses totales.

Pero ninguna de las dos distancias es constante, porque las órbitas son elípticas:

| Cuerpo | Distancia mínima | Distancia máxima | Diámetro aparente |
|---|---|---|---|
| Sol | 147,1 millones de km (perihelio) | 152,1 millones de km (afelio) | 31,4′ a 32,5′ |
| Luna | unos 356 400 km (perigeo) | unos 406 700 km (apogeo) | 29,4′ a 33,5′ |

(Los valores del Sol vienen de la ficha de la Tierra de la NASA. Los de la Luna son los habituales de las efemérides y varían de un ciclo a otro, así que son aproximados.) Los rangos se solapan. Si la Luna está cerca del perigeo, parece mayor que el Sol y puede tapar todo el disco (eclipse total); si está lejos, parece menor y deja un anillo (eclipse anular).

Una nota sobre la ilusión de la Luna: cerca del horizonte parece más grande que en lo alto del cielo, pero no lo es. Es una ilusión perceptiva, y se comprueba midiéndola con un dedo. De hecho, en el horizonte la Luna está algo más lejos (casi un radio terrestre, un 1,7 %) y su tamaño aparente es ligeramente menor.

**Qué hacer**

1. Verifica en tu cuaderno de notas que el cociente $d/D$ del Sol y de la Luna sale casi igual.
2. Responde por escrito: si la Luna se alejara el doble de la Tierra, ¿podría haber eclipses totales de Sol?

### Sesión 4 · Astronomía y observación (30-45 min)

Tu mano es un instrumento de medida. A brazo extendido, los valores habituales son:

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
- **Las herramientas.** Conversión entre grados, minutos de arco y radianes; la aproximación $\theta \approx d/D$ y cuándo vale; y la mano como instrumento de medida calibrado.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [La esfera celeste y la observación a simple vista, astronomas.org](https://astronomas.org/files/documents/learning/esfera_celeste.pdf). Español, PDF didáctico de la Universidad de Barcelona para Bachillerato, con las equivalencias de la mano y la construcción de una cruceta. Verificado el 31 de octubre de 2026.
2. [Apéndice C: notación científica, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_%28OpenStax%29/31%3A_Ap%C3%A9ndices/31.03%3A_Notaci%C3%B3n_cient%C3%ADfica_%28Ap%C3%A9ndice_C%29). Español, para repasar potencias de 10 si hace falta. Verificado el 31 de octubre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**: no he podido abrirlos desde mi entorno.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
