import streamlit as st
import numpy as np

st.title("🧮 Calculadora de Determinante de una Matriz")

# Selección del tamaño de la matriz
n = st.number_input("Ingrese el tamaño de la matriz (n x n):", min_value=2, max_value=10, value=3, step=1)

st.markdown("### Ingrese los elementos de la matriz")

# Crear una matriz vacía para los inputs
matrix = []

for i in range(n):
    row = []
    cols = st.columns(n)
    for j in range(n):
        val = cols[j].number_input(f"({i+1}, {j+1})", value=0.0, key=f"{i}-{j}")
        row.append(val)
    matrix.append(row)

# Botón para calcular la determinante
if st.button("Calcular Determinante"):
    matriz_np = np.array(matrix)
    determinante = round(np.linalg.det(matriz_np), 4)  # Redondeamos para mayor claridad

    st.markdown("## Resultado:")
    st.write(f"La determinante de la matriz es: **{determinante}**")

    if determinante == 0:
        st.warning("⚠️ La determinante es **0**. La matriz es **singular** (no invertible).")
