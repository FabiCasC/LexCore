import streamlit as st

def mostrar():
    st.title("LexCore — Auditoría Legal de Contratos")
    st.markdown("""
    Bienvenido a **LexCore**, sistema inteligente que analiza contratos legales
    detectando cláusulas riesgosas, incompletas o problemáticas.

    ### ¿Cómo funciona?
    1. Ve a **Cargar Contrato** y pega o sube el texto del contrato.
    2. El sistema tokeniza con Scala y valida con reglas Prolog.
    3. Revisa los **Resultados** con los hallazgos y nivel de riesgo.
    4. Consulta el **Historial** de contratos anteriores.
    """)
    st.info("Selecciona una opción del menú lateral para comenzar.")
