from typing import Optional

import sqlalchemy as sa
from sqlalchemy import ForeignKey
import sqlalchemy.orm as sa_orm
from sqlalchemy.orm import Mapped, mapped_column, relationship

import uuid

from core.database import Base, CompatibleUUID


class AddressModel(Base):
    __tablename__ = "address"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, index=True, insert_default=uuid.uuid4
    )
    email_address: Mapped[str] = mapped_column(sa.String)
