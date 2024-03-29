import os
import streamlit as st
from typing import List, Generator
from llama_index.core import Settings
from llama_index.core.llms import ChatMessage
from llama_index.llms.ollama import Ollama
from src.db_operations import initialize_database, load_and_index_documents

from src.config import MODEL, TIMEOUT, DATA_DIRECTORY, SYSTEM_PROMPT

class ChatEngine:
    def __init__(self, model: str = MODEL, timeout: int = TIMEOUT, system_prompt: str = SYSTEM_PROMPT):
        Settings.embed_model = "local"
        self.llm = Ollama(model=model, request_timeout=timeout)
        Settings.llm = self.llm

        self.system_prompt = system_prompt
        self.chat_history: List[ChatMessage] = [ChatMessage(role="system", content=self.system_prompt)]
        self.index = self.init_index()

    def init_index(self):
        if os.path.exists(DATA_DIRECTORY) and os.listdir(DATA_DIRECTORY):
            storage_context = initialize_database()
            return load_and_index_documents(storage_context)
        else:
            return None

    def chat(self, message: str) -> Generator[str, None, None]:    
        try:
            with st.spinner("Analyzing..."):
                if self.index:
                    response = self.index.as_chat_engine().stream_chat(message=message, chat_history=self.chat_history)
                    stream = response.response_gen
                else:
                    response = self.llm.stream_chat(messages=self.chat_history)
    
                    return self.stream_response(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")

        return stream

    def append_to_chat_history(self, role: str, content: str) -> None:
        self.chat_history.append(ChatMessage(role=role, content=content))

    def display_chat_history(self) -> None:
        for message in self.chat_history:
            if message.role != "system":
                with st.chat_message(message.role):
                    st.markdown(message.content)

    def clear_chat_history(self) -> None:
        self.chat_history = [ChatMessage(role="system", content=self.system_prompt)]
        st.success("Chat history cleared.")

    def stream_response(self, response):
        for r in response:
            yield r.delta
