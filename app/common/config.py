from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REPO_ID: str
    MODEL_FILENAME: str
    DEBUG: bool

    class Config:
        env_file = ".env"


settings = Settings()
