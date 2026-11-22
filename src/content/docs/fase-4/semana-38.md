---
title: "Semana 38 · ¿Qué es la Vía Láctea y dónde estoy yo?"
description: "Fase 4 · El universo grande. Coordenadas galácticas con matrices de rotación, el año galáctico, la extinción del polvo y el error de Herschel y Kapteyn, la estructura de la Vía Láctea, la posición del Sol y la Vía Láctea en un cielo oscuro."
sidebar:
  order: 38
  label: "38. ¿Qué es la Vía Láctea y dónde estoy yo?"
---

## La pregunta del cielo

Desde un cielo oscuro, lejos de las luces, se ve cruzar el cielo una banda tenue y lechosa, con manchas más brillantes y franjas oscuras. En 1610, Galileo apuntó su anteojo hacia ella y vio que estaba formada por una multitud de estrellas demasiado débiles para distinguirlas a simple vista.

Hoy sabemos que esa banda es nuestra galaxia vista desde dentro: un disco de cientos de miles de millones de estrellas, gas y polvo, y que el Sol está en él, a medio camino entre el centro y el borde. Pero averiguarlo costó siglos, porque es muy difícil dibujar el mapa de una ciudad sin poder salir de ella, y además en una noche con niebla. Esta semana aprendes a situarte en la galaxia: con qué coordenadas se describe, cómo es, dónde estás y por qué los primeros que lo intentaron se equivocaron.

:::note[De dónde viene la palabra]
**Galaxia** viene del griego *galaxías*, «lechoso», de *gála, gálaktos*, «leche» (la misma raíz que *lactosa*). Según el mito griego, la banda se formó con la leche que se derramó del pecho de la diosa Hera. **Vía Láctea** es la traducción latina, *via lactea*, «camino de leche». En la tradición popular española también se ha llamado **Camino de Santiago**, porque guiaba a los peregrinos hacia el oeste. Durante siglos, «galaxia» significó solo esta banda; hasta el siglo XX no se usó para las demás galaxias.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: coordenadas galácticas (40-45 min)

**Un tercer sistema de coordenadas.** Ya conoces dos maneras de dar la posición de un astro: las **coordenadas ecuatoriales** (ascensión recta y declinación, semana 3), referidas al ecuador de la Tierra, y las **eclípticas** (semana 19), referidas a la órbita de la Tierra. Para estudiar la galaxia conviene un tercer sistema referido al plano de la propia galaxia: las **coordenadas galácticas**.

- La **latitud galáctica** $b$ es el ángulo por encima ($b > 0$) o por debajo ($b < 0$) del plano de la Vía Láctea, de −90° a +90°.
- La **longitud galáctica** $\ell$ se mide a lo largo del plano, de 0° a 360°, empezando en la dirección del **centro de la galaxia**, en Sagitario.

El **polo norte galáctico** está en la Cabellera de Berenice, cerca de la cola de Leo; mirando hacia allí, miras «hacia arriba», fuera del disco. La dirección opuesta al centro, $\ell = 180°$, el **anticentro**, está en Tauro, cerca de la frontera con Auriga.

**Cambiar de coordenadas es girar.** En la semana 19 aprendiste a pasar de unas coordenadas a otras con una **matriz de rotación**: se escribe cada dirección como un vector unitario $(x, y, z)$ y se multiplica por una matriz que gira los ejes. Para pasar de ecuatoriales a galácticas, la matriz (fijada por la Unión Astronómica Internacional y usada en el catálogo Hipparcos) es

$$T = \begin{pmatrix} -0{,}0549 & -0{,}8734 & -0{,}4838 \\ 0{,}4941 & -0{,}4448 & 0{,}7470 \\ -0{,}8677 & -0{,}1981 & 0{,}4560 \end{pmatrix}.$$

Cada fila tiene un significado: la primera es la dirección del centro galáctico en coordenadas ecuatoriales; la tercera, la del polo norte galáctico; la segunda completa el trío, perpendicular a las otras dos. Con el vector galáctico $(x', y', z') = T\,(x, y, z)$:

$$b = \arcsin z', \qquad \ell = \operatorname{atan2}(y', x').$$

(La función $\operatorname{atan2}$ da el ángulo correcto en los cuatro cuadrantes, como en la semana 19.)

**Ejercicios**

1. El centro galáctico tiene ascensión recta 266,4° y declinación −28,9°. Calcula su vector unitario ecuatorial, $(\cos\delta\cos\alpha, \cos\delta\sin\alpha, \sin\delta)$, y comprueba que coincide con la primera fila de $T$.
2. Comprueba que la primera y la tercera filas de $T$ son perpendiculares: su producto escalar (semana 9) debe ser casi cero.
3. ¿Qué latitud galáctica tiene el polo norte celeste, $(0, 0, 1)$ en ecuatoriales? Pista: mira la tercera columna de $T$.

<details>
<summary>Soluciones</summary>

1. $\cos(-28{,}9^\circ) = 0{,}875$: $(0{,}875 \cdot (-0{,}063), 0{,}875 \cdot (-0{,}998), -0{,}483) \approx$ **(−0,055; −0,873; −0,483)**. Coincide.
2. $(-0{,}0549)(-0{,}8677) + (-0{,}8734)(-0{,}1981) + (-0{,}4838)(0{,}4560) = 0{,}0476 + 0{,}1730 - 0{,}2206 \approx$ **0**.
3. $T\,(0,0,1)$ es la tercera columna, $(-0{,}4838; 0{,}7470; 0{,}4560)$, así que $b = \arcsin 0{,}456 \approx$ **27,1°**.

</details>

### Sesión 2 · Matemáticas: el año galáctico y la niebla del polvo (35-40 min)

**El Sol da vueltas a la galaxia.** El Sol está a unos 8,2 kpc (unos 27 000 años luz) del centro galáctico y gira a su alrededor a unos 230 km/s. Una vuelta completa, un **año galáctico**, dura

$$T = \frac{2\pi R}{v} = \frac{2\pi \cdot 8{,}2\ \text{kpc}}{230\ \text{km/s}}.$$

Con $1\ \text{kpc} = 3{,}086\times10^{16}$ km, sale unos $6{,}9\times10^{15}$ s, es decir, unos **220 millones de años**. Desde que se formó la Tierra, el Sol ha dado unas veinte vueltas. La última vez que estuvo donde está ahora, empezaban los dinosaurios.

**Por qué Herschel y Kapteyn se equivocaron.** En 1785, William Herschel contó las estrellas que veía con su telescopio en cientos de direcciones. Supuso que las estrellas se reparten de forma uniforme y que, donde veía más, la galaxia se extendía más lejos. Le salió una galaxia en forma de rueda aplastada, con el Sol cerca del centro. En 1922, Jacobus Kapteyn repitió el estudio con más datos y fotografía, y obtuvo lo mismo: una galaxia de unos 15 kpc, con el Sol casi en el centro.

El error estaba en una suposición que no se veía: el espacio no es transparente. El **polvo interestelar** absorbe la luz (semana 33), y en el plano de la galaxia lo hace tanto que, en luz visible, solo se ven unos pocos miles de pársecs en cualquier dirección. Como cuando estás en un bosque con niebla, ves árboles a tu alrededor más o menos hasta la misma distancia en todas direcciones, y te parece que estás en el centro del bosque.

**Un modelo de la niebla.** Si la luz se atenúa de forma exponencial con la distancia (semana 26), con una magnitud de extinción por kilopársec $a$, una estrella a una distancia $d$ se ve más débil en $a\,d$ magnitudes, además de lo que corresponde a su distancia:

$$m = M + 5\log_{10}\frac{d}{10\ \text{pc}} + a\,d.$$

En el plano de la galaxia, en luz visible, $a$ es del orden de 1 magnitud por kpc (con muchas variaciones). En 1930, Robert Trumpler lo demostró al ver que los cúmulos abiertos lejanos parecían, por su brillo, más lejanos de lo que indicaba su tamaño aparente.

**Ejercicios**

1. ¿Cuántas vueltas a la galaxia ha dado el Sol en sus 4600 millones de años?
2. Una cefeida de $M = -4$ está a 5 kpc, en el plano galáctico, con $a = 1$ mag/kpc. ¿Qué magnitud aparente tiene? ¿Qué distancia calcularías si olvidaras el polvo?
3. ¿A qué distancia la extinción, con $a = 1$ mag/kpc, reduce el brillo de una estrella a una centésima?

<details>
<summary>Soluciones</summary>

1. $4600/220 \approx$ **21 vueltas**.
2. $m = -4 + 5\log(500) + 5 = -4 + 13{,}5 + 5 =$ **14,5**. Sin polvo, $5\log(d/10) = 18{,}5$, $d = 10^{4{,}7} \approx$ **50 kpc**: diez veces más lejos de lo real.
3. Una centésima son 5 magnitudes: **5 kpc**.

</details>

### Sesión 3 · Física: la estructura de nuestra galaxia (40-45 min)

**Shapley encuentra el centro.** En 1918, Harlow Shapley midió la distancia a los **cúmulos globulares**, bolas de cientos de miles de estrellas viejas, usando sus estrellas variables (de un tipo parecido a las cefeidas). Vio que no se reparten alrededor del Sol, sino alrededor de un punto lejano en la dirección de Sagitario. Dedujo, con razón, que ese punto era el centro de la galaxia y que el Sol estaba lejos de él. (Sobrestimó las distancias, también por culpa del polvo, pero la idea era correcta.) Como Copérnico había sacado a la Tierra del centro del Sistema Solar, Shapley sacó al Sol del centro de la galaxia.

**La Vía Láctea hoy.** Combinando observaciones en radio, infrarrojo (que atraviesan el polvo, semana 30) y las posiciones y movimientos de Gaia, el retrato actual es:

- **El disco**, de unos 30 kpc (100 000 años luz) de diámetro y solo unos cientos de pársecs de espesor: aquí están casi todas las estrellas jóvenes, el gas y el polvo. Se ve con **brazos espirales**, zonas más densas donde se forman estrellas nuevas.
- **El bulbo y la barra**: en el centro, un abultamiento de estrellas viejas atravesado por una barra de unos pocos kiloparsecs. La Vía Láctea es una **espiral barrada**.
- **El centro**: un agujero negro supermasivo, **Sagitario A***, de unos 4 millones de masas solares. Se pesó siguiendo durante décadas las órbitas de las estrellas que giran a su alrededor (las leyes de Kepler de la semana 15 a otra escala), un trabajo que mereció el Nobel de Física de 2020 para Reinhard Genzel y Andrea Ghez.
- **El halo**: una esfera enorme y poco poblada de estrellas viejas y unos 150 cúmulos globulares, que rodea todo lo demás. Y, más allá, un halo invisible de **materia oscura** mucho más masivo que todas las estrellas juntas (semana 43).
- En total, entre 100 000 y 400 000 millones de estrellas.

**Dónde estás tú.** El Sol está en el disco, a unos 8,2 kpc del centro y apenas unos 20 pc por encima del plano medio, en una estructura menor entre dos brazos, el **brazo de Orión** o **brazo Local**. Gira alrededor del centro a unos 230 km/s, junto con las estrellas vecinas.

**Una galaxia con historia.** La Vía Láctea no se formó de una vez: ha crecido tragándose galaxias más pequeñas. En 2018, los movimientos de las estrellas medidos por Gaia revelaron los restos de una galaxia enana que chocó con la nuestra hace unos 10 000 millones de años, llamada Gaia-Encélado o Gaia-Salchicha (por la forma que dibujan sus estrellas en un diagrama de velocidades). Las Nubes de Magallanes, visibles desde el hemisferio sur, son dos galaxias satélites que nos acompañan.

:::note[De dónde viene la palabra]
**Halo** viene del griego *hálōs*, la era redonda donde se trillaba el grano y, por extensión, el anillo de luz alrededor del Sol o de la Luna. **Bulbo** viene de *bulbus*, «cebolla». **Espiral** viene de *spira*, «rosca, vuelta». Los **cúmulos globulares** se llaman así por su forma de globo, del latín *globus*, «bola».
:::

**Qué hacer**

1. Si la galaxia fuera del tamaño de la península ibérica (unos 1000 km de diámetro), ¿a qué distancia estaría el Sol del centro? ¿Qué grosor tendría el disco?
2. Explica por qué la Vía Láctea se ve como una banda que da la vuelta a todo el cielo, y no como una mancha.
3. ¿Por qué el centro de la galaxia, que es la zona más brillante, no se ve como algo deslumbrante desde la Tierra?

### Sesión 4 · Astronomía y observación: la Vía Láctea en un cielo oscuro (30-45 min)

**Hace falta oscuridad.** La Vía Láctea es tenue: desde una ciudad no se ve, y desde un pueblo con farolas, apenas. Para verla hace falta un **cielo rural oscuro**, sin Luna, y al menos 20 minutos de adaptación a la oscuridad. Si alguna vez puedes, escápate a un lugar así: es una de las experiencias que más impresionan en astronomía, y la más olvidada en el mundo urbano.

**En las noches de noviembre**, a primera hora, la Vía Láctea forma un arco que va del oeste al noreste pasando cerca del cénit:

- **Cisne**, al oeste: la parte más brillante a esta hora. Fíjate en la **Gran Grieta**, una franja oscura que divide la banda en dos: no es un hueco sin estrellas, sino nubes de polvo que tapan las que hay detrás.
- **Cefeo y Casiopea**, casi en el cénit: con los prismáticos, recorre despacio la zona entre Casiopea y Perseo; está llena de cúmulos y de nubes de estrellas.
- **Perseo y Auriga**, al noreste, subiendo. En Auriga y en el límite con Tauro está el **anticentro**: cuando lo miras, miras hacia fuera de la galaxia, hacia el borde del disco más cercano. Por eso la Vía Láctea es ahí más tenue que en verano.

**El centro, en verano.** El centro de la galaxia está en Sagitario, bajo en el horizonte sur en las noches de julio y agosto. Es la parte más brillante de la Vía Láctea, con nubes de estrellas que con prismáticos parecen arena.

**Los polos.** En el polo norte galáctico, en la Cabellera de Berenice (en primavera), miras perpendicular al disco: hay pocas estrellas y polvo, y se ven galaxias lejanas, como desde una ventana abierta.

**Con Stellarium.** Activa la cuadrícula de coordenadas galácticas (en las opciones de visualización) y sitúa el ecuador galáctico, el centro y el anticentro. Comprueba que la banda de la Vía Láctea sigue el ecuador galáctico.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 38:

- convierte coordenadas ecuatoriales en galácticas con la matriz de rotación,
- dibuja un mapa del cielo en coordenadas galácticas con las estrellas del catálogo HYG, separando las cercanas de las lejanas y luminosas,
- dibuja en tres dimensiones las estrellas a menos de 25 pc, con el Sol en el centro,
- simula los recuentos de estrellas de Herschel con y sin polvo, y muestra por qué parecía que el Sol estaba en el centro.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-38.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-38.ipynb)

## Qué has aprendido

- **La respuesta.** La Vía Láctea es una galaxia espiral barrada de unos 100 000 años luz de diámetro y cientos de miles de millones de estrellas, con un agujero negro supermasivo en el centro. La banda que vemos es su disco visto desde dentro. El Sol está en el disco, a unos 27 000 años luz del centro, y da una vuelta cada unos 220 millones de años.
- **Por qué costó saberlo.** El polvo del disco tapa la luz y hace creer que estamos en el centro. Hizo falta mirar los cúmulos globulares, fuera del disco, y la luz infrarroja y de radio, que atraviesan el polvo.
- **Las herramientas.** Las coordenadas galácticas, la matriz de rotación entre sistemas de coordenadas y la extinción en el módulo de distancia.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**Pesar la galaxia con la órbita del Sol.** En la semana 22 pesaste Júpiter con la órbita de sus lunas. Con el Sol se puede hacer lo mismo para la galaxia. Si la masa de la galaxia estuviera toda en el centro, la velocidad de una órbita circular de radio $R$ sería $v = \sqrt{GM/R}$ (semana 17). Despejando,

$$M(<R) = \frac{v^2 R}{G}.$$

En realidad la masa no está toda en el centro, pero para una distribución con simetría esférica el resultado es el mismo con $M(<R)$, la masa encerrada dentro de la órbita (el teorema de la cáscara de Newton). Para un disco no es exacto, pero da el orden de magnitud.

Con $v = 230$ km/s y $R = 8{,}2$ kpc sale una masa de unos $10^{11}$ masas solares dentro de la órbita del Sol. Pero si sumas las estrellas, el gas y el polvo que se ven dentro de esa órbita, salen menos. Y la cosa empeora más lejos: las estrellas y el gas de las afueras de la galaxia giran casi a la misma velocidad que el Sol, cuando, si casi toda la masa estuviera dentro, deberían ir más despacio, como los planetas exteriores. Hay más masa de la que se ve. Es la pista de la **materia oscura**, que estudiarás en la semana 43.

**La velocidad de escape de la galaxia.** Las estrellas más rápidas medidas cerca del Sol se mueven a unos 550 km/s respecto al centro galáctico, y no se han escapado. Con $v_e = \sqrt{2GM/R}$ (semana 17), eso exige una masa todavía mayor que la del cálculo anterior: más pistas de que la galaxia pesa más de lo que brilla.

**Ejercicios**

1. Calcula $M(<R) = v^2R/G$ con $v = 2{,}3\times10^5$ m/s, $R = 8{,}2 \cdot 3{,}086\times10^{19}$ m y $G = 6{,}67\times10^{-11}$. Pásala a masas solares ($2\times10^{30}$ kg).
2. Si una estrella a 16 kpc del centro girara alrededor de una masa de $10^{11}$ masas solares concentrada en el centro, ¿a qué velocidad lo haría? (Se observa que gira a más de 200 km/s.)
3. ¿Qué masa (como si estuviera concentrada en el centro) haría falta para que la velocidad de escape a 8,2 kpc fuera de 550 km/s?

<details>
<summary>Soluciones</summary>

1. $(2{,}3\times10^5)^2 \cdot 2{,}53\times10^{20}/6{,}67\times10^{-11} \approx 2{,}0\times10^{41}$ kg, unos **10¹¹ masas solares**.
2. $v \propto 1/\sqrt{R}$: al doble de distancia, $230/\sqrt{2} \approx$ **160 km/s**. La diferencia con lo observado es la pista de la materia oscura.
3. $M = v_e^2R/(2G) = (5{,}5\times10^5)^2 \cdot 2{,}53\times10^{20}/(2 \cdot 6{,}67\times10^{-11}) \approx 5{,}7\times10^{41}$ kg, unos **3 × 10¹¹ masas solares**, casi el triple.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Capítulo 25, La Vía Láctea, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/25%3A_La_V%C3%ADa_L%C3%A1ctea). Español; arquitectura de la galaxia, poblaciones estelares, el centro galáctico y su formación. Verificado el 20 de noviembre de 2026.
2. [Capítulo 20, Entre las estrellas: gas y polvo en el espacio, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/20%3A_Entre_las_estrellas_-_Gas_y_polvo_en_el_espacio). Español; el polvo interestelar, la extinción y el enrojecimiento. Verificado el 20 de noviembre de 2026.
3. [Explora el cosmos con ESASky (ESA)](https://www.esa.int/Space_in_Member_States/Spain/Explora_el_cosmos_con_ESASky). Español; para ver la Vía Láctea en infrarrojo y en microondas, donde el polvo no tapa. Verificado el 20 de noviembre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). Con la cuadrícula galáctica. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno. Los datos de estrellas proceden de la base HYG v4.1 (David Nash, CC BY-SA 4.0).
