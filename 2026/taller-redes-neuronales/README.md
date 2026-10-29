# Taller de redes neuronales feed-forward

Configurador interactivo para el taller de apoyo del 03/11 sobre redes feed-forward.

- `index.html`: configurador de un perceptrón multicapa. Se avanza pantalla por pantalla y, en cada una, se toma una decisión de diseño: la vista previa de la red y la cantidad de parámetros entrenables se actualizan con cada elección.
- `generar_datos.py`: generador del dataset sintético de lecturas de sensores de un centro de datos.
- `embeber_datos.py`: copia el CSV dentro de `index.html`, para que la página funcione sin servidor.
- `datos/inspeccion_sensores.csv`: 1500 lecturas de sensores generadas con `generar_datos.py`.

## Versión para usar

El configurador se abre directamente desde GitHub Pages:

- [`index.html`](https://jumafernandez.github.io/machine-learning-unlu/2026/taller-redes-neuronales/)

También funciona al abrir el archivo local en el navegador. Es una página autocontenida: el dataset va embebido y el entrenamiento corre en el navegador con TensorFlow.js 4.22.0, que se descarga de jsdelivr. Sin conexión se pueden recorrer las decisiones y ver los parámetros, pero no entrenar.

## Recorrido

Las ocho pantallas siguen la red capa por capa:

1. **Datos y tarea**: muestra del dataset, distribuciones por clase y partición; elección de la tarea (clasificación binaria, clasificación multiclase, regresión o clustering).
2. **Capa de entrada**: variables de entrada y normalización z-score, con el rango de cada variable antes y después de normalizar.
3. **Capas ocultas**: de 0 a 3 capas, con neuronas y función de activación.
4. **Capa de salida**: neuronas y función de activación de salida (k en clustering).
5. **Función de pérdida**: BCE, CCE, MSE, MAE o MSE contra centroides, cada una con su curva, y la métrica que se reporta.
6. **Regularización**: dropout por capa, L2 y early stopping.
7. **Entrenamiento**: optimizador, learning rate, épocas y batch; curvas en vivo, resultado en prueba y comparación de hasta 4 entrenamientos.
8. **Resumen del modelo**: decisiones, `model.summary()`, cálculo por capa y código Keras listo para Colab.

"Siguiente" se bloquea ante un error y deja seguir ante un aviso. Cada error y cada aviso explica por qué, en diálogo con las clases C5 (*Perceptrón y MLP*) y C6 (*Entrenamiento de redes neuronales*) y con la notebook N02 (*FFNN: Guía paso a paso*).

## Modos

- **Configuración**: solo las decisiones y los avisos; la explicación de cada aviso queda plegada en "¿Por qué?".
- **Estudio**: cada pantalla abre un recuadro con el concepto que se aplica (neurona y sesgo, activación, función de pérdida, ciclo de entrenamiento, sobreajuste), con su referencia a C5, C6 o N02, y las explicaciones quedan abiertas.

El modo se cambia arriba a la derecha. Para compartir un enlace que abra directamente en modo Estudio:

- [`index.html?modo=estudio`](https://jumafernandez.github.io/machine-learning-unlu/2026/taller-redes-neuronales/?modo=estudio)

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

El código Keras del resumen del modelo lee el CSV publicado en GitHub, así que se ejecuta en Colab sin subir archivos. En el configurador, el dataset es un objeto con columnas, tareas y partición, separado de la interfaz, para poder sumar más adelante un importador de CSV.
