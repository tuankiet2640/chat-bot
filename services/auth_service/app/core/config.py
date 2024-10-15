from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY = str
    ALGORITHM = str
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    USE_LDAP = bool

    class Config:
        env_file = ".env"

settings = Settings()