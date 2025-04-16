
import streamlit as st

st.set_page_config(page_title="Strategie Auswahl", layout="centered")

st.title("📊 Strategie Auswahl")

hot = st.slider("Anteil heiße Zahlen (%)", 0, 100, 50)

if st.button("💾 Strategie speichern"):
    st.success(f"Strategie mit {hot}% heiße Zahlen gespeichert (Simuliert)")
    st.page_link("pages/TippGenerator.py", label="➡️ Weiter zum TippGenerator", icon="🚀")
