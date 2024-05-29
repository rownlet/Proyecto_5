import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos desde un archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis Visual de Datos de Vehículos')

# Botón para construir un histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para la columna "odometer" del conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write(
        'Creación de un gráfico de dispersión para las columnas "odometer" y "price"')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Opcional: Uso de casillas de verificación en lugar de botones
st.write("Opciones Avanzadas")
build_histogram = st.checkbox('Mostrar Histograma')
if build_histogram:
    st.write('Histograma para la columna "odometer"')
    fig_hist_check = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist_check, use_container_width=True)

build_scatter = st.checkbox('Mostrar Gráfico de Dispersión')
if build_scatter:
    st.write('Gráfico de dispersión para "odometer" vs "price"')
    fig_scatter_check = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter_check, use_container_width=True)
