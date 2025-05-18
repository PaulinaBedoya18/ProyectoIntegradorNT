import streamlit as st
import pandas as pd
import io

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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

st.title("Visualización de Estudiantes en Colombia")

@st.cache_data
def cargar_datos():
    return pd.read_csv("estudiantes_colombia.csv")

df = cargar_datos()

st.subheader("Primeras y Últimas Filas")
st.write("### Primeras 5 filas del dataset")
st.dataframe(df.head())

st.write("### Últimas 5 filas del dataset")
st.dataframe(df.tail())

st.subheader("Resumen del Dataset")
info_df = pd.DataFrame({
    "Columna": df.columns,
    "Tipo de dato": df.dtypes.values,
    "Valores nulos": df.isnull().sum().values,
    "Valores únicos": df.nunique().values
})


st.dataframe(info_df)
st.write("### Estadísticas Descriptivas")
st.dataframe(df.describe())

st.subheader("Seleccionar Columnas")
columnas = st.multiselect("Selecciona las columnas que quieres ver:", df.columns.tolist(), default=["nombre", "edad", "promedio"])
if columnas:
    st.dataframe(df[columnas])
else:
    st.warning("Por favor selecciona al menos una columna.")

st.subheader("Filtrar por Promedio")
valor_minimo = float(df["promedio"].min())
valor_maximo = float(df["promedio"].max())

umbral = st.slider("Mostrar estudiantes con promedio mayor a:", min_value=valor_minimo, max_value=valor_maximo, value=valor_minimo)

filtro = df[df["promedio"] > umbral]
st.write(f"Estudiantes con promedio mayor a {umbral}:")
st.dataframe(filtro)

