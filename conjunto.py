import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.title("Representações Matemáticas - Unicuritiba")
"""
### GRUPO:

### -Rafael Viegas (172114821)
### -Gustavo Henrique Santos (172117007)
### -Mateus S Krupa (172111058 )
### -Ramon Marinho (172320117)
### -Tito Cláudio (172220777)

###"""

st.header("1 - Conjuntos")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
common = A.intersection(B)
only_A = A - B
only_B = B - A

fig1 = go.Figure()

fig1.add_trace(go.Scatter3d(
    x=[1]*len(only_A), y=list(only_A), z=[1]*len(only_A),
    mode='markers', marker=dict(size=10, color='blue'), name="A"
))

fig1.add_trace(go.Scatter3d(
    x=[2]*len(only_B), y=list(only_B), z=[2]*len(only_B),
    mode='markers', marker=dict(size=10, color='green'), name="B"
))

fig1.add_trace(go.Scatter3d(
    x=[1.5]*len(common), y=list(common), z=[1.5]*len(common),
    mode='markers', marker=dict(size=10, color='purple'), name="A ∩ B"
))

st.plotly_chart(fig1)

st.title("2 - Plano cartesiano")

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis', opacity=0.7)])

fig.add_trace(go.Scatter3d(x=[-10, 10], y=[0, 0], z=[0, 0], mode='lines', line=dict(color='red', width=5), name='Eixo X'))
fig.add_trace(go.Scatter3d(x=[0, 0], y=[-10, 10], z=[0, 0], mode='lines', line=dict(color='green', width=5), name='Eixo Y'))
fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[-10, 10], mode='lines', line=dict(color='blue', width=5), name='Eixo Z'))

fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectratio=dict(x=1, y=1, z=0.3)
    ),
)

st.plotly_chart(fig)

st.title("3 - Grupos")

grupos = ['Grupo 1', 'Grupo 2', 'Grupo 3', 'Grupo 4', 'Grupo 5']
x = [1, 2, 3, 4, 5]
y = [10, 9, 7, 6, 8]
z = [5, 7, 3, 9, 6]

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers+text',
    marker=dict(size=8, color=z, colorscale='Viridis', opacity=0.8),
    text=grupos,
    textposition='top center',
))

fig.update_layout(
    scene=dict(
        xaxis_title='Eixo X',
        yaxis_title='Eixo Y',
        zaxis_title='Eixo Z',
    ),
)

st.plotly_chart(fig)

st.title("4 - Aneis")

st.markdown("""
### Curva Cúbica
A curva cúbica é definida pela equação:

\\[
z = x^3 + ax + b
\\]

onde:
- **a** e **b** são constantes que influenciam a forma da curva.
- Neste exemplo, utilizamos **a = -1** e **b = 1**.

### Adição Geométrica
- Os pontos **P** e **Q** são escolhidos na curva, e a reta entre eles se cruza novamente na curva em um ponto **R**. Este ponto **R** é refletido em relação ao plano XY.
""")

a = -1
b = 1

x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
x_mesh, y_mesh = np.meshgrid(x, y)
z = x_mesh**3 + a * x_mesh + b

P = np.array([-1, 0, (-1)**3 + a * (-1) + b])
Q = np.array([1, 0, (1)**3 + a * (1) + b])

m = (Q[2] - P[2]) / (Q[0] - P[0])
x_R = - (P[2] + Q[2]) / m
y_R = 0
z_R = x_R**3 + a * x_R + b

R = np.array([x_R, y_R, -z_R])

fig = go.Figure()

fig.add_trace(go.Surface(z=z, x=x_mesh, y=y_mesh, colorscale='Viridis', opacity=0.8, name='Curva Cúbica'))

fig.add_trace(go.Scatter3d(x=[P[0]], y=[P[1]], z=[P[2]], mode='markers+text',
                             marker=dict(size=5, color='red'), text=['P'], textposition='top center'))
fig.add_trace(go.Scatter3d(x=[Q[0]], y=[Q[1]], z=[Q[2]], mode='markers+text',
                             marker=dict(size=5, color='green'), text=['Q'], textposition='top center'))
fig.add_trace(go.Scatter3d(x=[R[0]], y=[R[1]], z=[R[2]], mode='markers+text',
                             marker=dict(size=5, color='orange'), text=['R'], textposition='top center'))

fig.add_trace(go.Scatter3d(x=[P[0], Q[0]], y=[P[1], Q[1]], z=[P[2], Q[2]],
                             mode='lines', line=dict(color='black', dash='dash'), name='Reta entre P e Q'))

fig.update_layout(
    scene=dict(
        xaxis_title='Eixo X',
        yaxis_title='Eixo Y',
        zaxis_title='Eixo Z',
        aspectmode='cube'
    ),
    showlegend=True
)

st.plotly_chart(fig)

st.header("5 - Corpos")

fractions = [1/2, 1/3, 1/4, 1/5]
x = fractions
y = np.square(fractions)
z = [1]*len(fractions)

fig5 = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers+text',
    text=[f"Frações: {f:.2f}<br>Área: {f**2:.2f}<br>Volume: {f**3:.2f}" for f in fractions],
    marker=dict(size=10, color='red')
)])

fig5.update_layout(scene=dict(
    xaxis_title="Frações",
    yaxis_title="Área (Frações^2)",
    zaxis_title="Constante Z",
    camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
))

st.plotly_chart(fig5)

st.header("6 - Funções")

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

fig6 = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')])
fig6.update_layout(title='Superfície da Função Quadrática Z = X² + Y²',
                   scene=dict(
                       xaxis_title='X',
                       yaxis_title='Y',
                       zaxis_title='Z'),
                   margin=dict(l=0, r=0, b=0, t=50)
                   )


st.plotly_chart(fig6)

st.header("7 - Sistema de Equações Lineares")

x = np.linspace(-10, 10, 100)

y1 = 2 * x + 1
y2 = -x + 3
y3 = 0.5 * x - 2

z = np.linspace(0, 10, 100)

fig7 = go.Figure()

fig7.add_trace(go.Scatter3d(x=x, y=y1, z=z, mode='lines', name='2x + 1', line=dict(color='blue', width=3)))
fig7.add_trace(go.Scatter3d(x=x, y=y2, z=z, mode='lines', name='-x + 3', line=dict(color='orange', width=3)))
fig7.add_trace(go.Scatter3d(x=x, y=y3, z=z, mode='lines', name='0.5x - 2', line=dict(color='green', width=3)))

fig7.update_layout(title='Sistema de Equações Lineares',
                   scene=dict(
                       xaxis_title="X",
                       yaxis_title="Y",
                       zaxis_title="Z"),
                   margin=dict(l=0, r=0, b=0, t=50)
                   )


st.plotly_chart(fig7)

st.header("8 - Transformações Lineares")
phi = np.pi / 4
rotation_matrix = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])
vector = np.array([1, 0])
rotated_vector = rotation_matrix @ vector

fig8 = go.Figure()

fig8.add_trace(go.Scatter3d(
    x=[0, vector[0]], y=[0, vector[1]], z=[0, 0],
    mode='lines+markers', name='Original',
    marker=dict(size=5, color='blue')
))

fig8.add_trace(go.Scatter3d(
    x=[0, rotated_vector[0]], y=[0, rotated_vector[1]], z=[0, 0],
    mode='lines+markers', name='Rotacionado',
    marker=dict(size=5, color='red')
))

fig8.update_layout(scene=dict(
    xaxis_title="X",
    yaxis_title="Y",
    zaxis_title="Z"
))
st.plotly_chart(fig8)
