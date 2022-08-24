"""_summary_"""
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:123456@localhost:5432/postgres"
    DBBaseModel = declarative_base()

    """
    Gerar JWT_SECRET
    import secrets
    secrets.token_urlsafe(32)
    """
    JWT_SECRET: str = '14OB6_mfiAJ_m543FZxjzwLwgZNDs4ACredxOuAQoP8'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings = Settings()
