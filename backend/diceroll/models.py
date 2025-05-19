from backend.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


class InfoDicePoll(Base):
    __tablename__ = "info_dice_roll"

    id: Mapped[int] = mapped_column(primary_key=True)
    lvl_dice_roll: Mapped[int]
    xp: Mapped[int]
    money: Mapped[int]
    ruby: Mapped[int]
    cube: Mapped[int]