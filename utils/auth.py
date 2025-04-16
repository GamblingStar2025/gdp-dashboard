
import streamlit as st

def require_login():
    if "email" not in st.session_state:
        st.warning("Bitte logge dich ein, um fortzufahren.")
        st.stop()
