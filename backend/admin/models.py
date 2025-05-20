from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class AdminInfo(Base):
    __tablename__ = "admin_info"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    price_ticket: Mapped[int] = mapped_column(default=100)
    minutes: Mapped[int] = mapped_column(default=15)
    price_mini_games: Mapped[int]