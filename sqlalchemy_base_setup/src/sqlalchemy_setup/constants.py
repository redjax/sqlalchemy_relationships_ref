from __future__ import annotations

from dynaconf import settings


ENV: str = settings.ENV or "prod"
CONTAINER_ENV: str = settings.CONTAINER_ENV or False
env_str: str = f"[env:{ENV}|container:{CONTAINER_ENV}]"

LOG_LEVEL: str = settings.LOG_LEVEL
LOG_DIR: str = settings.LOG_DIR

DB_TYPE: str = settings.DB_TYPE
DB_HOST: str = settings.DB_HOST
DB_USERNAME: str = settings.DB_USERNAME
DB_PASSWORD: str = settings.DB_PASSWORD
DB_PORT: str = settings.DB_PORT
DB_DATABASE: str = settings.DB_DATABASE

CACHE_DIR: str = settings.CACHE_DIR
SERIALIZE_DIR: str = settings.SERIALIZE_DIR
DB_DIR: str = settings.DB_DIR
