from typing import Union

import sqlalchemy as sa
import sqlalchemy.orm as sa_orm

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base

from domain.address import AddressModel
from domain.user import UserModel

import uuid


class UserAddressAssociation(Base):
    __tablename__ = "user_address_tbl"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), primary_key=True)
    address_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("address.id"), primary_key=True
    )

    extra_data: Mapped[str | None] = mapped_column(sa.String, nullable=True)

    addresses: Mapped[list["AddressModel"]] = relationship(back_populates="addresses")
