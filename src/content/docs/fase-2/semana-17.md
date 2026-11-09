---
title: "Semana 17 · ¿Qué velocidad hace falta para no caer?"
description: "Fase 2 · Órbitas. Despejar en ecuaciones con raíces; órbita circular, velocidad orbital y periodo; energía potencial gravitatoria y velocidad de escape; satélites visibles."
sidebar:
  order: 17
  label: "17. ¿Qué velocidad hace falta para no caer?"
---

## La pregunta del cielo

Al anochecer, a veces se ve un punto de luz que cruza el cielo en pocos minutos, sin parpadear, y se apaga de golpe antes de llegar al horizonte. Es la Estación Espacial Internacional, a unos 400 km de altura. Está cayendo hacia la Tierra continuamente, como la Luna, y aun así no se acerca al suelo. ¿Cómo es posible?

Newton lo explicó con un experimento mental. Imagina un cañón en lo alto de una montaña altísima, por encima de la atmósfera, que dispara en horizontal. Con poca velocidad, la bala cae cerca. Con más, cae más lejos. Pero la Tierra es redonda: si la bala va lo bastante deprisa, el suelo se curva hacia abajo tan rápido como la bala cae, y nunca llega a tocarlo. Ha entrado en órbita. Y si va todavía más rápido, se aleja y no vuelve.

Esta semana calculas esas velocidades: la que hace falta para una órbita circular y la que hace falta para escapar. Para ello necesitas despejar incógnitas en ecuaciones con raíces y potencias, y una idea nueva: la energía potencial gravitatoria lejos de la superficie.

## Las cinco sesiones

### Sesión 1 · Matemáticas: despejar en ecuaciones (30-40 min)

**Qué es despejar.** Una **ecuación** es una igualdad con alguna cantidad desconocida, la **incógnita**. Despejar es reescribir la igualdad, paso a paso, hasta dejar la incógnita sola a un lado. La regla de oro: lo que hagas a un lado del signo igual, házselo al otro. Así la igualdad se mantiene.

Las operaciones se deshacen con su inversa, en orden contrario al que se aplicaron:

- una suma se deshace restando, y un producto, dividiendo;
- un cuadrado se deshace con una raíz cuadrada, y un cubo, con una raíz cúbica;
- en general, $x^n = y$ se deshace con $x = y^{1/n}$ (si $x$ es positivo, como las distancias y los tiempos).

**Ejemplo.** Despeja $r$ en $T = 2\pi\sqrt{r^3/(GM)}$.

1. Divide entre $2\pi$: $\;T/(2\pi) = \sqrt{r^3/(GM)}$.
2. Eleva al cuadrado para quitar la raíz: $\;T^2/(4\pi^2) = r^3/(GM)$.
3. Multiplica por $GM$: $\;G M T^2/(4\pi^2) = r^3$.
4. Haz la raíz cúbica: $\;r = \sqrt[3]{G M T^2/(4\pi^2)}$.

**Comprobar con las unidades.** Un buen hábito: al final, mira si las unidades encajan. Si te sale una distancia en segundos, hay un error. Por ejemplo, $GM/r$ tiene unidades de $(\text{m}^3/\text{s}^2)/\text{m} = \text{m}^2/\text{s}^2$, y su raíz cuadrada, m/s: una velocidad, bien.

:::note[De dónde viene la palabra]
**Ecuación** viene del latín *aequatio*, «igualación», de *aequus*, «igual» (como *equilibrio* o *ecuador*, la línea que divide la Tierra en dos mitades iguales). **Álgebra** viene del árabe *al-ŷabr*, «la restauración, recomponer lo roto», del título de un libro del matemático persa al-Juarismi, escrito en Bagdad hacia el año 820. Allí *al-ŷabr* era pasar un término restado al otro lado de la ecuación, donde queda sumando: «restaurarlo». Del nombre de al-Juarismi viene *algoritmo*. **Raíz** traduce el árabe *ŷiḏr*, que también significa «raíz de una planta»: el número del que «brota» el cuadrado.
:::

**Ejercicios**

1. Despeja $v$ en $\tfrac{1}{2} m v^2 = G M m / R$.
2. Despeja $M$ en $v = \sqrt{GM/r}$.
3. Despeja $r$ en $g = G M/r^2$. ¿A qué distancia del centro de la Tierra la gravedad vale la cuarta parte que en la superficie?

<details>
<summary>Soluciones</summary>

1. Divide por $m$ y multiplica por 2: $v^2 = 2GM/R$, así que **$v = \sqrt{2GM/R}$**. La masa $m$ desaparece.
2. Eleva al cuadrado: $v^2 = GM/r$, y multiplica por $r/G$: **$M = v^2 r / G$**.
3. **$r = \sqrt{GM/g}$**. Si $g$ se divide entre 4, $r$ se multiplica por $\sqrt{4} = 2$: a **dos radios terrestres** del centro, es decir, a 6371 km de altura.

</details>

### Sesión 2 · Matemáticas: raíces y órdenes de magnitud (30-35 min)

Con números astronómicos conviene calcular las raíces con notación científica. Para la raíz cuadrada, haz par el exponente de 10 y divídelo entre 2; para la cúbica, hazlo múltiplo de 3 y divídelo entre 3:

$$\sqrt{4 \times 10^{9}} = \sqrt{40 \times 10^{8}} \approx 6{,}3 \times 10^{4}, \qquad \sqrt[3]{8 \times 10^{22}} = \sqrt[3]{80 \times 10^{21}} \approx 4{,}3 \times 10^{7}.$$

Un truco útil: $GM$ aparece siempre junto, y para la Tierra vale $GM_\text{T} = 3{,}986 \times 10^{14}$ m³/s². Se conoce con mucha más precisión que $G$ y $M$ por separado, porque se mide directamente siguiendo satélites. Lo usaremos así.

**Ejercicios**

1. Calcula $\sqrt{3{,}986 \times 10^{14} / 6{,}771 \times 10^{6}}$ en m/s.
2. Calcula $\sqrt[3]{7{,}5 \times 10^{22}}$.
3. Estima de cabeza $\sqrt{1{,}2 \times 10^{8}}$.

<details>
<summary>Soluciones</summary>

1. El cociente es $5{,}89 \times 10^{7}$, y su raíz, $\approx 7{,}67 \times 10^{3}$ m/s: **7,67 km/s**. Es la velocidad de la Estación Espacial.
2. $75 \times 10^{21}$: $\sqrt[3]{75} \approx 4{,}22$, así que $\approx$ **4,22 × 10⁷**.
3. $\sqrt{1{,}2} \approx 1{,}1$ y $\sqrt{10^{8}} = 10^{4}$: $\approx$ **1,1 × 10⁴**, unos 11 000.

</details>

### Sesión 3 · Física: órbita circular y velocidad de escape (35-45 min)

**La órbita circular.** Un satélite en órbita circular de radio $r$ alrededor de un cuerpo de masa $M$ tiene una aceleración hacia el centro $v^2/r$ (semana 9). La única fuerza que actúa es la gravedad, $GMm/r^2$. La segunda ley de Newton, $F = ma$, dice:

$$\frac{G M m}{r^2} = m\,\frac{v^2}{r} \quad \Rightarrow \quad v_\text{orb} = \sqrt{\frac{G M}{r}}.$$

La masa del satélite se simplifica: una nave y un tornillo suelto en la misma órbita van a la misma velocidad. Por eso los astronautas flotan dentro de la estación: no es que no haya gravedad (a 400 km todavía es el 89 % de la del suelo), es que la estación y ellos caen exactamente igual. Están en **caída libre**.

Como el satélite recorre $2\pi r$ en un periodo, $v = 2\pi r/T$. Sustituyendo y despejando:

$$T = 2\pi\sqrt{\frac{r^3}{G M}}.$$

Es la **tercera ley de Kepler** ($T^2 \propto r^3$), ahora deducida de la gravitación y con la constante explicada: $4\pi^2/(GM)$.

**La energía potencial gravitatoria.** En la fase 1 (semana 12) usaste $E_p = m g h$ para la energía de altura. Esa fórmula supone que $g$ no cambia, y lejos de la superficie no es así. La expresión válida a cualquier distancia es

$$E_p = -\frac{G M m}{r}.$$

El signo menos sorprende. Se ha elegido que la energía potencial valga cero infinitamente lejos. Al acercarse, el cuerpo «cae» y pierde energía potencial, así que esta se vuelve negativa: cuanto más cerca, más negativa. Lo que importa nunca es el valor, sino los cambios. Cerca de la superficie, el cambio al subir una altura pequeña $h$ coincide con $mgh$.

**La velocidad de escape.** Un cuerpo lanzado hacia arriba frena porque convierte energía cinética en potencial. Si la energía total $E = \tfrac{1}{2}mv^2 - GMm/r$ es negativa, en algún momento se queda sin energía cinética y vuelve: está **ligado** al planeta. Si es cero o positiva, puede llegar infinitamente lejos. La velocidad mínima para escapar es la que hace $E = 0$:

$$\tfrac{1}{2} m v_\text{esc}^2 = \frac{G M m}{r} \quad \Rightarrow \quad v_\text{esc} = \sqrt{\frac{2 G M}{r}} = \sqrt{2}\;v_\text{orb}.$$

La velocidad de escape es siempre un 41 % mayor que la orbital a la misma distancia. Desde la superficie de la Tierra son **11,2 km/s** (unos 40 000 km/h), sin contar el rozamiento del aire.

**El cañón de Newton, con números.** Desde lo alto de la montaña de Newton (supongamos que a ras del suelo, sin aire):

- Con menos de 7,9 km/s, la bala acaba chocando con el suelo.
- Con 7,9 km/s exactos, órbita circular a ras de suelo.
- Entre 7,9 y 11,2 km/s, órbitas elípticas, con el perigeo en el punto de lanzamiento.
- A partir de 11,2 km/s, escapa. A 11,2 km/s exactos, la trayectoria es una parábola; por encima, una hipérbola. Son las otras dos curvas de Apolonio (semana 14).

**Qué hacer**

1. Calcula la velocidad y el periodo de una órbita circular a ras de la superficie de la Tierra ($r = 6371$ km).
2. Un satélite **geoestacionario** da una vuelta en un día sidéreo (86 164 s), así que, si está sobre el ecuador, se queda quieto sobre el mismo punto de la Tierra. ¿A qué radio orbita? ¿A qué altura?
3. Calcula la velocidad de escape de la Luna ($GM_\text{L} = 4{,}90 \times 10^{12}$ m³/s², $R = 1737$ km) y compárala con la de la Tierra.

<details>
<summary>Soluciones</summary>

1. $v = \sqrt{3{,}986\times10^{14} / 6{,}371\times10^{6}} \approx$ **7,91 km/s**, y $T = 2\pi r / v \approx 5060$ s, unos **84 minutos**.
2. $r = \sqrt[3]{GM T^2/(4\pi^2)} = \sqrt[3]{3{,}986\times10^{14} \cdot 86\,164^2 / 39{,}48} \approx$ **42 160 km** del centro, es decir, unos **35 790 km de altura**.
3. $v_\text{esc} = \sqrt{2 \cdot 4{,}90\times10^{12} / 1{,}737\times10^{6}} \approx$ **2,38 km/s**, casi cinco veces menos que en la Tierra. Por eso las misiones Apolo pudieron despegar de la Luna con un módulo pequeño.

</details>

### Sesión 4 · Astronomía y observación: satélites a simple vista (30-45 min)

Los satélites no brillan con luz propia: reflejan la luz del Sol. Para verlos hacen falta dos condiciones a la vez: que tú estés a oscuras y que el satélite, a cientos de kilómetros de altura, siga iluminado por el Sol. Eso ocurre en las dos o tres horas siguientes a la puesta de Sol y anteriores a la salida.

**Cómo reconocerlos.** Un satélite es un punto de luz que se mueve de forma continua, sin parpadear y sin luces de colores (los aviones llevan luces intermitentes). Tarda unos minutos en cruzar el cielo. A menudo se apaga a mitad de camino: es el momento en que entra en la sombra de la Tierra.

**La Estación Espacial Internacional** es el objeto artificial más brillante del cielo nocturno: puede brillar más que cualquier estrella. Se ve perfectamente desde una ciudad con mucha luz. Las predicciones de pasos para tu localidad se pueden consultar en el servicio *Spot the Station* de la NASA o en la web Heavens-Above. Cuando la veas, cronometra cuánto tarda en cruzar.

**Cálculo: hasta cuándo se ve.** Un satélite a una altura $h$ sigue iluminado mientras el Sol no esté demasiado por debajo de tu horizonte. Si el satélite está justo encima de ti, deja de recibir luz cuando la línea que va del satélite al Sol roza la Tierra. Con un dibujo y un poco de trigonometría sale que eso ocurre cuando el Sol está a un ángulo $\alpha$ bajo el horizonte tal que

$$\cos\alpha = \frac{R}{R + h}.$$

1. Calcula $\alpha$ para la Estación Espacial ($h = 400$ km, $R = 6371$ km).
2. El Sol baja unos 15° por hora respecto al horizonte en el mejor de los casos, y bastante menos en latitudes medias. ¿Durante cuánto tiempo después del ocaso, como mínimo, puede verse la estación en el cénit?
3. Calcula la velocidad angular con la que la ves pasar si cruza justo por encima: su velocidad dividida por su distancia, en grados por segundo.

<details>
<summary>Soluciones</summary>

1. $\cos\alpha = 6371/6771 \approx 0{,}941$, así que $\alpha \approx$ **20°**.
2. Al menos **una hora y veinte minutos** (20° / 15° por hora). En latitudes como las de España la ventana es más larga, porque el Sol no baja en vertical sino en diagonal; y en verano, más todavía.
3. $7{,}67 / 400 \approx 0{,}019$ rad/s $\approx$ **1,1° por segundo**: cruza un palmo de cielo en unos veinte segundos.

</details>

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 17:

- calcula y dibuja la velocidad orbital, la velocidad de escape y el periodo en función de la altura, y marca la Estación Espacial, los satélites GPS, los geoestacionarios y la Luna,
- simula el cañón de Newton: dispara en horizontal con distintas velocidades y ve cómo pasa de caer, a orbitar en círculo, a orbitar en elipse y a escapar,
- comprueba en la simulación que la energía total se conserva y que su signo decide si el proyectil vuelve o no.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-17.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-2/semana-17.ipynb)

## Qué has aprendido

- **La respuesta.** Para no caer al suelo hay que ir de lado lo bastante deprisa: $v = \sqrt{GM/r}$, unos 7,9 km/s a ras de la Tierra y 7,7 km/s a 400 km de altura. El satélite sigue cayendo, pero el suelo se curva al mismo ritmo. Para no volver nunca hace falta $\sqrt{2}$ veces más: 11,2 km/s desde la superficie.
- **La conexión.** De la gravitación de Newton sale la tercera ley de Kepler, con su constante: $T^2 = 4\pi^2 r^3/(GM)$.
- **Las herramientas.** Despejar incógnitas deshaciendo operaciones en orden inverso, raíces en notación científica, comprobación por unidades y la energía potencial $-GMm/r$ con el criterio de energía total para órbitas ligadas y libres.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Sección 13.3, Energía potencial gravitacional y energía total, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-3-energia-potencial-gravitacional-y-energia-total). Español; la energía potencial $-GMm/r$ y la velocidad de escape, con ejemplos. Verificado el 6 de noviembre de 2026.
2. [Sección 13.4, Órbita satelital y energía, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/13-4-orbita-satelital-y-energia). Español; velocidad y periodo de una órbita circular, con el ejemplo de la Estación Espacial. Verificado el 6 de noviembre de 2026.
3. [Spot the Station (NASA)](https://spotthestation.nasa.gov/). Predicciones de pasos de la Estación Espacial. **(Sin verificar)**.
4. [Heavens-Above](https://www.heavens-above.com/). Predicciones de pasos de satélites visibles. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno.
