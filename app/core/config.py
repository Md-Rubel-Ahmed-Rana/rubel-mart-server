from pydantic_settings import BaseSettings, SettingsConfigDict




class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    APP_ENV: str

    HOST: str
    PORT: int

    FRONTEND_URL: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()

# config.py

print("APP_NAME =", settings.APP_NAME)
print("PORT =", settings.PORT)