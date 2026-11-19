#!/usr/bin/env python3
"""Genera profile/README.md a partir de projects.json.

Solo usa la biblioteca estándar. Se ejecuta a mano o desde
.github/workflows/readme.yml. Los repos privados se listan sin enlace.
"""
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ORG = "Takumi-Organization"


def fila(p):
    if p["visibilidad"] == "publico":
        nombre = f"[`{p['nombre']}`](https://github.com/{ORG}/{p['nombre']})"
    else:
        nombre = f"`{p['nombre']}`"
    return f"| {nombre} | {p['descripcion']} | {p['stack']} |"


def generar():
    datos = json.loads((RAIZ / "projects.json").read_text(encoding="utf-8"))
    total = len(datos["proyectos"])
    publicos = sum(1 for p in datos["proyectos"] if p["visibilidad"] == "publico")
    out = []
    out.append('<p align="center">\n  <img src="logo.png" alt="Takumi Organization" width="220">\n</p>\n')
    out.append("# Takumi Organization\n")
    out.append("Software propio, construido con oficio: aplicaciones móviles, herramientas de terminal, "
               "escritorio y aprendizaje automático. Cada proyecto se verifica antes de darse por terminado.\n")
    out.append(f"**{total} proyectos** · {publicos} públicos · {total - publicos} privados\n")
    for area in datos["areas"]:
        ps = [p for p in datos["proyectos"] if p["area"] == area["id"]]
        if not ps:
            continue
        out.append(f"## {area['titulo']}\n")
        out.append(f"{area['descripcion']}\n")
        out.append("| Proyecto | Descripción | Stack |\n|---|---|---|")
        out.extend(fila(p) for p in ps)
        out.append("")
    out.append("## Automatización\n")
    out.append("Este repositorio centraliza lo común a toda la organización:\n")
    out.append("- **Plantillas de workflow** (`workflow-templates/`): CI para Rust, Node, Python, Java con Maven y Android con Gradle, "
               "más un análisis de secretos. Aparecen en la pestaña *Actions → New workflow* de cada repo.")
    out.append("- **Este README** se regenera solo al cambiar `projects.json` (`readme.yml`).")
    out.append("- **Validación** (`validate.yml`): comprueba que el README está al día y que las plantillas son YAML válido.")
    out.append("- **Salud de la comunidad**: política de seguridad, guía de contribución y plantillas de issues y pull requests por defecto.\n")
    out.append("## Convenciones\n")
    out.append("- Ramas por funcionalidad; `main` siempre compila y pasa sus pruebas.")
    out.append("- Mensajes de commit en español, en imperativo y concretos.")
    out.append("- Nunca se versionan secretos, `.env` ni `local.properties`.")
    out.append("- Los proyectos nuevos nacen privados y se publican de forma deliberada.\n")
    return "\n".join(out)


if __name__ == "__main__":
    destino = RAIZ / "profile" / "README.md"
    texto = generar()
    if "--check" in sys.argv:
        actual = destino.read_text(encoding="utf-8") if destino.exists() else ""
        if actual != texto:
            sys.exit("profile/README.md desactualizado: ejecuta scripts/generate_readme.py")
        print("README al día")
    else:
        destino.write_text(texto, encoding="utf-8")
        print(f"README generado ({destino})")
