from typing import Optional

import sqlalchemy as sa
from sqlalchemy import ForeignKey
import sqlalchemy.orm as sa_orm
from sqlalchemy.orm import Mapped, mapped_column, relationship

import uuid

from core.database import Base, CompatibleUUID


class UserModel(Base):
    __tablename__ = "user"

    type_annotation_map = {uuid.UUID: CompatibleUUID}

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, index=True, insert_default=uuid.uuid4
    )
    first_name: Mapped[str] = mapped_column(sa.String(30))
    last_name: Mapped[str | None] = mapped_column(sa.String, nullable=True)
