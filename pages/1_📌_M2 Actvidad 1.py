import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

st.title("Actividad 1 - Creación de DataFrames")
st.write("En esta actividad, crearemos un DataFrame utilizando la biblioteca pandas y realizaremos algunas operaciones básicas.")
st.write("A continuación, se presentan los pasos para completar la actividad.")

# Sección 1: Diccionario
st.subheader("📚 DataFrame de Libros")
libros_dict = {
    "título": ["Cien años de soledad", "1984", "El principito", "Rayuela"],
    "autor": ["Gabriel García Márquez", "George Orwell", "Antoine de Saint-Exupéry", "Julio Cortázar"],
    "año de publicación": [1967, 1949, 1943, 1963],
    "género": ["Realismo mágico", "Distopía", "Fábula", "Ficción"]
}
df_libros = pd.DataFrame(libros_dict)
st.dataframe(df_libros) 



