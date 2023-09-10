from typing import Union
from core.database import saSQLiteConnection, saPGConnection

from sqlalchemy.orm import Session

from dynaconf import settings

from loguru import logger as log


def get_db_connection_conf(
    db_type: str = settings.DB_TYPE,
) -> Union[saSQLiteConnection, saPGConnection]:
    """Create a connection object for use by SQLAlchemy.

    Determines which connection model from core/database/connection_models.py
    to return, and configures it from the environment.
    """

    if not db_type:
        raise ValueError("Missing value for db_type.")

    match db_type:
        case "sqlite":
            log.debug(f"Detected SQLite DB")
            db_config = saSQLiteConnection(database=settings.DB_DATABASE)
        case "postgres":
            log.debug(f"Detected Postgres DB")
            db_config = saPGConnection(
                host=settings.DB_HOST,
                username=settings.DB_USERNAME,
                password=settings.DB_PASSWORD,
                database=settings.DB_DATABASE,
            )
        case _:
            raise Exception(f"Unknown DB_TYPE: {db_type}")

    return db_config


def get_db_dependency(session: Session = None):
    """Yield a database session.

    Use this function for applications like FastAPI or an asynchronous script.
    For all other uses, use get_db().
    """
    if not session:
        raise ValueError("Missing a SQLAlchemy Session object")

    db: Session = session()

    try:
        yield db
    except Exception as exc:
        raise Exception(f"Unhandled exception getting database session. Details: {exc}")

    finally:
        db.close()
