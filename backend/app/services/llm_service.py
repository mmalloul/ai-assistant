from app.llm_models.base import LLMModel
from app.core.logging import get_logger

logger = get_logger(__name__)

class LLMService:
    def __init__(self, llm_model: LLMModel):
        self.llm_model = llm_model

    def execute_analysis(self, prompts: list, code_review: bool):
        logger.info("Executing analysis")
        if code_review:
            try:
                result = self.llm_model.review_code(prompts)
    
                return result
            except Exception as e:
                logger.error(f"Error during code review: {e}")
                raise
        try:
            result = self.llm_model.analyze(prompts)
            return result
        except Exception as e:
            logger.error(f"Error during text analysis: {e}")
            raise
