import streamlit as st
from controller.analisis.reportes import generar_reporte

def mostrar_descarga(resultado: dict) -> None:
    reporte = generar_reporte(resultado)
    st.download_button(
        label="Descargar reporte JSON",
        data=reporte,
        file_name=f"reporte_{resultado.get('contrato_id', 'lexcore')}.json",
        mime="application/json",
    )
