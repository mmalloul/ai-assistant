import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List

from llama_index.core import Settings
from llama_index.llms.ollama import Ollama

from src.chat_engine import ChatEngine 
from src.query_engine import QueryEngine
from src.config import MODEL, TIMEOUT

app = FastAPI()
llm = Ollama(model=MODEL, request_timeout=TIMEOUT)

Settings.embed_model = "local"
Settings.llm = llm
        
chat_engine = ChatEngine(llm)
# query_engine = QueryEngine()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat/")
async def chat(request: ChatRequest):
    try:
        response = chat_engine.chat(prompt=request.prompt)
        print(f"Chat response: {response.message.content}")
        json_compatible_item_data = jsonable_encoder(response)
        return JSONResponse(content=json_compatible_item_data)
    except Exception as e:
        print(f"An internal error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")

@app.post("/query/")
async def chat(request: ChatRequest):
    try:
        print(f"Query request: {request.prompt}")
        response = llm.complete(request.prompt)
        json_compatible_item_data = jsonable_encoder(response)
        return JSONResponse(content=json_compatible_item_data)
    except Exception as e:
        print(f"An internal error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {str(e)}")
    

@app.get("/chat_history/")
async def get_chat_history():
    history = chat_engine.get_chat_history()
    return {"history": history}

@app.post("/clear_chat/")
async def clear_chat():
    chat_engine.clear_chat_history()
    return {"message": "Chat history cleared successfully."}

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8080, reload=True)

