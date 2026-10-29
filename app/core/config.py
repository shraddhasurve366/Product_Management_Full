from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Product Management API"
    environment: str = "development"
    database_url: str = "postgresql+psycopg://product_user:product_management@localhost:5435/product_management_full"
    redis_url: str = "redis://localhost:6380/0"
    secret_key: str = "change-this-secret-key-before-deployment"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
