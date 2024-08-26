import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Análisis de Datos de Vehículos en Venta')

# Casilla de verificación para el histograma
hist_checkbox = st.sidebar.checkbox('Mostrar histograma')

if hist_checkbox:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


# Casilla de verificación para el gráfico de dispersión
scatter_checkbox = st.sidebar.checkbox('Mostrar gráfico de dispersión')

if scatter_checkbox:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    scatter_fig = px.scatter(car_data, x="odometer", y="price", title='Gráfico de Dispersión del Odómetro vs Precio', labels={'odometer': 'Kilometraje', 'price': 'Precio'}, color_discrete_sequence=['blue'])
    st.plotly_chart(scatter_fig, use_container_width=True)