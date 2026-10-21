import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos del archivo CSV guardado en la raíz del proyecto
car_data = pd.read_csv('../vehicles_us.csv')

# Encabezado principal de la aplicación web
st.header('Cuadro de Mandos de Anuncios de Venta de Coches')

# Mensaje o texto descriptivo
st.write('Selecciona una opción para desplegar las visualizaciones interactivas de los datos de vehículos:')

# Casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches:')

    # Crear el histograma con Plotly Express
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del Kilometraje (Odómetro)"
    )

    # Desplegar el gráfico en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write(
        'Creación de un gráfico de dispersión: Precio vs. Kilometraje por Condición')

    # Crear el gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="condition",
        title="Relación entre Precio y Odómetro según la Condición"
    )

    # Desplegar el gráfico en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
