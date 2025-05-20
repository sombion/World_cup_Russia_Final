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
        max_count_ticket: int,
        count_ticket_win: int,
        price_ticket: int,
        time_start: datetime,
        time_end: datetime,
    ):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(
                title=title,
                description=description,
                max_count_ticket=max_count_ticket,
                count_ticket_win=count_ticket_win,
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
    async def all_future(cls, date_now: datetime):
        async with async_session_maker() as session:
            query = (
                select(
                    cls.model.id,
                    cls.model.title,
                    cls.model.description,
                    cls.model.price_ticket,
                    cls.model.accumulation,
                    cls.model.time_start,
                    cls.model.time_end,
                    func.count(Ticket.users_id)
                )
                .join(Ticket, cls.model.id == Ticket.lottery_id)
                .where(date_now < cls.model.time_end)
                .group_by(
                    cls.model.id,
                    cls.model.title,
                    cls.model.description,
                    cls.model.price_ticket,
                    cls.model.accumulation,
                    cls.model.time_start,
                    cls.model.time_end,
                )
            )
            result = await session.execute(query)
            return result.mappings().all()