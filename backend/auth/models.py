from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str]
    login: Mapped[str]
    hash_password: Mapped[str]
    is_admin: Mapped[bool]