import requests
import streamlit as st

from config.config import BACKEND_URL

class QueryService:
    def send_query(self, query):
        try:
            response = requests.post(f"{BACKEND_URL}/query/", json={"prompt": query})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            st.error(f"Failed to send query: {e}")
            return None
