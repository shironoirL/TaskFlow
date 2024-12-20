from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", ".env"
    )
)


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    class Config:
        env_file = None


settings = Settings()
print(settings)
