import streamlit as st
import pandas as pd

def mostrar_tabla(clausulas: list[dict]) -> None:
    if not clausulas:
        st.warning("No se encontraron cláusulas.")
        return
    df = pd.DataFrame([
        {"ID": c["id"], "Tipo": c["tipo"], "Texto (extracto)": c["texto"][:120] + "..."}
        for c in clausulas
    ])
    st.dataframe(df, use_container_width=True)
