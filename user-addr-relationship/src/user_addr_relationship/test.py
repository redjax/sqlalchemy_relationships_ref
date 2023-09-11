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

from domain.user import UserModel
from domain.address import AddressModel
from domain.tables.user_address import UserAddressAssociation

init_logger(sinks=[sinks.default_app_log_file_sink, sinks.default_stdout_color_sink])

create_base_metadata(Base(), engine=engine)

if __name__ == "__main__":
    ## Test creating users
    spongebob = UserModel(
        first_name="spongebob",
        last_name="squarepants",
        addresses=[AddressModel(email_address="spongebob@sqlalchemy.org")],
    )

    sandy = UserModel(
        first_name="sandy",
        last_name="cheeks",
        addresses=[
            AddressModel(email_address="sandy@sqlalchemy.org"),
            AddressModel(email_address="sandy@squirrelpower.org"),
        ],
    )

    patrick = UserModel(first_name="patrick", last_name="star")

    with SessionLocal() as sess:
        sess.add_all(spongebob, sandy, patrick)
        sess.commit()
        sess.refresh(spongebob)
        sess.refresh(sandy)
        sess.refresh(patrick)
