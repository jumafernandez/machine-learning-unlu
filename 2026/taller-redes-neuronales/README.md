# Taller de redes neuronales feed-forward

Configurador interactivo para el taller de apoyo del 03/11 sobre redes feed-forward.

- `index.html`: configurador de un perceptrón multicapa. Se avanza pantalla por pantalla y, en cada una, se toma una decisión de diseño: la vista previa de la red y la cantidad de parámetros entrenables se actualizan con cada elección. Trabaja con el dataset del taller o con un CSV propio.
- `generar_datos.py`: generador del dataset sintético de lecturas de sensores de un centro de datos.
- `embeber_datos.py`: copia el CSV dentro de `index.html`, para que la página funcione sin servidor.
- `datos/inspeccion_sensores.csv`: 1500 lecturas de sensores generadas con `generar_datos.py`.

## Versión para usar

El configurador se abre directamente desde GitHub Pages:

- [`index.html`](https://jumafernandez.github.io/machine-learning-unlu/2026/taller-redes-neuronales/)

También funciona al abrir el archivo local en el navegador. Es una página autocontenida: el dataset va embebido y el entrenamiento corre en el navegador con TensorFlow.js 4.22.0, que se descarga de jsdelivr. Sin conexión se pueden recorrer las decisiones y ver los parámetros, pero no entrenar.

## Recorrido

Las ocho pantallas siguen la red capa por capa:

1. **Datos y tarea**: se sube un CSV o se cargan los datos de ejemplo. Se ven las primeras filas, como en `df.head()`, se elige la tarea (clasificación binaria, clasificación multiclase, regresión o clustering) y, si es supervisada, la variable objetivo con un clic en su columna. Con otro clic en cada columna se suman o se quitan las entradas. La partición se define con los porcentajes de entrenamiento, validación y prueba y una semilla, 42 por defecto.
2. **Capa de entrada**: la red en grande, con el rango de cada variable entrando a su neurona. Al activar la normalización z-score, las barras se acomodan a la misma escala.
3. **Capas ocultas**: de 0 a 3 capas, con neuronas y función de activación.
4. **Capa de salida**: neuronas y función de activación de salida (k en clustering).
5. **Función de pérdida**: BCE, CCE, MSE, MAE o MSE contra centroides, cada una con su curva, y la métrica que se reporta.
6. **Regularización**: dropout por capa, L2 y early stopping, con un esquema de la paciencia.
7. **Entrenamiento**: optimizador (con su trayectoria sobre un valle de ejemplo), learning rate, épocas y batch. Se puede entrenar, pausar o avanzar de a una época; las curvas se actualizan en vivo y la vista previa muestra el peso de cada conexión. Al final, el resultado en prueba y la comparación de hasta 4 entrenamientos.
8. **Resumen del modelo**: decisiones, `model.summary()`, cálculo por capa y código Keras para copiar o descargar como notebook (`.ipynb`) y abrir en Colab.

"Siguiente" se bloquea ante un error y deja seguir ante un aviso. Cada error y cada aviso explica por qué, en diálogo con las clases C5 (*Perceptrón y MLP*) y C6 (*Entrenamiento de redes neuronales*) y con la notebook N02 (*FFNN: Guía paso a paso*).

## Modos

- **Configuración**: cada pantalla muestra las decisiones, la red y los avisos. Los gráficos secundarios (distribuciones, asociación, trayectoria del optimizador, esquema de paciencia, `model.summary()`) quedan plegados en "Ver …" y la explicación de cada aviso, en "¿Por qué?".
- **Estudio**: cada pantalla abre un recuadro con el concepto que se aplica (neurona y sesgo, activación, función de pérdida, ciclo de entrenamiento, sobreajuste), con su referencia a C5, C6 o N02, y todo lo plegado queda abierto.

El modo se cambia arriba a la derecha. Para compartir un enlace que abra directamente en modo Estudio:

- [`index.html?modo=estudio`](https://jumafernandez.github.io/machine-learning-unlu/2026/taller-redes-neuronales/?modo=estudio)

## Compartir una red

La configuración queda en el enlace, en un formato legible que se puede editar a mano. El botón "Copiar enlace a esta red" lo copia; desde la copia local, copia el de GitHub Pages. Al abrirlo, se aplica la red y se abre en el paso indicado. Por ejemplo, este enlace abre en el paso de entrenamiento una red binaria con una capa oculta de 16 neuronas, dropout y early stopping:

- [`#tarea=binaria&objetivo=alerta_real&ocultas=16:relu:0.2&salida=1:sigmoide&perdida=bce&early=10:restaura&paso=7`](https://jumafernandez.github.io/machine-learning-unlu/2026/taller-redes-neuronales/#tarea=binaria&objetivo=alerta_real&ocultas=16:relu:0.2&salida=1:sigmoide&perdida=bce&early=10:restaura&paso=7)

Lo que el enlace no indica toma el valor por defecto, y lo que no se reconoce se ignora con un aviso. Con un CSV propio, el enlace guarda el nombre del archivo: quien lo abra tiene que subir ese archivo, y entonces se aplica la configuración.

## Datos propios

En la primera pantalla se puede subir un CSV con encabezado, separado por coma, punto y coma o tabulación, y con decimales con punto o con coma. El archivo se procesa en el navegador y no se sube a ningún servidor.

- Las columnas numéricas pueden ser entradas; las de texto solo pueden ser variable objetivo.
- Cada tarea habilita las columnas compatibles como variable objetivo: dos valores para la clasificación binaria, de 3 a 20 para la multiclase y una numérica para la regresión. En clustering, una columna opcional sirve para interpretar los grupos.
- Se recomiendan hasta 20 variables de entrada y 10.000 filas; con más filas, el configurador ofrece entrenar con una muestra al azar. Los máximos son 200 columnas, 200.000 filas y 25 MB.
- La partición se genera al azar con los porcentajes y la semilla elegidos, y el código Keras la reproduce con `train_test_split` con los mismos tamaños.
- Las filas con valores vacíos en las columnas usadas se descartan.

El código generado lee el archivo por su nombre: antes de ejecutarlo en Colab, hay que subirlo al entorno.

## Datos del taller

Cada fila es una lectura de un rack con 8 variables (`temperatura`, `humedad`, `carga_cpu`, `ventiladores_rpm`, `consumo_w`, `errores_disco`, `latencia_ms` y `vibracion`), el `estado` del equipo (normal, termico, electrico, almacenamiento o red), `alerta_real` y `tiempo_reparacion_min` (vacío si el estado es normal). El archivo trae además una columna `particion` que el configurador no usa: la partición se genera con una semilla.

## Preparación para edición

Sólo quien quiera regenerar los datos necesita un entorno Python con:

```bash
pip install numpy pandas
```

Para volver a generar el CSV:

```bash
python generar_datos.py
```

El generador usa una semilla fija, de modo que siempre produce el mismo archivo. `index.html` trae embebida una copia de esos datos en formato JSON compacto. Si se modifica el generador, hay que actualizar también esa copia:

```bash
python embeber_datos.py
```

El script lee `datos/inspeccion_sensores.csv` y reemplaza el contenido del bloque `<script id="datos-inspeccion">` de `index.html`, sin tocar el resto de la página.

El código Keras del resumen del modelo lee el CSV publicado en GitHub, así que se ejecuta en Colab sin subir archivos. En el configurador, el dataset es un objeto con columnas, tareas y partición, separado de la interfaz, para poder sumar más adelante un importador de CSV.
