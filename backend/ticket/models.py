from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class Ticket(Base):
    __tablename__ = "ticket"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    numbder: Mapped[int]
    lottery_id: Mapped[int] = mapped_column(ForeignKey("lottery.id"))
    users_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True, default=None)
    is_win: Mapped[bool] = mapped_column(default=False)
    is_trade: Mapped[bool] = mapped_column(default=False)