from enum import Enum
from pydantic import BaseModel

class MessageRole(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

class ChatRequest(BaseModel):
    prompt: str
