from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Database
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    # JWT
    JWT_SECRET: str
    JWT_TTL: int = 3600
    JWT_REFRESH_TTL: int = 604800

    # Mail
    MAIL_HOST: str
    MAIL_PORT: int
    MAIL_ENCRYPTION: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM_ADDRESS: str
    MAIL_FROM_NAME: str
    MAIL_DEFAULT_TO: str

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignorar variables extra en el .env


@lru_cache()
def get_settings():
    return Settings()
