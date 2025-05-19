from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime


class Lottery(Base):
    __tablename__ = "lottery"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    max_count_ticket: Mapped[int]
    price_ticket: Mapped[int]
    time_start: Mapped[datetime] = mapped_column(DateTime)
    time_end: Mapped[datetime] = mapped_column(DateTime)