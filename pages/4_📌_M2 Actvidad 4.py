import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker
import random

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

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

fake = Faker('es_CO')
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'], weights=[0.3, 0.4, 0.15, 0.1, 0.05], k=n),
    'municipio': random.choices(
        ['Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja', 'Manizales',
         'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'], k=n),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        ['Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero', 'Médico', 'Desempleado',
         'Pensionado', 'Emprendedor', 'Obrero'], k=n),
    'tipo_vivienda': random.choices(['Propia', 'Arrendada', 'Familiar'], k=n),
    'fecha_nacimiento': [fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}
df = pd.DataFrame(data)
df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])


st.title("📊 Explorador interactivo con .loc y .iloc")


if st.checkbox("Mostrar todo el DataFrame"):
    st.dataframe(df)


st.subheader("Selección por posición con `.iloc`")
col1, col2 = st.columns(2)
start_idx = col1.number_input("Índice inicial", min_value=0, max_value=len(df)-1, value=0)
end_idx = col2.number_input("Índice final", min_value=1, max_value=len(df), value=5)
if st.button("Mostrar filas con iloc"):
    st.dataframe(df.iloc[int(start_idx):int(end_idx)])


st.subheader("Búsqueda por etiqueta con `.loc`")
col3, col4 = st.columns(2)
edad_min = col3.slider("Edad mínima", 15, 75, 25)
edad_max = col4.slider("Edad máxima", 15, 75, 60)
if st.button("Filtrar por edad con loc"):
    resultado = df.loc[(df['edad'] >= edad_min) & (df['edad'] <= edad_max)]
    st.dataframe(resultado)


st.subheader("Modificar ocupación con `.loc`")
col5, col6 = st.columns(2)
id_persona = col5.number_input("ID de la persona", min_value=1, max_value=50, value=1)
nueva_ocupacion = col6.selectbox("Nueva ocupación", df['ocupacion'].unique())
if st.button("Actualizar ocupación"):
    df.loc[df['id'] == id_persona, 'ocupacion'] = nueva_ocupacion
    st.success(f"Se actualizó la ocupación del ID {id_persona} a {nueva_ocupacion}")
    st.dataframe(df[df['id'] == id_persona])


st.subheader("Consultar valor específico con `.iloc`")
col7, col8 = st.columns(2)
fila_iloc = col7.number_input("Fila (posición)", 0, len(df)-1, 0)
columna_iloc = col8.number_input("Columna (posición)", 0, len(df.columns)-1, 0)
if st.button("Mostrar valor con iloc"):
    valor = df.iloc[int(fila_iloc), int(columna_iloc)]
    st.info(f"Valor en posición [{fila_iloc}, {columna_iloc}]: **{valor}**")


st.subheader("Consultar valor específico con `.loc`")
col9, col10 = st.columns(2)
id_loc = col9.number_input("ID", min_value=1, max_value=50, value=1)
columna_loc = col10.selectbox("Columna", df.columns)
if st.button("Mostrar valor con loc"):
    valor = df.loc[df['id'] == id_loc, columna_loc].values[0]
    st.info(f"Valor de '{columna_loc}' para ID {id_loc}: **{valor}**")