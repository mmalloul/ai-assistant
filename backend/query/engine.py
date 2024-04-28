import os
from llama_index.core import Settings
from dotenv import load_dotenv
load_dotenv('../../.env')

from .database import initialize_database, load_and_index_documents

class QueryEngine:
    def __init__(self, llm):
        if not os.environ.get("OPENAI_API_KEY"):
            Settings.embed_model = "local"
        self.storage_context = initialize_database()
        self.index = load_and_index_documents(self.storage_context) if self.storage_context else None
        self.llm = llm
        Settings.llm = self.llm
        
    def query(self, query_str: str):
        if not self.index:
            raise ValueError("Index not initialized. Please check the logs for more information.")
        response = self.index.as_query_engine().query(query_str)
        return response
