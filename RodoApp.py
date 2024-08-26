import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Análisis de Datos de Vehículos en Venta')

# Filtrado de datos
fuel_type = st.sidebar.selectbox('Selecciona el tipo de combustible', car_data['fuel'].unique())
filtered_data = car_data[car_data['fuel'] == fuel_type]

# Casilla de verificación para el histograma
hist_checkbox = st.sidebar.checkbox('Mostrar histograma')

if hist_checkbox:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(filtered_data, x="odometer", nbins=30, title='Distribución del Kilometraje')
    fig.update_layout(xaxis_title='Kilometraje', yaxis_title='Frecuencia')
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
scatter_checkbox = st.sidebar.checkbox('Mostrar gráfico de dispersión')

if scatter_checkbox:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    scatter_fig = px.scatter(filtered_data, x="odometer", y="price", color="condition", title='Gráfico de Dispersión del Odómetro vs Precio', labels={'odometer': 'Kilometraje', 'price': 'Precio'}, trendline="ols")
    st.plotly_chart(scatter_fig, use_container_width=True)