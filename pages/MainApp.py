import streamlit as st

email = st.session_state.get("email")
if not email:
    st.warning("Bitte logge dich zuerst ein.")
    st.stop()

st.title("🎯 EuroGenius Hauptbereich")
st.markdown(f"✅ Eingeloggt als **{email}**")

st.page_link("pages/Strategie.py", label="📊 Strategie wählen")
st.page_link("pages/TippGenerator.py", label="🎰 Tipp Generator")
