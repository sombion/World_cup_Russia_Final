from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class Vip(Base):
    __tablename__ = "vip"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    lvl: Mapped[int]


class VipInfo(Base):
    __tablename__ = "vip_info"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lvl: Mapped[int]
    description: Mapped[str]
    price: Mapped[int]