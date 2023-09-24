import streamlit as st
import pandas as pd
import numpy as np

#streamlit run uber_pickups.py

# Cargar el archivo de estilo CSS
css = """
<link rel='stylesheet' href='style.css'>
"""

# Aplicar el estilo
st.markdown(css, unsafe_allow_html=True)

# Título del sitio
st.markdown("<h1 style='text-align: center; font-family: \"S&L Gothic\", sans-serif; color: red;'>Banorte FinancIA</h1>", unsafe_allow_html=True)

# Agregar espacio entre el título y el botón
st.write("")

# Texto del botón
button_text = "Pruébalo ya"

# Crea un contenedor para centrar el botón
container_style = "display: flex; justify-content: center;"
st.markdown(f'<div style="{container_style}"><button>{button_text}</button></div>', unsafe_allow_html=True)

# Títulos de las categorías
categorias = ["Fondos de inversión", "Seguros", "Tarjetas adicionales", "Tarjeta de crédito"]

# Crea dos columnas para organizar las categorías en una estructura 2x2
col1, col2 = st.columns(2)

# Aplica estilo CSS para centrar los títulos en las columnas
titulo_style = "text-align: center;"

# Agrega las categorías a las columnas con el estilo aplicado
col1.markdown(f'<p style="{titulo_style}">{categorias[0]}</p>', unsafe_allow_html=True)
col2.markdown(f'<p style="{titulo_style}">{categorias[1]}</p>', unsafe_allow_html=True)

# Agrega espacio entre las categorías
st.write("")

# Agrega las otras dos categorías centradas en las columnas
col1.markdown(f'<p style="{titulo_style}">{categorias[2]}</p>', unsafe_allow_html=True)
col2.markdown(f'<p style="{titulo_style}">{categorias[3]}</p>', unsafe_allow_html=True)