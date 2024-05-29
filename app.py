import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos desde un archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis Visual de Datos de Vehículos')

# Permitir al usuario elegir la columna para el histograma
st.write("Opciones Avanzadas")
column_hist = st.selectbox('Elige la columna para el histograma', [
                           'odometer', 'price', 'days_listed'])
build_histogram = st.checkbox('Mostrar Histograma')
if build_histogram:
    st.write(f'Histograma para la columna "{column_hist}"')
    fig_hist = px.histogram(car_data, x=column_hist)
    st.plotly_chart(fig_hist, use_container_width=True)

# Permitir al usuario elegir las columnas para el gráfico de dispersión
st.write("Gráficos de Dispersión")
options_scatter = {
    'odometer vs price': ('odometer', 'price'),
    'odometer vs days_listed': ('odometer', 'days_listed'),
    'price vs days_listed': ('price', 'days_listed')
}
choice_scatter = st.selectbox(
    'Elige las columnas para el gráfico de dispersión', list(options_scatter.keys()))
build_scatter = st.checkbox('Mostrar Gráfico de Dispersión')
if build_scatter:
    x, y = options_scatter[choice_scatter]
    st.write(f'Gráfico de dispersión para "{x}" vs "{y}"')
    fig_scatter = px.scatter(car_data, x=x, y=y)
    st.plotly_chart(fig_scatter, use_container_width=True)

# Permitir al usuario elegir la columna para el gráfico de barras
st.write("Gráficos de Barras")
column_bar = st.selectbox('Elige la columna para el gráfico de barras', [
                          'condition', 'fuel', 'transmission', 'type'])
build_bar = st.checkbox('Mostrar Gráfico de Barras')
if build_bar:
    st.write(f'Gráfico de barras para la columna "{column_bar}"')
    count_data = car_data[column_bar].value_counts().reset_index()
    count_data.columns = [column_bar, 'count']
    fig_bar = px.bar(count_data, y=column_bar, x='count', text_auto=True,
                     title=f"Distribución de {column_bar}", orientation='h')
    st.plotly_chart(fig_bar, use_container_width=True)
