from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    class Config: # c in config must be capital
        env_file = ".env"

def get_settings():
    return Settings()
