from fastapi import FastAPI, Depends
from app.logging.middleware import LoggingMiddleware
from app.routers.base import router as base_router
from app.services.object_processing import get_object_processing_service

app = FastAPI()
app.include_router(base_router, prefix="", dependencies=[Depends(get_object_processing_service)])
app.add_middleware(LoggingMiddleware)
