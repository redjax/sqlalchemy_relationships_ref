from __future__ import annotations

import sys

## Appends the src/ dir at ../ to Python's path
#  Allows accessing files in i.e. ../.serialize
sys.path.append(".")

import stackprinter

stackprinter.set_excepthook()

from constants import CONTAINER_ENV, ENV, env_str
from dynaconf import settings

from red_utils.loguru_utils import init_logger, sinks
from loguru import logger as log

from core.database import create_base_metadata
from dependencies import engine, SessionLocal, db_connection_conf

from core.database import Base

init_logger(sinks=[sinks.default_app_log_file_sink, sinks.default_stdout_color_sink])

create_base_metadata(Base(), engine=engine)

if __name__ == "__main__":
    pass
