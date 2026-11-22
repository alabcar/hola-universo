# Datos de los cuadernos

## estrellas_hyg.csv

Subconjunto de la base de datos de estrellas **HYG**, versión 4.1, de David Nash (Astronexus), que combina los catálogos Hipparcos, Yale Bright Star y Gliese de estrellas cercanas.

- Fuente original: https://codeberg.org/astronexus/hyg (antes, https://github.com/astronexus/HYG-Database).
- Licencia de la base original: [Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.es). Este subconjunto se distribuye con la misma licencia.

**Qué estrellas contiene** (2773 filas): todas las de la base con índice de color conocido que están a menos de 25 pársecs, todas las más brillantes que la magnitud aparente 4, y el Sol.

**Cambios respecto al original:** se han seleccionado las filas anteriores, se han conservado solo algunas columnas, se han renombrado al español y se han redondeado los decimales.

| Columna | Significado |
|---|---|
| `hip` | número en el catálogo Hipparcos (vacío si no tiene) |
| `nombre` | nombre propio, en inglés, tal como viene en HYG |
| `bayer` | designación de Bayer abreviada (por ejemplo, `Alp` para alfa) |
| `constelacion` | abreviatura de la constelación |
| `dist_pc` | distancia en pársecs |
| `mag` | magnitud aparente visual |
| `absmag` | magnitud absoluta visual |
| `b_v` | índice de color B−V |
| `espectro` | tipo espectral |
| `lum_sol` | luminosidad visual en luminosidades solares, calculada a partir de la magnitud absoluta |
| `x`, `y`, `z` | posición en pársecs, en coordenadas ecuatoriales cartesianas con el Sol en el origen (x hacia el punto Aries, z hacia el polo norte celeste) |

Las distancias de las estrellas lejanas, sobre todo las de más de unos cientos de pársecs, tienen incertidumbres grandes.
