from sqlalchemy import insert, select, update

from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.vip.models import VipInfo


class VipDAO(BaseDAO):
    model = VipInfo

    @classmethod
    async def add(cls, user_id: int, lvl: int):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(user_id, lvl)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()