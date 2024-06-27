from app.llm_models.base import ChatModel
from app.core.logging import get_logger

logger = get_logger(__name__)

class ChatService:
    def __init__(self, chat_model: ChatModel):
        self.chat_model = chat_model

    def execute_chat(self, chat_history: list):
        logger.info("Executing chat")
        try:
            result = self.chat_model.chat(chat_history)
            return result
        except Exception as e:
            logger.error(f"Error during chat: {e}")
            raise
