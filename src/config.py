from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_user: str
    db_pass: str
    db_name: str
    db_host: str
    db_port: int

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
