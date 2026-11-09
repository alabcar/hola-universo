---
title: "Semana 22 · ¿Cómo se pesa un planeta?"
description: "Fase 2 · Órbitas. Notación científica y despeje con unidades; la masa a partir de la tercera ley de Kepler; las lunas de Júpiter con prismáticos."
sidebar:
  order: 22
  label: "22. ¿Cómo se pesa un planeta?"
---

## La pregunta del cielo

Nadie ha puesto Júpiter en una balanza, y sin embargo sabemos que su masa es de $1{,}898 \times 10^{27}$ kg, 318 veces la de la Tierra, con cuatro cifras de precisión. ¿Cómo?

La respuesta está en sus lunas. En la semana 17 viste que el periodo de una órbita depende de la masa del cuerpo central: $T^2 = 4\pi^2 r^3/(GM)$. Si mides el tamaño de la órbita de una luna y lo que tarda en recorrerla, puedes despejar $M$. Todo lo que tiene satélites se puede pesar así: la Tierra con la Luna, el Sol con los planetas, Júpiter con sus lunas, una estrella doble con su compañera, una galaxia con sus estrellas.

Las cuatro lunas grandes de Júpiter las descubrió Galileo en enero de 1610 con un telescopio de unos 20 aumentos. Hoy se ven con unos prismáticos corrientes. Esta semana las observas, calculas la masa de Júpiter con sus datos y repasas la notación científica y el despeje con unidades, que son el día a día del cálculo astronómico.

## Las cinco sesiones

### Sesión 1 · Matemáticas: notación científica sin miedo (30-40 min)

**Por qué hace falta.** La masa de Júpiter tiene 28 cifras antes de la coma. La constante $G$, 10 ceros después de la coma antes de la primera cifra significativa. Escribir esos números completos es incómodo y muy fácil de equivocar. La **notación científica** los escribe como un número entre 1 y 10 multiplicado por una potencia de 10:

$$1\,898\,000\,000\,000\,000\,000\,000\,000\,000 = 1{,}898 \times 10^{27}, \qquad 0{,}000\,000\,000\,066\,74 = 6{,}674 \times 10^{-11}.$$

El exponente cuenta cuántos lugares se mueve la coma: hacia la izquierda si es positivo, hacia la derecha si es negativo.

**Operar.** Las reglas son las de las potencias (semana 15). Se trabaja por separado con los números y con las potencias de 10:

- **Multiplicar:** se multiplican los números y se **suman** los exponentes. $(3 \times 10^{4}) \cdot (2 \times 10^{5}) = 6 \times 10^{9}$.
- **Dividir:** se dividen los números y se **restan** los exponentes. $(6 \times 10^{8}) / (3 \times 10^{-2}) = 2 \times 10^{10}$.
- **Potencias:** se eleva el número y se **multiplica** el exponente. $(2 \times 10^{3})^3 = 8 \times 10^{9}$.
- **Raíces:** como en la semana 17, se ajusta el exponente para que sea divisible y se divide.
- **Ajustar:** si el número resultante no está entre 1 y 10, se corre la coma y se corrige el exponente: $45 \times 10^{6} = 4{,}5 \times 10^{7}$.

**Sumar y restar** es lo único incómodo: hay que poner antes los dos números con el mismo exponente. $3 \times 10^{5} + 2 \times 10^{4} = 3 \times 10^{5} + 0{,}2 \times 10^{5} = 3{,}2 \times 10^{5}$. Y si los exponentes son muy distintos, el pequeño ni se nota: $10^{30} + 10^{24}$ es $10^{30}$ a efectos prácticos.

**En Python y en las calculadoras**, $6{,}674 \times 10^{-11}$ se escribe `6.674e-11`. La «e» significa «por diez elevado a».

:::note[De dónde viene la palabra]
**Júpiter** viene del latín *Iuppiter*, que a su vez viene de una forma antigua que significaba «padre cielo» o «padre del día»: *Iov-* (de la misma raíz que *dies*, «día», y que el griego *Zeús*) y *pater*, «padre». **Satélite** viene del latín *satelles*, «escolta, guardia personal». Kepler aplicó la palabra a las lunas de Júpiter en 1610 o 1611: acompañan al planeta como la escolta de un rey. Galileo las había llamado «estrellas mediceas», en honor de los Médici, sus mecenas. Los nombres de Ío, Europa, Ganimedes y Calisto, personajes de los mitos de Zeus, los propuso Simon Marius en 1614 a sugerencia de Kepler.
:::

**Ejercicios**

1. Escribe en notación científica: 384 400 km en metros; 27,32 días en segundos.
2. Calcula $(4{,}2 \times 10^{8})^3$.
3. Calcula $\dfrac{6 \times 10^{24} \cdot 7 \times 10^{22}}{(4 \times 10^{8})^2}$ sin calculadora, con una cifra.
4. Suma $1{,}989 \times 10^{30}$ y $1{,}898 \times 10^{27}$.

<details>
<summary>Soluciones</summary>

1. $3{,}844 \times 10^{8}$ m. $27{,}32 \cdot 86\,400 \approx 2{,}360 \times 10^{6}$ s.
2. $4{,}2^3 \approx 74{,}1$, así que $74{,}1 \times 10^{24} =$ **7,41 × 10²⁵**.
3. $42 \times 10^{46} / (16 \times 10^{16}) \approx 2{,}6 \times 10^{30}$, es decir, unos **3 × 10³⁰**.
4. $1{,}989 \times 10^{30} + 0{,}001898 \times 10^{30} \approx$ **1,991 × 10³⁰**: Júpiter apenas cambia la masa total.

</details>

### Sesión 2 · Matemáticas: despejar con unidades (30-35 min)

La fórmula de la semana 17, $T^2 = 4\pi^2 r^3/(GM)$, despejada para la masa, es

$$M = \frac{4\pi^2\,r^3}{G\,T^2}.$$

Antes de meter números, hay que poner todo en el **Sistema Internacional**: metros, segundos y kilogramos, porque $G$ está en esas unidades ($\text{N}\cdot\text{m}^2/\text{kg}^2 = \text{m}^3/(\text{kg}\cdot\text{s}^2)$). Comprueba las unidades del resultado: $\text{m}^3 / (\text{m}^3\,\text{kg}^{-1}\,\text{s}^{-2} \cdot \text{s}^2) = \text{kg}$. Sale una masa, como debe.

**El error más común** es mezclar unidades: radio en kilómetros y periodo en días. El resultado sale en unidades sin sentido y con un error de muchos órdenes de magnitud. Un método seguro es convertir primero cada dato a metros y segundos, en notación científica, y solo después sustituir.

**Ejemplo: la masa de la Tierra a partir de la Luna.** $r = 3{,}844 \times 10^{8}$ m y $T = 2{,}360 \times 10^{6}$ s.

$$M = \frac{39{,}48 \cdot (3{,}844 \times 10^{8})^3}{6{,}674 \times 10^{-11} \cdot (2{,}360 \times 10^{6})^2} = \frac{39{,}48 \cdot 5{,}680 \times 10^{25}}{6{,}674 \times 10^{-11} \cdot 5{,}570 \times 10^{12}} \approx 6{,}03 \times 10^{24}\ \text{kg}.$$

El valor aceptado es $5{,}97 \times 10^{24}$ kg. El 1 % de diferencia se debe a que la Luna no es despreciable frente a la Tierra: lo que hemos medido es la masa de la Tierra **más** la de la Luna (semana 20), que es $6{,}05 \times 10^{24}$ kg.

**Ejercicios**

1. Pesa el Sol con la órbita de la Tierra: $r = 1{,}496 \times 10^{11}$ m y $T = 365{,}26$ días.
2. Un satélite artificial da una vuelta a Marte en 7 h 39 min a unos 9380 km del centro del planeta. (Es Fobos, una de las lunas naturales de Marte.) ¿Qué masa tiene Marte?

<details>
<summary>Soluciones</summary>

1. $T = 3{,}156 \times 10^{7}$ s. $M = 39{,}48 \cdot 3{,}348 \times 10^{33} / (6{,}674 \times 10^{-11} \cdot 9{,}960 \times 10^{14}) \approx$ **1,99 × 10³⁰ kg**.
2. $T = 27\,540$ s y $r = 9{,}38 \times 10^{6}$ m. $M = 39{,}48 \cdot 8{,}25 \times 10^{20} / (6{,}674 \times 10^{-11} \cdot 7{,}58 \times 10^{8}) \approx$ **6,4 × 10²³ kg**, una décima parte de la masa de la Tierra.

</details>

### Sesión 3 · Física: pesar con órbitas (30-40 min)

**Una balanza universal.** Con la tercera ley de Kepler en la forma de Newton, cualquier cuerpo que orbita a otro lo convierte en una balanza. Lo que se mide son dos cosas: el periodo, que es fácil (solo hace falta un reloj y paciencia), y el tamaño de la órbita, que suele ser lo difícil. Desde la Tierra se mide un ángulo, la separación máxima entre la luna y el planeta en el cielo, y se convierte en distancia con la fórmula del tamaño angular de la semana 2:

$$r \approx D\,\theta,$$

donde $D$ es la distancia de la Tierra a Júpiter y $\theta$, la separación máxima en radianes. La distancia $D$ se conoce a partir de las órbitas (semana 15).

**Una comprobación de la teoría.** Con cada una de las cuatro lunas de Júpiter sale la misma masa, aunque sus órbitas sean muy distintas. Si la ley de Newton no fuera correcta, los cuatro resultados no coincidirían. Es la misma prueba que hizo Kepler con los planetas y el Sol, ahora en un sistema en miniatura. Las lunas de Júpiter fueron, además, la primera prueba directa de que no todo gira alrededor de la Tierra.

**Lo que no se puede pesar así.** La masa de la luna en sí no aparece en la fórmula (salvo como una pequeña corrección, semana 20). Para pesar una luna hace falta algo que la orbite a ella, o medir cómo perturba a otras lunas o a una nave espacial que pase cerca. Así se pesaron las lunas galileanas y los asteroides: por cómo desvían la trayectoria de las sondas.

**Qué hacer**

1. Calcula la masa de Júpiter con los datos de Ío: $r = 421\,700$ km y $T = 1{,}769$ días.
2. Repite con Calisto: $r = 1\,882\,700$ km y $T = 16{,}689$ días. ¿Coinciden?
3. Cuando Júpiter está en oposición, a unos 4,2 ua de la Tierra, ¿qué separación máxima, en minutos de arco, se ve entre Júpiter y Calisto?

<details>
<summary>Soluciones</summary>

1. $r = 4{,}217 \times 10^{8}$ m, $T = 1{,}528 \times 10^{5}$ s. $M = 39{,}48 \cdot 7{,}499 \times 10^{25} / (6{,}674 \times 10^{-11} \cdot 2{,}336 \times 10^{10}) \approx$ **1,90 × 10²⁷ kg**.
2. $r = 1{,}8827 \times 10^{9}$ m, $T = 1{,}442 \times 10^{6}$ s. $M \approx$ **1,90 × 10²⁷ kg**. Coinciden.
3. $D = 4{,}2 \cdot 1{,}496 \times 10^{8} \approx 6{,}28 \times 10^{8}$ km y $\theta = 1{,}883 \times 10^{6} / 6{,}28 \times 10^{8} \approx 0{,}0030$ rad $\approx$ **10′**, un tercio del diámetro de la Luna llena. Por eso caben las cuatro lunas en el campo de unos prismáticos.

</details>

### Sesión 4 · Astronomía y observación: las lunas de Júpiter con prismáticos (30-45 min)

**Dónde está Júpiter.** Júpiter llegará a la oposición el 11 de febrero de 2027. En noviembre de 2026 sale hacia la medianoche y se ve alto de madrugada, en la zona de Cáncer y Leo. Es el punto más brillante de esa parte del cielo, con una luz blanca y firme. Según la revista de divulgación EarthSky, hacia mediados de noviembre de 2026 Marte pasa muy cerca de Júpiter en el cielo: compruébalo en Stellarium y aprovecha para verlos juntos.

**Cómo observar.**

1. Usa unos prismáticos de 7 a 10 aumentos. Lo más importante es que no tiemblen: apóyalos en una valla, en el techo de un coche o en el respaldo de una silla, o sujétalos a un trípode con un adaptador.
2. Enfoca Júpiter. Verás un disco pequeño y, alineados a los lados, hasta cuatro puntitos de luz. No siempre se ven los cuatro: alguno puede estar delante o detrás del planeta, o demasiado cerca de su brillo.
3. Dibuja la posición de los puntos respecto a Júpiter. Usa el diámetro del disco como regla.
4. Repite la observación la noche siguiente a la misma hora, y si puedes, varias noches seguidas. Verás que los puntos cambian de lado. Ío se mueve tanto que puede cambiar de posición en pocas horas.
5. Compara tus dibujos con Stellarium, que muestra las cuatro lunas con su nombre, e identifica cada una.

Funciona bien incluso con un cielo urbano luminoso, porque Júpiter y sus lunas son brillantes. Lo que estás viendo es lo mismo que vio Galileo en enero de 1610, y lo que le convenció de que había cuerpos que giraban alrededor de algo que no era la Tierra.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 22:

- calcula la masa de Júpiter con cada una de sus cuatro lunas grandes, y la del Sol, la Tierra y Saturno con sus satélites,
- dibuja $T^2$ frente a $r^3$ para las lunas de Júpiter y obtiene la masa de la pendiente de la recta,
- simula unas observaciones de Calisto como las que harías con prismáticos (su separación de Júpiter cada noche, con un error de medida) y recupera de ellas el periodo, el tamaño de la órbita y la masa de Júpiter.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-22.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-22.ipynb)

## Qué has aprendido

- **La respuesta.** Un planeta se pesa con sus lunas. Midiendo el tamaño de la órbita de una luna y su periodo, la tercera ley de Kepler en la forma de Newton da la masa del planeta: $M = 4\pi^2 r^3/(G T^2)$. Con las cuatro lunas de Júpiter sale la misma masa, $1{,}90 \times 10^{27}$ kg, lo que confirma la ley.
- **El método.** El periodo se mide con un reloj; el tamaño de la órbita, con un ángulo y una distancia conocida. Es el mismo método con el que se pesan las estrellas y las galaxias.
- **Las herramientas.** Notación científica para operar con números enormes y diminutos, conversión de unidades al Sistema Internacional antes de sustituir y comprobación de las unidades del resultado.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 13.4, Órbita satelital y energía, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-4-orbita-satelital-y-energia). Español; la relación entre periodo, radio y masa central, con ejemplos. Verificado el 6 de noviembre de 2026.
2. [Unidad 5: Las leyes del movimiento planetario (Proyecto PETeR, Instituto de Astrofísica de Canarias)](https://outreach.iac.es/peter/wp-content/uploads/2025/10/Unidad-5-Leyes-del-Movimiento_Intro.pdf). Español, divulgativo; Galileo, sus observaciones y el paso al modelo heliocéntrico. Verificado el 6 de noviembre de 2026.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

Los periodos de las lunas galileanas los he contrastado en una fuente universitaria el 6 de noviembre de 2026; los radios de sus órbitas y los datos de Fobos y de Titán son valores redondeados de memoria. **(Sin verificar)**. La fecha de la oposición de Júpiter procede del Observatorio Astronómico Nacional de Japón, consultado el mismo día.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
