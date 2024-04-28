import logging
from llama_index.core.llms import ChatMessage, ChatResponse
from .enums import MessageRole
from config.config import SYSTEM_PROMPT

logger = logging.getLogger(__name__)

class ChatEngine:
    def __init__(self, llm):
        self.llm = llm
        self.chat_history = [ChatMessage(role=MessageRole.SYSTEM.value, content=SYSTEM_PROMPT)]

    def chat(self, prompt: str) -> ChatResponse:
        self.append_to_chat_history(role=MessageRole.USER.value, content=prompt)
        try:
            response = self.llm.chat(messages=self.chat_history)
            self.append_to_chat_history(role=MessageRole.ASSISTANT.value, content=response.message.content)
            return response
        except Exception as e:
            logger.error(f"Failed to process chat message: {str(e)}", exc_info=True)
            raise ValueError("Failed to process the chat message.")

    def append_to_chat_history(self, role: MessageRole, content: str):
        self.chat_history.append(ChatMessage(role=role, content=content))

    def clear_chat_history(self):
        self.chat_history = []

    def get_chat_history(self):
        return self.chat_history
