# utils/config.py
from typing import List, Optional
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False

    # DATABASE_URI: str = "postgresql://shreenathkadam@127.0.0.1:5432/ishara"

    ALLOWED_ORIGINS: str = "" 

    GEMINI_API_KEY: str = "AIzaSyDQxXj5c5B_WqVbDCa5HlmGs29FCslgaP0"

    @field_validator("ALLOWED_ORIGINS")
    @classmethod
    def parse_origins(cls, v: str) -> List[str]:
        return [origin.strip() for origin in v.split(",") if origin.strip()] if v else []

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore" 
    )

settings = Settings() 