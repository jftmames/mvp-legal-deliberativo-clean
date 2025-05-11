import streamlit as st
def boton_refinar_opcion():
    return st.button("🔄 Refinar preguntas")
def boton_exportar():
    col1, col2 = st.columns(2)
    return col1.button("📥 Export JSON"), col2.button("📥 Export CSV")
