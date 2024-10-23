import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_HOST: str = os.getenv("APP_HOST")
    APP_PORT: int = int(os.getenv("APP_PORT"))


settings = Settings()