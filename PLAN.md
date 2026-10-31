# Hola, universo · Plan de trabajo del proyecto

Este archivo es la memoria del proyecto. Cualquier sesión nueva debe leerlo antes de tocar nada.

## Qué es

Un plan de formación como aficionado en astronomía, física y matemáticas, publicado como web pública en GitHub Pages. El objetivo es aprender y disfrutar, no sacar ningún título. La persona parte de una ingeniería informática; las matemáticas y la física las tiene olvidadas desde hace más de 20 años, así que las matemáticas empiezan desde cero.

## Decisiones tomadas

- **Método:** cada semana empieza con una pregunta del cielo, y se estudia solo la matemática y la física necesarias para responderla.
- **Ritmo:** 4-5 sesiones por semana de 30-45 min: 2 de matemáticas, 1 de física, 1 de astronomía u observación, 1 de proyecto con Python en el ordenador.
- **Estructura:** 4 fases de unos 3 meses (12 semanas cada una), 48 semanas en total. Detalle en `TEMARIO.md`.
  1. Principios básicos de astronomía
  2. Órbitas
  3. La luz
  4. El universo grande
- **Idioma:** castellano. Los recursos en inglés se marcan como tales.
- **Herramienta:** Astro Starlight, desplegado en GitHub Pages con GitHub Actions. Sin casillas de progreso ni backend.
- **Sin Raspberry Pi ni cámara:** se descartó. Los proyectos son solo Python en el ordenador. La observación es a ojo, con Stellarium y, opcionalmente, prismáticos.
- **Privacidad:** la web es pública. No se escribe nada personal: ni lugares concretos de residencia u observación, ni nombres de personas, ni datos de trabajo. Se habla de "cielo urbano luminoso" o "cielo rural oscuro".
- **Autoría de commits:** con el correo noreply de GitHub, nunca con el correo real.

## Reglas de contenido

1. **Enlaces:** antes de poner un enlace se comprueba que existe y que es lo que se dice. Si no se puede verificar, se marca con la etiqueta `sin verificar` para que se revise a mano. Cada enlace lleva una nota de para qué sirve, el idioma y la duración aproximada.
2. **Material ajeno:** no se copia, se enlaza. Nada de reproducir textos, vídeos o ejercicios de otras personas.
3. **Imágenes:** solo de NASA/ESA u otras fuentes libres, con la fuente y el enlace citados en la propia página. Se comprueba la licencia de cada imagen; las condiciones de ESA pueden variar de una imagen a otra.
4. **Datos y cifras:** se verifican con fuente primaria. Si una cifra no se ha podido comprobar, se dice.
5. **Tono:** agradable pero riguroso. Sin paternalismo ni ingenuidad: se trata a la persona lectora como a un adulto capaz. Se explica la intuición y también la formulación correcta, sin esconder la dificultad ni simplificar hasta decir algo falso. Se escribe siempre "matemáticas", nunca "mates".

## Plantilla de cada semana

1. **La pregunta del cielo**: un párrafo que la plantea y explica por qué merece la pena.
2. **Las sesiones** (cada una dice qué hacer en 30-45 min y qué recurso usar):
   - Matemáticas 1
   - Matemáticas 2
   - Física
   - Astronomía u observación
   - Proyecto (Python)
3. **Qué has aprendido**: la respuesta a la pregunta en pocas líneas y las ideas que la sostienen.
4. **Recursos comentados**.
5. **Imágenes y créditos**.

## Flujo de trabajo con git

- `main` es lo publicado.
- Cada fase se escribe en su rama (`fase-1`, `fase-2`, ...) con un commit por semana.
- La revisión se hace en un pull request por fase. Las correcciones llegan como commits nuevos.
- Mensajes de commit: `Fase 1 · S03: <título corto>`.

## Estado

| Hito | Estado |
|---|---|
| Plan y temario (este archivo y `TEMARIO.md`) | aprobado |
| Esqueleto de la web (Starlight + despliegue) | publicado |
| Fase 1 · Principios básicos de astronomía | escrita (semanas 1 a 12), pendiente de revisión |
| Fase 2 · Órbitas | pendiente |
| Fase 3 · La luz | pendiente |
| Fase 4 · El universo grande | pendiente |
