import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Cargamos el excel de Pases vs. Yardas.
df = pd.read_excel('YARDAS_PASOS_DATOS_TICS.xlsx', index_col=0)

# Visualizar los primeros 5 datos de mi base de datos.
st.dataframe(df.head())
# Estadística descriptiva.
st.header("Estadística descriptiva")
st.dataframe(df.describe())

# Esto sirve para renombrar las columnas de mi dataframe.
df.columns = [c.lower().replace(' ', '_') for c in df.columns]


col1, col2 = st.columns(2)

with col1:
    # Esto es una gráfica de caja y bigote.
    # de los pases completos.
    fig, ax = plt.subplots()
    ax.boxplot(df['pases_completos'])
    st.header("Diagrama de caja y bigote\nde pases completos")
    st.pyplot(fig)
with col2:
    # Esto es una gráfica de caja y bigote.
    # de las yardas totales.
    fig, ax = plt.subplots()
    ax.boxplot(df['yardas_totales'])
    st.header("Diagrama de caja y bigote\nde yardas totales")
    st.pyplot(fig)
