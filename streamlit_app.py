import streamlit as st
from core.personalities import PERSONALITIES
from core.enforcement import is_in_scope
from core.llm import generate_response
from utils.session import init_session
from utils.chat_storage import save_file


st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 Ahsan Ali Personality AI Chatbot")

personality = st.radio(
    "Choose a chatbot personality:",
    list(PERSONALITIES.keys())
)
init_session()


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Ask your question...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    st.chat_message("user").write(user_input)

    selected = PERSONALITIES[personality]

    if not is_in_scope(user_input, selected["scope"]):
        response = (
            f"Sorry, I can only answer questions related to "
            f"{selected['scope']}."
        )
    else:
        response = generate_response(
            selected["system_prompt"],
            user_input
        )

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    st.chat_message("assistant").write(response)
    save_file(st.session_state.messages)
