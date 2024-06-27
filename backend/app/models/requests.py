from pydantic import BaseModel

class QueryRequest(BaseModel):
    prompts: list
    code_review: bool = False
    
class ChatRequest(BaseModel):
    chat_history: list
