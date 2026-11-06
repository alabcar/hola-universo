---
title: "Semana 6 · ¿Cómo se midió el tamaño de la Tierra sin salir de ella?"
description: "Fase 1 · Principios básicos de astronomía. Triángulos, rectas paralelas, triángulos semejantes, la tangente y el método de Eratóstenes."
sidebar:
  order: 6
  label: "6. ¿Cómo se midió el tamaño de la Tierra sin salir de ella?"
---

## La pregunta del cielo

Hace unos 2200 años, en Alejandría, Eratóstenes calculó cuánto mide la circunferencia de la Tierra con una vara, una sombra y la distancia a otra ciudad. No tenía satélites ni instrumentos de precisión. La pregunta es qué hacía falta saber para que eso funcionara, y qué hace falta para repetirlo hoy con una vara de un metro.

Que la Tierra era una esfera ya se sabía en Grecia al menos desde Aristóteles, en el siglo IV a. C. Él dio dos argumentos: la sombra de la Tierra sobre la Luna en los eclipses es siempre redonda, y al viajar hacia el sur aparecen en el horizonte estrellas que no se ven más al norte. Lo que faltaba era saber **cuánto** medía.

Esta semana aprendes los ingredientes matemáticos del método (las propiedades de los triángulos, las rectas paralelas y la primera trigonometría), entiendes la física que lo sostiene, y lo reproduces con datos históricos y con una medida propia de la sombra de una vara.

:::note[De dónde viene la palabra]
**Geometría** viene del griego *gê*, «tierra», y *métron*, «medida»: literalmente, «medida de la tierra». Según Heródoto, nació en Egipto para volver a trazar los límites de los campos después de cada crecida del Nilo. Con Eratóstenes, la palabra recuperó su sentido literal: medir la Tierra entera. A Eratóstenes, que dirigió la biblioteca de Alejandría, se le atribuye también la palabra **geografía**, «descripción de la tierra» (de *gráphein*, «escribir, dibujar»).
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: triángulos y triángulos semejantes (35-45 min)

**Lo básico de un triángulo.** Un triángulo tiene tres lados y tres ángulos, y sus tres ángulos suman siempre 180°. Puedes comprobarlo recortando un triángulo de papel, arrancando sus tres esquinas y juntándolas por los vértices: forman una línea recta, media vuelta. Un **triángulo rectángulo** tiene un ángulo de 90° (un ángulo recto); los otros dos suman entonces 90° y son **agudos**, menores de 90°. El lado opuesto al ángulo recto, el más largo, es la **hipotenusa**, y los otros dos son los **catetos**.

**Rectas paralelas.** Dos rectas son **paralelas** si nunca se cortan, por mucho que las prolongues. Si una tercera recta las atraviesa, forma con ellas ocho ángulos, y hay una regla que vas a usar en la sesión 3: los dos ángulos que quedan «en Z», a lados opuestos de la recta que atraviesa y entre las dos paralelas, son iguales. Se llaman **ángulos alternos internos**. Dibuja dos rayas paralelas y una diagonal que las corte, y lo verás: la diagonal se inclina lo mismo respecto a las dos.

**Triángulos semejantes.** Dos triángulos son **semejantes** si tienen los mismos ángulos. Uno es como una fotocopia ampliada o reducida del otro: tienen la misma forma y distinto tamaño. Y, como en una ampliación, todos los lados crecen en la misma proporción. Por tanto, sus lados son proporcionales: el cociente entre dos lados de uno es igual al cociente entre los lados correspondientes del otro. Es la regla de tres de la semana 1, con dibujos.

**Medir con sombras.** A la misma hora, los rayos del Sol llegan todos con la misma inclinación. Un objeto vertical, su sombra y el rayo que pasa por su punta forman un triángulo rectángulo, y todos los objetos verticales dan triángulos con los mismos ángulos: son semejantes. Entonces

$$\frac{\text{altura del objeto}}{\text{longitud de su sombra}} = \frac{\text{altura de la vara}}{\text{longitud de su sombra}}.$$

Según la tradición griega, Tales de Mileto midió así la altura de una pirámide de Egipto en el siglo VI a. C.: esperó a la hora en que la sombra de un palo medía lo mismo que el palo, y midió entonces la sombra de la pirámide.

:::note[De dónde viene la palabra]
**Hipotenusa** viene del griego *hypoteínousa*, «la que se tiende por debajo»: el lado que se extiende frente al ángulo recto, como la cuerda de un arco. **Cateto** viene de *káthetos*, «perpendicular, lo que cae a plomo», de *kathíēmi*, «dejar caer»: en un triángulo apoyado sobre un cateto, el otro cae en vertical. **Paralelo** viene de *pará allḗlois*, «uno al lado del otro». **Semejante** viene del latín *similis*, «parecido».
:::

**Ejercicios**

1. Una vara de 1,00 m proyecta una sombra de 0,80 m. A la misma hora, un árbol proyecta 12 m de sombra. ¿Cuánto mide el árbol?
2. Una persona de 1,80 m proyecta 3 m de sombra. ¿Qué altura tiene un edificio cuya sombra mide 30 m?
3. Los lados de un triángulo miden 3, 4 y 5. Otro triángulo semejante tiene su lado mayor de 20. ¿Cuánto miden los otros dos?
4. Un triángulo rectángulo tiene un ángulo de 35°. ¿Cuánto mide el tercero?

<details>
<summary>Soluciones</summary>

1. 12 · (1,00/0,80) = **15 m**.
2. 30 · (1,80/3) = **18 m**.
3. El factor es 20/5 = 4: los lados son **12 y 16**.
4. 180° − 90° − 35° = **55°**.

</details>

### Sesión 2 · Matemáticas: la tangente (35-40 min)

**Una idea que sale de la semejanza.** En un triángulo rectángulo, fija uno de los ángulos agudos, por ejemplo 30°. Todos los triángulos rectángulos con un ángulo de 30° tienen los mismos tres ángulos (90°, 30° y 60°), así que son semejantes, y el cociente entre dos de sus lados es siempre el mismo, sea el triángulo grande o pequeño. Ese cociente depende **solo del ángulo**. Es la idea de la trigonometría: a cada ángulo le corresponden unos cocientes fijos entre los lados.

**La tangente.** Para un ángulo agudo $z$ de un triángulo rectángulo, el **cateto opuesto** es el que está enfrente de $z$, y el **cateto contiguo** (o adyacente), el que forma el ángulo $z$ junto con la hipotenusa. La **tangente** de $z$ es el cociente entre los dos:

$$\tan z = \frac{\text{cateto opuesto}}{\text{cateto contiguo}}.$$

Con una vara de altura $h$ y una sombra de longitud $s$, el ángulo $z$ entre los rayos del Sol y la vara tiene la sombra enfrente y la vara al lado, así que

$$\tan z = \frac{s}{h}.$$

**La operación inversa.** Si conoces el cociente y quieres el ángulo, usas la **arcotangente**: $z = \arctan(s/h)$. «Arcotangente de 0,6» se lee como «el ángulo (el arco) cuya tangente vale 0,6». En una calculadora se escribe $\tan^{-1}$, y hay que comprobar que está en modo grados (DEG) y no en radianes (RAD). Valores que conviene recordar:

| Ángulo | 0° | 30° | 45° | 60° |
|---|---|---|---|---|
| Tangente | 0 | 0,577 | 1 | 1,732 |

La de 45° es fácil de entender: un triángulo rectángulo con un ángulo de 45° tiene el otro también de 45°, así que es la mitad de un cuadrado y sus dos catetos son iguales. Su cociente es 1.

**La tangente de un ángulo pequeño.** Para ángulos pequeños, expresados en radianes, $\tan z \approx z$. Cuando el ángulo es pequeño, el cateto opuesto es casi igual al arco de circunferencia que abarca el ángulo, y el cateto contiguo casi igual al radio, así que su cociente se parece mucho a $s/r$, que es el ángulo en radianes. Es la misma aproximación que usaste en la semana 2 para el tamaño angular: por eso funcionaba.

:::note[De dónde viene la palabra]
**Trigonometría** viene del griego *trígōnon*, «triángulo» (de *treîs*, «tres», y *gōnía*, «ángulo»), y *métron*, «medida». El nombre se usó por primera vez en 1595, en un libro del alemán Bartholomaeus Pitiscus. **Tangente** viene del latín *tangens*, «que toca», de *tangere*, «tocar» (como *tacto* o *contacto*). Si dibujas una circunferencia de radio 1, la tangente de un ángulo es la longitud de un trozo de la recta que toca la circunferencia en un solo punto, la recta tangente.
:::

**Ejercicios**

1. Una vara de 1 m proyecta 0,60 m de sombra. ¿Qué ángulo forman los rayos con la vertical?
2. Con la misma vara, ¿qué sombra corresponde a un ángulo de 7,2°?
3. Compara $\tan 7{,}2^\circ$ con $7{,}2^\circ$ expresado en radianes. ¿Cuánto difiere?
4. Si la sombra mide el doble que la vara, ¿cuánto vale el ángulo?

<details>
<summary>Soluciones</summary>

1. $\arctan(0{,}60) \approx$ **31,0°**.
2. $s = \tan 7{,}2^\circ \cdot 1\ \text{m} \approx$ **0,126 m**.
3. $\tan 7{,}2^\circ \approx 0{,}1263$ y $7{,}2^\circ = 7{,}2 \cdot \pi/180 \approx 0{,}1257$ rad: difieren en menos del 1 %.
4. $\arctan(2) \approx$ **63,4°**.

</details>

### Sesión 3 · Física: el método de Eratóstenes (35-45 min)

**La idea.** Eratóstenes sabía que, al mediodía del solsticio de verano, en Siena (hoy Asuán, en el sur de Egipto) el Sol iluminaba el fondo de un pozo, es decir, estaba en la vertical: no había sombras. Ese mismo día y a la misma hora, en Alejandría, más al norte, una vara proyectaba una sombra. Con la sombra y la vara obtuvo el ángulo de los rayos con la vertical (la **distancia cenital** del Sol, $90^\circ$ menos su altura): unos 7,2°, que es 1/50 de una circunferencia completa.

**Por qué ese ángulo es el que importa.** Haz un dibujo: una circunferencia (la Tierra), con dos puntos en su borde (Siena y Alejandría), y la vertical de cada uno, que es la línea que va del punto al centro de la Tierra. Los rayos del Sol llegan paralelos a los dos puntos. En Siena, el rayo coincide con la vertical. En Alejandría, el rayo forma con la vertical el ángulo de la sombra. Ahora mira la vertical de Alejandría como una recta que atraviesa dos paralelas: el rayo que llega a Alejandría y el que llega a Siena (prolongado hasta el centro de la Tierra). Los ángulos alternos internos de la sesión 1 son iguales: **el ángulo de la sombra en Alejandría es igual al ángulo que forman las dos verticales en el centro de la Tierra**.

**La regla de tres.** Ese ángulo en el centro abarca el arco entre las dos ciudades. Un ángulo de 7,2° es 1/50 de la vuelta completa, así que el arco entre las ciudades es 1/50 de la circunferencia de la Tierra. En general:

$$\frac{d}{C} = \frac{\Delta z}{360^\circ} \quad \Longrightarrow \quad C = d \cdot \frac{360^\circ}{\Delta z}.$$

Con $d = 5000$ estadios (la distancia tradicional) y $\Delta z = 7{,}2^\circ$, $C = 250\,000$ estadios.

**Cuánto es eso en kilómetros.** Depende de la longitud del estadio, que no se conoce con certeza. Con unos 160 m, que es el valor que usa el fascículo de la UNAM (recurso 1), son unos 40 000 km. Con el estadio ático, de unos 185 m, serían unos 46 000 km. Hoy sabemos que el meridiano mide unos 40 008 km y el ecuador, unos 40 075 km.

**Qué supuso Eratóstenes y qué no era cierto**

- Que Siena y Alejandría estaban en el mismo meridiano. En realidad difieren unos 3° de longitud.
- Que los rayos del Sol son paralelos. Son casi paralelos: el Sol ocupa 0,53° en el cielo, así que los rayos de sus bordes difieren ese ángulo. Esto introduce un error de unas décimas de grado en cada medida.
- Que la distancia de 5000 estadios, medida con pasos o por tradición, era exacta.
- Que su medida de la sombra era perfecta.

Y como la circunferencia es inversamente proporcional al ángulo (si el ángulo se duplica, la circunferencia que sale es la mitad), un error de un grado sobre 7 son más de un 12 %. El cuaderno lo calcula.

**Tu latitud con una vara.** El mismo método sirve para saber dónde estás. Al mediodía solar, la distancia cenital del Sol es $z = |\varphi - \delta|$, con $\varphi$ tu latitud y $\delta$ la declinación del Sol ese día (semanas 1 y 3). En el hemisferio norte, con la sombra apuntando al norte, $\varphi = \delta + z$.

:::note[De dónde viene la palabra]
**Estadio** viene del griego *stádion*, que primero fue una unidad de longitud, unos 600 pies. Como la pista de carreras de Olimpia medía un estadio, la palabra pasó a nombrar la carrera y después el lugar donde se corría. Como los pies variaban de una ciudad a otra, también variaba el estadio, y por eso no sabemos con certeza qué medida usó Eratóstenes.
:::

**Qué hacer**

1. Haz el dibujo de la Tierra, las dos ciudades y los rayos paralelos, y señala los dos ángulos iguales.
2. Calcula con tu calculadora cuántos kilómetros son 250 000 estadios con dos longitudes de estadio, y el error respecto al valor actual.
3. Explica por escrito por qué un error pequeño en el ángulo produce un error grande en la circunferencia.

### Sesión 4 · Astronomía y observación (30-45 min)

Vas a medir la sombra de una vara a lo largo de la mañana y descubrir cuándo es mediodía solar: el momento en que el Sol cruza el meridiano, está más alto y la sombra es más corta y apunta exactamente al norte.

**Material.** Una vara recta de al menos 1 m (un palo de escoba), una cinta métrica, una plomada o un nivel y una superficie plana al sol.

1. Coloca la vara vertical (comprueba con la plomada) sobre una superficie horizontal que dé sol toda la mañana.
2. Marca el extremo de la sombra cada 5 minutos desde unos 40 minutos antes de la hora prevista del mediodía solar, y anota la hora de cada marca. En España el mediodía solar cae aproximadamente entre las 13:00 y las 14:30 del reloj, según la longitud y el horario de verano.
3. Mide con la cinta la longitud de cada sombra (desde la base de la vara hasta la marca). La más corta es la del mediodía solar.
4. Anota la hora de la sombra mínima y su longitud, y la longitud exacta de la vara.

**En Stellarium.** Fija tu lugar y la fecha de tu medida, ve al mediodía solar y comprueba cuánto vale la altura del Sol. Su distancia cenital es 90° menos esa altura, y debe coincidir con la que calcules con la sombra.

No mires al Sol: solo necesitas mirar su sombra.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 6:

- convierte sombra y altura de vara en distancia cenital,
- aplica el método de Eratóstenes con los datos históricos y con dos longitudes de estadio,
- calcula cuánto cambia el resultado si el ángulo se mide con un error de hasta 1°,
- procesa un ejemplo inventado de dos varas y calcula tu latitud con tu medida.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-06.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-06.ipynb)

## Qué has aprendido

- **La respuesta.** La Tierra es esférica y su circunferencia se deduce de dos datos: el ángulo entre las verticales de dos lugares, que se mide con sombras, y la distancia entre ellos. Eratóstenes obtuvo 250 000 estadios, unos 40 000 km con la longitud de estadio que se suele usar.
- **La causa.** Como la Tierra es esférica, la vertical de cada lugar apunta a una dirección distinta, y los rayos del Sol, casi paralelos, forman con ellas ángulos diferentes. Por los ángulos alternos internos, el ángulo de la sombra es el mismo que el que forman las verticales en el centro de la Tierra.
- **Las herramientas.** La suma de los ángulos de un triángulo, rectas paralelas y ángulos alternos internos, triángulos semejantes, la tangente y su inversa, la regla de tres entre arcos y ángulos, y el análisis de cómo un error en una medida se propaga al resultado.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Experimentos para medir la Tierra, UNAM (fascículo de Geociencias)](https://tellus.geociencias.unam.mx/wp-content/uploads/2020/01/libro6_medicion_tierra.pdf). Español, PDF con el método de Eratóstenes y una réplica a escala; usa un estadio de unos 160 m. Verificado el 31 de octubre de 2026.
2. [Ficha de la Tierra, NASA NSSDCA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html). Inglés, valores actuales de radio y circunferencia para comparar. **(Sin verificar)** directamente, como en la semana 1.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
