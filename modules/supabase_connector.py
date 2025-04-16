
import streamlit as st
from st_supabase_connection import SupabaseConnection

@st.cache_resource
def get_authenticated_client():
    conn = st.connection("supabase", type=SupabaseConnection)
    return conn
