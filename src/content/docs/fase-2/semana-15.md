---
title: "Semana 15 · ¿Cuánto tarda un planeta en dar la vuelta?"
description: "Fase 2 · Órbitas. Proporciones, potencias y logaritmos; la tercera ley de Kepler; periodos sidéreos a partir de las oposiciones."
sidebar:
  order: 15
  label: "15. ¿Cuánto tarda un planeta en dar la vuelta?"
---

## La pregunta del cielo

Mercurio da la vuelta al Sol en tres meses; Saturno, en casi treinta años. Que los planetas lejanos tarden más era de esperar: tienen más camino que recorrer. Pero no es solo eso. Saturno está unas diez veces más lejos que la Tierra y su órbita es diez veces más larga, así que si fuera igual de rápido tardaría diez años. Tarda tres veces más: los planetas lejanos, además, van más despacio.

Kepler buscó durante años una regla que uniera distancias y periodos. La encontró en 1619 y la publicó en *Harmonices mundi* («Las armonías del mundo»): **el cuadrado del periodo es proporcional al cubo de la distancia media**. Es su tercera ley. Esta semana aprendes las matemáticas para entenderla y comprobarla (proporciones, potencias y logaritmos) y la usas con los datos reales del Sistema Solar.

## Las cinco sesiones

### Sesión 1 · Matemáticas: proporciones y potencias (30-40 min)

**Proporcionalidad.** Dos magnitudes son **proporcionales** si su cociente es siempre el mismo número. Si $y$ es proporcional a $x$, se escribe $y \propto x$, y significa que $y = k\,x$ para un número fijo $k$, la **constante de proporcionalidad**. Si $x$ se duplica, $y$ se duplica. El precio de la fruta es proporcional al peso, y $k$ es el precio por kilo.

Pero una magnitud puede ser proporcional al cuadrado o al cubo de otra. Si $y \propto x^2$, al duplicar $x$, $y$ se multiplica por 4. Si $y \propto x^3$, se multiplica por 8. Es lo que pasa con las áreas y los volúmenes: un cubo de lado doble tiene una cara cuatro veces mayor y un volumen ocho veces mayor.

**Potencias.** Recuerda las reglas básicas, con $a$ positivo:

- $a^m \cdot a^n = a^{m+n}$ y $a^m / a^n = a^{m-n}$.
- $(a^m)^n = a^{m \cdot n}$.
- $a^0 = 1$ y $a^{-n} = 1/a^n$.
- Un exponente fraccionario es una raíz: $a^{1/2} = \sqrt{a}$, $a^{1/3} = \sqrt[3]{a}$, y $a^{3/2} = (\sqrt{a})^3 = \sqrt{a^3}$.

La última regla es la que vas a usar más esta semana. Si $T^2 = a^3$, entonces $T = a^{3/2}$ y, al revés, $a = T^{2/3}$.

**Comparar en vez de calcular.** Las leyes de proporcionalidad se usan mejor comparando dos casos. Si $T^2 \propto a^3$ para todos los planetas, entonces para dos planetas cualesquiera

$$\left(\frac{T_1}{T_2}\right)^2 = \left(\frac{a_1}{a_2}\right)^3.$$

La constante desaparece. Y si el segundo planeta es la Tierra, con $a = 1$ ua y $T = 1$ año, queda simplemente $T^2 = a^3$, con $T$ en años y $a$ en unidades astronómicas.

:::note[De dónde viene la palabra]
**Potencia** viene del latín *potentia*, «poder, capacidad», que tradujo el griego *dýnamis*: Euclides llamaba así al cuadrado de una longitud, «lo que puede» generar. **Exponente** es el participio del latín *exponere*, «poner fuera, exponer»: el número que se pone fuera, arriba a la derecha. **Proporción** viene de *pro portione*, «según la parte que corresponde».
:::

**Ejercicios**

1. Calcula sin calculadora $8^{2/3}$, $16^{3/2}$ y $4^{-1/2}$.
2. Si $T^2 = a^3$, ¿cuánto tarda en dar la vuelta un planeta a 4 ua? ¿Y uno a 9 ua?
3. Un asteroide tarda 4,6 años en dar la vuelta al Sol. ¿A qué distancia media está?
4. Si una esfera tiene el triple de radio que otra, ¿cuántas veces mayor es su volumen?

<details>
<summary>Soluciones</summary>

1. $8^{2/3} = (\sqrt[3]{8})^2 = 2^2 =$ **4**. $16^{3/2} = (\sqrt{16})^3 = 4^3 =$ **64**. $4^{-1/2} = 1/\sqrt{4} =$ **0,5**.
2. $T = 4^{3/2} = 2^3 =$ **8 años**. $T = 9^{3/2} = 3^3 =$ **27 años**.
3. $a = 4{,}6^{2/3} \approx$ **2,77 ua**. Es la distancia de Ceres, el mayor objeto del cinturón de asteroides.
4. $3^3 =$ **27 veces**.

</details>

### Sesión 2 · Matemáticas: logaritmos y escalas logarítmicas (35-45 min)

**La pregunta inversa.** Una potencia responde a «¿cuánto es 10 elevado a 3?». El **logaritmo** responde a la pregunta inversa: «¿a qué hay que elevar 10 para obtener 1000?». La respuesta es 3, y se escribe $\log_{10} 1000 = 3$. En general:

$$\log_{10} y = x \quad \text{significa} \quad 10^x = y.$$

Así, $\log_{10} 100 = 2$, $\log_{10} 10 = 1$, $\log_{10} 1 = 0$ y $\log_{10} 0{,}01 = -2$. Un logaritmo en base 10 cuenta, más o menos, cuántas cifras tiene un número: $\log_{10} 5000 \approx 3{,}7$, entre 3 y 4. Solo existe para números positivos.

**Las propiedades** salen directamente de las de las potencias:

- $\log(x \cdot y) = \log x + \log y$: el logaritmo convierte productos en sumas.
- $\log(x / y) = \log x - \log y$.
- $\log(x^n) = n\log x$: convierte potencias en productos.

Esta es la razón por la que se inventaron. Durante tres siglos, antes de las calculadoras, los astrónomos multiplicaban números largos sumando sus logaritmos, que leían en tablas. La regla de cálculo era una tabla de logaritmos con forma de regla.

**Por qué sirven para la tercera ley.** Si $T^2 = a^3$, tomando logaritmos en los dos lados:

$$2\log T = 3\log a \quad \Rightarrow \quad \log T = \tfrac{3}{2}\log a.$$

Si en una gráfica pones $\log a$ en el eje horizontal y $\log T$ en el vertical, los planetas quedan sobre una **recta de pendiente 3/2**. Una relación de potencias se convierte en una recta, que es la relación más fácil de reconocer y de medir. Es la manera estándar de descubrir leyes de potencias en datos.

**Escalas logarítmicas.** En vez de calcular los logaritmos, se puede usar una gráfica en **escala logarítmica**: en el eje, cada marca vale diez veces la anterior (0,1, 1, 10, 100...), en lugar de sumar una cantidad fija. Así caben en la misma gráfica Mercurio, a 0,39 ua, y Neptuno, a 30 ua, sin que los planetas interiores queden aplastados en una esquina.

:::note[De dónde viene la palabra]
**Logaritmo** es una palabra inventada por el matemático escocés John Napier, que publicó las primeras tablas en 1614. La formó con el griego *lógos*, que entre otras cosas significa «razón, proporción», y *arithmós*, «número»: «número de la razón». Kepler fue uno de los primeros en usar las tablas de Napier, y en parte gracias a ellas pudo terminar sus tablas de los planetas.
:::

**Ejercicios**

1. Calcula $\log_{10}$ de 1 000 000, de 0,001 y de $10^{2{,}5}$.
2. Sabiendo que $\log_{10} 2 \approx 0{,}301$, calcula $\log_{10} 8$, $\log_{10} 20$ y $\log_{10} 0{,}5$.
3. Dos puntos de una gráfica log-log son $(\log a, \log T) = (0, 0)$ y $(1, 1{,}5)$. ¿Cuál es la pendiente? ¿Qué valores de $a$ y $T$ representan?

<details>
<summary>Soluciones</summary>

1. **6**, **−3** y **2,5**.
2. $\log 8 = 3\log 2 \approx$ **0,903**. $\log 20 = \log 2 + \log 10 \approx$ **1,301**. $\log 0{,}5 = -\log 2 \approx$ **−0,301**.
3. La pendiente es $1{,}5/1 =$ **1,5**. El primer punto es $a = 1$, $T = 1$ (la Tierra). El segundo es $a = 10$ ua y $T = 10^{1{,}5} \approx 31{,}6$ años, cerca de Saturno.

</details>

### Sesión 3 · Física: la tercera ley de Kepler (30-40 min)

**El enunciado de Kepler.** *Los cuadrados de los periodos de los planetas son proporcionales a los cubos de los semiejes mayores de sus órbitas.* Con $T$ en años y $a$ en unidades astronómicas:

$$T^2 = a^3.$$

Fíjate en que importa el **semieje mayor**, no la forma de la órbita. Un cometa muy excéntrico y un planeta en órbita casi circular con el mismo $a$ tardan lo mismo en dar la vuelta.

**La versión de Newton.** Kepler encontró la regla en los datos, sin saber por qué se cumplía. Newton la dedujo de su ley de la gravitación (semana 16) y descubrió que la constante no es universal: depende de la masa del cuerpo central. Para una órbita circular de radio $r$ alrededor de una masa $M$, lo verás en la semana 17:

$$T^2 = \frac{4\pi^2}{G M}\,r^3,$$

donde $G$ es la constante de la gravitación. Para una elipse, se cambia $r$ por el semieje mayor $a$. Las unidades de Kepler, años y ua, funcionan para todo lo que gira alrededor del Sol porque la masa central es siempre la misma. Para las lunas de Júpiter, la constante es otra, y al medirla se puede **pesar Júpiter** (semana 22).

**Lo que dice la ley.** De $T \propto a^{3/2}$ y de que la longitud de la órbita es proporcional a $a$, la velocidad media de un planeta es $v \propto a / a^{3/2} = a^{-1/2}$. Un planeta cuatro veces más lejano va a la mitad de velocidad. Es la respuesta a la pregunta del principio: Saturno, a unas 9,6 ua, se mueve a $1/\sqrt{9{,}6} \approx 0{,}32$ veces la velocidad de la Tierra, unos 9,7 km/s.

**Qué hacer**

1. Neptuno está a 30,1 ua del Sol. Calcula su periodo y compáralo con el valor real, 164,8 años.
2. El cometa Halley tiene $a = 17{,}8$ ua. ¿Cada cuántos años vuelve?
3. Un satélite artificial tarda 1,5 horas en dar la vuelta a la Tierra a unos 6800 km del centro. ¿Cuánto tardaría a 4 veces esa distancia?

<details>
<summary>Soluciones</summary>

1. $T = 30{,}1^{3/2} \approx$ **165 años**. Coincide con el valor real.
2. $T = 17{,}8^{3/2} \approx$ **75 años**. Su último paso por el perihelio fue en 1986 y el próximo será en 2061.
3. El periodo se multiplica por $4^{3/2} = 8$: **12 horas**. La masa central es la Tierra, pero la proporción se cumple igual.

</details>

### Sesión 4 · Astronomía y observación: los periodos del Sistema Solar (30-45 min)

**Cómo se miden los periodos.** Nadie ha esperado 165 años a ver dar una vuelta a Neptuno. Desde la Tierra se mide el periodo sinódico, el tiempo entre dos oposiciones (semana 13), y de él se deduce el sidéreo despejando en la fórmula $1/S = 1/T_\text{Tierra} - 1/T_\text{planeta}$:

$$\frac{1}{T_\text{planeta}} = \frac{1}{T_\text{Tierra}} - \frac{1}{S}.$$

Es lo que hizo Copérnico, y fue una de las ventajas de su modelo: por primera vez se podían calcular los periodos reales de los planetas y sus distancias relativas al Sol.

**Hazlo tú con Marte.** Las tres últimas oposiciones de Marte han sido o serán el 8 de diciembre de 2022, el 16 de enero de 2025 y el 19 de febrero de 2027.

1. Cuenta los días entre cada par de oposiciones (cuidado con 2024, que fue bisiesto).
2. Haz la media y calcula con ella el periodo sidéreo de Marte.
3. Compara con el valor real, 687 días. ¿Por qué no sale exacto? Pista: semana 14.

<details>
<summary>Solución</summary>

Del 8 de diciembre de 2022 al 16 de enero de 2025 hay 770 días, y de ahí al 19 de febrero de 2027, 764. La media es 767 días. Entonces $1/T = 1/365{,}25 - 1/767 \approx 0{,}001434$ y $T \approx$ **697 días**, un 1,5 % por encima del valor real. El periodo sinódico de Marte varía bastante de una oposición a otra, porque su órbita es excéntrica y Marte va más deprisa cerca del perihelio. Haciendo la media de muchas oposiciones sale 780 días, y con ese valor, $T = 687$ días.

</details>

**Comprueba una oposición en Stellarium.** Pon la fecha del 19 de febrero de 2027 a medianoche y busca Marte: debe estar alto hacia el sur, en Leo, justo en la dirección opuesta al Sol. Avanza dos semanas y comprueba que el Sol y Marte ya no están exactamente enfrentados.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 15:

- carga los datos de los ocho planetas (semieje mayor y periodo) de la hoja de datos de la NASA,
- calcula $T^2/a^3$ para cada uno,
- dibuja $T$ frente a $a$ en escala normal y en escala logarítmica, donde los planetas quedan en una recta,
- ajusta esa recta y mide su pendiente, que debe salir 1,5,
- usa la ley para predecir el periodo de cuerpos que no son planetas.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-15.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-15.ipynb)

## Qué has aprendido

- **La respuesta.** El periodo de un planeta depende de su distancia media al Sol según $T^2 = a^3$ (en años y ua). Los planetas lejanos tardan más porque su órbita es más larga y, además, porque van más despacio: la velocidad orbital disminuye como $1/\sqrt{a}$.
- **El método.** Los periodos sidéreos no se observan directamente: se deducen de los sinódicos, que se miden contando el tiempo entre oposiciones.
- **Las herramientas.** Proporciones con potencias, exponentes fraccionarios, logaritmos y sus propiedades, y la gráfica log-log como forma de reconocer y medir una ley de potencias.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 13.5, Leyes del movimiento planetario de Kepler, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-5-leyes-del-movimiento-planetario-de-kepler). Español; la tercera ley deducida de la gravitación. Verificado el 6 de noviembre de 2026.
2. [Unidad 5: Las leyes del movimiento planetario (Proyecto PETeR, Instituto de Astrofísica de Canarias)](https://outreach.iac.es/peter/wp-content/uploads/2025/10/Unidad-5-Leyes-del-Movimiento_Intro.pdf). Español, divulgativo; la tercera ley en la forma $P^2 = a^3$ y su historia. Verificado el 6 de noviembre de 2026.
3. [Planetary Fact Sheet de la NASA (NSSDC)](https://nssdc.gsfc.nasa.gov/planetary/factsheet/). Inglés; la tabla de datos de los planetas que usa el cuaderno. **(Sin verificar)**: no he podido abrirla desde mi entorno; los valores del cuaderno los he tomado de una reproducción de esa tabla.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.

Las fechas de las oposiciones de Marte las he comprobado en varias fuentes de divulgación astronómica el 6 de noviembre de 2026.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
