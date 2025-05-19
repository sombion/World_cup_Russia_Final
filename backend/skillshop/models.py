from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base

class ShopSkillsInfo(Base):
    __tablename__ = "shop_skills_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    skill_lvl: Mapped[int]
    skill_name: Mapped[str]
    ru_skill_name: Mapped[str]
    skill_value: Mapped[int]
    ruby_price: Mapped[int]