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
from models import User, Comment
from schemas import UserSchema, UserSchemaCreate, CommentSchema, CommentSchemaCreate

init_logger(sinks=[sinks.default_app_log_file_sink, sinks.default_stdout_color_sink])

# create_base_metadata(Base(), engine=engine)
log.info("Creating tables")
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    user1_dict: dict = {
        "username": "john",
        "email": "jonathan@sqlalchemy.org",
        "comments": [dict(text="Hello world"), dict(text="This is another comment")],
    }
    user1: UserSchemaCreate = UserSchemaCreate.model_validate(user1_dict)
    log.debug(f"User1 schema: {user1}")

    ## Dump user without comments. These are created separately
    db_user1: User = User(**user1.model_dump(exclude=["comments"]))
    db_user1_comments: list[Comment] = []

    for comment in user1.comments:
        comment_dict = comment.model_dump()
        db_comment: Comment = Comment(**comment_dict)
        db_comment.user = db_user1
        # log.debug(f"DB Comment ({type(db_comment)}): {db_comment}")
        db_user1_comments.append(db_comment)

    db_user1.comments = db_user1_comments
    log.debug(f"User1 for database: {db_user1.__repr__()}")

    with SessionLocal() as sess:
        sess.add(db_user1)

        sess.commit()

    # ## Define users
    # user1: User = User(
    #     username="john",
    #     email="jonathan@sqlalchemy.org",
    #     comments=[Comment(text="Hello world"), Comment(text="This is another comment")],
    # )

    # paul: User = User(
    #     username="paul",
    #     email="paul@sqlalchemy.org",
    #     comments=[
    #         Comment(text="What's up?"),
    #         Comment(text="I also made a second comment!"),
    #     ],
    # )

    # cathy: User = User(username="cathy", email="cathy@sqlalchemy.org")

    # insert_users: list[User] = [user1, paul, cathy]

    # with SessionLocal() as sess:
    #     sess.add_all(insert_users)
    #     sess.commit()
