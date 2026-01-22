"""Application configuration settings"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings from environment variables"""
    
    # Database
    DATABASE_URL: str = "postgresql://aiholdings:aiholdings@localhost:5432/aiholdings"
    TEST_DATABASE_URL: str = "postgresql://aiholdings:aiholdings@localhost:5432/aiholdings_test"
    
    # JWT
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Application
    APP_NAME: str = "AI Holdings Enterprise Management System"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
