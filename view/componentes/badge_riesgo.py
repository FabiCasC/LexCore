import streamlit as st

_ICONOS = {"critico": "🔴", "alto": "🟠", "medio": "🟡", "bajo": "🟢"}

def mostrar_badge(hallazgo: dict) -> None:
    sev   = hallazgo.get("severidad", "bajo")
    icono = _ICONOS.get(sev, "⚪")
    st.markdown(
        f"{icono} **Cláusula {hallazgo.get('clausula_id')}** — "
        f"Riesgo: `{hallazgo.get('tipo_riesgo')}` | Severidad: `{sev}`"
    )
