import uvicorn
from fastapi import FastAPI
from app.api.v1.endpoints import llm
from app.core.logging import get_logger
from app.core.config import settings
from contextlib import asynccontextmanager

logger = get_logger(__name__)

# Initialize the FastAPI application
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    logger.info(f"Running in {settings.environment} environment")
    yield
    logger.info("Application shutdown")

app = FastAPI(lifespan=lifespan)

app.include_router(llm.router, prefix="/api/v1", tags=["llm"])

if __name__ == "__main__":
    logger.info(f"Starting application in {settings.environment} environment")
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=settings.environment == "development")
    logger.info("Application stopped")
