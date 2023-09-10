from __future__ import annotations

from dynaconf import settings

ENV: str = settings.ENV or "prod"
CONTAINER_ENV: str = settings.CONTAINER_ENV or False
env_str: str = f"[env:{ENV}|container:{CONTAINER_ENV}]"