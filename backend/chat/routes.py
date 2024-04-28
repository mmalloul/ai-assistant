from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from .enums import ChatRequest
from .dependencies import get_chat_engine
from .engine import ChatEngine

router = APIRouter()

@router.post("/chat/")
async def chat(chat_request: ChatRequest, chat_engine: ChatEngine = Depends(get_chat_engine)):
    try:
        response = chat_engine.chat(chat_request.prompt)
        return JSONResponse(content={"message": response.message.content})
    except Exception as e:
        print(f"Failed to process chat message: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/chat_history/")
async def get_chat_history(chat_engine = Depends(get_chat_engine)):
    history = [{"role": msg.role, "content": msg.content} for msg in chat_engine.get_chat_history()]
    return JSONResponse(content={"history": history})

@router.post("/clear_chat/")
async def clear_chat(chat_engine = Depends(get_chat_engine)):
    chat_engine.clear_chat_history()
    return JSONResponse(content={"message": "Chat history cleared successfully."})
