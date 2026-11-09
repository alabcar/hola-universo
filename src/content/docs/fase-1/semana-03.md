---
title: "Semana 3 · ¿Cómo digo dónde está cada cosa en el cielo?"
description: "Fase 1 · Principios básicos de astronomía. El plano cartesiano, latitud y longitud, coordenadas horizontales y ecuatoriales, y la altura de la estrella Polar."
sidebar:
  order: 3
  label: "3. ¿Cómo digo dónde está cada cosa en el cielo?"
---

## La pregunta del cielo

Para decirle a alguien dónde mirar necesitas un sistema de referencia, igual que una dirección postal. El problema es que el cielo gira: la estrella que ves ahora a tu izquierda estará a tu derecha dentro de unas horas, y lo que ves desde tu ciudad no es lo que ve alguien en otra latitud. Hacen falta dos sistemas distintos: uno pegado a ti (el horizonte y el cénit de tu lugar) y otro pegado a las estrellas.

Esta semana aprendes qué son unas coordenadas, los dos sistemas del cielo, a convertir las unidades que usan, y a responder una pregunta concreta: ¿por qué la altura de la estrella Polar sobre el horizonte te dice la latitud en la que estás?

## Las cinco sesiones

### Sesión 1 · Matemáticas: el plano cartesiano y las coordenadas (35-40 min)

**Dos números para un punto.** Para señalar un punto en una hoja de papel bastan dos números. Se dibujan dos rectas perpendiculares, los **ejes**: uno horizontal, el eje $x$, y uno vertical, el eje $y$. Se cruzan en un punto llamado **origen**. Cada punto de la hoja se describe con dos números $(x, y)$: cuánto te desplazas en horizontal desde el origen y cuánto en vertical. Esos dos números son sus **coordenadas**. El orden importa: $(2, 5)$ y $(5, 2)$ son puntos distintos, y por convenio se escribe siempre primero el horizontal.

Las coordenadas pueden ser negativas: un número negativo significa que hay que ir hacia el otro lado del origen (a la izquierda o hacia abajo). Los dos ejes dividen el plano en cuatro regiones, los **cuadrantes**: en el primero, arriba a la derecha, las dos coordenadas son positivas; en el tercero, abajo a la izquierda, las dos son negativas.

**Coordenadas en una esfera.** La superficie de la Tierra no es un plano, pero también basta con dos números para situar un lugar, aunque ahora son ángulos:

- La **latitud** es el ángulo al norte o al sur del ecuador: 0° en el ecuador, 90° norte en el polo norte, 90° sur en el polo sur.
- La **longitud** es el ángulo al este o al oeste de un meridiano de referencia, el que pasa por el observatorio de Greenwich, en Londres: va de 0° a 180° hacia cada lado.

Un mapa del mundo es un plano donde $x$ es la longitud e $y$ la latitud. El mapa del cielo es lo mismo: un plano donde $x$ es la ascensión recta e $y$ la declinación (las definimos en la sesión 3). Lo importante es saber leer y dibujar: elegir una escala en cada eje, marcar los puntos y decidir en qué sentido crece cada eje. En los mapas del cielo es habitual que el eje horizontal crezca hacia la **izquierda**, porque se dibuja el cielo tal como lo ves cuando miras al sur, con el este a la izquierda. Un mapa de la Tierra se mira desde fuera; un mapa del cielo, desde dentro.

:::note[De dónde viene la palabra]
**Cartesiano** viene de *Cartesius*, el nombre latinizado de René Descartes, que en 1637 publicó la idea de describir curvas con ecuaciones entre coordenadas y unió así el álgebra y la geometría. **Coordenada** viene del latín *co-*, «juntos», y *ordinare*, «ordenar»: números que se ordenan juntos. **Latitud** y **longitud** son las palabras latinas para «anchura» y «largura». Vienen de los mapas antiguos, como los de Ptolomeo, en los que el mundo conocido, de España a la India, era mucho más largo de este a oeste que ancho de norte a sur: la longitud se medía a lo largo y la latitud a lo ancho.
:::

**Ejercicios**

1. Dibuja en papel los puntos Sirio (6,75; −16,7), Betelgeuse (5,9; 7,4) y Rigel (5,25; −8,2), con la primera coordenada en horas y la segunda en grados. ¿Cuál está más al norte? ¿Cuál tiene mayor primera coordenada?
2. Si el eje horizontal crece hacia la izquierda, ¿hacia qué lado queda el este en tu dibujo?
3. ¿Qué diferencia de primera coordenada hay entre Sirio y Rigel?

<details>
<summary>Soluciones</summary>

1. Más al norte: **Betelgeuse** (declinación +7,4). Mayor primera coordenada: **Sirio** (6,75).
2. El este queda a la **izquierda**.
3. 6,75 − 5,25 = **1,5 h**, es decir, 1 h 30 min, o 22,5°.

</details>

### Sesión 2 · Matemáticas: horas, minutos y grados (30-40 min)

**Por qué un ángulo se mide en horas.** La ascensión recta se mide en **horas** porque está ligada a la rotación de la Tierra. El cielo da una vuelta completa de 360° en 24 horas (en realidad, en un día sidéreo, unos 4 minutos menos, como viste en la semana 1). Así que 1 hora equivale a $360^\circ / 24 = 15^\circ$. Piensa en la esfera de un reloj gigante pintada sobre el cielo: si una estrella tiene una ascensión recta de 2 h más que otra, pasa por el sur dos horas más tarde.

Todo el sistema sexagesimal sigue: 1 minuto de tiempo equivale a 15′ de arco (la hora se divide en 60 minutos, como el grado) y 1 segundo de tiempo a 15″. Cuidado con la confusión de nombres: un «minuto de tiempo» de ascensión recta vale 15 «minutos de arco». Para pasar de horas y minutos a grados:

$$\text{grados} = \left(h + \frac{m}{60}\right) \cdot 15.$$

**La declinación** se mide en grados y minutos de arco, con signo: positiva al norte del ecuador celeste, negativa al sur. Cuidado con los signos al pasar a decimales: −8° 12′ es −8,2°, es decir, −(8 + 12/60), no −8 + 0,2. El signo afecta a todo el número.

**Ejercicios**

1. Pasa 6 h 45 min a grados.
2. Pasa 18 h 37 min a grados.
3. Pasa 89° 16′ a grados decimales.
4. ¿Cuántos minutos de tiempo tarda el cielo en desplazarse 1°?
5. Pasa −26° 26′ a grados decimales.

<details>
<summary>Soluciones</summary>

1. 6,75 · 15 = **101,25°**.
2. (18 + 37/60) · 15 = 18,6167 · 15 = **279,25°**.
3. 89 + 16/60 = **89,267°**.
4. 24 h = 1440 min corresponden a 360°, luego 1° tarda **4 minutos**.
5. −(26 + 26/60) = **−26,433°**.

</details>

### Sesión 3 · Física: sistemas de referencia (35-45 min)

**La esfera celeste.** Las estrellas están a distancias enormes y muy distintas, pero a simple vista no se nota: todas parecen pegadas a una gran esfera con centro en ti. Esa **esfera celeste** es una ficción, pero una ficción muy útil: como solo nos interesa la dirección en la que vemos cada astro, podemos tratarlos todos como puntos sobre la esfera y usar en ella coordenadas, como en la superficie de la Tierra. Para la esfera celeste, la Tierra es un punto en el centro.

**Horizontal.** Está pegado al observador. El **horizonte** es el plano del suelo, prolongado hasta el cielo. El punto justo sobre tu cabeza es el **cénit** y el opuesto, bajo tus pies, el **nadir**. Se miden dos ángulos:

- la **altura** $h$, ángulo sobre el horizonte, de 0° en el horizonte a 90° en el cénit;
- el **azimut** $A$, ángulo a lo largo del horizonte, contado desde el norte hacia el este, de 0° a 360°.

Es intuitivo y tiene un defecto: cambia con el lugar y con la hora. Una estrella tiene altura y azimut distintos cada minuto. El arco que va del norte al sur pasando por el cénit se llama **meridiano**: todas las estrellas alcanzan su mayor altura al cruzarlo, y el Sol lo cruza al mediodía.

**Ecuatorial.** Está pegado a las estrellas. Proyecta el ecuador terrestre en el cielo (el **ecuador celeste**) y los polos terrestres en los **polos celestes**, los dos puntos alrededor de los que parece girar todo el cielo. Se miden otros dos ángulos:

- la **declinación** $\delta$, que juega el papel de la latitud: de −90° en el polo sur celeste a +90° en el norte;
- la **ascensión recta** $\alpha$, que juega el papel de la longitud: se cuenta hacia el este a lo largo del ecuador celeste, desde el punto donde el Sol lo cruza en el equinoccio de marzo (el **punto Aries**, el «Greenwich» del cielo).

Las coordenadas ecuatoriales de una estrella son prácticamente constantes: no dependen del lugar ni de la hora, porque el sistema gira con el cielo. Cambian muy despacio porque el eje de la Tierra se tambalea como el de una peonza y describe un cono completo en unos 26 000 años: es la **precesión**, y desplaza las coordenadas unos 50″ al año. Por eso los catálogos indican la fecha de referencia de los datos, la **época**. La habitual es la J2000, el 1 de enero de 2000.

**Por qué la Polar da tu latitud.** Primero, qué es tu latitud con un dibujo: es el ángulo entre tu **vertical** (la dirección de una plomada, que apunta al centro de la Tierra) y el plano del ecuador. Ahora gira las dos cosas un ángulo recto. Tu horizonte es perpendicular a tu vertical, y el eje de la Tierra es perpendicular al ecuador. Si giras dos rectas 90° cada una, el ángulo que forman entre sí no cambia (haz la prueba con dos lápices), así que el ángulo entre tu horizonte y el eje de la Tierra es igual a tu latitud. Como las estrellas están tan lejos que sus rayos llegan paralelos a cualquier punto de la Tierra, el polo norte celeste se ve en la dirección del eje: a una altura igual a tu latitud. En el polo norte de la Tierra está en el cénit (90°), en el ecuador está en el horizonte (0°). La Polar, a menos de 1° del polo celeste, se queda siempre prácticamente en el mismo sitio, y su altura es tu latitud con ese error.

**Altura máxima de una estrella.** Cada día una estrella cruza el meridiano. El ecuador celeste corta el meridiano sur a una altura de $90^\circ - \varphi$, donde $\varphi$ (la letra griega fi) es tu latitud norte: es el complemento de la altura del polo, porque el ecuador está siempre a 90° de él. Una estrella con declinación $\delta$ está $\delta$ grados por encima de ese punto, luego

$$h_{\max} = 90^\circ - \varphi + \delta \quad (\text{si } \delta < \varphi), \qquad \text{y en general } h_{\max} = 90^\circ - |\varphi - \delta|.$$

Las barras $|\ |$ indican el **valor absoluto**: el número sin su signo. Es la misma fórmula que usaste en la semana 1 para la altura del Sol al mediodía, porque el Sol es una estrella más, con una declinación que cambia a lo largo del año.

De ahí salen las **circumpolares**, que giran alrededor del polo sin llegar a ponerse nunca (si $\delta > 90^\circ - \varphi$), y las que nunca llegan a salir desde tu latitud (si $\delta < -(90^\circ - \varphi)$).

:::note[De dónde viene la palabra]
**Polo** viene del griego *pólos*, «eje, pivote», del verbo *pélein*, «girar»: el punto alrededor del que gira algo. **Meridiano** viene del latín *meridies*, «mediodía» (*medius dies*): la línea por la que pasa el Sol a mediodía. **Nadir** es árabe, como cénit: *naẓīr as-samt*, «lo opuesto al cénit». **Ascensión recta** traduce el latín medieval *ascensio recta*. Los astrónomos llamaban «esfera recta» al cielo visto desde el ecuador terrestre, donde los astros salen en línea recta, perpendiculares al horizonte; allí, la ascensión recta de un punto del cielo indica cuándo sale. **Precesión** viene de *praecedere*, «ir delante»: por este movimiento, el equinoccio llega cada año un poco antes respecto a las estrellas.
:::

**Qué hacer**

1. Dibuja la esfera celeste con el horizonte, el cénit, el polo norte celeste a la altura de tu latitud y el ecuador celeste. Marca dónde cruza el meridiano una estrella de $\delta = 20^\circ$.
2. Responde: ¿qué estrellas son circumpolares en el polo norte? ¿Y en el ecuador?
3. Calcula, para tu latitud, la declinación mínima que debe tener una estrella para ser circumpolar.

### Sesión 4 · Astronomía y observación (30-45 min)

**En el cielo (si está despejado).** Localiza la Polar. El método clásico usa la Osa Mayor, cuyas siete estrellas más brillantes forman el Carro: las dos estrellas del extremo de la caja, las más alejadas del mango, apuntan hacia la Polar. Prolonga unas cinco veces la distancia entre ellas y llegarás a una estrella no muy brillante, sola en su zona: es la Polar. También se encuentra desde Casiopea, la «W» del otro lado del polo. Mide su altura con la mano, a brazo extendido (puño ≈ 10°) y compárala con tu latitud. Si tienes un cuadrante o una cruceta, el material de astronomas.org (recurso 1) explica cómo construirlos.

**En Stellarium.**

1. Fija tu lugar y activa las cuadrículas **ecuatorial** y **azimutal**.
2. Selecciona cinco estrellas de la tabla del cuaderno (Sirio, Vega, Capella, Arturo y Antares, por ejemplo) y anota su AR, su declinación, su altura y su azimut en el momento actual.
3. Compara la AR y la declinación con las de la tabla. Si alguna difiere más de un par de minutos, fíate de Stellarium: la tabla viene sin contrastar con un catálogo.
4. Repite la medida de una estrella una hora más tarde: ¿qué coordenadas han cambiado y cuáles no?

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 3:

- convierte AR en horas y declinación en grados y minutos a grados decimales,
- dibuja las 15 estrellas brillantes en el plano ecuatorial, con el eje de AR invertido,
- calcula para tu latitud la altura máxima de cada una y si es circumpolar o sale y se pone,
- compara tu cálculo con tres medidas tomadas en Stellarium.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-03.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-03.ipynb)

## Qué has aprendido

- **La respuesta.** Hay dos formas de situar un objeto: respecto a ti (altura y azimut, que cambian con la hora y el lugar) y respecto a las estrellas (ascensión recta y declinación, casi fijas). La altura de la Polar vale tu latitud porque el eje de la Tierra apunta, casi exactamente, hacia ella, y el ángulo entre tu horizonte y ese eje es tu latitud.
- **La causa.** La Tierra gira alrededor de un eje, que corta la esfera celeste en los polos celestes, y tu horizonte está inclinado respecto a ese eje según tu latitud.
- **Las herramientas.** El plano cartesiano y las coordenadas, también sobre una esfera (latitud y longitud); conversión entre horas, minutos y grados; el valor absoluto; y la fórmula de la altura máxima de una estrella en función de su declinación y de tu latitud.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [La esfera celeste y la observación a simple vista, astronomas.org](https://astronomas.org/files/documents/learning/esfera_celeste.pdf). Español, PDF didáctico para Bachillerato: coordenadas ecuatoriales y horizontales, cómo localizar la Polar y construir una cruceta y un cuadrante. Verificado el 31 de octubre de 2026.
2. [La esfera celestial, en *Mecánica celeste* de Tatum (LibreTexts Español)](https://espanol.libretexts.org/Fisica/Astronom%C3%ADa_y_Cosmolog%C3%ADa/Mec%C3%A1nica_Celestial_%28Tatum%29/06%3A_La_Esfera_Celestial). Español, nivel universitario avanzado: usa trigonometría esférica que aún no tienes. Para consultar más adelante, cuando llegues a las semanas 6 y 19. Licencia CC BY-NC 4.0. Verificado el 31 de octubre de 2026.
3. [4.1 Earth and Sky, *Astronomy* (OpenStax)](https://openstax.org/books/astronomy/pages/4-1-earth-and-sky). Inglés, introduce latitud, longitud, esfera celeste, declinación y ascensión recta. Verificado el 31 de octubre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
5. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
