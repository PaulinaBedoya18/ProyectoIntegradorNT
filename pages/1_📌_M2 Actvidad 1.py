import streamlit as st
import pandas as pd
import csv 
import sqlite3
import numpy as np
import openpyxl

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

st.subheader("DataFrame de Libros")
libros_dict = {
    "título": ["Cien años de soledad", "1984", "El principito", "Rayuela"],
    "autor": ["Gabriel García Márquez", "George Orwell", "Antoine de Saint-Exupéry", "Julio Cortázar"],
    "año de publicación": [1967, 1949, 1943, 1963],
    "género": ["Realismo mágico", "Distopía", "Fábula", "Ficción"]
}
df_libros = pd.DataFrame(libros_dict)
st.dataframe(df_libros) 

st.subheader("Información de Ciudades")

ciudades = [
    {"nombre": "Medellín", "población": 2500000, "país": "Colombia"},
    {"nombre": "Buenos Aires", "población": 3000000, "país": "Argentina"},
    {"nombre": "Madrid", "población": 3200000, "país": "España"},
    {"nombre": "Ciudad de México", "población": 9200000, "país": "México"}
]
df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)

st.subheader("Productos en Inventario")

productos = [
    ["Laptop", 3200000, 10],
    ["Mouse", 50000, 150],
    ["Teclado", 80000, 100],
    ["Monitor", 600000, 25]
]
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)


st.subheader("Datos de Personas")

nombres = pd.Series(["Laura", "Juan", "Pedro", "Ana"])
edades = pd.Series([23, 30, 28, 25])
ciudades = pd.Series(["Bello", "Bogotá", "Medellín", "Cali"])

df_personas = pd.DataFrame({
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
})
st.dataframe(df_personas)


st.subheader("Datos desde CSV")

df_csv = pd.read_csv("data.csv")

st.dataframe(df_csv)

st.subheader("Datos desde Excel")

df_excel = pd.read_excel("data.xlsx")

st.dataframe(df_excel)


df_json = pd.read_json("data.json")
st.write("### Datos de Usuarios desde JSON")
st.dataframe(df_json)



csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df_url = pd.read_csv(csv_url)
st.write("Datos desde URL")
st.dataframe(df_url)



conn = sqlite3.connect("estudiantes.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        calificacion REAL
    )
""")
conn.commit()

cursor.execute("SELECT COUNT(*) FROM estudiantes")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", [
        ("María", 88.0),
        ("Luis", 91.5),
        ("Camila", 79.3)
    ])
    conn.commit()

df_sqlite = pd.read_sql("SELECT * FROM estudiantes", conn)
st.write("### Datos desde SQLite")
st.dataframe(df_sqlite)
conn.close()



array_numpy = np.array([
    [1, 4.2, 150],
    [2, 5.6, 300],
    [3, 6.8, 450]
])

df_numpy = pd.DataFrame(array_numpy, columns=["ID", "Valor", "Cantidad"])
st.write("### Datos desde NumPy")
st.dataframe(df_numpy)