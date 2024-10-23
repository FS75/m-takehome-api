import uvicorn

from app.settings import settings

if __name__ == "__main__":
    uvicorn.run("app:app", host=settings.settings.APP_HOST , port=settings.settings.APP_PORT, reload=True)