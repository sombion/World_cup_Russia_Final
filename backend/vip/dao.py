from sqlalchemy import insert, select, update

from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.vip.models import Vip


class VipDAO(BaseDAO):
    model = Vip

    @classmethod
    async def add(cls, user_id: int, lvl: int):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(user_id=user_id, lvl=lvl).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()

    @classmethod
    async def update(cls, user_id: int, lvl: int):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(cls.model.user_id == user_id).values(lvl=lvl)
            await session.execute(stmt)
            await session.commit()