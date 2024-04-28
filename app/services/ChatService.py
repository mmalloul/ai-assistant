import requests
import streamlit as st

from config.config import BACKEND_URL

class ChatService:
        
    def fetch_chat_history(self):
        try:
            response = requests.get(f"{BACKEND_URL}/chat_history/")
            response.raise_for_status()
            return response.json().get("history", [])
        except requests.RequestException as e:
            st.error(f"Failed to load chat history: {e}")
            return []

    def clear_chat_history(self):
        try:
            response = requests.post(f"{BACKEND_URL}/clear_chat/")
            response.raise_for_status()
            st.success("Chat history cleared successfully.")
        except requests.RequestException as e:
            st.error(f"Failed to clear chat history: {e}")

    def send_chat_message(self, prompt):
        try:
            response = requests.post(f"{BACKEND_URL}/chat/", json={"prompt": prompt})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            st.error(f"Failed to send message: {e}")
            return None
