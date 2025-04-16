
import streamlit as st
import pandas as pd
from supabase_client import get_authenticated_client

st.set_page_config(page_title="CSV Upload", layout="centered")
st.title("📁 Admin CSV Upload")

email = st.session_state.get("email")

if email == "newspoolestate@gmail.com":
    uploaded_file = st.file_uploader("CSV-Datei hochladen", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
        st.success("✅ Datei erfolgreich geladen.")
else:
    st.error("🚫 Kein Zugriff – nur Admin erlaubt.")
