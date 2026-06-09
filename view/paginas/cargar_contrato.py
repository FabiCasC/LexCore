import streamlit as st
from controller.orquestador.pipeline import analizar_contrato

def mostrar():
    st.title("Cargar Contrato")

    nombre = st.text_input("Nombre del contrato", placeholder="Ej: Contrato de Arrendamiento 2024")
    metodo = st.radio("Método de carga", ["Pegar texto", "Subir archivo .txt"])

    texto = ""
    if metodo == "Pegar texto":
        texto = st.text_area("Texto del contrato", height=300)
    else:
        archivo = st.file_uploader("Sube el contrato", type=["txt"])
        if archivo:
            texto = archivo.read().decode("utf-8")
            st.text_area("Contenido", texto, height=200, disabled=True)

    if st.button("Analizar contrato", type="primary"):
        if not nombre or not texto.strip():
            st.warning("Ingresa el nombre y el texto del contrato.")
            return
        with st.spinner("Analizando contrato..."):
            try:
                resultado = analizar_contrato(texto, nombre)
                st.session_state["ultimo_resultado"] = resultado
                st.success(f"Análisis completado — {len(resultado['hallazgos'])} hallazgo(s) encontrado(s).")
                st.info("Ve a **Resultados** para ver el detalle.")
            except Exception as e:
                st.error(f"Error durante el análisis: {e}")
