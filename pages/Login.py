
import streamlit as st

st.set_page_config(page_title="Login", layout="centered")
st.title("🔐 Login")

email = st.text_input("E-Mail")
if st.button("Login"):
    st.session_state["email"] = email
    st.success("Erfolgreich eingeloggt")
