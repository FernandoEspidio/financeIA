from streamlit.components.v1 import html
import streamlit as st
import pandas as pd
import numpy as np

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)
    
#streamlit run uber_pickups.py

# Cargar el archivo de estilo CSS
#css = """
#<link rel='stylesheet' href='style.css'>
#"""

# Aplicar el estilo
#with open("style.css") as f:
#    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#[data-testid="stAppViewContainer"] {
    #background-color: #DDDDDD;
    #opacity: 1;
    #background-image: url("https://st3.depositphotos.com/2487349/31823/i/600/depositphotos_318232892-stock-photo-christmas-city-background-with-lantern.jpg");
    #background-size: cover; 
    #background-repeat: no-repeat;

#}

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #DDDDDD;
    opacity: 1;
    background-image: url("https://images.adsttc.com/media/images/5078/6651/28ba/0d16/3c00/0003/medium_jpg/EBA_(8).jpg?1375412500"), url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbU0siJvsbkv3S6hmc_s11SdoFLKIFkpWKAA&usqp=CAU");
    background-size: 20% 100%, 20% 100%; 
    background-repeat: no-repeat, no-repeat;
    background-position: left top, right top; 
}

[data-testid="stHeader"] {
    background-color: #FF0F4A;
    background-image: url("https://www.blancosyblancos.com/img/Gallery/Blancos-y-Blancos-logo-4.png");
    background-size: 10%; 
    background-repeat: no-repeat;
    background-position: 2% 50%;
    opacity: 1;
    height: 100px;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Título del sitio
st.markdown("<h1 style='text-align: center; font-family: \"S&L Gothic\", sans-serif; color: red;'>Banorte FinancIA</h1>", unsafe_allow_html=True)

# Agregar espacio entre el título y el botón
st.write("")

# Subtítulo
st.markdown("<h3 style='text-align: center;'>¿Qué es Banorte FinancIA?</h3>", unsafe_allow_html=True)

# Agregar espacio entre el título y el botón
st.write("")

text = "Banorte FinancIA es la única plataforma y servicio que te ofrece una Inteligencia Artifical que te ayuda a tomar las mejores decisiones financieras. Nuestro próposito es ser tu apoyo personal y personalizado para apoyarte con el conocimiento de inversiones y finanzas."
st.markdown(f"<p style='text-align: center;'>{text}</p>", unsafe_allow_html=True)


# Enlace al que deseas redirigir
enlace = "http://10.22.234.131:8501"  # Reemplaza esto con tu enlace real

st.button('Pruébalo ya', on_click=open_page, args=('http://10.22.144.211:8501',))


st.markdown("<h3 style='text-align: center;'>Objetivo y Visión</h3>", unsafe_allow_html=True)
# Espacio entre el título y las columnas
st.write("")

# Crea dos columnas para organizar la visión y el objetivo
col1, col2 = st.columns(2)

# En la primera columna, agrega la visión
with col1:
    st.markdown("<h4 style='text-align: center;'>Visión</h4>", unsafe_allow_html=True)
    text2 = "Nuestra visión es empoderar a la generación joven y al público en general a tomar el control de su futuro financiero, proporcionando una plataforma de Inteligencia Artificial líder en el mercado que ofrezca orientación experta, educación y herramientas personalizadas para tomar decisiones financieras informadas y exitosas."
    st.markdown(f"<p style='text-align: center;'>{text2}</p>", unsafe_allow_html=True)

# En la segunda columna, agrega el objetivo
with col2:
    st.markdown("<h4 style='text-align: center;'>Objetivo</h4>", unsafe_allow_html=True)
    text3 = "Establecer una red sólida de usuarios jóvenes comprometidos con el crecimiento financiero y la inversión inteligente. Nuestro objetivo es guiar al menos al 80% de nuestros usuarios hacia inversiones financieramente sólidas y proporcionar datos y análisis que respalden sus decisiones, logrando un rendimiento financiero superior al promedio del mercado en un plazo de 2 años. Además, aspiramos a educar a al menos 100,000 jóvenes sobre conceptos financieros clave y brindarles la confianza y la autonomía para tomar decisiones financieras acertadas."
    st.markdown(f"<p style='text-align: center;'>{text3}</p>", unsafe_allow_html=True)


st.write("")
st.markdown("<h3 style='text-align: center;'>Conoce un poco más sobre nuestros servicios</h3>", unsafe_allow_html=True)
st.write("")

# Títulos de las categorías
categorias = ["Fondos de inversión", "Seguros", "Tarjetas adicionales", "Tarjeta de crédito"]

# Crea dos columnas para organizar las categorías en una estructura 2x2
col1, col2 = st.columns(2)

# Estilo CSS personalizado para las categorías
titulo_style = "text-align: center; background-color: red; color: white; padding: 10px; border-radius: 5px; font-family: 'S&L Gothic', sans-serif;"

# Agrega las categorías a las columnas con el estilo aplicado
col1.markdown(f'<p style="{titulo_style}">{categorias[0]}</p>', unsafe_allow_html=True)
col2.markdown(f'<p style="{titulo_style}">{categorias[1]}</p>', unsafe_allow_html=True)

# Agrega espacio entre las categorías
st.write("")

# Agrega las otras dos categorías centradas en las columnas
col1.markdown(f'<p style="{titulo_style}">{categorias[2]}</p>', unsafe_allow_html=True)
col2.markdown(f'<p style="{titulo_style}">{categorias[3]}</p>', unsafe_allow_html=True)

