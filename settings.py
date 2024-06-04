from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")
    DATABASE_URL: str
    API_KEY: str
    API_KEY_NAME: str
    HOST: str
    PORT: int


app_settings = Settings()
