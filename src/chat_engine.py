import os
import streamlit as st
from typing import List
from llama_index.core import Settings, VectorStoreIndex
from llama_index.core.llms import ChatMessage
from llama_index.llms.ollama import Ollama
from src.db_operations import initialize_database, load_and_index_documents

from src.config import MODEL, TIMEOUT, SYSTEM_PROMPT, DATA_DIRECTORY

class ChatEngine:
    def __init__(self, model: str = MODEL, timeout: int = TIMEOUT):
        Settings.embed_model = "local"
        self.llm = Ollama(model=model, request_timeout=timeout)
        Settings.llm = self.llm
        
        self.chat_history: List[ChatMessage] = [ChatMessage(role="system", content=SYSTEM_PROMPT)]
        self.index = self.init_index()

    def init_index(self):
        if os.path.exists(DATA_DIRECTORY) and os.listdir(DATA_DIRECTORY):
            storage_context = initialize_database()
            return load_and_index_documents(storage_context)
        else:
            return None

    def chat(self, message: str) -> str:
        self.append_to_chat_history("user", message)
        
        content = "Unable to process your request."
        
        try:
            with st.spinner("Analyzing..."):
                if self.index:
                    response = self.index.as_chat_engine().chat(message=message, chat_history=self.chat_history)
                    content = response.response if hasattr(response, 'response') else content
                else:
                    response = self.llm.chat(messages=self.chat_history)
                    content = getattr(response.message, 'content', content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
        
        self.append_to_chat_history("assistant", content)
        return content

    def append_to_chat_history(self, role: str, content: str) -> None:
        self.chat_history.append(ChatMessage(role=role, content=content))

    def display_chat_history(self) -> None:
        for message in self.chat_history:
            if message.role != "system":
                with st.chat_message(message.role):
                    st.markdown(message.content)

    def clear_chat_history(self) -> None:
        self.chat_history = [ChatMessage(role="system", content=SYSTEM_PROMPT)]
        st.success("Chat history cleared.")
