"""Copia el dataset del agente de inspección dentro de index.html.

El configurador es una página autocontenida: lleva los datos embebidos como
JSON compacto en el bloque <script id="datos-inspeccion">. Las columnas de
texto (estado y particion) se guardan como índices de su lista de categorías
y los valores vacíos como null.

Uso: python embeber_datos.py   (lee datos/inspeccion_sensores.csv y actualiza index.html)
"""
import json
import math
from pathlib import Path

import pandas as pd

from generar_datos import ESTADOS

CATEGORIAS = {"estado": ESTADOS, "particion": ["entrenamiento", "validacion", "prueba"]}
INICIO = '<script type="application/json" id="datos-inspeccion">'
FIN = "</script>"


def valor(v):
    if isinstance(v, float) and math.isnan(v):
        return None
    if isinstance(v, float) and v.is_integer():
        return int(v)
    return v


def a_json(df):
    columnas = {}
    for columna in df.columns:
        if columna in CATEGORIAS:
            columnas[columna] = [CATEGORIAS[columna].index(x) for x in df[columna]]
        else:
            columnas[columna] = [valor(x) for x in df[columna].tolist()]
    return json.dumps({"categorias": CATEGORIAS, "columnas": columnas}, separators=(",", ":"), ensure_ascii=False)


if __name__ == "__main__":
    carpeta = Path(__file__).parent
    texto = a_json(pd.read_csv(carpeta / "datos" / "inspeccion_sensores.csv"))
    html = carpeta / "index.html"
    contenido = html.read_text(encoding="utf-8")
    inicio = contenido.index(INICIO) + len(INICIO)
    fin = contenido.index(FIN, inicio)
    html.write_text(contenido[:inicio] + texto + contenido[fin:], encoding="utf-8")
    print(f"Embebido en {html} ({len(texto.encode()) / 1024:.1f} KB)")
