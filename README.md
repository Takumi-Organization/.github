# .github

Repositorio general de **Takumi Organization**.

| Ruta | Para qué sirve |
|---|---|
| `profile/README.md` | Portada de la organización (generada, no editar a mano) |
| `projects.json` | Fuente de verdad del listado de proyectos |
| `scripts/generate_readme.py` | Genera la portada desde `projects.json` |
| `workflow-templates/` | Plantillas de CI y análisis de secretos para todos los repos |
| `.github/workflows/` | Automatización de este repo: regenerar README y validar |
| `SECURITY.md`, `CONTRIBUTING.md`, plantillas | Valores por defecto de la organización |

## Añadir un proyecto
1. Añade su entrada a `projects.json`.
2. Haz push a `main`: `readme.yml` regenera la portada.
