import streamlit as st

st.title("Mi primera app con Streamlit")

nombre = st.text_input("¿Cómo te llamás?")

if nombre:
    st.write(f"¡Hola, {nombre}!")
    