import streamlit as st
def encabezado_titulo():
    st.title("MVP Jurídico Deliberativo")
def mostrar_historial(steps):
    for s in steps:
        st.write(f"- **{s['step']}**: {s['detail']}")
