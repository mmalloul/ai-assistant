import os

from llama_index.core import PromptTemplate
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core.response_synthesizers import ResponseMode, get_response_synthesizer

from src.config import DATA_DIRECTORY, MODEL, TIMEOUT
from src.db_operations import initialize_database, load_and_index_documents


class QueryEngine():
    def __init__(self):
        self.llm = Ollama(model=MODEL, request_timeout=TIMEOUT)
        Settings.embed_model = "local"
        Settings.llm = self.llm
        self.index = self.init_index()
        
    def init_index(self):
        if os.path.exists(DATA_DIRECTORY) and os.listdir(DATA_DIRECTORY):
            storage_context = initialize_database()
            return load_and_index_documents(storage_context)
        return None
    
    def query(self, query_str: str):
        if self.index is None:
            raise ValueError("Index not initialized.")
        response = self.index.as_query_engine().query(query_str)
        return response
