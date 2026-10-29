# Taller de redes neuronales feed-forward

Configurador interactivo para el taller de apoyo del 03/11 sobre redes feed-forward.

- `index.html`: configurador de redes neuronales al estilo de los configuradores de autos. Se avanza pantalla por pantalla y, en cada una, se toma una decisión de diseño: la vista previa de la red y su "precio" en parámetros entrenables se actualizan con cada elección.
- `generar_datos.py`: generador del dataset sintético del agente de inspección del centro de datos.
- `embeber_datos.py`: copia el CSV dentro de `index.html`, para que la página funcione sin servidor.
- `datos/inspeccion_sensores.csv`: 1500 lecturas de sensores generadas con `generar_datos.py`.

## Versión para usar

El configurador se abre directamente desde GitHub Pages:

- [`index.html`](https://jumafernandez.github.io/machine-learning-unlu/2026/taller-redes-neuronales/)

También funciona al abrir el archivo local en el navegador. Es una página autocontenida: el dataset va embebido y el entrenamiento corre en el navegador con TensorFlow.js 4.22.0, que se descarga de jsdelivr. Sin conexión se pueden recorrer las decisiones y ver el precio, pero no entrenar.

## Recorrido

El escenario continúa el del taller de búsqueda: el agente de inspección ya llegó al centro de datos y registra los sensores de cada rack. Las ocho pantallas son:

1. **Misión**: detectar alertas reales (clasificación binaria), diagnosticar el estado del equipo (multiclase), estimar el tiempo de reparación (regresión) o descubrir perfiles de comportamiento (clustering).
2. **Entradas**: sensores, normalización z-score y partición en entrenamiento, validación y prueba.
3. **Capas ocultas**: de 0 a 3 capas, con neuronas y activación.
4. **Salida**: neuronas y activación de salida (k en clustering).
5. **Pérdida**: BCE, CCE, MSE, MAE o MSE contra centroides, y la métrica que se reporta.
6. **Regularización**: dropout por capa, L2 y early stopping.
7. **Entrenamiento**: optimizador, learning rate, épocas y batch; curvas en vivo, resultado en prueba y un "garage" para comparar hasta 4 corridas.
8. **Ficha técnica**: resumen de decisiones, summary estilo Keras, cálculo por capa y código Keras listo para Colab.

"Siguiente" se bloquea ante un error y deja seguir ante un aviso. Cada error y cada aviso explica por qué, en diálogo con las clases C5 (*Perceptrón y MLP*) y C6 (*Entrenamiento de redes neuronales*) y con la notebook N02 (*FFNN: Guía paso a paso*).

## Datos

Cada fila es una lectura de un rack con 8 variables (`temperatura`, `humedad`, `carga_cpu`, `ventiladores_rpm`, `consumo_w`, `errores_disco`, `latencia_ms` y `vibracion`), el `estado` del equipo (normal, termico, electrico, almacenamiento o red), `alerta_real`, `tiempo_reparacion_min` (vacío si el estado es normal) y la `particion`: 900 lecturas de entrenamiento, 300 de validación y 300 de prueba. El 6% de las etiquetas se corrompe a propósito para que exista error irreducible y el sobreajuste se vea en las curvas.

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

El código Keras de la ficha técnica lee el CSV publicado en GitHub, así que se ejecuta en Colab sin subir archivos. En el configurador, el dataset es un objeto con columnas, tareas y partición, separado de la interfaz, para poder sumar más adelante un importador de CSV.
