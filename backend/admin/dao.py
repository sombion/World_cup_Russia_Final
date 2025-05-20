from sqlalchemy import delete, insert, select, update
from backend.dao.base import BaseDAO
from backend.database import async_session_maker
from backend.admin.models import AdminInfo

class AdminInfoDAO(BaseDAO):
    model = AdminInfo

    @classmethod
    async def add(cls, price_ticket: int, minutes: int, price_mini_games: int) -> AdminInfo:
        async with async_session_maker() as session:
            stmt = (
                insert(cls.model)
                .values(price_ticket=price_ticket, minutes=minutes, price_mini_games=price_mini_games)
                .returning(cls.model)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()

    @classmethod
    async def update(cls, id: int, price_ticket: int, minutes: int, price_mini_games: int) -> AdminInfo:
        async with async_session_maker() as session:
            stmt = (
                update(cls.model)
                .values(price_ticket=price_ticket, minutes=minutes, price_mini_games=price_mini_games)
                .returning(cls.model)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()