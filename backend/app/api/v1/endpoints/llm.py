from fastapi import APIRouter, Depends, HTTPException, status
from app.services.llm_service import LLMService
from app.services.chat_service import ChatService
from app.llm_models.openai_model import OpenAIModel
from app.llm_models.ollama_model import OllamaModel
from app.llm_models.bedrock_model import BedrockModel
from app.models.requests import QueryRequest, ChatRequest
from app.core.logging import get_logger

router = APIRouter()
logger = get_logger(__name__)

def get_llm_service(engine):
    return LLMService(engine)

def get_chat_service(engine):
    return ChatService(engine)

@router.post("/analyze/openai")
def analyze_openai(request: QueryRequest, service: LLMService = Depends(lambda: get_llm_service(OpenAIModel()))):
    logger.info("OpenAI analysis requested")
    try:
        result = service.execute_analysis(request.prompts, request.code_review)
        logger.info("OpenAI analysis successful")
        return result
    except Exception as e:
        logger.error(f"Error analyzing with OpenAI: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/chat/openai")
def chat_openai(request: ChatRequest, service: ChatService = Depends(lambda: get_chat_service(OpenAIModel()))):
    logger.info("OpenAI chat requested")
    try:
        response = service.execute_chat(request.chat_history)
        logger.info("OpenAI chat successful")
        return {"response": response}
    except Exception as e:
        logger.error(f"Error during OpenAI chat: {e}")
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/analyze/ollama")
def analyze_ollama(request: QueryRequest, service: LLMService = Depends(lambda: get_llm_service(OllamaModel()))):
    logger.info("Ollama analysis requested")
    try:
        result = service.execute_analysis(request.prompts, request.code_review)
        logger.info("Ollama analysis successful")
        return result
    except Exception as e:
        logger.error(f"Error analyzing with Ollama: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/chat/ollama")
def chat_ollama(request: ChatRequest, service: ChatService = Depends(lambda: get_chat_service(OllamaModel()))):
    logger.info("Ollama chat requested")
    try:
        response = service.execute_chat(request.chat_history)
        logger.info("Ollama chat successful")
        return {"response": response}
    except Exception as e:
        logger.error(f"Error during Ollama chat: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/analyze/bedrock")
def analyze_bedrock(request: QueryRequest, service: LLMService = Depends(lambda: get_llm_service(BedrockModel()))):
    logger.info("Bedrock analysis requested")
    try:
        result = service.execute_analysis(request.prompts, request.code_review)
        logger.info("Bedrock analysis successful")
        return result
    except Exception as e:
        logger.error(f"Error analyzing with Bedrock: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/chat/bedrock")
def chat_bedrock(request: ChatRequest, service: ChatService = Depends(lambda: get_chat_service(BedrockModel()))):
    logger.info("Bedrock chat requested")
    try:
        response = service.execute_chat(request.chat_history)
        logger.info("Bedrock chat successful")
        return {"response": response}
    except Exception as e:
        logger.error(f"Error during Bedrock chat: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")