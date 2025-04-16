import streamlit as st

email = st.session_state.get("email")
if not email:
    st.warning("Bitte einloggen.")
    st.stop()

st.title("🎰 Tipp Generator")
st.markdown("Hier kannst du deine Tipps basierend auf deiner Strategie generieren.")
st.button("🌀 Tipps generieren")
st.page_link("pages/TippGenerator.py", label="➡️ Weiter zum Tipp Generator")
