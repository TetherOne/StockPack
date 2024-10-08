from pydantic import PostgresDsn, BaseModel
from pydantic_settings import SettingsConfigDict
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("./src/infrastructure/settings/envs/app.env",),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="PORTFOLIO__",
        arbitrary_types_allowed=True,
    )
    db: DatabaseConfig


settings = Settings()
