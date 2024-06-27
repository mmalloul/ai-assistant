from langchain_aws.chat_models import ChatBedrock
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.prompts import PromptTemplate
from app.llm_models.base import LLMModel, ChatModel
from app.models.issues import ListOfIssues
from app.core.logging import get_logger

logger = get_logger(__name__)

class BedrockModel(LLMModel, ChatModel):
    def __init__(self):
        self.model = ChatBedrock(model_id="meta.llama3-70b-instruct-v1:0")

    def analyze(self, text: str):
        try:
            response = self.model.invoke(text)
            return response
        except Exception as e:
            logger.error(f"Error analyzing text: {e}")
            raise

    def review_code(self, prompts: list):
        parser = JsonOutputParser(pydantic_object=ListOfIssues)

        prompt = PromptTemplate(
            template="Answer the user query.\n{format_instructions}\n{code}\n",
            input_variables=["code"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        sequence = prompt | self.model | parser

        try:
            response = sequence.invoke({"code": prompts})
            return response
        except Exception as e:
            logger.error(f"Error reviewing code: {e}")
            raise

    def chat(self, chat_history: list):
        messages = []
        logger.info(f"Chat history: {chat_history}")
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
