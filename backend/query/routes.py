from fastapi import APIRouter, HTTPException, Depends
from .engine import QueryEngine
from .enums import QueryRequest
from .dependencies import get_query_engine

router = APIRouter()

@router.post("/query/")
async def perform_query(request: QueryRequest,  query_engine: QueryEngine = Depends(get_query_engine)):
    try:
        response = query_engine.query(request.prompt)
        return {"message": response.response}
    except Exception as e:
        print(f"Failed to process query: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
