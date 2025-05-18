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

st.title("Momento 2 - Actividad 3")

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

# Configurar Faker para Colombia
fake = Faker('es_CO')

# Establecer semilla para reproducibilidad
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

# Crear datos
n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',  # Caribe
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',  # Andina
            'Cali', 'Quibdó', 'Buenaventura',           # Pacífica
            'Villavicencio', 'Yopal',                    # Orinoquía
            'Leticia', 'Puerto Inírida'                  # Amazonía
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(
        ['Propia', 'Arrendada', 'Familiar'],
        k=n
    ),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}

df_nuevo = pd.DataFrame(data)

df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan

df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])

print("Primeras 5 filas del nuevo DataFrame:")
print(df_nuevo.head())

st.write("Accede al notebook de Google Colab [aquí](https://colab.research.google.com/drive/1aJQFlK5Xwcq3a8e7vOn8DD9QX8i_vENJ?usp=sharing).")



st.title("Filtros Dinámicos en Streamlit")
df_filtrado = df_nuevo.copy()

if st.sidebar.checkbox("Filtrar por rango de edad"):
    edad_min, edad_max = st.sidebar.slider("Rango de edad", 15, 75, (20, 40))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(edad_min, edad_max)]

if st.sidebar.checkbox("Filtrar por municipios"):
    municipios = st.sidebar.multiselect("Municipios", [
        'Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja',
        'Manizales', 'Cali', 'Quibdó', 'Buenaventura', 'Villavicencio', 'Yopal',
        'Leticia', 'Puerto Inírida'
    ])
    if municipios:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(municipios)]

if st.sidebar.checkbox("Filtrar por ingreso mensual mínimo"):
    ingreso_min = st.sidebar.slider("Ingreso mínimo", 800000, 12000000, 3000000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_min]

if st.sidebar.checkbox("Filtrar por ocupación"):
    ocupaciones = st.sidebar.multiselect("Ocupaciones", [
        'Estudiante', 'Docente', 'Comerciante', 'Agricultor', 'Ingeniero',
        'Médico', 'Desempleado', 'Pensionado', 'Emprendedor', 'Obrero'
    ])
    if ocupaciones:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(ocupaciones)]

if st.sidebar.checkbox("Filtrar personas sin vivienda propia"):
    df_filtrado = df_filtrado[df_filtrado['tipo_vivienda'] != 'Propia']

if st.sidebar.checkbox("Filtrar por nombre"):
    texto = st.sidebar.text_input("Nombre contiene:")
    if texto:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto, case=False, na=False)]

if st.sidebar.checkbox("Filtrar por año de nacimiento"):
    anio = st.sidebar.selectbox("Año", list(range(1949, 2010)))
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == anio]

if st.sidebar.checkbox("Filtrar por acceso a internet"):
    acceso = st.sidebar.radio("¿Acceso a internet?", ["Sí", "No"])
    acceso_bool = True if acceso == "Sí" else False
    df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == acceso_bool]

if st.sidebar.checkbox("Filtrar por ingresos nulos"):
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

if st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento"):
    fecha_inicio = st.sidebar.date_input("Desde", datetime(1950, 1, 1))
    fecha_fin = st.sidebar.date_input("Hasta", datetime(2009, 12, 31))
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(fecha_inicio, fecha_fin)]

st.write(f"Resultados: {len(df_filtrado)} registros encontrados")
st.dataframe(df_filtrado)