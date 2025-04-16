
import streamlit as st
from save_strategy import save_strategy

st.set_page_config(page_title="Strategien", layout="centered")

email = st.session_state.get("email")

if not email:
    st.warning("Bitte logge dich ein, um Strategien zu speichern.")
    st.stop()

st.title("🧠 Strategien Übersicht")

def strategie_block(name, key_suffix):
    st.subheader(f"{name}")
    wert = st.slider(f"Einstellung für {name}", 0, 100, 50, key=f"slider_{key_suffix}")
    if st.button(f"💾 {name} speichern", key=f"btn_{key_suffix}"):
        res = save_strategy(email, name, {"anteil": wert})
        st.success(f"✅ {name} erfolgreich gespeichert!")

strategie_block("Heiße Zahlen", "hot")
strategie_block("Cluster", "cluster")
strategie_block("Rad-Prinzip", "rad")
strategie_block("Monaco Casino", "monaco")
strategie_block("KI-Strategie", "ki")
