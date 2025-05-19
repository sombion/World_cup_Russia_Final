from backend.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey
from datetime import datetime


class Arcade(Base):
    __tablename__ = "arcade"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name_arcade: Mapped[str]
    id_user: Mapped[int] = mapped_column(ForeignKey("profile.id"))
    win: Mapped[int]
    lose: Mapped[int]
    target_number: Mapped[int] = mapped_column(nullable=True)
    current_number: Mapped[int] = mapped_column(nullable=True)
    current_cube: Mapped[int] = mapped_column(nullable=True)
    status: Mapped[str]


class InfoArcade(Base):
    __tablename__ = "info_arcade"

    id: Mapped[int] = mapped_column(primary_key=True)
    title_name: Mapped[str]
    time_start: Mapped[datetime]
    time_end: Mapped[datetime]
    price: Mapped[int]
    url: Mapped[str]
    img: Mapped[str]