@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

df = load_data("data.csv")
st.write(df)
