from datetime import datetime
from backend.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey


class ShopItem(Base):
    __tablename__ = "shop_item"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title_item: Mapped[str]
    name_item_ru: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    count: Mapped[int]
    chance: Mapped[int]


class BuyShopItem(Base):
    __tablename__ = "buy_shop_item"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("profile.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("shop_item.id"))
    count_by: Mapped[int]
    time_buy: Mapped[datetime] = mapped_column(DateTime, default=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
