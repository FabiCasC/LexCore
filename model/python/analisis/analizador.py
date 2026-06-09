from datetime import datetime
from typing import List

import numpy as np
import pandas as pd


def calcular_perfil_estadistico(clausulas: List[dict]) -> dict:
    if not clausulas:
        return {
            "total_clausulas": 0,
            "clausulas_riesgo": 0,
            "porcentaje_riesgo": 0.0,
            "riesgo_promedio": 0.0,
            "riesgo_desviacion": 0.0,
            "riesgo_maximo": 0,
            "longitud_promedio": 0.0,
            "tipos_clausula": {},
            "severidades": {},
            "fecha_calculo": datetime.now().isoformat(),
        }

    df = pd.DataFrame(clausulas)

    tipos = df["tipo"].value_counts().to_dict() if "tipo" in df.columns else {}
    severidades = df["severidad"].value_counts().to_dict() if "severidad" in df.columns else {}

    pesos = np.array([c.get("peso_riesgo", 1) for c in clausulas])
    riesgo_promedio = float(np.mean(pesos))
    riesgo_desviacion = float(np.std(pesos))
    riesgo_maximo = int(np.max(pesos))

    longitudes = np.array([len(c.get("texto", "")) for c in clausulas])
    longitud_promedio = float(np.mean(longitudes))

    clausulas_riesgo = sum(1 for c in clausulas if c.get("es_riesgosa", False))
    total = len(clausulas)
    porcentaje_riesgo = round((clausulas_riesgo / total) * 100, 2) if total > 0 else 0.0

    return {
        "total_clausulas": total,
        "clausulas_riesgo": clausulas_riesgo,
        "porcentaje_riesgo": porcentaje_riesgo,
        "riesgo_promedio": round(riesgo_promedio, 2),
        "riesgo_desviacion": round(riesgo_desviacion, 2),
        "riesgo_maximo": riesgo_maximo,
        "longitud_promedio": round(longitud_promedio, 2),
        "tipos_clausula": tipos,
        "severidades": severidades,
        "fecha_calculo": datetime.now().isoformat(),
    }


def generar_dataframe_clausulas(clausulas: List[dict]) -> pd.DataFrame:
    if not clausulas:
        return pd.DataFrame()

    df = pd.DataFrame(clausulas)

    columnas_rename = {
        "id": "ID",
        "tipo": "Tipo",
        "texto": "Texto",
        "severidad": "Severidad",
        "es_riesgosa": "¿Es Riesgosa?",
        "peso_riesgo": "Peso de Riesgo",
        "categoria": "Categoría",
        "articulo_referencia": "Artículo de Referencia",
        "recomendacion": "Recomendación",
    }
    df = df.rename(columns={k: v for k, v in columnas_rename.items() if k in df.columns})

    if "¿Es Riesgosa?" in df.columns:
        df["¿Es Riesgosa?"] = df["¿Es Riesgosa?"].map({True: "⚠️ Sí", False: "✅ No"})

    return df


def comparar_con_promedio(estadisticas_actual: dict, historial: List[dict]) -> dict:
    if not historial:
        return {
            "promedio_historico": None,
            "diferencia": None,
            "tendencia": "sin_historial",
        }

    porcentajes = np.array([h.get("porcentaje_riesgo", 0) for h in historial])
    promedio_historico = float(np.mean(porcentajes))
    actual = estadisticas_actual.get("porcentaje_riesgo", 0)
    diferencia = round(actual - promedio_historico, 2)

    if diferencia < -2:
        tendencia = "mejor"
    elif diferencia > 2:
        tendencia = "peor"
    else:
        tendencia = "igual"

    return {
        "promedio_historico": round(promedio_historico, 2),
        "diferencia": diferencia,
        "tendencia": tendencia,
    }
