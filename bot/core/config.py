from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuracao central da aplicacao, carregada de variaveis de ambiente / .env."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_env: str = "development"
    log_level: str = "INFO"

    database_url: str
    redis_url: str

    whatsmiau_base_url: str
    whatsmiau_api_key: str
    whatsmiau_instance: str

    webhook_path: str = "/webhook"
    webhook_secret: str

    host: str = "0.0.0.0"
    port: int = 8000


@lru_cache
def get_settings() -> Settings:
    return Settings()
