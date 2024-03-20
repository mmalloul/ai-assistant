import streamlit as st
from src.chat_engine import ChatEngine, ChatMessage
from src.config import DEFAULT_SYSTEM_PROMPT, DEFAULT_MODEL, DEFAULT_TIMEOUT

st.title("AI Assistant")

st.sidebar.title("Configuration")
model = st.sidebar.text_input("Model", value=DEFAULT_MODEL)
timeout = st.sidebar.number_input("Timeout (seconds)", min_value=30, value=DEFAULT_TIMEOUT)
system_prompt = st.sidebar.text_area("System Prompt", value=DEFAULT_SYSTEM_PROMPT, height=300)
st.sidebar.button("Clear Chat History", on_click=lambda: st.session_state['chat_engine'].clear_chat_history())

if 'chat_engine' not in st.session_state:
    st.session_state.chat_engine = ChatEngine(model=model, timeout=timeout)

if "messages" not in st.session_state:
    st.session_state.messages = [ChatMessage(role="system", content=system_prompt)]

st.session_state['chat_engine'].display_chat_history()

prompt = st.chat_input("What can I do for you?", disabled=not input)

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    response_content = st.session_state.chat_engine.chat(prompt)

    with st.chat_message("assistant"):
        st.markdown(response_content)
 