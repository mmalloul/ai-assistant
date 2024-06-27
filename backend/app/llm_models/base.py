from abc import ABC, abstractmethod

class LLMModel(ABC):
    @abstractmethod
    def analyze(self, text: str):
        pass

    @abstractmethod
    def review_code(self, prompts: list):
        pass

class ChatModel(ABC):
    @abstractmethod
    def chat(self, messages: list):
        pass
