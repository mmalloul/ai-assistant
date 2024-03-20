import streamlit as st
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage
from src.db_operations import initialize_database, load_and_index_documents
from src.config import DEFAULT_MODEL, DEFAULT_TIMEOUT, DEFAULT_SYSTEM_PROMPT

class ChatEngine:
    def __init__(self, model=DEFAULT_MODEL, timeout=DEFAULT_TIMEOUT):
        self.llm = Ollama(model=model, request_timeout=timeout)
        self.storage_context = initialize_database()
        self.index = load_and_index_documents(self.storage_context)
        self.chat_history = [ChatMessage(role="system", content=DEFAULT_SYSTEM_PROMPT)]
        
        Settings.llm = self.llm
        Settings.embed_model = "local"

    def chat(self, message):
        self.append_to_chat_history("user", message)
        
        with st.spinner("Analyzing..."):
            try:
                if self.index:
                    response = self.index.as_chat_engine().chat(message=message, chat_history=self.chat_history)
                    content = response.response
                else:
                    response = self.llm.chat(messages=self.chat_history)
                    content = response.message.content
            except Exception as e:
                content = f"An error occurred: {str(e)}"

        self.append_to_chat_history("assistant", content)

        return content

        
    def display_chat_history(self):
        for message in self.chat_history:
            if message.role != "system":
                with st.chat_message(message.role):
                    st.markdown(message.content)

    def append_to_chat_history(self, role, content):
        self.chat_history.append(ChatMessage(role=role, content=content))

    def clear_chat_history(self):
        self.chat_history = [ChatMessage(role="system", content=DEFAULT_SYSTEM_PROMPT)]
        st.success("Chat history cleared")

