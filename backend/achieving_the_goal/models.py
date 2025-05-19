from backend.database import Base
from sqlalchemy.orm import mapped_column, Mapped


class InfoAchievingTheGoal(Base):
    __tablename__ = "info_achieving_the_goal"

    id: Mapped[int] = mapped_column(primary_key=True)
    lvl: Mapped[int]
    xp: Mapped[int]
    money: Mapped[int]
    ruby: Mapped[int]
    cube: Mapped[int]