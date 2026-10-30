"""Genera el dataset sintético del agente de inspección.

Cada fila es una lectura de los sensores de un rack del centro de datos.
El estado oculto del equipo (normal o uno de cuatro tipos de incidente)
determina la distribución de los sensores, la alerta y el tiempo de
reparación. Una parte de las etiquetas se corrompe a propósito para que
exista error irreducible y pueda observarse el sobreajuste.

Uso: python generar_datos.py   (escribe datos/inspeccion_sensores.csv)
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEMILLA = 2026
N = 1500
ESTADOS = ["normal", "termico", "electrico", "almacenamiento", "red"]
PROPORCIONES = [0.40, 0.15, 0.15, 0.15, 0.15]
RUIDO_ETIQUETAS = 0.06

# Media y desvío de cada sensor según el estado del equipo.
SENSORES = {
    #                    normal        termico       electrico     almacenam.    red
    "temperatura":     [(24, 2.2),   (31, 3.0),    (26.5, 2.6),  (25, 2.3),    (24.5, 2.2)],
    "humedad":         [(45, 7),     (39, 7),      (48, 7),      (46, 7),      (45, 7)],
    "carga_cpu":       [(45, 13),    (66, 13),     (50, 15),     (55, 14),     (38, 13)],
    "ventiladores_rpm": [(2500, 260), (3350, 380),  (2350, 400),  (2560, 270),  (2470, 260)],
    "consumo_w":       [(420, 42),   (500, 50),    (560, 65),    (440, 45),    (415, 42)],
    "latencia_ms":     [(12, 4),     (15, 5),      (17, 6),      (22, 8),      (42, 14)],
    "vibracion":       [(1.2, 0.3),  (1.5, 0.4),   (1.9, 0.55),  (1.8, 0.5),   (1.25, 0.3)],
}
ERRORES_DISCO = [0.6, 1.0, 1.5, 5.0, 0.8]  # tasa de Poisson por hora
BASE_REPARACION = {"termico": 45, "electrico": 90, "almacenamiento": 120, "red": 30}


def generar(semilla=SEMILLA, n=N):
    rng = np.random.default_rng(semilla)
    estado = rng.choice(len(ESTADOS), size=n, p=PROPORCIONES)
    datos = {}
    for sensor, parametros in SENSORES.items():
        medias = np.array([m for m, _ in parametros])[estado]
        desvios = np.array([s for _, s in parametros])[estado]
        datos[sensor] = rng.normal(medias, desvios)
    datos["errores_disco"] = rng.poisson(np.array(ERRORES_DISCO)[estado]).astype(float)

    df = pd.DataFrame(datos)[[
        "temperatura", "humedad", "carga_cpu", "ventiladores_rpm",
        "consumo_w", "errores_disco", "latencia_ms", "vibracion",
    ]]
    df["humedad"] = df["humedad"].clip(15, 85)
    df["carga_cpu"] = df["carga_cpu"].clip(2, 100)
    df["latencia_ms"] = df["latencia_ms"].clip(1, None)
    df["vibracion"] = df["vibracion"].clip(0.1, None)

    # Tiempo de reparación: base por tipo + severidad observable + ruido.
    nombres = np.array(ESTADOS)[estado]
    severidad = np.select(
        [nombres == "termico", nombres == "electrico", nombres == "almacenamiento", nombres == "red"],
        [
            4.0 * (df["temperatura"] - 28),
            0.35 * (df["consumo_w"] - 520),
            7.0 * (df["errores_disco"] - 4),
            0.9 * (df["latencia_ms"] - 35),
        ],
        default=0.0,
    )
    base = np.array([BASE_REPARACION.get(e, 0) for e in nombres])
    tiempo = base + severidad + rng.normal(0, 12, n)
    tiempo = np.where(nombres == "normal", np.nan, np.clip(tiempo, 5, None))

    # Etiquetas observadas: una fracción se registra mal (error irreducible).
    observado = estado.copy()
    corruptas = rng.random(n) < RUIDO_ETIQUETAS
    observado[corruptas] = rng.integers(0, len(ESTADOS), corruptas.sum())

    df["estado"] = np.array(ESTADOS)[observado]
    df["alerta_real"] = (observado != 0).astype(int)
    df["tiempo_reparacion_min"] = np.where(observado == 0, np.nan, tiempo)
    # Si una lectura normal se registró como incidente, el tiempo es el de su tipo base.
    falta = (observado != 0) & np.isnan(df["tiempo_reparacion_min"].to_numpy())
    base_obs = np.array([BASE_REPARACION.get(e, 0) for e in np.array(ESTADOS)[observado]])
    df.loc[falta, "tiempo_reparacion_min"] = np.clip(base_obs[falta] + rng.normal(0, 12, falta.sum()), 5, None)

    orden = rng.permutation(n)
    df = df.iloc[orden].reset_index(drop=True)

    redondeo = {"temperatura": 1, "humedad": 1, "carga_cpu": 1, "ventiladores_rpm": 0, "consumo_w": 0,
                "errores_disco": 0, "latencia_ms": 1, "vibracion": 2, "tiempo_reparacion_min": 0}
    for columna, decimales in redondeo.items():
        df[columna] = df[columna].round(decimales)
    for columna in ["ventiladores_rpm", "consumo_w", "errores_disco"]:
        df[columna] = df[columna].astype(int)
    return df


if __name__ == "__main__":
    salida = Path(__file__).with_name("datos") / "inspeccion_sensores.csv"
    salida.parent.mkdir(exist_ok=True)
    generar().to_csv(salida, index=False)
    print("Escrito", salida)
