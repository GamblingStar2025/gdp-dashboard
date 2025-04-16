import streamlit as st

st.set_page_config(page_title="Strategien", layout="centered")

st.title("📊 Strategie Auswahl")

# Auswahl Heiße Zahlen
hot = st.slider("Anteil heiße Zahlen (%)", 0, 100, 50)

# Auswahl Kalte Zahlen
cold = st.slider("Anteil kalte Zahlen (%)", 0, 100, 30)

# Cluster Level
cluster_level = st.slider("Cluster-Level", 1, 5, 3)

# Monaco Casino Durchmischung
monaco_mix = st.slider("Monaco Casino Durchmischung (max. 500000)", 10000, 500000, 200000, step=1000)

# KI Intensität
ki_intensity = st.slider("KI-Strategie Intensität", 0, 300, 120)

if st.button("💾 Strategie speichern"):
    st.success("Strategien gespeichert (Simuliert)")
    st.page_link("pages/TippGenerator.py", label="➡️ Weiter zum Tipp Generator")

