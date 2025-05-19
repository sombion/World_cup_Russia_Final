from sqlalchemy import insert, select, update

from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.info.models import InfoXP


class InfoXPDAO(BaseDAO):
    model = InfoXP

    @classmethod
    async def find_target_xp(cls, lvl: int):
        async with async_session_maker() as session:
            lvl+=1
            query = select(cls.model.__table__.columns).filter_by(lvl=lvl)
            result = await session.execute(query)
            return result.mappings().all()