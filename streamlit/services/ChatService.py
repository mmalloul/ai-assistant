import requests
import streamlit as st

from config.config import BACKEND_URL

class ChatService:
    def send_chat_message(self, chat_history, model_type):
        try:
            response = requests.post(f"{BACKEND_URL}/chat/{model_type}", json={"chat_history": chat_history})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            st.error(f"Failed to send message: {e}")
            return None