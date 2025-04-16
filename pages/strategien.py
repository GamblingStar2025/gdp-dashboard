
import streamlit as st

st.set_page_config(page_title="Strategien", layout="centered")
st.title("🧠 Strategie Auswahl")

strategie = st.slider("Anteil heiße Zahlen (%)", 0, 100, 50)
if st.button("💾 Strategie speichern"):
    st.success(f"Strategie mit {strategie}% heiße Zahlen gespeichert (Simuliert)")
