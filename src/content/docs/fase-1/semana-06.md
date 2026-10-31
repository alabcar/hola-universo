---
title: "Semana 6 · ¿Cómo se midió el tamaño de la Tierra sin salir de ella?"
description: "Fase 1 · Principios básicos de astronomía. Triángulos semejantes, primera trigonometría y el método de Eratóstenes."
sidebar:
  order: 6
  label: "6. ¿Cómo se midió el tamaño de la Tierra sin salir de ella?"
---

## La pregunta del cielo

Hace unos 2200 años, en Alejandría, Eratóstenes calculó cuánto mide la circunferencia de la Tierra con una vara, una sombra y la distancia a otra ciudad. No tenía satélites ni siquiera trigonometría. La pregunta es qué hacía falta saber para que eso funcionara, y qué hace falta para repetirlo hoy con una vara de un metro.

Esta semana aprendes los dos ingredientes matemáticos del método (la semejanza de triángulos y la primera trigonometría), entiendes la física que lo sostiene, y lo reproduces con datos históricos y con una medida propia de la sombra de una vara.

## Las cinco sesiones

### Sesión 1 · Matemáticas: triángulos semejantes (30-40 min)

Dos triángulos son **semejantes** si tienen los mismos ángulos. Entonces sus lados son proporcionales: el cociente entre dos lados de uno es igual al cociente entre los lados correspondientes del otro. Es la regla de tres de la semana 2, con dibujos.

Es el principio de la medición con sombras: a la misma hora, un objeto y su sombra forman con los rayos del Sol un triángulo rectángulo, y todos los objetos verticales dan el mismo ángulo. Entonces

$$\frac{\text{altura del objeto}}{\text{longitud de su sombra}} = \frac{\text{altura de la vara}}{\text{longitud de su sombra}}.$$

**Ejercicios**

1. Una vara de 1,00 m proyecta una sombra de 0,80 m. A la misma hora, un árbol proyecta 12 m de sombra. ¿Cuánto mide el árbol?
2. Una persona de 1,80 m proyecta 3 m de sombra. ¿Qué altura tiene un edificio cuya sombra mide 30 m?
3. Los lados de un triángulo miden 3, 4 y 5. Otro triángulo semejante tiene su lado mayor de 20. ¿Cuánto miden los otros dos?

<details>
<summary>Soluciones</summary>

1. 12 · (1,00/0,80) = **15 m**.
2. 30 · (1,80/3) = **18 m**.
3. El factor es 20/5 = 4: los lados son **12 y 16**.

</details>

### Sesión 2 · Matemáticas: la tangente (30-40 min)

En un triángulo rectángulo, la **tangente** de un ángulo agudo es el cociente entre el cateto opuesto y el adyacente. Con una vara de altura $h$ y una sombra de longitud $s$, el ángulo $z$ entre los rayos del Sol y la vara cumple

$$\tan z = \frac{s}{h}.$$

La operación inversa, la **arcotangente**, devuelve el ángulo a partir del cociente: $z = \arctan(s/h)$. En una calculadora se escribe $\tan^{-1}$ y hay que poner el modo en grados. Valores que conviene recordar:

| Ángulo | 0° | 30° | 45° | 60° |
|---|---|---|---|---|
| Tangente | 0 | 0,577 | 1 | 1,732 |

Para ángulos pequeños, expresados en radianes, $\tan z \approx z$. Es la misma aproximación que usaste en la semana 2 para el tamaño angular: por eso funcionaba.

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

### Sesión 3 · Física: el método de Eratóstenes (30-40 min)

**La idea.** Eratóstenes sabía que, al mediodía del solsticio de verano, en Siena (hoy Asuán) el Sol iluminaba el fondo de un pozo, es decir, estaba en la vertical. Ese día, en Alejandría, una vara proyectaba una sombra. Con la sombra y la vara obtuvo el ángulo de los rayos con la vertical: unos 7,2°, que es 1/50 de una circunferencia. Si los rayos son paralelos, ese ángulo es también el que forman las verticales de las dos ciudades vistas desde el centro de la Tierra. Y como la distancia entre las ciudades es la misma fracción de la circunferencia que ese ángulo es de los 360°, la circunferencia sale de una regla de tres:

$$C = d \cdot \frac{360^\circ}{\Delta z}.$$

Con $d = 5000$ estadios (la distancia tradicional) y $\Delta z = 7{,}2^\circ$, $C = 250\,000$ estadios.

**Cuánto es eso en kilómetros.** Depende de la longitud del estadio, que no se conoce con certeza. Con unos 160 m, que es el valor que usa el fascículo de la UNAM (recurso 1), son unos 40 000 km. Con el estadio ático, de unos 185 m, serían unos 46 000 km. Hoy sabemos que el meridiano mide unos 40 008 km y el ecuador, unos 40 075 km.

**Qué supuso Eratóstenes y qué no era cierto**

- Que Siena y Alejandría estaban en el mismo meridiano. En realidad difieren unos 3° de longitud.
- Que los rayos del Sol son paralelos. Son casi paralelos: el Sol ocupa 0,53° en el cielo, así que los rayos de sus bordes difieren ese ángulo. Esto introduce un error de unas décimas de grado en cada medida.
- Que la distancia de 5000 estadios, medida con pasos o por tradición, era exacta.
- Que su medida de la sombra era perfecta.

Y como la circunferencia es inversamente proporcional al ángulo, un error de un grado sobre 7 son más de un 12 %. El cuaderno lo calcula.

**Tu latitud con una vara.** El mismo método sirve para saber dónde estás. Al mediodía solar, la distancia cenital del Sol es $z = |\varphi - \delta|$, con $\varphi$ tu latitud y $\delta$ la declinación del Sol ese día (semana 1). En el hemisferio norte, con la sombra apuntando al norte, $\varphi = \delta + z$.

**Qué hacer**

1. Calcula con tu calculadora cuántos kilómetros son 250 000 estadios con dos longitudes de estadio, y el error respecto al valor actual.
2. Explica por escrito por qué un error pequeño en el ángulo produce un error grande en la circunferencia.

### Sesión 4 · Astronomía y observación (30-45 min)

Vas a medir la sombra de una vara a lo largo de la mañana y descubrir cuándo es mediodía solar.

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
- **La causa.** Como la Tierra es esférica, la vertical de cada lugar apunta a una dirección distinta, y los rayos del Sol, casi paralelos, forman con ellas ángulos diferentes.
- **Las herramientas.** Triángulos semejantes, la tangente y su inversa, la regla de tres entre arcos y ángulos, y el análisis de cómo un error en una medida se propaga al resultado.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Experimentos para medir la Tierra, UNAM (fascículo de Geociencias)](https://tellus.geociencias.unam.mx/wp-content/uploads/2020/01/libro6_medicion_tierra.pdf). Español, PDF con el método de Eratóstenes y una réplica a escala; usa un estadio de unos 160 m. Verificado el 31 de octubre de 2026.
2. [Ficha de la Tierra, NASA NSSDCA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html). Inglés, valores actuales de radio y circunferencia para comparar. **(Sin verificar)** directamente, como en la semana 1.
3. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
4. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
