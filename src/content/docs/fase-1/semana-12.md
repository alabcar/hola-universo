---
title: "Semana 12 · ¿Qué se conserva cuando todo se mueve?"
description: "Fase 1 · Principios básicos de astronomía. Energía cinética y potencial, conservación de la energía y repaso de la fase."
sidebar:
  order: 12
  label: "12. ¿Qué se conserva cuando todo se mueve?"
---

## La pregunta del cielo

Todo cambia en el cielo: la Luna cambia de fase, los planetas se desplazan, el Sol sube y baja. Pero la física que lo describe se apoya en un puñado de cantidades que **no** cambian. Encontrar lo que se conserva es una de las ideas más potentes de la ciencia, porque permite predecir sin seguir el movimiento paso a paso. La energía es la más importante.

Esta semana cierras la fase 1: aprendes qué es la energía cinética y la potencial, qué significa que se conserve, repasas lo estudiado en las semanas anteriores con un conjunto de problemas combinados, y terminas con una simulación que anticipa los problemas de la fase 2: un método numérico que no conserve la energía hace que un péndulo (o un planeta) se comporte de forma imposible.

## Las cinco sesiones

### Sesión 1 · Matemáticas: despejar fórmulas de energía (30-40 min)

La **energía cinética** de un cuerpo de masa $m$ con velocidad $v$ es $K = \tfrac{1}{2}\,m\,v^2$. La **energía potencial gravitatoria** cerca de la superficie, a una altura $h$ sobre un nivel de referencia, es $U = m\,g\,h$. Su unidad es el **julio**: $1\ \text{J} = 1\ \text{N}\cdot\text{m} = 1\ \text{kg}\cdot\text{m}^2/\text{s}^2$. Aparecen términos cuadráticos y raíces, y conviene saber despejar.

De $\tfrac{1}{2}\,m\,v^2 = m\,g\,h$ la masa se cancela, y sale $v = \sqrt{2\,g\,h}$: una piedra que cae desde una altura $h$ llega abajo con esa velocidad, sea cual sea su masa.

**Ejercicios**

1. Despeja $v$ de $K = \tfrac{1}{2}\,m\,v^2$ y calcula la velocidad de un cuerpo de 2 kg con 100 J de energía cinética.
2. Una piedra cae desde 5 m. ¿A qué velocidad llega al suelo? (Usa $g = 9{,}81$ m/s².)
3. ¿Cuánta energía potencial gana una masa de 3 kg al subir 4 m?
4. Si una piedra duplica la altura desde la que cae, ¿por qué factor se multiplica su velocidad al llegar al suelo?

<details>
<summary>Soluciones</summary>

1. $v = \sqrt{2K/m} = \sqrt{200/2} =$ **10 m/s**.
2. $v = \sqrt{2 \cdot 9{,}81 \cdot 5} \approx$ **9,9 m/s**.
3. $U = 3 \cdot 9{,}81 \cdot 4 \approx$ **118 J**.
4. $v \propto \sqrt{h}$, luego se multiplica por **$\sqrt{2} \approx 1{,}41$**.

</details>

### Sesión 2 · Matemáticas: repaso de la fase (40-45 min)

Una colección de problemas que combinan lo visto en las semanas 2 a 11. Resuélvelos sin mirar las páginas anteriores, y si te bloqueas, vuelve a la semana indicada.

1. (Semana 2) Un edificio de 12 m de ancho se ve desde 3 km. ¿Qué ángulo abarca, en grados?
2. (Semana 3) Pasa una ascensión recta de 14 h 16 min a grados.
3. (Semana 5) ¿Qué elongación y qué fracción iluminada tiene la Luna con 22,15 días de edad?
4. (Semana 6) Una vara de 1,00 m proyecta una sombra de 0,50 m. ¿Qué ángulo forman los rayos con la vertical?
5. (Semana 7) Una escalera de 4 m se apoya formando 70° con el suelo. ¿A qué altura llega?
6. (Semana 8) Un coche va a 90 km/h. ¿Cuánto tarda en recorrer 150 km?
7. (Semana 9) ¿Qué módulo tiene el vector $(6, 8)$? Una fuerza de 20 N actúa sobre un cuerpo de 4 kg: ¿qué aceleración le da?
8. (Semana 10) Deriva $s(t) = 2t^3$ y calcula la velocidad en $t = 2$.
9. (Semana 11) Integra esa velocidad entre $t = 0$ y $t = 2$ y comprueba que recuperas la distancia recorrida.

<details>
<summary>Soluciones</summary>

1. $\theta \approx 12/3000 = 0{,}004$ rad $\approx$ **0,23°** (unos 14′).
2. $(14 + 16/60) \cdot 15 =$ **214,0°**.
3. $\varepsilon = 360 \cdot 22{,}15/29{,}53 =$ **270°** y $k = (1 - \cos 270^\circ)/2 =$ **0,5** (cuarto menguante).
4. $\arctan 0{,}5 \approx$ **26,6°**.
5. $4 \sin 70^\circ \approx$ **3,76 m**.
6. $150/90 \approx$ **1,67 h**, es decir, 1 h 40 min.
7. $\sqrt{36 + 64} =$ **10**, y $a = F/m = 20/4 =$ **5 m/s²**.
8. $v = s' = 6t^2$, luego $v(2) =$ **24**.
9. $\int_0^2 6t^2\,dt = 2t^3\big|_0^2 =$ **16** $= s(2) - s(0)$.

</details>

### Sesión 3 · Física: conservación de la energía (30-40 min)

El **trabajo** de una fuerza (semana 11) es la energía que transfiere: $W = \int F\,dx$. El **teorema del trabajo y la energía** dice que el trabajo neto sobre un cuerpo es igual al cambio de su energía cinética: $W = \Delta K$. Si la fuerza es **conservativa** (como la gravedad), el trabajo que realiza se puede guardar como **energía potencial** $U$, y la suma $E = K + U$ no cambia mientras solo actúen fuerzas conservativas. Es la **conservación de la energía mecánica**.

**Aplicación al péndulo.** En el punto más alto, el péndulo está parado ($K = 0$) y tiene máxima energía potencial. Al bajar, la potencial se convierte en cinética, y abajo la velocidad es máxima. Para uno de 1 m soltado desde 30°, $h = L(1 - \cos 30^\circ) \approx 0{,}134$ m, y abajo $v = \sqrt{2 g h} \approx 1{,}62$ m/s. Hemos resuelto el problema sin resolver la ecuación del movimiento: eso es lo que da poder a las leyes de conservación.

**Si hay rozamiento.** Si actúan fuerzas no conservativas, la energía mecánica disminuye, pero la **energía total** se conserva: lo que falta se ha convertido en calor. Es el primer principio de la termodinámica.

**Qué hacer**

1. Explica con tus palabras por qué la energía potencial de una piedra es relativa (depende del nivel que elijas como cero) y la diferencia entre dos alturas no.
2. Piensa en una órbita: ¿cuándo es máxima la energía cinética de un planeta? ¿Y la potencial? Lo verás en la fase 2.

### Sesión 4 · Astronomía y observación (30-45 min)

**Tu primer mapa del cielo de la temporada.** Es la síntesis de lo que has observado en las 12 semanas. Haz un mapa de una zona del cielo de esta época del año, a una hora concreta, con:

1. El horizonte, los puntos cardinales y la altura de la Polar (semana 3).
2. Las constelaciones y las estrellas brillantes que identifiques, con una escala calibrada con tu mano (semana 2).
3. Las ascensiones rectas y declinaciones aproximadas de tres estrellas, contrastadas con Stellarium (semana 3).
4. La posición de la Luna (semana 5) y de un planeta si hay alguno visible (semana 9).
5. La fecha, la hora y tu latitud.

Puedes dibujarlo a mano o imprimir una captura de Stellarium y anotarla. Guárdalo: dentro de unos meses te servirá para comprobar cuánto ha girado el cielo.

**Un balance.** Escribe una lista de las cinco cosas que has medido o calculado estas semanas y con qué precisión. Es la mejor forma de saber qué te falta pulir antes de pasar a la fase 2.

### Sesión 5 · Proyecto en Python (30-45 min)

El cuaderno de la semana 12:

- calcula la velocidad de una piedra que cae por conservación de la energía,
- simula un péndulo con tres métodos (Euler explícito, Euler-Cromer y Verlet) y mide cuánto cambia la energía de cada uno,
- comprueba que el periodo depende de la amplitud para oscilaciones grandes.

[Abrir el cuaderno en Colab](https://colab.research.google.com/github/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-12.ipynb) · [Ver el cuaderno en GitHub](https://github.com/alabcar/hola-universo/blob/main/cuadernos/fase-1/semana-12.ipynb)

El resultado importante es que Euler explícito multiplica la energía por más de cinco en 20 segundos, mientras que Euler-Cromer y Verlet la conservan. En la fase 2, cuando simules la órbita de un planeta, elegirás el método con ese criterio.

## Qué has aprendido

- **La respuesta.** En un sistema donde solo actúan fuerzas conservativas, la suma de energía cinética y potencial no cambia. Eso permite calcular velocidades sin conocer la trayectoria.
- **La causa.** El trabajo de una fuerza conservativa depende solo de los puntos inicial y final, y por eso se puede guardar como energía potencial.
- **Las herramientas.** Despeje de fórmulas con raíces, energía cinética y potencial, y la comprobación de un método numérico mediante la conservación de la energía.

## Recursos

Los recursos marcados con **(sin verificar)** son enlaces que no he podido abrir desde mi entorno. Comprueba que funcionan antes de fiarte.

1. [8.3 Conservación de la energía, *Física universitaria* vol. 1 (OpenStax)](https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/8-3-conservacion-de-la-energia). Español, nivel universitario; incluye el ejemplo del péndulo simple (ejemplo 8.7). Verificado el 31 de octubre de 2026.
2. [Stellarium Web](https://stellarium-web.org/) y [Stellarium de escritorio](https://stellarium.org/). **(Sin verificar)**.
3. [Google Colab](https://colab.research.google.com/). **(Sin verificar)**.

## Imágenes y créditos

Esta semana no incluye imágenes de terceros.
