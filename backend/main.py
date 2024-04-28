import uvicorn
from fastapi import FastAPI
from chat.routes import router as chat_router
from query.routes import router as query_router

app = FastAPI()

app.include_router(chat_router, tags=["Chat"])
app.include_router(query_router, tags=["Query"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
