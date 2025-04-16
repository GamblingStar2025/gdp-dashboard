
import streamlit as st

st.title("Admin CSV Upload")

email = st.session_state.get("email", "")
if email == "newspoolestate@gmail.com":
    uploaded_file = st.file_uploader("CSV-Datei hochladen", type=["csv"])
    if uploaded_file is not None:
        st.success("Datei erfolgreich hochgeladen!")
else:
    st.warning("Zugriff nur für Admin erlaubt.")
