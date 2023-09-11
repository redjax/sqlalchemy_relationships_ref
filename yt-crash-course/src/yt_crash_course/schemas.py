from pydantic import BaseModel, Field, validator, ValidationError
from typing import Union, List

import uuid

from models import User, Comment


class UserSchemaBase(BaseModel):
    username: str = Field(default=None)
    email: str = Field(default=None)


class DBUserSchemaBase(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)

    comments: List["CommentSchemaCreate"] | None = None

    class Meta:
        orm_model = User

    class Config:
        from_attributes = True


class UserSchemaCreate(DBUserSchemaBase):
    comments: List["CommentSchemaCreate"] | None = None


class UserSchemaUpdate(DBUserSchemaBase):
    id: uuid.UUID | None = Field(default=None)
    username: str | None = Field(default=None)
    email: str | None = Field(default=None)


class UserSchemaOut(DBUserSchemaBase):
    comments: List["CommentSchemaOut"] | None = None


class UserSchema(UserSchemaBase):
    pass


class CommentSchemaBase(BaseModel):
    text: str = Field(default=None)


class DBCommentSchemaBase(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)

    class Meta:
        orm_model = Comment

    class Config:
        from_attributes = True


class CommentSchemaCreate(DBCommentSchemaBase):
    pass


class CommentSchemaUpdate(DBCommentSchemaBase):
    id: uuid.UUID | None = Field(default=None)
    text: str | None = Field(default=None)


class CommentSchema(CommentSchemaBase):
    pass


class CommentSchemaOut(DBCommentSchemaBase):
    id: uuid.UUID
