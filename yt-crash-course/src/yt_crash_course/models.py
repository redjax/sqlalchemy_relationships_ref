from core.database import Base, CompatibleUUID

from typing import List
import uuid

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "user"

    type_annotation_map = {uuid.UUID: CompatibleUUID}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, insert_default=uuid.uuid4)

    username: Mapped[str] = mapped_column(sa.String, nullable=False)
    email: Mapped[str | None] = mapped_column(sa.String, nullable=True)

    ## One-to-many relationship
    #  Use the typing.List type, instead of list
    #  The relationship accesses a Comment.user attribute.
    #  Access comments with User.comments
    comments: Mapped[List["Comment"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        """Print pre-defined string representation."""
        return f"<User id={self.id!r} username={self.username!r} comments={self.comments!r}"


class Comment(Base):
    __tablename__ = "comment"

    type_annotation_map = {uuid.UUID: CompatibleUUID}

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, insert_default=uuid.uuid4)

    text: Mapped[str] = mapped_column(sa.Text, nullable=False)

    ## Define ForeignKey lookup value. user_id will
    #  map a relationship on a User.id attribute
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    ## Back-fill the User class found by user_id ForeignKey above
    #  Accessing User.comments will back-fill the User.comments attribute
    #  with the value of a Comment instance.
    #  Access a Comment's user attribute with Comment.user
    user: Mapped["User"] = relationship(back_populates="comments")

    def __repr__(self):
        """Print pre-defined string representation."""
        return f"<Comment id={self.id!r} text={self.text!r}"
