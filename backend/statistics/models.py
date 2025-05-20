from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class Statistics(Base):
    __tablename__ = "statistics"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    xp: Mapped[int]
    lvl: Mapped[int]
    cube: Mapped[int]
    ruby: Mapped[int]
    money: Mapped[int]