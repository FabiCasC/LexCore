import streamlit as st
from controller.almacenamiento.lector_csv import leer_auditorias

def mostrar():
    st.title("Historial de Auditorías")

    df = leer_auditorias()
    if df.empty:
        st.info("No hay auditorías registradas aún.")
        return

    st.dataframe(df, use_container_width=True)
    st.caption(f"Total de auditorías: {len(df)}")
