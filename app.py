import streamlit as st
import plotly.graph_objects as go
import numpy as np
import random

# Configuración de la página web
st.set_page_config(page_title="Regalo 3D", layout="wide")

def crear_corazon_pro(off_x=0, off_y=0, off_z=0, escala=1.0):
    # Aumentamos de 50 a 50 o 150 para bordes mucho más suaves
    res = 80
    t = np.linspace(0, 2 * np.pi, res)
    phi = np.linspace(0, np.pi, res)
    T, PHI = np.meshgrid(t, phi)
    
    # Ecuación paramétrica con alta resolución
    x = escala * (16 * np.sin(T)**3 * np.sin(PHI)) + off_x
    y = escala * ((13 * np.cos(T) - 5 * np.cos(2*T) - 2 * np.cos(3*T) - np.cos(4*T)) * np.sin(PHI)) + off_y
    z = escala * (15 * np.cos(PHI)) + off_z
    
    return x.flatten(), y.flatten(), z.flatten()



st.title("❤️ Un detalle especial para mi pooooosaa bella poooooosaaaa ❤️")

fig = go.Figure()

# Generamos 15 corazones
for i in range(15):
    x, y, z = crear_corazon_pro(
        random.uniform(-50, 50), 
        random.uniform(-50, 50), 
        random.uniform(-50, 50), 
        random.uniform(0.6, 1.3)
    )
    fig.add_trace(go.Mesh3d(
    x=x, y=y, z=z,
    alphahull=0,
    color='red',
    flatshading=False, # <-- IMPORTANTE: False para que suavice las caras
    lighting=dict(
        ambient=0.5,
        diffuse=1,
        fresnel=1, # Da un brillo elegante en los bordes
        specular=0.5,
        roughness=0.05 # Lo hace ver más pulido/brillante
    ),
    lightposition=dict(x=100, y=100, z=100)
    ))
    
fig.update_layout(
    scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False),
    margin=dict(l=0, r=0, b=0, t=0),
    height=600
)


# ESTO ES LO QUE CAMBIA: Usamos st.plotly_chart para la web
st.plotly_chart(fig, use_container_width=True)

st.markdown("<h2 style='text-align: center;'>¡Espero que te guste muchisimo mi detallito bella bebeee!</h2>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Así de grande es el universo de amor que me haces sentir bella bebe</h2>", unsafe_allow_html=True)
