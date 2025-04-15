import streamlit as st

st.title("🔐 Login / Registrierung")

email = st.text_input("Email-Adresse")
password = st.text_input("Passwort", type="password")

if st.button("✅ Einloggen"):
    if email:
        st.session_state["email"] = email
        st.success(f"Erfolgreich eingeloggt als {email}")
        st.page_link("pages/MainApp.py", label="➡️ Weiter zur App")
    else:
        st.error("Bitte Email eingeben.")
