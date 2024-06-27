from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from app.llm_models.base import LLMModel, ChatModel
from app.models.issues import ListOfIssues
from app.core.logging import get_logger

logger = get_logger(__name__)

class OllamaModel(LLMModel, ChatModel):
    def __init__(self):
        self.model = ChatOllama(model="llama3")

    def analyze(self, text: str):
        try:
            response = self.model.invoke(text)
            return response
        except Exception as e:
            logger.error(f"Error analyzing text: {e}")
            raise

    def review_code(self, code: str):
        parser = JsonOutputParser(pydantic_object=ListOfIssues)

        prompt = PromptTemplate(
            template="Answer the user query.\n{format_instructions}\n{code}\n",
            input_variables=["code"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        chain = prompt | self.model | parser

        try:
            response = chain.invoke({"code": code})
            return response
        except Exception as e:
            logger.error(f"Error reviewing code: {e}")
            raise

    def chat(self, chat_history: list):
        messages = []
        if chat_history:
            for message in chat_history:
                if message['role'] == 'user':
                    messages.append(HumanMessage(content=message['content']))
                elif message['role'] == 'ai':
                    messages.append(AIMessage(content=message['content']))
                elif message['role'] == 'system':
                    messages.append(SystemMessage(content=message['content']))  
            
        try:
            response = self.model.invoke(messages)

            return response.content
        except Exception as e:
            logger.error(f"Error during chat: {e}")
            raise
