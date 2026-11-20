---
title: "Semana 36 · ¿Qué queda cuando muere una estrella?"
description: "Fase 3 · La luz. Órdenes de magnitud de densidades y velocidades de escape, el radio de Schwarzschild, nebulosas planetarias y enanas blancas, supernovas, estrellas de neutrones y púlsares, agujeros negros, el origen de los elementos y restos estelares para buscar en el cielo."
sidebar:
  order: 36
  label: "36. ¿Qué queda cuando muere una estrella?"
---

## La pregunta del cielo

El 4 de julio de 1054, los astrónomos de la corte china anotaron la aparición de una «estrella invitada» cerca de una estrella de Tauro. Fue tan brillante que se vio de día durante más de tres semanas, y de noche durante casi dos años. Hoy, en ese lugar, hay una nube de gas deshilachada que se expande a unos 1500 km/s: la **nebulosa del Cangrejo**, M1, la primera del catálogo de Messier. En su centro gira, treinta veces por segundo, un objeto del tamaño de una ciudad con más masa que el Sol.

Esta semana terminas la historia de las estrellas que empezaste en la semana 35: qué les pasa cuando se les acaba el combustible. Según su masa, dejan tras de sí uno de tres cadáveres, cada uno más extraño que el anterior: una enana blanca, una estrella de neutrones o un agujero negro. Y en su muerte fabrican los elementos de los que estás hecho.

:::note[De dónde viene la palabra]
**Nova** es «nueva» en latín: Tycho Brahe tituló *De nova stella*, «Sobre la estrella nueva», su libro sobre la que vio aparecer en Casiopea en 1572. Hoy sabemos que no eran estrellas nuevas, sino estrellas viejas que estallaban. **Supernova** lo acuñaron Walter Baade y Fritz Zwicky a principios de la década de 1930 para las explosiones mucho más potentes que las novas corrientes. **Púlsar** es un acrónimo inglés de los años sesenta, *pulsating star*, «estrella que late».
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: órdenes de magnitud de lo extremo (35-45 min)

En la semana 21 aprendiste a estimar con órdenes de magnitud. Esta semana lo necesitas más que nunca: los restos de las estrellas están tan lejos de la experiencia diaria que solo se pueden pensar con potencias de diez.

**La densidad.** La densidad es masa entre volumen, $\rho = M/(\tfrac{4}{3}\pi R^3)$. Compara:

| Objeto | Masa | Radio | Densidad media |
|---|---|---|---|
| Agua | | | 1 g/cm³ |
| Sol | 1 $M_\odot$ | 696 000 km | 1,4 g/cm³ |
| Enana blanca típica | 0,6 $M_\odot$ | ~9000 km | ~5 × 10⁵ g/cm³ |
| Núcleo atómico | | | ~2 × 10¹⁴ g/cm³ |
| Estrella de neutrones | 1,4 $M_\odot$ | ~12 km | ~4 × 10¹⁴ g/cm³ |

Una cucharadita de enana blanca (5 cm³) pesaría unas 2 toneladas; una de estrella de neutrones, unos 2000 millones de toneladas, como todos los coches del mundo juntos. Una estrella de neutrones es, en el fondo, un núcleo atómico gigante.

**La velocidad de escape.** En la semana 17 viste que, para escapar de la gravedad de un cuerpo de masa $M$ desde su superficie, a una distancia $R$ del centro, hace falta una velocidad

$$v_e = \sqrt{\frac{2GM}{R}}.$$

Para la Tierra, 11,2 km/s; para el Sol, 618 km/s. Cuanto más compacto es un objeto (más masa en menos radio), mayor es su velocidad de escape.

**Ejercicios**

1. Calcula la densidad media de una enana blanca de 0,6 masas solares ($1{,}2\times10^{30}$ kg) y un radio de 8700 km. Pásala a g/cm³.
2. Calcula la velocidad de escape de esa enana blanca y la de una estrella de neutrones de 1,4 masas solares ($2{,}8\times10^{30}$ kg) y 12 km de radio. Exprésala como fracción de $c$.
3. ¿Qué radio tendría que tener la Tierra ($6\times10^{24}$ kg) para tener la densidad de una estrella de neutrones?

<details>
<summary>Soluciones</summary>

1. $V = \tfrac{4}{3}\pi(8{,}7\times10^6)^3 \approx 2{,}8\times10^{21}$ m³; $\rho \approx 4{,}4\times10^8$ kg/m³ $=$ **4,4 × 10⁵ g/cm³**: casi media tonelada por centímetro cúbico.
2. Enana blanca: $\sqrt{2\cdot6{,}67\times10^{-11}\cdot1{,}2\times10^{30}/8{,}7\times10^6} \approx 4{,}3\times10^6$ m/s, **4300 km/s, un 1,4 % de $c$**. Estrella de neutrones: $\sqrt{2\cdot6{,}67\times10^{-11}\cdot2{,}8\times10^{30}/1{,}2\times10^4} \approx 1{,}8\times10^8$ m/s, **casi un 60 % de $c$**.
3. $R = (3M/(4\pi\rho))^{1/3} = (3\cdot6\times10^{24}/(4\pi\cdot4\times10^{17}))^{1/3} \approx$ **150 m**. La Tierra entera, en un estadio de fútbol.

</details>

### Sesión 2 · Matemáticas: el radio de Schwarzschild (35-40 min)

**Cuando ni la luz escapa.** Si un objeto es tan compacto que su velocidad de escape iguala la de la luz, $v_e = c$, nada puede salir de él. Despejando $R$ en $c = \sqrt{2GM/R}$:

$$r_s = \frac{2GM}{c^2}.$$

Es el **radio de Schwarzschild**. Lo calculó en 1916 el astrónomo alemán Karl Schwarzschild con la relatividad general de Einstein (semana 45), en la trinchera del frente ruso, pocos meses antes de morir. Curiosamente, sale lo mismo con la gravedad de Newton: en 1783, el clérigo inglés John Michell ya había especulado con «estrellas oscuras» tan masivas que la luz no podría escapar de ellas. (Esa coincidencia es un poco de suerte: el razonamiento de Newton no es correcto para la luz, pero el resultado sí.)

Un objeto de masa $M$ comprimido dentro de su radio de Schwarzschild es un **agujero negro**, y la esfera de radio $r_s$ es su **horizonte de sucesos**: lo que la cruza no vuelve a salir, ni siquiera la luz. Como el horizonte de la Tierra (semana 1), marca el límite de lo que se puede ver.

**Una regla útil.** Con los números del Sol,

$$r_s \approx 2{,}95\ \text{km}\cdot\frac{M}{M_\odot}.$$

El Sol tendría que comprimirse hasta un radio de 3 km para ser un agujero negro; la Tierra, hasta 9 mm, como una canica.

**Los agujeros negros grandes no son densos.** El radio de Schwarzschild crece con la masa, $r_s \propto M$, y el volumen con su cubo. Así que la densidad media dentro del horizonte va como $M/M^3 = 1/M^2$: cuanto más masivo, menos denso. Los agujeros negros supermasivos del centro de las galaxias tienen una densidad media menor que la del agua.

**Ejercicios**

1. Calcula el radio de Schwarzschild de un agujero negro de 10 masas solares y el de Sagitario A*, el del centro de la Vía Láctea, de unos 4,3 millones de masas solares. Pásalo a ua ($1{,}5\times10^8$ km).
2. El de la galaxia M87, fotografiado en 2019, tiene unos 6500 millones de masas solares. ¿Cuánto mide su horizonte comparado con la órbita de Neptuno (30 ua)?
3. La densidad media de un agujero negro de 1 masa solar dentro de su horizonte es de unos $1{,}8\times10^{19}$ kg/m³. ¿A partir de qué masa la densidad media es menor que la del agua (1000 kg/m³)?

<details>
<summary>Soluciones</summary>

1. **29,5 km**; para Sagitario A*, $2{,}95 \cdot 4{,}3\times10^6 \approx 1{,}27\times10^7$ km, unas **0,085 ua**, menos que la órbita de Mercurio.
2. $2{,}95 \cdot 6{,}5\times10^9 \approx 1{,}9\times10^{10}$ km $\approx$ **128 ua**: unas cuatro veces la órbita de Neptuno.
3. La densidad va como $1/M^2$: hay que dividir por $1{,}8\times10^{16}$, así que $M = \sqrt{1{,}8\times10^{16}} \approx$ **1,3 × 10⁸ masas solares**.

</details>

### Sesión 3 · Física: tres maneras de morir (40-45 min)

**Las estrellas como el Sol: nebulosa planetaria y enana blanca.** Las estrellas de hasta unas 8 masas solares, tras su fase de gigante roja (semana 35), expulsan sus capas externas en un viento lento. El núcleo que queda, muy caliente, ilumina esas capas, que brillan durante unas decenas de miles de años como una **nebulosa planetaria** (el nombre es un error histórico: con los telescopios del siglo XVIII parecían discos de planetas). El núcleo desnudo, de carbono y oxígeno, es una **enana blanca**: del tamaño de la Tierra, con la masa de medio Sol.

Una enana blanca no tiene fusión. ¿Qué la sostiene contra su gravedad? No la presión térmica, sino una presión cuántica: los electrones no pueden ocupar todos el mismo estado (el **principio de exclusión de Pauli**, semana 46), y al apretarlos se resisten. Es la **presión de degeneración** de los electrones. En 1930, Subrahmanyan Chandrasekhar, con 19 años y en el barco que lo llevaba de la India a Inglaterra, calculó que esa presión tiene un límite: una enana blanca no puede tener más de unas **1,4 masas solares**, el **límite de Chandrasekhar**. Una enana blanca se va enfriando durante miles de millones de años, sin apagarse del todo nunca en la edad actual del universo.

La enana blanca más famosa es **Sirio B**, la compañera de Sirio. Friedrich Bessel dedujo en 1844 que Sirio tenía una compañera invisible por el vaivén de su movimiento, y Alvan Clark la vio en 1862 con un telescopio nuevo.

**Las estrellas masivas: supernova.** En las estrellas de más de unas 8 masas solares, el núcleo funde helio en carbono, carbono en neón, oxígeno, silicio... hasta llegar al **hierro**. Y ahí se acaba: fundir hierro no libera energía, la consume, porque el hierro está entre los núcleos más fuertemente ligados. El núcleo de hierro, de más de 1,4 masas solares, ya no se sostiene: en menos de un segundo se colapsa desde el tamaño de la Tierra hasta unos 20 km. Los electrones se combinan con los protones y forman neutrones y una avalancha de neutrinos. El colapso rebota y, con la ayuda de los neutrinos, lanza las capas externas a miles de kilómetros por segundo: una **supernova**. Durante unas semanas, una sola estrella brilla como miles de millones de soles.

En 1987 estalló una supernova en la Gran Nube de Magallanes, una galaxia vecina: la SN 1987A. Tres detectores en Japón, Estados Unidos y Rusia registraron unos veinte neutrinos de esa explosión, horas antes de que se viera su luz. Fue la confirmación de que las supernovas son colapsos de núcleos estelares.

**Estrellas de neutrones y púlsares.** Lo que queda del núcleo, sostenido por la presión de degeneración de los neutrones, es una **estrella de neutrones**: unas 1,4 masas solares en una esfera de unos 12 km. Al encogerse, gira cada vez más deprisa (como una patinadora que encoge los brazos, por la conservación del momento angular, semana 12) y su campo magnético se concentra enormemente. En 1967, la estudiante de doctorado Jocelyn Bell Burnell descubrió una señal de radio que se repetía cada 1,34 segundos con la regularidad de un reloj. Era el primer **púlsar**: una estrella de neutrones que emite dos haces de radiación por sus polos magnéticos y, al girar, nos barre con ellos como un faro. El púlsar del Cangrejo gira unas 30 veces por segundo.

**Agujeros negros.** Si el núcleo que colapsa tiene demasiada masa (más de unas 2 o 3 masas solares, el límite exacto no se conoce bien), ni los neutrones pueden sostenerlo, y nada conocido lo detiene: se forma un **agujero negro**. No se ven, pero se detectan por lo que hacen a su alrededor:

- **Cygnus X-1**, descubierta como fuente de rayos X en 1964, fue el primer candidato sólido: una estrella supergigante que gira alrededor de un compañero invisible de unas 20 masas solares, que le arranca gas.
- En septiembre de 2015, los detectores LIGO registraron por primera vez **ondas gravitacionales**: las ondulaciones del espacio-tiempo producidas por la fusión de dos agujeros negros de unas 30 masas solares cada uno, a más de mil millones de años luz.
- En 2019, el *Event Horizon Telescope*, una red de radiotelescopios del tamaño de la Tierra, publicó la primera imagen de la sombra de un agujero negro, el de la galaxia M87; en 2022, la del nuestro, Sagitario A*.

**Somos polvo de estrellas.** El hidrógeno y casi todo el helio del universo se formaron en los primeros minutos tras el Big Bang (semana 42). Todo lo demás se fabricó en las estrellas. El carbono de tus células y el oxígeno que respiras, en el interior de estrellas como el Sol y de estrellas más masivas; el calcio de tus huesos y el hierro de tu sangre, en estrellas masivas y en supernovas; buena parte del oro y de otros elementos más pesados que el hierro, en explosiones extremas, como la fusión de dos estrellas de neutrones que LIGO detectó en 2017. Las supernovas y los vientos estelares devuelven esos elementos al espacio, donde forman nuevas nubes, nuevas estrellas y nuevos planetas.

:::note[De dónde viene la palabra]
**Neutrón** une *neutro*, del latín *neuter*, «ni uno ni otro» (sin carga), y la terminación *-ón* de *electrón*. Lo descubrió James Chadwick en 1932. La expresión **agujero negro** la popularizó el físico estadounidense John Wheeler en 1967; hasta entonces se hablaba de «estrellas congeladas» o «colapsadas». **Planetaria** viene de *planeta*, «errante» (semana 13): las nebulosas planetarias no tienen nada que ver con los planetas.
:::

**Qué hacer**

1. Ordena estos objetos de menos a más denso: el Sol, Sirio B, el núcleo de un átomo, la nebulosa del Cangrejo, el púlsar del Cangrejo.
2. ¿Por qué un púlsar que gira 30 veces por segundo no puede ser una enana blanca? (Pista: lo ves en el apartado opcional.)
3. Calcula cuánta energía libera una supernova si en el colapso se convierten en energía unas 0,1 masas solares. Compárala con la que emitirá el Sol en toda su vida (unos $3{,}8\times10^{26}$ W durante $10^{10}$ años).

### Sesión 4 · Astronomía y observación: restos de estrellas en el cielo (30-45 min)

**La nebulosa del Cangrejo (M1)**, en Tauro, cerca de la estrella ζ Tauri, el «cuerno» sur del toro. Tiene magnitud 8,4, pero es extensa, así que su brillo se reparte. Con prismáticos 8×30, desde un cielo oscuro y con visión lateral, es una manchita alargada muy tenue: un reto. Merece la pena saber que lo que ves es la luz de la explosión de 1054, todavía en expansión, a unos 6500 años luz.

**La nebulosa Dumbbell (M27)**, en la pequeña constelación de la Zorra (Vulpecula), cerca de la Flecha (Sagitta), al oeste a primera hora de la noche en noviembre: la nebulosa planetaria más fácil, una mancha rectangular de magnitud 7,5 que se ve bien con prismáticos. Su estrella central es una enana blanca en formación.

**La nebulosa del Anillo (M57)**, en la Lira, entre Sheliak y Sulafat: con 8 aumentos parece solo una estrella algo borrosa; con un telescopio pequeño a unos 100 aumentos se ve como un anillo de humo.

**Betelgeuse**, que se hará supernova algún día. No se sabe cuándo, probablemente dentro de unas decenas de miles de años o más. Está a unos 500-700 años luz, demasiado lejos para hacernos daño, pero cuando estalle brillará durante semanas tanto como la Luna en cuarto. Entre finales de 2019 y principios de 2020 se oscureció tanto que se habló de una explosión inminente: hoy se sabe que fue una nube de polvo que expulsó.

**Las supernovas históricas** de nuestra galaxia visibles a simple vista: 1006 (en Lupus, la más brillante registrada), 1054 (el Cangrejo), 1572 (la de Tycho, en Casiopea) y 1604 (la de Kepler, en Ofiuco). Desde entonces, ninguna en la Vía Láctea que se haya visto, aunque estadísticamente debería haber una o dos por siglo: el polvo esconde muchas. Si sucede, la verás a simple vista.

**Sirio B**, al lado de Sirio, es una enana blanca a unos 10″ de su brillantísima compañera. No se ve con prismáticos, ni siquiera con telescopios pequeños: el resplandor de Sirio la tapa. Pero cuando mires Sirio, piensa que tiene al lado una estrella del tamaño de la Tierra con la masa del Sol.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 36:

- programa una calculadora del radio de Schwarzschild y la aplica a objetos que van de una persona a un agujero negro supermasivo,
- dibuja en escala logarítmica las densidades de todo lo que has visto en la fase,
- calcula la relación entre la masa y el radio de las enanas blancas con una fórmula aproximada y ve cómo se desploma al acercarse al límite de Chandrasekhar,
- compara las fuerzas de marea cerca de un agujero negro pequeño y de uno supermasivo,
- calcula el periodo de giro mínimo de una enana blanca y de una estrella de neutrones.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-36.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-3/semana-36.ipynb)

## Qué has aprendido

- **La respuesta.** Lo que queda depende de la masa. Las estrellas como el Sol dejan una enana blanca y una nebulosa planetaria; las de más de unas 8 masas solares estallan como supernovas y dejan una estrella de neutrones o, si son muy masivas, un agujero negro.
- **El origen de tus átomos.** Casi todos los elementos más pesados que el helio se fabricaron en estrellas y se esparcieron al morir ellas.
- **Las herramientas.** Órdenes de magnitud con densidades y velocidades de escape, y el radio de Schwarzschild, $r_s = 2GM/c^2$.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la fase 4. Es para volver a él cuando quieras profundizar.

**Mareas cerca de un agujero negro.** En la semana 21 viste que la diferencia de aceleración gravitatoria entre dos puntos separados una distancia $\ell$, a una distancia $r$ de una masa $M$, es aproximadamente

$$\Delta a \approx \frac{2GM\,\ell}{r^3}.$$

Para una persona de 2 m de alto, de pie con los pies hacia un agujero negro, $\Delta a$ es lo que la estira. En el horizonte, $r = r_s = 2GM/c^2$, y sustituyendo,

$$\Delta a_\text{horizonte} \approx \frac{2GM\,\ell}{(2GM/c^2)^3} = \frac{\ell\,c^6}{4G^2M^2}.$$

¡Va como $1/M^2$! Cuanto más masivo es el agujero negro, más **suave** es la marea en su horizonte. Cerca de un agujero negro de pocas masas solares, una persona sería estirada como un espagueti mucho antes de llegar al horizonte (los físicos lo llaman, en serio, **espaguetización**). En uno supermasivo, cruzaría el horizonte sin notar nada especial... y ya no podría volver.

**El periodo mínimo de un púlsar.** Un objeto que gira demasiado deprisa se rompe: la gravedad en su ecuador tiene que poder producir la aceleración hacia el centro del giro (semana 9), $\omega^2 R \le GM/R^2$. El periodo mínimo es

$$P_\text{mín} = 2\pi\sqrt{\frac{R^3}{GM}} = \sqrt{\frac{3\pi}{G\,\bar\rho}},$$

que solo depende de la densidad media. En 1968, Thomas Gold usó este argumento para demostrar que los púlsares rápidos solo podían ser estrellas de neutrones.

**Ejercicios**

1. Calcula $\Delta a$ en el horizonte para una persona de 2 m junto a un agujero negro de 10 masas solares ($2\times10^{31}$ kg) y junto a Sagitario A* ($8{,}6\times10^{36}$ kg). Compara con la gravedad de la Tierra, 9,8 m/s².
2. Calcula $P_\text{mín}$ para una enana blanca de densidad media $5\times10^8$ kg/m³ y para una estrella de neutrones de $4\times10^{17}$ kg/m³.
3. Comprueba que $2\pi\sqrt{R^3/(GM)}$ y $\sqrt{3\pi/(G\bar\rho)}$ son la misma expresión, con $\bar\rho = M/(\tfrac{4}{3}\pi R^3)$.

<details>
<summary>Soluciones</summary>

1. Con $\ell = 2$ m: para 10 masas solares, $r_s \approx 29{,}5$ km y $\Delta a \approx 2\cdot6{,}67\times10^{-11}\cdot2\times10^{31}\cdot2/(2{,}95\times10^4)^3 \approx$ **2 × 10⁸ m/s²**, veinte millones de veces la gravedad terrestre. Para Sagitario A*, $r_s \approx 1{,}27\times10^{10}$ m y $\Delta a \approx$ **1 × 10⁻³ m/s²**, imperceptible.
2. Enana blanca: $\sqrt{3\pi/(6{,}67\times10^{-11}\cdot5\times10^8)} \approx$ **17 s**. Estrella de neutrones: $\sqrt{3\pi/(6{,}67\times10^{-11}\cdot4\times10^{17})} \approx 6\times10^{-4}$ s, **0,6 milisegundos**. Un púlsar de 33 ms solo puede ser una estrella de neutrones. (El púlsar más rápido conocido gira 716 veces por segundo: 1,4 ms.)
3. $R^3/(GM) = R^3/(G\bar\rho\,\tfrac{4}{3}\pi R^3) = 3/(4\pi G\bar\rho)$, y $2\pi\sqrt{3/(4\pi G\bar\rho)} = \sqrt{4\pi^2\cdot3/(4\pi G\bar\rho)} = \sqrt{3\pi/(G\bar\rho)}$.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Capítulo 23, La muerte de las estrellas, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/23%3A_La_muerte_de_las_estrellas). Español; enanas blancas, supernovas, púlsares y la SN 1987A. Verificado el 20 de noviembre de 2026.
2. [Capítulo 24, Agujeros negros y espacio-tiempo curvo, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/24%3A_Agujeros_negros_y_espacio-tiempo_curvo). Español; horizonte de sucesos, pruebas de los agujeros negros y ondas gravitacionales. Verificado el 20 de noviembre de 2026.
3. [Capítulo 22, Estrellas de la adolescencia a la vejez, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/22%3A_Estrellas_de_la_Adolescencia_a_la_Vejez). Español; nebulosas planetarias y el final de las estrellas como el Sol. Verificado el 20 de noviembre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). Para localizar M1, M27 y M57. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
