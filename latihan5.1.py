import streamlit as st
import pandas as pd

@st.cache_data
def load_large_data():
    # Simulasi data besar
    return pd.DataFrame({
        "Angka": range(1, 10001),
        "Kuadrat": [x**2 for x in range(1, 10001)]
    })

st.title("Optimasi Aplikasi dengan Caching")

# Memuat data dengan cache
data = load_large_data()
st.write("Data berhasil dimuat:")
st.dataframe(data)
