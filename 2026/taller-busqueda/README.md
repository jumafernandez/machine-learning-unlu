# Taller de agentes y problemas de búsqueda

Materiales Quarto para los encuentros del 27/08 y 03/09.

- `01-demostracion-docente.qmd`: recorrido completo para desarrollar en clase.
- `01-desafio-estudiantes.qmd`: desafío sobre un nuevo problema, con funciones a completar.
- `datos/`: grafos dirigidos en formato CSV.

## Preparación

Se necesita Quarto con un entorno Python que incluya:

```bash
pip install pandas networkx matplotlib
```

Para renderizar un material:

```bash
quarto render 01-demostracion-docente.qmd
```

Los archivos están pensados para abrirse también como notebooks/celdas de Quarto durante la clase. La implementación de los algoritmos se desarrolla de forma explícita: `networkx` se usa para representar y dibujar el grafo, no para resolver la búsqueda.
