from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class Ticket(Base):
    __tablename__ = "ticket"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number: Mapped[int]
    lottery_id: Mapped[int] = mapped_column(ForeignKey("lottery.id"))
    count_win: Mapped[int] = mapped_column(nullable=True)
    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True, default=None)
    time_buy: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    is_win: Mapped[bool] = mapped_column(nullable=True, default=None)
    is_trade: Mapped[bool] = mapped_column(default=False)