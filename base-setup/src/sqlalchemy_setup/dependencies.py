from typing import Union
from core.database import saSQLiteConnection, saPGConnection
from core.database import get_db_connection_conf, get_engine, get_session
from dynaconf import settings

from loguru import logger as log

db_connection_conf: Union[saSQLiteConnection, saPGConnection] = get_db_connection_conf()

engine = get_engine(connection=db_connection_conf, db_type=settings.DB_TYPE, echo=True)
SessionLocal = get_session(engine=engine, autoflush=True)
