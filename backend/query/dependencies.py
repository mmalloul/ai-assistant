from .engine import QueryEngine
from llama_index.llms.ollama import Ollama
from config.config import MODEL, TIMEOUT, SYSTEM_PROMPT

def get_llm():
    return Ollama(model=MODEL, request_timeout=TIMEOUT, system_prompt=SYSTEM_PROMPT)

query_engine = QueryEngine(get_llm())

def get_query_engine():
    return query_engine
