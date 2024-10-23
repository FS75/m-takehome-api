from fastapi import FastAPI
from app.logging.middleware import LoggingMiddleware
from app.routers.base import router as base_router

app = FastAPI()
app.include_router(base_router, prefix="")
app.add_middleware(LoggingMiddleware)