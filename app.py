# app.py  ── entry-point para Streamlit Cloud ──────────────────────────────────
import os, sys
ROOT = os.path.abspath(os.path.dirname(__file__))
SRC  = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
# -----------------------------------------------------------------------------

import streamlit as st
import json, pandas as pd

from src.engine.deliberative_engine import ejecutar_deliberacion
from src.components.layout import encabezado_titulo, mostrar_historial
from src.components.buttons import boton_refinar_opcion, boton_exportar

st.set_page_config(page_title="MVP Jurídico Deliberativo", layout="wide")
encabezado_titulo()

pregunta = st.text_input("🔍 Escribe tu pregunta jurídica principal:")

if st.button("Iniciar deliberación"):
    if not pregunta.strip():
        st.warning("Por favor, escribe una pregunta válida.")
    else:
        with st.spinner("Realizando indagación deliberativa…"):
            resultado = ejecutar_deliberacion(pregunta, n_subpreguntas=3)

        # ---------- UI ----------
        st.success("✅ Deliberación completada.")
        st.subheader("Respuesta central")
        st.write(resultado["respuesta_central"])

        st.subheader("Subpreguntas generadas")
        for sub in resultado["resultados"]:
            with st.expander(f"🔹 {sub['subpregunta']}"):
                st.write(sub["respuesta"])
                st.markdown("**Historial de razonamiento**")
                mostrar_historial(sub["trace"])
                st.markdown("**Métricas EEE**")
                st.json(sub["eee"])

        # Exportar
        exp_json, exp_csv = boton_exportar()
        if exp_json:
            st.download_button(
                "📥 JSON",
                data=json.dumps(resultado, ensure_ascii=False, indent=2),
                file_name="deliberacion.json",
                mime="application/json"
            )
        if exp_csv:
            filas = [
                {
                    "subpregunta": sub["subpregunta"],
                    "step": paso["step"],
                    "detail": paso["detail"],
                    **sub["eee"]
                }
                for sub in resultado["resultados"]
                for paso in sub["trace"]
            ]
            csv = pd.DataFrame(filas).to_csv(index=False).encode("utf-8")
            st.download_button("📥 CSV", data=csv, file_name="deliberacion.csv", mime="text/csv")
