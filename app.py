import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header('Análisis de Datos de Vehículos en Venta')
hist_button = st.button('Construir histograma') # crear un botón


        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)


# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión con personalización
    scatter_fig = px.scatter(car_data, x="odometer", y="price", title='Gráfico de Dispersión del Odómetro vs Precio', labels={'odometer': 'Kilometraje', 'price': 'Precio'}, color_discrete_sequence=['blue'])
    
    st.plotly_chart(scatter_fig, use_container_width=True)