from typing import List
from enum import Enum
from llama_index.core.llms import ChatMessage, ChatResponse

from src.config import SYSTEM_PROMPT

class MessageRole(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

class ChatEngine:
    def __init__(self, llm, system_prompt: str = SYSTEM_PROMPT):
        self.llm = llm
        self.system_prompt = system_prompt
        self.chat_history: List[ChatMessage] = [ChatMessage(role=MessageRole.SYSTEM.value, content=self.system_prompt)]

    def chat(self, prompt: str) -> ChatResponse:
        self.append_to_chat_history(role=MessageRole.USER.value, content=prompt)
        try:
            response = self.llm.chat(messages=self.chat_history)
            self.append_to_chat_history(role=MessageRole.ASSISTANT.value, content=response.message.content)
            return response
        except Exception as e:
            print(f"Failed to process chat message: {str(e)}")  
            raise ValueError("Failed to process the chat message.")
        
            
    def append_to_chat_history(self, role: str, content: str) -> None:
        self.chat_history.append(ChatMessage(role=role, content=content))

    def clear_chat_history(self) -> None:
        self.chat_history = [ChatMessage(role=MessageRole.SYSTEM.value, content=self.system_prompt)]

    def get_chat_history(self) -> List[ChatMessage]:
        return self.chat_history
