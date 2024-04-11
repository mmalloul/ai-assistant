from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn
from enum import Enum
from typing import List
from src.chat_engine import ChatEngine
from llama_index.core.llms import ChatMessage, ChatResponse, ChatResponseAsyncGen
from fastapi.responses import StreamingResponse

app = FastAPI()
chat_engine = ChatEngine()

class MessageRole(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

class ChatRequest(BaseModel):
    prompt: str

from typing import Iterator

async def async_wrapper(sync_gen):
    for item in sync_gen:
        yield item

@app.post("/chat/")
async def chat(request: ChatRequest):
    sync_generator: Iterator[ChatResponse] = chat_engine.chat(request.prompt)
    
    return StreamingResponse(sync_generator, media_type="application/json")


@app.get("/chat_history/")
async def chat():
    response = chat_engine.get_chat_history()
    return response

@app.post("/clear_chat/")
async def clear_chat():
    try:
        chat_engine.clear_chat_history()
        return {"message": "Chat history cleared successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
