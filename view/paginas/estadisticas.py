import streamlit as st
from controller.almacenamiento.lector_csv import leer_auditorias, leer_hallazgos

def mostrar():
    st.title("Estadísticas Globales")

    df_aud = leer_auditorias()
    df_hal = leer_hallazgos()

    if df_aud.empty:
        st.info("No hay datos suficientes para mostrar estadísticas.")
        return

    col1, col2 = st.columns(2)
    col1.metric("Contratos analizados", len(df_aud))
    col2.metric("Total hallazgos",      len(df_hal))

    if "resultado" in df_aud.columns:
        st.subheader("Contratos por resultado")
        st.bar_chart(df_aud["resultado"].value_counts())

    if not df_hal.empty and "severidad" in df_hal.columns:
        st.subheader("Hallazgos por severidad")
        st.bar_chart(df_hal["severidad"].value_counts())
