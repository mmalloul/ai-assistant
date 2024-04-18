import requests
import streamlit as st
from enum import Enum
import time
from llama_index.core.llms import ChatMessage, ChatResponse

class MessageRole(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

def fetch_chat_history():
    response = requests.get("http://localhost:8080/chat_history/")
    if response.status_code == 200:
        return response.json().get("history", [])
    else:
        st.error("Failed to load chat history.")
        return []
    
if "chat_history" not in st.session_state:
    st.session_state.chat_history = fetch_chat_history()
    
def update_chat_history(): 
    st.session_state.chat_history = fetch_chat_history()
    
def clear_chat_history():
    requests.post("http://localhost:8080/clear_chat/")
    st.session_state.chat_history = []


st.title("AI Assistant")
st.sidebar.title("Settings")
st.sidebar.button("Clear Chat History", on_click=clear_chat_history)


for message in st.session_state.chat_history:
    update_chat_history()
    if message['role'] != "system":
        with st.chat_message(message['role']):
            st.markdown(message['content'])


def display_chat_message(role: str, content: str):
    if role != MessageRole.SYSTEM.value:
        with st.chat_message(role):
            st.markdown(content)

prompt = st.chat_input("What can I do for you?", disabled=not input)

if prompt:
        display_chat_message(MessageRole.USER.value, prompt)
        with st.spinner("Analyzing your request..."):
            start_time = time.time()
            try:
                response = requests.post("http://localhost:8080/chat/", json={"prompt": prompt})
                response.raise_for_status()
                chat_response = response.json()
                end_time = time.time()
                elapsed_time = end_time - start_time
                st.success(f"Response received in {elapsed_time:.2f} seconds.")
                display_chat_message(MessageRole.ASSISTANT.value, chat_response['message']['content'])
            except Exception as e:
                st.error(f"An error occurred: {e}")
                print(f"An error occurred: {e}")