import requests
import streamlit as st

from config.config import BACKEND_URL

class CodeReviewService:
    def send_code_review(self, code, model_type):
        try:
            response = requests.post(f"{BACKEND_URL}/analyze/{model_type}", json={"prompts": [code], "code_review": True})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            st.error(f"Failed to send code for review: {e}")
            return None