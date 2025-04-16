import streamlit as st
from modules.supabase_connector import get_authenticated_client
from utils.auth import require_login

st.set_page_config(page_title="Strategien", layout="centered")

email = require_login()
supabase = get_authenticated_client()

st.title("🎯 Strategien festlegen")

def save_strategy(name, parameter):
    data = {
        "email": email,
        "strategy_name": name,
        "parameters": parameter
    }
    supabase.table("strategien").insert(data).execute()

# 1. Heiße Zahlen
with st.expander("🔥 Heiße Zahlen"):
    hot = st.slider("Anteil heiße Zahlen (%)", 0, 100, 60)
    if st.button("💾 Speichern: Heiße Zahlen"):
        save_strategy("Heiße Zahlen", {"anteil": hot})
        st.success("Gespeichert.")

# 2. Kalte Zahlen
with st.expander("❄️ Kalte Zahlen"):
    cold = st.slider("Anteil kalte Zahlen (%)", 0, 100, 40)
    if st.button("💾 Speichern: Kalte Zahlen"):
        save_strategy("Kalte Zahlen", {"anteil": cold})
        st.success("Gespeichert.")

# 3. Cluster-Methode
with st.expander("🔢 Cluster-Methode"):
    cluster_stärke = st.slider("Cluster-Stärke", 0, 100, 50)
    if st.button("💾 Speichern: Cluster"):
        save_strategy("Cluster", {"stärke": cluster_stärke})
        st.success("Gespeichert.")

# 4. Monaco Casino Prinzip
with st.expander("🎲 Monaco-Casino Prinzip"):
    risiko = st.slider("Risiko-Level", 0, 100, 70)
    if st.button("💾 Speichern: Monaco"):
        save_strategy("Monaco", {"risiko": risiko})
        st.success("Gespeichert.")

# 5. Rad-Prinzip
with st.expander("🌀 Rad-Prinzip"):
    abdeckung = st.slider("Rad-Abdeckung", 0, 100, 80)
    if st.button("💾 Speichern: Rad-Prinzip"):
        save_strategy("Rad-Prinzip", {"abdeckung": abdeckung})
        st.success("Gespeichert.")

# 6. KI-Strategie
with st.expander("🤖 KI-Strategie"):
    ki_power = st.slider("KI-Intensität", 0, 100, 90)
    if st.button("💾 Speichern: KI"):
        save_strategy("KI", {"intensität": ki_power})
        st.success("Gespeichert.")

# Navigation
st.page_link("pages/TippGenerator.py", label="➡️ Weiter zum Tipp Generator")
st.page_link("pages/Home.py", label="⬅️ Zurück zur Startseite")
