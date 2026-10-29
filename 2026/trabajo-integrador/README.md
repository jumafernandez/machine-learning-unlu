# Trabajo práctico integrador · Aprendizaje Automático

Materiales de la asignatura **11283 - Aprendizaje Automático**, Universidad Nacional de Luján, edición 2026.

El trabajo propone desarrollar una prueba de concepto de IA para una situación real, con datos reales y evidencia de funcionamiento. La entrega consiste en un repositorio de GitHub o una plataforma equivalente que contenga la solución, un README y un informe en PDF.

## Materiales

| Documento | PDF para leer | Fuente editable |
| --- | --- | --- |
| Consigna y orientaciones | [Consigna](pdf/consigna.pdf) | [consigna.tex](consigna.tex) |
| Propuesta breve, opcional | [Plantilla de propuesta](pdf/propuesta.pdf) | [propuesta.tex](propuesta.tex) |
| Informe que acompaña al proyecto | [Plantilla de informe](pdf/informe.pdf) | [informe.tex](informe.tex) |

El informe es parte obligatoria de la entrega y debe estar enlazado desde el README. El uso de las plantillas LaTeX es opcional: puede prepararse con otro editor y exportarse a PDF. No se exige un artículo científico, una aplicación desplegada ni un formato exclusivo de notebook.

## Instancias de entrega

- **Propuesta opcional:** hasta 200 palabras para recibir orientación. Sin una fecha de entrega obligatoria. No es requisito para presentar el trabajo final.
- **Entrega final obligatoria:** enlace al repositorio en la actividad del campus, hasta el **2 de diciembre de 2026, 23:59 h** (Argentina).

En la propuesta se presentan el problema real, la fuente de datos, el enfoque previsto y el resultado esperado. El repositorio final debe explicar el problema, los datos, el funcionamiento, la ejecución, los resultados, las limitaciones y cómo se imagina su uso en la situación real.

El informe incluye una **declaración de uso de IA**: herramientas o modelos utilizados como asistencia, tareas, aportes incorporados y verificación realizada. Si no se utilizó IA como apoyo, también debe indicarse. La declaración no reemplaza la responsabilidad de los autores ni la descripción metodológica de los modelos que integran la solución.

## Editar en Overleaf

Los paquetes [propuesta-overleaf.zip](distribucion/propuesta-overleaf.zip) e [informe-overleaf.zip](distribucion/informe-overleaf.zip) contienen un `main.tex` y el estilo común; pueden subirse como un proyecto nuevo y compilarse con **pdfLaTeX**. Reemplazá los campos y retirá las orientaciones antes de entregar.

Para leer los documentos alcanza con abrir los PDF. No es necesario instalar LaTeX.

## Compilar localmente

Requiere una distribución TeX con `latexmk`, pdfLaTeX y los paquetes declarados en `estilo.tex` (incluidos en TeX Live/MacTeX completos).

```sh
make
```

Genera los PDF en `pdf/` y los ZIP para Overleaf en `distribucion/`. Los archivos auxiliares se guardan en `build/` y están excluidos de Git. Los PDF, ZIP y fuentes sí se versionan, para facilitar la lectura y reutilización.

## Edición de los contenidos

- `consigna.tex`: consigna, líneas de desarrollo, evaluación y entrega.
- `propuesta.tex`: adaptación de la propuesta del seminario, con límite total de 200 palabras.
- `informe.tex`: estructura guiada para documentar un proyecto, adaptada al alcance de esta asignatura.
- `estilo.tex`: tipografía, colores, márgenes, encabezados y espaciado comunes.
- `campus/consigna.html`: versión web de la consigna, con el formato del aula y enlaces a las actividades de entrega.
- `campus/entrega.html`: descripción de la entrega final, con orientaciones para el repositorio y el uso opcional de la plantilla LaTeX. En el campus se adjunta `distribucion/informe-overleaf.zip` a la actividad.

## Procedencia

Las fuentes de referencia son las plantillas publicadas en el aula **11089 - Sistemas Inteligentes**, en el bloque **Trabajo Final del Seminario**, correspondientes al Seminario Agentes Inteligentes y LLM:

- [ZIP de la propuesta](https://platdig.unlu.edu.ar/prg_archivo.cgi?wAccion=ver_archivo&id_archivo=8871822&id_curso=10419&id_unidad=73960).
- [ZIP del short paper](https://platdig.unlu.edu.ar/prg_archivo.cgi?wAccion=ver_archivo&id_archivo=8881541&id_curso=10419&id_unidad=73960).

Se mantiene la articulación entre problema, metodología, implementación y evidencia. Se adapta el contenido a las técnicas del curso, se incorpora la procedencia de datos reales y la reflexión sobre el uso, y se simplifica la exigencia documental. El estilo se concentra en un archivo compartido para mantener homogéneos los documentos.

La plantilla del short paper original depende de la clase `llncs`, ausente en su ZIP. Esta adaptación utiliza `article` y paquetes estándar, por lo que no requiere obtener esa clase por separado.
