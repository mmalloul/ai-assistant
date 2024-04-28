from .engine import ChatEngine
from llama_index.llms.ollama import Ollama
from config.config import MODEL, TIMEOUT, SYSTEM_PROMPT

def get_llm():
    return Ollama(model=MODEL, request_timeout=TIMEOUT, system_prompt=SYSTEM_PROMPT)

chat_engine = ChatEngine(llm=get_llm())

def get_chat_engine():
    return chat_engine
