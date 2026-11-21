"""Genera src/content/docs/glosario.md a partir de los recuadros
«De dónde viene la palabra» de todas las semanas.

Uso, desde la raíz del repositorio:

    python3 scripts/generar_glosario.py

Cada recuadro se divide en frases. Una frase con términos en negrita
empieza una entrada nueva; las frases siguientes sin negritas se añaden
a la misma entrada. Los términos secundarios de una entrada aparecen
también en el índice alfabético, con una remisión al principal.
"""

import glob
import os
import re
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(RAIZ, "src", "content", "docs")
SALIDA = os.path.join(DOCS, "glosario.md")

RECUADRO = re.compile(r":::note\[De dónde viene la palabra\]\n(.*?)\n:::", re.S)
NEGRITA = re.compile(r"\*\*([^*]+)\*\*")
# Corta tras punto (o cierre de comillas) seguido de espacio y mayúscula, negrita o cursiva.
FRASE = re.compile(r"(?<=[.!?»”])\s+(?=[A-ZÁÉÍÓÚÑ¿«*])")


def clave(texto):
    """Clave de orden alfabético sin tildes ni mayúsculas."""
    t = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn" and (c.isalnum() or c == " "))


def bonito(termino):
    return termino[:1].upper() + termino[1:]


def entradas():
    resultado = []
    for ruta in sorted(glob.glob(os.path.join(DOCS, "fase-*", "semana-*.md"))):
        fase = os.path.basename(os.path.dirname(ruta))
        n = int(re.search(r"semana-(\d+)", ruta).group(1))
        texto = open(ruta, encoding="utf-8").read()
        titulo = re.search(r'^title:\s*"?(.*?)"?\s*$', texto, re.M).group(1)
        enlace = f"../{fase}/semana-{n:02d}/"
        for recuadro in RECUADRO.findall(texto):
            actual = None
            for frase in FRASE.split(" ".join(recuadro.split())):
                terminos = NEGRITA.findall(frase)
                if terminos or actual is None:
                    actual = {"terminos": [], "texto": [], "semana": n,
                              "enlace": enlace, "titulo": titulo}
                    resultado.append(actual)
                for t in terminos:
                    if t.lower() not in [x.lower() for x in actual["terminos"]]:
                        actual["terminos"].append(t)
                actual["texto"].append(frase)
    return [e for e in resultado if e["terminos"]]


def generar():
    lista = entradas()
    indice = {}
    for i, e in enumerate(lista):
        e["id"] = f"e{i}"
        principal = e["terminos"][0]
        for t in e["terminos"]:
            indice.setdefault(clave(t), []).append((t, e, t == principal))

    letras = {}
    for k in sorted(indice):
        letras.setdefault(k[:1].upper(), []).append(k)

    lineas = [
        "---",
        "title: Glosario de etimologías",
        "description: El origen de las palabras de la astronomía, la física y las matemáticas que aparecen en el plan, con un enlace a la semana donde se explican.",
        "---",
        "",
        "Este glosario reúne, en orden alfabético, todos los recuadros «De dónde viene la palabra» de las 48 semanas. Cada entrada enlaza con la semana donde aparece, para que puedas volver a la explicación completa. Cuando un recuadro explica varias palabras juntas, la entrada está bajo la primera, y las demás remiten a ella.",
        "",
        "Usa el buscador de la web (arriba) o salta a una letra: "
        + " · ".join(f"[{l}](#{l.lower()})" for l in letras),
        "",
    ]
    for letra, claves in letras.items():
        lineas += [f"## {letra}", ""]
        for k in claves:
            for t, e, es_principal in indice[k]:
                ref = f"[semana {e['semana']}]({e['enlace']})"
                if es_principal:
                    otros = [x for x in e["terminos"][1:]]
                    cabecera = f"**{bonito(t)}**"
                    if otros:
                        cabecera += " (con " + ", ".join(otros) + ")"
                    cuerpo = " ".join(e["texto"])
                    lineas += [f"{cabecera} · {ref}", "", f"> {cuerpo}", ""]
                else:
                    principal = bonito(e["terminos"][0])
                    lineas += [f"**{bonito(t)}** → véase **{principal}** ({ref}).", ""]
    texto = "\n".join(lineas).rstrip() + "\n"
    open(SALIDA, "w", encoding="utf-8").write(texto)
    return len(lista), len(indice)


if __name__ == "__main__":
    entradas_, terminos = generar()
    print(f"{entradas_} entradas y {terminos} términos en {os.path.relpath(SALIDA, RAIZ)}")
