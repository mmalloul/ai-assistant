import streamlit as st
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from config import DEFAULT_MODEL, DEFAULT_TIMEOUT, DEFAULT_SYSTEM_PROMPT

st.title("AI Assistant")

# Sidebar for configuration options
st.sidebar.title("Configuration")
model = st.sidebar.text_input("Model", value=DEFAULT_MODEL)
timeout = st.sidebar.number_input("Timeout (seconds)", min_value=1, value=DEFAULT_TIMEOUT)
system_prompt = st.sidebar.text_area("System Prompt", value=DEFAULT_SYSTEM_PROMPT, height=200)

# Initialize Ollama with user-specified configurations
llm = Ollama(model=model, request_timeout=timeout)

# System prompt
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(ChatMessage(role="system", content=system_prompt))

# Display chat history
for message in st.session_state.messages:
    if message.role == "system":
        continue
    with st.chat_message(message.role):
        st.markdown(message.content)

# Input field for user prompt
if prompt := st.chat_input("What can I do for you?", disabled=not input):
    st.session_state.messages.append(ChatMessage(role="user", content=prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Analyzing..."):
        response = llm.chat(
            model=model,
            messages=st.session_state.messages
        )
        content = response.message.content
    st.markdown(content)
    st.session_state.messages.append(ChatMessage(role="assistant", content=content))
