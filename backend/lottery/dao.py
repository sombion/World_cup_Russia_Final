from datetime import datetime
from backend.dao.base import BaseDAO
from backend.lottery.models import Lottery
from backend.database import async_session_maker
from sqlalchemy import func, insert, select, update

from backend.ticket.models import Ticket


class LotteryDAO(BaseDAO):
    model = Lottery

    @classmethod
    async def add(
        cls,
        title: str,
        description: str,
        price_ticket: int,
        time_start: datetime,
        time_end: datetime,
    ):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(
                title=title,
                description=description,
                price_ticket=price_ticket,
                time_start=time_start,
                time_end=time_end,
            ).returning(cls.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()

    @classmethod
    async def all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add_accumulation(cls, id: int):
        async with async_session_maker() as session:
            stmt = (
                update(cls.model)
                .where(cls.model.id==id)
                .values(accumulation=cls.model.accumulation+cls.model.price_ticket*0.6)
                .returning(cls.model))
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()

    @classmethod
    async def count_win(cls):
        async with async_session_maker() as session:
            query = (
                select(func.count(Ticket.users_id))
                .select_from(cls.model)
                .join(Ticket, Ticket.lottery_id==cls.model.id)
                .where(Ticket.is_win==True)
            )
            result = await session.execute(query)
            return result.scalar()

    @classmethod
    async def all_future(cls):
        async with async_session_maker() as session:
            query = (select(cls.model.__table__.columns).where(cls.model.time_end > datetime.utcnow()))
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def list_end_lottery(cls, time_now):
        async with async_session_maker() as session:
            query = select(Lottery).where(
                Lottery.time_end < time_now,
                Lottery.win_time.is_(None)
            )
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def update_win_time(cls, id: int, win_time):
        async with async_session_maker() as session:
            stmt = update(cls.model).where(cls.model.id==id).values(win_time=win_time)
            await session.execute(stmt)
            await session.commit()