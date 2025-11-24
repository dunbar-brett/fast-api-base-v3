# External Dependencies
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Use pydantic-settings' modern configuration so `.env` is loaded
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Default value kept for convenience; value from `.env` (or environment) will override it.
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/todo"


settings = Settings()
