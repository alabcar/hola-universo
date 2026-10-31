---
title: "Semana 3 · ¿Cómo digo dónde está cada cosa en el cielo?"
description: "Fase 1 · Principios básicos de astronomía. Coordenadas horizontales y ecuatoriales, y la altura de la estrella Polar."
sidebar:
  order: 3
  label: "3. ¿Cómo digo dónde está cada cosa en el cielo?"
---

## La pregunta del cielo

Para decirle a alguien dónde mirar necesitas un sistema de referencia, igual que una dirección postal. El problema es que el cielo gira: la estrella que ves ahora a tu izquierda estará a tu derecha dentro de unas horas, y lo que ves desde tu ciudad no es lo que ve alguien en otra latitud. Hacen falta dos sistemas distintos: uno pegado a ti (el horizonte y el cenit de tu lugar) y otro pegado a las estrellas.

Esta semana aprendes los dos, a convertir las unidades que usan, y a responder una pregunta concreta: ¿por qué la altura de la estrella Polar sobre el horizonte te dice la latitud en la que estás?

## Las cinco sesiones

### Sesión 1 · Matemáticas: el plano cartesiano (30-35 min)

Un **punto del plano** se describe con dos números $(x, y)$: cuánto te desplazas en horizontal y en vertical desde un origen. Las **coordenadas** son exactamente eso, y el mapa del cielo no es más que un plano donde $x$ es la ascensión recta e $y$ la declinación (las definimos en la sesión 3). Lo importante es saber leer y dibujar: elegir una escala en cada eje, marcar los puntos y decidir en qué sentido crece cada eje. En los mapas del cielo es habitual que el eje horizontal crezca hacia la **izquierda**, porque se dibuja el cielo tal como lo ves cuando miras al sur, con el este a la izquierda.

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

La ascensión recta se mide en **horas**, porque está ligada a la rotación de la Tierra: en 24 horas el cielo da una vuelta completa de 360°, luego 1 hora equivale a 15°. Todo el sistema sexagesimal sigue: 1 minuto de tiempo equivale a 15′ de arco (la hora se divide en 60 minutos, como el grado) y 1 segundo de tiempo a 15″. Para pasar de horas y minutos a grados: $\text{grados} = (h + m/60) \cdot 15$.

La declinación se mide en grados y minutos de arco, con signo (positiva al norte del ecuador celeste, negativa al sur). Cuidado con los signos: −8° 12′ es −8,2°, es decir, −(8 + 12/60), no −8 + 0,2.

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

### Sesión 3 · Física: sistemas de referencia (30-40 min)

**Horizontal.** Está pegado al observador. Se mide la **altura** $h$ (ángulo sobre el horizonte, de 0° a 90° en el cenit) y el **azimut** $A$ (ángulo sobre el horizonte, contado desde el norte hacia el este, de 0° a 360°). Es intuitivo y tiene un defecto: cambia con el lugar y con la hora. Una estrella tiene altura y azimut distintos cada minuto.

**Ecuatorial.** Está pegado a las estrellas. Proyecta el ecuador terrestre en el cielo (el **ecuador celeste**) y los polos terrestres en los **polos celestes**. La **declinación** $\delta$ juega el papel de la latitud (de −90° a +90°) y la **ascensión recta** $\alpha$ el de la longitud, contada hacia el este desde el punto donde el Sol cruza el ecuador en marzo. Las coordenadas ecuatoriales de una estrella son prácticamente constantes: no dependen del lugar ni de la hora. Cambian muy despacio por la precesión del eje terrestre, unos 50″ al año, y por eso los catálogos indican la época de los datos (aquí, J2000).

**Por qué la Polar da tu latitud.** El eje de la Tierra apunta, con muy buena aproximación, hacia la Polar. El polo norte celeste está sobre el horizonte a una altura igual a tu latitud: en el polo norte de la Tierra está en el cenit (90°), en el ecuador está en el horizonte (0°). La Polar, a menos de 1° del polo celeste, se queda siempre prácticamente en el mismo sitio, y su altura es tu latitud con ese error.

**Altura máxima de una estrella.** Cada día una estrella cruza el meridiano (el arco norte-cenit-sur). El ecuador celeste corta el meridiano sur a una altura de $90^\circ - \varphi$, donde $\varphi$ es tu latitud norte. Una estrella con declinación $\delta$ está $\delta$ grados por encima de ese punto, luego

$$h_{\max} = 90^\circ - \varphi + \delta \quad (\text{si } \delta < \varphi), \qquad \text{y en general } h_{\max} = 90^\circ - |\varphi - \delta|.$$

De ahí salen las **circumpolares** (nunca se ponen, si $\delta > 90^\circ - \varphi$) y las que nunca salen desde tu latitud.

**Qué hacer**

1. Dibuja la esfera celeste con el horizonte, el cenit, el polo norte celeste a la altura de tu latitud y el ecuador celeste. Marca dónde cruza una estrella de $\delta = 20^\circ$.
2. Responde: ¿qué estrellas son circumpolares en el polo norte? ¿Y en el ecuador?

### Sesión 4 · Astronomía y observación (30-45 min)

**En el cielo (si está despejado).** Localiza la Polar prolongando cinco veces la distancia entre las dos estrellas del extremo del Carro (la Osa Mayor), o con Casiopea. Mide su altura con la mano, a brazo extendido (puño ≈ 10°) y compárala con tu latitud. Si tienes un cuadrante o una cruceta, el material de astronomas.org (recurso 1) explica cómo construirlos.

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

- **La respuesta.** Hay dos formas de situar un objeto: respecto a ti (altura y azimut, que cambian con la hora y el lugar) y respecto a las estrellas (ascensión recta y declinación, casi fijas). La altura de la Polar vale tu latitud porque el eje de la Tierra apunta, casi exactamente, hacia ella.
- **La causa.** La Tierra gira alrededor de un eje, que corta la esfera celeste en los polos celestes, y tu horizonte está inclinado respecto a ese eje según tu latitud.
- **Las herramientas.** Plano cartesiano y coordenadas; conversión entre horas, minutos y grados; y la fórmula de la altura máxima de una estrella en función de su declinación y de tu latitud.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [La esfera celeste y la observación a simple vista, astronomas.org](https://astronomas.org/files/documents/learning/esfera_celeste.pdf). Español, PDF didáctico para Bachillerato: coordenadas ecuatoriales y horizontales, cómo localizar la Polar y construir una cruceta y un cuadrante. Verificado el 31 de octubre de 2026.
2. [La esfera celestial, en *Mecánica celeste* de Tatum (LibreTexts Español)](https://espanol.libretexts.org/Fisica/Astronom%C3%ADa_y_Cosmolog%C3%ADa/Mec%C3%A1nica_Celestial_%28Tatum%29/06%3A_La_Esfera_Celestial). Español, nivel universitario avanzado: usa trigonometría esférica que aún no tienes. Para consultar más adelante, cuando llegues a las semanas 6 y 19. Licencia CC BY-NC 4.0. Verificado el 31 de octubre de 2026.
3. [4.1 Earth and Sky, *Astronomy* (OpenStax)](https://openstax.org/books/astronomy/pages/4-1-earth-and-sky). Inglés, introduce latitud, longitud, esfera celeste, declinación y ascensión recta. Verificado el 31 de octubre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
5. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
