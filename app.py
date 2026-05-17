import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Exploración de Datos CSV", layout="wide")

st.title("📊 Aplicativo de Exploración de Datos")
st.write("Sube un archivo CSV para analizar sus datos y generar un diagrama de correlación.")

archivo = st.file_uploader("📂 Carga tu archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)

    st.success("✅ Archivo cargado correctamente")

    st.subheader("Vista previa de los datos")
    st.dataframe(df.head())

    st.subheader("Información general")
    st.write("Filas y columnas:", df.shape)

    st.write("Columnas del dataset:")
    st.write(df.columns.tolist())

    st.subheader("Estadísticas descriptivas")
    st.dataframe(df.describe())

    columnas_numericas = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    if len(columnas_numericas) >= 2:
        st.subheader("🔥 Diagrama de correlación")

        columnas_seleccionadas = st.multiselect(
            "Selecciona las columnas para analizar correlación:",
            columnas_numericas,
            default=columnas_numericas[:2]
        )

        if len(columnas_seleccionadas) >= 2:
            correlacion = df[columnas_seleccionadas].corr()

            fig, ax = plt.subplots(figsize=(8, 5))
            sns.heatmap(correlacion, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

            st.write("Matriz de correlación:")
            st.dataframe(correlacion)
        else:
            st.warning("Selecciona al menos 2 columnas numéricas.")
    else:
        st.warning("El archivo debe tener al menos 2 columnas numéricas para calcular correlación.")

else:
    st.info("Por favor, sube un archivo CSV para comenzar.")