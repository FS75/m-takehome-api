import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger("logger")
file_handler = logging.FileHandler("requests.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log request details
        logger.info(f"Request: {request.method} {request.url} - Headers: {request.headers} - Body: {await request.body()}")
        response = await call_next(request)
        # Log response status
        logger.info(f"Response status: {response.status_code}")
        return response
