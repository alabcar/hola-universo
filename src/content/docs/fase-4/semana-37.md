---
title: "Semana 37 · ¿Cómo medimos la distancia a las estrellas?"
description: "Fase 4 · El universo grande. La paralaje estelar, segundos y milisegundos de arco, la propagación de errores, la escalera de distancias, las candelas estándar y las cefeidas, las misiones Hipparcos y Gaia, y estrellas cercanas y variables para observar."
sidebar:
  order: 37
  label: "37. ¿Cómo medimos la distancia a las estrellas?"
---

## La pregunta del cielo

Durante dos mil años, uno de los mejores argumentos contra la idea de que la Tierra gira alrededor del Sol fue que las estrellas no se movían. Si la Tierra recorriera una órbita enorme, decían Aristóteles y, siglos después, Tycho Brahe, las estrellas cercanas deberían cambiar un poco de posición a lo largo del año respecto a las lejanas, igual que un árbol cercano se mueve respecto a las montañas cuando caminas. Nadie lo veía. Los copernicanos solo podían responder que las estrellas estaban muchísimo más lejos de lo que nadie imaginaba.

Tenían razón. En 1838, el alemán Friedrich Bessel midió por fin ese vaivén para la estrella 61 Cygni: un tercio de segundo de arco, el tamaño de una moneda vista a 15 km. Con ese ángulo diminuto, calculó la primera distancia a una estrella: unos 10 años luz. Esta semana empiezas la última fase del plan, la del universo grande, con la medida en la que se apoyan todas las demás distancias del cosmos.

:::note[De dónde viene la palabra]
**Paralaje** viene del griego *parállaxis*, «cambio, alternancia», del verbo *parallássein*, «alternar, cambiar de sitio»: el cambio aparente de posición de un objeto cuando cambias de punto de vista. **Astrometría** une *ástron*, «estrella», y *métron*, «medida»: la parte de la astronomía que mide posiciones y movimientos. **Gaia**, el nombre de la misión de la ESA, es el de la diosa griega de la Tierra; al principio era también una sigla, de *Global Astrometric Interferometer for Astrophysics*, aunque el diseño final ya no usó la interferometría.
:::

## Las cinco sesiones

### Sesión 1 · Matemáticas: el triángulo de la paralaje (35-45 min)

**El experimento del pulgar.** Estira el brazo con el pulgar hacia arriba y míralo alternando los ojos: el pulgar salta respecto al fondo. Tus ojos están separados unos 6,5 cm, y el pulgar, a unos 60 cm. Ese salto es la paralaje. Si acercas el pulgar, salta más; si lo alejas, menos. Midiendo el salto y conociendo la separación entre los ojos, podrías calcular la distancia al pulgar.

**Con la órbita de la Tierra.** Para las estrellas, la «separación entre los ojos» es el diámetro de la órbita terrestre. Se mide la posición de una estrella cercana respecto a otras muy lejanas, y se repite seis meses después, desde el otro lado de la órbita. Por convenio, la **paralaje** $p$ es la mitad del ángulo total que se desplaza: el ángulo con el que se vería el radio de la órbita, 1 ua, desde la estrella. En el triángulo rectángulo que forman el Sol, la Tierra y la estrella (semana 7),

$$\tan p = \frac{1\ \text{ua}}{d}.$$

Como $p$ es pequeñísimo, $\tan p \approx p$ en radianes (semana 2), y $d \approx 1\ \text{ua}/p$.

**El pársec, otra vez.** En la semana 33 viste que una estrella con una paralaje de un segundo de arco está a un **pársec**. En la práctica, con $p$ en segundos de arco,

$$d\ (\text{pc}) = \frac{1}{p\ (\text{''})}.$$

Las paralajes modernas se dan en **milisegundos de arco** (mas): $1\ \text{mas} = 0{,}001''$. Una paralaje de 10 mas son 100 pc; una de 1 mas, 1000 pc.

**Ejercicios**

1. En el experimento del pulgar, ¿qué ángulo salta el pulgar? Usa $6{,}5/60$ en radianes y pásalo a grados.
2. La paralaje de Sirio es de 0,379″. ¿A qué distancia está, en pársecs y en años luz?
3. Una estrella tiene una paralaje de 2,5 mas. ¿A qué distancia está?
4. ¿Qué tamaño tiene una moneda de 2 cm vista con un ángulo de 0,3″? Pista: la aproximación de ángulo pequeño, con $1'' = 1/206\,265$ rad.

<details>
<summary>Soluciones</summary>

1. $0{,}108$ rad $\approx$ **6,2°**: el salto que ves es grande porque el pulgar está muy cerca.
2. $1/0{,}379 \approx$ **2,64 pc**, unos **8,6 años luz**.
3. $1/0{,}0025 =$ **400 pc**.
4. $d = 0{,}02 \cdot 206\,265/0{,}3 \approx 13\,750$ m: a unos **14 km**.

</details>

### Sesión 2 · Matemáticas: cuánto nos fiamos de una distancia (35-45 min)

**Toda medida tiene un error.** Una paralaje se mide con una incertidumbre, $\sigma_p$. ¿Qué incertidumbre tiene la distancia que sale de ella? Para errores pequeños, se usa la derivada (semana 10): si $d = 1/p$, un cambio pequeño $\Delta p$ produce un cambio

$$\Delta d \approx \left|\frac{dd}{dp}\right|\Delta p = \frac{\Delta p}{p^2}.$$

Dividiendo por $d = 1/p$:

$$\frac{\sigma_d}{d} \approx \frac{\sigma_p}{p}.$$

**El error relativo de la distancia es el error relativo de la paralaje.** Si mides una paralaje con un 10 % de incertidumbre, la distancia tiene un 10 % de incertidumbre. Pero, como las paralajes son cada vez más pequeñas con la distancia y el error del instrumento es más o menos fijo, el error relativo crece deprisa con la distancia.

**De Hipparcos a Gaia.** El satélite Hipparcos de la ESA (1989-1993) midió paralajes con un error de alrededor de 1 mas. Con un 10 % de error máximo aceptable, eso permitía distancias de hasta 100 pc. Gaia mide las estrellas brillantes con errores de unas centésimas de mas: decenas de veces mejor, y llega a miles de pársecs.

**Cuando el error es grande.** Si $\sigma_p$ es comparable a $p$, la fórmula de propagación deja de valer, y la distancia $1/p$ puede ser muy engañosa (incluso salen paralajes negativas, que no tienen sentido físico pero son el resultado honesto de una medida con mucho ruido). Los astrónomos usan entonces métodos estadísticos más cuidadosos. El cuaderno lo muestra con una simulación.

**Ejercicios**

1. Una estrella tiene $p = 20 \pm 1$ mas. ¿Qué distancia y qué incertidumbre tiene?
2. Con un error de 1 mas, ¿a qué distancia el error relativo llega al 10 %? ¿Y con 0,02 mas?
3. Bessel midió para 61 Cygni 0,314″; el valor moderno es 0,286″. ¿Qué error relativo cometió? ¿Qué distancia daba y cuál es la actual?

<details>
<summary>Soluciones</summary>

1. $d = 50$ pc; error relativo $1/20 = 5$ %, así que **50 ± 2,5 pc**.
2. Con $\sigma_p/p = 0{,}1$: $p = 10$ mas, **100 pc**. Con 0,02 mas: $p = 0{,}2$ mas, **5000 pc**.
3. $(0{,}314 - 0{,}286)/0{,}286 \approx$ **10 %**. Daba $1/0{,}314 \approx 3{,}2$ pc (**10,4 años luz**); hoy, $1/0{,}286 \approx 3{,}5$ pc (**11,4 años luz**). Un resultado excelente para 1838.

</details>

### Sesión 3 · Física: la escalera de distancias (40-45 min)

**Ninguna regla mide todo.** La paralaje solo funciona para estrellas relativamente cercanas. Para ir más lejos, los astrónomos han construido una **escalera de distancias**: cada peldaño mide distancias mayores y se calibra con el anterior.

1. **El radar y las leyes de Kepler**, para el Sistema Solar: el valor de la unidad astronómica se fijó con ecos de radar en Venus a partir de 1961.
2. **La paralaje**, hasta unos miles de pársecs con Gaia.
3. **El ajuste de la secuencia principal**: si mides el diagrama HR de un cúmulo en magnitudes aparentes y lo comparas con el de las estrellas cercanas en magnitudes absolutas, la diferencia es el módulo de distancia (semana 33).
4. **Las candelas estándar**: objetos de luminosidad conocida. Si sabes cuánto brilla de verdad algo ($M$) y mides cuánto brilla en el cielo ($m$), el módulo de distancia te da la distancia. Las más importantes son las cefeidas y las supernovas de tipo Ia (semanas 40 y 41).
5. **La ley de Hubble**, para las galaxias más lejanas (semana 41).

**Las cefeidas y Henrietta Leavitt.** Las **cefeidas** son estrellas supergigantes que pulsan: se hinchan y se encogen con un periodo regular de días o semanas, y su brillo sube y baja con él. Henrietta Swan Leavitt, que trabajaba en el observatorio de Harvard midiendo placas fotográficas (semana 32), estudió cientos de estrellas variables en la Pequeña Nube de Magallanes. Como todas estaban más o menos a la misma distancia, sus diferencias de brillo aparente eran diferencias de brillo real. En 1912 publicó que **cuanto más largo es el periodo de una cefeida, más luminosa es**. Es la **relación periodo-luminosidad**, o **ley de Leavitt**. Basta medir el periodo de una cefeida, que no depende de la distancia, para saber su luminosidad; y con su brillo aparente, su distancia. Faltaba calibrarla con alguna cefeida cercana de distancia conocida, y Ejnar Hertzsprung lo hizo, de forma aproximada, en 1913. Con ella, Hubble mediría en 1925 la distancia a Andrómeda (semana 40).

**Gaia.** La misión Gaia de la ESA, lanzada el 19 de diciembre de 2013, ha medido posiciones, paralajes y movimientos de casi dos mil millones de estrellas de la Vía Láctea, el mayor mapa en tres dimensiones de nuestra galaxia. Dejó de observar en 2025, tras agotar su combustible, pero el trabajo sigue: su cuarta publicación de datos, **Gaia DR4**, basada en 66 meses de observaciones, está prevista para el **2 de diciembre de 2026**. En los cuadernos de esta fase la usarás de forma opcional, porque requiere conexión al archivo de la ESA.

:::note[De dónde viene la palabra]
**Cefeida** viene de δ (delta) Cephei, la estrella de la constelación de Cefeo en la que se descubrió este tipo de variabilidad en 1784 (por John Goodricke, el mismo de Algol en la semana 33). Cefeo era, en la mitología griega, un rey de Etiopía, padre de Andrómeda. **Candela estándar** es una metáfora: una vela de brillo conocido que, por lo débil que la ves, te dice lo lejos que está (*candela* viene de *candere*, «brillar», semana 31).
:::

**Qué hacer**

1. Una cefeida tiene, por su periodo, una magnitud absoluta $M = -4$, y se ve con $m = 21$. ¿A qué distancia está? (Ignora el polvo.)
2. Explica por qué una cefeida es más útil que una estrella normal de la secuencia principal para medir distancias grandes.
3. ¿Qué peldaño de la escalera usarías para medir la distancia a las Pléyades? ¿Y a la galaxia de Andrómeda?

### Sesión 4 · Astronomía y observación: estrellas cercanas y una cefeida a simple vista (30-45 min)

**Estrellas de paralaje grande que puedes ver.** Todas a menos de 6 pc:

| Estrella | Paralaje | Distancia | Dónde y cuándo |
|---|---|---|---|
| Sirio | 0,379″ | 8,6 años luz | Can Mayor, de madrugada en noviembre, al anochecer en invierno |
| ε Eridani | 0,311″ | 10,5 años luz | Erídano, baja al sur en las noches de noviembre a enero, magnitud 3,7 |
| Proción | 0,285″ | 11,5 años luz | Can Menor, desde medianoche en noviembre |
| 61 Cygni | 0,286″ | 11,4 años luz | Cisne, al oeste a primera hora en noviembre, magnitudes 5,2 y 6,1 |
| τ Ceti | 0,274″ | 11,9 años luz | Ballena, al sur en las noches de otoño, magnitud 3,5 |
| Altair | 0,195″ | 16,7 años luz | Águila, al oeste a primera hora en noviembre |

**61 Cygni con prismáticos.** La estrella de Bessel es doble: dos enanas naranjas separadas unos 31″. Desde un cielo algo oscuro, búscala con Stellarium junto al «cuerpo» del Cisne y, con los prismáticos bien apoyados, intenta separar sus dos componentes. Fíjate en su color anaranjado: son estrellas de tipo K, más frías que el Sol. La miras sabiendo que fue la primera estrella cuya distancia se midió.

**δ Cephei, la cefeida original.** Está en Cefeo, alta al norte en las noches de otoño. Su brillo oscila entre las magnitudes 3,5 y 4,4 con un periodo de 5,37 días. Puedes seguirla con el método de Argelander de la semana 33, usando dos estrellas de comparación cercanas, ζ Cephei (magnitud 3,4) y ε Cephei (4,2). Mírala una vez cada noche despejada durante dos o tres semanas, anota la fecha, la hora y tu estimación, y dibuja después su curva de luz: verás el periodo y la forma asimétrica típica, con una subida rápida y una bajada lenta.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 37:

- simula el movimiento aparente de una estrella cercana a lo largo de varios años: la elipse de la paralaje y el desplazamiento de su movimiento propio,
- calcula distancias a partir de paralajes y propaga sus errores,
- muestra con una simulación por qué $1/p$ es engañosa cuando el error es grande,
- usa el catálogo HYG de la semana 35 para ver cómo se reparten las distancias,
- incluye, como opción no probada, una consulta al archivo de Gaia.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-37.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-4/semana-37.ipynb)

## Qué has aprendido

- **La respuesta.** Las distancias a las estrellas cercanas se miden con la paralaje: el pequeño vaivén anual que les produce el movimiento de la Tierra alrededor del Sol. Una paralaje de $p$ segundos de arco corresponde a $1/p$ pársecs. Para distancias mayores se usan candelas estándar, como las cefeidas, calibradas con las paralajes.
- **La precisión.** El error relativo de la distancia es el de la paralaje. Hipparcos llegó a unos 100 pc con buena precisión; Gaia, a miles.
- **Las herramientas.** El triángulo de la paralaje, la aproximación de ángulo pequeño en segundos de arco, la propagación de errores con la derivada y la idea de la escalera de distancias.

## Para ir más lejos (opcional)

Este apartado no hace falta para seguir con la semana siguiente. Es para volver a él cuando quieras profundizar.

**La forma de la elipse de paralaje.** Visto desde una estrella, el movimiento de la Tierra alrededor del Sol es una circunferencia de radio 1 ua. Desde la Tierra, la estrella describe el reflejo de ese movimiento: una figura de radio angular $p$. Pero no siempre se ve como un círculo: depende de cómo esté inclinada la órbita respecto a la visual.

Si la estrella está en el **polo de la eclíptica** (perpendicular al plano de la órbita), ves la órbita de frente, y la estrella describe un círculo de radio $p$. Si está **en la eclíptica**, ves la órbita de canto, y la estrella va y viene en línea recta, con amplitud $p$. En general, con la estrella a una **latitud eclíptica** $\beta$ (la latitud en las coordenadas eclípticas de la semana 19), la circunferencia se ve proyectada como una **elipse** de semiejes

$$a = p, \qquad b = p\,\sin\beta.$$

Es la misma proyección que convierte un círculo inclinado en una elipse (semana 14): las distancias en la dirección de la inclinación se multiplican por el seno del ángulo de visión.

**Y además, el movimiento propio.** Las estrellas se mueven de verdad por la galaxia, y su posición cambia poco a poco en línea recta: es el **movimiento propio**, $\mu$, en segundos de arco por año. Sumado a la elipse anual, el camino de una estrella cercana en el cielo es una línea ondulada, una especie de muelle visto de lado. Separar las dos cosas exige observar durante varios años: por eso las misiones astrométricas duran tanto.

**Ejercicios**

1. 61 Cygni está a una latitud eclíptica de unos 52°. ¿Qué semiejes tiene su elipse de paralaje?
2. Sirio tiene una latitud eclíptica de unos −40°. ¿Cuánto mide el semieje menor de su elipse? ¿Qué forma tendría la de una estrella en la eclíptica?
3. La estrella de Barnard tiene un movimiento propio de 10,4″ por año. ¿En cuántos años recorre en el cielo el diámetro aparente de la Luna llena (unos 1800″)?

<details>
<summary>Soluciones</summary>

1. $a = 0{,}286''$; $b = 0{,}286 \cdot \sin 52^\circ \approx$ **0,225″**.
2. $b = 0{,}379 \cdot |\sin(-40^\circ)| \approx$ **0,244″**. En la eclíptica, $\sin 0 = 0$: un segmento recto de longitud $2p$.
3. $1800/10{,}4 \approx$ **173 años**. Es la estrella con mayor movimiento propio conocido: en una vida humana se mueve casi media Luna.

</details>

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [Capítulo 19, Distancias celestiales, *Astronomía* (OpenStax), en LibreTexts Español](https://espanol.libretexts.org/Bookshelves/Fisica/Astronomia_y_Cosmologia/Libro%3A_Astronom%C3%ADa_(OpenStax)/19%3A_Distancias_Celestiales). Español; unidades, paralaje, estrellas variables y la escalera de distancias. Verificado el 20 de noviembre de 2026.
2. [Última luz estelar para la pionera Gaia (ESA)](https://www.esa.int/Space_in_Member_States/Spain/Ultima_luz_estelar_para_la_pionera_Gaia). Español; resumen de la misión y su final. Verificado el 20 de noviembre de 2026.
3. [Gaia Data Release 4 (ESA)](https://www.cosmos.esa.int/web/gaia/data-release-4). Inglés; la página oficial de la cuarta publicación de datos. Verificado el 20 de noviembre de 2026.
4. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). Para localizar 61 Cygni, δ Cephei y sus estrellas de comparación. **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros. Las gráficas las genera el cuaderno. Los datos de estrellas proceden de la base HYG v4.1 (David Nash, CC BY-SA 4.0).
