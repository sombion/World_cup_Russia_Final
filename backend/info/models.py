from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class InfoXP(Base):
    __tablename__ = "info_xp"

    id: Mapped[int] = mapped_column(primary_key=True)
    lvl: Mapped[int]
    need_to: Mapped[int]