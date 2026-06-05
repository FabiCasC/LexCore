import streamlit as st
from view.componentes.tabla_clausulas  import mostrar_tabla
from view.componentes.badge_riesgo     import mostrar_badge
from view.componentes.descarga_reporte import mostrar_descarga

def mostrar():
    st.title("Resultados del Análisis")

    if "ultimo_resultado" not in st.session_state:
        st.info("No hay resultados aún. Ve a **Cargar Contrato** primero.")
        return

    res = st.session_state["ultimo_resultado"]
    st.subheader(f"Contrato: {res['nombre']}  ·  ID: {res['contrato_id']}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total cláusulas",      res["estadisticas"]["total"])
    col2.metric("Cláusulas con riesgo", res["estadisticas"]["riesgo"])
    col3.metric("% de riesgo",          f"{res['estadisticas']['porcentaje_riesgo']}%")

    st.divider()
    st.subheader("Cláusulas detectadas")
    mostrar_tabla(res["clausulas"])

    if res["hallazgos"]:
        st.subheader("Hallazgos")
        for h in res["hallazgos"]:
            mostrar_badge(h)

    st.divider()
    mostrar_descarga(res)
