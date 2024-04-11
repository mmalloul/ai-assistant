import requests
import streamlit as st
from typing import List
from llama_index.core.llms import ChatMessage

st.title("AI Assistant")
st.sidebar.title("Settings")
st.sidebar.button("Clear Chat History", on_click=lambda: requests.post("http://localhost:8080/clear_chat/"))

if "chat_history" not in st.session_state: 
    chat_history = requests.get("http://localhost:8080/chat_history/").json()
    print(chat_history)
    st.session_state.chat_history = chat_history
    print(st.session_state.chat_history)

for message in st.session_state.chat_history:
    print(message['role'], message['content'])
    if message['role'] != "system":
        with st.chat_message(message['role']):
            st.markdown(message['content'])

def update_chat_history(): 
    st.session_state.chat_history = requests.get("http://localhost:8080/chat_history/").json()
    
def clear_chat_history():
    requests.post("http://localhost:8080/clear_chat/")
    st.session_state.chat_history = []
    
# Chat input
prompt = st.chat_input("What can I do for you?", disabled=not input)

if prompt:
    response = requests.post("http://localhost:8080/chat/", json={"prompt": prompt})
    if response.status_code == 200:
        st.write_stream(response.json)
        update_chat_history()
    else:
        st.error("Failed to get response from the backend.")
        
        