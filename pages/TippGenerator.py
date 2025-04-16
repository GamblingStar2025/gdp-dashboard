
import streamlit as st

st.set_page_config(page_title="Tipp Generator", layout="centered")

st.title("🎰 Tipp Generator")

st.markdown("Hier kannst du deine Tipps basierend auf gespeicherten Strategien generieren.")

email = st.session_state.get("email", "Gast")

if email:
    st.success(f"✅ Eingeloggt als {email}")
    st.slider("Anzahl Tipps", 1, 20, 5)
    st.button("🎲 Tipp generieren")
else:
    st.warning("Bitte logge dich ein, um den Tipp Generator zu verwenden.")
