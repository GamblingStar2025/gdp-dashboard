import streamlit as st

st.set_page_config(page_title="EuroGenius Deluxe", layout="centered")

st.markdown("## 🎉 Willkommen bei **EuroGenius Deluxe!**")
st.markdown("Statistische Power, KI-Strategien und dein Bauchgefühl in einer App.")
st.markdown("💎 **Wähle deinen Stil** – spiele wie ein Profi und knacke den Jackpot!")

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("🔓 Als Gast starten"):
        st.switch_page("pages/MainApp.py")

with col2:
    if st.button("🔑 Einloggen / Registrieren"):
        st.switch_page("pages/Login.py")
