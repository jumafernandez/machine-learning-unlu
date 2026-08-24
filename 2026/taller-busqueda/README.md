# Taller de agentes y problemas de búsqueda

Materiales Quarto para los encuentros del 27/08 y 03/09.

- `01-demostracion.qmd`: demostración con AIPython (Poole y Mackworth) y aima-python (Russell y Norvig) sobre un agente de reparto.
- `01-desafio-estudiantes.qmd`: actividad de formulación y elección de estrategia para un agente de inspección.
- `02-heuristicas-y-busqueda-informada.qmd`: continuidad del mismo problema con heurísticas y A*.
- `datos/`: grafos dirigidos en formato CSV.

## Versiones para lectura

Los materiales también se incluyen en HTML, ya ejecutados y listos para consultar desde GitHub Pages:

- [`01-demostracion.html`](01-demostracion.html)
- [`01-desafio-estudiantes.html`](01-desafio-estudiantes.html)
- [`02-heuristicas-y-busqueda-informada.html`](02-heuristicas-y-busqueda-informada.html)

## Preparación para edición

Sólo quien edite y vuelva a renderizar los materiales necesita Quarto con un entorno Python que incluya:

```bash
pip install pandas networkx matplotlib
```

Para renderizar un material:

```bash
quarto render 01-demostracion.qmd
```

Los HTML publicados son autocontenidos: estudiantes y docentes pueden abrirlos sin instalar Quarto ni dependencias de Python. Los archivos están pensados para abrirse también como notebooks/celdas de Quarto durante la clase. `NetworkX` se utiliza únicamente para visualizar y explorar los entornos; las búsquedas se ejecutan con las implementaciones que acompañan los libros de Poole/Mackworth y Russell/Norvig. El foco pedagógico está en formular la tarea del agente, elegir un criterio de calidad y analizar la solución.
