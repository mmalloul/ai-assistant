import streamlit as st
from enums.MessageRole import MessageRole

def display_chat_message(role: MessageRole, content: str, history_key: str = None):
    """Displays chat messages on the page and stores them in session state if specified."""
    with st.chat_message(role.value.capitalize()):
        st.markdown(content)
    if history_key and st.session_state.get(history_key) is not None:
        st.session_state[history_key].append({'role': role.value, 'content': content})

def display_chat_history(history, history_key: str):
    """Displays the entire chat history from session state or an external source."""
    if history:
        for message in history:
            if message['role'] != MessageRole.SYSTEM.value:
                display_chat_message(MessageRole(message['role']), message['content'])

    else:
        st.session_state[history_key] = []
