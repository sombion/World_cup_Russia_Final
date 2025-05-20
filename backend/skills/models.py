from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database import Base

class Skills(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    drop_rate_gt_3: Mapped[int]
    no_die_spend_chance: Mapped[int]
    double_money_drop_chance: Mapped[int]
    ruby_drop_chance: Mapped[int]
    afk_dice: Mapped[int]
    dice_per_hour: Mapped[int]