import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from view.paginas import inicio, cargar_contrato, resultados, historial, estadisticas

st.set_page_config(
    page_title="LexCore",
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGINAS = {
    "Inicio":           inicio,
    "Cargar Contrato":  cargar_contrato,
    "Resultados":       resultados,
    "Historial":        historial,
    "Estadísticas":     estadisticas,
}

st.sidebar.title("LexCore")
st.sidebar.caption("Auditoría legal inteligente de contratos")
seleccion = st.sidebar.radio("Navegación", list(PAGINAS.keys()))

PAGINAS[seleccion].mostrar()
