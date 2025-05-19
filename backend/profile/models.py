from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base


class Profile(Base):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    statistics_id: Mapped[int] = mapped_column(ForeignKey("statistics.id"))
    skills_id: Mapped[int] = mapped_column(ForeignKey("skills.id"))
    time_now: Mapped[datetime] = mapped_column(DateTime, default=datetime.now().replace(second=0, microsecond=0))