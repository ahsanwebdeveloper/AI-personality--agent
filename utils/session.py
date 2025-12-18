 # Session state initialization
 
import streamlit as st
from utils.chat_storage import load_file

def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = load_file()


