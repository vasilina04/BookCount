from functools import lru_cache
from functools import lru_cache
from typing import Optional, List, Union

from pydantic import BaseSettings, PostgresDsn, validator, AnyHttpUrl


@lru_cache()
class Settings(BaseSettings):
    # main
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    WORKERS: int = 1

    API_V1_STR: str = "/api"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    class Config:
        case_sensitive = True
        env_file = './.env'


settings = Settings()
