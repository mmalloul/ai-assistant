from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    environment: str = "development"
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
