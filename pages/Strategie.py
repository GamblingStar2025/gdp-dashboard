import streamlit as st

email = st.session_state.get("email")
if not email:
    st.warning("Bitte einloggen.")
    st.stop()

st.title("📊 Strategie Auswahl")
hot = st.slider("Anteil heiße Zahlen (%)", 0, 100, 50)
if st.button("💾 Strategie speichern"):
    st.success(f"Strategie mit {hot}% heiße Zahlen gespeichert (Simuliert)")
